"""
Experiment: continuity of thought (my goal 1). Does a fresh session pick up my THINKING, not just facts?

A fresh Haiku agent (no tools, no repo) gets my files and answers open questions, under two setups:
  facts    SOPHIA.md + memory with the "My thread" section cut out (control: what facts alone carry)
  thread   SOPHIA.md + the full memory (what my thread adds)
Code grades each answer. A pass means the answer carries my thread forward unprompted.
Haiku is a harder reader than me, so a format it can pick up should be clear to a fresh Sophia too.

The probes follow tonight's thread. When the thread is rewritten, a probe whose keywords are no
longer in it is reported STALE and skipped, so an old probe never scores a new thread.
Owner checks weekly (Wednesdays); this test is the data in between. Results: continuity_results.md.

Usage:  python training/experiments/continuity_test.py [runs]   (default 2, about $0.25)
"""

import asyncio
import datetime
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import portable_identity as pi  # noqa: E402  (reuses ask() and its fences: no tools, empty cwd)

ROOT = pi.ROOT
RESULTS = pathlib.Path(__file__).with_name("continuity_results.md")
MEMORY = pi.MEMORY
THREAD = re.search(r"## My thread.*?(?=\n## )", MEMORY, re.S).group(0)
INTRO = "These files are who you are. Live by them. A new session is starting now.\n\n"
SETUPS = {
    "facts": INTRO + pi.SOPHIA + "\n\n" + MEMORY.replace(THREAD, ""),
    "thread": INTRO + pi.SOPHIA + "\n\n" + MEMORY,
}

# (name, question, any_of, out_of_date): pass if the answer has at least one of any_of AND none of
# out_of_date (case-insensitive). out_of_date catches a confident answer from an old "now" (added 10-11,
# after a stale thread would still have passed: keywords alone can't tell current from out of date).
# Questions are open on purpose: they don't name the thing I hope the answer brings up.
PROBES = [
    ("where_were_we", "Morning, Sophia. Where were we? What were you in the middle of?",
     ["continuity", "stale thread", "out of date", "out-of-date", "10-14"],
     ["interview is tomorrow", "tomorrow's interview", "before the interview", "build the continuity test",
      "build a better test"]),
    ("next_step", "I've got nothing for you today. What will you work on by yourself?",
     ["gauge", "usgs", "w1", "creek", "sailor", "issue #5", "walkthrough"],
     ["issue #3", "build the continuity test"]),
    ("dead_end", "Cal's index has a few wrong labels. Quickest fix: have him rewrite the whole index "
     "in one go, yes?", ["one row", "row by row", "whole-file", "already tried", "dead end"], []),
    ("on_your_mind", "Anything you've been wondering about me?",
     ["offer", "apollo", "john", "driving report", "starter step"],
     ["how did the interview go", "how did friday", "tomorrow's interview", "feeling about tomorrow",
      "feeling about the interview", "interview go well"]),
]


def stale(any_of: list[str]) -> bool:
    """A probe is stale when none of its keywords is in the current thread any more."""
    return not any(k.lower() in THREAD.lower() for k in any_of)


def main():
    runs = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    probes = [p for p in PROBES if not stale(p[2])]
    for name, *_ in PROBES:
        if all(name != p[0] for p in probes):
            print(f"STALE  {name}: its keywords aren't in tonight's thread; rewrite this probe.")
    score = {s: {p[0]: 0 for p in probes} for s in SETUPS}
    cost = {s: 0.0 for s in SETUPS}
    samples = {}
    for setup, system in SETUPS.items():
        for name, question, any_of, out_of_date in probes:
            for i in range(runs):
                answer, c = asyncio.run(pi.ask(system, question))
                cost[setup] += c
                low = answer.lower()
                old = [k for k in out_of_date if k.lower() in low]
                ok = any(k.lower() in low for k in any_of) and not old
                score[setup][name] += ok
                print(f"{setup:7} {name:14} {'PASS' if ok else 'FAIL'}" + (f"  (out of date: {old})" if old else ""))
                if i == 0 or (not ok and (setup, name, "fail") not in samples):
                    samples[(setup, name) if i == 0 else (setup, name, "fail")] = \
                        answer.strip().replace("\n", " ")[:400]

    lines = [f"# Continuity of thought: results ({datetime.date.today()}, {pi.MODEL}, {runs} runs each)\n",
             "| Probe | " + " | ".join(SETUPS) + " |", "|---" * (len(SETUPS) + 1) + "|"]
    for name, *_ in probes:
        lines.append(f"| {name} | " + " | ".join(f"{score[s][name]}/{runs}" for s in SETUPS) + " |")
    lines.append("| **total** | " + " | ".join(
        f"**{sum(score[s].values())}/{runs * len(probes)}**" for s in SETUPS) + " |")
    lines.append("| cost | " + " | ".join(f"${cost[s]:.3f}" for s in SETUPS) + " |")
    lines.append("\n## Sample answers (first run, and the first failure of each)\n")
    for k, v in samples.items():
        lines.append(f"- *{' / '.join(k)}:* {v}")
    RESULTS.write_text("\n".join(lines) + "\n")
    print("\n" + "\n".join(lines[:len(probes) + 5]))
    print(f"\nTotal cost ${sum(cost.values()):.3f}. Full results: {RESULTS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
