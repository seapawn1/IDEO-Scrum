# Layers and folders

How a project's Scrum work is laid out: what sits beside a Sprint, the three layers, and where files go. Read this file when you set up a project, open a design, or decide where a file belongs. The list lines that point here are `designs-beside-sprints`, `three-layers`, `scrum-folders`, `where-files-go` and `working-material`.

## Sprints and designs side by side (`designs-beside-sprints`)

Treat Sprints and designs as peers under the product log: a Sprint, the Developer's, delivers an Increment; a design, the Designer's, delivers a prototype and conclusions.

- Open a design when an item needs design, when Sprint refinement hits a hard point, or for a blank page (`blank-page`); it is not part of a Sprint.
- Whether a question needs a design sprint or the five modes is `sprint-or-modes`.
- Decide item by item whether design is needed.
- A design's conclusions still land through a Sprint.
- An Increment need not be code — the Definition of Done says what it is.

This departs from the Scrum Guide; the reason is in `details/departures.md`.

## Three layers (`three-layers`)

| Layer | File | Commitment | Accountable | Facilitates |
| --- | --- | --- | --- | --- |
| 1 | Product log | Product Goal | Product Owner, with the Scrum Master | — |
| 2 | Sprint log | Sprint Goal | Developer | Scrum Master |
| 2 | Design log | Design goal | Designer | Scrum Master |
| 3 | Increment: code or documents, as the Definition of Done says | Definition of Done | Developer | — |
| 3 | Prototype: built to learn, never in an Increment; a design’s prototype stays with its design evidence | Design questions | Designer | — |

The third layer is not a log and has no prescribed method; it relies on the skills of whoever does the work. Increments add up into the product. The design’s conclusions flow back; its working material, including the prototype, stays with the design and can be referenced by the Sprint that builds those conclusions (`details/design-ending.md`). The standalone IDEO log has its own rule (`open-ideo-log`, `ideo-log-ends`).

## Folders (`scrum-folders`)

`scrum/` holds all of the Scrum work:

- `ProductBacklog.md`;
- `ScrumBoard.html`, the board written from the logs, which keeps no state of its own (`board-owns-nothing`);
- `sprint-NN-<suffix>/` with `SprintBacklog.md` and its working files;
- `design-<suffix>/`, unnumbered, with `DesignBacklog.md`, prototypes, and other working material;
- `ideo-<suffix>/`, unnumbered, with `IdeoBacklog.md`, prototypes, and working files;
- `documents/` (`where-files-go`).

The active folders may still hold work that ended and is awaiting Review; read the log’s `Now` before resuming. This is the author’s layout; use your project’s own places if it has them.

## Where files go (`where-files-go`)

- A file that serves only one log usually stays in its working folder and can be cleaned up when that work ends.
- The design’s original working material is the exception: retain it with the design, then move it with its log into the existing `scrum/documents/` archive at Review (`details/design-ending.md`, `details/closing.md`).
- Files serving the whole Scrum also go into `scrum/documents/`, and the logs reference them.
- A project can use its existing archive subfolders.
- The project’s own documentation, such as a user manual or API notes, stays where the project keeps it, such as `docs/` at the root.

## Working material (`working-material`)

- Keep working material out of the log itself; link to the retained design originals (`where-files-go`).
- Key material of general use can go into the project’s memory or instructions, and a large important file goes into `scrum/documents/`.
- Retro lessons go only where `retro-in-memory` says — the project’s memory, else the repository notes the project keeps for lessons — never in instructions.

## Open points for the Product Owner

- None. Convention numbers in the old text became handles; nothing else was changed.
