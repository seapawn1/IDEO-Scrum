---
name: memory
description: "Use only when summoned: an ideo-scrum role command tells you to load it, or the user asks for the plugin's Memory (the shared rules every role follows). When summoned, invoke this skill before answering, even for a short request. General questions about Scrum or design that do not name this plugin are not a summons: answer normally without loading it."
---

# IDEO-Scrum Memory

> The rules every role follows, one line each. A line marked `[dev,sm]` binds those roles; a line with no mark binds every role. A line that ends in `Read details/<file>.md first.` has its detail in that file: read it before you do what the line is about. These are working conventions: follow what fits; where one does not fit, depart from it and write what you did and why in the log's notes (a Sprint's Increment notes, or the relevant chapter of an IDEO log).


## Who does what, and who decides

- **role-entry** On a role command, load that role's skills in order before any work; stop and report a failed load. Read details/roles.md first.
- **only-po-human** Only the Product Owner must be human; the other roles may all be AI.
- **ask-the-po** Decide what is yours; process questions go to the Scrum Master; PO-only ones to the PO or the Supporter. Read details/roles.md first.
- **po-as-developer** When the PO builds, they take part as a Developer and the How is worked out with them.
- **stage-gates** Enter or return to a stage only on the PO's explicit stage permission; approving a result is not one. Read details/gates.md first.
- **one-scrum-master** One Scrum Master session per project leads its roles; one above projects only summarizes; facts stay in each project's logs.
- **who-gets-which-work** The Scrum Master reviews, the Supporter keeps the board, a Developer never reviews itself. Read details/roles.md first.
- **answers-back** The Supporter returns the PO's answers word for word; scope, item and go-ahead decisions go to the Scrum Master to record.
- **po-word-relayed** A relayed PO opinion counts as theirs: record `PO (via Supporter): <words>` with date and place. Read details/roles.md first.
- **relay-limits** Permissions, settings, CLAUDE.md/AGENTS.md, pushes, releases: only an authorized Supporter may relay. Read details/roles.md first.
- **goal-fixed** Each log's commitment (a Goal, the Definition of Done) stays fixed; the plan under it may change. Read details/goal-fixed.md first.
- **po-owns-commitments** Only the PO changes a commitment or cancels a Sprint whose goal can no longer be met.
- **commitment-table** Keep each commitment in a one-row table, the only source of it. Read details/goal-fixed.md first.

## The product log

- **one-product-log** Start every project, new or old, from one product log.
- **write-product-log** Write the product log from the template; for an old project, from README, issues, plans, leaving history to version control.
- **blank-page** If the product or Product Goal cannot be written yet, Empathize has not gone far enough: use the IDEO five modes (Empathize/Define) to fill the log. Read details/product-log.md first.
- **facts-then-questions** [sm] *Supplement.* Look up facts yourself; ask the PO in one numbered message, each with a recommended answer.
- **product-log-header** Product statement (1.1) and Product Goal (1.2): one-row commitment tables; no Now or Waiting for PO line (other logs only).
- **dod-in-product-log** Keep the full Definition of Done in 1.3; a Sprint picks where to focus checks, never which standards apply.
- **dod-standards** Write standards precisely; keep only what holds across the product; item-specific or tentative ones go in acceptance criteria.
- **stakeholder-table** List stakeholders in 2.1 in a short table; a Stakeholder subagent gets one row, the AI fills in details; if empty, ask the PO.
- **architecture-map** Open 2.2 with a Mermaid flowchart TD map: actors (AI too) on top, ending at the bottom, 5-15 steps; subsections only if needed.
- **no-tbd** Turn an unclear point into an item; a Sprint or the IDEO five modes work it out.
- **no-technical-design** Keep technical design out of the product log; modules and interfaces live in the Increment.
- **item-columns** An item has seven columns: #, Title, User story, Place, Status, Size, Notes. Read details/product-log.md first.
- **numbers-not-ranks** Number items only to count them, every number unique; the PO ranks when an order is needed.
- **items-with-sm** The PO decides items with the Scrum Master; Scrum Master and Developer flag too much or little. Read details/product-log.md first.
- **status-lives-here** An item's status lives in the product log only; a sprint log names items by number.
- **refine-in-sprint** In the product log only add detail (it has no refinement section); finish refinement in the sprint log's 2.2.
- **acceptance-written-once** Acceptance criteria already in the product log are not repeated in the sprint log.
- **where-refined-content** Splits become rows; long design in 2.2 (Place links it); notes in Notes; big files in scrum/documents/, linked in Notes.
- **fresh-at-review** At each Review move done items to 3.2 with source, unfinished to 3.1; delete outdated text. Read details/closing.md first.
- **product-log-changes** Write item changes in Notes; a Product Goal change goes in 1.2 with date and reason, and needs evidence against the old one.

