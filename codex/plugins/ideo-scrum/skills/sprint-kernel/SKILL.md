---
name: sprint-kernel
description: "Use when opening, running, or closing a Sprint — Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective, refinement in the Sprint, the sprint log (SprintBacklog), Sprint Goal, Sprint Backlog, checkpoints. Load it before opening a Sprint or writing a sprint log, even for a draft: the sprint log and its templates come from this skill, not from memory. The product log, the roles, and the rest of Scrum are in the scrum-kernel skill, which every role loads first; the five Scrum events' source text is in `events/`. The Sprint here differs from the textbook — five stages (Why, What, How, Increment, Test), no end date, checkpoints instead of a Daily Scrum — so answer from this skill's conventions, not from memory."
---

# Sprint Kernel

> Source: the events chapter is quoted from the Scrum Guide Expansion Pack (Ralph Jocham, John Coleman, Jeff Sutherland); the rest is the plugin author's.
> License: the quotations are CC BY-SA 4.0 (© 2025 Ralph Jocham, John Coleman, and Jeff Sutherland); the plugin's own text is MIT.

A Sprint turns selected items into an Increment. This kernel holds what running one takes: the sprint log conventions in `conventions/`, and the five Scrum events in `events/`. The product log, the roles, and the rest of Scrum stay in the scrum-kernel skill (`../scrum-kernel/SKILL.md`, `../scrum-kernel/overview.md`); read it first if it is not loaded yet.

*(Author's methodology design for solo + AI teams, 2026-11-12 — not part of the Scrum Guide or SGEP.)*

## Conventions

How a solo + AI team runs a Sprint — the five stages, the sprint log, who decides — is in `conventions/sprint-log.md`; the sprint log template is `conventions/sprint-backlog-template.md`. These are working conventions, not source text: follow what fits, override what doesn't, and note why. When you open, run, or close a Sprint, write a log, or answer a question about how to do any of these, read the matching convention first, even for a rough answer.

| File | What it covers | Read when |
| --- | --- | --- |
| `conventions/sprint-log.md` | The five stages of a Sprint — Why, What, How, Increment, Test — and its close | Opening, running, or closing a Sprint |
| `conventions/sprint-backlog-template.md` | The sprint log template; the file made from it is `SprintBacklog.md` | Opening a Sprint |

## The Scrum Events in the Expansion Pack

Scrum combines four timeboxed events for Inspection and Adaptation within a containing fifth event of determinate consistent length, the Sprint. These events support the Scrum pillars of Transparency, Inspection, and Adaptation. Releases enable value, ideally, continuously. Infrequent releases lead to delayed result feedback.

A timebox is a stipulated maximum amount of elapsed time from beginning to end for a defined event, not to be confused with an expectation to use that full amount of time. The purpose of a timebox in Scrum is to foster the selection of essential work, creating Focus to achieve desired results quickly.

Events create cadence and minimize the need for other meetings not part of Scrum. Ideally, each event is held at the same time and place to reduce complexity [12-17] and foster the formation of habits. Skilled facilitation improves effectiveness. Ineffective events risk losing emphasis on the Sprint Goal, Product Goal, Transparency, Inspection, Adaptation, and Scrum Values.

Each event has its own purpose and should include deep, meaningful work. Together, the Scrum events provide a scaffold of Transparency to inspect and adapt, pause, and reflect. The Scrum events support structured thinking and working, effectiveness, and a balanced workload. (SGEP is influenced by Cynefin and Evidence-Based Management)

Communication is key to ensuring the Scrum Team and Supporters Focus on the right thing. Apart from the Sprint, events may consume less time as long as coherence is not lost.

| Event | Reference | Purpose | Read when |
| --- | --- | --- | --- |
| The Sprint | `events/scrum-event-sprint.md` | Container event that turns ideas into value through an iteration of determinate length. Provides Focus, stability, and a cadence for Inspection and Adaptation toward the Product Goal. | The team needs to understand Sprint rules: what cannot change during a Sprint, when cancellation is appropriate, how shorter Sprints affect learning cycles and risk, or why frequent releasing matters for result feedback. |
| Sprint Planning | `events/scrum-event-sprint-planning.md` | Initiate the Sprint by defining the Sprint Goal (Why), selecting Product Backlog Items (What), and creating an actionable plan (How). Where the Scrum Team gives Focus and creates commitment. | A new Sprint is about to begin. The Product Owner proposes value-increasing ideas, the Developers select and decompose PBIs, and the team must craft a Sprint Goal covering Why / What / How. Also when the team chronically overloads Sprints — consult the SGEP guidance on buffers and slack. |
| Daily Scrum | `events/scrum-event-daily-scrum.md` | Product Developers inspect progress toward the Sprint Goal and adapt the Sprint Backlog for the next day. Provides Focus, cohesion, urgency, and fosters self-management. | The Developers need to inspect progress toward the Sprint Goal, adapt the Sprint Backlog, identify impediments, or decide whether to pivot toward the Product Goal when the Sprint Goal is already met. Also when the team is starting too many items instead of finishing work in progress. |
| Sprint Review | `events/scrum-event-sprint-review.md` | Inspect the Sprint outcome with Stakeholders and collaboratively determine future adaptations. Inspects the Increment, Product Goal, Product Backlog, market, and Definition of Outcome Done. | The Sprint outcome is ready for Stakeholder inspection. The team presents the Increment, Definition of Output Done, and Definition of Outcome Done measures; Stakeholders and the Scrum Team collaborate on what to do next; the Product Backlog (and possibly Product Goal) may adapt. Also when incomplete PBIs need to be returned to the backlog. |
| Sprint Retrospective | `events/scrum-event-sprint-retrospective.md` | Plan ways to increase quality and effectiveness. The Scrum Team inspects how the last Sprint went and identifies the most helpful changes to improve. | The Sprint is ending. The Scrum Team inspects how the last Sprint went — individuals, interactions, processes, tools, Definition of Done — identifies bad assumptions, and agrees on the most impactful improvements. Also when improvement actions from prior Retros were not followed through. |

---
