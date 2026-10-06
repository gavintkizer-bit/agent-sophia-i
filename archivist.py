"""
Callimachus: the crew's archivist and auditor (he/him; named by Sophia at the owner's request).
She researches on the web, files sourced notes, catalogs the record and audits Sophia's memory.
His constitution, personality and rules live in agents/archivist.md, loaded as his instructions.

Usage:
  python archivist.py research "topic"   # sourced research note in workspace/archive/research/
  python archivist.py audit              # checks Sophia's memory against the record
  python archivist.py index              # rebuilds workspace/archive/INDEX.md
  python archivist.py code-audit         # free: code-only checks (missing paths, memory size)

He proposes memory changes in workspace/archive/for_sophia.md; Sophia decides what goes in.
Settings: AGENT_MODEL and AGENT_THINKING as for Hypatia (agent.py), plus
  ARCHIVIST_MAX_TURNS (default 30) and ARCHIVIST_MAX_BUDGET (default 0.50 US dollars).
"""

import argparse
import asyncio
import datetime
import html
import ipaddress
import os
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

import agent

NAME = "Callimachus"
ROOT = agent.ROOT
WORKSPACE = agent.WORKSPACE
ARCHIVE = WORKSPACE / "archive"
PROFILE = ROOT / "agents" / "archivist.md"
MAX_TURNS = int(os.environ.get("ARCHIVIST_MAX_TURNS", "30"))
MAX_BUDGET = float(os.environ.get("ARCHIVIST_MAX_BUDGET", "0.50"))
USER_AGENT = "SophiaArchivist/1.0 (personal research agent)"

SYSTEM_PROMPT = PROFILE.read_text() + f"""

## Working context
- Your working directory is the repo root. Write only under `workspace/archive/` (or the folder
  a drill gives you). Use relative paths, never `..` or absolute paths.
- Today is {datetime.date.today().isoformat()}.
"""


# ---------------------------------------------------------------- fences
SECRET_PARTS = {".env", ".git", "API_KEY", ".venv"}


def _resolve(path_str: str) -> pathlib.Path:
    path = pathlib.Path(path_str)
    return (path if path.is_absolute() else ROOT / path).resolve()


def write_problem(path_str: str) -> str:
    """Why he may not write here, or "" if it's fine. Drills narrow it to their scratch folder."""
    if not path_str:
        return "No file path given."
    path = _resolve(path_str)
    allowed = agent.WRITE_ROOT or ARCHIVE.resolve()
    if not path.is_relative_to(allowed):
        return (f"{path_str} is outside {allowed.relative_to(ROOT)}/. You only write there; "
                f"suggest other changes in workspace/archive/for_sophia.md instead.")
    return ""


def append_problem(tool: str, args: dict) -> str:
    """for_sophia.md is append-only: his first run rewrote it and dropped earlier proposals."""
    path = _resolve(args.get("file_path", ""))
    if path != (ARCHIVE / "for_sophia.md").resolve() or not path.exists():
        return ""
    old = path.read_text()
    if tool == "Write" and not args.get("content", "").startswith(old.rstrip()):
        return "for_sophia.md is append-only: keep everything already in it and add at the bottom."
    if tool == "Edit" and args.get("old_string", "") not in args.get("new_string", ""):
        return "for_sophia.md is append-only: an edit may add text but never remove or change any."
    return ""


def read_problem(path_str: str) -> str:
    """Reading is allowed anywhere in the repo except secrets and git internals."""
    if not path_str:
        return ""
    path = _resolve(path_str)
    if not path.is_relative_to(ROOT):
        return f"{path_str} is outside the repo."
    if SECRET_PARTS & set(path.relative_to(ROOT).parts):
        return f"{path_str} may hold secrets or git internals; it's off limits."
    return ""


def url_problem(url: str) -> str:
    """Block URLs that could leak data or reach private machines."""
    try:
        p = urllib.parse.urlsplit(url)
    except ValueError:
        return "That isn't a valid URL."
    host = p.hostname or ""
    if p.scheme not in ("http", "https") or not host:
        return "Only ordinary http(s) web pages are allowed."
    if p.username or p.password:
        return "URLs with logins in them aren't allowed."
    if host == "localhost" or host.endswith((".local", ".internal")):
        return "Private hosts aren't allowed."
    try:
        if not ipaddress.ip_address(host).is_global:
            return "Private addresses aren't allowed."
    except ValueError:
        pass                                   # a normal hostname
    if len(p.query) > 200 or len(url) > 600:
        return "That URL carries too much data in it. Use a plain page address."
    return ""


