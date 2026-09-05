---
name: scrum-kernel
description: "Use when work involves Scrum or a Scrum Sprint — Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, backlog refinement, Sprint Goal, Product Goal, Definition of Done, Scrum roles (Product Owner, Scrum Master, Developers), empirical process control for complex projects. Division of labor: IDEO handles research, Scrum handles implementation — before starting, check whether open questions need a pre-study: if the problem or solution direction is unvalidated, run the design-kernel skill first and treat its findings as key Sprint evidence; a difficult Sprint may open with an IDEO research round, and when stuck mid-Sprint, IDEO methods can help inspect the problem."
---

# Scrum Kernel

## The Scrum Guide

Scrum is described in `scrum-guide-2020.md`, the definitive 2020 Scrum Guide by Ken Schwaber & Jeff Sutherland. Scrum is a lightweight framework for addressing complex work, particularly in Product discovery, development, delivery, and value realization. Scrum is based on empirical process control (decisions informed by evidence) and lean thinking (reducing waste and focusing on the flow of value). Scrum is purposefully incomplete, guiding interactions rather than prescribing detailed recipes.

## Why Use Scrum?

Scrum enables Scrum Teams to identify, represent, or measure emergence, embrace uncertainty, respond to change, deliver and validate value frequently, and continuously improve. Scrum fosters collaboration, accountability, and evidence-informed decision-making, fostering the best possible outcomes in a rapidly changing environment. Self-managing Scrum Teams, organized around value, are crucial for creative problem-solving and opportunity capture; non-self-managing Scrum Teams hinder the ability to deal with complexity. Self-managing Scrum Teams are not to be confused with individual self-management.

## Working with the Design Kernel

Research and implementation are divided: the design side (design-kernel skill) handles research; Scrum handles implementation. Before a Sprint, judge whether open questions need a pre-study — when the problem or direction is unvalidated, run the design-kernel skill first and treat its findings as key Sprint evidence. A difficult Sprint may open with an IDEO research round (research → prototype) before implementation, and when the team gets stuck mid-Sprint (e.g., at the Daily Scrum), IDEO methods can inspect and research the problem the Sprint is stuck on.

*(Author's methodology design for solo + AI teams, 2026-08 — not part of the Scrum Guide or SGEP.)*

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

## The Scrum Events in the Expansion Pack

Scrum combines four timeboxed events for Inspection and Adaptation within a containing fifth event of determinate consistent length, the Sprint. These events support the Scrum pillars of Transparency, Inspection, and Adaptation. Releases enable value, ideally, continuously. Infrequent releases lead to delayed result feedback.

A timebox is a stipulated maximum amount of elapsed time from beginning to end for a defined event, not to be confused with an expectation to use that full amount of time. The purpose of a timebox in Scrum is to foster the selection of essential work, creating Focus to achieve desired results quickly.

Events create cadence and minimize the need for other meetings not part of Scrum. Ideally, each event is held at the same time and place to reduce complexity [12-17] and foster the formation of habits. Skilled facilitation improves effectiveness. Ineffective events risk losing emphasis on the Sprint Goal, Product Goal, Transparency, Inspection, Adaptation, and Scrum Values.

Each event has its own purpose and should include deep, meaningful work. Together, the Scrum events provide a scaffold of Transparency to inspect and adapt, pause, and reflect. The Scrum events support structured thinking and working, effectiveness, and a balanced workload. (SGEP is influenced by Cynefin and Evidence-Based Management)

Communication is key to ensuring the Scrum Team and Supporters Focus on the right thing. Apart from the Sprint, events may consume less time as long as coherence is not lost.

| Event | Reference | Purpose | Read when |
| --- | --- | --- | --- |
| The Sprint | `references/scrum-event-sprint.md` | Container event that turns ideas into value through an iteration of determinate length. Provides Focus, stability, and a cadence for Inspection and Adaptation toward the Product Goal. | The team needs to understand Sprint rules: what cannot change during a Sprint, when cancellation is appropriate, how shorter Sprints affect learning cycles and risk, or why frequent releasing matters for result feedback. |
| Sprint Planning | `references/scrum-event-sprint-planning.md` | Initiate the Sprint by defining the Sprint Goal (Why), selecting Product Backlog Items (What), and creating an actionable plan (How). Where the Scrum Team gives Focus and creates commitment. | A new Sprint is about to begin. The Product Owner proposes value-increasing ideas, the Developers select and decompose PBIs, and the team must craft a Sprint Goal covering Why / What / How. Also when the team chronically overloads Sprints — consult the SGEP guidance on buffers and slack. |
| Daily Scrum | `references/scrum-event-daily-scrum.md` | Product Developers inspect progress toward the Sprint Goal and adapt the Sprint Backlog for the next day. Provides Focus, cohesion, urgency, and fosters self-management. | The Developers need to inspect progress toward the Sprint Goal, adapt the Sprint Backlog, identify impediments, or decide whether to pivot toward the Product Goal when the Sprint Goal is already met. Also when the team is starting too many items instead of finishing work in progress. |
| Sprint Review | `references/scrum-event-sprint-review.md` | Inspect the Sprint outcome with Stakeholders and collaboratively determine future adaptations. Inspects the Increment, Product Goal, Product Backlog, market, and Definition of Outcome Done. | The Sprint outcome is ready for Stakeholder inspection. The team presents the Increment, Definition of Output Done, and Definition of Outcome Done measures; Stakeholders and the Scrum Team collaborate on what to do next; the Product Backlog (and possibly Product Goal) may adapt. Also when incomplete PBIs need to be returned to the backlog. |
| Sprint Retrospective | `references/scrum-event-sprint-retrospective.md` | Plan ways to increase quality and effectiveness. The Scrum Team inspects how the last Sprint went and identifies the most helpful changes to improve. | The Sprint is ending. The Scrum Team inspects how the last Sprint went — individuals, interactions, processes, tools, Definition of Done — identifies bad assumptions, and agrees on the most impactful improvements. Also when improvement actions from prior Retros were not followed through. |

---

## Reference Catalog

| Category | Reference | Contains | Read when |
| --- | --- | --- | --- |
| **Foundation** | `scrum-guide-2020.md` | The definitive 2020 Scrum Guide by Ken Schwaber & Jeff Sutherland | The team is new to Scrum, needs the canonical definitions of roles/events/artifacts, or a dispute about "what Scrum says" must be settled by the source. |
| **SGEP Source** | `assets/scrum-guide-expansion-pack-2026.1.md` | The full Scrum Guide Expansion Pack (SGEP) v2026.1 — the canonical source from which all reference files are derived. Contains content not yet extracted to references: supporting Theory (complexity, emergence, empiricism, lean thinking, cadence), Scrum Values through the OODA lens, Product/Systems/Discovery/Leadership theory, People & Change guidance, and the complete academic reference list (resolves inline citations like `[12-17]` found throughout reference files). | Specific artifact/event/role content should be looked up in the corresponding reference file first. Read the SGEP source directly when the reference file doesn't cover a topic, when the full theoretical underpinnings are needed, or to look up the full citation for an inline reference marker. |
| **Roles** | `references/scrum-roles.md` | The full Scrum Roles specification from the SGEP — every role and accountability in detail (Product Owner, Scrum Master, Product Developers, Stakeholder, Supporter, AI). | Role definitions or accountabilities are needed beyond the summary in Elements of Scrum §3, e.g. when clarifying who does what, or when writing role guidance. |