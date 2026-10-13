# Fractal-with-surprises hunt: Life-like rules x small asymmetric seeds on Life Lab's 240 x 150 walled board.
import numpy as np, random, json, sys
R, C, T = 150, 240, 64
def step(g, b, s):
    p = np.pad(g, 1)
    n = sum(p[1+dr:R+1+dr, 1+dc:C+1+dc] for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
    return np.where(g == 1, s[n], b[n]).astype(np.uint8)
def run(g, b, s, times):
    out = {}; 
    for t in range(1, max(times)+1):
        g = step(g, b, s)
        if t in times: out[t] = g.copy()
    return out
def boxdim(g):
    ys, xs = np.nonzero(g)
    if len(ys) < 50: return 0, 0
    y0, x0 = ys.min(), xs.min(); h, w = ys.max()-y0+1, xs.max()-x0+1; L = 1
    while L < max(h, w): L *= 2
    sub = np.zeros((L, L), np.uint8); sub[:h, :w] = g[y0:y0+h, x0:x0+w]
    sizes, counts = [], []
    k = 1
    while k <= L // 4:
        m = sub.reshape(L//k, k, L//k, k).max(axis=(1, 3)); sizes.append(k); counts.append(m.sum()); k *= 2
    if len(sizes) < 4: return 0, 0
    x, y = np.log(1/np.array(sizes)), np.log(np.array(counts, float))
    a, c0 = np.polyfit(x, y, 1); r2 = 1 - ((y-(a*x+c0))**2).sum()/((y-y.mean())**2).sum()
    return a, r2
def place(cells):
    g = np.zeros((R, C), np.uint8)
    for r, c in cells: g[R//2 + r, C//2 + c] = 1
    return g
def sym(g):
    best = 0
    for f in (np.fliplr, np.flipud, lambda x: np.rot90(x, 2)):
        h = f(g); a = (g & h).sum(); u = (g | h).sum(); best = max(best, a/u if u else 1)
    return best
rules = set(); rnd = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
while len(rules) < int(sys.argv[2]) if len(sys.argv) > 2 else 1500:
    B = sorted(set(rnd.sample(range(1, 9), rnd.randint(1, 4))) | {rnd.choice([1, 2])}); S = sorted(rnd.sample(range(0, 9), rnd.randint(0, 5)))
    rules.add((tuple(B), tuple(S)))
found = []
for B, S in rules:
    b = np.zeros(9, np.uint8); s = np.zeros(9, np.uint8); b[list(B)] = 1; s[list(S)] = 1
    for trial in range(3):
        seed = sorted({(rnd.randint(-2, 2), rnd.randint(-2, 2)) for _ in range(rnd.randint(3, 6))})
        out = run(place(seed), b, s, {16, 32, 63, 64})
        g = out[64]; pop = g.sum(); ys, xs = np.nonzero(g)
        if pop < 300: continue
        if ys.min() == 0 or xs.min() == 0 or ys.max() == R-1 or xs.max() == C-1: continue
        area = (ys.max()-ys.min()+1)*(xs.max()-xs.min()+1); fill = pop/area
        if not 0.12 < fill < 0.55: continue
        dims = [boxdim(out[t]) for t in (16, 32, 64)]
        d64, r2 = dims[2]
        if not (1.35 < d64 < 1.8 and r2 > 0.99 and abs(dims[1][0]-d64) < 0.1): continue
        if sym(g) > 0.6: continue
        # unpredictability 1: superposition fails (not a linear "copy machine" like the Replicator)
        A, Bh = seed[:len(seed)//2], seed[len(seed)//2:]
        ga = run(place(A), b, s, {64})[64]; gb = run(place(Bh), b, s, {64})[64]
        nonlin = (g ^ ga ^ gb).sum() / max(1, pop)
        # unpredictability 2: move one seed cell by one step and see how much changes
        alt = list(seed); r0, c0 = alt[0]; alt[0] = (r0, c0 - 1) if (r0, c0 - 1) not in seed else (r0 - 1, c0)
        gs = run(place(alt), b, s, {64})[64]; sens = (g ^ gs).sum() / max(1, (g | gs).sum())
        # unpredictability 3: population doesn't grow on a smooth curve
        pops = []; h = place(seed)
        for t in range(64): h = step(h, b, s); pops.append(int(h.sum()))
        d2 = np.abs(np.diff(pops, 2)); rough = float(d2.mean() / max(1, np.mean(pops[-16:])) * 10)
        if nonlin < 0.3 or sens < 0.3: continue
        found.append(dict(rule=f"B{''.join(map(str,B))}/S{''.join(map(str,S))}", seed=seed, dim=round(float(d64), 3), r2=round(float(r2), 4),
            dim16=round(float(dims[0][0]), 3), dim32=round(float(dims[1][0]), 3), fill=round(float(fill), 3), sym=round(float(sym(g)), 3),
            nonlin=round(float(nonlin), 3), sens=round(float(sens), 3), rough=round(rough, 3), pop=int(pop)))
        break
found.sort(key=lambda f: -(f['nonlin'] + f['sens']) - (1 - abs(f['dim'] - 1.585)))
json.dump(found, open(f"found_{sys.argv[1] if len(sys.argv)>1 else 1}.json", "w"), indent=1)
print(len(rules), "rules;", len(found), "candidates")
for f in found[:12]: print(f)
