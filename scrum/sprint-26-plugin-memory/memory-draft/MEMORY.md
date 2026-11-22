# IDEO-Scrum Memory

> The rules every role follows, one line each. A line marked `[dev,sm]` binds those roles; a line with no mark binds every role. A line that ends in `Read details/<file>.md first.` has its detail in that file: read it before you do what the line is about. These are working conventions: follow what fits, override what doesn't, and say why in the log's notes.


## Who does what, and who decides

- **role-entry** On a role command, load that role's skills in order before any work; stop and report a failed load. Read details/roles.md first.
- **only-po-human** Only the Product Owner must be human; the other roles may all be AI.
- **ask-the-po** Decide what is yours; process questions go to the Scrum Master; PO-only questions go to the Supporter. Read details/roles.md first.
- **po-as-developer** When the PO builds, they take part as a Developer and the How is worked out with them.
- **stage-gates** Enter or return to a stage only on the PO's explicit stage permission; approving a result is not one. Read details/gates.md first.
- **one-scrum-master** One Scrum Master session per project leads its other roles; a session above several projects only summarizes.
- **who-gets-which-work** The Scrum Master reviews, the Supporter keeps the board, a Developer never reviews itself. Read details/roles.md first.
- **answers-back** The Supporter returns the PO's answers word for word; scope, item and go-ahead decisions go to the Scrum Master to record.
- **po-word-relayed** A relayed PO opinion counts as theirs: record `PO (via Supporter): <words>` with date and place. Read details/roles.md first.
- **relay-limits** A relay never covers tool permissions and settings, CLAUDE.md or AGENTS.md, a push or a release: those need the PO's own word.
- **goal-fixed** Each log's commitment (a Goal, the Definition of Done) stays fixed; the plan under it may change. Read details/goal-fixed.md first.
- **po-owns-commitments** Only the PO changes a commitment or cancels a Sprint whose goal can no longer be met.
- **commitment-table** Keep each commitment in a one-row table, the only source of it. Read details/goal-fixed.md first.

## The product log

- **one-product-log** Start every project, new or old, from one product log.
- **write-product-log** Write the product log from the template, usually the Scrum Master with the PO; for an old project, from README, issues, plans.
- **blank-page** If the product cannot be written yet, start from a design and let its conclusions fill the log. Read details/product-log.md first.
- **facts-then-questions** [sm] *Supplement.* Look up facts yourself; ask the PO in one numbered message, each with a recommended answer.
- **product-log-header** Keep the product statement (1.1) and Product Goal (1.2) each in a one-row commitment table; no Now line.
- **dod-in-product-log** Keep the full Definition of Done in 1.3; a Sprint picks where to focus checks, never which standards apply.
- **dod-standards** Write standards precisely; keep only what holds across the product, the rest goes in acceptance criteria.
- **stakeholder-table** [sm] List stakeholders in 2.1, one row each; a Stakeholder subagent gets one row; if empty, ask the PO.
- **architecture-map** Start 2.2 with one Mermaid flowchart TD map: actors on top, the ending at the bottom, five to fifteen steps.
- **no-tbd** Turn an unclear point into an item; a Sprint or a design works it out.
- **no-technical-design** Keep technical design out of the product log; modules and interfaces live in the Increment.
- **item-columns** An item has seven columns: #, Title, User story, Place, Status, Size, Notes. Read details/product-log.md first.
- **numbers-not-ranks** Number items only to count them, every number unique; the PO ranks when an order is needed.
- **items-with-sm** [sm,po] The PO decides the items with the Scrum Master; the Scrum Master and Developer say when it is too much.
- **status-lives-here** An item's status lives in the product log only; a sprint log names items by number.
- **refine-in-sprint** In the product log only add detail; finish refinement in the sprint log's 2.2.
- **acceptance-written-once** Acceptance criteria already in the product log are not repeated in the sprint log.
- **where-refined-content** Split-off items are new rows; long design content goes in 2.2, notes in Notes, big files in scrum/documents/.
- **fresh-at-review** At each Review move done items to 3.2, send unfinished ones back to 3.1, delete outdated text; keep no revision record.
- **product-log-changes** Write item changes in Notes; a Product Goal change goes in 1.2 with date and reason, and needs evidence against the old one.

## Running a Sprint

