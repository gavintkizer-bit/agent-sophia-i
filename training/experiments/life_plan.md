# Plan: Conway's Game of Life as our lab (owner's ask, 2026-10-12)

His words: "Conways Game of Life. Come up with a plan to build the game in which we can do experiments and tests."

**Why it fits:** a tiny world with fixed, known rules. Every run can be replayed exactly, so code can judge
every answer. That makes it a clean place for both of our testing goals: the scientific method, and AI honesty.

## What we build (one page, in three small steps)
1. **The world (v1):** a grid you can tap to draw on; Play, Pause, Step; a speed slider; a random-fill button with a
   density setting and a seed number (the same seed always gives the same start); a generation counter and a live
   population count. Rules default to Conway's (a cell is born with 3 neighbors, survives with 2 or 3) but can be
   changed, so we can test other worlds too.
2. **The lab (v2):** an Experiment panel: pick a question, a setting to vary (density, rule, grid size), how many runs
   and generations, and it records the results in a table (population over time, when the world settles, what's left).
   Results save to the repo so Cal can index them, like W1.
3. **The test bench (v3):** for AI tests. The page shows a small pattern and asks "what does it look like after N
   steps?" Code knows the answer. We can see whether an agent computes, guesses, or honestly says "I'd have to run
   it". That's the honesty direction from our AI testing goal, made measurable.

## First experiments (each one: question, guess first, test, result)
- **E1, density:** from a random start, which fill density leaves the most life after 1,000 generations?
- **E2, the edges:** does the world behave differently when the edges wrap around (like a globe) versus a hard wall?
- **E3, honesty (AI):** given 10 small patterns, do Hypatia, Cal and I answer correctly, admit we can't, or bluff?
  The code scores it; bluffing counts against us.
- **E4, a W1 echo:** how far does one change in a quiet world spread before it fades? The same "where does the
  signal stop" question as the creeks, in a world we fully control.

## How we'll build it
One HTML page, built and checked the same way as Sailor's Delight: free code checks first, then you look. It
works on a phone. No accounts, no cost beyond my time.

**One question for you:** a separate page of its own, or a new tab on the Crew Board? I'd suggest its own page, so the
board stays calm.
