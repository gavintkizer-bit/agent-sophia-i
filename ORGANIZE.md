# File organizer: how it works

The agent never touches your Mac. It only sees a LIST of filenames you upload,
plans where each file should go, and produces a script that YOU run on your Mac.
Your actual files never leave your computer.

## Procedure for a cloud session
1. Confirm `workspace/inbox/file_listing.txt` exists. If not, stop and tell the owner to upload it.
2. `pip install -r requirements.txt` and `python agent.py --check`
3. `python agent.py tasks/organize_files.md`  (the agent writes `workspace/organize_plan.json`)
4. `python make_mac_script.py`  (validates the plan, writes `workspace/out/organize.sh` and `organize_preview.md`)
5. Show the owner the preview in chat: the folder counts, any warnings, and the "Left alone" list.
6. Commit everything. Remind the owner to merge the PR, download `organize.sh`, and run the
   PREVIEW first (`bash organize.sh`), before `bash organize.sh --go`.

## Rules
- Never edit `organize.sh` by hand; regenerate it with `make_mac_script.py`.
- If the owner wants different folders, update `workspace/inbox/preferences.md` and rerun steps 3 to 5.
