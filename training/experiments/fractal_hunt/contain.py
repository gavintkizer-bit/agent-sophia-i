# Top-down: build the end state (round ordered wall, chaos inside) and find rules that keep it.
import numpy as np, random, json, sys
def step(g, b, s):
    p = np.pad(g, 1); N0, N1 = g.shape
    n = sum(p[1+dr:N0+1+dr, 1+dc:N1+1+dc] for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
    return np.where(g == 1, s[n], b[n]).astype(np.uint8)
N = 96; yy, xx = np.mgrid[0:N, 0:N]; rad = np.hypot(yy - N/2 + .5, xx - N/2 + .5)
inner, outer = rad < 24, (rad >= 24) & (rad < 30); outside = rad >= 30
walls = {"solid": outer.astype(np.uint8), "checker": (outer & ((yy + xx) % 2 == 0)).astype(np.uint8),
         "rings": (outer & (np.floor(rad) % 2 == 0)).astype(np.uint8), "thick": ((rad >= 24) & (rad < 32)).astype(np.uint8)}
lo, hi = int(sys.argv[1]), int(sys.argv[2]); rnd = random.Random(99); rules = []; seen = set()
while len(rules) < hi:
    B = tuple(sorted(rnd.sample(range(1, 9), rnd.randint(1, 5)))); S = tuple(sorted(rnd.sample(range(0, 9), rnd.randint(0, 7))))
    if (B, S) not in seen: seen.add((B, S)); rules.append((B, S))
out = []
for B, S in rules[lo:hi]:
    b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[list(B)] = 1; s[list(S)] = 1
    for wname, w in walls.items():
        wall_zone = w.astype(bool) | ((rad >= 24) & (rad < 32))
        for trial in range(2):
            rng = np.random.default_rng(trial); g = w.copy(); g[inner] = (rng.random(inner.sum()) < 0.4).astype(np.uint8)
            ok = True; hist = {}
            for t in range(1, 801):
                g = step(g, b, s)
                if t in (50, 200, 800):
                    if g[rad >= 33].any(): ok = False; break           # leaked outside
                    if (g[wall_zone] != w[wall_zone]).mean() > 0.03 and (t < 800): pass
                if t >= 790: hist[t] = g.copy()
            if not ok: continue
            wall_kept = 1 - (hist[800][wall_zone] != w[wall_zone]).mean()
            core = hist[800][inner]; changing = (hist[800] != hist[799])[inner].mean(); changing2 = (hist[800] != hist[798])[inner].mean()
            density = core.mean()
            if wall_kept > 0.95 and changing > 0.05 and changing2 > 0.05 and 0.1 < density < 0.9:
                out.append(dict(rule=f"B{''.join(map(str,B))}/S{''.join(map(str,S))}", wall=wname, trial=trial, kept=round(float(wall_kept), 3), changing=round(float(changing), 3), density=round(float(density), 2)))
                break
json.dump(out, open(f"c_{lo}.json", "w")); print(lo, hi, len(out))
