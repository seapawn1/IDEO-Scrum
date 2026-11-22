# Stage gates: the Product Owner decides between stages

Read this file before you start a stage, return to one, or record a stage decision, in a Sprint or in a design. The list lines that point here are `stage-gates`, `read-the-goal` and `ideate-arrangement`. Here *stage* permission means the Product Owner's permission to enter or return to a stage (not a tool permission), and the Product Owner's own words relayed by the Supporter count as theirs.

## The rule, for both (`stage-gates`)

- The Product Owner settles each stage’s result.
- Before starting or returning to a stage of a Sprint or a design sprint, wait for explicit stage permission (not a tool permission) for that stage and scope. Approving a result is not stage permission to move on, though one message can say both clearly.
- While waiting, record the result or why a return is needed, but do not start or delegate that stage’s work.
- A new session may resume the same stage within its recorded stage permission and scope; earlier stage permission does not carry over to a return.
- The Scrum Master acts for the Product Owner only within a written handover covering the particular decision; handing over a review or a choice inside a stage does not hand over a stage transition.
- The Product Owner's own words, relayed by the Supporter on the conditions in `po-word-relayed`, count as theirs.
- Record who decided, the date and basis, and the stage and scope authorized, including the written handover if used. Keep the decision at the end of its stage chapter; if stage permission arrives later, add that dated decision without replacing the earlier one. Record first entry when opening the log.
- These are stage decisions, not reviews, formal acceptance, or approval of each step.
- A stage permission does not by itself authorize a commit, merge or push: in a Sprint the go-ahead says how far it reaches (`go-ahead`); in a design the stage or ending decision line records how far git permission reaches; push, release and other outward actions need the Product Owner's consent (`outward-needs-po`).
- The Sprint decisions are below under "In a Sprint"; the design decisions under "In a design".

## In a Sprint (`read-the-goal`)

- Follow the rule above, at entry and on return. Record explicit permission to start Why when opening; if no Sprint Goal is set yet, do not record a placeholder as a commitment. Closing is a separate decision from the stage transitions.
- The Product Owner sets the goal before What, ends refinement before How, authorizes building with the go-ahead (`go-ahead`), authorizes Sprint Test separately from approving the Increment, and after Test decides to close or authorizes a return to the stage that needs work.
- A Developer’s checks while building are not Sprint Test.
- For the decision that sets the goal, put the exact text in the §1.1 table. Before that decision is recorded and before each later stage decision, read the exact Sprint Goal from the table, and the Product Goal too if product direction is at issue. Check the work against what you read. If the required text cannot be read, stop at that gate.
- Keep the exact wording on the dated decision line as a record of the goal at the time, not a source for future decisions.
- Show the text to the Product Owner only when the goal has changed (including when Why sets it), when product direction is at issue, or when they ask.

## In a design (`ideate-arrangement`)

- Wait for explicit permission to enter or return, as the rule above says. Record permission to start Empathize when opening; if there is no design goal yet, do not record a placeholder as a commitment.
- Stage entry or return permission covers only that stage's design work and does not by itself authorize a commit, merge, or push; if git actions are permitted, record how far that permission reaches (for example, commit on the design branch; merge at ending decided separately; no push) on the stage or ending decision line.
- Before starting Ideate, the Product Owner settles how this round will diverge. Until that and entry are clear, do not gather ideas for the round, diverge, sketch, or delegate those tasks. Record the arrangement in chapter 3 before the solution section.
- Choosing a solution is not permission for Prototype, and a trial run is not permission for design Test.
- When the stage first sets a design goal, put its exact text in the §1.2 table. Before recording that decision and before each later stage decision, read the exact design goal from the table — and the Product Goal when product direction is at issue — then check the work against it and the table below. If the required text cannot be read, stop at that gate.
- Keep the exact wording on the dated decision line as a record of the goal at the time. Show the text to the Product Owner only when the goal has changed, when product direction is at issue, or when they ask.
- When a stage shows an earlier answer was wrong, report it and wait for permission to return; after Test the Product Owner decides whether to end the design or authorizes the return.

| Stage | The log holds | The check |
| --- | --- | --- |
| Empathize | the challenge, the design goal, and the design questions, with the source of each finding | The findings come from the people concerned — what they did, what they said, where the two differ — not from a pile of facts |
| Define | the map and the How Might We questions the Product Owner picked | The How Might We questions were written against the map and the challenge, the goal, and the questions of chapter 1 |
| Ideate | the chosen solution, and the storyboard if one was written | Whoever sketched diverged before converging, and when several sketches were drawn, they differ in approach, not only in detail |
| Prototype | the parts of the prototype, each with the design question it tests | It is rough and quick: built to learn, not to deliver |
| Test | the criteria written beforehand, what the trial run found, who tested and what showed up, and an answer to each design question with where it flows back | The answers come from real reactions, and "we were wrong" counts as an answer |

At each gate ask: would someone who never learned design have produced the same thing? If so, the stage missed its focus.
