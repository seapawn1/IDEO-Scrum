---
name: scrum-kernel
description: "Use when work involves Scrum — the Product Backlog, Product Goal, Definition of Done, Scrum roles (Product Owner, Scrum Master, Developers), empirical process control for complex projects, or the plugin's product log and its conventions. Load it before creating or changing the Product Backlog, even for a draft: the product log and its template come from this skill, not from memory. Every role loads this skill and the ideo-kernel skill first. Running a Sprint is the sprint-kernel skill, loaded when the work involves one. A new project with no product log yet — an idea on a blank page — starts from a design (design-kernel skill) that fills the product log. A design handles research, Scrum handles implementation: when a problem or direction is unvalidated, open a design first and treat its findings as Sprint evidence; the ideo-kernel methods can help at any time, e.g. when stuck mid-Sprint."
---

# Scrum Kernel

> Source: quoted and summarized from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland) and the Scrum Guide Expansion Pack (Ralph Jocham, John Coleman, Jeff Sutherland); the artifact chapter comes from the Expansion Pack.
> License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland; © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland); the plugin's own text is MIT.

## The Scrum Guide

Scrum is described in `assets/scrum-guide-2020.md`, the definitive 2020 Scrum Guide by Ken Schwaber & Jeff Sutherland. Scrum is a lightweight framework for addressing complex work, particularly in Product discovery, development, delivery, and value realization. Scrum is based on empirical process control (decisions informed by evidence) and lean thinking (reducing waste and focusing on the flow of value). Scrum is purposefully incomplete, guiding interactions rather than prescribing detailed recipes.

## Why Use Scrum?

Scrum enables Scrum Teams to identify, represent, or measure emergence, embrace uncertainty, respond to change, deliver and validate value frequently, and continuously improve. Scrum fosters collaboration, accountability, and evidence-informed decision-making, fostering the best possible outcomes in a rapidly changing environment. Self-managing Scrum Teams, organized around value, are crucial for creative problem-solving and opportunity capture; non-self-managing Scrum Teams hinder the ability to deal with complexity. Self-managing Scrum Teams are not to be confused with individual self-management.

## Working with the Design and IDEO Kernels

Research and implementation are divided: a design (design-kernel skill) handles research; Scrum handles implementation. Before a Sprint, judge whether open questions need a pre-study — when the problem or direction is unvalidated, settle first whether it needs a design sprint or the five modes (`../ideo-kernel/conventions/ideo-log.md`, convention 1) and treat the findings as key Sprint evidence; a hard point met during refinement can be settled the same way while the rest of the Sprint goes on. Before writing the product log, judge the same way: a new project whose product and Product Goal cannot yet be written starts from a design, which fills the product log (`conventions/product-log.md`, convention 2). A question about what people want or what counts as good, with no ready answer, never gets a solution first: it goes to a design sprint or the five modes, as above. The IDEO methods (ideo-kernel skill) are the plugin's shared toolbox and can be used at any time — when the team gets stuck mid-Sprint (e.g., at a checkpoint), they can inspect and research the problem the Sprint is stuck on.

