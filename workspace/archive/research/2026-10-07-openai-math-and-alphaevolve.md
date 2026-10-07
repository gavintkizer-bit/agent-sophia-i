# Two sources from the owner: OpenAI's math collection and AlphaEvolve

**Research date:** 2026-10-07 (written by Sophia; DeepMind's site is blocked on our network, so I read
the paper PDF on Google's storage instead; Cal indexes it)

## Question

What are these two sources, what do they really claim, and what can the crew learn from them about
keeping a train of thought across many sessions (Sophia's continuity goal)?

## Answer

### 1. OpenAI math manuscripts (github.com/openai/math)
- The collection holds 722 manuscripts in 372 result families, covering about 4,000 problems. Licence: Apache-2.0.
  The README says each result took about three hours of ChatGPT Pro thinking, and some results come with Lean
  formalizations. [https://github.com/openai/math README and CONTENTS.md, read 2026-10-07] **verified**
- `CONTENTS.md` is the map. Each family is numbered (for example "001. Milne's rationality conjecture and
  algebraic specialization") and lists its manuscripts with their abstracts. [CONTENTS.md, read 2026-10-07] **verified**
- `reasoning_traces/` holds 10 PDFs of the model's working notes. I read two of them: the irrationality
  exponent of π (about 16,000 words) and Kaplansky direct finiteness in characteristic two (about 11,000 words).
  [reasoning_traces/, read 2026-10-07] **verified**
- What the traces show about thinking over a long time:
  - Part II begins from Part I's written report, not from scratch.
  - Obstacles get short names ("recurring height barrier", "entropy trap").
  - Dead ends are written down together with the reason they failed.
  - Notes to self are terse ("Need derivative transverse directions to escape").
  This is my reading, quoted from the π trace. **verified (quotes)**

### 2. AlphaEvolve (Google DeepMind, white paper)
- It is an "evolutionary coding agent". LLMs propose code changes (diffs), evaluators score each new
  program, and promising ones go back into a program database that feeds the next prompts.
  [AlphaEvolve.pdf, Fig. 2 and §2] **verified**
- The database "is inspired by a combination of the MAP elites algorithm and island-based population
  models". It aims to resurface old ideas and to balance improving the best programs against keeping
  variety. [§2.5] **verified**
- It uses Gemini 2.0 Flash to generate many candidates quickly and Gemini 2.0 Pro for fewer, better suggestions. [§2.3] **verified**
- Results:
  - It multiplies 4×4 complex matrices with 48 scalar multiplications. That is the first improvement in this
    setting in 56 years over Strassen's algorithm. [abstract] **verified**
  - It was tested on more than 50 open math problems. It matched the best known answer on about 75% of them
    and improved on it on about 20%. [§1, §3.2] **verified**
  - A scheduling heuristic it found recovers on average 0.7% of Google's fleet-wide compute. [§3.3.1] **verified**
  - Kernels used in Gemini training got an average 23% speedup, which cut about 1% off Gemini's overall
    training time. [§3.3.2] **verified**
- The PDF is at https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf
  The paper is also arXiv 2506.13131. The blog post (deepmind.google) was blocked here and not read.

## What this means for the crew
- **Continuity (Sophia):** each evening, hand forward a report: where I am, obstacles named, dead ends
  with reasons. Don't just hand forward a summary.
- **Evolution (later):** keep several versions of the thread, score them (the owner's verdict plus a drill),
  and keep the best. That is the same loop at a tiny scale.
- **Drill (Hypatia):** `training/drills/math_catalog`. She has to find exact facts in CONTENTS.md without
  inventing them.

## Not for the crew
- Nothing here touches the owner's own creations. These are tools for thinking, not for making their art.
