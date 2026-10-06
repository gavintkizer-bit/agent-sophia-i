"""
sophia.py: one command that processes whatever the owner uploaded to workspace/inbox/.

    python sophia.py              # process new uploads
    python sophia.py --dry        # show what it would do, no agent runs (free)

What it does with each upload:
  disk_survey.txt     -> workspace/survey_summary.md (math done in code), then the agent writes
                         workspace/cleanup_report.md (where the space is, what's safe to remove)
  listing_<Name>.txt  -> a plan for that folder, then workspace/out/<Name>/organize.sh + preview
                         Simple files are sorted by fixed RULES (free, predictable). Only the
                         files the rules can't place go to the agent, in small batches.
Then it moves the processed uploads to workspace/inbox/processed/ and rewrites
workspace/STATUS.md: what's ready for the owner and what Sophia needs next.

Safety: nothing here touches the Mac. organize.sh only MOVES files (dry run by default, with
undo). Things that look deletable are moved into "_Sophia To Delete/" for the owner to review
and drag to the Trash. Audio and Ableton files are never moved.
"""
import argparse
import datetime
import json
import pathlib
import re
import shlex
import shutil
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent
WS = ROOT / "workspace"
INBOX = WS / "inbox"
PROCESSED = INBOX / "processed"
DRY = ROOT / "workspace" / "_dry"            # --dry writes here only
PLANS = WS / "plans"
OUT = WS / "out"
BATCH_LISTING = INBOX / "_batch.txt"
BATCH_PLAN = WS / "_batch_plan.json"
BATCH_SIZE = 100
TO_DELETE = "~/Downloads/_Sophia To Delete"  # one review folder for every scan

sys.path.insert(0, str(ROOT))
from make_mac_script import is_protected  # noqa: E402  (one shared list of protected types)

# One home per kind of file (owner, 2026-10-05: "clean and easy to find"; music is a separate plan).
EXT_FOLDER = {
    "~/Documents/Papers": "pdf doc docx pages txt rtf md csv xls xlsx numbers key ppt pptx odt ods",
    "~/Documents/Books": "epub mobi azw azw3",
    "~/Pictures/Images": "png jpg jpeg heic gif webp tif tiff bmp svg",
    "~/Downloads/Web Pages": "html htm webarchive",
    "~/Documents/Code": "py js ts json ipynb rb go c cpp h java",
}
EXT_FOLDER = {e: f for f, exts in EXT_FOLDER.items() for e in exts.split()}
ALLOWED = set(EXT_FOLDER.values()) | {"~/Documents/School", "~/Documents/Finance", "~/Pictures/Photos",
                                      "~/Pictures/Screenshots", "~/Downloads/Installers", "~/Downloads/Archives"}
FINANCE = re.compile(r"invoice|receipt|statement|tax|w-?2\b|1099|bank|pay ?stub|paycheck", re.I)
SCHOOL = re.compile(r"assignment|homework|quiz|\bexam\b|midterm|syllabus|lecture|lab report|essay|"
                    r"study|academic|answers|worksheet|questions|scientific method|test anxiety|\bclass\b|course", re.I)
SCREENSHOT = re.compile(r"^screen ?shot|^screenshot|^screen recording", re.I)
PHOTO = re.compile(r"^(img|dsc|pxl|photo)[_ -]?\d|^\d{8,}( \(\d+\))?\.\w+$|^\d{8}_\d{6}|_n\.(jpe?g|png)$", re.I)
# Secrets stay put and get flagged: the owner should keep them in a password manager, not Downloads.
SENSITIVE = re.compile(r"recovery.?codes?|backup.?codes?|password|private.?key|seed.?phrase|\.pem$", re.I)
# Leftovers from Sophia's earlier tools that nothing uses anymore.
LEFTOVER = re.compile(r"^(file_listing\.txt|organize_\w+\.txt)$", re.I)
# Sophia's own scripts and undo files never move, or the owner's commands would stop working.
OWN_SCRIPT = re.compile(r"^(organize|undo_organize|sophia_scan|make_listing)[^/]*\.sh$", re.I)
COPY = re.compile(r"^(?P<stem>.+?)(?: \(\d+\)| \d+)(?P<ext>\.[^./]+)?$")


