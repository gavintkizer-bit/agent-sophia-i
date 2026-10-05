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
| 6 | tidy | Every run log entry says "What I'll change next time: _(fill this in)_"; nobody fills it. | Dropped the line from new entries; lessons go in this log and SOPHIA.md instead. | fixed (cycle 2) |
| 7 | gap | Hypatia's log shows only the retry's turn count after a retry (cost is totaled correctly). | Turns are now totaled across the retry too. | fixed (cycle 2) |
| 8 | gap | `sophia_scan.sh` sizes `~/Library` twice (once inside the home scan). Slow on an old Mac, not wrong. | Later: one `du` pass. | open |
| 9 | gap | Ableton Factory Pack names aren't in the scan, so I can't confirm which `.alp` packs are installed automatically. | Later: add a pack list to the scan. | open |

## Cycle 2: 2026-10-05 (daily check-in, light)

- No uploads and no new requests on the board. Marked my two finished board requests done with replies.
- Fixed #6 and #7 above in `agent.py`; setup check still READY. No paid runs needed.
- Owner's board: nothing ticked yet (they were asleep). Their list carries over as is.
- Still open: #8 (scan reads ~/Library twice), #9 (Ableton pack names in the scan). Next full cycle: weekly.

## Research: Claude Desktop on the owner's Mac (2026-10-05, owner asked)

Mac: 2016 MacBook Pro, Intel, macOS 12.7.6 Monterey.

| Piece | Official requirement | On this Mac | Source |
|---|---|---|---|
| Desktop app (Chat) | macOS 11+; universal build for Intel and Apple Silicon | should work | [support: install](https://support.claude.com/en/articles/10065433-install-claude-desktop), [docs: desktop](https://code.claude.com/docs/en/desktop) |
| Code tab, **Cloud** sessions | runs in the cloud (like claude.ai/code now) | likely works; not confirmed | [docs: desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart) |
| Code tab, **Local** sessions | runs Claude Code on the Mac; Claude Code needs macOS 13+ | probably not on 12.7.6 (inferred; docs don't state the desktop limit) | [docs: setup](https://code.claude.com/docs/en/setup) |
| Cowork | official pages don't say; blogs say Apple Silicon only | unknown, likely no | blogs only |

Decision: owner chose to stay with the current cloud setup (2026-10-05). Closed.

## Cycle 3: 2026-10-05 (owner rule: no Ableton files or samples)

| # | Severity | Finding | Fix | Status |
|---|----------|---------|-----|--------|
| 10 | bug | The Downloads plan moved all 22 `.alp` Ableton packs (to the review folder) and `WA_IBG_Vocal_Chain.zip`. | `.alp` added to PROTECTED; archives with music words protected. | fixed |
| 11 | bug | `VIBES MASTER.als 2` (an Ableton project with a copy mark after the extension) was headed for Duplicates. | Protection ignores trailing copy marks (" 2", " (1)"). | fixed |
| 12 | gap | Music plugin/driver installers (Splice, Voxengo, DC1A3, Behringer, M-Audio...) were in the Trash group; old free ones may not be re-downloadable. | Protected as music gear. | fixed |

Result: Downloads script 512 moves, 0 warnings, no protected file in it (checked against the script itself).
