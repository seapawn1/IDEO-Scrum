# Overview — How the Pieces Fit

> These are working conventions — the author's reading of Scrum and design thinking for solo + AI teams. They are less precise than the official guides. Use them as reference: follow what fits, override what doesn't, and note why. Where a convention departs from the official guide on purpose, the Departures section says so and gives the reason.

> Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland) and the Scrum Guide Expansion Pack v2026.1 (Ralph Jocham, John Coleman, Jeff Sutherland), marked where they appear; the rest is the author's working conventions.
> License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland; © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland).

Source labels and short names are explained in convention 15.

The other files: `conventions/product-log.md` and `../../template/product-backlog-template.md`; `../sprint-kernel/conventions/sprint-log.md` and `../../template/sprint-backlog-template.md`; for designs, `../design-kernel/conventions/design-log.md` and `../../template/design-backlog-template.md`; for the five modes, `../ideo-kernel/conventions/ideo-log.md` and `../../template/ideo-backlog-template.md` (paths are relative to the scrum-kernel skill folder, where this file sits beside `SKILL.md`; the Sprint conventions belong to the sprint-kernel skill, the design conventions to the design-kernel skill, the IDEO conventions to the ideo-kernel skill, and the four log templates sit together in the plugin's `template/` folder, the board's files in its `board/` folder — read them when you open or resume a design, a Sprint, or a run of the five modes).

## The map

```mermaid
flowchart TD
    PO["Product Owner"]
    SM["Scrum Master"]
    DEV["Developer"]
    DES["Designer"]
    SH["Stakeholders"]
    PO --> A["Write the product log: product, architecture, items<br/>product-log.md"]
    SM --> A
    A -- "an item needs design" --> X0["A design question: design sprint or the five modes?<br/>ideo-log.md"]
    BP["A blank page<br/>product-log.md"] -- "PO authorizes Empathize" --> X
    A -- "PO authorizes Why" --> S1["Why: the Sprint Goal<br/>sprint-log.md"]
    S1 -- "PO authorizes What" --> S2["What: the items, refined<br/>sprint-log.md"]
    S2 -- "refinement hits a hard point" --> X0
    S2 -- "PO authorizes How" --> S3["How: a plan<br/>sprint-log.md"]
    S3 -- "PO gives the go-ahead" --> S4["Increment: build, with notes<br/>sprint-log.md"]
    DEV --> S4
    S4 -- "PO authorizes Test" --> S5["Test: tests, review, PO acceptance when required<br/>sprint-log.md"]
    S5 -. "PO authorizes a return to building" .-> S4
    S5 -- "PO decides: close" --> V["Close: Review (archive the logs, refresh the product log) and Retro<br/>sprint-log.md"]
    DES --> X
    SH --> X
    SH --> V
    X0 -- "PO authorizes starting a design sprint" --> X["Design sprint: five stages, each standing on one IDEO mode<br/>design-log.md"]
    X0 -- "the five modes" --> X2["The five modes: one or two methods, recorded in the log they serve;<br/>or an IDEO log for a run of its own<br/>ideo-log.md"]
    X -- "conclusions flow back — a blank page's design fills the product log" --> A
    X2 -- "conclusions flow back" --> A
    V --> E["End: Sprint Goal met, Increment delivered, Product Goal one step closer"]
```

## Conventions

### Where things live

1. **One product log** — Start every project, new or old, from one product log.
2. **Sprints and designs side by side** — Treat Sprints and designs as peers under the product log: a Sprint, the Developer's, delivers an Increment; a design, the Designer's, delivers a prototype and conclusions. Open a design when an item needs design, when Sprint refinement hits a hard point, or for a blank page (`conventions/product-log.md`, convention 2); it is not part of a Sprint. Whether a question needs a design sprint or the five modes is `../ideo-kernel/conventions/ideo-log.md`, convention 1. Decide item by item whether design is needed; a design's conclusions still land through a Sprint; an Increment need not be code — the Definition of Done says what it is. This departs from the Scrum Guide: see Departures.
3. **Three layers**

   | Layer | File | Commitment | Accountable | Facilitates |
   | --- | --- | --- | --- | --- |
   | 1 | Product log | Product Goal | Product Owner, with the Scrum Master | — |
   | 2 | Sprint log | Sprint Goal | Developer | Scrum Master |
   | 2 | Design log | Design goal | Designer | Scrum Master |
   | 3 | Increment: code or documents, as the Definition of Done says | Definition of Done | Developer | — |
   | 3 | Prototype: built to learn, never in an Increment; a design’s prototype stays with its design evidence | Design questions | Designer | — |

   The third layer is not a log and has no prescribed method; it relies on the skills of whoever does the work. Increments add up into the product. The design’s conclusions flow back; its working material, including the prototype, stays with the design and can be referenced by the Sprint that builds those conclusions (`../design-kernel/conventions/design-log.md`, convention 19). The standalone IDEO log has its own rule (`../ideo-kernel/conventions/ideo-log.md`, convention 4).
