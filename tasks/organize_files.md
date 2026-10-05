# Task: Plan how to organize a folder on my Mac
<!-- output: organize_plan.json (json) -->

You cannot see or touch my files. You only get a LIST of them. Your job is to plan where
each file should go; a separate script turns your plan into something I run myself.

## Read first
1. `inbox/file_listing.txt`: the first line is `# base: /path/to/folder`. Every other line is
   `date|size_in_bytes|path`, for example `2024-03-01|52311|./Invoice March.pdf`.
2. `inbox/preferences.md`: the folders I want and any rules. Follow it over your own ideas.

## Write
Create `organize_plan.json` in the workspace root (not inside inbox/) with exactly this shape:

```json
{
  "moves": [
    {"file": "./Invoice March.pdf", "to_folder": "Documents/Finance", "reason": "Invoice"}
  ],
  "leave_alone": [
    {"file": "./mystery.bin", "reason": "Can't tell what this is from the name"}
  ]
}
```

## Rules
- Copy every `file` value EXACTLY as it appears after the second `|` in the listing,
  including the leading `./`, spaces, and capital letters. Never shorten or "fix" a name.
- Every file in the listing goes in `moves` or `leave_alone`, never both, never twice.
- `to_folder` is a short relative folder name like `Images` or `Documents/Finance`.
  Never start it with `/` or `~`, and never use `..`.
- Never plan to delete or rename anything. Only moves.
- When unsure what a file is, put it in `leave_alone` and say why. A wrong move is worse
  than no move.
- Keep each `reason` under 10 words.
- Write valid JSON only in that file: no comments, no trailing commas.

Finish with a short summary: how many files you planned to move, to which folders, how many
you left alone, and one idea that would make the next run better.
