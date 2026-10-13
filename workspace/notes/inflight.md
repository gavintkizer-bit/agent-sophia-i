# In flight (read first after any restart)

**Request:** Gavin, 2026-10-13 ~06:00 UTC: "I tried running a free test and it bricked the website on me" (Life Lab).
Likely cause: Experiment/Numbers runs compute synchronously in long blocks (200 numbers x 1000 gens), freezing the page on a phone.
- [ ] Reproduce: time Test 1 settings (1-200, 1000 gens) and measure the longest freeze
- [ ] Fix: faster step, yield every ~30 ms inside runs, Stop button, progress, time estimate before big runs
- [ ] Self-test 12/12; publish; PR; merge; ask him which button he pressed