4. **Folders** — `scrum/` holds all of the Scrum work: `ProductBacklog.md`; `ScrumBoard.html`, the board written from the logs, which keeps no state of its own (`../../board/board-log.md`); `sprint-NN-<suffix>/` with `SprintBacklog.md` and its working files; `design-<suffix>/`, unnumbered, with `DesignBacklog.md`, prototypes, and other working material; `ideo-<suffix>/`, unnumbered, with `IdeoBacklog.md`, prototypes, and working files; and `documents/` (convention 5). The active folders may still hold work that ended and is awaiting Review; read the log’s `Now` before resuming. This is the author’s layout; use your project’s own places if it has them.
5. **Where files go** — A file that serves only one log usually stays in its working folder and can be cleaned up when that work ends. The design’s original working material is the exception: retain it with the design, then move it with its log into the existing `scrum/documents/` archive at Review (`../design-kernel/conventions/design-log.md`, convention 19; `../sprint-kernel/conventions/sprint-log.md`, convention 17). Files serving the whole Scrum also go into `scrum/documents/`, and the logs reference them. A project can use its existing archive subfolders. The project’s own documentation, such as a user manual or API notes, stays where the project keeps it, such as `docs/` at the root.
6. **Working material** — Keep working material out of the log itself; link to the retained design originals as convention 5 says. Key material of general use can go into the project’s memory or instructions, and a large important file goes into `scrum/documents/`. Retro lessons go only where `../sprint-kernel/conventions/sprint-log.md`, convention 18, says, never in instructions.
7. **Names** — The terms used in all the conventions are defined here once:
   - the **product log** is the Product Backlog, kept in `ProductBacklog.md`; the **sprint log** is the Sprint Backlog, kept in `SprintBacklog.md`; the **design log** is kept in `DesignBacklog.md` — a file made from a template takes these names, whatever the template is called;
   - an **IDEO log** is the log of a run of the five modes, kept in `IdeoBacklog.md`;
   - a **product backlog item (PBI)** is one row of the product log's item table;
   - a **role card** is one row of the product log's stakeholder table;
   - a **fresh subagent** starts from its brief alone; a fork of a session, or a copy of one, does not count. When the tool has no subagents, a new session given only the brief is the equivalent.

### Who does what

8. **Roles** — On a Claude Code role command, invoke the kernels in the order shown before doing any role work.

   | Role | Home turf | Accountable for | Claude Code entry kernels, in order |
   | --- | --- | --- | --- |
   | Product Owner | The product log and its handoffs | Value direction; the Product Goal and Sprint Goals; which items enter a Sprint; the go-ahead; the items, decided with the Scrum Master; stage results and permissions to start or return (convention 12) | — (a person) |
   | Scrum Master | Sprint logs and design logs | Facilitating Planning and refinement; recording; tracking; reviewing the How and the Increment; serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded | ideo → scrum → sprint → design |
   | Developer | The Sprint | The sprint log, the How, the Increment; the last check that nothing in refinement is unclear | ideo → scrum → sprint |
   | Designer | The design | Ideas, prototypes, and tests for a design, from Ideate on (the Product Owner and the Scrum Master settle its research and definition); conclusions back to the product log and the Sprint that asked | ideo → scrum → design |
   | Stakeholder | An outside view | Looking as one row of the product log's stakeholder table | ideo → scrum |
   | Supporter | Standing chores that touch no source (in the Scrum Guide Expansion Pack a Supporter is a Stakeholder type) | Doing what is requested: keeping the board, organizing the product log, summarizing progress, relaying settled work, explaining the mechanism, and being the Product Owner's contact point (gathering what waits for them, sending back what is not theirs, carrying their answers back, relaying their own words as theirs); does not rank, decide, answer for the Product Owner, review or edit plugin files | ideo → scrum |

   In Claude Code, use the Skill tool one at a time, wait for success, and skip only calls already successful in this conversation. Stop and report a failed load rather than substituting a file read. In DSH, native role entries instead preload ideo and scrum in order, then load sprint and design as needed for the work. Subagents a role dispatches load the ideo-kernel and scrum-kernel skills too.

   The Product Owner, the Scrum Master, and the Developer keep the sprint log together; without a Developer, the Product Owner and the Scrum Master run the Sprint alone.
