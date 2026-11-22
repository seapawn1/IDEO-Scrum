# The stages of a Sprint: the details

> Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland), marked where they appear.
> License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland).

The detail behind the Sprint lines that point here: opening, the How, the go-ahead, checkpoints, and the Test. Read it when you plan, build or test a Sprint. The list lines that point here are `sprint-folder`, `how-is-a-plan`, `go-ahead`, `checkpoints`, `outline-first`, `full-text-review`, `reviewer-required` and `record-the-tests`. The text is the old rules word for word, cut into bullets; the old pointers to convention numbers became handles.

## Opening a Sprint (`sprint-folder`)

- Give each Sprint one branch, with a separate working copy if wanted, and one folder, `scrum/sprint-NN-<suffix>/`: a two-digit number — the previous Sprint's plus one, starting at 01 — and a suffix saying what the Sprint is about.
- The folder's name is also the branch's name, and the tag's at close.

## How: a plan, not steps (`how-is-a-plan`, `no-steps`)

- The Developer writes chapter 3 as a plan for making the selected items: the work items in order, each done within one session, each with its output and how to tell it is done; the key choices and their reasons; the known risks and open points.
- Write it to the level of approach, not steps: no step-by-step instructions, no file contents, no polishing of the plan; if you can write the steps, do the work.
- It is not the solution a design chose: if a design gave a solution, the plan is how to build it.
- The Scrum Guide's measure, "decomposing Product Backlog items into smaller work items of one day or less", becomes one session here.
- The Scrum Master and the Product Owner check the plan.
- This departs from the Scrum Guide; the reason is in `details/departures.md`.

## The go-ahead (`go-ahead`, `review-handover`)

- Start building only after the Product Owner's go-ahead; approving a plan is not a go-ahead.
- Write it as the last line of chapter 3, with the date and how far it reaches: commit, merge, tag, release, push.
- The Product Owner may hand the review of the How, of new structures, and of full texts to the Scrum Master; write the handover in the log.
- The right to review the How is not the right to give the go-ahead (`stage-gates`).

## Checkpoints (`checkpoints`)

- Stop and check the work against the Sprint Goal at the end of each stage (`stage-gates`), whenever the AI is stuck, and whenever the Product Owner asks how things stand.
- Stuck means one of these: waiting for a decision or a piece of information only the Product Owner can give, a block from outside the team, the same approach tried twice and failed, or the current How no longer showing how to reach the Sprint Goal; anything else is an adjustment inside the plan.
- This departs from the Scrum Guide's Daily Scrum; the reason is in `details/departures.md`.

## Tests: criteria first (`tests-criteria-first`, `check-script-misses`)

- In section 2.2, set the method and pass lines: what needs fresh evidence, what earlier evidence is expected to still hold, and which outcome signals must be shown in this Test.
- Commit the method and pass lines before running the Test; do not change them after seeing results.
- Check a script’s wrong calls one by one and write down why.

## Outline first, then the full text (`outline-first`, `full-text-review`)

- Before writing a new lasting document or a new template, show its outline to whoever reviews it: the headings at every level, each with one line on what its part will hold. For a new template, the outline is its chapter list.
- Write the full text once the reviewer agrees.
- Put a new lasting document's full text — word for word, not an outline — where the reviewer can annotate it, with the problems you found and a recommendation for each; change the source files only after approval.
- The version on disk wins: read before you overwrite.

## A reviewer is required (`reviewer-required`)

- Have someone other than the builder review: the Scrum Master by default, or a Stakeholder or a fresh subagent when the Product Owner names one.
- A Stakeholder named as reviewer checks the work item by item against the Definition of Done and the acceptance criteria.
- When the Scrum Master also built the work, a fresh subagent reviews, checking only whether the work was done right.
- When the Developer only shares the Scrum Master's context, the Scrum Master still reviews: a shared context does not make it the builder.
- Brief a review subagent with the task, the project's rules, and the decisions already issued.
- The Scrum Master may send a subagent to do the review or to read a long diff, and still owns the conclusion.
- This departs from the Scrum Guide; the reason is in `details/departures.md`.

## Record the tests (`record-the-tests`)

- In chapter 5, keep the Developer’s tests, the independent check, and any required Product Owner acceptance.
- Show the result of every Output Done standard and item acceptance criterion: link the new evidence or cite the old evidence and why it still holds. When a stated condition did not arise, record it and why it did not apply. An applicable standard without valid evidence does not pass, even if it was not a focus.
- Record the result of each Outcome Done signal separately from Output Done. An outcome required for this Test by the Sprint Goal, an item’s outcome or acceptance criteria, or another pass line set beforehand blocks a Test pass if unmet or unproven. Otherwise record a signal without evidence as not yet observed; report contrary evidence as not met and explain its effect. Do not claim the full DoD has passed on those signals.
- The Increment’s quality can pass on its own evidence; the Sprint Test passes only when all its required checks, review, and acceptance pass.
- Fix a problem within Test and test again; a return to an earlier stage needs a decision under `stage-gates`.

## Open points for the Product Owner

- None. Convention numbers became handles; the "see the Departures section" pointers became a pointer to the departures long file.
