# W1 step 2 analysis. Pearson r on log10 daily flow, creek vs its own river and vs a stranger river,
# split by the creek's baseflow share (Lyne-Hollick filter, alpha 0.925, one forward pass).
import json, math
import os, glob
HERE=os.path.dirname(os.path.abspath(__file__))
F={}
for p in glob.glob(os.path.join(HERE,"*_daily_cfs_2000_2025.csv")):
    site=os.path.basename(p).split("_")[0]; F[site]={}
    for line in open(p).read().splitlines()[1:]:
        d,q=line.split(","); F[site][d]=float(q)
PAIRS=[("McMullen Cr","02146700","McAlpine bl McMullen","02146750","Goose Cr (Rocky R basin)","0212467595"),
       ("Irwin Cr","02146300","Sugar Cr at NC 51","02146381","Goose Cr (Rocky R basin)","0212467595"),
       ("Little Sugar at Archdale","02146507","Little Sugar at Pineville","02146530","Long Cr (Catawba)","02142900"),
       ("Blue R at Blue River","09046490","Blue R near Dillon","09046600","Tenmile Cr at Frisco","09050100")]
def r(a,b):
    n=len(a); ma=sum(a)/n; mb=sum(b)/n
    sab=sum((x-ma)*(y-mb) for x,y in zip(a,b)); sa=math.sqrt(sum((x-ma)**2 for x in a)); sb=math.sqrt(sum((y-mb)**2 for y in b))
    return sab/(sa*sb) if sa and sb else float("nan")
def bfi(series):  # dates sorted; returns {date: baseflow share}
    out={}; qf_prev=0; q_prev=None
    for d,q in series:
        if q_prev is None: qf=0
        else: qf=0.925*qf_prev+(1+0.925)/2*(q-q_prev); qf=max(0,min(qf,q))
        out[d]=(q-qf)/q if q>0 else 1.0; qf_prev=qf; q_prev=q
    return out
L=lambda q: math.log10(q+0.01)
rows=[]
for cn,c,rn,rv,xn,x in PAIRS:
    days=sorted(set(F[c])&set(F[rv])&set(F[x]))
    share=bfi(sorted(F[c].items()))
    def stats(sel):
        d=[t for t in days if sel(t)]
        if len(d)<60: return (float("nan"),float("nan"),len(d))
        a=[L(F[c][t]) for t in d]; return (r(a,[L(F[rv][t]) for t in d]), r(a,[L(F[x][t]) for t in d]), len(d))
    def chg(sel):  # day-to-day change in log flow
        d=[t for t in days if sel(t)]; ok=[(p,t) for p,t in zip(d,d[1:]) if (datetime_ok(p,t))]
        a=[L(F[c][t])-L(F[c][p]) for p,t in ok]
        return (r(a,[L(F[rv][t])-L(F[rv][p]) for p,t in ok]), r(a,[L(F[x][t])-L(F[x][p]) for p,t in ok]), len(ok))
    import datetime
    def datetime_ok(p,t): return (datetime.date.fromisoformat(t)-datetime.date.fromisoformat(p)).days==1
    allr=stats(lambda t:True); base=stats(lambda t:share.get(t,1)>=0.8); storm=stats(lambda t:share.get(t,1)<=0.5)
    ch=chg(lambda t:True)
    melt=stats(lambda t:t[5:7] in ("05","06","07")); rest=stats(lambda t:t[5:7] not in ("05","06","07"))
    rows.append(dict(creek=cn,river=rn,stranger=xn,days=allr[2],all=allr[:2],base=base,storm=storm,change=ch[:2],melt=melt,rest=rest))
f=lambda v:f"{v:.2f}"
print("Pearson r of log daily flow, 2000-2025 (own river / stranger river)")
for o in rows:
    print(f"\n{o['creek']} -> {o['river']}  (stranger: {o['stranger']}), {o['days']} shared days")
    print(f"  all days        own {f(o['all'][0])}  stranger {f(o['all'][1])}")
    print(f"  baseflow days   own {f(o['base'][0])}  stranger {f(o['base'][1])}  (n={o['base'][2]})")
    print(f"  storm days      own {f(o['storm'][0])}  stranger {f(o['storm'][1])}  (n={o['storm'][2]})")
    print(f"  day-to-day chg  own {f(o['change'][0])}  stranger {f(o['change'][1])}")
    print(f"  May-Jul         own {f(o['melt'][0])}  stranger {f(o['melt'][1])}   rest of year own {f(o['rest'][0])} stranger {f(o['rest'][1])}")

