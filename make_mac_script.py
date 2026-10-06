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
import re
import pathlib
import shlex
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent
LISTING = ROOT / "workspace" / "inbox" / "file_listing.txt"
PLAN = ROOT / "workspace" / "organize_plan.json"
OUT = ROOT / "workspace" / "out"

# Audio, Ableton, and sample files never move: Ableton projects find samples by their location,
# and the owner asked that nothing Ableton- or sample-related be moved (2026-10-05).
PROTECTED = {
    ".wav", ".aif", ".aiff", ".mp3", ".m4a", ".flac", ".ogg", ".caf", ".mid", ".midi",
    ".asd", ".als", ".adg", ".adv", ".agr", ".alc", ".ams", ".amxd", ".ask", ".rx2", ".alp",
    # Video too: the owner often puts videos in Ableton sets (2026-10-05).
    ".mov", ".mp4", ".m4v", ".mkv", ".avi", ".webm", ".3gp", ".wmv", ".flv", ".mpg", ".mpeg",
}
# Archives whose names sound like music material (sample packs, kits, racks, chains) also stay put.
ARCHIVES = (".zip", ".rar", ".7z", ".gz", ".tgz", ".tar")
MUSIC_WORDS = re.compile(
    r"sample|kit|drum|loop|808|acapella|vocal|stem|preset|ableton|beat|snare|kick|perc|"
    r"one.?shot|sound|synth|bass|chord|melod|midi|serum|splice|rack|chain|fx|instrument|"
    r"\blive\b|pack", re.I)


# Installers for music gear (plugins, drivers, Splice): old free ones often can't be re-downloaded.
INSTALLERS = (".dmg", ".pkg", ".mpkg", ".zip")
MUSIC_GEAR = re.compile(
    r"vst|plug.?in|splice|instrument|verb|voxengo|klanghelm|dc1a3|multiply|acon|behringer|"
    r"m.?audio|focusrite|boogex|deltamodulator|izotope|xfer|arturia|native.?instruments|ableton|"
    r"serum|vital|kontakt|massive|valhalla|fabfilter|waves|soundtoys|u.?he|spitfire|labs|"
    r"output|komplete|omnisphere|spectrasonics|toontrack|superior|addictive|audio", re.I)   # safety_test.py
COPY_MARK = re.compile(r"(?: \d+| \(\d+\))+$")


def is_protected(path):
    name = pathlib.PurePosixPath(path).name
    # "VIBES MASTER.als 2" is still an Ableton project: ignore copy marks after the extension.
    bare = COPY_MARK.sub("", name)
    if pathlib.PurePosixPath(bare).suffix.lower() in PROTECTED:
        return True
    low = name.lower()
    if low.endswith(ARCHIVES) and MUSIC_WORDS.search(name):
        return True
    return low.endswith(INSTALLERS) and bool(MUSIC_GEAR.search(name))


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


# A plan may also send files to these home folders ("~/Pictures/Screenshots"). Never ~/Music or ~/Library.
HOME_ROOTS = ("Documents", "Pictures", "Downloads", "Desktop")


# Music checked as unused by every Ableton project (music_plan.py) may go here, and only here.
# A new folder: it never touches ~/Music/Ableton or anything else already in ~/Music.
SOUND_LIBRARY = "~/Music/Sound Library"
# New music homes the owner chose (2026-10-05): one home for new songs, bounces, and the pre-2021 archive.
# All are new folders; nothing already in ~/Music is touched.
MUSIC_HOMES = (SOUND_LIBRARY, "~/Music/Projects", "~/Music/Bounces", "~/Music/Archive")


def safe_folder(folder):
    f = folder.strip()
    if f.startswith("~/"):
        p = pathlib.PurePosixPath(f[2:])
        if ".." in p.parts:
            return False
        if any(f == h or f.startswith(h + "/") for h in MUSIC_HOMES):
            return True
        return len(p.parts) >= 1 and p.parts[0] in HOME_ROOTS
    p = pathlib.PurePosixPath(f)
    return f != "" and not p.is_absolute() and not f.startswith("~") and ".." not in p.parts


def shell_folder(folder):
    """Quote a plan folder for bash; "~/X" becomes "$HOME"/'X'."""
    if folder.startswith("~/"):
        return '"$HOME"/' + shlex.quote(folder[2:])
    return shlex.quote(folder)


def main():
    global PLAN, OUT
    ap = argparse.ArgumentParser(description="Turn a plan into a safe Mac script.")
    ap.add_argument("--listing", default=str(LISTING))
    ap.add_argument("--plan", default=str(PLAN))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--name", default="organize.sh", help="script filename (unique per folder)")
    ap.add_argument("--made", default="", help="date of the listing, printed by the script")
    ap.add_argument("--music-checked", action="store_true",
                    help="allow music files marked music_checked (unused by every project) into ~/Music/Sound Library")
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
        music_ok = (args.music_checked and m.get("music_checked") is True
                    and any(str(folder).strip().startswith(h) for h in MUSIC_HOMES))
        if is_protected(f) and not music_ok:
            continue  # audio/Ableton: always left alone (reported below)
        if not safe_folder(folder):
            problems.append(f"Unsafe folder '{folder}' for {f} (skipped)")
            continue
        seen.add(f)
        folder = folder.strip()
        folder = "~/" + str(pathlib.PurePosixPath(folder[2:])) if folder.startswith("~/") else str(pathlib.PurePosixPath(folder))
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
            leave.append({"file": f, "reason": "Audio, video, Ableton, or sample file: never moved"})
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
        # One home for undo files, named per folder (several folders can run in the same second).
        f'UNDO="$HOME/Documents/Sophia/Undo/undo_{pathlib.PurePosixPath(args.name).stem.removeprefix("organize_")}_$(date +%Y%m%d_%H%M%S).sh"',
        "moved=0; skipped=0",
        'if [ "$GO" -eq 1 ]; then',
        '  mkdir -p "$HOME/Documents/Sophia/Undo" || exit 1',
        '  { echo "#!/bin/bash"; printf "mkdir -p %q && cd %q || exit 1\\n" "$BASE" "$BASE"; } > "$UNDO"',
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
        sh.append(f"move_one {q(m['file'])} {shell_folder(m['to_folder'])}")
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
