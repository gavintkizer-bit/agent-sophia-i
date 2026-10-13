import numpy as np, json, sys
exec(open("stable1.py").read().split("lo, hi =")[0])
cands = json.load(open("s1_all.json")); k, K = int(sys.argv[1]), int(sys.argv[2]); cands = cands[k::K]
N = 401; yy, xx = np.mgrid[0:N, 0:N]; rad = np.hypot(yy - N//2, xx - N//2); out = []
def rb(rule):
    Bs, Ss = rule[1:].split("/S"); b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[[int(x) for x in Bs]] = 1
    if Ss: s[[int(x) for x in Ss]] = 1
    return b, s
for c in cands:
    b, s = rb(c["rule"]); g = np.zeros((N, N), np.uint8)
    for r, cc in seeds[c["seed"]]: g[N//2 + r, N//2 + cc] = 1
    stats = {}; prev = None; ok = True
    for t in range(1, 181):
        prev = g; g = step(g, b, s)
        if t in (60, 120, 180):
            ys, xs = np.nonzero(g)
            if len(ys) < 100: ok = False; break
            R = float(np.hypot(ys - N//2, xs - N//2).max()); d = disorder(g) & (rad < R - 4)
            dy, dx = np.nonzero(d)
            if len(dy) < 30: ok = False; break
            rc = float(np.percentile(np.hypot(dy - N//2, dx - N//2), 90))
            core = float(d[rad < max(3, rc * 0.5)].mean()); band = float(d[(rad > rc + 3) & (rad < R - 4)].mean()) if R - rc > 10 else 1.0
            stats[t] = dict(R=round(R, 1), rc=round(rc, 1), core=round(core, 2), band=round(band, 3))
    if not ok: continue
    live = float((g != prev)[rad < stats[180]["rc"]].mean())
    a, z = stats[120], stats[180]
    if z["rc"] <= a["rc"] * 1.08 + 2 and z["core"] > 0.35 and z["R"] - z["rc"] > 20 and z["band"] < 0.15 and live > 0.05:
        out.append(dict(c, s=stats, live=round(live, 3)))
json.dump(out, open(f"s2_{k}.json", "w")); print(k, len(cands), len(out))
