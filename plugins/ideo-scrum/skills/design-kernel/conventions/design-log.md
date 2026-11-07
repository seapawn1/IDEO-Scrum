# Design Log Conventions (v1)

> These are working conventions, v1 — the author's reading of Scrum and design thinking for solo + AI teams. They are less precise than the official guides. Use them as reference: follow what fits, override what doesn't, and note why. Where a convention departs from the official guide on purpose, it says so and gives the reason.

Each convention has a short name, so it can be referred to in conversation, and one source label:

- **Author's practice** — how the author works.
- **Supplement** — inferred by the author's assistant; not yet confirmed in practice.
- **Decide on the spot** — no fixed rule; decide when it comes up.

The design log template is `design-backlog-template.md` in this folder. The book's techniques are in this skill's stage folders; the methods are in the ideo-kernel skill.

## Where a design sits

1. **Design beside the Sprint** — *Author's practice.* Below the product backlog sit two peer modules: Sprints and designs. A Sprint is the Developer's and delivers an Increment; a design is the Designer's and delivers a prototype and conclusions. Both answer to the product backlog. A design is opened as its own module, not inside a Sprint.
   *Departs from the Scrum Guide on purpose.* The Scrum Guide says: "All the work necessary to achieve the Product Goal, including Sprint Planning, Daily Scrums, Sprint Review, and Sprint Retrospective, happen within Sprints." Reason: a design's output is a prototype and conclusions, not an Increment; a design lives as long as its design questions are open, which may span several Sprints; and the Designer and the Developer are peers, both accountable to the product.
2. **Hard point, not the whole item** — *Author's practice.* Open a design when a product backlog item needs design, or when Sprint refinement hits a hard point. From a Sprint, take out only the hard point; the rest of the Sprint goes on.
3. **Who** — *Author's practice.* The Designer is accountable for the design. The Scrum Master facilitates and records. The Product Owner decides the design goal, the chosen solution, and when the design is done.
4. **Where** — *Author's practice.* A design lives in `scrum/design-<suffix>/` — no number; the suffix says what the design is about. The folder holds `DesignBacklog.md` and the prototypes. Prototypes never go into an Increment.
5. **Branch** — *Decide on the spot.* Whether the design branches from the Sprint branch or from `main` is decided when the design opens. Do not name the branch `<sprint-branch>/<name>`: git cannot hold both `a` and `a/b` as branch names.
6. **Ask the PO** — *Author's practice.* When anyone working on the design is unsure, they ask the Product Owner to decide — unless the Product Owner has said that a kind of question goes to someone else.

## How the log is written

7. **Five chapters, not five days** — *Author's practice.* The log has one chapter per stage: Empathize, Define, Ideate, Prototype, Test. It does not follow the book's Monday-to-Friday schedule, and it has no separate notes section: the work is written straight into the chapter it belongs to.
8. **IDEO always in play** — *Author's practice.* The book's techniques in this skill are here so the design sprint runs as one piece; they do not limit the methods. In any stage, use any ideo-kernel method whenever the work needs it.
9. **Renamed terms** — *Author's practice.* The book's *long-term goal* is the **design goal**; its *sprint questions* are the **design questions**; its *Decider* is the **Product Owner**; its *Facilitator* is the **Scrum Master**.

## How each stage runs with AI

| Stage | The book | Here |
| --- | --- | --- |
| Empathize | Interviews with the team, the company, and outsiders, one at a time | Convention 10 |
| Define | Map on a whiteboard; How Might We sticky notes; dot vote; the Decider picks a target | Convention 11 |
| Ideate | Lightning Demos; each person sketches alone; Sticky Decision; Rumble; storyboard | Conventions 12–16 |
| Prototype | A façade built in one day by Makers, a Stitcher, a Writer, an Asset Collector | Convention 17 |
| Test | Five customers, the Five-Act Interview, the team watching together | Convention 18 |

10. **Experts at hand** — *Author's practice.* Write the challenge, the design goal, and the design questions first. Then ask the experts: the Product Owner, in the conversation, and the Stakeholders written as role cards in the product backlog, each summoned as a fresh subagent that is given its card. Research fills the rest. Fix the goal, the questions, and the map as you learn.
11. **Map and questions in the log** — *Author's practice.* Draw the map in the log as a Mermaid diagram (`flowchart TD`). List the How Might We questions in the log and group them by theme; the Product Owner picks the ones that matter — no dot voting. A target is optional: pick one when the challenge is too wide for one design.
12. **Lightning Demos** — *Author's practice.* Before anyone sketches, look for existing solutions — other products, other domains, earlier attempts in the project — and list ten to twenty ideas worth remixing in chapter 3. Subagents can search in parallel.
13. **Isolated solutions** — *Author's practice.* Several fresh subagents, unable to see one another, each produce one complete solution — the book's "work alone together". Give each one chapters 1 and 2 of the log, the Lightning Demos list, and `ideate/sketch.md`, and ask for a solution sketch: a step-by-step storyboard in words (Mermaid allowed), self-explanatory, with a catchy title and without the author's name.
14. **Choosing is the key step** — *Author's practice.* Run the book's Sticky Decision (`ideate/decide.md`) in the log. Lay all the solutions side by side. The Scrum Master marks the standout parts and runs a speed critique — narrate each solution, name its standout ideas, list concerns — before hearing from whoever wrote it. If the Product Owner wants input, ask the role-card Stakeholders for a straw poll. Then the Product Owner makes the final call. Do not seek consensus. Solutions not chosen are "maybe-later", not failures.
15. **Combine or rumble** — *Author's practice.* When the winning solutions fit together, combine them into one. When two conflict, prototype both and let the test decide (`ideate/rumble.md`). The Product Owner decides which.
16. **Storyboard** — *Author's practice.* The Designer strings the chosen solution into a storyboard of about fifteen steps in the log, starting from an opening scene (`ideate/storyboard.md`). Fill gaps from the maybe-later solutions rather than inventing new ones; the Product Owner decides what stays.
17. **Just enough prototype** — *Supplement.* Build in the design folder, following the storyboard, just real enough for honest reactions (`prototype/fake-it.md`). Subagents can take the Maker parts while one session stitches the whole together; do a trial run against the storyboard and the design questions before testing.
18. **Role-card test** — *Author's practice.* Test with the Stakeholders from the role cards, each a fresh subagent given only its card, the prototype, and the tasks; the Product Owner tests too. The Designer interviews with the Five-Act Interview (`test/interview.md`). Record reactions in a grid — testers by storyboard steps — then look for patterns and answer each design question in chapter 5 (`test/learn.md`).
    *Supplement:* the book's "five is the magic number" counts customers. With role cards, test every card the design touches, and add runs while the patterns are still unclear.

## Closing

19. **Close as a Review** — *Author's practice.* A design closes when its design questions are answered or the Product Owner stops it. Rewrite the whole design log as one Review document, replacing the log; rename it `design-<suffix>.md` and move it to `docs/`. Delete the prototypes and the other files in the folder — git keeps them. Then refresh the product backlog: the conclusions flow back to the product backlog items and to the Sprint that asked for the design.
    *Supplement:* the Review document holds the challenge and the design questions, the chosen solution, the test conclusion for each design question, where the conclusions flowed back, and the commit that still holds the prototype.
20. **Retro as in a Sprint** — *Author's practice.* The design log has no Retro chapter. Lessons go to the project's memory or its CLAUDE.md, written as principles — what broke, why, and the rule that follows — not as stories.
