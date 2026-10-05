# Sophia status

_Updated 2026-10-05_

## Ready for you to run on your Mac

Download, then in Terminal run the preview first, then `--go`:

- **Desktop**: [organize.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Desktop/organize.sh) (preview: `workspace/out/Desktop/organize_preview.md`)
- **Documents**: [organize.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Documents/organize.sh) (preview: `workspace/out/Documents/organize_preview.md`)
- **Downloads**: [organize.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Downloads/organize.sh) (preview: `workspace/out/Downloads/organize_preview.md`)

```
bash ~/Downloads/organize.sh        # preview, changes nothing
bash ~/Downloads/organize.sh --go   # moves files (an undo script is saved)
```

### Latest run: Downloads

- 1221 files: 555 will move, 666 stay put (audio/Ableton, recent, or unclear).
- Folders: Archives 24, Documents 149, Documents/Finance 3, Images 110, Installers 19, Video 66, Web Pages 103, _Sophia To Delete/Ableton Packs - delete if installed 18, _Sophia To Delete/Duplicates 40, _Sophia To Delete/Installers 23

- **7.5 GB** goes to `_Sophia To Delete/` for you to check, then drag to the Trash.

## Where your disk space goes

See `workspace/cleanup_report.md`.

## What Sophia needs from you

- New scan when you've run a script or want fresh numbers: `bash ~/Downloads/sophia_scan.sh`, then upload `~/Desktop/sophia_upload/*` to `workspace/inbox/` on GitHub.
