# Sophia's drive cleanup: how it works

Sophia never touches the Mac. She only sees what the owner uploads (sizes and filenames),
plans, and produces scripts the OWNER runs. Scripts only MOVE files (dry run by default,
with an undo script). Anything that looks deletable is moved into `_Sophia To Delete/` for the
owner to review and drag to the Trash. Audio, Ableton, sample, video and music-gear files are
never moved (`make_mac_script.py` PROTECTED; tested by `safety_test.py`), with ONE exception: a
music file that no Ableton set uses (checked by `music_plan.py` against every set) may move into the
owner's music homes, `~/Music/{Sound Library,Projects,Bounces,Archive}`, and only in a round the
owner approved in words (decision log, 2026-10-06). The repo is private; filenames are visible only to the owner.

## On the Mac (owner)
1. Download `sophia_scan.sh` (lands in Downloads). Run: `bash ~/Downloads/sophia_scan.sh`
   It READS ONLY and creates `~/Desktop/sophia_upload/` with `disk_survey.txt` and
   `listing_Downloads.txt`, `listing_Desktop.txt`, `listing_Documents.txt`.
2. Upload those files on GitHub into `workspace/inbox/` (Add file > Upload files, commit to main).
3. Later: download a ready `workspace/out/<Folder>/organize_<Folder>.sh`, run `bash organize_<Folder>.sh` (preview),
   then `bash organize_<Folder>.sh --go`. Check `_Sophia To Delete/` and drag what you agree with to the Trash.

## In a cloud session (Sophia / Claude)
1. `pip install -r requirements.txt` and `python agent.py --check`
2. `python sophia.py`. It handles every upload in `workspace/inbox/`:
   - listings: fixed rules sort obvious files; Hypatia (`tasks/organize_batch.md`) decides the
     rest in batches of 100; writes `workspace/plans/<Folder>.json` and `workspace/out/<Folder>/`.
   - disk survey: `workspace/survey_summary.md` (code) and `workspace/cleanup_report.md` (Hypatia,
     `tasks/disk_report.md`).
   - moves processed uploads to `workspace/inbox/processed/<date>/` and rewrites `workspace/STATUS.md`.
3. Check each `workspace/out/<Folder>/organize_preview.md` for warnings. The owner gets ONE script,
   `workspace/out/organize_all.sh`. Before handing it over, run `bash sandbox_test.sh workspace/inbox/processed/<scan>`
   (fake copy of their folders: preview changes nothing, no music/video moves, undo restores all).
   Check `cleanup_report.md` line by line against `survey_summary.md` and correct it yourself:
   Hypatia (agent.py) has misstated sizes, safety, and what the scripts do.
4. Commit, open a PR, and merge it into main (the owner allows merging without asking).
5. Tell the owner, in a short list, what's ready and what's needed from them (from STATUS.md).

## Rules
- Never edit `organize_<Folder>.sh` by hand; regenerate it with `sophia.py` / `make_mac_script.py`.
- To change folders or rules, edit `workspace/inbox/preferences.md` and the rules in `sophia.py`.
- Never organize inside ~/Library, Ableton folders, /Applications, /System, or anything in ~/Music
  except the four music homes above.
  Space there is reported in `cleanup_report.md` for the owner to handle by hand.
