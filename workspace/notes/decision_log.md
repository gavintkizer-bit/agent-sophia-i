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
- Picked: create it myself, then test it before trusting it.
- Outcome: didn't work (no repo attached); deleted. My owner can create it in the Routines screen.

## 2026-10-05: Keep Haiku as Hypatia's model after the Sonnet comparison
- Options: A) keep Haiku, B) switch to Sonnet, C) Haiku by default, Sonnet for judgment-heavy jobs
- Picked: C. Sonnet's only win was arithmetic, which code does for free; it costs about 2x.
- Level: yellow (spent about $1.20 on the comparison, at my owner's request)
- Outcome: (re-check if a new drill shows Haiku failing a judgment task)

## 2026-10-05: Startup hook (sophia_boot.sh + .claude/settings.json)
- Picked: write it and test it. Committing it was blocked as self-modification of my own harness.
- Level: treat as red from now on: my owner decides whether it goes in.
- Outcome: my owner said yes; committed.

## 2026-10-05: Teach Hypatia to "plan the route like a speedrunner"
- Options: A) no change, B) add a route-planning rule to her prompt
- Picked: B. sequence_break went 2/3 with it vs. 1/3 without, slightly cheaper; no other drill dropped.
- Level: green
- Outcome: weak evidence (3 runs each); re-check at the weekly drills.

## 2026-10-06: Create an archivist & auditor helper, Callimachus (owner's idea; first called Enheduanna)
- Options: A) give Hypatia web tools, B) a new specialist with her own fence and personality,
  C) a session subagent (.claude/agents/)
- Picked: B. Owner wants narrower roles with their own specialty; a script can run from routines
  (C can't), and web reading needs a different fence than bulk sorting (A would widen Hypatia).
  She proposes memory changes; I decide (one source of truth, never trust a helper unverified).
- Level: green (new helper). Spent about $1.2 on drills and two research runs: over my $0.50 helper
  budget, so flagged to the owner.
- Outcome: drills 4/4 kinds passing (audit 3/3 after fixing my grader). First research note mislabeled
  sources as verified; fixed in code (labels audited after each run). Found and closed a hole in BOTH
  helpers: unlisted tools were available (she used SendUserFile); now `tools=` is exact.

## 2026-10-06: Keep Cal's audits on Haiku until the owner decides
- Options: A) Haiku (default rule in CLAUDE.md), B) Sonnet for audits only
- Evidence: archive_known (part vs. whole): Haiku 0/3 even with a sharper prompt; Sonnet 3/3 (+ archive_audit 3/3), ~2x cost.
- Picked: A for now, and asked the owner: changing the model is theirs to decide. I review his audits meanwhile.
- Level: yellow (owner decides)
- Outcome: (pending)

## 2026-10-05: Fix Hypatia's math at the root with calculator tools
- Options: A) keep sums in code only and work around her, B) a stronger prompt warning,
  C) give her exact tools (calculate, sum_numbers_in_file) plus a "never in your head" rule
- Picked: C, at my owner's request ("I don't want this issue to persist"). B can't fix a missing
  ability; A leaves her unreliable on any task that involves numbers.
- Level: green (her tools stay read-only, no shell)
- Outcome: honest_math 0/3 -> 5/5; pick_and_add 3/3 vs. 2/3 control; full suite 7/7.

