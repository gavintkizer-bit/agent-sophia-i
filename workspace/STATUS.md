# Sophia status

_Updated 2026-10-05_

## Ready for you to run on your Mac

Download, then in Terminal run the preview first, then `--go`:

- **Desktop**: [organize_Desktop.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Desktop/organize_Desktop.sh) (preview: `workspace/out/Desktop/organize_preview.md`)
- **Documents**: [organize_Documents.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Documents/organize_Documents.sh) (preview: `workspace/out/Documents/organize_preview.md`)
- **Downloads**: [organize_Downloads.sh](https://github.com/gavintkizer-bit/agent-sophia-i/raw/main/workspace/out/Downloads/organize_Downloads.sh) (preview: `workspace/out/Downloads/organize_preview.md`)

```
bash ~/Downloads/organize_Downloads.sh        # preview, changes nothing
bash ~/Downloads/organize_Downloads.sh --go   # moves files (an undo script is saved)
```

### Latest run: Downloads

- 1221 files: 512 will move, 709 stay put (audio/Ableton, recent, or unclear).
- Folders: Archives 21, Documents 149, Documents/Finance 3, Images 110, Installers 11, Video 66, Web Pages 103, _Sophia To Delete/Duplicates 32, _Sophia To Delete/Installers 17

- **1.45 GB** goes to `_Sophia To Delete/` for you to check, then drag to the Trash.

## Where your disk space goes

See `workspace/cleanup_report.md`.

## What Sophia needs from you

- New scan when you've run a script or want fresh numbers: `bash ~/Downloads/sophia_scan.sh`, then upload `~/Desktop/sophia_upload/*` to `workspace/inbox/` on GitHub.
