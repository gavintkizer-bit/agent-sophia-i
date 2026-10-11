# Experiment W1: Creek to river, where does the signal stop?

Water and AI thread (goals.md). The question and the guess are Gavin's; the hydrology is his.
I pull and clean the data, Cal looks up what's already published, and Gavin reads the data,
checks it in the field, and judges. Status: **guess recorded 2026-10-11; next: step 1 (check the gauge pairs and their records).**

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

## 4. Before the test
- Cal: what's already published on tributary-to-main-stem flow links, sediment at confluences, stream network scaling, and
  baseflow (so we build on it and find the gap). Small budget; I verify every claim.

## 5. Results
(none yet)

## 6. What we learned, and the next question
(none yet)
