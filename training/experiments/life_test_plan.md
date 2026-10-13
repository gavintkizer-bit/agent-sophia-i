# Life Lab: a starter test plan (2026-10-13)

Gavin: "I have this thing, I don't know where to start." So: three tests, smallest first, each about 5 minutes.
Each has exact settings, a place to write your guess, and what counts as yes or no. Do them in order, one a day is plenty.

## Test 1: Is 42 the number of life? (Numbers panel)
- **Claim:** 42 makes a longer-lived world than ordinary numbers do.
- **Settings:** Numbers to test `42`. How a number becomes a world: *Random fill with the number as the seed*.
  Range 1 to 200, Generations 1000. In the claim box, write your prediction (e.g. "42 lands in the top 5%").
- **Yes if:** 42's lifespan "Beats % of range" is 95% or more. **No if:** it's anywhere in the ordinary middle.
- **Then:** switch to *Picture: binary digits* and run again. A real "number of life" should stand out both ways.

## Test 2: Which density lives longest? (Experiment panel; known baseline B1)
- **Settings:** Densities `10, 20, 30, 40, 50, 60`, Seeds per density `5`, Generations `2000`, rule B3/S23, edges wrap.
- **Guess first:** which density has the most life at the end, and which settles fastest.
- **Read:** the bold row is the most alive at the end; "Settled" and "Classes" show which ones calm down.

## Test 3: Do "sacred" rules behave differently? (Numbers panel, one-row worlds)
- **Settings:** Numbers to test `3, 7, 9, 11, 22, 33, 42, 111`. How a number becomes a world: *One-row world, the number
  as the rule*. Range 0 to 255, Generations 500.
- **Guess first:** will the sacred rules be more often class III/IV (never settling) than the rest?
- **Read:** compare their Class column with the "Classes across the range" counts. Known fact to check yourself:
  rules 30 and 110 are famous for never settling (chaotic and complex).

## After these three
1. Baselines B2-B4 (ant highway, Rule 90 dimension, ash census) as the tools for them get built.
2. Numerology N1-N3 at full size (ranges of 500-1,000 numbers).
3. Your own conjectures, the real point. Every saved seed and experiment is a place to start.