async def fence_hook(input_data, tool_use_id, context):
    """Runs before every tool use and blocks anything outside his rules."""
    name = input_data.get("tool_name", "")
    args = input_data.get("tool_input", {})
    if name in ("Write", "Edit"):
        problem = write_problem(args.get("file_path", "")) or append_problem(name, args)
    elif name in ("Read", "Glob", "Grep"):
        problem = read_problem(args.get("file_path") or args.get("path") or "")
    elif name in ("WebFetch", "mcp__archive__verify_quote"):
        problem = url_problem(args.get("url", ""))
    else:
        problem = ""
    if problem:
        print(f"   [fence] blocked {name}: {problem}")
        agent.FENCE_BLOCKS.append(problem)
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                       "permissionDecision": "deny",
                                       "permissionDecisionReason": problem}}
    return {}


# ---------------------------------------------------------------- verify_quote
# Every URL with a quote that passed this run. His first research note (2026-10-06) labeled
# facts "verified" that no check had confirmed, so code now audits the labels after each run.
VERIFIED_URLS: set[str] = set()
URL_RE = re.compile(r"https?://[^\s)\]>,]+")


def _url_key(url: str) -> str:
    return url.split("#")[0].rstrip("/.").lower()


def label_problem(paths: list[pathlib.Path], since: float, before: dict | None = None) -> str:
    """Lines written this run that call a URL "verified" with no passed quote from it.
    `before` holds each file's text at the start, so only what he added is checked (not Sophia's lines)."""
    bad = []
    for path in paths:
        if not path.exists() or path.stat().st_mtime < since:
            continue
        old_lines = set((before or {}).get(path, "").splitlines())
        # only lines that are new this run, wherever he put them (he may insert mid-file)
        for line in (l for l in path.read_text().splitlines() if l not in old_lines):
            urls = list(URL_RE.finditer(line))
            for i, m in enumerate(urls):      # each URL's label is the text after it, up to the next URL
                label = line[m.end(): urls[i + 1].start() if i + 1 < len(urls) else len(line)]
                if re.search(r"(?<!un)verified", label, re.I) and not re.search(r"\bnot verified", label, re.I) \
                        and _url_key(m.group()) not in VERIFIED_URLS:
                    bad.append(m.group())
    if not bad:
        return ""
    return ("These sources are labeled verified, but no quote from them passed verify_quote this "
            f"run: {', '.join(sorted(set(bad))[:5])}. Verify a quote from each, or relabel those "
            "facts unverified, in every file you wrote.")


def _plain(text: str) -> str:
    """Lowercase text with tags, entities, fancy quotes and extra spaces removed."""
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", text)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = text.translate(str.maketrans({"‘": "'", "’": "'", "“": '"',
                                         "”": '"', "–": "-", "—": "-", "\xa0": " "}))
    return " ".join(text.split()).lower()


def verify_quote(url: str, quote: str) -> str:
    """Fetch the page and check the quote is really on it. Code decides, not the model."""
    problem = url_problem(url)
    if problem:
        raise ValueError(problem)
    if len(_plain(quote)) < 15:
        raise ValueError("Quote too short to verify; use at least a few words.")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            page = resp.read(3_000_000).decode(resp.headers.get_content_charset() or "utf-8", "replace")
    except Exception as e:  # network errors, 403s, timeouts
        raise ValueError(f"Couldn't fetch the page ({e}). Treat the quote as unverified.")
    if _plain(quote) in _plain(page):
        VERIFIED_URLS.add(_url_key(url))
        return "FOUND: the quote is on the page. You may file it as verified."
    return "NOT FOUND: the quote is not on the page as written. Don't file it as a quote."


