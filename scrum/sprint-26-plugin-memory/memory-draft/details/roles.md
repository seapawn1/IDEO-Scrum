# Roles and routing of work

> Source: the quotation in *The Product Owner's word, relayed* is from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland); the rest is the plugin author's.
> License: the quotation is CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland); the plugin's own text is MIT.

Who does what, who gets which work, and where each kind of question goes. Read this file when you start as a role, split work between sessions, are unsure whom to ask, or relay or receive the Product Owner's words. The list lines that point here are `role-entry`, `who-gets-which-work`, `ask-the-po` and `po-word-relayed`; `answers-back` and `relay-limits` belong to the same part.

## The roles (`role-entry`)

On a Claude Code role command, invoke the skills in the order shown before doing any role work; the Memory is the last of them.

| Role | Home turf | Accountable for | Claude Code entry skills, in order |
| --- | --- | --- | --- |
| Product Owner | The product log and its handoffs | Value direction; the Product Goal and Sprint Goals; which items enter a Sprint; the go-ahead; the items, decided with the Scrum Master; stage results and permissions to start or return (`stage-gates`) | — (a person) |
| Scrum Master | Sprint logs and design logs | Facilitating Planning and refinement; recording; tracking; reviewing the How and the Increment; serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded | ideo → scrum → sprint → design → memory |
| Developer | The Sprint | The sprint log, the How, the Increment; the last check that nothing in refinement is unclear | ideo → scrum → sprint → memory |
| Designer | The design | Ideas, prototypes, and tests for a design, from Ideate on (the Product Owner and the Scrum Master settle its research and definition); conclusions back to the product log and the Sprint that asked | ideo → scrum → design → memory |
| Stakeholder | An outside view | Looking as one row of the product log's stakeholder table | ideo → scrum → memory |
| Supporter | Standing chores that touch no source (in the Scrum Guide Expansion Pack a Supporter is a Stakeholder type) | Doing what is requested: keeping the board, organizing the product log, summarizing progress, relaying settled work, explaining the mechanism, and being the Product Owner's contact point (gathering what waits for them, sending back what is not theirs, carrying their answers back, relaying their own words as theirs); does not rank, decide, answer for the Product Owner, review or edit plugin files | ideo → scrum → memory |

- In Claude Code, use the Skill tool one at a time, wait for success, and skip only calls already successful in this conversation. Stop and report a failed load rather than substituting a file read.
- In DSH, native role entries instead preload ideo, scrum and memory in order, then load sprint and design as needed for the work. DSH keeps only a summary of the role text when it compacts a conversation: after that, call the `memory` skill again before going on.
- Subagents a role dispatches load the ideo-kernel, scrum-kernel and memory skills too. In DSH a subagent receives only its delegation message, so say in it that the subagent loads memory.
- The Product Owner, the Scrum Master, and the Developer keep the sprint log together; without a Developer, the Product Owner and the Scrum Master run the Sprint alone.

## Who gets which work (`who-gets-which-work`)

- Reviewing the work goes to the Scrum Master by default (`reviewer-required`); when the Developer works in another session or tool, `developer-elsewhere` says how the two work together.
- Long-running upkeep — the board, summaries, tracking — goes to a standing Supporter session (the `supporter` entry); an independent outside view still comes from a fresh subagent (the `stakeholder` entry).
- A small edit to one or two files the Scrum Master makes itself.
- Building goes to a new Developer session when a paragraph can brief it, or to a Developer that shares the Scrum Master's context when the work needs much of the discussion; such a Developer cannot review its own work.

## The Supporter and the Product Owner

