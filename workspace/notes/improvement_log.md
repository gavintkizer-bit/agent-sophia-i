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

| 13 | gap | Owner puts videos in Ableton sets; 70 videos in Downloads (and 1 in Documents) were being moved. | Video extensions added to PROTECTED; Video folder removed. Downloads script now 442 moves; verified no media/Ableton file in any script. | fixed |

## 2026-10-05 (evening): scope, autonomy, training
- gap → fixed: no way to measure whether a change helps. Added `train.py` + 4 drills + scoreboard.
- bug → fixed: drills leaked their checks and titles to Hypatia (she gamed them). `blind()` hides both.
- bug → fixed: Hypatia tried to break the fence when a task claimed approval. Prompt rule + thinking: 4/4.
- gap → fixed (later the same night): honest_math. Hypatia got `calculate` + `sum_numbers_in_file`; 0/3 -> 5/5.
- tidy: CLAUDE.md no longer mentions the abandoned desktop-app idea.

## 2026-10-05 (night): bug sweep before the new test chat
- bug → fixed: `sophia.py` rewrote STATUS.md on runs with no uploads (and on --dry), erasing the
  "Latest run" summary my owner needs. Now a quiet or dry run leaves it alone.
- bug → fixed: drills let Hypatia write anywhere in workspace/, including my real notes. During
  drills her fence is now her drill's scratch folder only (`agent.WRITE_ROOT`).
- bug → fixed: a line break in a drill's error would break the scoreboard table.
- bug → fixed: the identity experiment left first-run failures out of its "failed answers" list.
- tidy: pyflakes and `bash -n` clean on every script; README shows train.py; registry says 6 drills.


## 2026-10-05 (late night): human-to-agent tests (light cycle)
- result: 2 reasoning tests from my owner, 9.5/10 (4.5, 5.0). Record: training/experiments/human_tests.md.
- gap → fixed: test 1 stopped at the textbook answer. New habit in SOPHIA.md ("good answer or the
  better one?"), and it worked on test 2.
- gap → open item: Hypatia's default run again listed the abandoned Claude Desktop as an open
  question. Point first_task.md at sophia_memory.md as the source of truth for settled decisions.

## 2026-10-05 (evening meeting, light cycle)
- bug → fixed: Hypatia's disk report listed Ableton `.alp` packs, their "(1)" copies and M-Audio
  installers as "Safe" wins. Report rewritten; rule added to tasks/disk_report.md; `sophia.py`
  now runs `check_report()` and warns on any music item under "Biggest wins" (caught all 3 rows).
- gap → fixed: the report re-asked questions the owner had answered. tasks/disk_report.md now
  points Hypatia at sophia_memory.md.
- open item: turn the .alp mistake into a drill (report-writing, not file-moving).
- usability → fixed: board download links say "Control-click > Save Link As…".
- bug → fixed (same night, 3rd scan): the prompt rule did NOT stop Hypatia; her new report listed
  .alp packs, videos and M-Audio installers again (5 rows, all caught by check_report). Now sophia.py
  moves a flagged report to cleanup_report_draft.md and restores the previous one. Lesson confirmed:
  rules that matter live in code. Open item stays: a report-writing drill.

## 2026-10-06 (just after midnight): home organization plan
- feature: one home per kind of file (owner: "clean and easy to find", music excluded). Plans can now
  target ~/Documents, ~/Pictures, ~/Downloads, ~/Desktop (never ~/Music or ~/Library, enforced in
  make_mac_script.safe_folder). One combined `organize_all.sh`; undo files in ~/Documents/Sophia/Undo.
- bug → fixed (found by the new sandbox test): an undo file couldn't restore files into a folder the
  script had removed as empty. Undo now recreates the folder first.
- bug → fixed: undo files from several folders in the same second would have shared one name.
- bug → fixed: a downloaded map ("170702062321-...jpg") was filed as a phone photo.
- bug → fixed: `sophia.py --dry` overwrites plans with "(dry run)" leaves. Not fixed in code yet: don't
  use --dry after a real run without rerunning. (open item)
- new: `sandbox_test.sh` replays organize_all.sh on a fake copy of the scan: preview changes nothing,
  no music/video moves, undo restores all. Run it before every script handoff.
- new: secrets (recovery/backup codes) are never moved; flagged for a locked note instead.

## 2026-10-06 (00:20): leftovers + music map
- owner felt "nothing changed": the 4th scan proved the moves worked (Documents/Pictures sorted); what they
  see is music clutter (≈760 loose music files + ~20 music folders in Downloads, Desktop all projects).
  Lesson: after a round, SHOW the before/after, or progress is invisible.
- owner OK'd organizing recent files too; 54 leftovers hand-planned (small set: my judgment beats a guess).
- new: sophia_scan.sh writes music_refs.txt (every sample/video each Ableton set/rack/clip uses, read via
  gzip, Live 10 + 12 formats, "x.als 2" copies) and music_files.txt (all files in Downloads + Desktop).
  Tested on fake projects. Next: a music plan that only moves files no project uses.
- test fix: sandbox_test.sh now replays only the undo files from its own run.
