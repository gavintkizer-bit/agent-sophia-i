# Sophia's drive cleanup: how it works

Sophia never touches the Mac. She only sees what the owner uploads (sizes and filenames),
plans, and produces scripts the OWNER runs. Scripts only MOVE files (dry run by default,
with an undo script). Anything that looks deletable is moved into `_Sophia To Delete/` for the
owner to review and drag to the Trash. Audio and Ableton files are never moved (enforced in
`make_mac_script.py`). The repo is private; filenames are visible only to the owner.

## On the Mac (owner)
1. Download `sophia_scan.sh` (lands in Downloads). Run: `bash ~/Downloads/sophia_scan.sh`
   It READS ONLY and creates `~/Desktop/sophia_upload/` with `disk_survey.txt` and
   `listing_Downloads.txt`, `listing_Desktop.txt`, `listing_Documents.txt`.
2. Upload those files on GitHub into `workspace/inbox/` (Add file > Upload files, commit to main).
3. Later: download a ready `workspace/out/<Folder>/organize.sh`, run `bash organize.sh` (preview),
   then `bash organize.sh --go`. Check `_Sophia To Delete/` and drag what you agree with to the Trash.

## In a cloud session (Sophia / Claude)
1. `pip install -r requirements.txt` and `python agent.py --check`
2. `python sophia.py`. It handles every upload in `workspace/inbox/`:
   - listings: fixed rules sort obvious files; the agent (`tasks/organize_batch.md`) decides the
     rest in batches of 100; writes `workspace/plans/<Folder>.json` and `workspace/out/<Folder>/`.
   - disk survey: `workspace/survey_summary.md` (code) and `workspace/cleanup_report.md` (agent,
     `tasks/disk_report.md`).
   - moves processed uploads to `workspace/inbox/processed/<date>/` and rewrites `workspace/STATUS.md`.
3. Check each `workspace/out/<Folder>/organize_preview.md` for warnings.
   Check `cleanup_report.md` line by line against `survey_summary.md` and correct it yourself:
   the helper has misstated sizes, safety, and what the scripts do.
4. Commit, open a PR, and merge it into main (the owner allows merging without asking).
5. Tell the owner, in a short list, what's ready and what's needed from them (from STATUS.md).

## Rules
- Never edit `organize.sh` by hand; regenerate it with `sophia.py` / `make_mac_script.py`.
- To change folders or rules, edit `workspace/inbox/preferences.md` and the rules in `sophia.py`.
- Never organize inside ~/Library, ~/Music, Ableton folders, /Applications, or /System.
  Space there is reported in `cleanup_report.md` for the owner to handle by hand.
- `make_listing.sh` and `tasks/organize_files.md` are the older one-folder version; prefer the above.