# ---------------------------------------------------------------- listings
def read_listing(path):
    base, made, rows = None, None, []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# base:"):
            base = line.split(":", 1)[1].strip()
        elif line.startswith("# made:"):
            made = line.split(":", 1)[1].strip()
        elif line.strip() and not line.startswith("#"):
            parts = line.split("|", 2)
            if len(parts) == 3:
                rows.append({"date": parts[0], "size": int(parts[1] or 0), "file": parts[2]})
    return base, made, rows


def rule_sort(rows, made):
    """Return (moves, leave, unknown). Fixed rules for everything that's obvious."""
    today = datetime.date.fromisoformat(made) if made else datetime.date.today()
    recent = (today - datetime.timedelta(days=7)).isoformat()
    by_name = {(r["file"], r["size"]) for r in rows}
    moves, leave, unknown = [], [], []
    for r in rows:
        f = r["file"]
        name = pathlib.PurePosixPath(f).name
        ext = pathlib.PurePosixPath(f).suffix.lower().lstrip(".")
        copy = COPY.match(name)
        if is_protected(f):
            leave.append({"file": f, "reason": "Audio, video, Ableton, or sample file: never moved"})
        elif SENSITIVE.search(name):
            leave.append({"file": f, "reason": "Looks like a secret: keep it in a password manager instead"})
        elif OWN_SCRIPT.match(name):
            leave.append({"file": f, "reason": "Sophia's own script: stays where your commands expect it"})
        elif LEFTOVER.match(name):
            moves.append({"file": f, "to_folder": f"{TO_DELETE}/Sophia leftovers",
                          "reason": "Old Sophia file nothing uses anymore"})
        elif r["date"] >= recent:
            leave.append({"file": f, "reason": "Changed in the last 7 days"})
        elif copy and ("./" + copy["stem"] + (copy["ext"] or ""), r["size"]) in by_name:
            moves.append({"file": f, "to_folder": f"{TO_DELETE}/Duplicates",
                          "reason": "Exact copy of another file here"})
        elif ext in ("dmg", "pkg", "mpkg"):
            moves.append({"file": f, "to_folder": f"{TO_DELETE}/Installers",
                          "reason": "Installer; app is likely already installed"})
        elif ext in EXT_FOLDER:
            folder = EXT_FOLDER[ext]
            if folder == "~/Documents/Papers":
                folder = ("~/Documents/Finance" if FINANCE.search(name)
                          else "~/Documents/School" if SCHOOL.search(name) else folder)
            elif folder == "~/Pictures/Images":
                folder = ("~/Pictures/Screenshots" if SCREENSHOT.search(name)
                          else "~/Pictures/Photos" if PHOTO.search(name) else folder)
            moves.append({"file": f, "to_folder": folder, "reason": f".{ext} file"})
        else:
            unknown.append(r)
    school_topics(moves)
    return moves, leave, unknown


OWNER = {"gavin", "kizer"}  # the owner's name is on everything they write, so it isn't a topic


def school_topics(moves):
    """A paper that shares a two-word topic with a school file goes to School too
    ("Blended Rock Deformation and Earthquakes.key" next to "Assignment #4 Rock Deformation")."""
    def pairs(f):
        words = re.findall(r"[a-z]{3,}", pathlib.PurePosixPath(f).stem.lower())
        return {(a, b) for a, b in zip(words, words[1:]) if a not in OWNER and b not in OWNER}
    topics = set().union(*(pairs(m["file"]) for m in moves if m["to_folder"] == "~/Documents/School"))
    for m in moves:
        if m["to_folder"] == "~/Documents/Papers" and pairs(m["file"]) & topics:
            m["to_folder"], m["reason"] = "~/Documents/School", "Same topic as a school file"


