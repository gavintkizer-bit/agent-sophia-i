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
