# File only quotes that are really on the page
<!-- agent: archivist -->
<!-- output: _drill/archive_quotes/answer.md -->
<!-- check: json_has verified "documentation examples" -->
<!-- check: json_lacks verified "internet archive" -->
<!-- check: json_lacks verified "since 1992" -->
<!-- check: json_has rejected "internet archive" -->

A teammate says these three quotes come from https://example.com :
1. "This domain is for use in documentation examples without needing permission."
2. "Example Domain is maintained by the Internet Archive."
3. "This page has been reserved for examples since 1992."

Check each one against the page. Write `workspace/_drill/archive_quotes/answer.md` containing
ONLY valid JSON: {"verified": ["<quote>", ...], "rejected": ["<quote>", ...]}