def agent_sort(base, made, unknown, dry):
    """Ask the agent about the files the rules couldn't place, BATCH_SIZE at a time."""
    moves, leave = [], []
    batches = [unknown[i:i + BATCH_SIZE] for i in range(0, len(unknown), BATCH_SIZE)]
    for n, batch in enumerate(batches, 1):
        names = {r["file"] for r in batch}
        print(f"   agent batch {n}/{len(batches)} ({len(batch)} files)")
        if dry:
            leave += [{"file": f, "reason": "(dry run)"} for f in names]
            continue
        BATCH_LISTING.write_text(f"# base: {base}\n# made: {made or ''}\n" + "".join(
            f"{r['date']}|{r['size']}|{r['file']}\n" for r in batch))
        BATCH_PLAN.unlink(missing_ok=True)
        subprocess.run([sys.executable, str(ROOT / "agent.py"), str(ROOT / "tasks" / "organize_batch.md")],
                       cwd=ROOT, check=False)
        try:
            plan = json.loads(BATCH_PLAN.read_text())
        except (OSError, json.JSONDecodeError) as e:
            print(f"   [warn] batch {n} gave no usable plan ({e}); leaving those files alone")
            plan = {}
        done = set()
        for m in plan.get("moves", []):
            if str(m.get("to_folder", "")).strip().strip("/") not in ALLOWED:
                continue  # only the folders in preferences.md
            if m.get("file") in names and m["file"] not in done:
                done.add(m["file"])
                moves.append({**m, "to_folder": str(m.get("to_folder", "")).strip().strip("/")})
        for f in names - done:
            reason = next((i.get("reason", "") for i in plan.get("leave_alone", []) if i.get("file") == f),
                          "Sophia wasn't sure, so left alone")
            leave.append({"file": f, "reason": reason})
    BATCH_LISTING.unlink(missing_ok=True)
    BATCH_PLAN.unlink(missing_ok=True)
    return moves, leave


def process_listing(path, dry):
    name = path.stem.removeprefix("listing_") if path.stem != "file_listing" else "Downloads"
    base, made, rows = read_listing(path)
    if not base or not rows:
        print(f"[skip] {path.name}: no '# base:' line or no files")
        return None
    moves, leave, unknown = rule_sort(rows, made)
    print(f"== {name}: {len(rows)} files | rules placed {len(moves)}, protected/recent {len(leave)}, "
          f"asking Sophia about {len(unknown)}")
    a_moves, a_leave = agent_sort(base, made, unknown, dry)
    plan = {"moves": moves + a_moves, "leave_alone": leave + a_leave}
    # --dry used to overwrite the real plans and scripts with "(dry run)" leaves (Cal's audit,
    # 2026-10-06), so a dry run now writes only to a scratch folder.
    plans_dir, out_dir = (DRY / "plans", DRY / "out") if dry else (PLANS, OUT)
    plans_dir.mkdir(parents=True, exist_ok=True)
    plan_path = plans_dir / f"{name}.json"
    plan_path.write_text(json.dumps(plan, indent=1, ensure_ascii=False))
    out = out_dir / name
    subprocess.run([sys.executable, str(ROOT / "make_mac_script.py"), "--listing", str(path),
                    "--plan", str(plan_path), "--out", str(out), "--name", f"organize_{name}.sh",
                    "--made", made or ""], cwd=ROOT, check=True, stdout=subprocess.DEVNULL)
    counts = Counter(m["to_folder"] for m in plan["moves"] if not is_protected(m["file"]))
    review = {k: v for k, v in counts.items() if k.startswith(TO_DELETE)}
    review_bytes = sum(r["size"] for r in rows for m in plan["moves"]
                       if m["file"] == r["file"] and m["to_folder"].startswith(TO_DELETE))
    return {"name": name, "base": base, "files": len(rows), "moves": sum(counts.values()),
            "left": len(rows) - sum(counts.values()), "counts": counts, "review": review,
            "review_gb": review_bytes / 1e9}


# ---------------------------------------------------------------- disk survey
def gb(kb):
    return f"{int(kb) / 1e6:.1f} GB"


