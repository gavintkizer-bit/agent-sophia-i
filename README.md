# my-first-agent

My first Claude agent, built with the Claude Agent SDK and run in claude.ai/code cloud sessions.

**What it does right now:** reads my notes in `workspace/notes/` and writes an organized plan
to `workspace/organized_plan.md`, then records the run (cost, turns, tools) in `logs/run_log.md`.

## Run it (in a claude.ai/code session)
```
pip install -r requirements.txt
python agent.py --check      # free setup check
python agent.py              # run the default task
```

## Improve it over time
After each run, open `logs/run_log.md` and fill in "What I'll change next time".
Then change ONE thing per run:
- the agent's rules: `SYSTEM_PROMPT` in `agent.py`
- the task: files in `tasks/`
- the inputs: files in `workspace/notes/`
- the model: set `AGENT_MODEL` in the environment variables
Read CLAUDE.md and follow its standard procedure: install requirements, run
`python agent.py --check`, and if it's READY, run `python agent.py`. Show me
workspace/organized_plan.md and the newest run_log entry, suggest one
improvement, and commit everything to the branch. If anything fails, explain
in plain English exactly what I need to change and where.
