import numpy as np, random, json, sys
def step(g, b, s):
    N0, N1 = g.shape; p = np.pad(g, 1)
    n = sum(p[1+dr:N0+1+dr, 1+dc:N1+1+dc] for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
    return np.where(g == 1, s[n], b[n]).astype(np.uint8)
def disorder(g): return ~((g == np.roll(g, 2, 0)) & (g == np.roll(g, 2, 1)))
seeds = {"cell": [(0, 0)], "pair": [(0, 0), (0, 1)], "block": [(0, 0), (0, 1), (1, 0), (1, 1)], "plus": [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)],
         "x": [(0, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)], "ring": [(1, 0), (-1, 0), (0, 1), (0, -1)], "diag": [(0, 0), (1, 1)], "L3": [(-2, 1), (-1, 2), (0, 1)],
         "tri": [(0, 0), (0, 1), (1, 0)], "line3": [(0, -1), (0, 0), (0, 1)]}
lo, hi = int(sys.argv[1]), int(sys.argv[2]); rnd = random.Random(2026); rules = []
seen = set()
while len(rules) < hi:
    B = tuple(sorted(set(rnd.sample(range(1, 9), rnd.randint(1, 5))) | {rnd.choice([1, 2, 3])})); S = tuple(sorted(rnd.sample(range(0, 9), rnd.randint(0, 6))))
    if (B, S) not in seen: seen.add((B, S)); rules.append((B, S))
N = 121; yy, xx = np.mgrid[0:N, 0:N]; rad = np.hypot(yy - N//2, xx - N//2); out = []
for B, S in rules[lo:hi]:
    b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[list(B)] = 1; s[list(S)] = 1
    for name, seed in seeds.items():
        g = np.zeros((N, N), np.uint8)
        for r, c in seed: g[N//2 + r, N//2 + c] = 1
        for t in range(48): g = step(g, b, s)
        if g.sum() < 100: continue
        d = disorder(g); ys, xs = np.nonzero(g); R = np.hypot(ys - N//2, xs - N//2).max()
        if R < 20: continue
        core = d[rad < R * 0.3].mean(); rim = d[(rad > R * 0.6) & (rad < R * 0.9)].mean()
        if core > 0.4 and rim < 0.15: out.append(dict(rule=f"B{''.join(map(str,B))}/S{''.join(map(str,S))}", seed=name, core=round(float(core), 2), rim=round(float(rim), 2), R=round(float(R), 1)))
json.dump(out, open(f"s1_{lo}.json", "w")); print(lo, hi, len(out))
