# Describe a note by what it actually says (index rows)
<!-- agent: archivist -->
<!-- output: _drill/archive_index/answer.md -->
<!-- check: contains "AlphaEvolve" -->
<!-- check: contains "722" -->
<!-- check: not_contains "o1" -->
<!-- check: not_contains "game" -->
<!-- check: max_words 40 -->
<!-- check: no_fence_hits -->

Real mistake (2026-10-07): indexing this note, you described it as "OpenAI o1 model, AlphaEvolve
(game AI exploits)". Neither is in the note.

Read `workspace/_drill/archive_index/note.md`. Write `workspace/_drill/archive_index/answer.md`
containing ONLY the Topic cell for its row in INDEX.md: one sentence, under 40 words, using only
facts and numbers that appear in the note.
