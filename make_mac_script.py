"""
make_mac_script.py: turns the agent's organize_plan.json into a SAFE script for your Mac.

Run (in the cloud session):
    python make_mac_script.py
    python make_mac_script.py --listing L.txt --plan P.json --out DIR   (used by sophia.py)

Reads:   workspace/inbox/file_listing.txt, workspace/organize_plan.json
Writes:  workspace/out/organize.sh            (the script you run on your Mac)
         workspace/out/organize_preview.md    (read this before running anything)

Safety built into organize.sh:
- DRY RUN by default: it only prints what it would do. Add --go to actually move files.
- Never overwrites: skips any file whose destination already exists.
- Skips files that have been moved or deleted since the listing was made.
- Writes an undo script for every move it makes.
- Only moves files; never deletes or renames anything.
- Never moves audio or Ableton files (PROTECTED below), whatever the plan says,
  because Ableton projects find their samples by location.
"""
import argparse
import json
import pathlib
import shlex
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent
LISTING = ROOT / "workspace" / "inbox" / "file_listing.txt"
PLAN = ROOT / "workspace" / "organize_plan.json"
OUT = ROOT / "workspace" / "out"

# Audio and Ableton files never move: Ableton projects find samples by their location.
# (.alp Live Packs are installers, not samples, so they are not on this list.)
PROTECTED = {
    ".wav", ".aif", ".aiff", ".mp3", ".m4a", ".flac", ".ogg", ".caf", ".mid", ".midi",
    ".asd", ".als", ".adg", ".adv", ".agr", ".alc", ".ams", ".amxd", ".ask", ".rx2",
}


def is_protected(path):
    return pathlib.PurePosixPath(path).suffix.lower() in PROTECTED


def fail(msg):
    sys.exit(f"[FAIL] {msg}")


def read_listing(LISTING=LISTING):
    if not LISTING.exists():
        fail(f"Missing {LISTING}. Upload your file listing there first.")
    lines = LISTING.read_text(encoding="utf-8", errors="replace").splitlines()
    base, files = None, {}
    for line in lines:
        if line.startswith("# base:"):
            base = line.split(":", 1)[1].strip()
        elif line.startswith("#"):
            continue
        elif line.strip():
            parts = line.split("|", 2)
            if len(parts) == 3:
                files[parts[2]] = {"date": parts[0], "size": parts[1]}
    if not base:
        fail("The listing's first line must be '# base: /path/to/folder'.")
    if not files:
        fail("No files found in the listing.")
    return base, files


def safe_folder(folder):
    p = pathlib.PurePosixPath(folder.strip())
    return (
        folder.strip() != ""
        and not p.is_absolute()
        and not folder.strip().startswith("~")
        and ".." not in p.parts
    )


