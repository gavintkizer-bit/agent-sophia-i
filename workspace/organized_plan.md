# Organized Plan: Run Claude Agent on Limited Hardware

## Goal
Set up a working Claude agent workflow that runs on a 2016 MacBook Pro (2 cores, 8GB RAM, outdated macOS) so you can test, iterate, and improve it over time.

## Constraints
- MacBook Pro 2016 cannot install desktop apps or update macOS beyond current version
- Claude Code locally requires macOS 13+; older Mac doesn't support upgrades
- Browser will eventually stop updating (Chrome already has; can use Firefox or Edge)
- Limited hardware and storage space

## Plan

### Path A: Browser-Only (No Code Locally)
**What**: Use Claude.ai Projects + Cowork entirely in the browser; scheduled tasks run in Anthropic's cloud.
- **Requires**: Claude.ai account + browser; no setup on Mac
- **Cost**: Depends on Pro/Enterprise plan
- **Next actions**:
  1. Create a new project in Claude.ai
  2. Set up scheduled tasks in Cowork
  3. Test one simple automation to verify cloud execution

### Path B: Cloud-Based Agent (RECOMMENDED)
**What**: GitHub repo + Claude.ai/code cloud session + Claude Agent SDK agent in Python.
- **Requires**: GitHub repo + API key (separate "pay as you go" billing) + network access to api.anthropic.com
- **Cost**: Per-token pricing; Haiku is cheapest model for testing
- **Next actions**:
  1. Run `python agent.py --check` to verify API setup and network access
  2. Confirm AGENT_API_KEY is set in cloud environment variables
  3. Run first task and log results; plan one improvement for next run

### Path C: Fix the Mac (Long-term Option)
**What**: Upgrade to macOS Monterey or use OpenCore Legacy Patcher for Ventura+ (unofficial workaround).
- **Requires**: Check About This Mac; free up disk space; backup system first
- **Cost**: Time + risk (unofficial patching isn't guaranteed)
- **Next actions**:
  1. Check current macOS version and available storage
  2. Back up entire system
  3. Attempt official Monterey upgrade; if blocked, research OpenCore Legacy Patcher

## Open Questions
- Does the cloud network allow api.anthropic.com by default? (Test with `agent.py --check`)
- Billing model for separate API key—is it truly separate from Claude.ai subscription?

## Recommended Next Step
**Start with Path B**: Run `python agent.py --check` in your cloud session to verify API key and network access, then run your first task and keep a run log to track improvements.