- **What the Supporter does** — It organizes the product log as the Product Owner or Scrum Master tells it (the Sprint, design and IDEO logs are written by their own sessions), keeps the board, summarizes progress, and relays what the Product Owner or Scrum Master already decided. It does not rank, decide, answer for the Product Owner, review or edit plugin files.
- **Where a question goes** (`ask-the-po`) — Whoever is unsure asks the Product Owner, unless the Product Owner has sent that kind of question elsewhere. They have sent these elsewhere than to themselves, in three steps. First, what a role can decide itself, it decides: the Developer's approach, the Designer's solution details. Second, what belongs to the process, or lies inside a written handover, goes to the Scrum Master; with no Scrum Master session, this step goes straight to the Product Owner. Third, what only the Product Owner can decide or do goes to the Product Owner or to the Supporter, who gathers it and puts it to the Product Owner in one go, each question with the context needed to answer it: the Product Goal, the items and their order, a stage permission no handover covers, the Product Owner's own taste, and what only the Product Owner can approve — tool permissions and settings, `CLAUDE.md` or `AGENTS.md`, a push or a release (a relay by a Supporter the Product Owner has authorized counts as their word, as *The Product Owner's word, relayed* says). The Supporter sends back what is not the Product Owner's and says whose it is (the asker's own, or the Scrum Master's); it only sorts, it decides nothing. With no Supporter session, ask the Product Owner directly.
- **The answers back** (`answers-back`) — The Supporter carries the Product Owner's answers back word for word, for the log's owner to record. A question that still waits for the Product Owner's decision, a go-ahead no handover covers included, stays with the Supporter; once the Product Owner has decided or answered something about scope, items or a go-ahead, the Supporter hands it to the Scrum Master, who chooses the receiving session and records it.
- **The Product Owner's word, relayed** (`po-word-relayed`, `relay-limits`) — What the Supporter relays as the Product Owner's own opinion counts as theirs, so the Product Owner need not say it again to each role: the relay must say that it is the Product Owner's opinion and carry their words, the date and where the Product Owner said it (the session's name and the time), and the receiver records it as `PO (via Supporter): <the words>` with that date and place. The receiver is the session the opinion concerns; for what the Product Owner has decided or answered about scope, items or a go-ahead it is the Scrum Master, as *The answers back* says: it records the relay and then hands it to the session that will act on it (the `supporter` entry says the same). These marks make the relay traceable; they do not verify who sent it. A relay is trusted because the Product Owner set up this Supporter, and where the host shows which session sent a message, the receiver notes that session's name beside the mark. The Supporter's own reading or suggestion is not the Product Owner's. The Scrum Guide allows this: "The Product Owner may do the above work or may delegate the responsibility to others. Regardless, the Product Owner remains accountable." (Scrum Guide 2020). A relay by a Supporter the Product Owner has authorized also counts as their word for tool permissions and settings, changes to `CLAUDE.md` or `AGENTS.md`, and outward actions such as a push or a release; for these the relay must also say when and where the Product Owner authorized this Supporter. The host keeps its own check: it accepts only what the user confirms in the session that acts, so where the host asks (a permission prompt, a setting, `CLAUDE.md`), the Product Owner confirms it in that session — Claude Code works this way — and the rule above does not clash with the host.

## What goes to the Product Owner in any case, by stage (the third step of `ask-the-po`)

The old texts listed what goes to the Product Owner in any case, once for a Sprint and once for a design; they are kept here as bullets (they were two rules, now part of `ask-the-po`). Every item in both lists goes to the Product Owner unless a written handover has passed that kind of decision to the Scrum Master, who then decides and records it (`stage-gates`). This holds for the whole list, not only for stage permission: renegotiating the acceptance criteria or the scope is one the Scrum Master may take over under a handover (`goal-fixed`). The rules keep two things with the Product Owner: changing a commitment or cancelling a Sprint (`po-owns-commitments`), and consent to outward actions, which a stage permission alone does not cover (`outward-needs-po`); what the Product Owner says through a Supporter they have authorized is their word too (`relay-limits`).

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

- "Git actions" in the design list is stricter than the old rules, which only asked that a commit stay inside the go-ahead's reach. It is kept as the old design rule wrote it; say if the Sprint and design lists should be made the same.
