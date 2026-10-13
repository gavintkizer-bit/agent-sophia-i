# Chaos in the middle, order toward the edge, roughly round. Order = a cell matches the cell two steps away (lattice) or its neighbors (solid).
import numpy as np, random, json
N, T = 301, 96
def run(seed, b, s, T=T):
    g = np.zeros((N, N), np.uint8)
    for r, c in seed: g[N//2 + r, N//2 + c] = 1
    for t in range(T):
        p = np.pad(g, 1); n = sum(p[1+dr:N+1+dr, 1+dc:N+1+dc] for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
        g = np.where(g == 1, s[n], b[n]).astype(np.uint8)
    return g
yy, xx = np.mgrid[0:N, 0:N]; rad = np.hypot(yy - N//2, xx - N//2); ang = np.arctan2(yy - N//2, xx - N//2)
def profile(g):
    ys, xs = np.nonzero(g)
    if len(ys) < 500: return None
    # extent by angle: roundness = std/mean of the farthest live cell in 16 directions
    bins = ((ang[ys, xs] + np.pi) / (2*np.pi) * 16).astype(int) % 16; far = np.zeros(16)
    np.maximum.at(far, bins, rad[ys, xs]); Rm = far.mean()
    if Rm < 20 or far.min() == 0: return None
    roundness = far.std() / Rm
    # order map: matches its shift by 2 in both axes (period-2 lattices and solids count as ordered)
    o = ((g == np.roll(g, 2, 0)) & (g == np.roll(g, 2, 1)) & (g == np.roll(g, 1, 0) ^ np.roll(g, 1, 0) ^ g)).astype(float)
    o = ((g == np.roll(g, 2, 0)) & (g == np.roll(g, 2, 1))).astype(float)
    inside = rad < Rm * 0.95
    rings = [o[inside & (rad >= Rm*a) & (rad < Rm*(a+0.2))].mean() for a in (0, 0.2, 0.4, 0.6, 0.8)]
    return dict(roundness=round(float(roundness), 3), rings=[round(float(x), 2) for x in rings], R=round(float(Rm), 1), pop=int(len(ys)))
seeds = {"cell": [(0, 0)], "pair": [(0, 0), (0, 1)], "block": [(0, 0), (0, 1), (1, 0), (1, 1)], "plus": [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)],
         "x": [(0, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)], "ring": [(1, 0), (-1, 0), (0, 1), (0, -1)], "diag": [(0, 0), (1, 1)], "L3": [(-2, 1), (-1, 2), (0, 1)]}
rnd = random.Random(11); rules = {((2, 4, 5, 7), (1, 4, 5, 6, 7))}
while len(rules) < 1200:
    B = tuple(sorted(set(rnd.sample(range(1, 9), rnd.randint(1, 4))) | {rnd.choice([1, 2])})); S = tuple(sorted(rnd.sample(range(0, 9), rnd.randint(0, 5)))); rules.add((B, S))
res = []
for B, S in rules:
    b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[list(B)] = 1; s[list(S)] = 1
    for name, seed in seeds.items():
        g = run(seed, b, s); ys, xs = np.nonzero(g)
        if len(ys) and (ys.min() == 0 or xs.min() == 0 or ys.max() == N-1 or xs.max() == N-1): continue
        p = profile(g)
        if not p: continue
        r = p["rings"]; rise = r[-1] - r[0]
        if r[0] < 0.6 and r[-1] > 0.85 and rise > 0.3 and all(r[i+1] >= r[i] - 0.05 for i in range(4)):
            res.append(dict(rule=f"B{''.join(map(str,B))}/S{''.join(map(str,S))}", seed=name, rise=round(rise, 2), **p))
res.sort(key=lambda x: x["roundness"] - x["rise"])
json.dump(res, open("res3.json", "w"), indent=1); print(len(res))
for x in res[:15]: print(x)
