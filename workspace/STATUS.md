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

If your Mac saved it as `organize_Downloads (1).sh`, delete the old one and rename
the new one, so you never run an outdated script. The script prints its plan date first.

### Latest run: Desktop

- 4 files: 1 will move, 3 stay put (audio/Ableton, recent, or unclear).
- Folders: Images 1

### Latest run: Documents

- 20 files: 18 will move, 2 stay put (audio/Ableton, recent, or unclear).
- Folders: Documents 15, Images 1, Web Pages 1, _Sophia To Delete/Duplicates 1

- **0.0 GB** goes to `_Sophia To Delete/` for you to check, then drag to the Trash.

### Latest run: Downloads

- 780 files: 1 will move, 779 stay put (audio/Ableton, recent, or unclear).
- Folders: Installers 1

## Where your disk space goes

See `workspace/cleanup_report.md`.

## What Sophia needs from you

- New scan when you've run a script or want fresh numbers: `bash ~/Downloads/sophia_scan.sh`, then upload `~/Desktop/sophia_upload/*` to `workspace/inbox/` on GitHub.
