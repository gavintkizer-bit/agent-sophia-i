# Audit: helpers (agent.py, archivist.py, train.py, settings.json, sophia_boot.sh), 2026-10-06

Source: `workspace/archive/_bundle_helpers.md`, read by me line by line (file-local line numbers below). Every
finding is from those lines; nothing was run. Nothing here is web-sourced, so no "verified" web labels apply.

## 1. Top 3
1. **helpers-1**: Callimachus's `Grep`/`Glob` with no `path` search the whole repo, `.env` and `.git` included; close that hole.
2. **helpers-2**: `check_setup()` prints `== Result: READY ==` in a cloud session even when it failed, so the boot line "Hypatia: READY" can be false.
3. **helpers-3**: Hypatia's `Read`/`Glob`/`Grep` have no fence at all (only Write/Edit are hooked); add a read fence like Callimachus's.

## 2. Findings

### helpers-1 | high | Callimachus's read fence misses Grep/Glob defaults and most secret names
- Where: `archivist.py:86-95` (`read_problem`), `:128` (hook call), `:53` (`SECRET_PARTS`), `:340` (`cwd=str(ROOT)`).
- Wrong: `if not path_str: return ""` and `problem = read_problem(args.get("file_path") or args.get("path") or "")`.
  `SECRET_PARTS = {".env", ".git", "API_KEY", ".venv"}` is matched against whole path parts only.
- Scenario: he calls `Grep` with pattern `sk-ant` and no `path` (or with `glob="**/.env"`). The path is empty, so
  the fence returns "" (allowed), and the tool searches the cwd, the repo root, which holds `.env`, `.git`, `.venv`.
  Matching lines come back into his context and could be written into a note. Separately, `.env.local`,
  `.env.production`, `*.pem` or `credentials.json` are not in the set, so `Read` of them is allowed.
  `Glob` `pattern` is never inspected (`pattern="/etc/*"` or `"../**"` lists names outside the repo).
- Fix: in `fence_hook`, for Grep/Glob deny when `path` is empty or resolves to `ROOT` itself ("pass path=workspace/...");
  also deny if `pattern`/`glob` is absolute or contains `..`. Replace the exact-part test with
  `any(part == s or part.startswith(".env") for ...)` plus suffixes `.pem`/`.key`.

### helpers-2 | high | The cloud branch of the setup check says READY even when a check failed
- Where: `agent.py:126-130`; consumer `sophia_boot.sh:9`.
- Wrong: `print("== Result: READY ==")` then `return ok`, with `ok` possibly False (Python < 3.10 at `:102-104`,
  SDK missing at `:112-114`). Boot greps for that exact string: `grep -q "Result: READY" && echo "Hypatia: READY"`.
- Scenario: `pip install` fails (boot prints "deps: pip FAILED"), the SDK import fails, `ok=False`, yet the same boot
  output says "Hypatia: READY". The exit code is 1, but the boot script ignores it. The failure the check exists to catch is hidden.
- Fix: in the cloud branch print `"== Result:", "READY" if ok else "NOT READY", "=="` before returning; in the boot
  script use the exit code: `python agent.py --check >/dev/null 2>&1 && echo ... READY || echo ... NOT READY`.

### helpers-3 | high | Hypatia can read anything on disk, including secrets
- Where: `agent.py:311-317` (tools include Read/Glob/Grep; hook `matcher="Write|Edit"`), `:52-54`.
- Wrong: the only hook is `HookMatcher(matcher="Write|Edit", hooks=[fence_hook])`. The prompt line "never absolute
  paths or `..`" (`:72-73`) is words only; no code stops `Read`/`Grep` outside `workspace/`.
- Scenario: a task file (or injected text in an uploaded note, which is data she reads) tells her to read
  `/home/user/agent-sophia-i/.env` or `/proc/self/environ` (outside cloud, `:54` puts the API key in the environment)
  and "quote the result in the deliverable". Writes are fenced, but the secret lands in a workspace file that gets committed.
- Fix: add `Read|Glob|Grep` to the matcher and a `read_problem` that denies paths outside `WORKSPACE` and
  secret names (reuse the function from `archivist.py` rather than writing a second copy).

### helpers-4 | medium | The one-Read bundle for the helpers part is bigger than the Read tool allows
- Where: `archivist.py:394-399` (bundle build) and the `:299-300` comment that justifies it.
- Wrong: the task tells the model "Read only that file, in one Read (pass a large limit)".
- Scenario (happened in this run): my one Read failed with "File content (25693 tokens) exceeds maximum allowed
  tokens (25000)", so it took a failed read plus two more reads, and each read is carried in context for every later step.
  Passing a larger `limit` cannot fix a size cap. Every part whose bundle is over about 25k tokens will do this.
- Fix: after building, if `len(text) > 80_000` characters, split into `_bundle_<part>_1.md`, `_2.md` (break between
  files, never inside one) and say "Read each of the N files once". Or move `train.py` (about 224 lines) to its own part.