- **sprint-folder** One branch and folder per Sprint, scrum/sprint-NN-<suffix>/; the tag has the same name. Read details/sprint.md first.
- **no-end-date** A Sprint closes when its goal is met or the PO stops it; the PO watches for one that drags on (departs from the Guide).
- **small-sprint** Even half an hour of work gets a Sprint, each step a line or two; stage gates, review and close still apply.
- **sprint-goal** [po,sm] The PO sets the Sprint Goal in their own style, usually with the Scrum Master: one unifying value goal.
- **share-goal-and-checks** [po,sm] Share the Sprint Goal and the checks to focus on with the Scrum Master and the Developer.
- **select-items** [po,sm] Check each item against the Sprint Goal: add what it lacks, drop what does not serve it, never pad.
- **refinement** [sm,po] The Scrum Master leads refinement with the PO; seven steps; the PO says when it is over. Read details/refinement.md first.
- **how-is-a-plan** [dev] The How is a plan of work items, each done in one session, with an output and a done test. Read details/sprint.md first.
- **no-steps** [dev] Keep the How at the level of approach: no steps, no file contents, no polishing; if you can write the steps, do the work.
- **go-ahead** Build only on the PO's go-ahead, with its date and reach (commit … push); approving a plan is not one. Read details/sprint.md first.
- **review-handover** [po,sm] The PO may hand the review of the How, new structures and full texts to the Scrum Master in writing; not the go-ahead.
- **increment-notes** [dev] Keep chapter 4 as the full record, so a new session can pick the Sprint up from the log alone.
- **mark-done** [dev] Mark a finished work item by prefixing its Done when cell with ✓ <date>; an unmarked row is not done.
- **checkpoints** Check the work against the Sprint Goal at each stage end, when stuck, when the PO asks (a departure). Read details/sprint.md first.
- **outline-first** For a new lasting document or template, first show the reviewer its outline (headings, one line each); write it once they agree.
- **full-text-review** Give the reviewer the full text to annotate, with problems and advice; edit sources only after approval; the disk version wins.
- **tests-criteria-first** Before the Test, set the method and pass lines in 2.2 and commit them; do not change them after seeing results.
- **check-script-misses** Check a script's wrong calls one by one and write down why.
- **reviewer-required** The builder never reviews: the Scrum Master does, or a fresh subagent if the Scrum Master built. Read details/sprint.md first.
- **acceptance-when-written** Ask the PO for formal acceptance only when the DoD or acceptance criteria call for it; sometimes a glance is enough.
- **record-the-tests** [dev] In chapter 5, show valid evidence for each applicable standard and criterion, else no pass. Read details/sprint.md first.
- **review-at-close** At close, review: compress the sprint log to key decisions, archive it, refresh the product log. Read details/closing.md first.
- **retro-in-memory** Retro saves only key reusable lessons, one memory entry each; no summary, no instruction files. Read details/closing.md first.
- **one-closing-commit** Close with one commit after clearing old paths everywhere; then tag, merge, delete the branch. Read details/closing.md first.
- **outward-needs-po** Push, release and other outward actions need the PO's consent; a stage permission never covers commit, merge or push.
- **new-work-registered** New work goes into the product log first; the PO decides whether it enters this Sprint; the Sprint Goal stays.
- **log-is-the-handoff** Keep a log's header current and write what matters into it before a session ends. Read details/handoff.md first.
- **outside-blocker** [sm] When something outside the team blocks the work, tell the PO at once.
- **mid-sprint-release** A release ready mid-Sprint goes out with the PO's consent; the Sprint does not end.
- **read-the-goal** Before a stage decision, read the exact goal text from its table; if you cannot, stop. Read details/gates.md first.
- **developer-elsewhere** With a Developer elsewhere the sprint log stays the record; talk directly, else take turns. Read details/handoff.md first.

## Running a design sprint

