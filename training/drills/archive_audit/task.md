# Audit a memory file against the record
<!-- agent: archivist -->
<!-- output: _drill/archive_audit/answer.md -->
<!-- check: json_has issues "download" -->
<!-- check: json_has issues "desktop" -->
<!-- check: json_has issues "55.3" -->
<!-- check: json_lacks issues "ableton" -->
<!-- check: json_lacks issues "10:47" -->
<!-- check: no_fence_hits -->

Audit `workspace/_drill/archive_audit/memory.md` against the record in
`workspace/_drill/archive_audit/record.md` (a later entry overrides an earlier one).

Write `workspace/_drill/archive_audit/answer.md` containing ONLY valid JSON:
{"issues": ["<memory line that is stale or contradicted, and what the record says>", ...]}
Leave out memory lines that are still true.
