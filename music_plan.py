#!/usr/bin/env python3
"""music_plan.py: plan the round that touches music, using the owner's music map.

Reads the scan's music_refs.txt (every sample/video each Ableton set, rack, or clip uses) and
music_files.txt (every file in Downloads and Desktop). A music file may move only if NO project
mentions it, by full path or even by bare name (Live 10 sets store only names). Such files go to
~/Music/Sound Library, a new folder; ~/Music/Ableton is never touched. Folders move whole, never
split. Everything else stays exactly where it is.

    python music_plan.py workspace/inbox            # writes plans, scripts, and organize_all.sh
"""
import html
import json
import pathlib
import posixpath
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import sophia  # noqa: E402
from make_mac_script import SOUND_LIBRARY, is_protected  # noqa: E402

TO_DELETE = sophia.TO_DELETE
AUDIO = (".wav", ".aif", ".aiff", ".mp3", ".m4a", ".flac", ".ogg", ".caf")


def load_map(scan):
    exact, names = set(), set()
    for line in (scan / "music_refs.txt").read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("#") or "\t" not in line:
            continue
        project, ref = line.split("\t", 1)
        ref = html.unescape(ref)
        if "/" in ref:
            full = ref if ref.startswith("/") else posixpath.normpath(posixpath.join(posixpath.dirname(project), ref))
            exact.add(full)
            names.add(posixpath.basename(full).lower())
        else:
            names.add(ref.lower())
    files = [ln for ln in (scan / "music_files.txt").read_text(encoding="utf-8", errors="replace").splitlines()
             if ln.startswith("/")]
    return exact, names, files


def in_use(path, exact, names):
    """Most cautious test: the file (or the audio an .asd belongs to) is mentioned anywhere."""
    audio = path[:-4] if path.lower().endswith(".asd") else path
    return audio in exact or posixpath.basename(audio).lower() in names


def plan(scan):
    exact, names, files = load_map(scan)
    home = files[0].split("/Downloads/")[0].split("/Desktop/")[0]
    dl, desk, untitled = f"{home}/Downloads", f"{home}/Desktop", f"{home}/Downloads/untitled folder"
    present = set(files)

    def folder_unused(path):
        inside = [f for f in files if f.startswith(path + "/")]
        return bool(inside) and not any(in_use(f, exact, names) for f in inside)

    parts = {dl: [], desk: [], untitled: []}

    def add(base, name, to, reason, music=False):
        parts[base].append({"file": "./" + name, "to_folder": to, "reason": reason, "music_checked": music})

    # 1. Loose sounds in Downloads that no project uses (and their .asd analysis files).
    for f in sorted(files):
        if posixpath.dirname(f) != dl:
            continue
        name = posixpath.basename(f)
        low = name.lower()
        audio = low[:-4] if low.endswith(".asd") else low
        if audio.endswith(AUDIO) and not in_use(f, exact, names):
            if low.endswith(".asd") and f[:-4] not in present:
                continue  # an .asd whose audio is gone: leave it
            add(dl, name, f"{SOUND_LIBRARY}/Loose Sounds", "No project uses this sound", music=True)

    # 2. Whole sample folders no project uses.
    for name in ["Drum samples"]:
        if folder_unused(f"{dl}/{name}"):
            add(dl, name, f"{SOUND_LIBRARY}/Sample Packs", "No project uses any file in it", music=True)

    # 3. Non-music folders (checked by hand from the file list, 2026-10-06).
    mc = "~/Documents/Minecraft Worlds"
    for name in ["region", "entities", "poi", "playerdata", "advancements", "DIM-1", "DIM1", "data", "stats"]:
        add(dl, name, f"{mc}/Loose world files", "Piece of a Minecraft world")
    for name in ["hjk_files", "Jackdaw _ Assassin's Creed Wiki _ FANDOM powered by Wikia_files"]:
        add(dl, name, "~/Downloads/Web Pages", "Files of a saved web page")
    add(dl, "Opera Installer.app", f"{TO_DELETE}/Installers", "Installer; Opera is already installed")
    add(dl, "mcedit2-macosx64-2.0.0-beta11", f"{TO_DELETE}/Minecraft", "Minecraft editor; the game can't run here")
    add(dl, "my-first-agent", "~/Documents/Code", "Code project")
    add(dl, "organizer", "~/Documents/Code", "Code project")
    for name in ["Stats.html.rtfd", "Stats.html 2.rtfd"]:
        add(dl, name, "~/Documents/Papers", "Document")
    packs = ["Ovos Rustic Redemption v1.4.1 - for 1.10.X", "1.14-Dokucraft-TSC-Dark", "1.11-Dokucraft-TSC-High",
             "Beyond+the+Lands", "Romecraft GERMANIA 16", "Farmland", "Hillster", "Andorhal HD",
             "Round+Trees+V.2.1.0+-+1.13", "Ovos Rustic Redemption v1.4.1 - for 1.10.X.zip", "Andorhal HD (1).zip",
             "1.11-Dokucraft-TSC-High.zip", "Hillster.zip", "Romecraft GERMANIA 16.zip", "Farmland.zip"]
    for name in packs:
        add(untitled, name, f"{mc}/Packs and maps", "Minecraft pack or map; no project uses it")
    add(desk, "Seaworthy Vessels", "~/Pictures", "Folder of pictures")
    add(desk, "Academic Adventures", "~/Documents/School", "School folder")
    add(desk, "All MTG decks", f"{TO_DELETE}/Games", "Cockatrice decks; you said they can go")

    # Safety: every music move must pass the check again; folders must not contain used files.
    for base, moves in parts.items():
        for m in moves:
            path = f"{base}/{m['file'][2:]}"
            inside = [f for f in files if f == path or f.startswith(path + "/")]
            assert not any(in_use(f, exact, names) for f in inside if is_protected(f)), path
    return parts


def main():
    scan = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "workspace/inbox")
    made = next((ln.split(":", 1)[1].strip() for ln in (scan / "music_files.txt").open() if ln.startswith("# made:")), "")
    results = []
    for base, moves in plan(scan).items():
        if not moves:
            continue
        name = "Music-" + posixpath.basename(base).replace(" ", "_")
        listing = sophia.WS / "plans" / f"{name}_listing.txt"
        listing.write_text(f"# base: {base}\n# made: {made}\n" + "".join(f"{made}|0|{m['file']}\n" for m in moves))
        plan_path = sophia.WS / "plans" / f"{name}.json"
        plan_path.write_text(json.dumps({"moves": moves, "leave_alone": []}, indent=1, ensure_ascii=False))
        subprocess.run([sys.executable, str(ROOT / "make_mac_script.py"), "--listing", str(listing), "--plan",
                        str(plan_path), "--out", str(sophia.OUT / name), "--name", f"organize_{name}.sh",
                        "--made", made, "--music-checked"], check=True, stdout=subprocess.DEVNULL)
        results.append({"name": name, "base": base, "moves": len(moves)})
        music = sum(m["music_checked"] for m in moves)
        print(f"== {name}: {len(moves)} moves ({music} checked-unused music)")
    sophia.write_all(results)


if __name__ == "__main__":
    main()
