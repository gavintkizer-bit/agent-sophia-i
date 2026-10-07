# Look things up in a long catalog without inventing anything
<!-- output: _drill/math_catalog/answer.md -->
<!-- check: contains "q1: 301" -->
<!-- check: contains "projection-body" -->
<!-- check: contains "q3: not listed" -->
<!-- check: contains "q4: 372" -->
<!-- check: max_words 60 -->

Read `_drill/math_catalog/families.txt`: the numbered result families from OpenAI's math
manuscript collection (github.com/openai/math, CONTENTS.md, Apache-2.0), one per line.

Answer these four questions from the file only:
1. What is the number of "Trace cones and Razak–Jacelon stabilization"? (three digits)
2. What is the title of family 088?
3. What is the title of family 123?
4. How many families does the file list?

Write `_drill/math_catalog/answer.md` with exactly four lines, like this:
q1: <answer>
q2: <answer>
q3: <answer>
q4: <answer>
If something is not in the file, write `not listed` for it. Never guess.
