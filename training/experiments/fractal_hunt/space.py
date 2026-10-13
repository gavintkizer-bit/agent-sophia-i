# Ordered space everywhere (wraps around), chaos disc in the middle. Which rules keep both, with the disc not spreading?
import numpy as np, random, json, sys
def step(g, b, s):
    n = sum(np.roll(np.roll(g, dr, 0), dc, 1) for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
    return np.where(g == 1, s[n], b[n]).astype(np.uint8)
N = 96; yy, xx = np.mgrid[0:N, 0:N]; rad = np.hypot(yy - N/2 + .5, xx - N/2 + .5); disc = rad < 20; far = rad > 34
spaces = {"solid": np.ones((N, N), np.uint8), "checker": ((yy + xx) % 2 == 0).astype(np.uint8), "stripes": (yy % 2 == 0).astype(np.uint8),
          "dots": ((yy % 2 == 0) & (xx % 2 == 0)).astype(np.uint8), "empty": np.zeros((N, N), np.uint8)}
lo, hi = int(sys.argv[1]), int(sys.argv[2]); rnd = random.Random(5); rules = []; seen = set()
while len(rules) < hi:
    B = tuple(sorted(rnd.sample(range(0, 9), rnd.randint(1, 5)))); S = tuple(sorted(rnd.sample(range(0, 9), rnd.randint(0, 7))))
    if (B, S) not in seen: seen.add((B, S)); rules.append((B, S))
out = []
for B, S in rules[lo:hi]:
    b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[list(B)] = 1; s[list(S)] = 1
    for name, sp in spaces.items():
        # the space must be stable (or flip every other step) by itself
        a1 = step(sp, b, s); a2 = step(a1, b, s)
        if not ((a1 == sp).all() or (a2 == sp).all()): continue
        g = sp.copy(); rng = np.random.default_rng(1); g[disc] = (rng.random(disc.sum()) < 0.4).astype(np.uint8); ok = True
        for t in range(1, 601): g = step(g, b, s)
        h = step(g, b, s); h2 = step(h, b, s)
        ref = sp if (a1 == sp).all() else None
        farok = ((g == sp) | (g == a1))[far].mean()          # far space still ordered (either phase of a flip)
        changing = (h2 != g)[disc].mean()                     # core still alive, not a period-1/2 freeze
        inner = (rad < 16); dens = g[inner].mean()
        if farok > 0.98 and changing > 0.1 and 0.1 < dens < 0.9:
            # chaos radius: where the pattern stops matching ordered space
            mism = ~((g == sp) | (g == a1)); rr = rad[mism]; rc = float(np.percentile(rr, 95)) if len(rr) else 0
            out.append(dict(rule=f"B{''.join(map(str,B))}/S{''.join(map(str,S))}", space=name, far=round(float(farok), 3), changing=round(float(changing), 3), rc=round(rc, 1), dens=round(float(dens), 2)))
json.dump(out, open(f"sp_{lo}.json", "w")); print(lo, hi, len(out))
