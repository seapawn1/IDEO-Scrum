---
name: design-kernel
description: "Use when the user mentions a design sprint or asks to open a design — \"run a design sprint\", \"open a design for this\", \"this needs designing before we build\" — works in a design log (DesignBacklog), or has an undefined challenge that needs a pre-study before any Sprint. Load it before answering, even for a quick outline: the design sprint here differs from the common five-day version, so answer from this skill, not from memory. A design is a research module beside the Sprint, from a challenge to a tested prototype and conclusions — not code, API, or UI design work. Five stages, not five days: Empathize (challenge, design goal, design questions, ask the experts), Define (map, How Might We), Ideate (sketch solutions, choose one, storyboard), Prototype, Test. Built on the ideo-kernel skill, the plugin's shared toolbox; for IDEO, design thinking, or one named method alone, use ideo-kernel."
---

# Design Kernel

A design answers a hard question before the team builds: it starts from a challenge and ends with a tested prototype and conclusions. It is a module beside the Sprint, not inside it; the rule and the reason are in `../scrum-kernel/overview.md`, convention 2. The method is the design sprint from Knapp, Zeratsky & Kowitz, _Sprint_ (2016), regrouped under the five IDEO stages. The book runs the sprint Monday to Friday with a team in one room; here the stages run as fast as the work allows, not by day. Day names, clock times, and timers left in the source text are the book's schedule, not an instruction. The source text keeps the book's terms: its long-term goal is the design goal here, its sprint questions are the design questions, its Decider is the Product Owner, and its Facilitator is the Scrum Master.

Each stage maps to an IDEO mode. The mode's guide and its methods live in the ideo-kernel skill, the plugin's shared toolbox, and are not repeated here — read the mode file named in the table when you need them.

**IDEO methods are always in play.** The book's methods excerpted here are added so the design sprint runs as one piece; they do not limit what you use. In any stage, use any method from the ideo-kernel toolbox whenever the work needs it — for example, Interview for Empathy while asking the experts, or Brainstorming and Analogous Empathy while ideating — even where the book prefers a different technique.

*(Author's methodology design for solo + AI teams, 2026-11-08; source excerpts are cited per file.)*

## Five Stages

| Stage | IDEO mode (ideo-kernel) | What happens | Source excerpts |
| --- | --- | --- | --- |
| **Empathize** | `../ideo-kernel/IDEO-modes/empathize.md` | Write the challenge, the design goal, and the design questions; ask the experts and research when needed, after drafting a rough map (it lives in Define). The focus is the people: start from the people concerned and give every finding its source (conventions 9, 23) | `empathize/define-the-challenge.md`, `empathize/start-at-the-end.md`, `empathize/ask-the-experts.md` |
| **Define** | `../ideo-kernel/IDEO-modes/define.md` | Make a map; turn what you learned into a Point of View (user, need, insight) and How Might We questions. The focus is framing the problem, not drawing a flow. No target step: the design is already the target; if it is too wide, split it out (conventions 10, 24) | `define/make-a-map.md`, `define/how-might-we.md` |
| **Ideate** | `../ideo-kernel/IDEO-modes/ideate.md` | Diverge first, then converge to one solution the Product Owner chooses, with the ideo-kernel's Ideate methods as well as the book's steps: fill an idea pool and gather existing ideas; each person sketches one solution alone; decide; rumble if two winners conflict; storyboard the winner if it helps (here: conventions 7, 11–15, 25) | `ideate/remix-and-improve.md`, `ideate/sketch.md`, `ideate/decide.md`, `ideate/rumble.md`, `ideate/storyboard.md` |
| **Prototype** | `../ideo-kernel/IDEO-modes/prototype.md` | Adopt the prototype mindset and build a realistic facade of the chosen solution (and its storyboard, if there is one) — just enough to learn; divide the work, stitch it together, do a trial run. The focus is learning, not delivering: rough, quick, and thrown away after (convention 16) | `prototype/fake-it.md`, `prototype/prototype.md` |
| **Test** | `../ideo-kernel/IDEO-modes/test.md` | Interview the testers one at a time with the Five-Act Interview; watch together, look for patterns, and answer the design questions (here the testers are Stakeholders from the product log's stakeholder table, and the Product Owner: convention 17). The focus is learning from real reactions, and "we were wrong" is an answer (conventions 17, 26, 27) | `test/small-data.md`, `test/interview.md`, `test/learn.md` |

## Conventions

How a solo + AI team runs a design — where the design log lives, who decides, how each stage works with subagents and role cards, and how a design closes — is in `conventions/design-log.md`. The design log template is `conventions/design-backlog-template.md`. These are working conventions, not source text: follow what fits, override what doesn't, and note why.

## Use Protocol

1. If the ideo-kernel skill is not loaded yet, invoke `ideo-scrum:ideo-kernel` first — every stage stands on it.
2. Work in the design log — `scrum/design-<suffix>/DesignBacklog.md`, started from the template. Read the conventions whenever you open or resume a design: convention 3 says how to open one, convention 20 how to pick one up.
3. Identify the current stage. Keep to the stage order — Empathize, Define, Ideate, Prototype, Test — and go back when a later stage shows that an earlier answer was wrong.
4. Read the stage's source excerpts before running it, and treat them as source text. Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — the conventions say how a solo + AI team does that step, and the conventions apply.
5. Use the IDEO methods whenever the work needs them — first from the mode the stage maps to, but from any mode if it helps — following the ideo-kernel skill's Use Protocol.
6. The Product Owner decides the design goal, the chosen solution, and when the design is done.
7. When the design questions are answered, the conclusions flow back to the product log and to the Sprint that asked for the design (scrum-kernel skill); close the design as in conventions 18–19.
