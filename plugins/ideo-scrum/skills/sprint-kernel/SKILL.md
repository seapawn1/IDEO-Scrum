---
name: sprint-kernel
description: "Use only when summoned to open, run, resume or close this plugin's Sprint: an ideo-scrum role command tells you to load it for Sprint work; the user names ideo-scrum or sprint-kernel for that work; or they ask to create or change the plugin's logs (ProductBacklog.md / 产品日志, SprintBacklog.md / sprint log / 冲刺日志) and the work involves a Sprint. When summoned, invoke this skill before answering, even for a brief request. General Sprint, Sprint Goal, Sprint Backlog, Planning, Review or Retro questions alone are not a summons: answer normally without loading this skill. Once summoned, read the Memory's Sprint rules before planning or writing the log; use scrum-kernel first for the product log and roles. Covers Why, What, How (including solution design with IDEO Ideate when needed, waiting for go-ahead), Increment, Test, refinement, checkpoints and closing, with no Sprint end date; the five Scrum events' source text is in `events/`."
---

# Sprint Kernel

> Source: the events and Sprint Backlog excerpts are from the Scrum Guide Expansion Pack v2026.1 (Ralph Jocham, John Coleman, Jeff Sutherland); the rest is the plugin author's.
> License: the quotations are CC BY-SA 4.0 (© 2025 Ralph Jocham, John Coleman, and Jeff Sutherland); the plugin's own text is MIT.

A Sprint turns selected items into an Increment. This kernel holds what running one takes: the five Scrum events in `events/`, and the pointers to the Sprint rules in the Memory (`../memory/SKILL.md`). The product log, the roles, and the rest of Scrum stay in the scrum-kernel skill (`../scrum-kernel/SKILL.md`); read it first if it is not loaded yet.