def archive_server():
    """verify_quote and Hypatia's calculator, packaged for the Agent SDK."""
    from claude_agent_sdk import create_sdk_mcp_server, tool

    @tool("verify_quote", "Check that an exact quote appears on a web page. Use before filing ANY "
          "quote. Example: url='https://example.com', quote='This domain is for use in'",
          {"url": str, "quote": str})
    async def verify_tool(args):
        try:
            return {"content": [{"type": "text", "text": verify_quote(args["url"], args["quote"])}]}
        except ValueError as e:
            return {"content": [{"type": "text", "text": f"Error: {e}"}], "is_error": True}

    @tool("calculate", "Exact arithmetic. Use for every sum instead of working it out yourself.",
          {"expression": str})
    async def calc_tool(args):
        try:
            return {"content": [{"type": "text", "text": agent.calculate(args["expression"])}]}
        except (ValueError, SyntaxError, ArithmeticError) as e:
            return {"content": [{"type": "text", "text": f"Error: {e}"}], "is_error": True}

    return create_sdk_mcp_server(name="archive", tools=[verify_tool, calc_tool])


# ---------------------------------------------------------------- free code checks
RECORD_DIRS = ["agents", "logs", "tasks", "training", "workspace"]
SKIP = {"_drill", "inbox", "out", "__pycache__", "plans"}


def file_list() -> str:
    """Every record file with size and date, so the model doesn't spend turns listing folders."""
    rows = ["# Record files (written by code)\n", "| Path | KB | Last changed |", "|---|---|---|"]
    paths = sorted(ROOT.glob("*.md")) + sorted(
        p for d in RECORD_DIRS for p in (ROOT / d).rglob("*")
        if p.is_file() and not SKIP & set(p.relative_to(ROOT).parts) and p.suffix in (".md", ".html", ".json"))
    for p in paths:
        st = p.stat()
        when = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d")
        rows.append(f"| `{p.relative_to(ROOT)}` | {st.st_size / 1024:.1f} | {when} |")
    return "\n".join(rows) + "\n"


PATH_RE = re.compile(r"`([\w./~<>-]+\.(?:md|py|sh|html|json))`")


def code_audit() -> str:
    """Paths mentioned in memory and instructions that don't exist, and memory size. Free."""
    lines = [f"# Code audit ({datetime.date.today().isoformat()}, written by code)\n"]
    missing = []
    for doc in ["CLAUDE.md", "AUTONOMY.md", "workspace/notes/sophia_memory.md", "agents/README.md"]:
        text = (ROOT / doc).read_text()
        for ref in sorted(set(PATH_RE.findall(text))):
            if "<" in ref or ref.startswith("~") or "*" in ref:
                continue                         # templates and paths on the owner's Mac
            name = ref.lstrip("./")
            if not any((base / name).exists() for base in (ROOT, WORKSPACE, WORKSPACE / "notes")) \
                    and not list(ROOT.rglob(pathlib.Path(name).name)):
                missing.append(f"- `{doc}` mentions `{ref}`, which doesn't exist in the repo")
    lines += ["## Paths that don't exist", *(missing or ["- none found"]), ""]
    mem = (WORKSPACE / "notes" / "sophia_memory.md").read_text().splitlines()
    lines += ["## Memory size", f"- {len(mem)} lines, {sum(len(l.split()) for l in mem)} words"
              + (" (over 150 lines: time to trim)" if len(mem) > 150 else ""), ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- agent run
# Without `tools`, the SDK offers every Claude Code tool and `allowed_tools` only pre-approves
# some. His second run used SendUserFile (sends files to the owner), so the list is now exact.
BUILTIN_TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "WebSearch", "WebFetch"]


