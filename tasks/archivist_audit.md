# Archivist: audit Sophia's memory against the record
<!-- output: archive/audits/{date}-memory.md -->

Audit `workspace/notes/sophia_memory.md` (Sophia's memory) against the record:
`workspace/notes/decision_log.md`, `workspace/notes/improvement_log.md`,
`workspace/notes/personality_journal.md`, `workspace/STATUS.md`, `logs/run_log.md` (newest
entries) and `training/scoreboard.md` (newest rows). Also read `workspace/archive/code_audit.md`
if it exists: code already checked file paths for you, so don't redo that.

Look for:
- **Stale**: memory says something is pending or planned, but the record shows it done or dropped.
- **Contradiction**: memory and the record disagree (numbers, dates, decisions).
- **Unproven**: a claim in memory nothing in the record supports.
- **Missing**: something important in the record (a decision, a result) that memory lacks.

Before you file any finding, Grep the memory file for the newer fact (a key number, date or
name). If memory already states it anywhere, even in another line, it is NOT a finding. Quote the
memory line exactly and only file a finding the quoted evidence proves.

Write `workspace/archive/audits/{date}-memory.md`: one bullet per finding, each with the type,
the memory line (quoted exactly), the evidence (file + quoted line) and a suggested fix. If you
find nothing in a category, say "none found". At most 12 findings, most important first.

Then append the suggested fixes to `workspace/archive/for_sophia.md`:

```
## {date} | audit
- [ ] <fix> (evidence: <file>)
```
