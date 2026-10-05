# Setup plan

## Status: WORKING (tested 2026-10-05)
In a claude.ai/code cloud session, **the agent doesn't need an API key.** It uses the
session's own Claude connection. On 2026-10-05 it ran `tasks/first_task.md` with no key:
8 turns, 20 seconds, wrote `workspace/organized_plan.md`, logged in `logs/run_log.md`.

The key was never going to work. Cloud sessions don't pass `ANTHROPIC_API_KEY` to your
code, and even if they had, the session's own connection takes priority over it.

## Tomorrow
1. Start a new session on this repo (default `main` branch; the fix is merged).
2. Type: **run agent**
3. Expected: `--check` says `READY`, then the agent runs and writes its output file.

Nothing else is needed: no key, no environment settings, no network changes.

## Contingencies (in order; if one fails, move straight on)

**1. "No API key found" or an old error message**
The session is running old code. Check the session is on `main` (the fix was merged
in PR #4) and that `agent.py` contains `IN_CLOUD_SESSION`.

**2. The agent crashes with an SDK or Claude Code error**
Ask Claude: "run `pip install -U claude-agent-sdk` and try again; if it still fails,
explain the error." If it's still broken after that, go to 3.

**3. Skip agent.py: let the cloud session do the task itself**
Claude Code in the cloud session is already a full agent. Type:
> Do the task in tasks/first_task.md yourself, working in the workspace/ folder.

Same result, no SDK involved. You lose the cost log but keep everything else.

**4. Skip code entirely: use a Claude.ai Project (Path A in your notes)**
In claude.ai, create a Project. Upload the files from `workspace/notes/`, paste the
contents of `tasks/first_task.md` into the Project instructions, and chat.
Works on any browser, no setup.

**5. Use the API key route instead (only if you need it outside claude.ai/code)**
For running the agent somewhere other than a cloud session (another computer, a server).
In the Claude Console, test the key in the **Workbench** first (no code). Then set
`AGENT_API_KEY` (or `ANTHROPIC_API_KEY`) wherever you run it.

## Housekeeping (not urgent)
- `API_KEY` (a file holding a real key) is committed to the repo. The repo is private,
  but replace that key anyway: Claude Console → API Keys → delete it, then ask Claude to
  "delete the API_KEY file and add it to .gitignore".
- You can delete any `ANTHROPIC_API_KEY` / `AGENT_API_KEY` lines from the environment settings.
  They aren't used in cloud sessions.
