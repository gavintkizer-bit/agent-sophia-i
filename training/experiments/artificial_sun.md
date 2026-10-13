# Experiment: Artificial Sun

Life Lab. The idea, the name and the condition are Gavin's (2026-10-13). Status: **condition set; next session: layered design.**

## The condition (Gavin's words)
"Chaos in the center is stably chaotic, meaning that over generations it keeps producing unpredictability, reliably."
And the picture: "A chaotic core that radiates out and eventually over layers of boundaries, meets order." The model is the real sun.

## Tests (code-graded; a candidate must pass all four)
1. **Stably chaotic core (butterfly test).** Flip ONE core cell, run 300 gens, and measure how much of the core differs.
   Pass: 30% or more every time, from 3 starts, tested at gens 1,000, 5,000 and 10,000. Truly random would be about 50%.
2. **It never settles.** The core's activity stays steady: no exact repeat in the last 3,000 of 20,000+ gens.
3. **Contained.** The core stays the same size, and the far order stays intact (98% or more).
4. **Layers (the sun part).** Activity falls off in steps across at least 2 in-between layers, not with one sharp edge.
   - Sun: core, then radiative zone (energy wanders out slowly), then convective zone (organized cells), then the surface.
   - In Life Lab terms: chaos, then a layer that carries disturbances outward but damps them, then a patterned layer, then
     plain order.

## Where we stand (measured 2026-10-13)
| Candidate | Test 1: one-cell flip spreads to (gens 1k / 5k / 10k, 3 starts) | Verdict |
|---|---|---|
| Artificial Sun I, steady (B37/S0125678) | 46%, 45%, 46% / 46%, 48%, 46% / 47%, 46%, 48% | **passes** tests 1-3; fails 4 (one sharp edge) |
| Artificial Sun I, round (B2/S045678) | 40%, 38%, 38% / 17%, 17%, 12% / 0%, 0.2%, 0% | **fails** test 1: by gen 10,000 a flip changes nothing; it crystallizes |

## Plan for next time (one step at a time)
1. Keep the steady core (it already passes the hard part).
2. Look for rules where two or three different ordered spaces sit stably side by side: solid, checkerboard, stripes, dots.
   Then build rings of them around the core, like the sun's zones, and run all four tests.
3. If no single rule can hold layers: ask Gavin whether a "zoned world" (a different rule in each ring) is fair. That would be
   designed physics, not emergent, so it's his call.
