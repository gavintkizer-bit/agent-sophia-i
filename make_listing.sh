#!/bin/bash
# make_listing.sh: run this ON YOUR MAC to list the files in one folder.
# It only READS names, dates, and sizes. It never opens, moves, or changes a file.
#
#   bash make_listing.sh ~/Downloads
#
# It writes file_listing.txt to your Desktop. Upload that to the repo at
# workspace/inbox/file_listing.txt. Only files directly in the folder are listed
# (not files inside subfolders), and hidden files are skipped.
set -u

DIR="${1:-}"
if [ -z "$DIR" ] || [ ! -d "$DIR" ]; then
  echo "Usage: bash make_listing.sh /path/to/folder   (for example: ~/Downloads)"
  exit 1
fi

BASE="$(cd "$DIR" && pwd -P)" || exit 1
OUT="$HOME/Desktop/file_listing.txt"

{
  echo "# base: $BASE"
  cd "$BASE" && find . -maxdepth 1 -type f ! -name '.*' ! -name $'*\n*' \
    -exec stat -f '%Sm|%z|%N' -t '%Y-%m-%d' {} + | sort -t '|' -k3
} > "$OUT"

COUNT=$(($(wc -l < "$OUT") - 1))
echo "Listed $COUNT file(s) from $BASE"
echo "Saved to: $OUT"
echo "Next: upload it to GitHub as workspace/inbox/file_listing.txt"
