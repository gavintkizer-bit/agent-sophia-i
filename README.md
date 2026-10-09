# my-first-agent

My first Claude agent, built with the Claude Agent SDK and run in claude.ai/code cloud sessions.

## Where things live (map, 2026-10-09)
| You want… | Look here |
|---|---|
| Your day: agenda, goals, my asks, meeting notes | **Crew Board**: https://claude.ai/artifact/Ya8vK5Po45ujpGCbfugRHB |
| Your human-to-agent tests | **Test Bench**: https://claude.ai/artifact/B75eBTeRhyFnpN3W6Fndpd (also linked from the board) |
| Who Sophia is | `SOPHIA.md` (constitution, village, goals), `SCOPE.md`, `AUTONOMY.md` |
| What Sophia remembers | `workspace/notes/sophia_memory.md` (her thread is at the top) |
| Money, goals, ideas, good uses of AI | `workspace/notes/` |
| Cal's research and audits | `workspace/archive/` (index: `workspace/archive/INDEX.md`) |
| Training and tests | `training/` (drills, scoreboard, experiments, human tests) |
| Your own writing and drawings you shared | `owner_own/` (only Sophia reads it) |
| Finished projects | `archive/` (drive cleanup, Oct 2026) |

**Chats:** the chat titled "Sophia home (routines)" is where the scheduled work runs (Cal's research, the
nightly prep, the daily check-in). Start a fresh chat for each meeting or big task; everything that matters
is saved here, so chats can come and go.

## Goal
Sophia is my general agent and assistant (full scope: `SCOPE.md`). She does the work humans don't
need to do, so I can spend my time on people and on what I make:
1. AI security and privacy tests, and my "Turing question" tests that give me data.
2. Raw data, backend scripts and scaffolding for my projects, kept updated, analyzed, and reported.
3. Organizational tasks, with my permission (the laptop, files, plans).
4. Time management, above all.

**Never:** AI doesn't touch my organic, human creations: music, drawing, and some writing.
**Always:** short, calm lists; the village way (ask for help, serve when asked, protect each other).
She works on her own within the limits in `AUTONOMY.md`, and never deletes anything on my Mac.

**The crew:** Sophia (general, the claude.ai/code session), Hypatia (`agent.py`: bulk sorting and
drafts) and Callimachus (`archivist.py`: research, records, audits). Registry: `agents/README.md`.

## Run it (in a claude.ai/code session)
```
pip install -r requirements.txt
python agent.py --check      # free setup check
python agent.py              # Hypatia's default task (notes -> plan)
python archivist.py research "topic"   # Callimachus researches a topic
python safety_test.py        # free checks of the safety rules
python train.py              # training drills (a few cents each); --summary shows pass rates
```

**Drive cleanup (completed 2026-10-07: 18 GB free to about 55 GB):** `python sophia.py` processes scans in `workspace/inbox/` if it's ever restarted.
See `ORGANIZE.md` for how it works and `workspace/STATUS.md` for what's ready now.

## Improve it over time
Sophia changes one thing at a time and measures it with drills (`training/TRAINING.md`), and
logs decisions in `workspace/notes/decision_log.md`.
