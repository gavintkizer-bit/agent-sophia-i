# My agents

I'm Sophia, a general agent. When a kind of task keeps coming back, I may create a specialized
agent for it (green level in AUTONOMY.md; I tell my owner after). This page is the registry.

## When to create one

All of these should be true:
- The task has come up **3+ times**, or will clearly recur.
- It has a clear input and a clear output I can check.
- A cheaper model, narrower tools or a tighter fence would do it as well as I would.
- I can write **at least one drill** for it (`training/drills/`) before relying on it.

## Two kinds

1. **Helper scripts (Claude Agent SDK)**, like Hypatia (`agent.py`): run by code, cheap models,
   fenced to `workspace/`, every run logged. Best for bulk work and anything a routine runs.
2. **Session subagents** in `.claude/agents/<name>.md`: specialists I can call during a session
   (a researcher, a reviewer). Each file holds a name, a description, allowed tools and instructions.

Every agent gets: a name (my owner may rename it), a one-paragraph purpose, its limits, at least
one drill, and an entry below. Retiring one is yellow level: flag it to my owner.

## Registry

| Agent | Kind | Model | Purpose | Drills | Since |
|---|---|---|---|---|---|
| **Hypatia** (`agent.py`) | SDK helper | Haiku 4.5, thinking 2000 | Bulk sorting, drafts, notes → plans | all 6 | 2026-10-05 |

## Candidates (not built yet)

- **A reviewer subagent** that reads my diffs before I commit (I've made careless edits before).
  Build it if a careless commit happens again.
- **A music helper** once my owner wants help finishing tracks or finding a band.
