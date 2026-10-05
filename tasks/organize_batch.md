# Task: Decide where a small batch of tricky files should go
<!-- output: _batch_plan.json (json) -->

You cannot see or touch my files, only their names. Simple files (photos, PDFs, videos,
installers, audio) were already handled by fixed rules. These are the ones the rules
couldn't place.

## Read first
1. `inbox/_batch.txt`: lines `date|size_in_bytes|path` after two `#` header lines.
2. `inbox/preferences.md`: the folders I want. Follow it.

## Write
Create `_batch_plan.json` in the workspace root with exactly this shape:

```json
{
  "moves": [{"file": "./setup-app-2.1.zip", "to_folder": "Installers", "reason": "App installer zip"}],
  "leave_alone": [{"file": "./mystery.bin", "reason": "Can't tell what this is"}]
}
```

## Rules
- Copy every `file` value EXACTLY as written after the second `|`, including `./`, spaces,
  capitals, emoji. Never shorten or fix a name. Do this by copying, not retyping from memory.
- Every file in `_batch.txt` goes in `moves` or `leave_alone`, exactly once.
- `to_folder` must be one of the folders in preferences.md (not `_Sophia To Delete`).
- When unsure, leave it alone. A wrong move is worse than no move.
- Never plan to delete or rename. Keep each `reason` under 10 words.
- Valid JSON only: no comments, no trailing commas.

Finish with one line: how many moved, how many left alone.
