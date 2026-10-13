import numpy as np, json, sys
from PIL import Image
def step(g, b, s):
    n = sum(np.roll(np.roll(g, dr, 0), dc, 1) for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
    return np.where(g == 1, s[n], b[n]).astype(np.uint8)
J = json.load(open("bh2.json")); N = 150
g0 = np.zeros(N*N, np.uint8); i = 0; v = 0
for n in map(int, J["runs"].split(",")): g0[i:i+n] = v; i += n; v ^= 1
yy, xx = np.mgrid[0:N, 0:N]; rad = np.hypot(yy - N/2 + .5, xx - N/2 + .5)
rule, T = sys.argv[1], int(sys.argv[2])
Bs, Ss = rule[1:].split("/S"); b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[[int(x) for x in Bs]] = 1; s[[int(x) for x in Ss]] = 1
g = g0.reshape(N, N).copy(); act = np.zeros((N, N)); marks = sorted({10, 100, 1000, 2500, 5000, 10000, 20000, 40000} & set(range(T+1)) | {T})
seen = {}; period = None; snaps = []
for t in range(1, T + 1):
    h = step(g, b, s); act += (h != g); g = h
    if t in marks:
        # activity in the last stretch, by ring: centre (r<10), middle (10-20), edge (20-30)
        a = act / (t if t <= 10 else 1)
        rings = [round(float(a[(rad >= lo) & (rad < hi)].mean()), 3) for lo, hi in ((0, 10), (10, 20), (20, 30))]
        print(t, "share of cells that changed since last mark, centre/middle/edge:", rings, "alive in core", int(g[rad < 30].sum()))
        snaps.append(np.pad(g[30:120, 30:120], 2, constant_values=1)); act[:] = 0
    if t > T - 3000:
        k = g.tobytes()
        if k in seen and period is None: period = t - seen[k]
        seen.setdefault(k, t)
print("exact repeat found in the last 3000 gens:", period)
img = np.concatenate(snaps, 1); Image.fromarray(((1 - img) * 255).astype(np.uint8)).resize((img.shape[1]*2, img.shape[0]*2), 0).save(f"cool_{rule.replace('/','_')}.png")