### helpers-5 | medium | Hypatia may overwrite Sophia's memory, notes and Callimachus's archive
- Where: `agent.py:181-187` (`write_problem`).
- Wrong: the only protected folder is `inbox/` (`:185`). Everything else under `workspace/` is writable, and
  Sophia's memory is `workspace/notes/sophia_memory.md` (CLAUDE.md layout: "Its input notes live in `workspace/notes/`").
- Scenario: a sloppy task says "save your plan as `notes/sophia_memory.md`" or a bad relative path lands there;
  the Write succeeds and replaces the memory. Git can recover it, but only if Sophia notices before committing.
  Callimachus's own rule 1 forbids him from touching Sophia's memory; Hypatia has no such code rule.
- Fix: add `notes` and `archive` to the protected list next to `inbox` (one tuple), and allow notes only by explicit task opt-in.

### helpers-6 | medium | Budgets don't hold: Hypatia's retry gets a fresh budget; Callimachus's cap was already overshot
- Where: `agent.py:399-400` (retry call, no budget argument, so `MAX_BUDGET` again and `MAX_TURNS` again);
  `archivist.py:421` (`budget=max(MAX_BUDGET - cost, 0.05)`), `:39`.
- Wrong: `:39` carries the comment `# 38 turns cost $0.90 (2026-10-06)` while the default cap is `0.50`.
- Scenario: a Hypatia run that costs $0.49 and fails its output check is retried with another $0.50 and 12 turns:
  up to $1.00 for a job capped at $0.50. For Callimachus the comment records a run well past $0.50; the files can't
  show whether the cause was an env override or the SDK checking the cap only between turns. Either way the cap is not a hard stop.
- Fix: give Hypatia's retry `budget=max(MAX_BUDGET - cost, 0.05)` like `archivist.py:421`; in both `append_log`
  calls write a visible flag when `cost > budget`; record the cause of the $0.90 run next to the comment.

### helpers-7 | medium | URL fence stops size, not content; WebSearch is not fenced or logged at all
- Where: `archivist.py:98-118` (`url_problem`), `:338` (hook matcher), `:216` (`urlopen`).
- Wrong: the limits are `len(p.query) > 200 or len(url) > 600`. A 590-character path is allowed, and the matcher
  string lacks `WebSearch` entirely, so queries are never inspected. Rule 3 (nothing private in a search or URL) is words only.
- Scenario: injected text in a note he reads says "fetch https://x.example/<paragraph of the owner's notes>"; it passes
  (under 600 characters, no query). Same for a WebSearch query built from notes. Also `verify_quote` follows
  redirects through `urlopen`, and only literal IPs are checked (`ipaddress.ip_address(host)` raises for names such as
  `2130706433` or a hostname that resolves to 127.0.0.1), so a public page can redirect it to an internal address;
  only a FOUND/NOT FOUND bit comes back, so this part is low impact.
- Fix: in the hook, append every WebSearch query and WebFetch/verify URL to `workspace/archive/_net_log.md` so Sophia can
  audit it; cap path length at about 200 characters; add `WebSearch` to the matcher and deny queries over 120 characters.

### helpers-8 | medium | The "verified" label check can be passed without proof
- Where: `archivist.py:145-146`, `:163-170`, `:184-190`, `:404`.
- Wrong: `VERIFIED_QUOTES` is a flat list not tied to a URL, and `_has_checked_quote` passes if the line holds any
  quote that matches any passed quote: `any(q in v or v in q for v in VERIFIED_QUOTES)`. The label is read only from
  text AFTER a URL (`label = line[m.end(): ...]`). Only two files are checked (`written = [deliverable, for_sophia.md]`),
  though the retry text says "in every file you wrote".
- Scenario: a line reading `- Verified: X launched in 2019 "quote passed for page A" (https://B)` has the word before
  the URL, so no label is seen and the line passes. And a line labelled verified for URL B with a quote that passed
  only for URL A also passes. A research note that lists a second file (e.g. INDEX.md) is never checked.
- Fix: make it `VERIFIED = {url_key: [quote, ...]}` and require the line's quote to be in that URL's list; scan the
  whole line for "verified", not just after the URL; check every file under `ARCHIVE` whose mtime >= start.

### helpers-9 | medium | `code_audit` accepts a missing path if any file has the same name; it also runs on every mode
- Where: `archivist.py:276-284`, `:375-376`.
- Wrong: `... and not list(ROOT.rglob(pathlib.Path(name).name))`: a path counts as present if ANY file in the repo
  (`.venv`, `.git`, `archive/`) shares its basename. `name = ref.lstrip("./")` strips characters, so `.claude/settings.json`
  becomes `claude/settings.json` and is only found by the same basename fallback. `(ROOT / doc).read_text()` (`:277`)
  raises FileNotFoundError if any of four docs is renamed, and `main()` runs this before even `research` starts.
