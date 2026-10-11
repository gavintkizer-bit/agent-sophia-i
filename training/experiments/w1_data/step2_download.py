# W1 step 2: daily flow, creek vs its own river vs a stranger river. Free USGS data, code-computed.
import urllib.request, csv, math, json, datetime, sys, os
OUT=sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
SITES=["02146700","02146750","02146300","02146381","02146507","02146530","0212467595","02142900","09046490","09046600","09047500","09050100"]
def daily(site, start="2000-01-01", end="2025-12-31"):
    url=f"https://waterservices.usgs.gov/nwis/dv/?format=json&sites={site}&parameterCd=00060&statCd=00003&startDT={start}&endDT={end}"
    j=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=120))
    v=j["value"]["timeSeries"][0]["values"][0]["value"]
    return {x["dateTime"][:10]: float(x["value"]) for x in v if x["value"] not in ("", "-999999") and float(x["value"])>=0}
data={}
for s in SITES:
    data[s]=daily(s); print(s,len(data[s]),file=sys.stderr)
    with open(os.path.join(OUT,f"{s}_daily_cfs_2000_2025.csv"),"w") as f:
        f.write("date,discharge_cfs\n"); [f.write(f"{d},{q}\n") for d,q in sorted(data[s].items())]