*(Author's methodology design for solo + AI teams, 2026-08; revised 2026-11-08 — not part of the Scrum Guide or SGEP.)*

## Conventions

How a solo + AI team keeps its product log and runs its Sprints is in `overview.md`, beside this file, and in the conventions: `conventions/` here for the product log, and the sprint-kernel skill's `conventions/` for running a Sprint. Start with the overview. When you write the product log or answer a question about how to do it, read the matching convention first, even for a rough answer. The references below are the official texts; the conventions depart from them on purpose in a few places — no Sprint end date, checkpoints instead of the Daily Scrum, a go-ahead before building — and the overview lists them all. Running a Sprint is the sprint-kernel skill's work: `../sprint-kernel/conventions/sprint-log.md` has the five stages and the close, and its `events/` holds the five Scrum events.

| File | What it covers | Read when |
| --- | --- | --- |
| `overview.md` | How the product log, Sprints, and designs fit together; folders, including `scrum/documents/`; roles; what stays fixed | Starting a project, or unsure who does what or where a file goes |
| `conventions/product-log.md` | Writing the product log and refining its items | Writing, refining, or refreshing the product log |
| `conventions/product-backlog-template.md` | The product log template; the file made from it is `ProductBacklog.md` | Creating a product log |

## Elements of Scrum

### 1. Scrum Theory

Built on three pillars:

- **Transparency** – Making work and value visible for Inspection.
- **Inspection** – Regularly assessing progress and outcomes for Adaptation.
- **Adaptation** – Adjusting plans informed by insights and feedback.

### 2. Scrum Values

**Focus, Openness, Courage, Commitment, and Respect** enable effective teamwork; they support trust.

### 3. Roles / Accountabilities

**Scrum Team** – A small, self-managing, cross-functional, cognitively diverse team consisting of:

- **Product Owner** – Maximizes long-term value, engages Stakeholders, and manages the Product Backlog.
- **Scrum Master** – Guides the Scrum adoption, removes impediments, and fosters continuous improvement.
- **Product Developers** – Deliver Increments every Sprint through their cross-functional capabilities.
- **Stakeholder** – An entity, individual, or group interested in, affected by, or impacting inputs, activities, and outcomes with a direct or indirect interest inside or outside the organization, its Products, or services.
- **Supporter** (a Stakeholder type) – Fosters the climate and environment and participates as requested.
- **AI** – As a tool or also a possible Product Developer, but not to be entirely trusted yet.

*(Here only the Product Owner must be human: see `overview.md`, convention 9.)*

### 4. Scrum Events & Activities

Scrum operates in Sprints (iterations of determinate length up to four weeks) with four timeboxed events:

- **Sprint Planning** – Define the Sprint Goal and plan the work.
- **Daily Scrum** – Product Developers align daily on progress toward the Sprint Goal or Product Goal.
- **Sprint Review** – Inspect the Increment, value, and marketplace, and adapt the Product Backlog.
- **Sprint Retrospective** – Reflect and improve the Scrum Team.
- **Refinement** – Clarify upcoming or selected work, formally (as an optional event) or informally.

### 5. Scrum Artifacts & Commitments

- **Product & Definition of Outcome Done** – Product and valuable outcomes that provide evidence of realized benefits.
- **Increment & Definition of Output Done** – A potentially valuable, releasable candidate update for the Product.
- **Product Backlog & Product Goal** – The ordered (sequenced) list of work to achieve a medium-term, more strategic objective.
- **Sprint Backlog & Sprint Goal** – Selected Product Backlog Items and a plan for the Sprint, short-term objective.

---

## The Scrum Artifacts in the Expansion Pack

Scrum’s artifacts provide Transparency about what the Scrum Team and Stakeholders believe will deliver value. Thus, everyone can have the same basis for Inspection and Adaptation.

Each artifact contains a commitment:

For the Product serving the Stakeholders, it is the Definition of Outcome Done. (SGEP added)
For the Increment that is a candidate update for the Product, it is the Definition of Output Done (SGEP renamed).
For the Product Backlog, it is the Product Goal.
For the Sprint Backlog, it is the Sprint Goal.

Upon release of the Increment (output), the Product is what creates value (outcomes). Value is the measurable or observable fulfillment or creation of expectations, needs, or wants from the Stakeholders’ perspective.

These commitments reinforce the pillars of Transparency, Inspection, and Adaptation, enabling empirical process control [27-29]. The Product Goal is fixed for as long as no contrary evidence or observations emerge in the observed Product’s Definition of Outcome Done. The Definition of Output Done is not weakened during the Sprint. So what could be changed instead? It could be the Acceptance Criteria for a specific Product Backlog Item, the implementation or fidelity of a specific feature, or even alternative Product Backlog Items for achieving the Sprint Goal, etc.

If the Product Goal shifts often, it could indicate that something is off, perhaps due to a lack of Focus on what matters. Focus is about being professional and deciding what to work on but also what not to work on.

| Artifact | Reference | Commitment | Read when |
| --- | --- | --- | --- |
| Product | `references/scrum-artifact-product.md` | Definition of Outcome Done | The team needs to define what the Product is (experience vs. platform), identify its Stakeholders, or establish outcome measures for value validation. Also when distinguishing output (Increment) from outcome (realized value). |
| Increment | `references/scrum-artifact-increment.md` | Definition of Output Done | The team negotiates quality standards, inspects whether work meets the Definition of Output Done, or decides if an Increment is releasable. Also when multiple Scrum Teams share a Definition of Output Done. |
| Product Backlog | `references/scrum-artifact-product-backlog.md` | Product Goal | The Product Owner orders the backlog, the team refines PBIs into smaller items, writes Acceptance Criteria or Outcome Criteria, or connects Sprint work to the medium-term Product Goal. Also when evaluating whether a Product Vision should be decomposed into a Product Goal. |
| Sprint Backlog | `references/scrum-artifact-sprint-backlog.md` | Sprint Goal | Sprint Planning is about to start, the Developers need to create or adapt their actionable plan, or the Sprint Goal must be negotiated without endangering it. Also when multiple objectives within one Sprint risk diluting Focus. |

---

## Reference Catalog

| Category | Reference | Contains | Read when |
| --- | --- | --- | --- |
| **Foundation** | `assets/scrum-guide-2020.md` | The definitive 2020 Scrum Guide by Ken Schwaber & Jeff Sutherland | The team is new to Scrum, needs the canonical definitions of roles/events/artifacts, or a dispute about "what Scrum says" must be settled by the source. |
| **SGEP Source** | `assets/scrum-guide-expansion-pack-2026.1.md` | The Scrum Guide Expansion Pack (SGEP) v2026.1, minus its Artifacts and Events chapters — the Artifacts chapters are in `references/`, the Events chapters in the sprint-kernel skill's `events/`. Holds supporting Theory (complexity, emergence, empiricism, lean thinking, cadence), Scrum Values through the OODA lens, Product/Systems/Discovery/Leadership theory, People & Change guidance, and the complete academic reference list (resolves inline citations like `[12-17]` found throughout the reference files). | Specific artifact/event/role content should be looked up in the corresponding reference file first. Read the SGEP source directly when the reference file doesn't cover a topic, when the full theoretical underpinnings are needed, or to look up the full citation for an inline reference marker. |