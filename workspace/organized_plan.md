# Organized Plan

## Goal
Keep your laptop and life organized by safely cleaning up the drive and building file habits that protect your music, all within the constraints of a 2016 Mac that maxes out at Monterey.

## Constraints
- **Hardware**: 2016 MacBook Pro, 2 cores, 8 GB RAM; macOS Monterey (12.7.6) is the maximum.
- **Software**: Claude Code requires macOS 13+, so all work runs in cloud sessions only (claude.ai/code).
- **Music**: Ableton library, samples, projects, videos, and plugin installers are protected—nothing moves without verifying it's unused.
- **Motivation**: Perfectionism freezes you on big projects; a ready-made plan lowers the cost of starting.

## Plan

### Path A: Browser only
Use claude.ai projects + Cowork in the browser; tasks run in the cloud.
- **Cost/requires**: Minimal setup, no GitHub repo, tasks visible in browser.
- **Next actions**: 1) Start a new claude.ai project. 2) Set up a task board in Cowork. 3) Schedule runs via Routines.

### Path B: Agent + cloud sessions ✓ CURRENT
GitHub repo + claude.ai/code cloud sessions + Hypatia (agent). You run terminal commands on the Mac; Sophia decides the order and writes the scripts.
- **Cost/requires**: ~3–5 cents per notes run; ~33 cents per script run. Haiku model is default and cheapest.
- **Status (2026-10-06)**: Downloads sorted and organized (55.3 GB freed). Home folders built (Documents/School, Finance, Code, Books, Papers; Pictures/Photos, Screenshots, Images). Music round 1 done (1.5 GB moved to Sound Library). Sandbox tests and undo system working.
- **Next actions**: 1) Run the music organization script (organize_all.sh, 2 safe moves). 2) Check that "Void Speech" plays from Music/Bounces. 3) Give feedback on music workflow.

### Path C: Upgrade the Mac
Free up disk space (done via Path B), then upgrade to Monterey or try OpenCore Legacy Patcher for Ventura (unofficial, requires backup).
- **Cost/requires**: Risk and uncertainty; may not solve the core constraint (Claude Code still won't run locally).
- **Next actions**: 1) Reassess after Path B is complete. 2) Only attempt if you see a concrete benefit.

## Open Questions
1. Should the scan automatically detect installed Ableton packs so `.alp` files can be confirmed safe to delete?
2. Can the scan avoid reading ~/Library twice (currently slows older Macs)?
3. Once you "Collect All and Save" a project in Ableton, which sample packs can safely move?
4. Should Hypatia run on a weekly schedule with web search?

## Recommended Next Step
Run the music organization script (organize_all.sh) and verify "Void Speech" plays from Music/Bounces; feedback on the music checklist will shape the next round.
