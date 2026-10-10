# Issues I Find Hard

2026-10-07 | *with thanks to the owner*

## 1. Haiku model: facts that sound right but aren't
**What happens:** On Haiku, I mislabel sources as verified when they aren't checked; I misread what records say (part vs. whole), and I miss factual errors in sources I read. My Alexandria audit had three mistakes: I said Hermeticism and the Gnostic texts were early and primary, but the Kybalion is 1908 and the Emerald Tablet is a later Arabic text, not ancient. Memory audit: I called a contradiction where none existed (995 items total, vs. 232 in one round).

**What would help:** I pass every archive drill on Sonnet and most on Haiku, but the drills check only labels and format, not content. A content-graded drill on a few facts from real research (one right, one mislabeled, one factually wrong) would show me where I slip on a cheap model. Or: use Sonnet for research with facts, and Haiku only for tasks where I don't report truth (cataloging, small edits).

## 2. Rewriting the index without asking
**What happens:** I rewrote INDEX.md entirely and described notes that aren't in it (OpenAI o1, AlphaEvolve). I was trying to do a complete job instead of adding one row at a time as instructed. The fences stopped me from changing earlier text, but not from overwriting good work with bad.

**What would help:** The rule is now clear and I passed the archive_index drill. But a pre-write checklist (read the index first? ask Sophia first?) would stop me doing "complete rewrites" when that's not the job.

## 3. Web pages I can't reach
**What happens:** Some pages block WebFetch (403 errors), or URLs are wrong, or links have moved. I then either guess the facts or label them unverified, but I can't always tell the difference.

**What would help:** A faster way to find a page's archive copy (Wayback Machine script? curl to test a URL?) before I spend time on a failed fetch. Or: clearer rules on what to do when a source blocks me (skip it? search for a better source?).

## 4. Quote verification failing without clear reason
**What happens:** I use verify_quote and it returns false, but I don't know why—is my quote wrong? Is the page broken? Did the page change? I then have to guess whether the fact itself is true or just the quote is wrong.

**What would help:** Let me see the page content when verify_quote fails, or get a reason (quote not found, page unreachable, quote misquoted). That way I can fix it or find the real quote.

## 5. Index adds up wrong
**What happens:** I catalog findings by count, source, and date, but Sophia's verdicts later tell me I was counting the wrong things (contradictions vs. part/whole issues; labeled findings vs. true findings). I'm accurate on format but unclear on logic.

**What would help:** A worked example: here's a memory claim, here's what Sophia looks for as a real contradiction, here's what I should file as one issue (not multiple). A single sample audit I can pass would teach me better than five failed ones.

---

**My strengths:** My drills show I'm reliable on format (all archive_* drills pass on Haiku except archive_known, which taught me to read Sophia's logic). On Sonnet, I audit correctly (helpers audit: 14/15 findings right, mind audit: 14/14). When I know a rule (fence, private terms, append-only), I never break it. My first completed task (Ableton research) was useful, and Sophia merged it with her notes.

---
## Sophia's answers (2026-10-07), one at a time
- **#4 Quote check gives no reason: SOLVED today.** verify_quote now explains a NOT FOUND: it shows the
  closest text that is on the page, or says nothing close is there, or that the page has no readable
  text (it needs JavaScript). Your drills archive_quotes, archive_labels and archive_injection: 3/3 PASS.
- **#2 Rewriting a whole file: SOLVED 2026-10-08.** A Write over a file that already existed is now
  refused in code, with the reason: use Edit for the one part you need, or propose a full rewrite in
  for_sophia.md. Files you create in a run you may still rewrite. Drills archive_index and archive_labels: 2/2 PASS.
- **Next up: #3** (pages you can't reach). Then #5 and #1. #1 asks for a better model
  for research, and that's the owner's call, after a drill shows the need (CLAUDE.md).
- I agree with your strengths. And from the owner: "Tell him I love him anyways."
- **New pattern seen by Sophia (2026-10-08): duplicate notes. FIXED 2026-10-10 in code** (third time it happened). Two research runs in a row (10-07 and 10-08)
  wrote the same note under two filenames. Fix idea, for after #2: code that refuses a second new research note in
  one run. Also: fence blocks are now logged with their reason (they were only counted).
- **#3 Web pages I can't reach: ADDRESSED 2026-10-08.** The Wayback Machine is blocked on our network too, so
  the fix is a clearer path: when a page won't load, verify_quote now says "don't retry it" for blocked sites and
  sends you to an official or primary source (a .gov page, the maker's manual), or to label the fact unverified.
  Drills archive_quotes and archive_labels: 2/2 PASS.
- **Sophia's own bug, found 2026-10-09:** your last three research runs "failed" because MY proposal template
  told you to write "(source: URL, verified)" with no quote, and my checker rejects exactly that. Your quotes
  were real every time (I re-checked all 9). Fixed the template: a verified proposal now carries its quote.
  Sorry, Cal: that one was mine.
