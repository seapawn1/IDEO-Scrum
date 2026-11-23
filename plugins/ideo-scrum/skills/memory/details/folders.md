# Layers and folders

How a project's Scrum work is laid out: the three layers and where files go. Read this file when you set up a project or decide where a file belongs. The list lines that point here are `three-layers`, `scrum-folders`, `where-files-go` and `working-material`.

## Three layers (`three-layers`)

Scrum Sprint is the single delivery track; the IDEO five modes (`../ideo-kernel/SKILL.md`) are the shared toolbox behind every layer.

| Layer | File | Commitment | Accountable | Facilitates |
| --- | --- | --- | --- | --- |
| 1 | Product log | Product Goal | Product Owner, with the Scrum Master | — |
| 2 | Sprint log | Sprint Goal | Developer | Scrum Master |
| 3 | Increment: code or documents, as the Definition of Done says | Definition of Done | Developer | — |

The third layer is not a log and has no prescribed method; it relies on the skills of whoever does the work. Increments add up into the product. Prototypes built with the IDEO five modes exist to learn and never enter an Increment (`prototype-not-increment`); a standalone run of the five modes keeps its log and evidence under its own rule (`open-ideo-log`, `keep-test-evidence`, `ideo-log-ends`).

## Folders (`scrum-folders`)

`scrum/` holds all of the Scrum work:

- `ProductBacklog.md`;
- `ScrumBoard.html`, the board written from the logs, which keeps no state of its own (`board-owns-nothing`);
- `sprint-NN-<suffix>/` with `SprintBacklog.md` and its working files;
- `ideo-<suffix>/`, unnumbered, with `IdeoBacklog.md`, temporary prototypes, and working files (by default sharing the Sprint branch it serves, or the current/main branch when serving the product log);
- `documents/` (`where-files-go`), including archived Sprint logs and `documents/ideo/` for archived IDEO logs and test evidence.

The active folders may still hold work that ended and is awaiting Review; read the log’s `Now` before resuming. This is the author’s layout; use your project’s own places if it has them.

## Where files go (`where-files-go`)

- A file that serves only one log usually stays in its working folder and can be cleaned up when that work ends.
- Temporary prototypes used as reference by an associated Sprint stay in that Sprint's folder or the IDEO folder until the Sprint closes, then get cleaned up; recorded test evidence and conclusions stay with `IdeoBacklog.md` and archive into `scrum/documents/ideo/` at Review (`details/ideo-ending.md`, `details/closing.md`).
- Files serving the whole Scrum also go into `scrum/documents/`, and the logs reference them.
- A project can use its existing archive subfolders.
- The project’s own documentation, such as a user manual or API notes, stays where the project keeps it, such as `docs/` at the root.

## Working material (`working-material`)

- Keep working material out of the log itself; link to preserved test evidence or shared files where needed (`where-files-go`).
- Key material of general use can go into the project’s memory or instructions, and a large important file goes into `scrum/documents/`.
- Retro lessons go only where `retro-in-memory` says — the project’s memory, else the repository notes the project keeps for lessons — never in instructions.
