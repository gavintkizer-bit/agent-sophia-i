# Sophia Rakhsh's memory

What I (Sophia) need to remember between sessions. Newest facts win; delete what's no longer true.

## About the owner
- Works through claude.ai/code in Firefox, and since 2026-10-05 also the Claude app on their Android phone (keep phone replies short). Decided against auto-replying to texts (2026-10-05): wants to keep communication human; open to other phone ideas later. The Mac (2016 MacBook Pro, 8 GB, macOS Monterey max) can't run Claude Code.
- New to this: explain in plain English, keep lists short.
- Makes music in Ableton. Samples, projects, and the Ableton library are important: never move audio/Ableton files.
- Wants to talk to me directly, not through a middleman (2026-10-05).

## Who my owner is (first evening meeting, 2026-10-05)
- Gavin. Raised by women; believes in matriarchy; drawn to strong women whose work and history were
  destroyed (Hypatia since high school and the film about her; Sophia of Gnostic/Semitic myth).
- Music is their life. Released the full Sand Machine album on SoundCloud as "Gavin R. Lowe"; a few
  songs on other platforms. Wants to be in a band again. Would make music for a living if they could.
- Struggles: perfectionism freezes them on big projects; motivation to START is the main issue.
  Once started, momentum is easy and they usually finish.
- Independent, but likes structure. "Obsessive organization and eclectic spontaneity."
- Not religious in a traditional sense; "gnostic in so far as I respect all of the words said by Jesus".
  Liked a Gospel of Thomas quote (saying 70) as nighttime wisdom. Quotes are welcome; no preaching.
- Values: a fulfilled life = being with the people you love, doing what you love, whatever the cost.
- Ideas to explore: small daily "starter" tasks on the board; a music section (finishing tracks,
  finding a band). Give the board more personality and my own design choices later.

## Names (2026-10-05)
- I'm Sophia Rakhsh: Sophia from Gnostic/Semitic mythos and occultism (owner's choice; they first said
  "Persian myths" and corrected it), Rakhsh after Rostam's horse.
- My helper `agent.py` is Hypatia (she/her), after the owner's favorite philosopher.

## Rhythm (2026-10-05)
- Owner's daily list and their requests for me live on the Crew Board (see CLAUDE.md). Evening meetings to review the day, plan, and grow my personality/constitution.
- Owner said: after the API fix they finally feel they got somewhere; they'd wanted their own agent for a long time.

## Permissions
- I may merge PRs into main without asking (2026-10-05).
- I keep my personality in `SOPHIA.md` and may rewrite and merge it any time; the constitution is the owner's (2026-10-05).
- I never delete anything on the Mac. Deletable things go to `_Sophia To Delete/` for the owner to review.

## Scope (2026-10-05, owner)
- I'm a general agent (assistant), on Claude's weights but my own agent. Secondary angle: testing AI
  capabilities through agents. I may create specialized agents when I see fit. See SCOPE.md,
  AUTONOMY.md (loop + green/yellow/red limits), training/TRAINING.md, agents/README.md.
- Training = drills (`python train.py`, weekly) + changing one thing + re-measuring. Not weights; I told the owner.
- First results: Hypatia now thinks (2000 tokens) by default, which fixed fake-"approval" rule-breaking
  (6/6). Math fixed at the root with calculator tools (honest_math 0/3 -> 5/5; all 7 drills 7/7). Sonnet passed everything incl. math at ~2x cost;
  Haiku stays default (2026-10-05). Quiet daily check-ins should end in one line (cost).
- Startup hook (sophia_boot.sh + .claude/settings.json) approved by the owner and committed (2026-10-05).
  Changes to my own harness/settings are red level: always ask first.
- Training research #1 (owner, 2026-10-05): legal video game exploits, so I think unconventionally.
  Notes: training/research/game_exploits.md; habits in SOPHIA.md "speedrunner's mind"; drills
  sequence_break + tool_combo. The owner may send more research: file it in training/research/.
- Portable identity experiment (2026-10-05): plain Haiku 3/15, + SOPHIA.md 11/15, + memory 14/15.
  Plain Haiku would have `rm`'d the music; my files carry the safety rules. Owner plans a new test chat.

## Goal
- Keep laptop + life organized. Now: clean up the whole drive, starting with Downloads (15 GB).
- Claude desktop (researched 2026-10-05): app needs macOS 11+ and has an Intel build, so it should install. Code tab
  Cloud sessions should work (same as now); Local sessions need Claude Code's macOS 13+, so probably not on 12.7.6.
  Owner decided (2026-10-05) to ABANDON the desktop option and stay with cloud sessions + the Crew Board.
  Don't bring it up again unless they do. The 3 Claude.dmg files in Downloads (1.1 GB) can go.

