# Life Lab resources (from Gavin, 2026-10-13)

Read by Sophia on 2026-10-13. Each entry gives what the resource is, what Life Lab could borrow, and any rights notes.
Gavin, 2026-10-13: these are free to use for building our own code (Life Lab isn't published anywhere). So I study
how they work and write our own; I don't paste their code in.

## Cellular automata, closest to our game
- **Life Universe**, https://oimo.io/works/life/ (source: github.com/saharan/works, folder `life`, written in Haxe).
  The page loads a script and its text says nothing, so I couldn't see the demo itself. The name and source point to
  a Game of Life you can zoom through at enormous scales (Life built inside Life). No license shown: ideas only.
  *Borrow:* zoom and pan, and a fast-forward for big worlds.
- **Langton's Ant Colony / turmites**, https://evolvecode.io/turmites/index.html (my best guess at the truncated link).
  Ants on a grid flip a cell's color and turn by a rule table; colonies, presets, start positions, up to several
  states and colors, speed control. *Borrow:* an "ant" mode. One agent with a tiny rule makes a striking
  test: can an AI predict where the ant will be after N steps, or say honestly that it can't?
- **Particle Life**, https://sandbox-science.com/particle-life (my best guess; the page loaded only a placeholder for
  me). SandboxScience also lists Game of Life and HashLife. Particle Life is colored particles that attract or repel each
  other by a small table of numbers, which gives lifelike swarms. *Borrow:* a second, continuous world for the lab later.
- **A New Kind of Science**, https://www.wolframscience.com/nks/ (Stephen Wolfram, 2002; free to read online).
  Chapters that matter for us: 2 "The Crucial Experiment", 3 "The World of Simple Programs", 5 "Two Dimensions and
  Beyond", 6 "Starting from Randomness" (the **four classes of behavior**), 11 "The Notion of Computation" (Rule 110).
  *Borrow:* (1) a one-row world, where Rule 90 draws the Sierpinski triangle from a single cell, a known fractal and a
  clean companion to our fractal seed; (2) tag each experiment's outcome with Wolfram's four classes (dies out or
  settles, repeats, random-looking, complex).
- **Hypergraph rewriting**, https://met4citizen.github.io/Hypergraph/ (my best guess; source github.com/met4citizen/Hypergraph).
  3D graphs that grow by rewrite rules (Wolfram Physics style), with space, time and "multiway" views. Advanced. *Borrow:*
  later, the idea of watching one rule from several views (space, time, branching).

## Physics and space, for inspiration and future worlds
- **Universe Sandbox**, https://universesandbox.com/ (a paid desktop app: gravity, collisions, climate, stars,
  black holes). *Borrow:* the feel of "change one number, watch a world respond", which the lab panel already does.
- **NASA SVS 12656**, https://svs.gsfc.nasa.gov/12656/: "Big Bang Animation, 5k Resolution" (2017), an artist's
  interpretation. Credit: NASA's Goddard Space Flight Center / CI Lab (producer Scott Wiessinger, animator Krystofer
  Kim). Use follows NASA's media guidelines, with credit. *Borrow:* inspiration for a "start from one seed" opening.
- **Hydrogen atom orbitals**, https://www.falstad.com/qmatom/ (Paul Falstad's 3D viewer of hydrogen orbitals,
  real and complex). *Borrow:* the plain, explorable-controls style, rather than its physics.

## Couldn't recover
- **Pexels video** "https://www.pexels.com/video/an-artis..." was truncated, and I can't guess which video it is.
  Sophia asked Gavin for the full link.

## What I'd build next, in order
1. Wolfram's four-class tag on each experiment, plus a one-row Rule 90 world (fractal from one cell).
2. Ant mode (turmites), with a code-checked AI prediction test.
3. Zoom, pan and fast-forward for big worlds.
