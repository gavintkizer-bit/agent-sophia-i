#!/bin/bash
# sophia_share.sh: you choose writings and drawings to share with Sophia.
# It only READS and COPIES into a zip. It never moves, renames or deletes any of your files.
# Music is never included (no audio, no Ableton, no project or sample folders).
#
# Step 1:  bash ~/Downloads/sophia_share.sh find
#          Lists the folders that hold documents and pictures, with how many files each has.
# Step 2:  open ~/Desktop/sophia_share/keep_folders.txt, DELETE the lines of folders you
#          don't want to share (bills, photos, other people's PDFs...), and save.
# Step 3:  bash ~/Downloads/sophia_share.sh zip
#          Zips only the files directly in the folders you kept, in pieces of up to 20 MB
#          (sophia_share.zip, .z01, .z02...). Upload every piece to the repo's owner_own/ folder.
#
# macOS may ask "Terminal would like to access files in ...": click OK (it's reading only).
set -u

OUT="$HOME/Desktop/sophia_share"
ALL="$OUT/all_files.txt"
KEEP="$OUT/keep_folders.txt"
ROOTS=("$HOME/Documents" "$HOME/Desktop" "$HOME/Downloads" "$HOME/Pictures"
       "$HOME/Library/Mobile Documents/com~apple~CloudDocs")
# Folders never included: money, code, other people's books, Sophia's own files, photos and
# screenshots, and everything musical.
SKIP='/Finance/|/Code/|/Books/|/Sophia/|/_Sophia To Delete/|/Photos/|/Screenshots/|/Music/|Ableton| Project/|/Samples/|/sophia_share/|/sophia_upload/'

find_files() {
  for ROOT in "${ROOTS[@]}"; do
    [ -d "$ROOT" ] || continue
    find "$ROOT" \
      \( -type d \( -name '.*' -o -iname '*.photoslibrary' -o -iname '*.app' -o -name node_modules \) -prune \) -o \
      \( -type d \( -iname '*.rtfd' -o -iname '*.pages' \) -print -prune \) -o \
      \( -type f \( -iname '*.txt' -o -iname '*.rtf' -o -iname '*.md' -o -iname '*.doc' -o -iname '*.docx' \
         -o -iname '*.pages' -o -iname '*.odt' -o -iname '*.pdf' -o -iname '*.png' -o -iname '*.jpg' \
         -o -iname '*.jpeg' -o -iname '*.heic' -o -iname '*.tif' -o -iname '*.tiff' -o -iname '*.gif' \
         -o -iname '*.psd' -o -iname '*.procreate' -o -iname '*.svg' \) -print \) 2>/dev/null
  done | grep -v -E "$SKIP"
}

case "${1:-}" in
  find)
    mkdir -p "$OUT"
    find_files > "$ALL"
    sed -E 's|/[^/]*$||' "$ALL" | sort | uniq -c | sort -rn \
      | awk '{c=$1; sub(/^ *[0-9]+ /, ""); printf "%6d files\t%s\n", c, $0}' | sed "s|	$HOME|	~|" > "$KEEP"
    echo "Found $(wc -l < "$ALL" | tr -d ' ') files in $(wc -l < "$KEEP" | tr -d ' ') folders."
    echo "Next: open $KEEP"
    echo "      delete the lines of folders you DON'T want to share, save, then run:"
    echo "      bash ~/Downloads/sophia_share.sh zip"
    open -e "$KEEP" 2>/dev/null
    ;;
  zip)
    [ -s "$KEEP" ] || { echo "Run 'bash ~/Downloads/sophia_share.sh find' first."; exit 1; }
    cut -f2- "$KEEP" | grep -v '^$' | sed "s|^~|$HOME|" > "$OUT/.kept_dirs"
    awk 'NR==FNR {keep[$0]=1; next} {d=$0; sub(/\/[^\/]*$/, "", d); if (d in keep) print}' \
      "$OUT/.kept_dirs" "$ALL" > "$OUT/chosen_files.txt"
    N=$(wc -l < "$OUT/chosen_files.txt" | tr -d ' ')
    [ "$N" -gt 0 ] || { echo "No files chosen. Keep at least one folder in keep_folders.txt."; exit 1; }
    # Old zip pieces go to the Trash, never deleted.
    for OLD in "$OUT"/sophia_share.z*; do
      [ -e "$OLD" ] && mv -f "$OLD" "$HOME/.Trash/$(basename "$OLD")-$(date +%H%M%S)"
    done
    cd / && zip -q -r -s 20m "$OUT/sophia_share.zip" -@ < "$OUT/chosen_files.txt"
    echo "Zipped $N files. The pieces (upload ALL of them to owner_own/ on GitHub):"
    ls -lh "$OUT"/sophia_share.z* | awk '{print "  " $5 "  " $NF}'
    open "$OUT"
    ;;
  *)
    echo "Usage: bash ~/Downloads/sophia_share.sh find    (then edit keep_folders.txt)"
    echo "       bash ~/Downloads/sophia_share.sh zip"
    ;;
esac
