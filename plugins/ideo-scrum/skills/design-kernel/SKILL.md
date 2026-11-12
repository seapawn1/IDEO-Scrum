---
name: design-kernel
description: "Use when the user mentions a design sprint or asks to open a design — \"run a design sprint\", \"open a design for this\", \"this needs designing before we build\" — works in a design log (DesignBacklog), has an undefined challenge that needs a pre-study before any Sprint, or starts a new project with no product log yet — an idea on a blank page — which begins with a design that fills the product log. Load it before answering, even for a quick outline: the design sprint here differs from the common five-day version, so answer from this skill, not from memory. A design is a research module beside the Sprint, from a challenge to a tested prototype and conclusions — not code, API, or UI design work. Five stages, not five days: Empathize (challenge, design goal, design questions, ask the experts), Define (map, How Might We), Ideate (sketch solutions, choose one, storyboard), Prototype, Test. Built on the ideo-kernel skill, the shared toolbox; for IDEO alone, use ideo-kernel."
---

# Design Kernel

A design answers a hard question before the team builds: it starts from a challenge and ends with a tested prototype and conclusions. It is a module beside the Sprint, not inside it; the rule and the reason are in `../scrum-kernel/overview.md`, convention 2. A new project whose product and Product Goal cannot yet be written starts from a design, which fills the product log (`../scrum-kernel/conventions/product-log.md`, convention 2). The method is the design sprint from Knapp, Zeratsky & Kowitz, _Sprint_ (2016), regrouped into five stages, each standing on one of the five IDEO modes (how the modes and the sprint differ: `../ideo-kernel/conventions/ideo-log.md`, convention 2). The book runs the sprint Monday to Friday with a team in one room; here the stages run as fast as the work allows, not by day. Day names, clock times, and timers left in the source text are the book's schedule, not an instruction. The source text keeps the book's terms: its long-term goal is the design goal here, its sprint questions are the design questions, its Decider is the Product Owner, and its Facilitator is the Scrum Master.

Each stage maps to an IDEO mode. The mode's guide and its methods live in the ideo-kernel skill, the plugin's shared toolbox, and are not repeated here — read the mode file named in the table before the stage begins.

**IDEO is required in every stage.** The design sprint here is only the skeleton: the stages and the book's steps. The detailed methodology each stage needs is in the ideo-kernel, and you must use it: before a stage, read the IDEO mode file the stage maps to and work to its focus; pick the methods that fit from there, and read a method's file before using it, as the ideo-kernel skill's Use Protocol says. Each stage runs the book's steps and the IDEO mode together — not one or the other — even where the book prefers a different technique.

*(Author's methodology design for solo + AI teams, 2026-11-08; source excerpts are cited per file.)*

## Five Stages

| Stage | IDEO mode (ideo-kernel) and its focus | The book's steps | Source excerpts |
| --- | --- | --- | --- |
| **Empathize** | `../ideo-kernel/IDEO-modes/empathize.md` — understand the people: start from the people concerned, and write the challenge, the design goal, and the design questions from what they told you, each finding with its source (conventions 6–7) | Write the challenge, the design goal, and the design questions; ask the experts and research when needed, after drafting a rough map (it lives in Define) | `steps/1-1-define-the-challenge.md`, `steps/1-2-start-at-the-end.md`, `steps/1-3-ask-the-experts.md` |
| **Define** | `../ideo-kernel/IDEO-modes/define.md` — frame the problem: write the How Might We questions against the map, with the challenge, the design goal, and the design questions of the Empathize chapter beside it (convention 8) | Make a map; turn what you learned into How Might We questions. No target step while the design runs: the design is already the target; a blank-page design picks its target when it ends (convention 19); if it is too wide, split it out (convention 8) | `steps/2-1-make-a-map.md`, `steps/2-2-how-might-we.md` |
| **Ideate** | `../ideo-kernel/IDEO-modes/ideate.md` — diverge first, then converge: each sketcher diverges before it sketches (convention 10) | Reach one solution the Product Owner chooses: gather existing ideas; each person sketches one solution alone; decide; rumble if two winners conflict; storyboard the winner if it helps (here: conventions 9 and 11–15) | `steps/3-1-remix-and-improve.md`, `steps/3-2-sketch.md`, `steps/3-3-decide.md`, `steps/3-4-rumble.md`, `steps/3-5-storyboard.md` |
| **Prototype** | `../ideo-kernel/IDEO-modes/prototype.md` — build to learn: rough, quick, and thrown away after (convention 16) | Adopt the prototype mindset and build a realistic facade of the chosen solution (and its storyboard, if there is one) — just enough to learn; divide the work, stitch it together, do a trial run | `steps/4-1-fake-it.md`, `steps/4-2-prototype.md` |
| **Test** | `../ideo-kernel/IDEO-modes/test.md` — learn from real reactions; "we were wrong" is an answer (conventions 17–18) | Interview the testers one at a time with the Five-Act Interview; watch together, look for patterns, and answer the design questions (here the testers are Stakeholders from the product log's stakeholder table, and the Product Owner: convention 17) | `steps/5-1-small-data.md`, `steps/5-2-interview.md`, `steps/5-3-learn.md` |

## Conventions

How a solo + AI team runs a design — where the design log lives, who decides, how each stage works with subagents and role cards, and how a design ends — is in `conventions/design-log.md`. The design log template is `conventions/design-backlog-template.md`. These are working conventions, not source text: follow what fits, override what doesn't, and note why.

## Use Protocol

1. If the ideo-kernel skill is not loaded yet, invoke `ideo-scrum:ideo-kernel` first — every stage stands on it.
2. Work in the design log — `scrum/design-<suffix>/DesignBacklog.md`, started from the template. Read the conventions whenever you open, run, or resume a design, or answer a question about how to do any of these, even roughly: convention 5 says how to open one, convention 24 how to pick one up.
3. Identify the current stage. Keep to the stage order — Empathize, Define, Ideate, Prototype, Test — and go back when a later stage shows that an earlier answer was wrong.
4. Read the stage's source excerpts before running it, and treat them as source text. Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — the conventions say how a solo + AI team does that step, and the conventions apply.
5. Use the IDEO methods in every stage — first from the mode the stage maps to, but from any mode if it helps — following the ideo-kernel skill's Use Protocol.
6. The Product Owner decides at the end of each stage (`../scrum-kernel/overview.md`, *Product Owner decides between stages*), and on the rest of what convention 21 lists.
7. When the design questions are answered, the conclusions flow back to the product log (scrum-kernel skill) and to the Sprint that asked for the design (sprint-kernel skill); end the design as in convention 19.
