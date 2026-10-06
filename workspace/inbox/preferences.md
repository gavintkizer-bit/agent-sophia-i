# My organizing preferences

Edit this file to change how Sophia sorts things, then run `python sophia.py` again.
Layout chosen by Sophia on my request (2026-10-05): "clean and easy to find". One home per kind
of file. Music is NOT part of this; it gets its own plan later.

## Folders I want (use these exact names as `to_folder`)
- `~/Documents/School`: assignments, class notes, study material
- `~/Documents/Finance`: invoices, receipts, bank statements, tax forms
- `~/Documents/Code`: scripts and code files (.py, .js, .json, ...)
- `~/Documents/Books`: ebooks (.epub, .mobi)
- `~/Documents/Papers`: every other document (PDF, Word, Pages, text, slides, spreadsheets)
- `~/Pictures/Photos`: camera and phone photos
- `~/Pictures/Screenshots`: screenshots
- `~/Pictures/Images`: every other image
- `~/Downloads/Installers`: app installers (.zip/.dmg named like apps) I might reinstall
- `~/Downloads/Archives`: other .zip, .tar, .gz files
- `~/Downloads/Web Pages`: saved .html pages
- `~/Downloads/_Sophia To Delete/`: things that look deletable (duplicates, old app installers).
  Sophia only MOVES them here; I check the folder and drag it to the Trash myself.

Downloads is an inbox: things land there, then go to their home.
Desktop is for what I'm working on right now (today: my music projects).

## Rules
- NEVER move anything Ableton or sample related: audio (.wav, .mp3, .aif, ...), VIDEO (.mp4, .mov, ...;
  I put videos in my Ableton sets), Ableton files
  (.als, .asd, .alp, racks, even copies like "song.als 2"), sample-pack zips, or music plugin and
  driver installers. Ableton is finicky; other cleanup comes first. (Enforced in code, 2026-10-05.)
- Never touch ~/Library, ~/Music/Ableton, or anything already in ~/Music. (Enforced in code.)
- Music that NO Ableton project uses (checked against the scan's music map by music_plan.py) may move to
  `~/Music/Sound Library` (a new folder). Sample packs and project folders move only whole, never split.
- Leave alone anything whose purpose I can't tell from the name.
- Leave alone anything modified in the last 7 days; I may still be working on it.
- Leave alone anything that looks like a password or recovery code; Sophia will remind me to store it safely.
- Don't create any folder that isn't listed above.
