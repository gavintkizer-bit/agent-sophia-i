# Organized Plan: Set Up Claude Agent on MacBook

## Goal
Build and run a Claude agent on a 2016 MacBook Pro using cloud infrastructure to work around hardware and OS limitations.

## Constraints
- MacBook Pro 13" (2016): 2 cores, 8GB RAM, cannot run desktop apps or update to macOS 13+
- Chrome stops updating on old macOS; must use Firefox or Edge
- Local Claude Code setup requires macOS 13+ (not available on this machine)

## Plan

### Path A: Browser-Only (No Code)
Claude.ai projects + Cowork in the browser, with scheduled tasks running in the cloud.
- **Cost/Requirements**: Free tier available; minimal setup
- **Next steps**: 
  1. Create a Claude.ai project in the browser
  2. Enable Cowork for collaboration features
  3. Test scheduling a simple task in the cloud

### Path B: Recommended — Cloud Agent (Selected)
GitHub repo + Claude.ai/code cloud session + Claude Agent SDK. Agent runs in the cloud; you edit code locally.
- **Cost/Requirements**: Pay-as-you-go API billing (separate from Claude subscription); requires ANTHROPIC_API_KEY
- **Next steps**:
  1. Run `pip install -r requirements.txt` and `python agent.py --check` to verify API access
  2. Confirm cloud network allows `api.anthropic.com` (test via `--check` flag)
  3. Choose Haiku model for cheapest testing; set up a run log to track costs and improvements

### Path C: Fix the Mac
Check disk space, upgrade to macOS Monterey, or use OpenCore Legacy Patcher for Ventura+ (unofficial; requires backup).
- **Cost/Requirements**: Free, but time-intensive; Ventura+ method is experimental and unsupported
- **Next steps**:
  1. Check "About This Mac" to see current OS and storage
  2. Free up disk space if needed
  3. Attempt Monterey upgrade; if blocked, decide on OpenCore Legacy Patcher risk

## Open Questions
- Does the cloud network allow `api.anthropic.com` by default? (Run `agent.py --check` to verify)
- Which model is cheapest for testing — Haiku?
- Should the agent have web search capability?
- Is pay-as-you-go billing separate from Claude subscription?

## Recommended Next Step
Proceed with Path B: run `python agent.py --check` in a cloud session to verify API connectivity and confirm API billing setup.
