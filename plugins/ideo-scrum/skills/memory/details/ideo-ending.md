# The five modes and the IDEO log

When to open an IDEO log, the four operational disciplines for solo + AI discovery, where an IDEO run lives, where its conclusions go, and how prototypes and test evidence are handled when the work is done. Read this file before running the IDEO five modes, opening an IDEO log, or ending one. The list lines that point here are `open-ideo-log`, `diverge-first`, `isolated-sketches`, `prototype-not-increment`, `keep-test-evidence`, and `ideo-log-ends`.

## When to open an IDEO log (`open-ideo-log`)

- The IDEO five modes (`../ideo-kernel/SKILL.md`) are the shared toolbox behind every practice — not a parallel track beside Scrum Sprints.
- When one or two methods in a single session are enough, write their output into the log they serve — a Sprint's Increment notes, chapter 2.2 refinement notes, or the product log's Notes.
- When the five modes make a run of their own — more than one or two methods, or more than one session — open an IDEO log from `../../template/ideo-backlog-template.md`: `scrum/ideo-<suffix>/IdeoBacklog.md`, five chapters (one per mode), with no Product Owner stage gates between modes.
- Each chapter holds what that mode produced, not every step taken.
- Before a mode, read its file in `../ideo-kernel/IDEO-modes/`; before a method, read the method's file, as the ideo-kernel skill's Use Protocol says.

## Four operational disciplines

1. **Diverge before converging (`diverge-first`)** — Before choosing a solution, diverge first using at least two methods, including at least one Ideate method from `../ideo-kernel/SKILL.md`. Go for quantity and hold judgment back; keep raw ideas as working material, and record only the meaningful options and the Product Owner's choice in the log.
2. **Isolated subagent sketches (`isolated-sketches`)** — When several solutions that genuinely differ in approach are wanted, dispatch fresh subagents that cannot see one another to sketch independently. Give each the problem context and its own inspiration (or none), never one shared example summary (a shared summary causes subagents to converge on one idea), and tell them not to copy the current implementation. If the host still injects shared project instructions, note that in the log.
3. **Prototypes are for learning, never an Increment (`prototype-not-increment`)** — Build prototypes rough, quick, and disposable to test risky assumptions; never slip a prototype into a formal Increment.
4. **Preserve test evidence (`keep-test-evidence`)** — Record who tested (users, the Product Owner, or fresh role-card Stakeholders), what they did and said, and the answer to each question in chapter 5 of `IdeoBacklog.md` (or in the log served). Keep this evidence and the conclusions whether or not the conclusions are later built.

## Where it lives and branches

- The log, any temporary prototypes, and working material live in `scrum/ideo-<suffix>/`.
- By default, do **not** open a separate branch for an IDEO run: if it serves a Sprint, share that Sprint's branch; if it serves the product log, work on the current branch or `main` (a user who wants a separate branch may still open one).
- The log has no commitment of its own: its `For` field holds the relative path to the log it serves — `../ProductBacklog.md` or a Sprint's `../sprint-NN-<suffix>/SprintBacklog.md` — where the commitment is kept. Its header lines `Now` and `Waiting for PO` follow `../../template/ideo-backlog-template.md`.

## Conclusions, prototypes, and archiving (`ideo-log-ends`)

- **Conclusions**: flow back to the log that asked (the product log or the sprint log), and the Product Owner decides what changes.
- **Prototypes**: while an associated Sprint is actively using a prototype or its ideas as a reference specification, keep the prototype in that Sprint's working folder or the IDEO folder and clean it up when that Sprint closes. If there is no associated Sprint, or once the work is settled and the prototype is no longer needed, the prototype files themselves may be deleted — prototypes are never Increments.
- **Test evidence and archiving**: keep `IdeoBacklog.md` together with its recorded test evidence and conclusions, and archive it into `scrum/documents/ideo/ideo-<suffix>.md` (preserving any key supporting evidence beside it) at the next Sprint Review (`details/closing.md`, `one-closing-commit`). When a blank-page run finishes before any Sprint exists, archive it at the first Sprint Review or once the Product Owner confirms.
