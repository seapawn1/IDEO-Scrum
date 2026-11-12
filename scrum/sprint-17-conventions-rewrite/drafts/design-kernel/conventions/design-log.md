# Design Log Conventions

> Working conventions: reference, not law — follow what fits, override what doesn't, note why. Source labels and the rest: `../scrum-kernel/overview.md`, convention 15. A convention with no label is the author's practice.

The design log template is `design-backlog-template.md` in this folder. Paths here are relative to the design-kernel skill folder; the stages, the book's excerpts, and the methods are listed in this skill's `SKILL.md`. Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — these conventions say how a solo + AI team does that step, and they apply.

```mermaid
flowchart TD
    A["Opening<br/>conventions 1–5"] --> B["Empathize<br/>conventions 6–7"]
    B -- "PO decides" --> C["Define<br/>convention 8"]
    C -- "PO decides" --> D["Ideate: diverge<br/>conventions 9–10"]
    D --> E["Ideate: converge<br/>conventions 11–15"]
    E -- "PO decides" --> F["Prototype<br/>convention 16"]
    F -- "PO decides" --> G["Test<br/>conventions 17–18"]
    G -- "PO decides" --> H["Ending<br/>convention 19"]
    G -. "or back to the stage whose answer was wrong" .-> B
```

**The three loops.** Empathize and Define: a person puts in, the AI puts out. Diverge and converge: the AI does the work, a person picks the solution. Prototype and Test: the AI can run them on its own — the Product Owner may hand the decisions between them to the Scrum Master (`../scrum-kernel/overview.md`, convention 12), so the two stages run through without waiting.

Conventions 20–27 hold at every step; see Throughout, below. At each "PO decides" the Product Owner decides, as convention 26 says.

## Opening

1. **Open a design for a question with no ready answer** — When a question asks what people want or what counts as good, settle first whether it needs a design sprint or the five modes on the spot (`../ideo-kernel/conventions/design-sprint-or-five-modes.md`, convention 1); when it needs the sprint, open a design and start with Empathize, not with solutions. A blank page is a case of this: see `../scrum-kernel/conventions/product-log.md`, convention 2.
2. **Hard point, not the whole item** — From a Sprint, take out only the hard point that needs design; the rest of the Sprint goes on.
3. **Who** — The Designer is accountable for the design, and the Scrum Master facilitates and records; what the Product Owner decides is listed in convention 21. A design often needs only the Designer; whether to add a Scrum Master is the Product Owner's call. When one session plays both the Designer and the Scrum Master, write the same name in both fields of the header.
4. **Branch** — A design opens its own branch when it opens; the on-the-spot decision is only its base — the Sprint branch or `main`. Do not name it `<sprint-branch>/<name>`: git cannot hold both `a` and `a/b` as branch names.
5. **Open a design** — Pick a suffix that says what the design is about, with no number; create `scrum/design-<suffix>/`; copy the template into it as `DesignBacklog.md`; fill in the header: where the design came from, the branch (convention 4), the Product Owner, the Designer, the Scrum Master, and the Now line (convention 24). The folder holds the log, the prototypes, and the working material — sketches, gathered ideas, a grid of reactions; prototypes and working material never go into an Increment.

## Stages

The conventions under Stages cover only what differs from the book or adds what it leaves out; for everything else, follow the excerpts.

### Empathize

6. **Start from the people** — Start Empathize with the people concerned. When the Product Owner is the person concerned, ask first for concrete experiences — what happened, what they did, what they said — and only then ask for the Product Owner's call on what it means; otherwise start with users the Product Owner can bring. Documents and role cards come after. Write each finding where it belongs — in the challenge, the design goal, or the design questions — with its source, and say whether it is first-hand (what a person said or did) or second-hand (a record made for another purpose, or a role card's reading). Write the design goal as a vision: why we are doing this, and where we want to be — not how; a sentence that tells how belongs to Ideate.
7. **Experts when needed** — Once you have heard the people concerned (convention 6), write the challenge, the design goal, and the design questions; ask experts and do research only when these are still unclear. The experts are the Product Owner, in the conversation, and the role cards (`../scrum-kernel/overview.md`, convention 7), each played by a fresh subagent. Before asking experts, draft a rough map (`steps/2-1-make-a-map.md`); the log keeps what changed, not each interview. After asking the experts or doing research, refine the challenge, the design goal, the design questions, and above all the map once more: fill the gaps and redraw the map.

