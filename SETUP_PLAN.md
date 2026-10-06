# Setup plan

## Status: WORKING (since 2026-10-05)
In a claude.ai/code cloud session the helpers need **no API key**: the SDK uses the session's own
Claude connection. The old key was removed from the repo and revoked by the owner.

## If a helper stops working (in order)
1. **"No API key found" or an old error:** the session is on old code. Check it's on `main` and that
   `agent.py` contains `IN_CLOUD_SESSION`.
2. **An SDK or Claude Code error:** run `pip install -U claude-agent-sdk` and try again; read the
   whole traceback before anything else.
3. **Still broken:** Sophia does the task herself in the session (no SDK); only the cost log is lost.
4. **Outside claude.ai/code** (another computer): test a Console API key in the Workbench, then set
   `AGENT_API_KEY` (or `ANTHROPIC_API_KEY`) where the helper runs.