9. **Only the Product Owner must be human** — The other roles may all be AI. This departs from the Scrum Guide Expansion Pack: see Departures.
10. **Ask the Product Owner** — Whoever is unsure asks the Product Owner, unless the Product Owner has sent that kind of question elsewhere: convention 14 says where each kind goes.
11. **Product Owner as Developer** — When the Product Owner builds, they take part as a Developer, and the How is worked out with them.
12. **Product Owner decides between stages** — The Product Owner settles each stage’s result. Before starting or returning to a stage of a Sprint or a design sprint, wait for explicit stage permission (not a tool permission) for that stage and scope. Approving a result is not stage permission to move on, though one message can say both clearly. While waiting, record the result or why a return is needed, but do not start or delegate that stage’s work. A new session may resume the same stage within its recorded stage permission and scope; earlier stage permission does not carry over to a return. The Scrum Master acts for the Product Owner only within a written handover covering the particular decision; handing over a review or a choice inside a stage does not hand over a stage transition. The Product Owner's own words, relayed by the Supporter on the conditions in convention 14, count as theirs. Record who decided, the date and basis, and the stage and scope authorized, including the written handover if used. Keep the decision at the end of its stage chapter; if stage permission arrives later, add that dated decision without replacing the earlier one. Record first entry when opening the log. These are stage decisions, not reviews, formal acceptance, or approval of each step. Sprint decisions: `../sprint-kernel/conventions/sprint-log.md`, convention 24; design decisions: `../design-kernel/conventions/design-log.md`, convention 26.

### Sessions

13. **One Scrum Master per project** — Each project has one session as its Scrum Master, leading its Developer, Designer, and Stakeholders. A session above several projects only summarizes; each project's facts stay in its own logs.
14. **Who gets which work** — Reviewing the work goes to the Scrum Master by default (`../sprint-kernel/conventions/sprint-log.md`, convention 14); when the Developer works in another session or tool, `../sprint-kernel/conventions/sprint-log.md`, convention 26, says how the two work together. Long-running upkeep — the board, summaries, tracking — goes to a standing Supporter session (the `supporter` entry); an independent outside view still comes from a fresh subagent (the `stakeholder` entry). A small edit to one or two files the Scrum Master makes itself. Building goes to a new Developer session when a paragraph can brief it, or to a Developer that shares the Scrum Master's context when the work needs much of the discussion; such a Developer cannot review its own work.

    The Supporter and the Product Owner:

    - **What the Supporter does** — It organizes the product log as the Product Owner or Scrum Master tells it (the Sprint, design and IDEO logs are written by their own sessions), keeps the board, summarizes progress, and relays what the Product Owner or Scrum Master already decided. It does not rank, decide, answer for the Product Owner, review or edit plugin files.
    - **Where a question goes** — The Product Owner has sent these questions elsewhere than to themselves (convention 10), in three steps. First, what a role can decide itself, it decides: the Developer's approach, the Designer's solution details. Second, what belongs to the process, or lies inside a written handover, goes to the Scrum Master; with no Scrum Master session, this step goes straight to the Product Owner. Third, what only the Product Owner can decide or do goes to the Supporter, who gathers it and puts it to the Product Owner in one go, each question with the context needed to answer it: the Product Goal, the items and their order, a stage permission no handover covers, the Product Owner's own taste, and what needs the Product Owner in person — tool permissions and settings, `CLAUDE.md` or `AGENTS.md`, a push or a release. The Supporter sends back what is not the Product Owner's and says whose it is (the asker's own, or the Scrum Master's); it only sorts, it decides nothing. With no Supporter session, ask the Product Owner directly.
    - **The answers back** — The Supporter carries the Product Owner's answers back word for word, for the log's owner to record. A question that still waits for the Product Owner's decision, a go-ahead no handover covers included, stays with the Supporter; once the Product Owner has decided or answered something about scope, items or a go-ahead, the Supporter hands it to the Scrum Master, who chooses the receiving session and records it.
    - **The Product Owner's word, relayed** — What the Supporter relays as the Product Owner's own opinion counts as theirs, so the Product Owner need not say it again to each role: the relay must say that it is the Product Owner's opinion and carry their words, the date and where the Product Owner said it (the session's name and the time), and the receiver records it as `PO (via Supporter): <the words>` with that date and place. The receiver is the session the opinion concerns; for what the Product Owner has decided or answered about scope, items or a go-ahead it is the Scrum Master, as "The answers back" says: it records the relay and then hands it to the session that will act on it (the `supporter` entry says the same). These marks make the relay traceable; they do not verify who sent it. A relay is trusted because the Product Owner set up this Supporter, and where the host shows which session sent a message, the receiver notes that session's name beside the mark. The Supporter's own reading or suggestion is not the Product Owner's. The Scrum Guide allows this: "The Product Owner may do the above work or may delegate the responsibility to others. Regardless, the Product Owner remains accountable." (Scrum Guide 2020). The relay does not cover tool permissions and settings, changes to `CLAUDE.md` or `AGENTS.md`, or outward actions such as a push or a release: those need the Product Owner's own confirmation.

