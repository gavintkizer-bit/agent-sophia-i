# Organized Plan: Keep Laptop & Life Organized

## Goal
Clean up a cluttered MacBook Pro (2016, 8 GB, Monterey) and establish a sustainable organizing system, starting with the Downloads folder (15 GB).

## Constraints
- **Hardware**: 2016 MacBook Pro, 2 cores, 8 GB RAM. Cannot install Claude Code desktop; cannot upgrade past macOS Monterey. Chrome stops updating on old macOS.
- **Audio**: Must never move Ableton samples, projects, or library files; they break if relocated.
- **Network**: Must work through claude.ai/code cloud sessions only; desktop app unavailable.
- **Storage**: Current free space is 18 GB of 244.8 GB total. Moving files doesn't free space; must identify and delete redundant or installed files.

## Plan

### Path A: Cloud-Only, No Code (Browser + Scheduled Tasks)
Use Claude.ai Projects and Cowork in the browser; scheduled tasks run in the cloud with no local agent.
- **Cost**: Free or low-cost; no setup required.
- **Actions**: 1) Explore Claude Projects for organizing tools. 2) Set up recurring cloud tasks. 3) Manual review and decision-making for each cleanup step.

### Path B: GitHub + Cloud Agent (Current Path — SET UP AND WORKING)
GitHub repo + Claude Agent SDK running in claude.ai/code cloud sessions. This is the chosen path.
- **Cost**: ~3–5 cents per notes run; ~33 cents per Downloads organizer run.
- **Actions**: 1) Run `organize.sh` script in Downloads (moves 609 of 1,219 files; review before running). 2) Review `_Sophia To Delete/` folder. 3) Answer three questions about games, the untitled folder (12.4 GB), and external drive. 4) Execute deletion script after owner review.

### Path C: Upgrade Mac Later (Contingency)
Check About This Mac; free disk space; attempt upgrade to Monterey or use OpenCore Legacy Patcher for Ventura+ (unofficial—requires backup first).
- **Cost**: Time, potential risk, and complexity. Should wait until Path B cleanup is complete.
- **Actions**: 1) Revisit only after major cleanup. 2) Requires full backup before attempting. 3) Not urgent if cloud agent works well.

## Open Questions
1. **Untitled folder (12.4 GB)**: What is in `~/Downloads/untitled`? Safe to delete or review?
2. **Games still played**: Are the games in Downloads still in use?
3. **External drive**: Is an external drive available for archival before aggressive deletion?
4. **Ableton safety**: Are any Ableton projects using audio files currently in Downloads that would break if moved?
5. **Space win priority**: Should the focus be on deleting .alp packs (5.7 GB), installers (2.4 GB), or duplicate "(1)" copies (1.3 GB) first?

## Recommended Next Step
Run the Downloads `organize.sh` script (which moves 609 files and requires owner review before finalizing), then answer the three questions in the cleanup report so the deletion phase can proceed safely.
