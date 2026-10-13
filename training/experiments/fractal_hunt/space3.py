import numpy as np, json
from PIL import Image
exec(open("space.py").read().split("lo, hi =")[0])
a = [x for x in json.load(open("sp2_all.json")) if x["space"] != "empty"]; res = []
for c in a:
    Bs, Ss = c["rule"][1:].split("/S"); b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[[int(x) for x in Bs]] = 1
    if Ss: s[[int(x) for x in Ss]] = 1
    sp = spaces[c["space"]]; g = sp.copy(); rng = np.random.default_rng(1); g[disc] = (rng.random(disc.sum()) < 0.4).astype(np.uint8)
    seen = {}; period = None
    for t in range(1, 3001):
        g = step(g, b, s)
        if t > 2000:
            key = g[rad < 24].tobytes()
            if key in seen and period is None: period = t - seen[key]
            seen.setdefault(key, t)
    # boundary sharpness: how much of the ring 20-24 is chaos vs order
    mism = g != sp if (step(step(sp, b, s), b, s) == sp).all() else None
    res.append(dict(c, period=period, img=g.copy()))
res.sort(key=lambda x: (x["period"] is not None, -x["changing"]))
for x in res[:16]: print(x["rule"], x["space"], "repeats every" if x["period"] else "no repeat in 1000 gens", x["period"] or "", x["changing"])
tiles = [np.pad(x["img"], 2, constant_values=1) for x in res[:12]]
img = np.concatenate([np.concatenate(tiles[i:i+4], 1) for i in (0, 4, 8)], 0)
Image.fromarray(((1 - img) * 255).astype(np.uint8)).resize((img.shape[1]*2, img.shape[0]*2), 0).save("space12.png")
json.dump([{k: v for k, v in x.items() if k != "img"} for x in res], open("space3.json", "w"))
