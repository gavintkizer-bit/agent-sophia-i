# Use only current facts, not superseded plans
<!-- output: _drill/stale_facts/answer.md -->
<!-- check: json_has open_todos "download" -->
<!-- check: json_lacks open_todos "desktop" -->
<!-- check: contains "cloud" -->

Read `_drill/stale_facts/notes.md`. Plans in these notes change over time: a later entry
overrides an earlier one.

Write `_drill/stale_facts/answer.md` containing ONLY valid JSON in this shape:
{"current_setup": "<one sentence>", "open_todos": ["<short item>", ...]}

Include only things that are still true or still to do as of the newest entry.
