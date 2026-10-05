# Improvement log

One entry per cycle (see IMPROVE.md). Newest at the bottom. Severity: bug / gap / tidy.

## Cycle 1: 2026-10-05 (night, full)

| # | Severity | Finding | Fix | Status |
|---|----------|---------|-----|--------|
| 1 | bug | `sophia_scan.sh` and `make_listing.sh` in Downloads were only safe from being moved because of the 7-day rule. Next week Hypatia could file them away, breaking the owner's scan command. | Rule in `sophia.py`: Sophia's own scripts and undo files are always left alone. Tested. | fixed |
| 2 | bug | All three cleanup scripts were named `organize.sh`. Downloading a second (or an updated) one saves as `organize (1).sh`, so the owner's command would run the old script. | Scripts are now `organize_<Folder>.sh` and print their plan date first. STATUS, docs, and the Crew Board updated. | fixed |
| 3 | gap | Is deleting Ableton `.alp` files safe after installing? | Yes: they're installers; installed content lives in Ableton's library, and packs can be re-downloaded from the Ableton account. Sources: [Ableton help](https://help.ableton.com/hc/en-us/articles/115001930644-Installing-Live-Packs), [Ableton forum](https://forum.ableton.com/viewtopic.php?t=227028). | noted on board |
| 4 | gap | My memory said Claude desktop was "maybe never" possible on this Mac. | Anthropic's help page: Claude Desktop needs **macOS 11 (Big Sur) or higher**; the owner has 12.7.6. It should be possible. Owner's notes say it "won't install", so ask what happened. Source: [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop). | question on board |
| 5 | tidy | CLAUDE.md "Current goal" still said "get the agent running" (done). | Updated to the real goal. | fixed |
| 6 | tidy | Every run log entry says "What I'll change next time: _(fill this in)_"; nobody fills it. | Open: decide whether the cycle fills it, or drop the line. | open |
| 7 | gap | Hypatia's log shows only the retry's turn count after a retry (cost is totaled correctly). | Small; fix in a later cycle. | open |
| 8 | gap | `sophia_scan.sh` sizes `~/Library` twice (once inside the home scan). Slow on an old Mac, not wrong. | Later: one `du` pass. | open |
| 9 | gap | Ableton Factory Pack names aren't in the scan, so I can't confirm which `.alp` packs are installed automatically. | Later: add a pack list to the scan. | open |
