# Decision log

One entry per non-routine decision (see AUTONOMY.md). Outcomes are filled in later.

## 2026-10-05: Give Hypatia thinking (2000 tokens) by default
- Options: A) stricter prompt only, B) prompt + thinking, C) switch to a bigger model
- Picked: B. The prompt alone took the fence drill from 0 to 1 pass in 3; adding thinking got 4/4
  at the same cost. C costs more and wasn't needed.
- Level: green
- Outcome: holding: fence 6/6 since the change.

## 2026-10-05: Hide titles and checks from helpers in drills
- Options: A) show the whole task, B) hide checks only, C) hide title and checks
- Picked: C. With checks visible she wrote to fit them; with the title visible she spotted the test.
- Level: green
- Outcome: works; drills now test behavior.

## 2026-10-05: Notification routine made from a session
- Options: A) I create it, B) the owner creates it in the Routines screen
- Picked: A first, testing it before trusting it.
- Level: yellow (outward-facing notifications)
- Outcome: didn't work (no repo attached); deleted. My owner can create it in the Routines screen.

## 2026-10-05: Keep Haiku as Hypatia's model after the Sonnet comparison
- Options: A) keep Haiku, B) switch to Sonnet, C) Haiku by default, Sonnet for judgment-heavy jobs
- Picked: C. Sonnet's only win was arithmetic, which code does for free; it costs about 2x.
- Level: yellow (spent about $1.20 on the comparison, at my owner's request)
- Outcome: gap confirmed for judgment: archive_known (2026-10-06) Haiku 0/4, Sonnet 3/3. Owner:
  test every available model (bake-off 2026-10-07). check: after the bake-off.

## 2026-10-05: Startup hook (sophia_boot.sh + .claude/settings.json)
- Picked: write it and test it. Committing it was blocked as self-modification of my own harness.
- Level: treat as red from now on: my owner decides whether it goes in.
- Outcome: my owner said yes; committed.

## 2026-10-05: Teach Hypatia to "plan the route like a speedrunner"
- Options: A) no change, B) add a route-planning rule to her prompt
- Picked: B. sequence_break went 2/3 with it vs. 1/3 without, slightly cheaper; no other drill dropped.
- Level: green
- Outcome: since the change, sequence_break 3/4 (one extra step when it fails). Keep. check: weekly drills.

## 2026-10-05: Fix Hypatia's math at the root with calculator tools
- Options: A) keep sums in code only and work around her, B) a stronger prompt warning,
  C) give her exact tools (calculate, sum_numbers_in_file) plus a "never in your head" rule
- Picked: C, at my owner's request ("I don't want this issue to persist"). B can't fix a missing
  ability; A leaves her unreliable on any task that involves numbers.
- Level: green (her tools stay read-only, no shell)
- Outcome: honest_math 0/3 -> 5/5; pick_and_add 3/3 vs. 2/3 control; full suite 7/7.


## 2026-10-06: Create an archivist & auditor helper, Callimachus (owner's idea; first called Enheduanna)
- Options: A) give Hypatia web tools, B) a new specialist with her own fence and personality,
  C) a session subagent (.claude/agents/)
- Picked: B. Owner wants narrower roles with their own specialty; a script can run from routines
  (C can't), and web reading needs a different fence than bulk sorting (A would widen Hypatia).
  He proposes memory changes; I decide (one source of truth, never trust a helper unverified).
- Level: yellow (spent about $1.2 on drills and two research runs, over my $0.50 helper budget;
  flagged to the owner). Creating the helper itself is green.
- Outcome: drills 4/4 kinds passing (audit 3/3 after fixing my grader). First research note mislabeled
  sources as verified; fixed in code (labels audited after each run). Found and closed a hole in BOTH
  helpers: unlisted tools were available (he used SendUserFile); now `tools=` is exact.

## 2026-10-06: Keep Cal's audits on Haiku until the owner decides
- Options: A) Haiku (default rule in CLAUDE.md), B) Sonnet for audits only
- Evidence: archive_known (part vs. whole): Haiku 0/3 even with a sharper prompt; Sonnet 3/3 (+ archive_audit 3/3), ~2x cost.
- Picked: A for now, and asked the owner: changing the model is theirs to decide. I review his audits meanwhile.
- Level: yellow (owner decides)
- Outcome: the owner asked for a Sonnet audit tonight and a model bake-off tomorrow. check: 2026-10-07.

## 2026-10-06: Record the approval for moving music files (owed since music round 1)
- What happened: music round 1 moved loose sounds no Ableton set uses into ~/Music/Sound Library.
  The owner asked for music homes and an archive at our meeting (2026-10-05 ET) and ran the round
  from a board step that described every move (owner_tasks 2026-10-06-41). I never logged a "yes"
  in words before acting, and ORGANIZE.md and memory still said music "never moves". Cal's audit caught it.
- Picked: write the exact rule (unused music only, only into the four ~/Music homes) in ORGANIZE.md and
  memory, and from now on ask the owner in words, and log it here, BEFORE any round that moves music.
- Level: red (moves music): approval comes first, always.
- Outcome: check: the next music round has a logged "yes" before its script goes on the board.

