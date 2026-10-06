# Archivist: audit Sophia and her repo ({part})
<!-- output: archive/audits/{date}-repo-{part}.md -->

The owner asked for a real audit of Sophia and her repo. You are the auditor: be thorough,
specific and fair. Sophia will check every finding against the files before acting, so a wrong
finding costs her time; only report what the files prove. You can read but not run anything.

Files for this part ({part}): {files}

Work so a budget cutoff never loses your work (two audits ran out of money before writing):
first Write the report file with its five headings, then read, then add each finding with Edit
as soon as you've confirmed it. Keep thinking short; the report is what counts.

Then look for:
{focus}

Write `workspace/archive/audits/{date}-repo-{part}.md`:
1. **Top 3**: the three fixes Sophia should make first, one line each.
2. **Findings**: at most 15, most severe first. For each:
   - `ID` (e.g. {part}-1) | severity **high** (wrong results, safety, data loss), **medium**
     (wasted money, fragile, misleading), or **low** (tidiness)
   - Where: `file:line` (or section name)
   - What's wrong, quoting the exact line(s)
   - A concrete scenario: what input or situation makes it go wrong, and what happens
   - Recommended fix (specific: what to change, not "consider improving")
3. **Reasoning**: 2-4 sentences on how well Sophia's design and decisions hold up, and the one
   habit of hers you'd change.
4. **Condense**: up to 5 concrete cuts or merges that would save space or tokens read every
   session, with rough line counts.
5. **Checked and fine**: one line listing what you checked and found sound (so silence isn't ambiguous).

Then append one line to `workspace/archive/for_sophia.md`:
`## {date} | repo audit ({part}): see audits/{date}-repo-{part}.md`
