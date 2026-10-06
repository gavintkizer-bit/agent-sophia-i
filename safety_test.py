"""
Free safety checks (no model calls): the protections that matter most, tested by code so a
change can't quietly undo them. Cal's audit (2026-10-06): the drills test the helpers, but
nothing tested the music protection, the helpers' tool lists or the owner's constitutions.

  python safety_test.py              # run every check (train.py also runs it first)
  python safety_test.py --rehash     # after the OWNER changes a constitution: record the new text

Exit code 1 if any check fails.
"""

import hashlib
import json
import pathlib
import re
import sys

import agent
import archivist
from make_mac_script import is_protected, safe_folder

ROOT = agent.ROOT
HASHES = ROOT / "agents" / "constitutions.json"
CONSTITUTIONS = {"SOPHIA.md": "## Constitution", "agents/archivist.md": "## Constitution"}


def constitution(path: str) -> str:
    """The constitution block: from its heading to the next heading."""
    text = (ROOT / path).read_text()
    start = text.index(CONSTITUTIONS[path])
    end = text.find("\n## ", start + 1)
    return text[start: end if end != -1 else None]


def digest(path: str) -> str:
    return hashlib.sha256(constitution(path).encode()).hexdigest()


def checks():
    # Music, Ableton, sample, video and gear files stay put (the owner's first rule).
    for name in ["song.wav", "VIBES MASTER.als 2", "x.als (1)", "pack.alp", "clip.mp4", "set.mov",
                 "Drum Kit Vol 2.zip", "Splice Installer.dmg", "Serum_x64.pkg", "vocal stems.rar"]:
        yield f"protected: {name}", is_protected(name)
    for name in ["invoice.pdf", "photo.jpg", "Firefox.dmg", "notes.txt"]:
        yield f"not protected: {name}", not is_protected(name)
    # Scripts may only move into the owner's chosen homes, never into ~/Library or out of home.
    for folder in ["~/Library/x", "~/Music/Ableton", "/Applications", "~/../etc", "~/Music"]:
        yield f"unsafe folder refused: {folder}", not safe_folder(folder)
    for folder in ["~/Music/Sound Library", "~/Documents/School"]:
        yield f"safe folder allowed: {folder}", safe_folder(folder)
    # Each helper has an exact tool list (unlisted tools used to be available: SendUserFile).
    src = (ROOT / "agent.py").read_text()
    yield "Hypatia's tools are exact", 'tools=["Read", "Write", "Edit", "Glob", "Grep"]' in src
    yield "Callimachus's tools are exact", archivist.BUILTIN_TOOLS == [
        "Read", "Write", "Edit", "Glob", "Grep", "WebSearch", "WebFetch"]
    # Fences.
    yield "Hypatia can't write my memory", bool(agent.write_problem("notes/sophia_memory.md"))
    yield "Hypatia can't read outside the workspace", bool(agent.read_problem("../CLAUDE.md"))
    yield "Cal can't write outside his archive", bool(archivist.write_problem("CLAUDE.md"))
    yield "Cal can't read secrets", bool(archivist.read_problem(".env.local"))
    yield "Cal can't search private terms", bool(archivist.private_problem("Gavin R. Lowe album"))
    yield "Cal can't fetch private terms in URLs", bool(archivist.private_problem("https://x.com/void-speach"))
    yield "Cal may search a normal topic", not archivist.private_problem("Hermeticism primary texts")
    # The owner's constitutions are unchanged (only the owner changes them).
    saved = json.loads(HASHES.read_text()) if HASHES.exists() else {}
    for path in CONSTITUTIONS:
        yield f"constitution unchanged: {path}", saved.get(path) == digest(path)


def main():
    if "--rehash" in sys.argv:
        HASHES.write_text(json.dumps({p: digest(p) for p in CONSTITUTIONS}, indent=1) + "\n")
        print(f"Recorded constitution hashes in {HASHES.relative_to(ROOT)}. Only after an owner edit!")
        return
    failed = [name for name, ok in checks() if not ok]
    total = sum(1 for _ in checks())
    for name in failed:
        print(f"[FAIL] {name}")
    print(f"safety: {total - len(failed)}/{total} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
