# Roles and routing of work

PENDING SPRINT 27: this is the text as it stands today; Sprint 27 changes the role table (a Supporter role), the routing of questions and who writes the board, and this file is rewritten when 27 is merged. Read it when you start as a role, split work between sessions, or are unsure whom to ask. The list lines that point here are `role-entry`, `who-gets-which-work` and `ask-the-po`.

## The roles (`role-entry`)

On a Claude Code role command, invoke the kernels in the order shown before doing any role work.

| Role | Home turf | Accountable for | Claude Code entry kernels, in order |
| --- | --- | --- | --- |
| Product Owner | The product log and its handoffs | Value direction; the Product Goal and Sprint Goals; which items enter a Sprint; the go-ahead; the items, decided with the Scrum Master; stage results and permissions to start or return (`stage-gates`) | — (a person) |
| Scrum Master | Sprint logs and design logs | Facilitating Planning and refinement; recording; tracking; reviewing the How and the Increment; serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded | ideo → scrum → sprint → design |
| Developer | The Sprint | The sprint log, the How, the Increment; the last check that nothing in refinement is unclear | ideo → scrum → sprint |
| Designer | The design | Ideas, prototypes, and tests for a design, from Ideate on (the Product Owner and the Scrum Master settle its research and definition); conclusions back to the product log and the Sprint that asked | ideo → scrum → design |
| Stakeholder | An outside view, or standing non-source chores | Looking as one row of the product log's stakeholder table; a PO assistant organizes logs, summarizes progress, relays settled work and maintains the board, but does not rank, decide, review or edit plugin files | ideo → scrum |

- In Claude Code, use the Skill tool one at a time, wait for success, and skip only calls already successful in this conversation. Stop and report a failed load rather than substituting a file read.
- In DSH, native role entries instead preload ideo and scrum in order, then load sprint and design as needed for the work.
- Subagents a role dispatches load the ideo-kernel and scrum-kernel skills too.
- The Product Owner, the Scrum Master, and the Developer keep the sprint log together; without a Developer, the Product Owner and the Scrum Master run the Sprint alone.

## Who gets which work (`who-gets-which-work`)

- Reviewing the work goes to the Scrum Master by default (`reviewer-required`); when the Developer works in another session or tool, `developer-elsewhere` says how the two work together.
- Long-running upkeep — the board, summaries, tracking — goes to a standing Stakeholder session with a working identity the project writes down, such as PO assistant. That assistant relays only what the Product Owner or Scrum Master already decided; scope or item changes and go-aheads go through the Scrum Master, who chooses the receiving session. It does not rank, decide, review or edit plugin files; an independent outside view still comes from a fresh subagent.
- A small edit to one or two files the Scrum Master makes itself.
- Building goes to a new Developer session when a paragraph can brief it, or to a Developer that shares the Scrum Master's context when the work needs much of the discussion; such a Developer cannot review its own work.

## What goes to the Product Owner (`ask-the-po`)

Ask the Product Owner whenever you are unsure, unless the Product Owner has said that a kind of question goes to someone else. The old text also listed what goes to the Product Owner in any case; the Sprint list and the design list are kept here word for word in meaning, as bullets (they were two rules, now one under `ask-the-po`).

**In a Sprint:**

- set the Sprint Goal (`sprint-goal`);
- select the items (`items-with-sm`, `select-items`);
- say when refinement is over (`refinement`);
- give the go-ahead (`go-ahead`);
- decide at the end of each stage (`stage-gates`);
- renegotiate the acceptance criteria (`goal-fixed`);
- decide whether new work enters the Sprint, and renegotiate the scope (`new-work-registered`);
- give formal acceptance, when it is written (`acceptance-when-written`);
- consent to outward actions such as a push (`outward-needs-po`);
- cancel a Sprint whose goal can no longer be met (`po-owns-commitments`).

**In a design:**

- settle each stage result and authorize entry or return, including how this round of Ideate will diverge (`stage-gates`, `ideate-arrangement`);
- set or change the design goal (`goal-fixed`);
- pick the How Might We questions that matter (`design-stages`);
- choose the solution and decide between combining and a rumble (`choose-with-po`, `combine-or-rumble`);
- agree how real the prototype must be (`design-stages`);
- decide that the design ends (`design-ends`);
- explicitly permit git actions (commit, merge, branch deletion, push) before they run (`outward-needs-po`, `log-is-the-handoff`, `stage-gates`).

## Open points for the Product Owner

- PENDING SPRINT 27: the three-tier routing of questions (decide and log it yourself; process questions to the Scrum Master; what only the Product Owner decides goes to the Supporter, who collects it for the Product Owner), a Product Owner opinion relayed by the Supporter counting as the Product Owner's (with exceptions), and the board written by the Supporter. The lists above become the third tier; "git actions" is stricter here than in the old rules (the old rules only ask that a commit stay inside the go-ahead's reach).
