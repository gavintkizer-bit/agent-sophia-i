#!/bin/bash
# sophia_scan.sh: run this ON YOUR MAC. It only READS sizes, dates, and names.
# It never opens, moves, or changes a file.
#
#   bash ~/Downloads/sophia_scan.sh
#
# It creates the folder ~/Desktop/sophia_upload/ with:
#   disk_survey.txt          where the space on your drive is going
#   listing_Downloads.txt    the files directly in Downloads (same for Desktop, Documents)
#   music_refs.txt           which samples/videos each Ableton project uses (read from the projects)
#   music_files.txt          names of every file in Downloads and Desktop, all levels
# Upload everything in that folder to the repo's workspace/inbox/ folder.
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

# ---- 3. music map (read-only): which samples and videos each Ableton project uses, so Sophia
#         can tell which loose music files are safe to tidy. Projects are only READ (gzip -dc).
{
  echo "# made: $TODAY"
  echo "# home: $HOME"
  echo "# format: project<TAB>file it uses (as Ableton stored it)"
  find "$HOME" -xdev \( -path "$HOME/Library" -o -path "$HOME/.Trash" -o -path "$HOME/Music/Ableton/Factory Packs" \) -prune \
    -o -type f \( -iname '*.als' -o -iname '*.als [0-9]*' -o -iname '*.alc' -o -iname '*.adg' -o -iname '*.adv' \) -print 2>/dev/null |
  while IFS= read -r SET; do
    gzip -dcf "$SET" 2>/dev/null |
      grep -oiE 'Value="[^"]*\.(wav|aif|aiff|mp3|m4a|flac|ogg|caf|aac|mid|midi|mp4|mov|m4v|mkv|avi|webm)"' |
      sed 's/^Value="//; s/"$//' | sort -u | awk -v set="$SET" '{print set "\t" $0}'
  done
} > "$OUT/music_refs.txt"
echo "  wrote music_refs.txt ($(grep -vc '^#' "$OUT/music_refs.txt") sample links)"
{
  echo "# made: $TODAY"
  echo "# every file inside Downloads and Desktop, all levels (names only)"
  find "$HOME/Downloads" "$HOME/Desktop" -xdev -type f ! -name '.*' -print 2>/dev/null
} > "$OUT/music_files.txt"
echo "  wrote music_files.txt ($(($(wc -l < "$OUT/music_files.txt") - 2)) files)"

echo ""
echo "Done. Nothing on your Mac was changed."
echo "Next: upload everything in $OUT to GitHub, into workspace/inbox/"
open "$OUT" 2>/dev/null
