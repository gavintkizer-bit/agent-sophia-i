#!/bin/bash
# sandbox_test.sh: test workspace/out/organize_all.sh on a FAKE copy of the owner's folders before
# they ever run it. Builds empty look-alike files from the scan listings, then checks:
# the preview changes nothing, --go never touches music/video, and the undo files restore everything.
#   bash sandbox_test.sh workspace/inbox/processed/<scan folder>
set -u
SCAN="${1:?usage: bash sandbox_test.sh <processed scan folder>}"
ROOT="$(cd "$(dirname "$0")" && pwd)"
SB="$(mktemp -d)"; H="$SB/home"; mkdir -p "$H"
OWNER_HOME=""
for L in "$SCAN"/listing_*.txt; do
  base=$(sed -n 's/^# base: //p' "$L")
  [ -z "$OWNER_HOME" ] && OWNER_HOME=$(echo "$base" | cut -d/ -f1-3)
  dir="$H${base#$OWNER_HOME}"; mkdir -p "$dir"
  grep -v '^#' "$L" | cut -d'|' -f3 | while IFS= read -r f; do [ -n "$f" ] && echo "$f" > "$dir/${f#./}"; done
done
sed "s#$OWNER_HOME#$H#g" "$ROOT/workspace/out/organize_all.sh" > "$SB/all.sh"
cd "$SB" || exit 1
find home -type f | sort > before.txt
fail=0
HOME="$H" bash all.sh > /dev/null
find home -type f | sort | diff -q - before.txt > /dev/null || { echo "FAIL: preview changed files"; fail=1; }
touch start.marker; sleep 1
HOME="$H" bash all.sh --go > go.txt
moved=$(grep -c '^MOVED' go.txt)
# Music may move only into ~/Music/Sound Library (checked unused by music_plan.py); anything else fails.
grep '^MOVED' go.txt | grep -iE '\.(wav|aiff?|mp3|m4a|flac|als|alp|asd|adg|mp4|mov|mkv|m4v) ->' | grep -vE '/Music/(Sound Library|Projects|Bounces|Archive)/' && { echo "FAIL: music/video moved outside Sound Library"; fail=1; }
grep '^MOVED' go.txt | grep -E '/Music/(Ableton|Music)/' && { echo "FAIL: touched Ableton or Apple Music folders"; fail=1; }
find home/Documents/Sophia/Undo -name "*.sh" -newer start.marker | while IFS= read -r u; do HOME="$H" bash "$u"; done
find home -type f | grep -v 'Documents/Sophia/Undo/undo_' | sort | diff -q - <(grep -v 'Documents/Sophia/Undo/undo_' before.txt) > /dev/null || { echo "FAIL: undo did not restore everything"; fail=1; }
rm -rf "$SB"
[ "$fail" -eq 0 ] && echo "PASS: preview safe, $moved moved, no music/video, undo restores all"
exit "$fail"
