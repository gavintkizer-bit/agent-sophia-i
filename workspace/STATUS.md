# Sophia status

_Updated 2026-10-05_

## Ready for you to run on your Mac

Download, then in Terminal run the preview first, then `--go`:

- **Downloads**: [organize.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Downloads/organize.sh) (preview: `workspace/out/Downloads/organize_preview.md`)

```
bash ~/Downloads/organize.sh        # preview, changes nothing
bash ~/Downloads/organize.sh --go   # moves files (an undo script is saved)
```

### Latest run: Downloads

- 1219 files: 547 will move, 672 stay put (audio/Ableton, recent, or unclear).
- Folders: Archives 17, Documents 132, Documents/Finance 3, Images 110, Installers 26, Video 65, Web Pages 113, _Sophia To Delete/Ableton Packs - delete if installed 18, _Sophia To Delete/Duplicates 40, _Sophia To Delete/Installers 23

- **7.5 GB** goes to `_Sophia To Delete/` for you to check, then drag to the Trash.

## What Sophia needs from you

- New scan when you've run a script or want fresh numbers: `bash ~/Downloads/sophia_scan.sh`, then upload `~/Desktop/sophia_upload/*` to `workspace/inbox/` on GitHub.
