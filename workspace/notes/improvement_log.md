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

## Research: Claude Desktop (2026-10-05)
App should run on macOS 12, Local Code sessions probably not; owner chose cloud sessions. Closed.

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

## 2026-10-06 (00:50): first music round
- upload hit GitHub's 25 MB web limit (music_refs.txt was 23.5 MB + others): zip fixed it. Keep scans zipped;
  processed/ keeps only the zip of big files.
- music map: 1,368 Ableton files read, 151,385 sample links, 38,534 files in Downloads+Desktop.
- new `music_plan.py`: a music file moves only if no project names it (path OR bare name, since Live 10
  stores names only), into a new ~/Music/Sound Library (fence allows only that inside ~/Music); folders move
  whole. Second, independent check (substring search of all links) agreed: 0 of 196 loose sounds named.
  It flagged "Drum samples" (a Factory Pack folder of the same name): false alarm, verified.
- sandbox_test.sh now fails if music moves anywhere except Sound Library, or touches Music/Ableton; I
  confirmed it catches both on fake lines.
- Not moved, on purpose: sample packs with any used file (673 Samples, Samples 1+2, lo-fi, TriSamples,
  ProducerSpot), project folders, .als/.alp/devices, videos, plugin/driver folders.
- result (after round): Sound Library 1.5 GB; Downloads loose 780 -> 530; music_files 38.5k -> 20.2k; free 55.3 GB.
  Processed scans keep only the zip (big text files stay out of git).

## 2026-10-06 (01:50): prep for tomorrow
- music homes: fence allows ~/Music/{Sound Library,Projects,Bounces,Archive} only (new folders; Ableton and
  Apple Music folders still refused). sandbox_test.sh updated to match.
- scan: projects.txt (last-saved date of every .als, no backups) for the archive; the scan now zips itself
  (old zip to Trash) and sophia.py unpacks sophia_scan.zip from inbox/ or workspace/.
- tomorrow's script: 2 checked moves (Grandpa's Familiar folder -> Music/Projects/2026; unused Void Speech.wav
  bounce -> Music/Bounces). Sandbox pass. Owner checks Void Speech plays from its new home.

## Cycle 4: 2026-10-06 (night, full): Cal's Sonnet audit of me + nightly cleanup

Fixed tonight (details: workspace/archive/for_sophia.md, audits/2026-10-06-repo-*.md): 14 helpers
findings, 12 mind findings, `safety_test.py` (found an unprotected Serum installer), `--dry` to scratch.
Cleanup: legacy one-folder tools removed, old scans pruned to the newest two, memory 130 -> 82 lines.

| # | Severity | Open item | Next step | Status |
|---|----------|-----------|-----------|--------|
| 8 | gap | Scan sizes ~/Library twice (slow) | one `du` pass | open |
| 9 | gap | Ableton Factory Pack names not in the scan | add a pack list | open |
| 14 | gap | `sophia.py` doesn't run sandbox_test.sh itself (mind-6) | gate organize_all.sh on a pass | open (2026-10-07) |
| 15 | gap | No report-writing drill (the .alp mistake) (mind-7) | write the drill | open |
| 16 | gap | Constitution change isn't shown at boot (mind-8) | boot hook warning: red, owner decides | open (ask) |
| 17 | gap | Repo audit "mac" part not done | re-run on the chosen model | open (2026-10-07) |

## Daily check-in 2026-10-06 (Tuesday, quiet)

- No uploads, requests, ticks, or answers since last night. Owner's list for today is already on the board.
- Reviewed Cal's 3 unreviewed proposals (band-finding research): rejected, since the owner called band research "superficial".
- No helper runs, no code changes.

## 2026-10-07: computer cleanup project closed (owner)
- Final: 18.0 GB free to about 55 GB; 995 items placed; undo files on the Mac.
- Closed without fixing (no longer needed): #8 (scan reads ~/Library twice), #9 (Ableton pack names in the
  scan; the scan no longer reads music at all), the report-writing drill for Hypatia's disk report.