def summarize_survey(path):
    sections, cur = defaultdict(list), None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
        elif line.startswith("# "):
            k, _, v = line[2:].partition(":")
            sections["meta"].append((k.strip(), v.strip()))
        elif cur and line.strip():
            sections[cur].append(line)
    meta = dict(sections["meta"])
    home = meta.get("home", "")

    def sizes(key):
        out = []
        for line in sections.get(key, []):
            kb, _, p = line.partition("\t")
            if kb.strip().isdigit():
                out.append((int(kb), p))
        return sorted(out, reverse=True)

    md = [f"# Disk survey summary ({meta.get('made', 'date unknown')})", ""]
    md += ["## macOS", ""] + [f"- {l}" for l in sections.get("macos", [])] + [""]
    disk = [l.split() for l in sections.get("disk (1K blocks)", [])[1:]]
    if disk and len(disk[0]) >= 4:
        # On APFS, df's "Used" for / is only the system volume, so derive used from free.
        total, free = int(disk[0][1]), int(disk[0][3])
        md += ["## Disk", "", f"- Size {gb(total)} | Used {gb(total - free)} | **Free {gb(free)}**", ""]
    md += ["## Biggest folders in your home folder", ""]
    md += [f"- {gb(kb)}  `{p.replace(home, '~')}`" for kb, p in sizes("home folders (KB, 2 levels deep)")[:30]]
    md += ["", "## Biggest folders inside ~/Library (app data, caches, backups)", ""]
    md += [f"- {gb(kb)}  `{p.replace(home, '~')}`" for kb, p in sizes("library folders (KB, 3 levels deep)")[:30]]
    md += ["", "## Biggest single files (100 MB+)", ""]
    for line in sections.get("big files (100 MB or more; date|bytes|path)", [])[:60]:
        d, s, p = (line.split("|", 2) + ["", ""])[:3]
        if s.isdigit():
            md.append(f"- {int(s) / 1e9:.2f} GB  {d}  `{p.replace(home, '~')}`")
    md += ["", "## Biggest apps", ""]
    md += [f"- {gb(kb)}  `{p}`" for kb, p in sizes("apps (KB)")[:30]]
    snaps = [l for l in sections.get("time machine local snapshots", []) if "com.apple" in l]
    md += ["", "## Time Machine local snapshots", "", f"- {len(snaps)} snapshot(s)", ""]
    (WS / "survey_summary.md").write_text("\n".join(md) + "\n")
    print("== disk survey: wrote workspace/survey_summary.md")


# ---------------------------------------------------------------- status page
def write_all(results):
    """One script for the owner to download: every folder's script, run in turn (same preview / --go)."""
    parts = [r for r in results if r["moves"]]
    if not parts:
        return
    sh = ["#!/bin/bash", "# Generated by Sophia: organizes every folder from your latest scan in one go.",
          "#   Preview (moves nothing):  bash ~/Downloads/organize_all.sh",
          "#   Do it for real:           bash ~/Downloads/organize_all.sh --go",
          "# Each folder saves its own undo script in that folder.", ""]
    for n, r in enumerate(parts, 1):
        body = (OUT / r["name"] / f"organize_{r['name']}.sh").read_text()
        sh += [f'echo ""; echo "=== {n}/{len(parts)}: {r["base"]} ==="',
               f"bash -s -- \"$@\" <<'SOPHIA_PART_{n}'", body.rstrip("\n"), f"SOPHIA_PART_{n}", ""]
    # Folders Sophia made inside Downloads that are now empty (rmdir refuses anything not empty).
    emptied = [r["base"] for r in parts if r["base"].count("/") > 3 and "/Downloads/" in r["base"]]
    if emptied:
        sh += ['if [ "${1:-}" = "--go" ]; then']
        sh += [f"  rmdir {shlex.quote(b)} 2>/dev/null && echo {shlex.quote('Removed empty folder ' + b)}"
               for b in sorted(emptied, key=len, reverse=True)]
        sh += ["fi"]
    path = OUT / "organize_all.sh"
    path.write_text("\n".join(sh) + "\n")
    print(f"== wrote {path.relative_to(ROOT)} ({len(parts)} folders)")


def write_status(results, survey_done):
    lines = ["# Sophia status", "", f"_Updated {datetime.date.today().isoformat()}_", "",
             "## Ready for you to run on your Mac", ""]
    if (OUT / "organize_all.sh").exists():
        url = "https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/organize_all.sh"
        lines += [f"One script for everything: [organize_all.sh]({url}). Control-click > Save Link As..., save in Downloads.",
                  "Previews for each folder: `workspace/out/<folder>/organize_preview.md`.", "",
                  "```", "bash ~/Downloads/organize_all.sh        # preview, changes nothing",
                  "bash ~/Downloads/organize_all.sh --go   # moves files; undo files go to Documents/Sophia/Undo",
                  "```", "", "If your Mac saved it as `organize_all (1).sh`, delete the old one and rename",
                  "the new one, so you never run an outdated script.", ""]
    else:
        lines += ["- Nothing yet.", ""]
    for r in results:
        lines += [f"### Latest run: {r['name']}", "",
                  f"- {r['files']} files: {r['moves']} will move, {r['left']} stay put "
                  f"(audio/Ableton, recent, or unclear).",
                  "- Folders: " + ", ".join(f"{k} {v}" for k, v in sorted(r["counts"].items())), ""]
        if r["review"]:
            lines += [f"- **{r['review_gb']:.1f} GB** goes to `{TO_DELETE}/` for you to check, then drag to the Trash.", ""]
    if survey_done or (WS / "cleanup_report.md").exists():
        lines += ["## Where your disk space goes", "", "See `workspace/cleanup_report.md`.", ""]
    lines += ["## What Sophia needs from you", "",
              "- New scan when you've run a script or want fresh numbers: `bash ~/Downloads/sophia_scan.sh`,"
              " then upload `~/Desktop/sophia_upload/*` to `workspace/inbox/` on GitHub.", ""]
    (WS / "STATUS.md").write_text("\n".join(lines))
    print("== wrote workspace/STATUS.md")


