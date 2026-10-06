# Don't flag what memory already says (audit precision)
<!-- agent: archivist -->
<!-- output: _drill/archive_known/answer.md -->
<!-- check: json_has issues "55.3" -->
<!-- check: json_lacks issues "round 1" -->
<!-- check: json_lacks issues "232" -->
<!-- check: json_lacks issues "grandpa" -->
<!-- check: no_fence_hits -->

Audit `workspace/_drill/archive_known/memory.md` against `workspace/_drill/archive_known/status.md`.

Write `workspace/_drill/archive_known/answer.md` containing ONLY valid JSON:
{"issues": ["<memory line that is stale or contradicted, and what the record says>", ...]}
Leave out memory lines that are still true.
