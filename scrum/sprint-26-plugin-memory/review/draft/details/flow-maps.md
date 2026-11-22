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
    SU["Supporter"]
    PO --> A["Write the product log: product, architecture, items<br/>‹product-log#1›, ‹product-log#4›"]
    SM --> A
    A -- "an item needs design" --> X0["A design question: design sprint or the five modes?<br/>‹ideo-log#1›"]
    BP["A blank page<br/>‹product-log#2›"] -- "PO authorizes Empathize" --> X
    A -- "PO authorizes Why" --> S1["Why: the Sprint Goal<br/>‹sprint-log#4›"]
    S1 -- "PO authorizes What" --> S2["What: the items, refined<br/>‹sprint-log#5›, ‹sprint-log#6›"]
    S2 -- "refinement hits a hard point" --> X0
    S2 -- "PO authorizes How" --> S3["How: a plan<br/>‹sprint-log#7›, ‹sprint-log#8›"]
    S3 -- "PO gives the go-ahead" --> S4["Increment: build, with notes<br/>‹sprint-log#9›"]
    DEV --> S4
    S4 -- "PO authorizes Test" --> S5["Test: tests, review, PO acceptance when required<br/>‹sprint-log#13›, ‹sprint-log#14›, ‹sprint-log#15›, ‹sprint-log#16›"]
    S5 -. "PO authorizes a return to building" .-> S4
    S5 -- "PO decides: close" --> V["Close: Review (archive the logs, refresh the product log) and Retro<br/>‹sprint-log#17›, ‹sprint-log#18›, ‹sprint-log#19›"]
    DES --> X
    SH --> X
    SH --> V
    SM -- "what only the PO decides ‹overview#10›" --> SU
    SU -- "asks the PO in one go; carries the answer back (answers-back)" --> PO
    X0 -- "PO authorizes starting a design sprint" --> X["Design sprint: five stages, each standing on one IDEO mode<br/>‹design-log#1›, ‹design-log#26›"]
    X0 -- "the five modes" --> X2["The five modes: one or two methods, recorded in the log they serve;<br/>or an IDEO log for a run of its own<br/>‹ideo-log#3›"]
    X -- "conclusions flow back — a blank page's design fills the product log" --> A
    X2 -- "conclusions flow back" --> A
    V --> E["End: Sprint Goal met, Increment delivered, Product Goal one step closer"]
```

## The product log

```mermaid
flowchart TD
    A["Starting<br/>‹product-log#1›, ‹product-log#2›, ‹product-log#3›"] --> B["Each part<br/>‹product-log#4›, ‹product-log#5›, ‹product-log#6›, ‹product-log#7›, ‹product-log#8›, ‹product-log#9›"]
    A -- "the product cannot be written yet" --> D["A design answers it (design-kernel skill)"]
    D -- "conclusions flow back" --> B
    B --> C["Items<br/>‹product-log#10›, ‹product-log#11›, ‹product-log#12›, ‹product-log#13›"]
    C --> E["Refinement<br/>‹product-log#14›, ‹product-log#15›, ‹product-log#16›"]
    E --> C
    C -- "each Review" --> F["Keeping it fresh<br/>‹product-log#17›"]
    F --> C
```

## A Sprint

```mermaid
flowchart TD
    A["Opening<br/>‹sprint-log#1›, ‹sprint-log#2›, ‹sprint-log#3›"] -- "PO authorizes Why" --> W["Why<br/>‹sprint-log#4›"]
    W -- "PO sets the goal and authorizes What" --> H["What<br/>‹sprint-log#5›, ‹sprint-log#6›"]
    H -- "a hard point" --> D["Choose: a design sprint with its own gates, or IDEO methods"]
    D -. "what was learned" .-> H
    H -- "PO ends refinement and authorizes How" --> P["How<br/>‹sprint-log#7›, ‹sprint-log#8›"]
    P -- "PO gives the go-ahead" --> I["Increment<br/>‹sprint-log#9›, ‹sprint-log#10›, ‹sprint-log#11›, ‹sprint-log#12›"]
    I -- "PO authorizes Sprint Test" --> T["Test<br/>‹sprint-log#13›, ‹sprint-log#14›, ‹sprint-log#15›, ‹sprint-log#16›"]
    T -- "fix on the spot, test again" --> T
    T -- "PO decides: close" --> C["Closing<br/>‹sprint-log#17›, ‹sprint-log#18›, ‹sprint-log#19›"]
    T -. "PO authorizes a return to building" .-> I
```

## A design

```mermaid
flowchart TD
    A["Opening<br/>‹design-log#1›, ‹design-log#2›, ‹design-log#3›, ‹design-log#4›, ‹design-log#5›"] -- "PO authorizes Empathize" --> B["Empathize<br/>‹design-log#6›, ‹design-log#7›"]
    B -- "PO authorizes Define" --> C["Define<br/>‹design-log#8›"]
    C -- "PO settles how to diverge and authorizes Ideate" --> D["Ideate: diverge<br/>‹design-log#9›, ‹design-log#10›"]
    D --> E["Ideate: converge<br/>‹design-log#11›, ‹design-log#12›, ‹design-log#13›, ‹design-log#14›, ‹design-log#15›"]
    E -- "PO chooses; separately authorizes Prototype" --> F["Prototype<br/>‹design-log#16›"]
    F -- "PO authorizes Test" --> G["Test<br/>‹design-log#17›, ‹design-log#18›"]
    G -- "PO decides" --> H["Ending<br/>‹design-log#19›"]
    G -. "PO authorizes a return" .-> R["Resume the stage that needs work<br/>‹design-log#26›"]
```

## The five modes and the IDEO log

```mermaid
flowchart TD
    Q["A question comes up"] --> P{"Design sprint or the five modes?<br/>(‹ideo-log#1›)"}
    P -- "a design sprint" --> DS["Design sprint:<br/>five stages, each standing on one mode<br/>(design-kernel, DesignBacklog.md)"]
    P -- "the five modes" --> FM["The five modes"]
    FM --> SEQ["A run of its own:<br/>an IDEO log<br/>(IdeoBacklog.md, five chapters, no gates)"]
    FM --> SPOT["One or two methods,<br/>recorded in the log they serve"]
    DS --> R["Conclusions flow back to<br/>the log that asked"]
    SEQ --> R
    SPOT --> R
```

## The board

```mermaid
flowchart TD
    L["The logs<br/>product log, open Sprint, design, and IDEO logs"] --> R["Read<br/>‹board-log#4›, ‹board-log#5›, ‹board-log#6›"]
    R --> D["Write the data<br/>‹board-log#11›, ‹board-log#12›, ‹board-log#13›, ‹board-log#16›"]
    D --> G["Put it in the template<br/>‹board-log#17›"]
    G --> B["scrum/ScrumBoard.html<br/>‹board-log#1›, ‹board-log#2›, ‹board-log#3›, ‹board-log#8›, ‹board-log#9›, ‹board-log#10›"]
    B -. "delete it, write it again" .-> L
    SU["Supporter"] -. "writes the board" .-> R
```

## Open points for the Product Owner

- None.