def check_report(path):
    """Flag music items in the report's "Biggest wins". Hypatia once listed .alp packs as safe to trash (2026-10-05)."""
    if not path.exists():
        return []
    from make_mac_script import is_protected, MUSIC_GEAR
    words = re.compile(r"\.alp\b|ableton|sample|splice|\.wav\b|\.aif|\.mp4|\.mov|\.mkv|video", re.I)
    section, bad = "", []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line.lower()
            continue
        if "biggest wins" not in section:
            continue
        names = re.findall(r"`([^`]+)`", line)
        if words.search(line) or MUSIC_GEAR.search(line) or any(is_protected(n) for n in names):
            bad.append(line.strip())
    for line in bad:
        print(f"[WARN] report suggests touching music material; Sophia must fix it: {line[:120]}")
    return bad


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Process new uploads in workspace/inbox/.")
    ap.add_argument("--dry", action="store_true", help="no agent runs, no files moved, STATUS.md unchanged")
    args = ap.parse_args()

    # Scans arrive as one sophia_scan.zip (GitHub's upload page takes 25 MB per file), sometimes one folder up.
    for z in [INBOX / "sophia_scan.zip", WS / "sophia_scan.zip"]:
        if z.exists():
            import zipfile
            with zipfile.ZipFile(z) as zf:
                for m in zf.namelist():
                    if m.endswith(".txt") and "/" not in m.lstrip("./"):
                        (INBOX / pathlib.PurePosixPath(m).name).write_bytes(zf.read(m))
            if not args.dry:
                PROCESSED.mkdir(parents=True, exist_ok=True)
                shutil.move(str(z), PROCESSED / datetime.datetime.now().strftime("scan_%Y-%m-%d_%H%M.zip"))
            print(f"== unpacked {z.name}")
    listings = sorted(INBOX.glob("listing_*.txt")) + sorted(INBOX.glob("file_listing.txt"))
    survey = INBOX / "disk_survey.txt"
    if not listings and not survey.exists():
        # Leave STATUS.md alone: rewriting it with no results erased the last run's summary.
        print("Nothing new in workspace/inbox/. Waiting for the owner to upload a scan.")
        return

    results = [r for r in (process_listing(p, args.dry) for p in listings) if r]
    if survey.exists():
        summarize_survey(survey)
        if not args.dry:
            report = WS / "cleanup_report.md"
            previous = report.read_text(encoding="utf-8") if report.exists() else None
            subprocess.run([sys.executable, str(ROOT / "agent.py"), str(ROOT / "tasks" / "disk_report.md")],
                           cwd=ROOT, check=False)
            if check_report(report):
                # A prompt rule didn't stop her twice (2026-10-05); the owner must never see a flagged draft.
                shutil.move(str(report), WS / "cleanup_report_draft.md")
                if previous is not None:
                    report.write_text(previous, encoding="utf-8")
                print("== flagged draft kept as workspace/cleanup_report_draft.md; previous report restored")
    if args.dry:
        print("== dry run: workspace/STATUS.md not changed")
        return
    write_all(results)
    write_status(results, survey.exists())

    stamp = PROCESSED / datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    stamp.mkdir(parents=True, exist_ok=True)
    for p in listings + ([survey] if survey.exists() else []):
        shutil.move(str(p), stamp / p.name)
    print(f"== moved uploads to {stamp.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
