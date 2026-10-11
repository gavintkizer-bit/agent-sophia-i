# Experiment W1: Creek to river, where does the signal stop?

Water and AI thread (goals.md). The question and the guess are Gavin's; the hydrology is his.
I pull and clean the data, Cal looks up what's already published, and Gavin reads the data,
checks it in the field, and judges. Status: **step 2 first look done 2026-10-11; waiting on Gavin's reading of the numbers.**

## 1. Question
A creek's health reflects the health of the river it feeds, but other factors count too.
**How far does that hold, and where does the line break?**

The first round uses flow, because USGS gauges measure it every day:
- Does daily flow at a creek track flow in its parent river downstream?
- How does that change with how big the creek is (its share of the river's drainage area), with the
  season (snowmelt vs. rain), and with baseflow days vs. storm days?
- Later rounds: the health measures some gauges also record (temperature, conductance, turbidity,
  dissolved oxygen), and the water table (wells).

## 2. Guess (written BEFORE we look at any data)
**Gavin, 2026-10-11, his words:** "My guess is that the boundary, or the difference, is runoff among other
things (how much sediment is carried, where sediment is being removed and where it is building and what
formations does it make)."

Turned into predictions the data could prove wrong (my wording; he corrects):
- **P1, runoff:** on baseflow days the creek tracks its river closely; on runoff (storm) days the link
  weakens, and more so as runoff grows.
- **P2, sediment carried:** where the creek's sediment load differs from the river's (suspended sediment,
  turbidity), the flow link is weaker too; the gap widens with runoff.
- **P3, erosion and deposition:** the line shows on the ground, where sediment is removed or builds up
  (bars, deltas and fans at the confluence). Field and imagery, his eye.

## 3. Test (built so it could prove the guess wrong)
- **Pairs:** creek gauges and the river gauge downstream of each, all USGS daily discharge.
  - Charlotte candidates: Mallard and Reedy creeks with the Rocky River; McDowell and Long creeks with the
    Catawba (careful: the Catawba is dammed).
  - Summit County candidates: Tenmile Creek, Snake River and Keystone Gulch with the Blue River; Blue River
    at Blue River vs. near Dillon. Dillon Reservoir and the Hoosier Pass diversions change the flow.
  - Step 1 (mine) checks each pair's years of overlapping record before we use it.
- **Fair comparison (the control):** shared rain makes neighboring streams rise together even when they
  aren't connected. So each creek is also compared with a river it does NOT feed, in a neighboring basin.
  The connection is real only where the link to its own river beats the link to the stranger.
- **Measures:** correlation of daily flow (log scale), by season, and on baseflow vs. storm days.
  Dams and diversions are flagged, not hidden: where they break the link is part of the answer.
- **Sediment data (checked 2026-10-11, USGS):** suspended sediment samples exist at Mallard Creek, a Reedy Creek
  tributary and the Catawba at NC 73 (Charlotte), and at Indiana Creek above its mouth, French Gulch at
  Breckenridge, the Blue River at Blue River and near Dillon, the Snake River and Tenmile Creek (Summit County).
  These are samples, not daily records: step 1 counts how many each has. Continuous turbidity: only the Blue River
  below Green Mountain Reservoir.
- **Formations (P3):** photos and notes at confluences on his walks, plus aerial imagery over the years.
- **Field check (Gavin):** measure a Charlotte creek's outflow by hand two days after a moderate rain, and
  compare with the USGS gauge at the same time. USGS reports cubic feet per second; I convert
  (1 cfs = 0.0283168 m³/s).
- **Judges:** code computes the numbers; Gavin reads them for patterns and discrepancies.

### Step 1 results (2026-10-11, USGS series catalog; counts are what USGS lists, checked by code)
**Flow is rich; sediment is thin.** A correction to the sediment line above: an earlier query of mine counted every
measurement as sediment. Real suspended-sediment (SSC) samples:
- Charlotte: McMullen Cr 43 (1977-2014), McAlpine Cr below McMullen 27 (1977-79), McAlpine at Sardis Rd 19 (1977-79),
  Little Sugar at Archdale 25 (1978-79), Irwin Cr 23 (1977-79), Long Cr 31 (1977-82), Goose Cr 10 (2014).
- Summit County: French Gulch 95 (1995-99), Blue R near Dillon 45 (1996-98), Snake R 3, Blue R at Blue River 2.
  Indiana Creek: only 12 samples and 66 days of flow, all 2005 (too thin; dropped).
- So P2 can only be tested in two windows: **1977-79 in Charlotte** (McMullen Cr and McAlpine below McMullen are a
  sampled creek-river pair) and **1996-98 in Summit County** (French Gulch and the Blue near Dillon).

**Pairs chosen (all USGS daily discharge):**
| Creek | Feeds | Daily flow since | Notes |
|---|---|---|---|
| McMullen Cr (02146700) | McAlpine Cr below McMullen (02146750) | 1962 / 1974 | McAlpine at Sardis Rd (02146600) is above the junction |
| Irwin Cr (02146300) | Sugar Cr at NC 51 (02146381) | 1962 / 1994 | |
| Little Sugar at Archdale (02146507) | Little Sugar at Pineville (02146530) | 1977 / 1997 | same creek, downstream |
| Blue R at Blue River (09046490) | Blue R near Dillon (09046600) | 1983 / 1957 | French Gulch (09046530, 1995-2005) joins between |

**Controls (a river the creek does NOT feed):** Goose Cr (0212467595, Rocky River basin, 2002-) and Long Cr
(02142900, a Catawba tributary, 1965-) for Charlotte; Snake R near Montezuma (09047500) or Tenmile Cr at Frisco
(09050100) for the Blue, since both flow to Dillon Reservoir by other valleys.
- Charlotte's creeks are urban, so runoff from pavement is strong there: a good place for P1. Summit County is
  snowmelt-driven: the melt-thaw side of his question.

## 4. Before the test
- Cal: what's already published on tributary-to-main-stem flow links, sediment at confluences, stream network scaling, and
  baseflow (so we build on it and find the gap). Small budget; I verify every claim.

## 5. Results
### Step 2, first look (2026-10-11): flow only, 2000-2025, code-computed
Data and code: `training/experiments/w1_data/` (USGS daily discharge CSVs; `step2_download.py`, `step2_analyze.py`;
output in `step2_results.txt`). Pearson r of log daily flow; baseflow vs storm days split by the creek's baseflow
share (Lyne-Hollick filter, alpha 0.925: baseflow day >= 80% baseflow, storm day <= 50%).

| Creek -> its river (stranger) | All days own / stranger | Baseflow days | Storm days | Day-to-day change |
|---|---|---|---|---|
| McMullen -> McAlpine (Goose) | 0.84 / 0.75 | 0.84 / 0.76 | 0.84 / 0.74 | 0.69 / 0.69 |
| Irwin -> Sugar (Goose) | 0.91 / 0.75 | 0.87 / 0.74 | 0.84 / 0.69 | 0.80 / 0.72 |
| Little Sugar Archdale -> Pineville (Long Cr) | 0.97 / 0.78 | 0.92 / 0.75 | 0.93 / 0.67 | 0.95 / 0.79 |
| Blue at Blue River -> near Dillon (Tenmile) | 0.91 / 0.80 | 0.90 / 0.76 | 0.89 / 0.82 | 0.55 / 0.34 |

**What it seems to say (for Gavin to judge):**
- The connection is real: every creek tracks its own river better than the stranger, by 0.07 to 0.19.
- **P1 as I worded it isn't supported.** On storm days the own-river link barely moves (0.84 to 0.84, 0.87 to 0.84,
  0.92 to 0.93). What drops on storm days is the match with the *stranger*, so storms make the real connection stand
  out more, not less.
- **A possible line:** McMullen to McAlpine is no more linked than McMullen to a stranger in day-to-day changes
  (0.69 / 0.69). At the scale of single storms, shared rain explains as much as the channel does there.
- In Summit County the stranger gap is widest outside May-July (0.84 / 0.60), when snowmelt isn't driving every
  stream at once.

**Limits:** correlation, not cause. Seasonal cycles inflate level correlations (the stranger control is there for
that). One stranger per pair. Urban Charlotte creeks may not behave like rural ones. My P1 wording may not be what
Gavin meant by "runoff": his guess may be about what runoff carries (sediment), which is P2, and P2 can only be
tested in 1977-79 (Charlotte) and 1996-98 (Summit County).

## 6. What we learned, and the next question
(none yet)