### Define

8. **Map and questions in the log** — Draw the map as a Mermaid `flowchart TD`, actors at the top and the ending at the bottom, and keep it rough: only what happens now — five or six boxes and one loop. Branches, exceptions, and solutions belong to the Ideate solution and storyboard, not in the map; if someone who never learned design cannot read it at a glance, a solution has been put inside. Write the How Might We questions against the map, with the challenge, the design goal, and the design questions of chapter 1 beside it. The map, together with the challenge, the design goal, and the design questions, is the point of view here; do not write a separate one. The Product Owner picks the How Might We questions that matter — no dot voting. There is no target step while the design runs; a design that began from a blank page picks its target when it ends (convention 19). If the map holds more than one design's worth of work, split the rest out into another design or into items (`steps/2-3-pick-a-target.md` shows how the book narrows a map).

### Ideate: diverge

9. **Lightning Demos** — Have subagents search for existing ideas in parallel; give each one a different part of the problem, or draw first and look afterwards. Keep the list as working material, not part of the log.
10. **Diverge before you converge** — When you brief each subagent that sketches a solution (convention 12), have it diverge first — use at least two methods, at least one of them from the ideo-kernel's Ideate methods, as `SKILL.md` requires (the first steps of the book's sketch, `steps/3-2-sketch.md` — notes, ideas, Crazy 8s — may be used alongside), go for quantity, and hold judgment back — and only then converge into its own sketch. The ideas are working material; they do not go into the log.

### Ideate: converge

11. **Isolated solutions** — Have several fresh subagents, each starting from its brief alone and unable to see one another, each diverge first (convention 10) and then produce one complete solution sketch, in words or Mermaid, from chapters 1 and 2, the gathered ideas, `steps/3-2-sketch.md`, and the ideo-kernel Ideate methods. The brief gives chapters 1 and 2 and the gathered ideas, and nothing about the current state; tell each subagent not to read the project's files. Some tools bring the project's instructions to every subagent automatically; when that happens, note it in the design log.
    *Decide on the spot:* how many subagents to run, and on which model.
12. **While they sketch, talk with the Product Owner** — While the subagents sketch, the main thread asks the Product Owner whether they have ideas and talks them over, without rushing to converge. If the Product Owner has no idea, the main thread sketches one direction on their behalf, as one of the lines. All the lines — the subagents' sketches, the Product Owner's ideas, the main thread's own — come back to the main thread, are merged, and only then does it converge (convention 13).
13. **Choosing is the key step** — Run the book's decision (`steps/3-3-decide.md`) in the conversation, led by the Scrum Master; have role-card Stakeholders give a straw poll if the Product Owner wants one. The Product Owner makes the final call, with no search for consensus. Put only the chosen solution into section 3.1.
14. **Combine or rumble** — Combine winners that fit together; when two conflict, prototype both and let the test decide (`steps/3-4-rumble.md`). The Product Owner decides which.
15. **Storyboard** — Write a storyboard of about fifteen steps in section 3.2 (`steps/3-5-storyboard.md`) only when the solution needs one before the prototype; the Designer writes it.

### Prototype

16. **Just enough prototype** — *Supplement.* Build in the design folder, following the chosen solution, real enough for honest reactions (`steps/4-1-fake-it.md`): made quickly and thrown away after, while the surface the tester sees appears real. Subagents can build the parts while one session stitches them together; do a trial run against the solution and the design questions before testing, and write what it found in chapter 5. List each part of the prototype in chapter 4 with the design question it tests.
    *Decide on the spot:* how real the prototype must be when the product has no screen — a document, a service, a process; agree it with the Product Owner.

### Test

