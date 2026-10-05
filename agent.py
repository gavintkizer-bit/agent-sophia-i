"""
my-first-agent: a small, file-based Claude agent built on the Claude Agent SDK.

Usage:
  python agent.py --check              # checks setup (no API cost)
  python agent.py                      # runs tasks/first_task.md
  python agent.py tasks/other_task.md  # runs any other task file

Settings (optional environment variables):
  AGENT_API_KEY       your Claude Console API key. NOT needed in claude.ai/code cloud
                      sessions (the agent uses the session's own connection there).
                      ANTHROPIC_API_KEY also works outside cloud sessions.
  AGENT_MODEL         default: claude-haiku-4-5 (cheapest; good for testing)
  AGENT_MAX_TURNS     default: 12 (safety cap on how many steps the agent takes)
"""

import argparse
import asyncio
import datetime
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
WORKSPACE = ROOT / "workspace"
LOG_FILE = ROOT / "logs" / "run_log.md"
DEFAULT_TASK = ROOT / "tasks" / "first_task.md"

# Inside a claude.ai/code cloud session, the SDK uses the session's own Claude
# connection, so no API key is needed (and any key you set is ignored there).
# Elsewhere you need a key. Cloud sessions don't pass a variable named
# ANTHROPIC_API_KEY through, so AGENT_API_KEY is accepted too.
IN_CLOUD_SESSION = bool(os.environ.get("CLAUDE_CODE_REMOTE"))
API_KEY = (os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("AGENT_API_KEY") or "").strip()
if API_KEY:
    os.environ["ANTHROPIC_API_KEY"] = API_KEY

MODEL = os.environ.get("AGENT_MODEL", "claude-haiku-4-5")
MAX_TURNS = int(os.environ.get("AGENT_MAX_TURNS", "12"))

# The agent's "personality and rules". Edit this to change how it behaves.
SYSTEM_PROMPT = """You are a careful, organized assistant that works with files.

Rules:
- Work only inside your current working directory (the workspace folder).
- Before writing anything, look for and read existing files related to the task.
- Save your final deliverable as a Markdown file using the exact filename the task asks for.
- Do not invent facts that are not in the files; mark any assumption clearly.
- Finish with a short summary: what you did, which files you created or changed,
  and one specific idea that would make the next run better.
"""


# ---------------------------------------------------------------- setup check
def check_setup() -> bool:
    """Verify Python, the SDK, the API key, and network access. Costs nothing."""
    ok = True
    print("== Setup check ==")

    if sys.version_info < (3, 10):
        print(f"[FAIL] Python {sys.version.split()[0]} found; 3.10+ is required.")
        ok = False
    else:
        print(f"[ OK ] Python {sys.version.split()[0]}")

    try:
        import claude_agent_sdk  # noqa: F401
        version = getattr(claude_agent_sdk, "__version__", "unknown version")
        print(f"[ OK ] claude-agent-sdk installed ({version})")
    except ImportError:
        print("[FAIL] claude-agent-sdk not installed. Run: pip install -r requirements.txt")
        ok = False

    # AGENT_ENV_TEST=hello is a harmless test variable: it tells us whether ANY of
    # your environment variables are reaching this session.
    if os.environ.get("AGENT_ENV_TEST"):
        print("[ OK ] AGENT_ENV_TEST found: your environment variables are reaching this session")
    else:
        print("[info] AGENT_ENV_TEST not found: either you didn't add it, or your environment")
        print("       variables aren't reaching this session (wrong environment, not saved,")
        print("       or this session was started before you saved).")

    key = API_KEY
    if IN_CLOUD_SESSION:
        print("[ OK ] Running in a claude.ai/code cloud session: no API key needed.")
        print("       The agent uses this session's own Claude connection.")
        print("== Result: READY ==")
        return ok
    if not key:
        print("[FAIL] No API key found. In the cloud environment's Environment variables add:")
        print("       AGENT_API_KEY=sk-ant-...   (use this name, NOT ANTHROPIC_API_KEY)")
        print("       then start a NEW session.")
        return False
    if not key.startswith("sk-ant-"):
        print("[FAIL] The key doesn't start with sk-ant-. Check for quotes, spaces, or a")
        print("       variable name pasted into the value.")
        return False
    print("[ OK ] API key is set (value hidden)")

    # Listing models is free, so it safely tests both the key and the network.
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/models",
        headers={"x-api-key": key, "anthropic-version": "2023-06-01"},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode())
            count = len(data.get("data", []))
            print(f"[ OK ] Reached api.anthropic.com; key accepted ({count} models visible)")
    except urllib.error.HTTPError as e:
        deny = e.headers.get("x-deny-reason", "")
        if e.code == 401:
            print("[FAIL] The API key was rejected (401). Re-copy it from the Claude Console.")
        elif e.code == 403 and deny:
            print(f"[FAIL] Network blocked api.anthropic.com ({deny}).")
            print("       Fix: edit the cloud environment -> Network access -> Custom,")
            print("       keep the default package-manager list, and add: api.anthropic.com")
        else:
            print(f"[FAIL] API returned HTTP {e.code}: {e.reason}")
        ok = False
    except Exception as e:  # network errors, timeouts, proxy problems
        print(f"[FAIL] Could not reach api.anthropic.com: {e}")
        ok = False

    print("== Result:", "READY" if ok else "NOT READY", "==")
    return ok