## 2026-10-07 (light): two sources from the owner
- Measured: Hypatia math_catalog PASS ($0.04); Cal archive_index PASS ($0.02). Cal's full-index rewrite FAILED
  in real use (mislabeled the note), so I rejected it.
- One change: Cal indexes one row at a time. My thread gains *named obstacles* and *dead ends, and why*.

## 2026-10-07 (light): Cal's issues, #4
- Measured: Cal's reflect run passed after one retry ($0.11); his quote drills afterward 3/3 PASS ($0.06).
- One change: verify_quote explains a NOT FOUND (closest text, nothing close, or no readable text).

## 2026-10-08 (light): Cal's issues, #2
- Measured: safety 43/43 (2 new checks); Cal's archive_index and archive_labels 2/2 PASS ($0.05).
- One change: Cal can't Write over a file that already existed; he Edits one part or proposes a rewrite.

## 2026-10-08 (light, daily check-in): Cal's issue #3
- Measured: Cal's taxes run (10-08) hit a 403 and kept retrying the blocked page; the Wayback Machine is unreachable here.
- One change: verify_quote's fetch error now says not to retry blocked sites and to find an official source.
  Re-drilled: archive_quotes and archive_labels 2/2 PASS ($0.06).

## 2026-10-09 (light, daily check-in): check my own "[To verify]" before it matters
- Measured: the Colorado plan carried two unverified claims. codot.gov showed one was WRONG for his car: a 2WD car
  needs chains or an approved device under the Traction Law; good tires only count on AWD/4WD (rule updated Fall 2025).
- One change: the plan and the board note now say so, with verified quotes. The DMV deadline stays marked (site blocked).
- Lesson: a "[To verify]" tag is a debt. Pay it before the owner acts on the plan, not after.

## 2026-10-10 (light): Cal's duplicate notes, and a missed meeting prep
- Measured: Cal wrote duplicate research notes on 10-07, 10-08 and 10-10. Now the code refuses a second note in one
  research run (he's asked to merge and empty it; the code removes emptied extras). archive_quotes still PASS.
- Missed: the 10-09 nightly prep was cut off by a worker restart before it wrote the board; I then wrongly treated
  the turn as finished. Next time after a restart: check whether the task's output exists before standing down.

## 2026-10-10 (light, daily check-in): restarts
- One change: AUTONOMY.md now says what to do after a worker restart: check the last task's output exists before
  standing down; finish it if it still matters, else say so and log it.

## 2026-10-11 (light): Cal's budget cap didn't hold
- Found: a $0.40-capped research run cost $0.79. The SDK checks the cap between turns, so one heavy turn (a fetched
  PDF) can blow past it; the retry then got its $0.05 floor on top. Cal also wrote a made-up cost ($0.29) and time into his note.
- Open: make the cap hold (e.g. stop fetching PDFs whole, or a lower turn cap for research); add a drill that rejects
  any cost or time claim in his notes. Not changed tonight: it's a helper change, so it gets a drill first.

## 2026-10-11 (light, Sunday check-in): Sailor's Delight and the cap
- Board asks done: walkthrough, speed (live), brief-first (preview). Weekly mask in the journal.
- One change: the site check can stub the forecast, labelled, when Open-Meteo's shared daily limit is spent.

## 2026-10-13 (light, daily check-in): quiet
- No uploads, no waiting requests. Today's real cycle already happened in the home chat: the Life Lab freeze fixed with a
  self-test row (worker matches page), a rule trap fixed (warning plus switch-back), and a new habit, "look first, then measure".
- Open (small, not urgent): Show for a rule1d number draws on the board's width, while the test ran 101 cells wide;
  the picture can differ slightly from what was scored. Fix when Life Lab next changes.

## 2026-10-14 (light, daily check-in): quiet; one small fix
- No uploads, no waiting requests, no new ticks. Fixed yesterday's open item: Show for a one-row rule now uses the same
  101-cell wrapping row the test scored (live as Life Lab v12; self-test 13/13, no sideways scroll at 390 px).
