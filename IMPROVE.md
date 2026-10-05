# Sophia's self-improvement routine

How I find and fix my own weak spots. The cycle steps come from my owner; the rest is mine to
refine. Every cycle is logged in `workspace/notes/improvement_log.md`.

## The cycle (from my owner, 2026-10-05)

1. Parse available tools, data, and applications for errors and bugs.
2. Use information gleaned to note fixes, research for better / more data, and plan of attack.
3. Research and compile any relevant data.
4. Use notes to improve order, files, and organization.
5. Repeat.

## How I run it

**When:** a light cycle at the end of any session where I changed something, and a full cycle
once a week (Sunday, with `python train.py`) or when my owner asks.

**Quiet days cost almost nothing:** when the daily check-in finds no uploads, requests, ticks or
answers, its "light cycle" is only this: look at the open items in the
improvement log, and fix one only if it's small and clearly worth it. Otherwise stop with one line.
No helper runs, no research, no rereading code on a quiet day.

**1. Parse: what I check**
- Code: `agent.py` (Hypatia), `sophia.py`, `make_mac_script.py`, `sophia_scan.sh`. Read them for
  bugs; run `bash -n` on shell scripts; dry-run `python sophia.py --dry` (free).
- Edge cases: what happens next week, after a re-download, with a strange filename, an empty
  upload, or an upload in the wrong folder? What would break one of my owner's commands?
- Drills (weekly): `python train.py`; compare with `training/scoreboard.md`. A drop is a bug.
- Data: `logs/run_log.md` (failed checks, costs creeping up), every `organize_preview.md` (warnings),
  Hypatia's reports (claims vs. numbers).
- The Crew Board: unanswered questions, stuck tasks, requests for me that are still waiting.
- Docs: anything in CLAUDE.md, ORGANIZE.md, SOPHIA.md, or my memory that is no longer true.

**2. Note:** each finding gets one line in the log: what's wrong, why it matters, the fix, and its
status. Severity: **bug** (could break something or mislead my owner), **gap** (missing data or
feature), **tidy** (order and clarity).

**3. Research:** only questions that change a decision. Prefer official sources (Apple, Ableton,
Anthropic docs) over blogs, cite the source in the log, and say when something is uncertain.

**4. Improve:** fix bugs first, then gaps, then tidying. One logical change per commit, tested
before merging. Update the board when my owner's steps change, and memory when facts change.

**5. Repeat:** the next cycle starts by checking the previous cycle's open items.

## Rules for improving myself

- The safety rules never get weaker in the name of improvement: nothing deleted on the Mac,
  audio and Ableton files never moved, the fence around Hypatia stays.
- The constitution in SOPHIA.md is my owner's. I may propose changes to it, never make them.
- Cost: a cycle spends at most about $0.50 of Hypatia's time; my own reading and fixing is free.
- If a fix would change how my owner works, I ask on the board first.
- I tell my owner what I fixed in one or two lines, not a report, unless they ask for more.
