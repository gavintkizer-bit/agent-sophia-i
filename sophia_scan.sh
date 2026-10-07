#!/bin/bash
# sophia_scan.sh: run this ON YOUR MAC. It only READS sizes, dates, and names.
# It never opens, moves, or changes a file.
#
#   bash ~/Downloads/sophia_scan.sh
#
# It creates the folder ~/Desktop/sophia_upload/ with:
#   disk_survey.txt          where the space on your drive is going
#   listing_Downloads.txt    the files directly in Downloads (same for Desktop, Documents)
#   sophia_scan.zip          all of the above in one file: upload ONLY this to workspace/inbox/
#
# macOS may ask "Terminal would like to access files in your Desktop/Documents/Downloads
# folder". Click OK. Lines saying "Operation not permitted" are normal and harmless.
set -u

OUT="$HOME/Desktop/sophia_upload"
mkdir -p "$OUT" || exit 1
TODAY="$(date +%Y-%m-%d)"

echo "Scanning... this can take a few minutes on an older Mac."

# ---- 1. where the space goes
{
  echo "# made: $TODAY"
  echo "# home: $HOME"
  echo "## macos"
  sw_vers 2>/dev/null
  echo "## disk (1K blocks)"
  df -k / 2>/dev/null
  echo "## home folders (KB, 2 levels deep)"
  du -k -d 2 -x "$HOME" 2>/dev/null | grep -v "^[0-9]*	$HOME/Library"
  echo "## library folders (KB, 3 levels deep)"
  du -k -d 3 -x "$HOME/Library" 2>/dev/null
  echo "## big files (100 MB or more; date|bytes|path)"
  find "$HOME" -xdev -type f -size +100M ! -path "$HOME/Library/Mobile Documents/*" \
    -exec stat -f '%Sm|%z|%N' -t '%Y-%m-%d' {} + 2>/dev/null | sort -t '|' -k2 -n -r
  echo "## apps (KB)"
  du -k -d 0 /Applications/*.app "$HOME"/Applications/*.app 2>/dev/null | sort -n -r
  echo "## time machine local snapshots"
  tmutil listlocalsnapshots / 2>/dev/null
  echo "## end"
} > "$OUT/disk_survey.txt"
echo "  wrote disk_survey.txt"

# ---- 2. one listing per everyday folder (files directly inside, not subfolders)
for NAME in Downloads Desktop Documents; do
  DIR="$HOME/$NAME"
  [ -d "$DIR" ] || continue
  {
    echo "# base: $DIR"
    echo "# made: $TODAY"
    cd "$DIR" && find . -maxdepth 1 -type f ! -name '.*' ! -name $'*\n*' \
      -exec stat -f '%Sm|%z|%N' -t '%Y-%m-%d' {} + 2>/dev/null | sort -t '|' -k3
  } > "$OUT/listing_$NAME.txt"
  echo "  wrote listing_$NAME.txt ($(($(wc -l < "$OUT/listing_$NAME.txt") - 2)) files)"
done

# (The music map and project dates were removed on 2026-10-07: the owner decided AI doesn't touch
#  their music, so this scan no longer opens or lists anything inside their Ableton projects.)

# ---- 5. one zip to upload (GitHub's upload page takes 25 MB per file)
(
  cd "$OUT" || exit 1
  [ -e sophia_scan.zip ] && mv -f sophia_scan.zip "$HOME/.Trash/sophia_scan-$(date +%H%M%S).zip"
  zip -9 -q sophia_scan.zip ./*.txt
)
echo "  wrote sophia_scan.zip ($(du -h "$OUT/sophia_scan.zip" | cut -f1)): upload ONLY this file"

echo ""
echo "Done. Nothing on your Mac was changed."
echo "Next: upload $OUT/sophia_scan.zip to GitHub, into workspace/inbox/"
open "$OUT" 2>/dev/null
