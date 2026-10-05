# Setup plan: getting the API key working

## What was actually wrong
It wasn't you. In a Claude Code cloud session, a variable named `ANTHROPIC_API_KEY`
never reaches your code. Claude Code uses `ANTHROPIC_*` names for its own connection,
and the session we checked had no `ANTHROPIC_API_KEY` in it. Saving it 30 times
couldn't fix that.

**Fix:** `agent.py` now also reads the key from a variable called **`AGENT_API_KEY`**.

Already confirmed: the network reaches api.anthropic.com, so no network changes are needed.

## Tomorrow: about 10 minutes

### 1. Make a fresh key (old one is exposed)
1. Go to console.anthropic.com → **API Keys**.
2. **Delete** the old key (the one saved in the `API_KEY` file in this repo).
3. Click **Create Key** and copy the new one (starts with `sk-ant-`).
4. Check that **Billing** has some credit (even $5). A key with no credit fails later.

### 2. Put it in the environment
1. In claude.ai/code, click the environment name **agent-env** in the session's title bar, then **Edit**.
2. In **Environment variables**, delete any old `ANTHROPIC_API_KEY=...` line.
3. Add these two lines exactly (no quotes, no spaces around `=`):
   ```
   AGENT_API_KEY=sk-ant-PASTE-YOUR-NEW-KEY
   AGENT_ENV_TEST=hello
   ```
4. **Save.**

### 3. Start a NEW session
Old sessions never see new settings. Start a brand-new session on this repo
(branch `claude/funny-hawking-rbvqwd`, or `main` once this is merged) using **agent-env**, and type:

> run agent

### 4. Reading the check result
| What `--check` says | Meaning | Do this |
|---|---|---|
| `AGENT_ENV_TEST found` + `READY` | Everything works | Nothing. The agent runs. |
| `AGENT_ENV_TEST found` + `401` | Variables arrive; key is wrong | Re-copy the key. Make sure it's the new one. |
| `AGENT_ENV_TEST not found` | Your settings aren't reaching the session | The session isn't using **agent-env**, the save didn't stick, or it's an old session. Screenshot the Edit screen. |

### 5. Clean up
Ask Claude: "delete the API_KEY file and add it to .gitignore".