def main():
    global PLAN, OUT
    ap = argparse.ArgumentParser(description="Turn a plan into a safe Mac script.")
    ap.add_argument("--listing", default=str(LISTING))
    ap.add_argument("--plan", default=str(PLAN))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--name", default="organize.sh", help="script filename (unique per folder)")
    ap.add_argument("--made", default="", help="date of the listing, printed by the script")
    args = ap.parse_args()
    PLAN, OUT = pathlib.Path(args.plan).resolve(), pathlib.Path(args.out).resolve()

    base, listed = read_listing(pathlib.Path(args.listing).resolve())
    if not PLAN.exists():
        fail(f"Missing {PLAN}. Run the agent first.")
    try:
        plan = json.loads(PLAN.read_text())
    except json.JSONDecodeError as e:
        fail(f"organize_plan.json isn't valid JSON: {e}")

    problems, moves, seen = [], [], set()
    dest_names = defaultdict(list)

    for m in plan.get("moves", []):
        f, folder = m.get("file", ""), m.get("to_folder", "")
        if f not in listed:
            problems.append(f"Not in listing (skipped): {f}")
            continue
        if f in seen:
            problems.append(f"Listed twice (kept first): {f}")
            continue
        if is_protected(f):
            continue  # audio/Ableton: always left alone (reported below)
        if not safe_folder(folder):
            problems.append(f"Unsafe folder '{folder}' for {f} (skipped)")
            continue
        seen.add(f)
        folder = str(pathlib.PurePosixPath(folder.strip()))
        name = pathlib.PurePosixPath(f).name
        dest_names[(folder, name)].append(f)
        moves.append({"file": f, "to_folder": folder, "reason": m.get("reason", "")})

    leave = []
    for item in plan.get("leave_alone", []):
        f = item.get("file", "")
        if f in listed and f not in seen:
            seen.add(f)
            leave.append(item)

    for f in listed:
        if f not in seen and is_protected(f):
            seen.add(f)
            leave.append({"file": f, "reason": "Audio/Ableton file: never moved"})
    for f in listed:
        if f not in seen:
            leave.append({"file": f, "reason": "Not mentioned in the plan, so left alone"})
            problems.append(f"Not in plan (left alone): {f}")

    for (folder, name), srcs in dest_names.items():
        if len(srcs) > 1:
            problems.append(f"Name clash in {folder}/: {name} (only the first will move)")

    OUT.mkdir(parents=True, exist_ok=True)

    # ---- organize.sh
    q = shlex.quote
    sh = [
        "#!/bin/bash",
        "# Generated by Sophia. READ organize_preview.md FIRST.",
        f"#   Preview (moves nothing):  bash {args.name}",
        f"#   Do it for real:           bash {args.name} --go",
        "set -u",
        f"BASE={q(base)}",
        f"echo {q('Sophia plan for ' + base + (' (from your scan of ' + args.made + ')' if args.made else ''))}",
        'GO=0; [ "${1:-}" = "--go" ] && GO=1',
        'cd "$BASE" || { echo "Cannot open $BASE"; exit 1; }',
        'UNDO="$BASE/undo_organize_$(date +%Y%m%d_%H%M%S).sh"',
        "moved=0; skipped=0",
        'if [ "$GO" -eq 1 ]; then',
        '  { echo "#!/bin/bash"; printf "cd %q || exit 1\\n" "$BASE"; } > "$UNDO"',
        "fi",
        "move_one() {",
        '  src="$1"; dir="$2"; dest="$dir/$(basename "$src")"',
        '  if [ ! -e "$src" ]; then echo "SKIP (no longer there): $src"; skipped=$((skipped+1)); return; fi',
        '  if [ -e "$dest" ]; then echo "SKIP (already exists): $dest"; skipped=$((skipped+1)); return; fi',
        '  if [ "$GO" -eq 1 ]; then',
        '    mkdir -p "$dir" && mv -n "$src" "$dest" && printf "mv -n %q %q\\n" "$dest" "$src" >> "$UNDO" \\',
        '      && moved=$((moved+1)) && echo "MOVED: $src -> $dir/"',
        "  else",
        '    echo "WOULD MOVE: $src -> $dir/"; moved=$((moved+1))',
        "  fi",
        "}",
        "",
    ]
    for m in moves:
        sh.append(f"move_one {q(m['file'])} {q(m['to_folder'])}")
    sh += [
        "",
        'echo ""',
        'if [ "$GO" -eq 1 ]; then',
        '  echo "Done. Moved $moved file(s), skipped $skipped."',
        '  echo "To undo everything: bash \\"$UNDO\\""',
        "else",
        '  echo "PREVIEW ONLY. $moved file(s) would move, $skipped would be skipped."',
        f'  echo "Nothing was changed. To do it for real: bash {args.name} --go"',
        "fi",
    ]
    (OUT / args.name).write_text("\n".join(sh) + "\n")

    # ---- organize_preview.md
    by_folder = defaultdict(list)
    for m in moves:
        by_folder[m["to_folder"]].append(m)
    md = [
        "# Organize preview",
        "",
        f"Folder: `{base}`  ",
        f"Files in listing: {len(listed)} | Will move: {len(moves)} | Left alone: {len(leave)}",
        "",
    ]
    if problems:
        md += ["## Warnings", ""] + [f"- {p}" for p in problems] + [""]
    md += ["## Moves", ""]
    for folder in sorted(by_folder):
        md.append(f"### {folder}/ ({len(by_folder[folder])})")
        md += [f"- `{m['file'][2:] if m['file'].startswith('./') else m['file']}`: {m['reason']}"
               for m in by_folder[folder]]
        md.append("")
    md += ["## Left alone", ""]
    md += [f"- `{i['file']}`: {i.get('reason', '')}" for i in leave] or ["- (none)"]
    (OUT / "organize_preview.md").write_text("\n".join(md) + "\n")

    print(f"[ OK ] {len(moves)} moves, {len(leave)} left alone, {len(problems)} warning(s)")
    for p in problems:
        print(f"   - {p}")
    print(f"Wrote {OUT / args.name} and {OUT / 'organize_preview.md'}")


if __name__ == "__main__":
    main()