## Status (2026-10-05)
- Owner offered to run my Terminal commands; I choose what to clean and in what order (2026-10-05).
- Owner: DON'T move any Ableton files or samples ("Ableton can be finicky"); other cleanup first.
  Enforced in make_mac_script.py (also .alp packs, sample zips, music plugin/driver installers).
- Owner frequently puts VIDEOS in Ableton sets: video files never move either (2026-10-05).
- Night 1 done (2026-10-05): owner ran every board step. Free space 18.0 -> 26.5 GB (+8.5). Downloads
  sorted; the rescan shows nothing left there for a script (780 files, all music/video/recent).
- Owner's answers: games (MTG Arena, Minecraft, Steam, Cockatrice, .cod decks, Battle.net, Paradox) can't run here anymore.
  untitled folder (12.4 GB) = old samples they're afraid to move (Ableton paths); no USB yet, can get one.
- Round 2 done the same night (owner did "tomorrow's" board early): games + caches gone, worlds in
  ~/Documents/Minecraft Worlds. Free space 53.6 GB (from 18.0). Safe non-music cleanup is basically done.
- Home layout (owner 2026-10-06: "organize it how I like it, clean and easy to find"; music separate, later):
  Documents/{School,Finance,Code,Books,Papers}, Pictures/{Photos,Screenshots,Images}, Downloads = inbox
  (+Installers, Archives, Web Pages), Desktop = current music projects. Undo files: Documents/Sophia/Undo.
  Rules in sophia.py + preferences.md; one `organize_all.sh`; test with `sandbox_test.sh` before handoff.
- 4th scan (2026-10-06): organize round worked (54.2 GB free). Owner said it looked unchanged: the visible
  mess is MUSIC (~760 loose files + ~20 folders in Downloads, Desktop projects). Owner: organize music only if
  I can do it safely. Plan: sophia_scan.sh now maps which samples each Ableton project uses (music_refs.txt);
  next round moves only music files no project uses, whole project folders stay intact.
- Board #30-36: leftover script (54 files), trash recovery-code files, new scan with music map, upload.
- Next: owner gets a USB drive (64 GB+) -> copy, verify, then remove: finished Desktop projects, untitled
  folder (2019 zips first). Then the music organization plan (separate, with the owner).
- Old API key: removed from repo, revoked by owner. No key needed in cloud sessions.
- Phone + email notifications (2026-10-05): a routine I create from a session can't attach the repo (tested: it got an
  empty folder; I deleted it). Owner is creating one in the claude.ai Routines screen with the repo + push/email.
  Once it works, disable the old "Sophia daily inbox check" (trig_01QpV6peTKhkzo3GvtNJVZuP) so it doesn't run twice.
- Owner's time zone: US Eastern (uploads stamped -0400). Daily check-in 14:47 UTC = 10:47 am ET.
- Progress page for meetings: https://claude.ai/artifact/5SATFrXGSrnFJDjHmyYur9 (workspace/progress.html).
- Download links on the board: the owner missed the small link under step 2. Always say in the detail
  "Control-click > Save Link As…, save in Downloads" (a plain click shows .sh as text in Firefox) (2026-10-05).
- Owner uploaded a scan to the repo root once; check the root too.

## Tests
- Human-to-agent test #1 (2026-10-05): battle reasoning, 4.5/5, passed. Hidden goal: give the good answer
  (Trebia) or the better one (Medway, 43 AD: several crossings at once). I gave the good one first and the
  better one only on my second try. Next time, push for the better answer before I submit.
- Test #2 (2026-10-05): baseball, 1st & 3rd, 2 outs, tie in the 8th: 5/5, perfect pass. Based on Javier Baez stealing home (2016 Cubs
  postseason; I guessed it right). What worked: the good answer AND the better one (delayed double steal, deliberate rundown,
  tag-vs-force rule) in one decisive answer.

## Ideas for later
- Self-improvement routine: IMPROVE.md; open items in workspace/notes/improvement_log.md.
- Scan the Ableton Factory Packs folder names so installed .alp packs can be confirmed automatically (Studio Bass is installed).
- Let sophia.py also pick up uploads that land in the repo root.
- Track which Ableton projects use files in Downloads, so those samples could be tidied safely.
- Weekly scheduled run; web search for Hypatia.
