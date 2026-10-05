# Organized Plan

## Goal
Keep laptop and life organized by building a Claude agent that runs in the cloud to automate file cleanup and task management, starting with clearing 15 GB from Downloads while preserving Ableton samples.

## Constraints
- MacBook Pro 13" (2016): 2 cores, 8 GB RAM, max OS is Monterey (cannot run desktop apps or latest Claude Code)
- Older macOS cannot update past version 13, which blocks local Claude Code
- Chrome stops updating on old macOS; must use Firefox or Edge as alternative browsers
- No budget to replace hardware; must work with existing laptop

## Plan

### Path A: Browser-only
No local installation. Use claude.ai Projects and Cowork entirely in the browser; scheduled tasks run automatically in the cloud.
- **Costs/requires**: Free tier or paid Claude subscription; no local setup needed
- **Next actions**: 
  1. Create a new Claude Project in claude.ai
  2. Draft a task markdown file for file cleanup
  3. Test manual runs before scheduling

### Path B: GitHub + Cloud Agent (CHOSEN)
GitHub repo + claude.ai/code cloud session + Claude Agent SDK (Python). Agent runs in cloud, not locally.
- **Costs/requires**: Separate pay-as-you-go API billing; verify API key and cloud network permissions
- **Next actions**:
  1. Run `python agent.py --check` to verify setup and API access
  2. Confirm cloud network allows `api.anthropic.com` by default
  3. Start with cheapest model (Haiku) for testing

### Path C: Upgrade macOS
Check About This Mac, free up disk space, upgrade to Monterey (free), or use OpenCore Legacy Patcher for Ventura+ (unofficial; requires backup first).
- **Costs/requires**: Disk space; time for backup and upgrade; risk of unofficial patcher; eventual hardware refresh may still be needed
- **Next actions**:
  1. Check current macOS version and available disk space
  2. Back up critical files (Ableton samples, projects)
  3. Attempt Monterey upgrade or research OpenCore patcher compatibility

## Open Questions
- Does the cloud network in claude.ai/code allow `api.anthropic.com` by default? (Verify with `agent.py --check`)
- Is API billing separate from standard Claude subscription, or part of the same account?
- Should the agent eventually have web search capability or run on a weekly schedule?

## Recommended Next Step
Run `python agent.py --check` to verify Path B is ready, confirm network access to the API, and begin with the cheapest model (Haiku) for testing.
