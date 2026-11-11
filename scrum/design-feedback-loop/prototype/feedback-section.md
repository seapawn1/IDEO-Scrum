## Feedback

When the user says 「记一下」 or asks you to note an idea, complaint, or correction about one of their products, save it as feedback for that product. The user does not say where; you decide.

- **Which product**: decide from what the user said and what they are using, with the product table below. Spoken names are often misheard, so match the aliases too. Do not default to the current project: the user often talks about one product while working in another. If you are not sure, file it under `待认领`; do not guess.
- **A rule, not feedback**: if the point is a rule for how you should work in general, not about a product, save it as an ordinary global memory entry instead.
- **Where**: one file per point in `S:\SeaPawn-Memory\memory\GlobalMemory\feedback\<folder>\`, named `<YYYY-MM-DD>-<short-slug>.md`, with the usual frontmatter (`metadata.type: feedback`, and `metadata.product`). In the body: the date; the project the session was in; the user's words, verbatim; what was going on; what you take it to mean. Then add one line to the `## Feedback` section at the end of `S:\SeaPawn-Memory\memory\GlobalMemory\MEMORY.md`: `- [<product>：<title>](feedback/<folder>/<file>.md) — <the point in one line>`. Ordinary entries stay above that section.
- **Already there**: if the same point is already in `## Feedback`, do not add a second one; add the new words to its file.
- **Then**: reply with exactly one line, 「记下了 · <product> · 可改」 (or 「已有这一条 · <product> · 补了原话」), and nothing else: no file paths, no notes. Ask nothing, and go back to the work at hand.
- **Use them now**: the lines in `## Feedback` are standing instructions, in force right away, before the product itself is changed. A line applies whenever your work touches what it is about, in any project: using that product or its method (for IDEO-Scrum, its design and Sprint process), not only working on it. Before you produce a plan, a map, a design, or code, check the lines; follow each one that applies, and name it in a few words (「照 Feedback：设计地图要粗」), so the user sees the point at work and can judge it.
- **When updating a product** (before refining its product log or opening a Sprint): read its lines in `## Feedback` and the `待认领` lines, open their files, and list the points to the user grouped by theme. The user decides what goes into the product log. When a point goes in, add its PBI number to the end of its line and keep following it; delete the line and its file only when the product has been changed. Git keeps them.

| Product | Folder | Also heard as |
| --- | --- | --- |
| IDEO-Scrum: the ideo-scrum plugin, design thinking and Scrum for Claude Code | IDEO-Scrum | Ido Scrum, IDU Scrum, IDEO Scrum |
| ClaudeDream: the dreaming plugin, which turns transcripts into memory | ClaudeDream | dreaming, Claude Dream |
| SeaPawn | SeaPawn | Sea Pawn |
| ClaudeToCodex | ClaudeToCodex | Claude to Codex |
| MTGP | MTGP | |
| StrataGP | StrataGP | |
| MidTerm | MidTerm | |
| Hanlin | Hanlin | |
| SGCC | SGCC | |
| Engineering-Rock-Mechanics | Engineering-Rock-Mechanics | |
| RockMass-rating-agent | RockMass-rating-agent | |
| paper-writing-polish | paper-writing-polish | |
