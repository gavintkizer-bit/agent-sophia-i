# Life Lab: the rules, exactly (phase 0, 2026-10-13)

Gavin: "run a bunch of tests to make sure that we have clearly defined rules and code", before variables and conjectures.
This file is the definition. The page's **Self-test** checks the code against it (12 checks, all passing on 2026-10-13;
a planted engine bug made 6 of them fail, so the checks have teeth).

## Life (2D)
- **Grid:** COLS x ROWS cells (96x60, 240x150 or 480x300). Each cell is 0 (dead) or 1 (alive).
- **Neighbors:** the 8 surrounding cells (Moore neighborhood).
- **Update:** synchronous. Every cell's next state is computed from the current generation, then all change at once.
- **Rule notation B/S:** `B3/S23` means a dead cell with exactly 3 live neighbors is born; a live cell with 2 or 3
  survives; every other cell is dead next generation. Any digits 0-8 are allowed (e.g. `B1357/S1357`, the Replicator).
- **Edges:** *wrap* = a torus (top meets bottom, left meets right); *walled* = cells outside the grid count as dead.
- **Random fill:** each cell is alive if a seeded generator (mulberry32) gives a number below the density. The same seed and
  density always make the same world.

## One row (1D)
- One line of cells; each new line is computed from the line above and drawn below it (space-time picture).
- **Rule number 0-255** (Wolfram code): a cell's new value is bit (4L + 2C + R) of the rule number, where L, C, R are
  the left, center and right cells above it. Edges wrap or count as 0, as set.
- When the page fills, the oldest line scrolls off the top.

## Ant (turmites)
- Cells hold a color 0..k-1, where k is the length of the turn rule (`RL` gives k = 2). Turn letters: R right, L left,
  N straight, U back.
- **Each step, in this order:** turn by the letter for the current cell's color, advance that cell's color by 1 (mod k),
  then move one cell forward. The ant starts at the center facing up. With walls, it stops at the edge.
- "Generation" counts ant steps.

## Measures in experiments (Life only)
- **Alive at end:** live cells at the last generation run. **Peak:** the most live cells at any generation.
- **Settled:** the whole grid repeated an earlier state exactly (checked by hash). Settled generation = when that repeated
  state first appeared; period = gap between repeats (period 1 = frozen).
- **Classes (Wolfram):** I = died out or froze (period 1); II = repeats with a period > 1; III/IV = didn't settle within
  the generations run. Code can't tell III (random-looking) from IV (complex structures); that's a human call.

## Self-test checks (known answers)
Block still · blinker period 2 · glider moves (1,1) per 4 · pulsar period 3 with 48 cells · diehard dies at 130 ·
Gosper gun +5 cells per 30 (36 at start) · glider wraps a 20x20 torus in 80 · same seed same world · Replicator one cell gives
8 cells at generations 16 and 32 · Rule 90 row t has 2^(ones in t) cells · RL ant makes a 2x2 square and is home after 4 ·
the ant is exactly reversible over 1,000 steps.

## Open question for later (his call)
Whether Life Lab talks to other artifacts (e.g. the Test Bench) gets decided per experiment.
