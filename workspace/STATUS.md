# Sophia status

_Updated 2026-10-06_

## Ready for you to run on your Mac

One script for everything: [organize_all.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/organize_all.sh). Control-click > Save Link As..., save in Downloads.
Previews for each folder: `workspace/out/<folder>/organize_preview.md`.

```
bash ~/Downloads/organize_all.sh        # preview, changes nothing
bash ~/Downloads/organize_all.sh --go   # moves files; undo files go to Documents/Sophia/Undo
```

If your Mac saved it as `organize_all (1).sh`, delete the old one and rename
the new one, so you never run an outdated script.

### Latest run: Documents

- 2 files: 1 will move, 1 stay put (audio/Ableton, recent, or unclear).
- Folders: ~/Documents/Papers 1

### Latest run: Downloads

- 779 files: 53 will move, 726 stay put (audio/Ableton, recent, or unclear).
- Folders: ~/Documents/Code 9, ~/Documents/Minecraft Worlds 1, ~/Documents/Minecraft Worlds/Loose world files 3, ~/Documents/Papers 6, ~/Documents/Sophia/Undo 1, ~/Downloads/Archives 2, ~/Downloads/Web Pages 9, ~/Downloads/_Sophia To Delete/Sophia leftovers 2, ~/Pictures/Images 1, ~/Pictures/Photos 19

- **0.0 GB** goes to `~/Downloads/_Sophia To Delete/` for you to check, then drag to the Trash.

## Where your disk space goes

See `workspace/cleanup_report.md`.

## What Sophia needs from you

- New scan when you've run a script or want fresh numbers: `bash ~/Downloads/sophia_scan.sh`, then upload `~/Desktop/sophia_upload/*` to `workspace/inbox/` on GitHub.
