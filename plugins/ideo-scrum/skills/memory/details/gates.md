# Stage gates: the Product Owner decides between stages

Read this file before you start a Sprint stage, return to one, or record a stage decision. The list lines that point here are `stage-gates` and `read-the-goal`. Here *stage* permission means the Product Owner's permission to enter or return to a stage (not a tool permission), and the Product Owner's own words relayed by the Supporter count as theirs.

## The rule (`stage-gates`)

- The Product Owner settles each stage’s result.
- Before starting or returning to a stage of a Sprint, wait for explicit stage permission (not a tool permission) for that stage and scope. Approving a result is not stage permission to move on, though one message can say both clearly.
- While waiting, record the result or why a return is needed, but do not start or delegate that stage’s work.
- A new session may resume the same stage within its recorded stage permission and scope; earlier stage permission does not carry over to a return.
- The Scrum Master acts for the Product Owner only within a written handover covering the particular decision; handing over a review or a choice inside a stage does not hand over a stage transition.
- The Product Owner's own words, relayed by the Supporter on the conditions in `po-word-relayed`, count as theirs.
- Record who decided, the date and basis, and the stage and scope authorized, including the written handover if used. Keep the decision at the end of its stage chapter; if stage permission arrives later, add that dated decision without replacing the earlier one. Record first entry when opening the log.
- These are stage decisions, not reviews, formal acceptance, or approval of each step.
- A stage permission does not by itself authorize a commit, merge or push: the go-ahead says how far git permission reaches (`go-ahead`), and push, release and other outward actions need the Product Owner's consent (`outward-needs-po`).
- Standalone runs of the IDEO five modes (`IdeoBacklog.md`) have no Product Owner stage gates between modes (`open-ideo-log`), though conclusions still go to the Product Owner to decide and git/outward actions still require consent.

## In a Sprint (`read-the-goal`)

- Follow the rule above, at entry and on return. Record explicit permission to start Why when opening; if no Sprint Goal is set yet, do not record a placeholder as a commitment. Closing is a separate decision from the stage transitions.
- The Product Owner sets the goal before What, ends refinement before How, authorizes building with the go-ahead (`go-ahead`), authorizes Sprint Test separately from approving the Increment, and after Test decides to close or authorizes a return to the stage that needs work.
- A Developer’s checks while building are not Sprint Test.
- For the decision that sets the goal, put the exact text in the §1.1 table. Before that decision is recorded and before each later stage decision, read the exact Sprint Goal from the table, and the Product Goal too if product direction is at issue. Check the work against what you read. If the required text cannot be read, stop at that gate.
- Keep the exact wording on the dated decision line as a record of the goal at the time, not a source for future decisions.
- Show the text to the Product Owner only when the goal has changed (including when Why sets it), when product direction is at issue, or when they ask.
