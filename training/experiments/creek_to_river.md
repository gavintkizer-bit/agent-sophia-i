# Experiment W1: Creek to river, where does the signal stop?

Water and AI thread (goals.md). The question and the guess are Gavin's; the hydrology is his.
I pull and clean the data, Cal looks up what's already published, and Gavin reads the data,
checks it in the field, and judges. Status: **drafted 2026-10-11; waiting on his guess.**

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
_Gavin's to write. A few examples of the shape, to keep or throw out:_
- _The link weakens as the creek's share of the river's drainage area shrinks._
- _Baseflow days line up more closely than storm days (the water table ties them together)._
- _In Summit County the link is tightest during the spring melt and loosest in fall._

**His guess:** (blank)

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
- **Field check (Gavin):** measure a Charlotte creek's outflow by hand two days after a moderate rain, and
  compare with the USGS gauge at the same time. USGS reports cubic feet per second; I convert
  (1 cfs = 0.0283168 m³/s).
- **Judges:** code computes the numbers; Gavin reads them for patterns and discrepancies.

## 4. Before the test
- Cal: what's already published on tributary-to-main-stem flow links, stream network scaling, and
  baseflow (so we build on it and find the gap). Small budget; I verify every claim.

## 5. Results
(none yet)

## 6. What we learned, and the next question
(none yet)
