# Search Life-like rules (single-cell seed) for self-similar growth. Scores:
#  dim: box-counting dimension of the gen-64 pattern (fractal if clearly between 1 and 2, good straight-line fit)
#  self: overlap of gen-64 shrunk by 2 with gen-32 (self-similar growth doubles itself)
import numpy as np, itertools, random, json
N=161; C=N//2
def run(B,S,gens):
    g=np.zeros((N,N),np.uint8); g[C,C]=1; out={}
    for t in range(1,gens+1):
        n=sum(np.roll(np.roll(g,dr,0),dc,1) for dr in (-1,0,1) for dc in (-1,0,1) if dr or dc)
        g=(np.isin(n,B)&(g==0)|np.isin(n,S)&(g==1)).astype(np.uint8)
        if g[0].any() or g[-1].any() or g[:,0].any() or g[:,-1].any(): return None
        if t in (16,32,64): out[t]=g.copy()
    return out
def boxdim(g):
    ys,xs=np.nonzero(g)
    if len(ys)<50: return None,0
    sizes=[1,2,4,8,16]; counts=[]
    for s in sizes:
        counts.append(len(set(zip(ys//s,xs//s))))
    x=np.log(1/np.array(sizes)); y=np.log(counts); a,b=np.polyfit(x,y,1); r=np.corrcoef(x,y)[0,1]**2
    return a,r
def shrink(g):
    h=g[C-64:C+64,C-64:C+64]; return h.reshape(64,2,64,2).max(axis=(1,3))
def selfsim(o):
    a=shrink(o[64]); b=o[32][C-32:C+32,C-32:C+32]
    inter=(a&b).sum(); uni=(a|b).sum(); return inter/uni if uni else 0
random.seed(11); res=[]
known={"1/1":"Gnarl","1357/1357":"Fredkin's Replicator","1/012345678":"H-trees"}
rules=set()
while len(rules)<2500:
    B=[1]+[k for k in range(2,9) if random.random()<.3]; S=[k for k in range(0,9) if random.random()<.4]
    rules.add((tuple(B),tuple(S)))
for B,S in list(rules)+[((1,),(1,)),((1,3,5,7),(1,3,5,7))]:
    o=run(list(B),list(S),64)
    if not o: continue
    d,r=boxdim(o[64])
    if d is None: continue
    ss=selfsim(o)
    res.append(dict(rule="B%s/S%s"%("".join(map(str,B)),"".join(map(str,S))),dim=round(d,3),fit=round(r,4),selfsim=round(ss,3),alive=int(o[64].sum())))
res=[x for x in res if 1.2<x["dim"]<1.85 and x["fit"]>0.995]
res.sort(key=lambda x:-x["selfsim"])
for x in res[:15]: print(x)
json.dump(res,open("results.json","w"))
print(len(res),"fractal candidates")
