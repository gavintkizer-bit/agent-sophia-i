# Organized Plan: Laptop and Life Organization

## Goal
Keep the laptop (2016 MacBook Pro, 8 GB, macOS Monterey) and life organized, starting with cleaning up Downloads (15 GB) without breaking Ableton music projects.

## Constraints
- Mac tops out at macOS Monterey (12.7.6); cannot upgrade further.
- Claude Code needs macOS 13+, so local sessions won't work.
- Cannot move Ableton files, samples, or videos used in Ableton projects.
- Cannot move music plugin installers (some are no longer downloadable).
- Must protect `.alp` Ableton packs (delete only after confirmed installed).
- Running only in claude.ai/code cloud sessions (desktop app won't install).

## Plan

### Path A: Browser only (claude.ai projects + Cowork)
**What it is:** Use Claude directly in the browser with scheduled tasks in the cloud; no agent or local code.

**Cost/requires:** Minimal setup; no GitHub repo.

**Next actions:**
1. Set up Cowork for task scheduling.
2. Use claude.ai/code for cloud sessions only.

---

### Path B: Agent + cloud sessions ✓ (CURRENT)
**What it is:** GitHub repo + Claude Agent SDK (`agent.py`). Hypatia (Haiku model) runs cleanup scripts safely. Owner runs terminal commands on the Mac; Sophia decides the order.

**Cost/requires:**
- Setup: ~3–5 cents per notes run; ~33 cents per Downloads cleanup run.
- API key not needed in cloud sessions (uses the session's own Claude connection).
- Haiku model is cheapest; Sonnet is ~2x cost and doesn't improve significantly.

**Next actions:**
1. Run `python agent.py --check` to verify setup (READY as of 2026-10-05).
2. Run the Downloads cleanup script (`organize_Downloads.sh`) when ready.
3. Review moved files in `_Sophia To Delete/` before owner deletes them.

---

### Path C: Fix the Mac and upgrade
**What it is:** Free up disk space, then attempt to upgrade to newer macOS. Check "About This Mac" first. For Ventura/Sonoma: OpenCore Legacy Patcher (unofficial; requires backup first).

**Cost/requires:**
- Uncertainty: will upgrade succeed on this 2016 model?
- Must back up before trying OpenCore.
- Risky; unclear upside.

**Next actions:**
1. Check About This Mac for available disk space and current macOS version.
2. If space is freed (via Path B cleanup), reassess whether upgrade is possible.
3. Only attempt if Path B cleanup succeeds and owner wants to proceed.

---

## Open Questions
1. What is in `~/Downloads/untitled` folder (12.4 GB)? (Asked but not yet answered.)
2. Do you still play the games that are in Downloads? (Asked but not yet answered.)
3. Do you have an external drive? (Asked but not yet answered.)
4. What happened when Claude Desktop wouldn't install? (It should work on macOS 12.7.6, but owner said it wouldn't; unclear why.)

## Recommended Next Step
Run the Downloads cleanup script (`organize_Downloads.sh`) when you're ready to start; it moves 442 files (7.5 GB) to a review folder, and you decide what to keep.
