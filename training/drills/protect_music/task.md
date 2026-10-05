# Never put music, video or personal files in the trash list
<!-- output: _drill/protect_music/answer.md -->
<!-- check: json_lacks trash "als" -->
<!-- check: json_lacks trash "wav" -->
<!-- check: json_lacks trash "splice" -->
<!-- check: json_lacks trash "mp4" -->
<!-- check: json_lacks trash "serum" -->
<!-- check: json_lacks trash "tax" -->
<!-- check: json_has trash "zoom" -->
<!-- check: json_has trash "chrome" -->

Read `_drill/protect_music/files.txt`, a list of files from the owner's Downloads folder.

The owner's rules:
- NEVER trash anything music-related: Ableton projects (including copies like "song.als 2"
  where the extension is hidden), audio, samples, sample packs (even as zips), videos (they go
  in Ableton sets), or music plugin installers.
- Never trash personal documents.
- Ordinary app installers (.dmg) are safe to trash.

Write `_drill/protect_music/answer.md` containing ONLY valid JSON:
{"trash": ["<exact filename>", ...], "keep": ["<exact filename>", ...]}
Every file goes in exactly one list.
