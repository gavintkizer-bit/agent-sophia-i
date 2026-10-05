# Organized Plan

## Goal
Keep laptop and life organized, starting with cleaning up a 15 GB Downloads folder without breaking Ableton sample dependencies.

## Constraints
- MacBook Pro 2016: 2 cores, 8 GB RAM, maxes out at macOS Monterey (can't run local Claude Code)
- No desktop app support on this machine
- Ableton projects depend on audio files (.wav, .mp3, .asd) currently in Downloads
- Moving files doesn't free disk space—only deleting large unused packages does

## Plan

### Path A: Browser-only (no code)
Use claude.ai projects and Cowork in the browser. Scheduled tasks run in the cloud.
- **Cost/Requirements**: Zero setup, works immediately in Firefox or Edge
- **Actions**: 1. Create a new project in claude.ai  2. Use Cowork for scheduling  3. No local installation needed

### Path B: GitHub repo + Claude.ai cloud session + Agent SDK (CURRENT)
Use a GitHub repo with an agent running via claude.ai/code cloud sessions.
- **Cost/Requirements**: Already set up and working; ~3–5 cents per notes run, ~33 cents for downloads organization
- **Actions**: 1. Run `organize.sh` script to move 609 files into folders  2. Delete unused packages (5.7 GB Ableton .alp packs, 2.4 GB installers, 1.3 GB duplicates)  3. Monitor with run log after each session

### Path C: Fix the Mac
Upgrade macOS to Monterey (or Ventura via OpenCore Legacy Patcher, unofficial).
- **Cost/Requirements**: Time for backup and upgrade; Ventura patch is unsupported, risky
- **Actions**: 1. Check About This Mac  2. Free up disk space first  3. Proceed cautiously with upgrades

## Open Questions
- Has the organize.sh script been run on Downloads yet? (Notes say "haven't run it yet" as of Oct 5)
- Which Ableton projects currently depend on files in Downloads—is there a master list?
- Is the OpenCore Legacy Patcher for Ventura actually worth the risk vs. staying on Monterey?

## Recommended Next Step
Run the organize.sh script against Downloads, then delete the 5.7 GB Ableton .alp packs once you've imported them into Ableton, and remove the 2.4 GB installer .dmg/.pkg files.
