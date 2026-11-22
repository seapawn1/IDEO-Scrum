# An IDEO log: where it lives and how it ends

When to open an IDEO log, where a run of the five modes keeps its work, where its conclusions go, and what happens to its prototypes when the work is done. Read this file when you open an IDEO log, finish one, or decide what to do with a prototype from one. The list lines that point here are `open-ideo-log` and `ideo-log-ends`.

## When to open an IDEO log (`open-ideo-log`)

- Outside a design, use one or two methods when that is enough; their output goes into the log they serve — a Sprint's Increment notes, the product log's Notes.
- When the five modes make a run of their own — more than one or two methods, or more than one session — open an IDEO log: `scrum/ideo-<suffix>/IdeoBacklog.md`, five chapters, one per mode, with no Product Owner gate between them.
- Inside a design, the methods a stage uses (`ideo-in-every-stage`) write their output into that stage's chapter of the design log; no IDEO log is opened for them.
- Each chapter holds what that mode produced, not every step taken.
- Before a mode, read its file in `../ideo-kernel/IDEO-modes/`; before a method, read the method's file, as the ideo-kernel skill's Use Protocol says.

## Where it lives

The log, the prototypes, and the working material live in `scrum/ideo-<suffix>/`. The log has no commitment of its own: its For cell holds the relative path to the log it serves — the product log, a Sprint's `SprintBacklog.md`, or a design's `DesignBacklog.md` — where the commitment is kept. Its header lines `Now` and `Waiting for PO` come from the IDEO log template.

## How the conclusions go back

The conclusions flow back to the log that asked for it — the product log, the sprint log or the design log — and the Product Owner decides what changes.

## When the work is done

Keep the log: the first Sprint Review after that archives it (`one-closing-commit` and `details/closing.md` say how a Review archives).

## What happens to a prototype

- A prototype whose conclusions will be built goes to the Sprint that builds them, as that Sprint's specification.
- If that Sprint is not open yet, keep the prototype in the IDEO folder until handoff.
- Any other standalone IDEO prototype is deleted when the work is done.

## Open points for the Product Owner

- The old rule also described the header format (`Now` on its own header line with the current mode and next step, then `Waiting for PO` with the number and short question of each pending decision, separated by semicolons, or `None`; both updated with the log change that causes them). The IDEO log template has that format (lines 4-5; the template now sits in the plugin's `template/` folder), so it is not repeated here. The rule that both are updated with the log change that causes them is also in the sprint log's handoff rule (`log-is-the-handoff`).