*(Author's methodology design for solo + AI teams, 2026-11-12 — not part of the Scrum Guide or SGEP.)*

## The Memory

How a solo + AI team runs a Sprint — the five stages, the sprint log, who decides — is in the memory skill (`../memory/SKILL.md`), its *Running a Sprint* section, with the longer rules in `../memory/details/` (`sprint.md`, `gates.md`, `refinement.md`, `closing.md`, `handoff.md`); the sprint log template is `../../template/sprint-backlog-template.md`. The role commands load the Memory after the kernels; if it is not loaded yet, invoke `ideo-scrum:memory` first. These are working conventions, not source text: follow what fits, depart from what doesn't, and note why. When you open, run, or close a Sprint, write a log, or answer a question about how to do any of these, read the matching Memory lines first, even for a rough answer.

| File | What it covers | Read when |
| --- | --- | --- |
| `../memory/SKILL.md`, `../memory/details/sprint.md` | The Memory's Sprint rules: the five stages of a Sprint — Why, What, How, Increment, Test — and its close | Opening, running, or closing a Sprint |
| `../../template/sprint-backlog-template.md` | The sprint log template; the file made from it is `SprintBacklog.md` | Opening a Sprint |

**Before drafting a Sprint Goal or a refinement, even in chat:** read the whole Memory list (`../memory/SKILL.md`) and, in full, `../memory/details/sprint.md`, `../memory/details/goal-fixed.md`, `../memory/details/gates.md`, `../memory/details/refinement.md`, and `events/scrum-event-sprint-planning.md`. Then read the material for the task:

| Draft | Also read before drafting | Use in the draft |
| --- | --- | --- |
| Sprint Goal (Why) | The full `../scrum-kernel/references/scrum-artifact-sprint-backlog.md` (the excerpt below covers only its Sprint Backlog section), the full comments in `../../template/sprint-backlog-template.md` §§1.1–1.2, and the project's Product Goal in §1.2 of the product log | One objective about the value of this Sprint, toward the Product Goal. Keep item selection and the plan out of the Why. |
| Item refinement (What) | The full `../scrum-kernel/references/scrum-artifact-product-backlog.md`, `../memory/details/product-log.md`, `../ideo-kernel/IDEO-modes/define.md`, and `../ideo-kernel/methods/how-might-we-questions.md`, plus the full §2.2 comment in `../../template/sprint-backlog-template.md` | Take the POV word for word from the item or goal, frame HMWs that leave more than one solution open, distinguish what the Product Owner decides, what the Developer can propose, and what needs research, and propose checkable acceptance criteria. |

Read any other method in full before using it. Material already present in the conversation counts only for the text it covers; a link, a Skill call without the text, or an unfinished read is not enough. If required text is missing, say what is missing and stop before drafting. When the Product Owner says a draft misapplies the method, reread the applicable source and instructions before redrafting. Drafting does not give the go-ahead for the next stage; follow the Memory's stage-gate rules (`stage-gates`).

## Using IDEO Modes Across a Sprint

The IDEO five modes (`../ideo-kernel/SKILL.md`) are the shared toolbox behind every Sprint stage — invoke them on demand when the work calls for them, and skip ceremony when the path is already straightforward. In particular, **How corresponds to Ideate**: when a Sprint involves multiple viable routes, design or architecture tradeoffs, or solution options, read `../ideo-kernel/IDEO-modes/ideate.md` first and diverge before converging (using isolated fresh subagents when distinct approaches are needed; Memory `diverge-first`, `isolated-sketches`); straightforward small changes need no ceremony.

| Sprint stage | On-demand IDEO mode | When to pull it in |
| --- | --- | --- |
| **Why** | Empathize (`../ideo-kernel/IDEO-modes/empathize.md`) | The goal or user need behind the Sprint is unclear |
| **What** | Define (`../ideo-kernel/IDEO-modes/define.md`) | Refining items into POV, HMW questions, and crisp scope |
| **How** | Ideate (`../ideo-kernel/IDEO-modes/ideate.md`) | Choosing between routes, architecture tradeoffs, or solution proposals before writing the plan |
| **Increment** | Prototype (`../ideo-kernel/IDEO-modes/prototype.md`) | Low-fidelity, disposable checks of risky assumptions (never put prototypes into an Increment; Memory `prototype-not-increment`) |
| **Test** | Test (`../ideo-kernel/IDEO-modes/test.md`) | Validating experience and gathering user or role-card reactions (Memory `keep-test-evidence`) |

*(Author's working guide for solo + AI teams, 2026-11-24 — not part of the Scrum Guide or SGEP.)*

## The Scrum Events in the Expansion Pack

Scrum combines four timeboxed events for Inspection and Adaptation within a containing fifth event of determinate consistent length, the Sprint. These events support the Scrum pillars of Transparency, Inspection, and Adaptation. Releases enable value, ideally, continuously. Infrequent releases lead to delayed result feedback.

A timebox is a stipulated maximum amount of elapsed time from beginning to end for a defined event, not to be confused with an expectation to use that full amount of time. The purpose of a timebox in Scrum is to foster the selection of essential work, creating Focus to achieve desired results quickly.

Events create cadence and minimize the need for other meetings not part of Scrum. Ideally, each event is held at the same time and place to reduce complexity [12-17] and foster the formation of habits. Skilled facilitation improves effectiveness. Ineffective events risk losing emphasis on the Sprint Goal, Product Goal, Transparency, Inspection, Adaptation, and Scrum Values.

Each event has its own purpose and should include deep, meaningful work. Together, the Scrum events provide a scaffold of Transparency to inspect and adapt, pause, and reflect. The Scrum events support structured thinking and working, effectiveness, and a balanced workload. (SGEP is influenced by Cynefin and Evidence-Based Management)

Communication is key to ensuring the Scrum Team and Supporters Focus on the right thing. Apart from the Sprint, events may consume less time as long as coherence is not lost.

| Event | Reference | Purpose | Read when |
| --- | --- | --- | --- |
| The Sprint | `events/scrum-event-sprint.md` | Container event that turns ideas into value through an iteration of determinate length. Provides Focus, stability, and a cadence for Inspection and Adaptation toward the Product Goal. | The team needs to understand Sprint rules: what cannot change during a Sprint, when cancellation is appropriate, how shorter Sprints affect learning cycles and risk, or why frequent releasing matters for result feedback. |
| Sprint Planning | `events/scrum-event-sprint-planning.md` | Initiate the Sprint by defining the Sprint Goal (Why), selecting Product Backlog Items (What), and creating an actionable plan (How). Where the Scrum Team gives Focus and creates commitment. | Before drafting the Sprint Goal or refining selected items. Also when the team chronically overloads Sprints — consult the SGEP guidance on buffers and slack. |
| Daily Scrum | `events/scrum-event-daily-scrum.md` | Product Developers inspect progress toward the Sprint Goal and adapt the Sprint Backlog for the next day. Provides Focus, cohesion, urgency, and fosters self-management. | The Developers need to inspect progress toward the Sprint Goal, adapt the Sprint Backlog, identify impediments, or decide whether to pivot toward the Product Goal when the Sprint Goal is already met. Also when the team is starting too many items instead of finishing work in progress. |
| Sprint Review | `events/scrum-event-sprint-review.md` | Inspect the Sprint outcome with Stakeholders and collaboratively determine future adaptations. Inspects the Increment, Product Goal, Product Backlog, market, and Definition of Outcome Done. | The Sprint outcome is ready for Stakeholder inspection. The team presents the Increment, Definition of Output Done, and Definition of Outcome Done measures; Stakeholders and the Scrum Team collaborate on what to do next; the Product Backlog (and possibly Product Goal) may adapt. Also when incomplete PBIs need to be returned to the backlog. |
| Sprint Retrospective | `events/scrum-event-sprint-retrospective.md` | Plan ways to increase quality and effectiveness. The Scrum Team inspects how the last Sprint went and identifies the most helpful changes to improve. | The Sprint is ending. The Scrum Team inspects how the last Sprint went — individuals, interactions, processes, tools, Definition of Done — identifies bad assumptions, and agrees on the most impactful improvements. Also when improvement actions from prior Retros were not followed through. |

---

> Source: Scrum Guide Expanded v2026.1, "The Scrum Artifacts in the Expansion Pack"
> License: CC BY-SA 4.0 (c) 2025 Ralph Jocham, John Coleman, Jeff Sutherland
> Local reference: [Sprint Backlog](../scrum-kernel/references/scrum-artifact-sprint-backlog.md).

## Sprint Backlog

The Sprint Backlog is an artifact. It is composed of the Sprint Goal (the why for the Sprint), the set of Product Backlog Items selected (the what, also known as the forecast) for the Sprint, and often has an actionable plan for delivering the Increment (the how). It provides Transparency (work clarity) throughout the Sprint.

The Sprint Backlog is a plan by and for the Product Developers. It is the Product Developers' viewpoint of the understood work to achieve the Sprint Goal (the why for the Sprint). Suppose a suboptimal scenario where most items in the Sprint Backlog are continually unrelated to the Product Goal. In that case, the Focus and Commitment Scrum Values are not being upheld.

Within the context of the Sprint Goal, the Product Developers update their plan, even the forecast, throughout the Sprint as more is learned. The Sprint Backlog should have enough work to get started, e.g., start with one or two Product Backlog Items toward the Sprint Goal. (SG2017 idea brought back) The Product Developers inspect their progress toward the Sprint Goal in the Daily Scrum or more often. Product Developers learn to adapt and respond to uncertainty.

### Commitment: Sprint Goal

To attain coherence, the Sprint Goal is a commitment created and owned by the Scrum Team (SG2020 Developers owned the commitment). The Sprint Goal is the single unifying objective (coherent with the Product Goal) of the Sprint (the why) for the Product Developers, created in Sprint Planning. Delivery of the Sprint Goal is a commitment by the Product Developers. The Sprint Backlog (including the why, the what, and, often, the how) provides Focus and flexibility regarding the evolving work, thus improving Transparency.

The Sprint Goal encourages the Scrum Team to work together rather than on separate initiatives. If the work turns out to be different from what the Product Developers expected, the Product Developers collaborate with the Product Owner to negotiate possibilities within the Sprint without affecting the Sprint Goal. No one tells the Product Developers how to size or do their work.

If there are multiple objectives, as long as they are coherent with the Product Goal it might be ok. Be careful. Consider the trade off of context switching and focus. The Scrum Team should strive to attain balance over time –– balancing current team capabilities and climate, current stakeholder value, potential stakeholder value and time to value. (SGEP considers DevSecOps)
