# The process maps

The process maps of the six old convention files, with the lines (handles) that apply at each step written into the boxes, so each map is also an index. Read it to see where a rule sits in the flow.

## The whole flow

```mermaid
flowchart TD
    PO["Product Owner"]
    SM["Scrum Master"]
    DEV["Developer"]
    DES["Designer"]
    SH["Stakeholders"]
    SU["Supporter (Sprint 27, pending)"]
    PO --> A["Write the product log: product, architecture, items<br/>write-product-log, product-log-header"]
    SM --> A
    A -- "an item needs design" --> X0["A design question: design sprint or the five modes?<br/>sprint-or-modes"]
    BP["A blank page<br/>blank-page"] -- "PO authorizes Empathize" --> X
    A -- "PO authorizes Why" --> S1["Why: the Sprint Goal<br/>sprint-goal, share-goal-and-checks"]
    S1 -- "PO authorizes What" --> S2["What: the items, refined<br/>select-items, refinement"]
    S2 -- "refinement hits a hard point" --> X0
    S2 -- "PO authorizes How" --> S3["How: a plan<br/>how-is-a-plan, no-steps, go-ahead, review-handover"]
    S3 -- "PO gives the go-ahead" --> S4["Increment: build, with notes<br/>increment-notes, mark-done"]
    DEV --> S4
    S4 -- "PO authorizes Test" --> S5["Test: tests, review, PO acceptance when required<br/>tests-criteria-first, check-script-misses, reviewer-required, acceptance-when-written, record-the-tests"]
    S5 -. "PO authorizes a return to building" .-> S4
    S5 -- "PO decides: close" --> V["Close: Review (archive the logs, refresh the product log) and Retro<br/>review-at-close, retro-in-memory, one-closing-commit, outward-needs-po"]
    DES --> X
    SH --> X
    SH --> V
    SM -- "what only the PO decides" --> SU
    SU -- "collects it for the PO; relays the answer" --> PO
    X0 -- "PO authorizes starting a design sprint" --> X["Design sprint: five stages, each standing on one IDEO mode<br/>question-needs-design, open-a-design, ideate-arrangement"]
    X0 -- "the five modes" --> X2["The five modes: one or two methods, recorded in the log they serve;<br/>or an IDEO log for a run of its own<br/>open-ideo-log, read-mode-file"]
    X -- "conclusions flow back — a blank page's design fills the product log" --> A
    X2 -- "conclusions flow back" --> A
    V --> E["End: Sprint Goal met, Increment delivered, Product Goal one step closer"]
```

## The product log

```mermaid
flowchart TD
    A["Starting<br/>write-product-log, blank-page, facts-then-questions"] --> B["Each part<br/>product-log-header, dod-in-product-log, dod-standards, stakeholder-table, architecture-map, no-tbd, no-technical-design"]
    A -- "the product cannot be written yet" --> D["A design answers it (design-kernel skill)"]
    D -- "conclusions flow back" --> B
    B --> C["Items<br/>item-columns, numbers-not-ranks, items-with-sm, status-lives-here"]
    C --> E["Refinement<br/>refine-in-sprint, acceptance-written-once, where-refined-content"]
    E --> C
    C -- "each Review" --> F["Keeping it fresh<br/>fresh-at-review"]
    F --> C
```

## A Sprint

```mermaid
flowchart TD
    A["Opening<br/>sprint-folder, no-end-date, small-sprint"] -- "PO authorizes Why" --> W["Why<br/>sprint-goal, share-goal-and-checks"]
    W -- "PO sets the goal and authorizes What" --> H["What<br/>select-items, refinement"]
    H -- "a hard point" --> D["Choose: a design sprint with its own gates, or IDEO methods"]
    D -. "what was learned" .-> H
    H -- "PO ends refinement and authorizes How" --> P["How<br/>how-is-a-plan, no-steps, go-ahead, review-handover"]
    P -- "PO gives the go-ahead" --> I["Increment<br/>increment-notes, mark-done, checkpoints, outline-first, full-text-review"]
    I -- "PO authorizes Sprint Test" --> T["Test<br/>tests-criteria-first, check-script-misses, reviewer-required, acceptance-when-written, record-the-tests"]
    T -- "fix on the spot, test again" --> T
    T -- "PO decides: close" --> C["Closing<br/>review-at-close, retro-in-memory, one-closing-commit, outward-needs-po"]
    T -. "PO authorizes a return to building" .-> I
```

## A design

```mermaid
flowchart TD
    A["Opening<br/>question-needs-design, open-a-design, hard-point-only, design-roles, one-session-both-roles, design-branch, design-folder"] -- "PO authorizes Empathize" --> B["Empathize<br/>design-stages, design-stages"]
    B -- "PO authorizes Define" --> C["Define<br/>design-stages"]
    C -- "PO settles how to diverge and authorizes Ideate" --> D["Ideate: diverge<br/>design-stages, diverge-first"]
    D --> E["Ideate: converge<br/>design-stages, talk-with-po, choose-with-po, combine-or-rumble, storyboard"]
    E -- "PO chooses; separately authorizes Prototype" --> F["Prototype<br/>design-stages"]
    F -- "PO authorizes Test" --> G["Test<br/>design-stages, criteria-before-test"]
    G -- "PO decides" --> H["Ending<br/>design-ends, design-conclusions"]
    G -. "PO authorizes a return" .-> R["Resume the stage that needs work<br/>ideate-arrangement"]
```

## The five modes and the IDEO log

```mermaid
flowchart TD
    Q["A question comes up"] --> P{"Design sprint or the five modes?<br/>(sprint-or-modes)"}
    P -- "a design sprint" --> DS["Design sprint:<br/>five stages, each standing on one mode<br/>(design-kernel, DesignBacklog.md)"]
    P -- "the five modes" --> FM["The five modes"]
    FM --> SEQ["A run of its own:<br/>an IDEO log<br/>(IdeoBacklog.md, five chapters, no gates)"]
    FM --> SPOT["One or two methods,<br/>recorded in the log they serve"]
    DS --> R["Conclusions flow back to<br/>the log that asked"]
    SEQ --> R
    SPOT --> R
    SEQ -. "a prototype must be tested<br/>with role cards first" .-> DS
```

## The board

```mermaid
flowchart TD
    L["The logs<br/>product log, open Sprint, design, and IDEO logs"] --> R["Read<br/>board-rules, board-rules, board-rules"]
    R --> D["Write the data<br/>board-rules, board-rules, board-rules, board-rules"]
    D --> G["Put it in the template<br/>board-rules"]
    G --> B["scrum/ScrumBoard.html<br/>one-board, board-owns-nothing, board-writer, board-rules, board-rules, board-rules, board-rules"]
    B -. "delete it, write it again" .-> L
    SU["Supporter (Sprint 27, pending)"] -. "writes the board" .-> R
```

## Open points for the Product Owner

- PENDING SPRINT 27: the Supporter's place in the whole-flow map and the board map follows what Sprint 27 has drafted (the Supporter collects what only the Product Owner decides, and writes the board); redraw the edges when 27 is merged.
