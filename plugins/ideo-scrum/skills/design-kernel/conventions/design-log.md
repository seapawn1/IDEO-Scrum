# Design Log Conventions (v1)

> Working conventions, v1: reference, not law — follow what fits, override what doesn't, note why. Source labels and the rest: the scrum-kernel skill's `conventions/overview.md`, convention 13.

The design log template is `design-backlog-template.md` in this folder. The book's techniques are in this skill's stage folders, with paths such as `ideate/sketch.md` relative to the skill folder; the methods are in the ideo-kernel skill. Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — these conventions say how a solo + AI team does that step, and they apply.

- **Role card** — one row of the product log's stakeholder table: who the stakeholder is, what they want, when to summon them. A role-card Stakeholder is a fresh subagent given one row as its identity; the AI fills in the details. If the table is empty, ask the Product Owner who belongs in it.
- **Folders** — `scrum/design-<suffix>/` holds a design in progress; a closed design's Review goes to the project's document folder (the scrum-kernel skill's `conventions/overview.md`, conventions 4 and 5).

## Where a design sits

1. **Design beside the Sprint** — *Author's practice.* A design is a module beside the Sprint, not inside it; the rule and the reason are in the scrum-kernel skill's `conventions/overview.md`, convention 2.
2. **Hard point, not the whole item** — *Author's practice.* From a Sprint, take out only the hard point that needs design; the rest of the Sprint goes on.
3. **Who** — *Author's practice.* The Designer is accountable for the design; the Scrum Master facilitates and records; the Product Owner decides the design goal, the chosen solution, and when the design is done. When one session plays both the Designer and the Scrum Master, write the same name in both fields of the header.
4. **Open a design** — *Author's practice.* Pick a suffix that says what the design is about, with no number; create `scrum/design-<suffix>/`; copy the template into it as `DesignBacklog.md`; fill in the header: where the design came from, the branch (convention 5), the Product Owner, the Designer, the Scrum Master, and the Now line (convention 21). The folder holds the log and the prototypes; prototypes never go into an Increment.
5. **Branch** — *Decide on the spot.* Whether the design branches from the Sprint branch or from `main` is decided when it opens. Do not name it `<sprint-branch>/<name>`: git cannot hold both `a` and `a/b` as branch names.
6. **Ask the PO** — *Author's practice.* See the scrum-kernel skill's `conventions/overview.md`, convention 9.

## How the log is written

7. **Five chapters, not five days** — *Author's practice.* One chapter per stage — Empathize, Define, Ideate, Prototype, Test — not the book's Monday to Friday, and no notes section. Each chapter records what its stage produced, not the steps taken.
8. **IDEO always in play** — *Author's practice.* The book's techniques do not limit the methods: in any stage, use any ideo-kernel method the work needs. Above all in Ideate, the book's steps are one way to a solution, not the only one; use the ideo-kernel's Ideate methods — How Might We Questions, Brainstorming, Analogous Empathy, Yes, And! Brainstorm, Brainstorm selection — alongside them or in their place.
9. **Renamed terms** — *Author's practice.* The book's *long-term goal* is the **design goal**, its *sprint questions* the **design questions**, its *Decider* the **Product Owner**, its *Facilitator* the **Scrum Master**.

## Where a solo + AI team departs from the book

Conventions 10 to 18 cover only what differs from the book; for everything else, follow the excerpts.

10. **Experts when needed** — *Author's practice.* Write the challenge, the design goal, and the design questions first; ask experts and do research only when these are still unclear. The experts are the Product Owner, in the conversation, and the stakeholder rows, each played by a fresh subagent. Before asking experts, draft a rough map (`define/make-a-map.md`); the log keeps what changed, not each interview.
11. **Map and questions in the log** — *Author's practice.* Draw the map as a Mermaid `flowchart TD`, actors at the top and the ending at the bottom. The Product Owner picks the How Might We questions that matter — no dot voting. There is no target step: if the map holds more than one design's worth of work, split the rest out into another design or into items (`define/pick-a-target.md` shows how the book narrows a map).
12. **Lightning Demos** — *Author's practice.* Subagents can search for existing ideas in parallel; the list is working material, not part of the log.
13. **Isolated solutions** — *Author's practice.* Several fresh subagents, unable to see one another, each produce one complete solution sketch, in words or Mermaid, from chapters 1 and 2, the gathered ideas, and `ideate/sketch.md`, or from an ideo-kernel Ideate method.
    *Decide on the spot:* how many subagents to run, and on which model.
14. **Choosing is the key step** — *Author's practice.* The Scrum Master runs the book's decision (`ideate/decide.md`) in the conversation; role-card Stakeholders give a straw poll if the Product Owner wants one; the Product Owner makes the final call, with no search for consensus. Only the chosen solution goes into section 3.1.
15. **Combine or rumble** — *Author's practice.* Combine winners that fit together; when two conflict, prototype both and let the test decide (`ideate/rumble.md`). The Product Owner decides which.
16. **Storyboard** — *Author's practice.* Optional: when the solution needs it before the prototype, the Designer writes a storyboard of about fifteen steps in section 3.2 (`ideate/storyboard.md`).
17. **Just enough prototype** — *Supplement.* Build in the design folder, following the chosen solution, real enough for honest reactions (`prototype/fake-it.md`): made quickly and thrown away after, while the surface the tester sees appears real. Subagents can build the parts while one session stitches them together; do a trial run against the solution and the design questions before testing.
    *Decide on the spot:* how real the prototype must be when the product has no screen — a document, a service, a process; agree it with the Product Owner.
18. **Role-card test** — *Author's practice.* Test with stakeholder rows, each a fresh subagent given only its row, the prototype, and the tasks; the Product Owner tests too. The Designer runs the Five-Act Interview (`test/interview.md`); a grid of reactions is working material; chapter 5 keeps who tested, what showed up, and the answer to each design question. The book tests five customers; here, test every row the design touches, and add runs while the patterns are unclear.

## Closing

19. **Close as a Review** — *Author's practice.* A design closes when its questions are answered or the Product Owner stops it. Rewrite the log as one Review document, rename it `design-<suffix>.md`, and move it to the document folder. Delete the prototypes and other files; git keeps them. Refresh the product log.
    *Supplement:* the Review holds the challenge and the design questions, the chosen solution, each question's test conclusion, where the conclusions flowed back, and the commit that holds the prototype.
20. **Retro as in a Sprint** — *Author's practice.* No Retro chapter; lessons are written as in the scrum-kernel skill's `conventions/sprint-log.md`, convention 19.

## Resuming

21. **Resume from the header** — *Author's practice.* Keep the header's Now line current: the stage, and the next step. A session that picks up the design reads it first.

## What stays fixed

22. **Goal fixed, plan flexible** — *Author's practice.* The design goal is sharpened during Empathize; once set, only the Product Owner changes it. The questions, the map, and the solution may change with what the work shows; write what changed and why in the chapter it belongs to (the scrum-kernel skill's `conventions/overview.md`, convention 16).
