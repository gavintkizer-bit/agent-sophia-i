# my-first-agent

My first Claude agent, built with the Claude Agent SDK and run in claude.ai/code cloud sessions.

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

**Drive cleanup:** `python sophia.py` processes the scans uploaded to `workspace/inbox/`.
See `ORGANIZE.md` for how it works and `workspace/STATUS.md` for what's ready now.

## Improve it over time
Sophia changes one thing at a time and measures it with drills (`training/TRAINING.md`), and
logs decisions in `workspace/notes/decision_log.md`.