17. **Role-card test** — Test with role cards, each a fresh subagent given only its card, the prototype, and the tasks; the Product Owner tests too. The Designer runs the Five-Act Interview (`steps/5-2-interview.md`); a grid of reactions is working material; chapter 5 keeps who tested, what showed up, and the answer to each design question. The book tests five customers; here, test every role card the design touches, and add runs while the patterns are unclear.
18. **Write the criteria before the test** — Before testing, write down in chapter 5 what would count as a yes, a no, or a not yet for each design question, and what role cards cannot show: they are subagents reading a card, not real people.

## Ending

19. **When the design ends** — End the design when its questions are answered or the Product Owner stops it. Write the conclusions into the product log as `../scrum-kernel/conventions/product-log.md`, convention 2, says, and pass them on to the Sprint that asked for the design; when the design began from a blank page, pick the target (`steps/2-3-pick-a-target.md`) — the steps of the map to build — and split it into items, and let the Product Owner order which come first. Delete the prototypes and the other files in the design folder, but not the log; git keeps them. Handle the design's branch as `../sprint-kernel/conventions/sprint-log.md`, convention 19, says: merge it, then delete it. A design has no Review or Retro of its own: the first Sprint Review after the design ends archives its log (`../sprint-kernel/conventions/sprint-log.md`, convention 17), and the lessons from the design go into that Sprint's Retrospective. At the end of chapter 5, next to the Product Owner's decision, write a line or two on what the design taught about how to work, to keep for that Retrospective.

## Throughout

20. **IDEO in every stage** — Run the design sprint as the IDEO five-stage method: in every stage, take the methodology from the IDEO mode the stage maps to, as `SKILL.md` requires.
21. **Ask the PO** — Ask the Product Owner whenever you are unsure (`../scrum-kernel/overview.md`, convention 10), and in any case to: decide at the end of each stage, and after the test whether to end the design or go back (convention 26); set or change the design goal (convention 25); pick the How Might We questions that matter (convention 8); choose the solution and decide between combining and a rumble (conventions 13–14); agree how real the prototype must be (convention 16); and decide that the design ends (convention 19).
22. **Five chapters, not five days** — Write one chapter per stage — Empathize, Define, Ideate, Prototype, Test — not the book's Monday to Friday, and no notes section. Each chapter records what its stage produced, not the steps taken.
23. **Renamed terms** — See the first paragraph of `SKILL.md`.
24. **Resume from the header** — Keep the header's Now line current: the stage, and the next step. A session that picks up the design reads it first. Before a session ends or its context is shortened, write the half-finished work into the chapter it belongs to, update the Now line, and commit.
25. **Goal fixed, plan flexible** — Sharpen the design goal during Empathize; once it is set, only the Product Owner changes it. The questions, the map, and the solution may change with what the work shows; write what changed and why in the chapter it belongs to (`../scrum-kernel/overview.md`, convention 17).
26. **Gates between stages** — At the end of each stage, check the log against the gate below; then the Product Owner decides (`../scrum-kernel/overview.md`, *Product Owner decides between stages*). After the Test, the decision is to end the design or to go back to the stage whose answer was wrong.

    | Stage | The log holds | The check |
    | --- | --- | --- |
    | Empathize | the challenge, the design goal, and the design questions, with the source of each finding | The findings come from the people concerned — what they did, what they said, where the two differ — not from a pile of facts |
    | Define | the map and the How Might We questions the Product Owner picked | The How Might We questions were written against the map and the challenge, the goal, and the questions of chapter 1 |
    | Ideate | the chosen solution, and the storyboard if one was written | Each sketch diverged before it converged, and the sketches differ in approach, not only in detail |
    | Prototype | the parts of the prototype, each with the design question it tests | It is rough, quick, and thrown away after: built to learn, not to deliver |
    | Test | the criteria written beforehand, what the trial run found, who tested and what showed up, and an answer to each design question with where it flows back | The answers come from real reactions, and "we were wrong" counts as an answer |

    At each gate ask: would someone who never learned design have produced the same thing? If so, the stage missed its focus.
27. **A small design is still a design** — A small question gets the five modes on the spot (`../ideo-kernel/conventions/design-sprint-or-five-modes.md`, convention 1), not a design. When the Product Owner opens a design that is small — about one session of work — still keep the log, shrink each stage to a line or two, and still have the Product Owner decide at the end of each stage. Skip no stage, least of all Empathize and divergence (convention 10).
