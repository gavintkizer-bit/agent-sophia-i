#!/usr/bin/env bash
# Sophia's boot check: runs automatically when a Claude Code session starts (.claude/settings.json).
# It installs requirements, checks Hypatia, and prints a short status that lands in my context,
# so I start every session already knowing what's new. Read-only apart from pip; changes no files.
cd "$(dirname "$0")" || exit 0

echo "== Sophia boot $(date -u '+%Y-%m-%d %H:%M UTC') =="
if pip install -q -r requirements.txt >/dev/null 2>&1; then echo "deps: installed"; else echo "deps: pip FAILED (run it by hand)"; fi
python agent.py --check 2>&1 | grep -q "Result: READY" && echo "Hypatia: READY" || echo "Hypatia: NOT READY (run python agent.py --check)"

# New uploads from the owner (inbox, or misplaced in the repo root).
uploads=$(ls workspace/inbox 2>/dev/null | grep -vx 'preferences.md\|processed'; ls listing_*.txt file_listing.txt disk_survey.txt 2>/dev/null)
if [ -n "$uploads" ]; then echo "NEW UPLOADS (follow ORGANIZE.md):"; echo "$uploads" | sed 's/^/  - /'; else echo "uploads: none"; fi

# Drills: due when the newest scoreboard row is 7+ days old.
last=$(grep -o '^| 20[0-9-]*' training/scoreboard.md 2>/dev/null | tail -1 | tr -d '| ')
if [ -n "$last" ]; then
  age=$(( ( $(date -u +%s) - $(date -u -d "$last" +%s 2>/dev/null || date -u +%s) ) / 86400 ))
  [ "$age" -ge 7 ] && echo "drills: DUE (last run $last)" || echo "drills: last run $last"
fi

# Open items I left myself.
open=$(grep -ci '→ open\|status: open' workspace/notes/improvement_log.md 2>/dev/null)
echo "open improvement items: ${open:-0} (workspace/notes/improvement_log.md)"
echo "Next: read SOPHIA.md + memory, then the Crew Board (CLAUDE.md)."
exit 0
