import numpy as np, json, sys
exec(open("space.py").read().split("lo, hi =")[0])
cands = json.load(open("sp_all.json")); k, K = int(sys.argv[1]), int(sys.argv[2]); out = []
for c in cands[k::K]:
    Bs, Ss = c["rule"][1:].split("/S"); b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[[int(x) for x in Bs]] = 1
    if Ss: s[[int(x) for x in Ss]] = 1
    sp = spaces[c["space"]]; g = sp.copy(); rng = np.random.default_rng(1); g[disc] = (rng.random(disc.sum()) < 0.4).astype(np.uint8)
    rcs = {}
    for t in range(1, 1201):
        g = step(g, b, s)
        if t in (200, 600, 1200):                       # even steps: a flipping space is back in its starting phase
            mism = g != sp; rr = rad[mism]
            rcs[t] = round(float(np.percentile(rr, 95)), 1) if len(rr) > 20 else 0.0
            if t == 1200: farok = float((~mism)[far].mean())
    h = step(step(g, b, s), b, s); changing = float((h != g)[rad < 12].mean())
    if farok > 0.98 and changing > 0.1 and rcs[1200] > 8 and rcs[1200] <= rcs[200] + 3:
        out.append(dict(c, far=round(farok, 3), changing=round(changing, 3), rc=rcs))
json.dump(out, open(f"sp2_{k}.json", "w")); print(k, len(out))
