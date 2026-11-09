# Design Log Conventions (v1)

> Working conventions, v1: reference, not law — follow what fits, override what doesn't, note why. Source labels and the rest: `../scrum-kernel/overview.md`, convention 13.

The design log template is `design-backlog-template.md` in this folder. Paths here are relative to the design-kernel skill folder; the stages, the book's excerpts, and the methods are listed in this skill's `SKILL.md`. Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — these conventions say how a solo + AI team does that step, and they apply.

## Where a design sits

1. **Hard point, not the whole item** — *Author's practice.* From a Sprint, take out only the hard point that needs design; the rest of the Sprint goes on.
2. **Who** — *Author's practice.* The Designer is accountable for the design, and the Scrum Master facilitates and records; what the Product Owner decides is in `SKILL.md`, Use Protocol step 6. When one session plays both the Designer and the Scrum Master, write the same name in both fields of the header.
3. **Open a design** — *Author's practice.* Pick a suffix that says what the design is about, with no number; create `scrum/design-<suffix>/`; copy the template into it as `DesignBacklog.md`; fill in the header: where the design came from, the branch (convention 4), the Product Owner, the Designer, the Scrum Master, and the Now line (convention 20). The folder holds the log, the prototypes, and the working material — sketches, gathered ideas, a grid of reactions; prototypes and working material never go into an Increment.
4. **Branch** — *Decide on the spot.* Whether the design branches from the Sprint branch or from `main` is decided when it opens. Do not name it `<sprint-branch>/<name>`: git cannot hold both `a` and `a/b` as branch names.
5. **Ask the PO** — *Author's practice.* See `../scrum-kernel/overview.md`, convention 9.

## How the log is written

6. **Five chapters, not five days** — *Author's practice.* One chapter per stage — Empathize, Define, Ideate, Prototype, Test — not the book's Monday to Friday, and no notes section. Each chapter records what its stage produced, not the steps taken.
7. **IDEO always in play** — *Author's practice.* The rule is in `SKILL.md`. Above all in Ideate, use the ideo-kernel's Ideate methods — How Might We Questions, Brainstorming, Analogous Empathy, Yes, And! Brainstorm, Brainstorm selection — alongside the book's steps or in their place.
8. **Renamed terms** — *Author's practice.* See the first paragraph of `SKILL.md`.

## Where a solo + AI team departs from the book

Conventions 9 to 17 cover only what differs from the book; for everything else, follow the excerpts.

9. **Experts when needed** — *Author's practice.* Write the challenge, the design goal, and the design questions first; ask experts and do research only when these are still unclear. The experts are the Product Owner, in the conversation, and the role cards (`../scrum-kernel/overview.md`, convention 6), each played by a fresh subagent. Before asking experts, draft a rough map (`define/make-a-map.md`); the log keeps what changed, not each interview. After asking the experts or doing research, refine the challenge, the design goal, the design questions, and above all the map once more: fill the gaps and redraw the map.
10. **Map and questions in the log** — *Author's practice.* Draw the map as a Mermaid `flowchart TD`, actors at the top and the ending at the bottom. The Product Owner picks the How Might We questions that matter — no dot voting. There is no target step: if the map holds more than one design's worth of work, split the rest out into another design or into items (`define/pick-a-target.md` shows how the book narrows a map).
11. **Lightning Demos** — *Author's practice.* Subagents can search for existing ideas in parallel; the list is working material, not part of the log.
12. **Isolated solutions** — *Author's practice.* Several fresh subagents, unable to see one another, each produce one complete solution sketch, in words or Mermaid, from chapters 1 and 2, the gathered ideas, and `ideate/sketch.md`, or from an ideo-kernel Ideate method.
    *Decide on the spot:* how many subagents to run, and on which model.
13. **Choosing is the key step** — *Author's practice.* The Scrum Master runs the book's decision (`ideate/decide.md`) in the conversation; role-card Stakeholders give a straw poll if the Product Owner wants one; the Product Owner makes the final call, with no search for consensus. Only the chosen solution goes into section 3.1.
14. **Combine or rumble** — *Author's practice.* Combine winners that fit together; when two conflict, prototype both and let the test decide (`ideate/rumble.md`). The Product Owner decides which.
15. **Storyboard** — *Author's practice.* Optional: when the solution needs it before the prototype, the Designer writes a storyboard of about fifteen steps in section 3.2 (`ideate/storyboard.md`).
16. **Just enough prototype** — *Supplement.* Build in the design folder, following the chosen solution, real enough for honest reactions (`prototype/fake-it.md`): made quickly and thrown away after, while the surface the tester sees appears real. Subagents can build the parts while one session stitches them together; do a trial run against the solution and the design questions before testing.
    *Decide on the spot:* how real the prototype must be when the product has no screen — a document, a service, a process; agree it with the Product Owner.
17. **Role-card test** — *Author's practice.* Test with role cards, each a fresh subagent given only its card, the prototype, and the tasks; the Product Owner tests too. The Designer runs the Five-Act Interview (`test/interview.md`); a grid of reactions is working material; chapter 5 keeps who tested, what showed up, and the answer to each design question. The book tests five customers; here, test every role card the design touches, and add runs while the patterns are unclear.

## Closing

18. **Close as a Review** — *Author's practice.* A design closes when its questions are answered or the Product Owner stops it. Rewrite the log as one Review document, rename it `design-<suffix>.md`, and move it to `scrum/documents/`. Delete the prototypes and other files; git keeps them. Handle the design's branch as `../scrum-kernel/conventions/sprint-log.md`, convention 20, says: merge it, then delete it. Refresh the product log.
    *Supplement:* the Review holds the challenge and the design questions, the chosen solution, each question's test conclusion, where the conclusions flowed back, and the commit that holds the prototype.
19. **Retro as in a Sprint** — *Author's practice.* No Retro chapter; lessons are written as in `../scrum-kernel/conventions/sprint-log.md`, convention 19.

## Resuming

20. **Resume from the header** — *Author's practice.* Keep the header's Now line current: the stage, and the next step. A session that picks up the design reads it first. Before a session ends or its context is shortened, write the half-finished work into the chapter it belongs to, update the Now line, and commit.

## What stays fixed

21. **Goal fixed, plan flexible** — *Author's practice.* The design goal is sharpened during Empathize; once set, only the Product Owner changes it. The questions, the map, and the solution may change with what the work shows; write what changed and why in the chapter it belongs to (`../scrum-kernel/overview.md`, convention 16).
