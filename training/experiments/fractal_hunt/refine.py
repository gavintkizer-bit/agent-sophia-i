import json, numpy as np, sys
sys.argv=[sys.argv[0]]; exec(open("hunt.py").read().split("rules = set()")[0])
def local_slopes(g):
    ys, xs = np.nonzero(g); y0, x0 = ys.min(), xs.min(); h, w = ys.max()-y0+1, xs.max()-x0+1; L = 1
    while L < max(h, w): L *= 2
    sub = np.zeros((L, L), np.uint8); sub[:h, :w] = g[y0:y0+h, x0:x0+w]; cs = []; k = 1
    while k <= L // 4: cs.append(sub.reshape(L//k, k, L//k, k).max(axis=(1, 3)).sum()); k *= 2
    return [float(np.log2(cs[i]/cs[i+1])) for i in range(len(cs)-1)]
def rulearr(rule):
    bs, ss = rule[1:].split("/S"); b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[[int(x) for x in bs]] = 1
    if ss: s[[int(x) for x in ss]] = 1
    return b, s
F = json.load(open("found_1.json")); keep = []
for f in F:
    b, s = rulearr(f["rule"]); out = run(place([tuple(x) for x in f["seed"]]), b, s, {16, 32, 64})
    sl = local_slopes(out[64]); sl32 = local_slopes(out[32])
    spread = max(sl) - min(sl)
    # time self-similarity: gen 64 shrunk by 2 vs gen 32 (both centered on the seed)
    a = out[64][R//2-64:R//2+64, C//2-64:C//2+64].reshape(64, 2, 64, 2).max(axis=(1, 3)); bb = out[32][R//2-32:R//2+32, C//2-32:C//2+32]
    ss = (a & bb).sum() / max(1, (a | bb).sum())
    f.update(slopes=[round(x, 2) for x in sl], spread=round(spread, 2), selfsim=round(float(ss), 3), slopes32=[round(x, 2) for x in sl32])
    if spread < 0.35: keep.append(f)
keep.sort(key=lambda f: f["spread"])
print(len(F), "->", len(keep))
for f in keep[:15]: print(f["rule"], f["seed"], "dim", f["dim"], "slopes", f["slopes"], "s32", f["slopes32"], "selfsim", f["selfsim"], "nonlin", f["nonlin"], "sens", f["sens"], "fill", f["fill"])
json.dump(keep, open("keep.json", "w"), indent=1)
