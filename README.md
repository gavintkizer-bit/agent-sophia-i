# my-first-agent

My first Claude agent, built with the Claude Agent SDK and run in claude.ai/code cloud sessions.

## Goal
Sophia is my general agent and assistant (full scope: `SCOPE.md`). First job: keep my laptop
and my life organized, one small, safe step at a time. Second: test what AI agents can do
(`training/TRAINING.md`). She works on her own within the limits in `AUTONOMY.md`.
- **Laptop:** free up disk space and keep Downloads tidy, without breaking my Ableton samples or projects.
- **Life:** turn my messy notes into clear plans I can act on.
- **Safety:** the agent never touches my Mac or deletes anything. It makes plans and scripts; I review and run them.

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