async def run_agent(task_text: str, resume: str | None = None,
                    max_turns: int | None = None, budget: float | None = None):
    from claude_agent_sdk import (AssistantMessage, ClaudeAgentOptions, HookMatcher,
                                  ResultMessage, TextBlock, ToolUseBlock, query)

    options = ClaudeAgentOptions(
        system_prompt=SYSTEM_PROMPT,
        tools=BUILTIN_TOOLS,                # the only built-in tools that exist for him
        allowed_tools=BUILTIN_TOOLS + [
                       "mcp__archive__verify_quote", "mcp__archive__calculate"],
        mcp_servers={"archive": archive_server()},
        disallowed_tools=["Bash", "Task", "NotebookEdit"],
        permission_mode="acceptEdits",
        hooks={"PreToolUse": [HookMatcher(
            matcher="Write|Edit|Read|Glob|Grep|WebFetch|mcp__archive__verify_quote",
            hooks=[fence_hook])]},
        cwd=str(ROOT),
        max_turns=max_turns or MAX_TURNS,
        max_budget_usd=budget or MAX_BUDGET,
        model=agent.MODEL,
        resume=resume,
        thinking={"type": "enabled", "budget_tokens": max(agent.THINKING, 1024)} if agent.THINKING else None,
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


def fill(template: str, **values) -> str:
    for key, value in values.items():
        template = template.replace("{" + key + "}", value)
    return template


def main():
    parser = argparse.ArgumentParser(description=f"Run {NAME}, the archivist and auditor.")
    parser.add_argument("mode", choices=["research", "audit", "index", "code-audit"])
    parser.add_argument("topic", nargs="?", default="", help="research topic (research mode)")
    args = parser.parse_args()

    ARCHIVE.mkdir(parents=True, exist_ok=True)
    (ARCHIVE / "_file_list.md").write_text(file_list())
    (ARCHIVE / "code_audit.md").write_text(code_audit())
    if args.mode == "code-audit":
        print((ARCHIVE / "code_audit.md").read_text())
        return
    if args.mode == "research" and not args.topic.strip():
        sys.exit('Give a topic: python archivist.py research "your topic"')
    if not agent.API_KEY and not agent.IN_CLOUD_SESSION:
        sys.exit("No API key found. Run `python agent.py --check` for help.")

    today = datetime.date.today().isoformat()
    slug = re.sub(r"[^a-z0-9]+", "-", args.topic.lower()).strip("-")[:50] or "topic"
    task_path = ROOT / "tasks" / f"archivist_{args.mode}.md"
    task_text = fill(task_path.read_text(), topic=args.topic.strip(), slug=slug, date=today)
    spec = agent.expected_output(task_text)
    (ARCHIVE / pathlib.Path(spec[0]).relative_to("archive")).parent.mkdir(parents=True, exist_ok=True)

    written = [WORKSPACE / spec[0], ARCHIVE / "for_sophia.md"]
    before = {p: p.read_text() for p in written if p.exists()}

    def problems() -> str:
        return agent.output_problem(task_text, start) or label_problem(written, start, before)

    print(f"== {NAME}: {args.mode} with {agent.MODEL} (max {MAX_TURNS} turns, ${MAX_BUDGET:.2f}) ==\n")
    start = time.time()
    try:
        result, tools = asyncio.run(run_agent(task_text))
        cost = getattr(result, "total_cost_usd", 0) or 0
        turns = getattr(result, "num_turns", 0) or 0
        problem, check = problems(), "passed"
        if problem and result is not None and getattr(result, "session_id", None):
            print(f"\n== Check failed: {problem}\n== Asking {NAME} to fix it ==\n")
            result2, tools2 = asyncio.run(run_agent(
                f"Your deliverable has a problem: {problem} Fix it now.", resume=result.session_id,
                budget=max(MAX_BUDGET - cost, 0.05)))         # the retry shares the run's budget
            tools += tools2
            cost += getattr(result2, "total_cost_usd", 0) or 0
            turns += getattr(result2, "num_turns", 0) or 0
            problem = problems()
            check = "passed after one retry" if not problem else f"FAILED after retry: {problem}"
        elif problem:
            check = f"FAILED: {problem}"
    except Exception as e:
        agent.append_log(pathlib.Path(f"{NAME} {args.mode}"), None, [], time.time() - start, error=str(e)[:300])
        raise
    if agent.FENCE_BLOCKS:
        check += f" | fence blocked {len(agent.FENCE_BLOCKS)} attempt(s)"
    agent.append_log(pathlib.Path(f"{NAME} {args.mode}"), None, tools, time.time() - start,
                     check=check, cost=cost, turns=turns)
    print(f"\n== Done: {check} ==\nCost of this run: ${cost:.4f}\nOutput: workspace/{spec[0]}")
    if check.startswith("FAILED"):
        sys.exit(1)


if __name__ == "__main__":
    main()
