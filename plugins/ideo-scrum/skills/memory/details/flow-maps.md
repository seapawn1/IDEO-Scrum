# The process maps

The process maps of the whole flow and of each log, with the lines (handles) that apply at each step written into the boxes, so each map is also an index. Read it to see where a rule sits in the flow.

## The whole flow

Scrum Sprint is the single delivery track below the product log. The IDEO five modes are the shared toolbox supporting every step on demand — not a separate parallel track beside Sprints.

```mermaid
flowchart TD
    PO["Product Owner"]
    SM["Scrum Master"]
    DEV["Developer"]
    SH["Stakeholders"]
    SU["Supporter"]
    IDEO["Shared toolbox: IDEO five modes (Empathize · Define · Ideate · Prototype · Test)<br/>open-ideo-log, diverge-first, isolated-sketches, prototype-not-increment, keep-test-evidence"]
    PO --> A["Write the product log: product, architecture, items<br/>write-product-log, product-log-header, blank-page"]
    SM --> A
    A -- "PO authorizes Why" --> S1["Why: the Sprint Goal<br/>sprint-goal, share-goal-and-checks"]
    S1 -- "PO authorizes What" --> S2["What: the items, refined<br/>select-items, refinement"]
    S2 -- "PO authorizes How" --> S3["How: full solution plan (Ideate when multi-route)<br/>how-is-a-plan, go-ahead, review-handover"]
    S3 -- "PO gives the go-ahead" --> S4["Increment: build, with notes<br/>increment-notes, mark-done"]
    DEV --> S3
    DEV --> S4
    S4 -- "PO authorizes Test" --> S5["Test: tests, review, PO acceptance when required<br/>tests-criteria-first, check-script-misses, reviewer-required, acceptance-when-written, record-the-tests"]
    S5 -. "PO authorizes a return to building" .-> S4
    S5 -- "PO decides: close" --> V["Close: Review (archive Sprint & IDEO logs, refresh product log) and Retro<br/>review-at-close, disputed-points, retro-in-memory, one-closing-commit, outward-needs-po"]
    SH --> V
    SM -- "what only the PO decides (ask-the-po)" --> SU
    SU -- "asks the PO in one go; carries answers back (answers-back)" --> PO
    IDEO -. "Empathize / Define (blank page or unclear goal)" .-> A
    IDEO -. "Empathize (unclear value or users)" .-> S1
    IDEO -. "Define (POV / HMW in refinement)" .-> S2
    IDEO -. "Ideate (diverge-first, isolated-sketches)" .-> S3
    IDEO -. "Prototype (prototype-not-increment)" .-> S4
    IDEO -. "Test (user checks, keep-test-evidence)" .-> S5
    V --> E["End: Sprint Goal met, Increment delivered, Product Goal one step closer"]
```

## The product log

```mermaid
flowchart TD
    A["Starting<br/>write-product-log, blank-page, facts-then-questions"] --> B["Each part<br/>product-log-header, dod-in-product-log, dod-standards, stakeholder-table, architecture-map, no-tbd, no-technical-design"]
    A -. "goal unclear: Empathize & Define (ideo-kernel)" .-> A
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
    H -. "unvalidated user question: IDEO methods / IdeoBacklog.md" .-> H
    H -- "PO ends refinement and authorizes How" --> P["How<br/>how-is-a-plan, diverge-first, isolated-sketches, go-ahead, review-handover"]
    P -- "PO gives the go-ahead" --> I["Increment<br/>increment-notes, mark-done, checkpoints, outline-first, full-text-review, prototype-not-increment"]
    I -- "PO authorizes Sprint Test" --> T["Test<br/>tests-criteria-first, check-script-misses, reviewer-required, acceptance-when-written, record-the-tests, keep-test-evidence"]
    T -- "fix on the spot, test again" --> T
    T -- "PO decides: close" --> C["Closing<br/>review-at-close, disputed-points, retro-in-memory, one-closing-commit, outward-needs-po"]
    T -. "PO authorizes a return to building" .-> I
```

## The five modes and the IDEO log

```mermaid
flowchart TD
    Q["A question with no ready answer (in product log or Sprint)"] --> FM["IDEO five modes (Empathize · Define · Ideate · Prototype · Test)<br/>diverge-first, isolated-sketches, prototype-not-increment, keep-test-evidence"]
    FM -- "1–2 methods in one session" --> SPOT["Record in the log served<br/>(open-ideo-log)"]
    FM -- "multi-method or multi-session run" --> SEQ["Open an IDEO log<br/>(scrum/ideo-suffix/IdeoBacklog.md, no stage gates)"]
    SPOT --> R["Conclusions flow back to the log served; PO decides"]
    SEQ --> R
    R -- "next Sprint Review" --> AR["Archive IdeoBacklog.md + test evidence to scrum/documents/ideo/<br/>(ideo-log-ends)"]
```

## The board

```mermaid
flowchart TD
    L["The logs<br/>product log and open Sprint logs only"] --> R["Read<br/>board-rules"]
    R --> D["Write the data<br/>board-rules"]
    D --> G["Put it in the template<br/>board-rules"]
    G --> B["scrum/ScrumBoard.html<br/>one-board, board-owns-nothing, board-writer, board-rules"]
    B -. "delete it, write it again" .-> L
    SU["Supporter"] -. "writes the board" .-> R
```