## Running a Sprint

- **sprint-folder** One branch and folder per Sprint, scrum/sprint-NN-<suffix>/; the tag has the same name. Read details/sprint.md first.
- **no-end-date** A Sprint closes when its goal is met or the PO stops it; the PO watches for one that drags on (departs from the Guide).
- **small-sprint** Even half an hour of work gets a Sprint, each step a line or two; stage gates, review and close still apply.
- **sprint-goal** [po,sm] The PO sets the Sprint Goal in their own style, usually with the Scrum Master: one unifying value goal.
- **share-goal-and-checks** [po,sm] Share the Sprint Goal and the checks to focus on with the Scrum Master and the Developer.
- **select-items** [po,sm] Copy items into 2.1 word for word; each serves the Sprint Goal: add a missing one to the product log first; never pad.
- **refinement** [sm,po] The Scrum Master leads refinement with the PO; seven steps; the PO says when it is over. Read details/refinement.md first.
- **how-is-a-plan** [dev] Write chapter 3 as a full solution plan (use IDEO Ideate for multi-route tradeoffs), keeping the work items table (each <=1 session). Read details/sprint.md first.
- **go-ahead** Build only on the PO's go-ahead, with its date and reach (commit … push); approving a plan is not one. Read details/sprint.md first.
- **review-handover** [po,sm] The PO may hand the review of the How, new structures and full texts to the Scrum Master in writing; not the go-ahead.
- **increment-notes** [dev] Keep chapter 4 as the full record: a new session goes by the notes alone and does not work everything out again.
- **mark-done** [dev] Mark a finished work item by prefixing its Done when cell with ✓ <date>, keeping the condition; an unmarked row is not done.
- **checkpoints** Check the work against the Sprint Goal at each stage end, when stuck, when the PO asks (a departure). Read details/sprint.md first.
- **outline-first** Before a new lasting document or template, show the reviewer its outline; write it once they agree. Read details/sprint.md first.
- **full-text-review** Give the reviewer the full text, word for word, to annotate; edit sources only after approval. Read details/sprint.md first.
- **tests-criteria-first** Before the Test, set the method and pass lines in 2.2 and commit them; do not change them after seeing results.
- **check-script-misses** When a check script judges wrongly (false alarm or miss), go through the cases one by one and write down why.
- **reviewer-required** The builder never reviews: the Scrum Master does, or a fresh subagent if the Scrum Master built. Read details/sprint.md first.
- **acceptance-when-written** PO acceptance follows the DoD and the acceptance criteria; where they ask for none, a glance from the PO is enough.
- **record-the-tests** [dev] In chapter 5, show valid evidence for each applicable standard and criterion, else no pass. Read details/sprint.md first.
- **review-at-close** At close, review: compress the sprint log to key decisions, archive it, refresh the product log. Read details/closing.md first.
- **disputed-points** At Review and Retro the Scrum Master lists disputed or deep-research points; the PO may keep any in scrum/documents/ or memory.
- **retro-in-memory** Retro saves only key reusable lessons, one memory entry each; no summary, no instruction files. Read details/closing.md first.
- **one-closing-commit** Close with one commit after clearing old paths everywhere; then tag, merge, delete the branch. Read details/closing.md first.
- **outward-needs-po** Push, release and other outward actions need the PO's consent; a stage permission alone does not cover commit, merge or push.
- **new-work-registered** New work goes in the product log first; the PO decides if it joins the Sprint; the Sprint Goal stays, scope is renegotiable.
- **log-is-the-handoff** Keep a log's header current and write what matters into it before a session ends. Read details/handoff.md first.
- **outside-blocker** [sm] When something outside the team blocks the work, tell the PO at once.
- **mid-sprint-release** A release ready mid-Sprint goes out with the PO's consent; the Sprint does not end.
- **read-the-goal** Before a stage decision, read the exact goal text from its table; if you cannot, stop. Read details/gates.md first.
- **developer-elsewhere** With a Developer elsewhere the sprint log stays the record; talk directly, else take turns. Read details/handoff.md first.

