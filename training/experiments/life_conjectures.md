# Life Lab baselines: known results to reproduce first (2026-10-13)

Gavin's ask: "Propose a few conjectures to test (known) so we can get baselines." Reproducing known results first
tests our tools; if we can't get a known answer, we fix the lab before trusting it with an unknown one.
Rules and measures: `life_lab_rules.md`. For each one: what's known, what we'd measure, and what the page still needs.
Write the guess in the Experiment panel before running, as always.

## B1. Random soups settle (Conway, B3/S23)
- **Known:** almost every random start eventually stops changing except for small oscillators and escaping gliders.
  On a wrapped grid it must eventually repeat (there are only finitely many states); the open part is how long it takes.
- **Measure:** % settled and settle time vs. density (the panel does this now). Use 2,000+ generations; 500 is often too
  short, so our first runs showed 0% settled.
- **Needs:** nothing new. Ready to run.

## B2. Langton's ant builds a highway after about 10,000 steps (ant, RL)
- **Known:** from a blank grid the ant wanders chaotically for roughly 10,000 steps, then repeats a 104-step cycle
  that moves it diagonally forever (the "highway").
- **Measure:** the step where its position starts changing by the same (dx, dy) every 104 steps.
- **Needs:** a small highway detector (code). Use the 480x300 world with wrap off.

## B3. Rule 90's triangle has fractal dimension log2(3), about 1.585 (one row)
- **Known:** from one cell, Rule 90 draws the Sierpinski triangle; its box-counting dimension is log 3 / log 2.
- **Measure:** box-counting dimension of the space-time picture. This tests our dimension tool against an exact answer
  before we use it on new patterns (like the fractal search).
- **Needs:** a dimension meter (code).

## B4. The ash is mostly blocks, blinkers and beehives (Conway)
- **Known:** in large censuses of random soups (the Catagolue project), the block is the most common leftover object,
  followed by the blinker and the beehive.
- **Measure:** count each small object left after a soup settles.
- **Needs:** an object counter (code). The hardest of the four; I'd do it last.

**Order I'd suggest:** B1 (ready now), B3 (checks a tool we need for every fractal question), B2, then B4.
Exact figures beyond these (e.g. final density of ash) I'm not sure enough to state; we measure first and cite later.
