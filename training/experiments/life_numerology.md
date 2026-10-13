# Numerology claims, tested in Life Lab (proposal, 2026-10-13)

Gavin: "pull conjecture and patterns from numerology that can be tested in game. These tests could directly prove or
disprove claims in numerology and sort the good from the bad."

## What Life Lab can and can't test
- **Can:** claims that certain numbers *show up more often in natural or emergent systems* than chance predicts (3, 7, 9,
  "master numbers" 11/22/33, repeating "angel numbers" like 111, Tesla's 3-6-9, the golden ratio). Life is a fair test
  bed: its rules know nothing about numerology, so any excess would be a real surprise.
- **Can't:** claims about people (a life-path number shaping personality or destiny). Life Lab has no people in it.
  Those need human data and a different study.
- **Kept apart:** real mathematics that numerology borrows (Fibonacci numbers, the golden ratio in plant spirals).
  Where math predicts a number, we test the math claim on its own terms.

## How every test runs (fair by design)
1. Write the numerology prediction and the **null** (what plain chance predicts) before running.
2. Decide what counts as a hit (e.g. "9 appears at least 25% more often than chance").
3. Run many seeds; code counts. Report the result whichever way it goes, with a simple chance test (chi-square).
4. Run a **control** first: a known statistical law, so we know the tool works (Benford's law for first digits).

## Proposed tests
- **N0 (control), Benford's law:** first digits of final populations across many soups. Real data often favors 1
  (about 30%); this checks our counter before we test anything mystical.
- **N1, digital roots and 9:** numerology treats the digital root (repeat digit-summing to 1-9) as meaningful, with 9 as
  "completion". Null: roots of large varying counts are close to uniform (about 11.1% each). Test: final populations, peaks
  and settle times across 1,000+ runs.
- **N2, sacred and Tesla numbers (3, 6, 7, 9):** do oscillator periods and settle times favor them? Science predicts
  period 1 and 2 dominate (blocks and blinkers are everywhere), so a 3/7/9 excess would be news.
- **N3, master and angel numbers (11, 22, 33; 111, 222, ...):** do they appear as exact counts more often than their
  neighbors (10, 12, 21, 23...)? Null: a smooth distribution with no spikes at repdigits.
- **N4, golden ratio:** do growth ratios between generations settle near 1.618 in any common pattern? (Math says phi shows
  up in some growth processes; numerology says it's everywhere.)

## Tools the page needs
A batch runner that collects many numbers (counts, periods, times), plus a "Numbers" readout: first-digit and
digital-root histograms against chance, a repdigit counter, and the chi-square check. One build serves all five tests.
