# Product Log Conventions (v1)

> Working conventions, v1: reference, not law — follow what fits, override what doesn't, note why. Source labels and the rest: `overview.md`, convention 13.

> Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland), marked where they appear.
> License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland).

The product log is the first layer. Its template is `product-backlog-template.md`; the Scrum Master usually writes it with the Product Owner. Paths starting with `../` are relative to the scrum-kernel skill folder.

## Starting

1. **One product log** — *Author's practice.* Every project, new or old, starts by writing one product log from the template.
2. **Blank page** — *Author's practice.* When neither the product nor its architecture is clear, the IDEO methods alone will not make them clear; run a design (design-kernel skill), which adds the design sprint, a prototype, and a test to those methods. Until its conclusions flow back, the product log holds less: a challenge in place of the product, questions in place of acceptance criteria, and a provisional roadmap in place of the architecture.
3. **Facts first, then questions** — *Supplement.* The Scrum Master looks up the facts itself; what the Product Owner must decide goes into one message, numbered, each question with a recommended answer.

## Each part

4. **Product and Product Goal** — *Author's practice.* Fill sections 1.1 and 1.2 as the template shows; the vision line is optional.
5. **Two kinds of Done** — *Author's practice.* Outcome Done covers the value the product delivers to its stakeholders; Output Done covers the quality of every Increment. A Sprint picks the items that matter to it; the whole Definition of Done still applies. Write the Definition of Done precisely: add an item only when it holds in every case you can foresee, not just because it came up; one you are unsure of goes into the acceptance criteria instead.
6. **Stakeholders in a short table** — *Author's practice.* Section 2.1 lists the stakeholders in a short table, not a long profile per person. A Stakeholder subagent gets one row as its identity, and the AI fills in the details. If the table is empty, ask the Product Owner who belongs in it, and add the rows.
7. **Architecture as a map** — *Author's practice.* Section 2.2 starts with one map, drawn as `../design-kernel/define/make-a-map.md` describes: actors on top, AI roles included, the ending at the bottom, five to fifteen steps between, as a Mermaid `flowchart TD`. Add a subsection only for a step that needs more words.
8. **No TBD** — *Author's practice.* An unclear point becomes an item, and a Sprint or a design works it out.
9. **Technical design stays out** — *Author's practice.* Modules and interfaces are the Developer's; they live in the Increment.

## Items

10. **Seven columns** — *Author's practice.*

    | Column | What goes in it |
    | --- | --- |
    | # | PBI- and three digits, counting up: PBI-001, PBI-002, and so on |
    | Title | A short name |
    | User story | "As <someone from section 2.1>, I want …, so that …" |
    | Place | A step of the map, or a subsection of section 2.2 |
    | Status | Where the item stands: waiting, in Sprint NN, in a design |
    | Size | S — one or two sessions; M — three to five sessions; L — more than five sessions, to be split when refining |
    | Notes | Source, open points, draft acceptance criteria, refinement notes |
11. **Numbers, not ranks** — *Author's practice.* A number counts an item and must be unique; ranking is another matter — moving an item up the list — and the Product Owner does it when an order is needed.
12. **Items with the Scrum Master** — *Author's practice.* The Product Owner decides the items together with the Scrum Master, who works as a secretary. At Planning the Product Owner leads the selection, and the Scrum Master and the Developer say when it is too much or too little. The measure is the Sprint Goal: every selected item serves it, and an item the goal still needs is added — never one just to fill the Sprint. *Departs from the Scrum Guide on purpose*, where "the Developers select items from the Product Backlog": the Product Owner sets the value direction, and the others say how much fits.
13. **Status lives here** — *Author's practice.* An item's status is written in the product log only; a sprint log names items by number.

## Refinement

14. **Refine any time, finish in the Sprint** — *Author's practice.* Refining in the product log only adds detail; the refinement is finished in the sprint log's section 2.2 (`sprint-log.md`, convention 6). The product log has no refinement section.
15. **Seven steps** — *Author's practice.* Refine one item at a time:
    1. Take one item; it is the point of view.
    2. Confirm the point of view, copied from the goal or the item without change.
    3. Open the item into How Might We questions and unclear points.
    4. Place each point: the Product Owner decides it, the Developer proposes a solution, or it needs research, which opens a design.
    5. Cut the item into items of a few sessions at most, with acceptance criteria.
    6. Check that no questions are left — the Developer's about what is meant, the Product Owner's about what will be built: the Developer restates each point, and the Product Owner agrees.
    7. The Product Owner says when refinement is over.

    Acceptance criteria already written in full here are not repeated in the sprint log.
16. **Where refined content goes** — *Author's practice.* A split-off item becomes a new row; long design content goes into the architecture, and the Place column points to it; short notes go into Notes; large material goes into `scrum/documents/` (`overview.md`, convention 5), referenced from Notes.

## Keeping it fresh

17. **Fresh at every Review** — *Author's practice.* Done items move to section 3.2, one line each, with the source, usually the archived sprint log in `scrum/documents/`; outdated architecture text and resolved open points are deleted; unfinished items go back to section 3.1. There is no revision record; version control keeps the history. Fresh means more than the items: the same Review goes through the whole `scrum/` folder, `scrum/documents/` included (`sprint-log.md`, convention 18).

## What stays fixed

18. **Goal fixed, plan flexible** — *Author's practice.* Items and acceptance criteria can be refined at any time; the Product Goal changes only on evidence against it, and only by the Product Owner. Write an item's change and its reason in its Notes, and a Product Goal change with its date and reason in section 1.2 (`overview.md`, convention 16).