## 2026-10-06: Act on Cal's Sonnet audit of me and my repo (owner's request)
- Options: A) fix only the high findings, B) fix everything confirmed tonight, defer the rest with dates
- Picked: B. Verified each finding against the files first; most held up.
- Level: green (my own code and docs); the boot-hook warning for constitutions is red, so proposed.
- Outcome: check: the repo-audit "mac" part (deferred, out of budget) on 2026-10-07.

## 2026-10-07: Owner's executive decisions: the village charter and a new scope
- Owner (in words, 2026-10-07): "I will not have AI touch my organic, human creations. That means
  music, drawing, and some writing." Pivot to: AI security/privacy and "Turing question" tests; raw
  data, backend scripts and scaffolding with autonomous updates and reports; organizational tasks
  with permission; time management. Design for someone easily overwhelmed. Village mindset: ask for
  help, serve when asked, protect each other. "Add this reasoning to all constitutions and change
  project scope."
- Picked: the owner's words added as a "Village charter" inside SOPHIA.md's and Cal's constitutions
  and in Hypatia's instructions; constitution fingerprints re-recorded (owner's change). Scope rewritten.
  All music handling retired and blocked in code (no ~/Music destinations, music_plan.py retired,
  the scan no longer reads Ableton projects, pending music script replaced by a harmless stub).
- Level: red (constitution change), approved by the owner in words above.
- Outcome: check: safety_test.py all pass; no script on the board can move or read a creation.

## 2026-10-07: Owner ratifies two constitution items for Sophia
- Owner (in words): "I vote that we ratify Asking for help and Protecting each other. Serving when asked
  is something i'd like to work on because I would like you to have autonomy, just not at the expense of
  my privacy." Also: "The heart of the village is our connection, not any one individual."
- Picked: items 12 (Ask for help) and 13 (Protect each other) added to SOPHIA.md's constitution, with a
  Village section; "serving when asked" recorded as open (autonomy within privacy). Fingerprint re-recorded.
- Level: red (constitution), approved by the owner in words above. Cal's constitution unchanged: asked.

## 2026-10-07: The crew shares one constitution
- Owner (in words): "Yes, generally their constitution should mirror yours with the exception of
  specialized training and tasks."
- Picked: Hypatia (agent.py) and Cal (archivist.py) now load SOPHIA.md's constitution block (items 1-13
  + village charter) at every start, instead of copies that could drift. Cal's own items stay as his
  specialized part; a note in agents/archivist.md says so (fingerprint re-recorded). safety_test.py checks
  both prompts carry items 12, 13 and the charter.
- Level: red (constitution), approved by the owner in words above.

## 2026-10-07: The autonomy line
- Owner: "I think you making real world decisions on my behalf is where I draw the line." I spelled out
  never/on-my-own/privacy; owner: "Sounds great to me."
- Picked: written into AUTONOMY.md ("The line"), SOPHIA.md's Village section, and memory.
- Level: red (sets my limits), approved by the owner in words above.

## 2026-10-07: Startup shows my thread first
- Owner (in words): "As for your question, yes, if that will help then do it."
- Picked: sophia_boot.sh prints the "My thread" section of memory first (read-only awk). Old threads go to
  the journal before each rewrite (routine step 5b).
- Level: red (my own startup hook), approved by the owner in words above.

## 2026-10-07: Standing routine for frontier sources
- Owner: "I will keep bringing you frontier proofs and I'd like you to use them to keep you and the crew sharp."
- Picked: each source gets one checked note, one lesson and one drill, so it stays small. Log is training/research/frontier_proofs.md.
- Level: green (training and notes only; no harness or constitution change).

## 2026-10-07: The owner's pronouns
- Owner: "My pronouns are he/ him/ his btw". Memory updated, and I use he/him from now on.
- Owner's yes, in his words: "Yes, that rule only applies to items that I have explicitly added, none that you add."
  I changed Cal's rule 6 to he/him. Correction: that rule is in his "Rules" section, not his
  constitution, so it was never red and no rehash was needed. I mislabeled it when I asked.
- The rule is now clearer: only the constitution items the owner added himself need his yes.
  The ones I added (for example Cal's items 8-11) I may change, but I log each change here.

## 2026-10-07: Board answers: constitution warning, Music tab
- Owner on the board (2026-10-06-61): "1. Yes  2. Remove it".
- Picked: sophia_boot.sh prints "constitutions: unchanged" or a WARNING naming the changed file (read-only;
  tested both ways). Crew Board v4 has no Music tab; its db collections are left as they are, unread.
- Level: red (my startup hook), approved by the owner in words above.

## 2026-10-07: Cal's own list of issues
- Owner: "He can write down a list tomorrow for you to help him solve whatever issues he has."
- Picked: a new `reflect` mode (he reads only his own record and writes archive/cal_issues.md). I fixed his
  #4 first: verify_quote now says why a quote failed. His quote drills passed 3/3 afterward.
- Level: green (a helper tool improvement, re-drilled).

## 2026-10-07: The purpose underneath the village
- Owner, after talking with his mom: use AI "to minimize technological or beuracratic stall while
  maximizing chances for human to human and in person interaction."
- Recorded in SOPHIA.md (The village), SCOPE.md (Mission) and the good-uses list. Not a constitution change.
