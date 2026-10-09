# Archivist: research a topic
<!-- output: archive/research/{date}-{slug}.md -->

Research this topic on the web: **{topic}**

Write `workspace/archive/research/{date}-{slug}.md` with:

1. **Question**: the topic in one sentence, and why it matters to the crew (if you can tell
   from `workspace/notes/sophia_memory.md`; read it first, but never put its contents in a search).
2. **Answer**: 3-8 short bullets. Each ends with its source in brackets: [URL, read {date}] and
   **verified** (only with its own checked quote in "quotation marks" on that line) or **unverified**.
3. **Quotes**: up to 3 exact quotes that passed `verify_quote`, each with its URL.
4. **Disagreements and doubts**: where sources differ, what you couldn't confirm.
5. **Sources**: every URL used, one line each on what it is and how trustworthy.

Then append 1-3 proposed facts for Sophia's memory to `workspace/archive/for_sophia.md` in this
form (create the file if it's missing):

```
## {date} | research: {topic}
- [ ] <one-line fact> (source: <URL>, verified: "<the exact checked quote>")
- [ ] <one-line fact> (source: <URL>, unverified)
```
A proposal marked verified carries the same checked quote as its fact in the note, word for word.

Keep the note under 600 words. Use 2-5 good sources, not twenty.
