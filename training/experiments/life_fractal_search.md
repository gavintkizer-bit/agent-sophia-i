# Fractal seed search (2026-10-13, his ask: "try to find a new one, if you can't you may use one that is known")

**Method (code, `life_fractal_search.py`):** 2,500 random Life-like rules that let a single cell grow (B1 in the rule),
plus two known fractal rules. Each was run from one cell for 64 generations. Two scores were computed:
box-counting dimension (fractal if clearly between 1 and 2, with a straight-line fit of r² > 0.995) and
self-similarity (generation 64 shrunk by half, compared with generation 32).

**Result:** 129 rules had fractal-like dimension, but the top ones (about 1.8) were dense blobs with holes. In the
cleaner 1.4-1.7 range, the best was **B12357/S01234** (dimension 1.69), a symmetric carpet that is NOT truly self-similar
(score 0.51). I can't honestly call it a new fractal, and I couldn't check whether it's already documented.

**Loaded instead (known):** Fredkin's Replicator, B1357/S1357 (1970s). Every pattern copies itself. From one cell
it gives 416 cells at generation 15, then 8 copies at 16, then a 1,617-cell carpet at 31: the nested pattern
repeats at each doubling. Life Lab's "Fractal seed" button loads it.

**Next, if he wants:** a proper hunt (more rules, multi-cell seeds, a stricter self-similarity test across three
doublings) and a check of the candidates against published rule lists.

## Hunt 2 (2026-10-13): a fractal with surprises. Found: "Void meets matter"
**Ask (Gavin):** a unique fractal seed with elements of unpredictability, saved in Life Lab.
**Method (`fractal_hunt/hunt.py`, `refine.py`):** 1,500 random rules x 3 small asymmetric seeds on the 240 x 150 walled board,
64 gens. Kept patterns with a box-counting dimension of 1.35-1.8 that also passed three unpredictability tests: superposition fails
(it isn't a copy machine like the Replicator), moving one seed cell changes 30%+ of the result, and the pattern is asymmetric.
879 passed, but pictures showed most were noise blobs. The stricter test (structure even across scales) left one.
**The find:** rule **B2457/S14567**, three cells in a bent line: (-2,1), (-1,2), (0,1) from the center.
- It grows into a diamond. One side is ragged chaos and the other is a perfect checkerboard lattice. The border between them
  holds as it grows (checked to gen 256 on a 600 x 600 grid, `long.png`).
- Numbers at gen 64: 5,679 alive; dimension about 1.71 (local slopes 1.58-1.91, so it's fractal-ish, not a strict fractal);
  self-similarity 0.65 (gen 64 shrunk by half vs gen 32); moving one seed cell changes 38%; superposition fails by 55%.
- Gavin, on seeing it: "void meeting matter. Chaos meeting order. Beautiful." He named its feel; the name is his phrase.
- Checked in Life Lab itself: loading the saved seed and stepping to gen 64 gives the same 5,679.
- I can't confirm it's undocumented: B2457/S14567 is one of 262,144 Life-like rules, and I haven't checked rule catalogs.
- Saved in Life Lab seeds: "Void meets matter" (240 x 150; it reaches the wall at gen 74) and a huge-board copy (to about gen 145).
**Lesson (top-down):** I judged by scores first and got 879 "fractals" that were noise. Looking at the whole picture first, then
measuring, found the real one. Gavin spotted it before my filter did.

## Hunt 3 (2026-10-13): "Black hole", chaos in the middle and order toward the edge
**Ask (Gavin):** "a pattern or fractal that coalesces in the middle in chaos and orders itself the farther it gets from the center,
circularly." Name it Black hole.
**Method (`fractal_hunt/hunt3.py`):** 1,200 rules x 8 small seeds, 96 gens on a 301 x 301 grid. Order was measured ring by ring:
a cell counts as ordered when it matches the cells two steps away. Kept patterns with a disordered core (under 0.6), an ordered rim
(over 0.85) and order rising outward: 68 passed. I looked at the 12 best pictures first (`bh12.png`), then checked the numbers.
**The find:** rule **B12356/S** (nothing survives; a cell is born with 1, 2, 3, 5 or 6 neighbors), started from **two diagonal cells**
(0,0) and (1,1).
- A chaotic star with jets along one diagonal, inside perfect concentric square rings (`bh_time.png`, gens 40-160).
- Order by ring at gen 96, core to rim: 0.27, 0.46, 0.77, 0.91, 0.91.
- The rings grow at one cell per generation and the chaos follows more slowly, so the ordered band holds while it grows. By gen 160
  the chaos fills most of it. The best view is around gen 80-120.
- Limit: on a square grid the rings are squares, not circles. Every rule here spreads through the 8 neighbors.
- Checked in Life Lab: typed in by hand, it gives 19,470 cells at gen 100, the same as the search code.
- Saved in Life Lab seeds as "Black hole" (300 x 300, walls). I haven't checked rule catalogs, so I can't say it's new.
