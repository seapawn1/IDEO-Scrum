# Product Log Conventions (v1)

> These are working conventions, v1 — the author's reading of Scrum and design thinking for solo + AI teams. They are less precise than the official guides. Use them as reference: follow what fits, override what doesn't, and note why. Where a convention departs from the official guide on purpose, it says so and gives the reason.

> Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland) and the Scrum Guide Expansion Pack v2026.1 (Ralph Jocham, John Coleman, Jeff Sutherland), marked where they appear; the rest is the author's working conventions.
> License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland; © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland).

Each convention has a short name, so it can be referred to in conversation, and one source label:

- **Author's practice** — how the author works.
- **Supplement** — inferred by the author's assistant; not yet confirmed in practice.
- **Decide on the spot** — no fixed rule; decide when it comes up.

The product log is the first layer: every Sprint and every design answers to it. Its template is `product-backlog-template.md` in this folder, and a product log made from it is named `ProductBacklog.md`. How the product log fits with sprint and design logs is in `overview.md`; the Scrum Master usually writes the product log with the Product Owner.

## Starting

1. **One product log** — *Author's practice.* Every project, new or old, starts by writing one product log from the template. There is only one, and only one way to write it.
2. **Blank page** — *Author's practice.* When a project starts from nothing and the first chapter is unclear — what the product is, who it is for, what goal to set — make it clear with the IDEO methods in the ideo-kernel skill: empathize, define, interview.
3. **Facts first, then questions** — *Supplement.* The Scrum Master looks up the facts itself. What the Product Owner has to decide goes into one message, numbered, each question with a recommended answer.

## Each part

4. **Product and Product Goal** — *Author's practice.* Section 1.1 says what the product is and where its boundary lies. Section 1.2 may open with one line of vision, then states the current Product Goal and the directions after it. The Scrum Guide Expansion Pack puts the relation this way: "The Product Goal often supports the Product strategy and Product Vision."
5. **Two kinds of Done** — *Author's practice.* The Definition of Done has two parts, as the Scrum Guide Expansion Pack names them: Outcome Done, for the value the product delivers to its stakeholders, and Output Done, for the quality of every Increment. A Sprint picks the items that matter to it, and the whole Definition of Done still applies.
6. **Stakeholders in a short table** — *Author's practice.* Section 2.1 lists who the stakeholders are in a short table, not one long card per person; add a column if it helps. When any role summons a Stakeholder subagent — for an outside view, a review, a test, or a second opinion on a solution — it gives the subagent one row as its identity, and the AI writes whatever details it needs. If the table is empty, ask the Product Owner who belongs in it, and add the rows.
7. **Architecture as a map** — *Author's practice.* Section 2.2 starts with one map, drawn as the design-kernel skill's `define/make-a-map.md` describes: the actors on top — the stakeholders, and the AI roles too — the ending at the bottom, five to fifteen steps in between, with words, arrows, and a few boxes. Draw it in Mermaid as `flowchart TD`. Add a subsection after the map only for a step that needs more words.
8. **No TBD** — *Author's practice.* The product log does not say "to be decided". An unclear point becomes a product backlog item, and a Sprint or a design works it out.
9. **Technical design stays out** — *Author's practice.* The technical architecture — modules, interfaces — is the Developer's skill. It lives in the Increment, not in the product log.

## Items

10. **Seven columns** — *Author's practice.* Each current item has seven columns:

    | Column | What goes in it |
    | --- | --- |
    | # | The item's number: PBI- and three digits, counting up — PBI-001, PBI-002, and so on |
    | Title | A short name |
    | User story | "As <someone from section 2.1>, I want …, so that …" |
    | Place | Where the item sits: a step of the map, or a subsection of section 2.2 |
    | Status | Where the item stands, such as waiting, in Sprint NN, or in a design |
    | Size | S — one or two sessions; M — about half a Sprint; L — a whole Sprint, to be split when refining |
    | Notes | Source, open points, draft acceptance criteria, refinement notes |
11. **Numbers, not ranks** — *Author's practice.* An item's number only counts it; it is not a priority, and there is no ranking column. The Product Owner orders the items when a person needs the order.
    *Departs from the Scrum Guide on purpose.* The Scrum Guide says: "The Product Backlog is an emergent, ordered list of what is needed to improve the product." Reason: the AI roles rarely need the order; the Product Owner ranks the items when a person needs it.
12. **Items with the Scrum Master** — *Author's practice.* The Product Owner decides the product backlog items together with the Scrum Master, who works as the Product Owner's secretary. At Sprint Planning the Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little.
    *Departs from the Scrum Guide on purpose.* The Scrum Guide says: "The Product Owner may do the above work or may delegate the responsibility to others. Regardless, the Product Owner remains accountable." and "Through discussion with the Product Owner, the Developers select items from the Product Backlog to include in the current Sprint." Reason: the Product Owner sets the value direction; the Scrum Master and the Developer say how much fits.
13. **Status lives here** — *Author's practice.* An item's status is written in the product log and nowhere else. A sprint log names the items by number and does not copy their status; progress goes into the sprint log's notes.

## Refinement

14. **Refine any time, finish in the Sprint** — *Author's practice.* The Scrum Guide says: "Product Backlog refinement is the act of breaking down and further defining Product Backlog items into smaller more precise items. This is an ongoing activity to add details, such as a description, order, and size." In the product log, refinement only adds detail; it is finished in the sprint log's refinement section, at Sprint Planning (`sprint-log.md`, convention 6). There is no separate refinement section here.
15. **Seven steps** — *Author's practice.* Refine one item at a time:
    1. Take one item. The item is the point of view; do not write a separate one.
    2. Confirm the point of view: copy it from the goal or the item, without changing it.
    3. Open the item into How Might We questions and unclear points.
    4. Place each point: the Product Owner decides it, the Developer proposes a solution, or it needs research — research opens a design (design-kernel skill), and the rest goes on.
    5. Cut the item into small items, each done in a few sessions at most, and write their acceptance criteria.
    6. Check the two "no more questions": the Developer no longer needs to ask "what do you mean?", and the Product Owner no longer needs to ask "what are you building?". The test: the Developer restates each point in their own words, and the Product Owner agrees.
    7. The Product Owner says when refinement is over.

    Acceptance criteria may be written in the product log or added in the sprint log; what the product log already says in full is not repeated there.
16. **Where refined content goes** — *Author's practice.* Refinement does not get a section of its own; each kind of content goes to its place:
    - an item split off becomes a new row;
    - long design content goes into the architecture, and the item's Place column points to it;
    - short notes go into the item's Notes;
    - large material goes into the project's document folder, and the Notes reference it (`overview.md`, convention 5).

## Keeping it fresh

17. **Fresh at every Review** — *Author's practice.* At each Sprint Review, bring the product log up to date and keep it complete, with nothing that no longer matters:
    - done items move to section 3.2, one line each, with the source, usually the archived sprint log;
    - outdated architecture text and resolved open points are deleted;
    - items not finished go back to section 3.1;
    - there is no revision record; version control keeps the history.

## What stays fixed

18. **Goal fixed, plan flexible** — *Author's practice.* Product backlog items and their acceptance criteria can be refined at any time. The Product Goal stays, and only the Product Owner changes it, when there is evidence against it; the Scrum Guide says: "The Product Goal is the long-term objective for the Scrum Team. They must fulfill (or abandon) one objective before taking on the next." When an item changes, write what changed and why in its Notes. When the Product Goal changes, write the date and the reason in section 1.2. Version control keeps the rest. The whole rule, for all three logs, is in `overview.md`, convention 16.