# ---------------------------------------------------------------- agent run
async def run_agent(task_text: str):
    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ResultMessage,
        TextBlock,
        ToolUseBlock,
        query,
    )

    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        allowed_tools=["Read", "Write", "Edit", "Glob", "Grep"],
        disallowed_tools=["Bash"],          # no shell access for this first agent
        permission_mode="acceptEdits",      # may edit files in the workspace without asking
        cwd=str(WORKSPACE),
        max_turns=MAX_TURNS,
        model=MODEL,
    )

    tools_used: list[str] = []
    result = None
    async for message in query(prompt=task_text, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
                elif isinstance(block, ToolUseBlock):
                    print(f"   [tool] {block.name}")
                    tools_used.append(block.name)
        elif isinstance(message, ResultMessage):
            result = message
    return result, tools_used


# ---------------------------------------------------------------- run log
def append_log(task_path: pathlib.Path, result, tools_used, seconds: float, error: str = ""):
    """Add one entry per run so you can compare runs and improve over time."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        LOG_FILE.write_text("# Run log\n\nOne entry per agent run, newest at the bottom.\n")

    cost = getattr(result, "total_cost_usd", None) if result else None
    turns = getattr(result, "num_turns", None) if result else None
    failed = bool(error) or (result is not None and getattr(result, "is_error", False))
    status = "FAILED" if failed else "OK"

    entry = [
        f"\n## {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} | {task_path.name} | {status}",
        f"- Model: {MODEL} | Turns: {turns if turns is not None else 'n/a'} | "
        f"Time: {seconds:.0f}s | Cost: {f'${cost:.4f}' if cost is not None else 'n/a'}",
        f"- Tools used: {', '.join(sorted(set(tools_used))) or 'none'}",
    ]
    if error:
        entry.append(f"- Error: {error}")
    entry.append("- What I'll change next time: _(fill this in after reviewing the output)_")
    with LOG_FILE.open("a") as f:
        f.write("\n".join(entry) + "\n")


# ---------------------------------------------------------------- main
def main():
    parser = argparse.ArgumentParser(description="Run my first Claude agent.")
    parser.add_argument("task", nargs="?", default=str(DEFAULT_TASK), help="path to a task .md file")
    parser.add_argument("--check", action="store_true", help="check setup only (no API cost)")
    args = parser.parse_args()

    if args.check:
        sys.exit(0 if check_setup() else 1)

    task_path = pathlib.Path(args.task).resolve()
    if not task_path.exists():
        sys.exit(f"Task file not found: {task_path}")
    if not API_KEY and not IN_CLOUD_SESSION:
        sys.exit("No API key found. Run `python agent.py --check` for help.")

    WORKSPACE.mkdir(exist_ok=True)
    print(f"== Running {task_path.name} with {MODEL} (max {MAX_TURNS} turns) ==\n")
    start = time.time()
    try:
        result, tools_used = asyncio.run(run_agent(task_path.read_text()))
    except Exception as e:
        append_log(task_path, None, [], time.time() - start, error=str(e)[:300])
        raise
    append_log(task_path, result, tools_used, time.time() - start)

    cost = getattr(result, "total_cost_usd", None) if result else None
    print("\n== Done ==")
    if cost is not None:
        print(f"Cost of this run: ${cost:.4f}")
    print(f"Logged to {LOG_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
