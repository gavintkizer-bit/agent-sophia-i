# Project: my-first-agent

A beginner's first Claude agent, built on the Claude Agent SDK (Python).
The owner works only through claude.ai/code cloud sessions (their Mac is too old to run Claude Code locally),
so YOU are their hands: install, run, debug, and explain in plain language.

## Layout
- `agent.py`: the agent. `--check` verifies setup at no API cost.
- `tasks/`: one Markdown file per task the agent can run.
- `workspace/`: the ONLY folder the agent reads and writes. Its input notes live in `workspace/notes/`.
- `logs/run_log.md`: one entry per run (model, turns, time, cost, tools used).

## Standard procedure for every session
1. `pip install -r requirements.txt`
2. `python agent.py --check`. If it reports NOT READY, stop and explain the exact fix (see Troubleshooting).
3. Run the requested task: `python agent.py` (default task) or `python agent.py tasks/<name>.md`.
4. Show the owner: the output file the agent created, and the newest entry in `logs/run_log.md`.
5. Suggest ONE improvement for the next run (system prompt, task wording, tools, or model).
6. Commit outputs and the log to the session branch.

## Rules
- Never print, echo, log, or commit the value of ANTHROPIC_API_KEY.
- If `.gitignore` is missing, create it with: `__pycache__/`, `*.pyc`, `.env`, `.venv/`.
- Keep the default model (claude-haiku-4-5) unless the owner asks otherwise; it's cheapest.
- Explain technical steps briefly and in plain English; the owner is new to this.

## Troubleshooting
- "ANTHROPIC_API_KEY is not set": the owner must add `ANTHROPIC_API_KEY=...` under the cloud
  environment's Environment variables (environment selector -> gear icon), then start a NEW session.
- "Network blocked api.anthropic.com": the owner must set the environment's Network access to Custom,
  keep the default package-manager list enabled, and add `api.anthropic.com`. Then start a new session.
- "401": the key is wrong or was revoked; create a new one in the Claude Console.
- SDK or CLI errors: read the full traceback, check the installed SDK version, and try
  `pip install -U claude-agent-sdk` before anything else. Explain what you found.
