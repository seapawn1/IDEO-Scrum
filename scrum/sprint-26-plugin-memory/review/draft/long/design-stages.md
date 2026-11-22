# The stages of a design: the details

The detail behind the design lines that point here, stage by stage. Read it when you run a design sprint, together with the design-kernel skill's step files (`steps/…` below are that skill's). The list lines that point here are `design-stages`. The text is the old rules word for word, cut into bullets; the old pointers to convention numbers became handles.

## How these rules sit beside the book

- The design log template is `design-backlog-template.md`, in the design-kernel skill's `conventions/` folder; the stages, the book's excerpts, and the methods are listed in that skill's `SKILL.md`.
- Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — these rules say how a solo + AI team does that step, and they apply.
- The rules under the stages cover only what differs from the book or adds what it leaves out; for everything else, follow the excerpts.

## The three loops

- **Empathize and Define:** the Product Owner and the Scrum Master settle the research and definition together; the Scrum Master records it, and the Designer takes over when Ideate is authorized (`design-roles`).
- **Diverge and converge:** the Product Owner first settles how to open up ideas; the AI can do the work, and a person picks the solution.
- **Prototype and Test:** the AI can do the work once each stage is authorized.
- Any stage decision handed to the Scrum Master still has to be within the written handover and recorded (`stage-gates`).

## Empathize: start from the people

- Start Empathize with the people concerned. When the Product Owner is the person concerned, ask first for concrete experiences — what happened, what they did, what they said — and only then ask for the Product Owner's call on what it means; otherwise start with users the Product Owner can bring. Documents and role cards come after.
- Write each finding where it belongs — in the challenge, the design goal, or the design questions — with its source, and say whether it is first-hand (what a person said or did) or second-hand (a record made for another purpose, or a role card's reading).
- Write the design goal as a vision: why we are doing this, and where we want to be — not how; a sentence that tells how belongs to Ideate. Keep the goal's one-row commitment table in section 1.2 (`commitment-table`).
- Once you have heard the people concerned, write the challenge, the design goal, and the design questions; ask experts and do research only when these are still unclear. The experts are the Product Owner, in the conversation, and the role cards (`names`), each played by a fresh subagent.
- Before asking experts, draft a rough map (`design-kernel/steps/2-1-make-a-map.md`); the log keeps what changed, not each interview.
- After asking the experts or doing research, refine the challenge, the design goal, the design questions, and above all the map once more: fill the gaps and redraw the map.

## Define: map and questions in the log

- Draw the map as a Mermaid `flowchart TD`, actors at the top and the ending at the bottom, and keep it rough — five or six boxes and one loop.
- Draw the experience we want to reach, not what happens now: the way things are today, and where it hurts, go in chapter 1 with their sources (see Empathize above). *Departs from the book:* the book's step maps the situation as it is.
- Branches, exceptions, and solutions belong to the Ideate solution and storyboard, not in the map; if someone who never learned design cannot read it at a glance, a solution has been put inside.
- Write the How Might We questions against the map, with the challenge, the design goal, and the design questions of chapter 1 beside it. The map, together with the challenge, the design goal, and the design questions, is the point of view here; do not write a separate one.
- The Product Owner picks the How Might We questions that matter — no dot voting.
- There is no target step while the design runs; a design that began from a blank page picks its target when it ends (`design-conclusions`).
- If the map holds more than one design's worth of work, split the rest out into another design or into items (`design-kernel/steps/2-3-pick-a-target.md` shows how the book narrows a map).

## Ideate: Lightning Demos (optional)

When existing ideas would help, have subagents search for them in parallel; keep the list as working material, not part of the log. If subagents sketch (see Isolated solutions below), the list is split among them, so that each starts from different ideas.

## Ideate: isolated solutions (optional)

- When several solutions that differ in approach are wanted, have several fresh subagents, unable to see one another, each sketch one complete solution in words or Mermaid.
- Give each its own materials — chapters 1 and 2 and its own part of the gathered ideas, or none until it has drawn — together with `design-kernel/steps/3-2-sketch.md` and the ideo-kernel Ideate methods, and give any summary apart too: one summary handed to all of them makes the sketches converge on one idea (in one design, two subagents given the same summary of reference examples both drew a subway map).
- Beyond chapters 1 and 2, give it nothing about how things are solved today — no current design, rules, or code — and tell it not to read the project's files. Each diverges first (`diverge-first`).
- Some tools hand the project's instructions to every subagent anyway; when that happens, note it in the design log.
- Without subagents, the main thread and the Product Owner sketch together (`talk-with-po`).
- *Decide on the spot:* whether to use subagents at all, how many, and on which model, within how the Product Owner chose to run this round (`ideate-arrangement`).

## Prototype: just enough

- *Supplement.* Build in the design folder, following the chosen solution, real enough for honest reactions (`design-kernel/steps/4-1-fake-it.md`): made quickly for learning, not for production, while the surface the tester sees appears real.
- Keep it as design evidence under `design-ends`; keeping it does not make it an Increment.
- Subagents can build the parts while one session stitches them together; do a trial run against the solution and the design questions before testing, and write what it found in chapter 5. List each part of the prototype in chapter 4 with the design question it tests.
- *Decide on the spot:* how real the prototype must be when the product has no screen — a document, a service, a process; agree it with the Product Owner.

## Test: role cards

- Test with role cards, each a fresh subagent given only its card, the prototype, and the tasks; the Product Owner tests too.
- The Designer runs the Five-Act Interview (`design-kernel/steps/5-2-interview.md`); a grid of reactions is working material; chapter 5 keeps who tested, what showed up, and the answer to each design question.
- The book tests five customers; here, test with the role cards the prototype is about — those who would meet it — and leave out the rest, and add runs while the patterns are unclear.
- When the thing is for the Product Owner alone, the Product Owner testing it is enough: do not make up a role card.

## Open points for the Product Owner

- None. Convention numbers became handles; the one *Departs from the book* mark (the map draws the experience we want, not today's) is kept where it was.