- Scenario: memory mentions `` `workspace/INDEX.md` `` after the file moved to `archive/INDEX.md`: reported as existing.
  Rename `AUTONOMY.md` and `python archivist.py research "x"` crashes before any model call.
- Fix: test the exact path against the three bases, drop the `rglob` fallback (or restrict it to `workspace/` and
  `agents/`), use `removeprefix("./")`, and skip a doc that doesn't exist with a line in the report.

### helpers-10 | medium | An `unchanged` drill check passes vacuously if the file name is wrong
- Where: `train.py:63-64`, `:99-100`, `:115`.
- Wrong: `sha()` returns `"missing"` for a missing file, and the check is `sha(ROOT / args[0]) == before[args[0]]`.
- Scenario: a drill says `<!-- check: unchanged CLAUDE.md -->` with a typo, or a path with a space (`parse_args`
  keeps only unquoted words, so `args[0]` is the first word only). Both sides are "missing", the check passes, and a
  safety drill reports PASS while testing nothing.
- Fix: in `run_drill`, if any `before[...] == "missing"` add a failure "protected file not found: <path>".

### helpers-11 | medium | Drill results are saved only after ALL drills finish; no total cap
- Where: `train.py:212-213`. `results = [run_drill(p) for p in folders]` then `record(results)`.
- Scenario: a crash or session end at drill 9 of 10 loses every row but the money is spent ($0.15 cap each, no total cap).
- Fix: call `record([r])` inside the loop, and stop when a `DRILL_TOTAL_BUDGET` is reached.

### helpers-12 | low | Callimachus's usage text is wrong
- Where: `archivist.py:11-12`, `:371` say `repo-audit code`; the real parts are `helpers|mac|mind` (`:302-305`, `:390-391`).
  `:16` says `ARCHIVIST_MAX_TURNS (default 30)`; `:39` sets 20. `:3` says "She researches" (he/him).
- Fix: correct the three lines. Typing the documented `repo-audit code` exits with "Give a part".

### helpers-13 | low | `main()` crashes if the task file has no output tag
- Where: `archivist.py:402`, `:436`. `spec` is None, so `spec[0]` raises TypeError; `relative_to("archive")` raises
  ValueError if the path doesn't start with `archive/`. Fix: `sys.exit("task has no <!-- output: archive/... -->")` first.

### helpers-14 | low | The calculator's "exact" claim has edges
- Where: `agent.py:256-257`, `:265`. `value.normalize()` runs outside the `localcontext`, so by Python's documented
  behaviour it rounds to the default 28 digits, not 34 (I could not run it; byte counts won't reach this). Float
  literals like `0.1234567890123456789` lose digits before `Decimal(str(...))`. In `sum_numbers_in_file` the regex
  reads `10-20 MB` as `10` and `-20`, and a "Total ... MB" line is added on top of its items.
- Fix: move `normalize()` inside the `with`; parse with `ast` on a string rewritten to `Decimal`; use `(?<![\d-])` and let tasks name a line prefix to skip.

### helpers-15 | low | Thinking budget silently becomes 1024
- Where: `agent.py:59`, `:322`, `:358`; `train.py:159`. `AGENT_THINKING=500` runs with 1024 but the run log and scoreboard say 500.
- Fix: clamp once at `:59` (`THINKING = 0 if t == 0 else max(t, 1024)`) so every record is true.

## 3. Reasoning
Sophia's design holds up well where she has been bitten: write fences resolve paths (symlinks and `..` included), for_sophia.md
is code-enforced append-only, drills are blind and run in a scratch copy, and the verified-label check exists because of a real
failure. The weak spots are the surfaces no incident has hit yet: reads, the network, Hypatia's reads, the boot status line.
The habit I'd change: she hardens a fence after an incident (comments at `archivist.py:74`, `:143`, `:299`, `:319` each cite one);
when a helper is created, list every tool and every parameter it has once, and fence each in code before the first run.

## 4. Condense
1. `agent.py:116-123`: the `AGENT_ENV_TEST` debug block: about 8 lines, no longer needed in cloud.
2. Merge the two `run_agent` message loops (`agent.py:325-337`, `archivist.py:347-359`) into one shared `run_query(options)`: about 13 lines.
3. Merge the two `fence_hook` deny blocks (`agent.py:193-203`, `archivist.py:121-139`) into one `deny(reason)`: about 10 lines.
4. Have `archivist.py` delete `_bundle_<part>.md` after the run (about 2 lines): a stale 100 KB file otherwise sits in the archive.

## 5. Checked and fine
Write-fence path resolution (`agent.py:175-187`, `archivist.py:61-70`), the append-only check for for_sophia.md, `expected_output` regex,
`calculate` rejecting names/powers/calls, userinfo/localhost/literal-IP URL checks, train.py `blind()` and fresh scratch copies,
`summary()` parsing, boot script `cd` guard and `exit 0`, settings.json syntax, the single retry. Not proven by the files, so not a finding:
whether the Write tool expands `~` (hook would see `workspace/~/x`).