## The five modes and the IDEO log

- **open-ideo-log** Use the IDEO five modes across the Sprint: 1-2 methods in one session go in the log served; more opens an IDEO log (`IdeoBacklog.md`). Read details/ideo-ending.md first.
- **diverge-first** Diverge before converging: at least two methods, including at least one ideo-kernel Ideate method; quantity first, judgment later. Read details/ideo-ending.md first.
- **isolated-sketches** When distinct approaches are wanted, have fresh isolated subagents sketch separately without sharing one example summary. Read details/ideo-ending.md first.
- **prototype-not-increment** Prototypes are rough, quick and built to learn — never put a prototype into an Increment. Read details/ideo-ending.md first.
- **keep-test-evidence** Keep who tested, what showed up, and the answers in `IdeoBacklog.md` or the log served, whether or not conclusions are built. Read details/ideo-ending.md first.
- **ideo-log-ends** Conclusions flow back to the log that asked and the PO decides; archive the IDEO log to `scrum/documents/ideo/` at the next Review. Read details/ideo-ending.md first.

## The Scrum board

- **one-board** Keep one board page for the whole project that shows at a glance where it stands and what each line of work is doing.
- **board-owns-nothing** The board only reads the logs: no state, no log changed from it; whether to commit it is the project's call.
- **board-writer** A cheap model or the Supporter writes scrum/ScrumBoard.html when the PO wants to look or a log changed.
- **board-rules** What the board reads, the data it holds, how to copy and check it; the brief for its writer. Read ../../board/board-log.md first.

## About these rules

- **three-layers** Product log, then sprint log, then Increment; prototypes built with the IDEO five modes stay outside Increments. Read details/folders.md first.
- **scrum-folders** All Scrum work lives under scrum/; use your project's own places if it has them. Read details/folders.md first.
- **where-files-go** One log's files stay in its folder; archived logs, IDEO test evidence and shared files go to scrum/documents/. Read details/folders.md first.
- **working-material** Keep working material out of the log; big files in scrum/documents/; Retro lessons: memory only. Read details/folders.md first.
- **names** Use the plugin's own terms (product log, sprint log, IDEO log, PBI, role card) as defined. Read details/names.md first.
- **fresh-subagent** A fresh subagent starts from its brief alone; a fork or copy of a session does not count.
- **rule-labels** No label: author's practice; *Supplement*: inferred, unconfirmed; *Decide on the spot*: no fixed rule. Read details/names.md first.
- **templates-record-outputs** A template section holds only what its step produced; keep every heading, add none. Read details/names.md first.
- **flow-maps** Process maps of the whole flow and of each log, with the lines that apply at each step. Read details/flow-maps.md first.
- **departures** The plugin departs from the Scrum Guide on purpose in six places, each with its reason. Read details/departures.md first.