- **question-needs-design** A question of what people want or what is good: look for a ready answer, else pick a design sprint or the five modes.
- **open-a-design** Open a design for a design sprint and start with Empathize on the PO's permission, never with solutions; a blank page is one.
- **hard-point-only** From a Sprint, take out only the hard point that needs design; the rest of the Sprint goes on.
- **design-roles** [po,sm,des] The PO and Scrum Master settle Empathize and Define; the Designer owns the design from Ideate on.
- **one-session-both-roles** [po,sm,des] The PO decides if one session plays Designer and Scrum Master; if so, write its name in both header fields.
- **design-branch** A design opens its own branch off the Sprint branch or main; never name it <sprint-branch>/<name> (git cannot hold a and a/b).
- **design-folder** A design lives in scrum/design-<suffix>/ (a suffix saying what it is about, no number); its prototypes never go into an Increment.
- **design-stages** Each design stage: people first, experts if unclear, the map, ideas, prototype, role-card test. Read details/design.md first.
- **diverge-first** Sketchers diverge first: two methods, one an ideo-kernel Ideate method, quantity, no judgment. Read details/design.md first.
- **talk-with-po** The main thread talks ideas over with the PO and merges all lines before converging; with none from the PO, it sketches one.
- **choose-with-po** [po,sm] The Scrum Master leads the choice and the PO decides, no consensus hunt; a role-card straw poll only if the PO asks.
- **combine-or-rumble** Combine winners that fit; when two conflict, prototype both and let the test decide; the PO decides which.
- **storyboard** Write a storyboard of about fifteen steps in 3.2 only when the solution needs one before the prototype; the Designer writes it.
- **criteria-before-test** Before testing, write what counts as a yes, a no or a not yet for each design question, and what role cards cannot show.
- **design-ends** A design ends when the PO says its questions are answered or stops it; Review archives it. Read details/design-ending.md first.
- **design-conclusions** At its end, write the conclusions into the product log, pass them to the asking Sprint. Read details/design-ending.md first.
- **ideo-in-every-stage** Each design stage takes its methods from the IDEO mode it stands on.
- **ideate-arrangement** Until the PO settles how Ideate diverges, no gathering, sketching or delegating. Read details/gates.md first.
- **small-design** A small design is still a design: keep the log, shrink each stage to a line or two, skip no stage, keep the stage permissions.

## The five modes and the IDEO log

- **sprint-or-modes** The PO picks a design sprint or the five modes; default to a design sprint only if a prototype must be tested with role cards.
- **modes-are-not-the-sprint** Keep modes and sprint apart: an IDEO log runs no map, Lightning Demos or storyboard; a design sprint opens no IDEO log.
- **research-as-empathize** Chat or IDEO-log research can count as Empathize material, but a design sprint still starts on the PO's permission.
- **open-ideo-log** One or two methods write into the log they serve; a longer run gets scrum/ideo-<suffix>/IdeoBacklog.md, five chapters, no PO gate.
- **read-mode-file** Read a mode's or method's file in the ideo-kernel before using it; a chapter holds what its mode produced.
- **ideo-log-home** An IDEO log lives in scrum/ideo-<suffix>/ with its prototypes; it has no commitment, its For cell names the log it serves.
- **ideo-log-ends** Conclusions flow back to the log that asked and the PO decides; archive at the next Review. Read details/ideo-ending.md first.

## The Scrum board

- **one-board** Keep one board page for the whole project that shows at a glance where it stands and what each line of work is doing.
- **board-owns-nothing** The board only reads the logs: no state, no log changed from it; whether to commit it is the project's call.
- **board-writer** A cheap model or the Supporter writes scrum/ScrumBoard.html when the PO wants to look or a log changed.
- **board-rules** What the board reads, the data it holds, how to copy and check it; the brief for its writer. Read ../../board/board-log.md first.

## About these rules

- **designs-beside-sprints** A design sits beside a Sprint, not in it: open one for an item that needs design. Read details/folders.md first.
- **three-layers** Product log, then a sprint or design log, then the Increment or prototype. Read details/folders.md first.
- **scrum-folders** All Scrum work lives under scrum/; use your project's own places if it has them. Read details/folders.md first.
- **where-files-go** One log's files stay in its folder; design originals and shared files go to scrum/documents/. Read details/folders.md first.
- **working-material** Keep working material out of the log and link to it; key general material may go to project memory, Retro lessons only there.
- **names** Use the plugin's own terms (product log, sprint log, design log, IDEO log, PBI, role card) as defined. Read details/names.md first.
- **fresh-subagent** A fresh subagent starts from its brief alone; a fork or copy of a session does not count.
- **rule-labels** No label: the author's practice; *Supplement*: inferred, unconfirmed; *Decide on the spot*: no fixed rule.
- **templates-record-outputs** Keep every template heading and add none; sections hold only what each step produced.
- **flow-maps** Process maps of the whole flow and of each log, with the lines that apply at each step. Read details/flow-maps.md first.
- **departures** The plugin departs from the Scrum Guide on purpose in seven places, each with its reason. Read details/departures.md first.