### About these conventions

15. **Working conventions** — Reference, not law. Each convention has a short name, for use in conversation, and only the exceptions carry a source label: a convention with no label is the author's practice — how the author works; **Supplement** — inferred by the author's assistant, not yet confirmed in practice; **Decide on the spot** — no fixed rule, decide when it comes up. When you override a convention, write what you did and why in the log's notes: the sprint log's Increment notes, or the chapter of the design log it concerns. The templates carry the flow; the convention files say how, and when a step may be skipped. They describe roles and steps, not the mechanics of any tool.
16. **Templates record outputs** — A template's chapters follow the flow, and its sections hold only what each step produced; how to do a step belongs in the conventions. A log made from a template keeps all of the template's headings, including the chapters filled in later, and adds no sections of its own; put work remarks in the sprint log’s Increment notes or the relevant design chapter. An optional explanation below a commitment table belongs in the commitment’s own section (convention 17).

### What stays fixed

17. **Goal fixed, plan flexible** — Each log has one fixed commitment: the Product Goal, the Sprint Goal, the design goal; the Definition of Done is not weakened either. Everything under a commitment — items, refinement points, acceptance criteria, the How, the chosen design solution — may change as you learn, and each log records what changed and why. Only the Product Owner changes a commitment, and only the Product Owner cancels a Sprint whose goal can no longer be met.
    Keep the product statement in the product log's section 1.1, the Product Goal in its section 1.2, the Sprint Goal in the sprint log's section 1.1, and the design goal in the design log's section 1.2. Each has one one-row table: the first cell is `Commitment` (`承诺` in a Chinese log), the second is the exact text, without bold. Keep one copy, not another at the file’s top; its section heading identifies it. The table is the only source of the current commitment. Optional reasons can follow below it; they are not part of the commitment or what a reader extracts from the table. Exact text on a stage decision line is a snapshot of the commitment at that time, not a second source; do not update it when the current goal changes. Give each goal one short name and keep using that name. An IDEO log has no commitment of its own: its For field points to the log it serves.
    The Scrum Guide says it this way. On the Product Goal: "They must fulfill (or abandon) one objective before taking on the next." During the Sprint: "No changes are made that would endanger the Sprint Goal", "Quality does not decrease", and "Scope may be clarified and renegotiated with the Product Owner as more is learned." And: "Only the Product Owner has the authority to cancel the Sprint."

## Departures from the official guides

Each departure is stated here once, with its reason; the convention named in the last column points back to this table.

| Here | The official guide | Why | See |
| --- | --- | --- | --- |
| Only the Product Owner must be human | SGEP: the Product Owner and the Scrum Master "must be human", and "At least one Product Developer should be human" | One person works with AI and keeps the value decisions | Convention 9 |
| Designs sit beside Sprints | Scrum Guide: all the work "happen within Sprints" | A design delivers no Increment, may span several Sprints, and the Designer and the Developer are peers | Convention 2 |
| The Product Owner decides the items with the Scrum Master | Scrum Guide: "the Developers select items from the Product Backlog" | The Product Owner sets the value direction, and the others say how much fits | `conventions/product-log.md`, convention 12 |
| The How is a plan, and building waits for the go-ahead | Scrum Guide: how to build is "at the sole discretion of the Developers" | The Scrum Master and the Product Owner check the plan, because AI may drift | `../sprint-kernel/conventions/sprint-log.md`, conventions 7 and 8 |
| Checkpoints replace the Daily Scrum | Scrum Guide: the Daily Scrum is "a 15-minute event for the Developers" | AI works by session, not by day | `../sprint-kernel/conventions/sprint-log.md`, convention 10 |
| A reviewer is required | Scrum Guide: the Developers are accountable for "Instilling quality by adhering to a Definition of Done" | A Developer may drift, and a second look catches it | `../sprint-kernel/conventions/sprint-log.md`, convention 14 |
| No Sprint end date | Scrum Guide: Sprints are "fixed length events of one month or less" | AI works by session, so the Product Owner watches at checkpoints for a Sprint that drags on | `../sprint-kernel/conventions/sprint-log.md`, convention 2 |
