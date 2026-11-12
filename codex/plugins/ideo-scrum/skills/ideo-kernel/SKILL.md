---
name: ideo-kernel
description: "Use when the user mentions IDEO, the five modes, the IDEO five-stage method, design thinking, or a design-thinking method by name — load it before answering, even for a quick outline. The IDEO five-stage method is these five modes, not the design sprint: a run of their own is kept in an IDEO log. Load it also when a question asks what people want or what counts as good and has no ready answer — before anything else — to settle whether it needs a design sprint or the five modes (`conventions/ideo-log.md`). Also load it whenever a design stage or a stuck Sprint needs a method: it is the plugin's shared toolbox and the foundation of every stage, and every role loads it first. Covers the IDEO five modes (Empathize, Define, Ideate, Prototype, Test), human-centered design, user interviews, journey mapping, POV, HMW questions, brainstorming, user testing; rapid prototype validation — when an idea must be checked quickly with a prototype that feels like a prototype (fast, informal, never a formal result, built to learn rather than ship). A full design sprint, from a challenge to a tested prototype, is design-kernel."
---

# IDEO Kernel

> Source: the five-mode summaries and the method catalog come from the Stanford d.school Design Thinking Bootleg and IDEO's Design Guides; the surrounding text is the plugin author's.
> License: the d.school material is CC BY-NC-SA 4.0 (© Stanford d.school) — https://dschool.stanford.edu/tools/design-thinking-bootleg; the plugin's own text is MIT.

## The Shared Toolbox

This kernel is the plugin's shared toolbox and the foundation of every stage: the IDEO five modes and the method catalog. Every role loads it first. Each stage of a design (design-kernel skill) stands on one of the five modes, and a design must use the modes and methods in every stage (the rule is in the design-kernel skill's `SKILL.md`) — the design sprint's own techniques are added on top of these, not in place of them. A Scrum Sprint (sprint-kernel skill) uses the methods whenever the work calls for them — for example, when the team is stuck mid-Sprint.

*(Author's methodology design for solo + AI teams, 2026-11-08.)*

## Conventions

Whether a question needs a design sprint or the five modes, how the two relate, when to open an IDEO log, and how one ends are in `conventions/ideo-log.md`; the log template is `conventions/ideo-backlog-template.md`.

## IDEO design thinking

Design Thinking is a **human-centered approach to innovation** that integrates the needs of people, the possibilities of technology, and the requirements for business success. Originating from IDEO and formalized at Stanford's Hasso Plattner Institute of Design (the d.school, founded by David Kelley), it is an iterative, non-linear methodology for tackling complex, ill-defined problems. Its core ethos is **bias toward action** — learning by doing rather than analysis alone.

**Bias toward fast prototype validation.** The design work optimizes for speed of learning, not polish: a prototype must feel like a prototype — rough, quick, and disposable — built to learn, never a formal result. In a design sprint test, this describes how the prototype is made and treated — quickly, and thrown away after; the surface the tester sees should still appear real enough for honest reactions (design-kernel skill, `../design-kernel/steps/4-1-fake-it.md`).

IDEO's five-mode model:

| Mode | Focus | Key Action | Reference | Read when |
|---|---|---|---|---|
| **Empathize** | Understand users deeply | Observe, engage, immerse in users' lives to uncover real needs | `IDEO-modes/empathize.md` | When the user needs to understand people — observe, engage, immerse — to discover deep needs from human behavior and emotion |
| **Define** | Frame the right problem | Synthesize findings into a Point of View (user + need + insight) | `IDEO-modes/define.md` | When empathy findings are collected and a meaningful challenge needs framing — craft a Point of View (user + need + insight) |
| **Ideate** | Generate possibilities | Diverge — brainstorm radical alternatives beyond the obvious | `IDEO-modes/ideate.md` | When a POV is ready and a wide range of ideas is needed — diverge and explore, don't converge too early |
| **Prototype** | Make ideas tangible | Build low-cost artifacts to test; "build to think" | `IDEO-modes/prototype.md` | When selected ideas need low-cost prototypes — build, fail fast, iterate and learn; keep it fast and prototype-feeling — rough, quick, and disposable, built to learn, never a formal result; in a design sprint test, the surface the tester sees should still appear real (see above) |
| **Test** | Learn from users | Put prototypes in front of real users; iterate based on feedback | `IDEO-modes/test.md` | When prototypes are ready for user feedback — test in real contexts, continue learning about users |

The process is **not linear** — teams move back and forth between modes as insights emerge. Empathize and Ideate are divergent (opening up possibilities); Define and Prototype are convergent (narrowing toward solutions); Test feeds learning back into any mode.

---

## Method Catalog

Methods by mode — names only; the Trigger and the file for each are in the table below:

- **Empathize** (13): Assume a beginner's mindset; What? How? Why?; Interview Preparation; Interview for Empathy; Extreme Users; Story Share-and-Capture; Journey Map; Prototype for Empathy; Empathetic Data; Empathy Probe; Analogous Empathy; Shooting Video; Editing Video
- **Define** (13): What? How? Why?; Extreme Users; Story Share-and-Capture; Journey Map; Powers of Ten; 2x2 Matrix; Why-How Laddering; Point of View; Design Guidelines; How Might We Questions; Storytelling; Review Your Portfolio; Surprise-to-Insights Leap
- **Ideate** (13): Analogous Empathy; Powers of Ten; Why-How Laddering; Design Guidelines; How Might We Questions; Stoke; Brainstorming; Facilitate a brainstorm; Brainstorm selection; Impose Constraints; I Like, I Wish, What If; Describe Your Concept; Yes, And! Brainstorm
- **Prototype** (10): Prototype for Empathy; Brainstorm selection; Impose Constraints; Describe Your Concept; Improvise to Life; Scenes/Props/Roles; Prototype to Decide; Identify a Variable; User-Driven Prototyping; Wizard of Oz Prototyping
- **Test** (13): Empathetic Data; Shooting Video; Editing Video; Storytelling; Review Your Portfolio; I Like, I Wish, What If; Scenes/Props/Roles; Prototype to Decide; Identify a Variable; User-Driven Prototyping; Wizard of Oz Prototyping; Testing with Users; Feedback Capture Matrix

In the table, each method is listed once; **Modes** names the modes it serves.

| Method | Modes | Document | Trigger |
| --- | --- | --- | --- |
| Assume a beginner's mindset | Empathize | `methods/assume-beginners-mindset.md` | Use before interviews, observation, or source review when prior expertise may bias interpretation. |
| What? How? Why? | Empathize, Define | `methods/what-how-why.md` | Use when observations are too abstract or when the user gives conclusions without scene-level detail. |
| Interview Preparation | Empathize | `methods/interview-preparation.md` | Use before a scheduled or intercept interview. |
| Interview for Empathy | Empathize | `methods/interview-for-empathy.md` | Use when the work needs lived stories, choices, and behavior rather than opinions about a solution. |
| Extreme Users | Empathize, Define | `methods/extreme-users.md` | Use when average cases hide strong needs, constraints, or workarounds. |
| Story Share-and-Capture | Empathize, Define | `methods/story-share-and-capture.md` | Use after fieldwork to preserve stories before synthesis. |
| Journey Map | Empathize, Define | `methods/journey-map.md` | Use when the experience unfolds across time, roles, handoffs, or emotional shifts. |
| Prototype for Empathy | Empathize, Prototype | `methods/prototype-for-empathy.md` | Use when making something can reveal user behavior, emotion, or context. |
| Empathetic Data | Empathize, Test | `methods/empathetic-data.md` | Use when research or test material needs evidence separated from interpretation. |
| Empathy Probe | Empathize | `methods/empathy-probe.md` | Use when participants can capture lived evidence over time without you present. |
| Analogous Empathy | Empathize, Ideate | `methods/analogous-empathy.md` | Use when the direct domain is stuck and analogous human experiences may reveal patterns. |
| Shooting Video | Empathize, Test | `methods/shooting-video.md` | Use when video can preserve behavior, setting, emotion, or interaction evidence. |
| Editing Video | Empathize, Test | `methods/editing-video.md` | Use when video material must be turned into a shareable learning artifact. |
| Powers of Ten | Define, Ideate | `methods/powers-of-ten.md` | Use when the problem frame may be too narrow or too broad. |
| 2x2 Matrix | Define | `methods/two-by-two-matrix.md` | Use to compare observations, users, insights, or concepts along two meaningful dimensions. |
| Why-How Laddering | Define, Ideate | `methods/why-how-laddering.md` | Use to move between concrete needs and deeper purpose. |
| Point of View | Define | `methods/point-of-view.md` | Use only when user, need, and insight are grounded in empathy material. |
| Design Guidelines | Define, Ideate | `methods/design-guidelines.md` | Use when insights should become constraints for later ideation. |
| How Might We Questions | Define, Ideate | `methods/how-might-we-questions.md` | Use when a POV is ready to open an ideation space. |
| Storytelling | Define, Test | `methods/storytelling.md` | Use when others need to understand a user, problem, or prototype experience. |
| Review Your Portfolio | Define, Test | `methods/review-your-portfolio.md` | Use when multiple artifacts, prototypes, or evidence points need review. |
| Surprise-to-Insights Leap | Define | `methods/surprise-to-insights-leap.md` | Use when material contains surprise, contradiction, or unexpected behavior. |
| Stoke | Ideate | `methods/stoke.md` | Use before divergent work when energy is low or judgment is premature. |
| Brainstorming | Ideate | `methods/brainstorming.md` | Use after an HMW is clear and many varied ideas are needed. |
| Facilitate a brainstorm | Ideate | `methods/facilitate-a-brainstorm.md` | Use when a group needs structure, pace, and guardrails for ideation. |
| Brainstorm selection | Ideate, Prototype | `methods/brainstorm-selection.md` | Use after a pool of ideas exists and prototype candidates must be chosen. |
| Impose Constraints | Ideate, Prototype | `methods/impose-constraints.md` | Use when ideas are too broad or a prototype needs focus. |
| I Like, I Wish, What If | Ideate, Test | `methods/i-like-i-wish-what-if.md` | Use to gather constructive feedback while keeping possibility open. |
| Describe Your Concept | Ideate, Prototype | `methods/describe-your-concept.md` | Use when a concept must become clear enough to build, compare, or test. |
| Yes, And! Brainstorm | Ideate | `methods/yes-and-brainstorm.md` | Use when ideas are killed too early or need collaborative build-up. |
| Improvise to Life | Prototype | `methods/improvise-to-life.md` | Use when a service or interaction can be made tangible through enactment. |
| Scenes/Props/Roles | Prototype, Test | `methods/scenes-props-roles.md` | Use when testing an experience rather than a static artifact. |
| Prototype to Decide | Prototype, Test | `methods/prototype-to-decide.md` | Use when alternatives need concrete comparison. |
| Identify a Variable | Prototype, Test | `methods/identify-a-variable.md` | Use when a prototype or test tries to validate too many things at once. |
| User-Driven Prototyping | Prototype, Test | `methods/user-driven-prototyping.md` | Use when participant modification or assembly can reveal needs and preferences. |
| Wizard of Oz Prototyping | Prototype, Test | `methods/wizard-of-oz-prototyping.md` | Use when the visible experience can be simulated before the backend exists. |
| Testing with Users | Test | `methods/testing-with-users.md` | Use when a low-resolution prototype is ready for behavior-based user learning. |
| Feedback Capture Matrix | Test | `methods/feedback-capture-matrix.md` | Use after a test to structure feedback, questions, positives, and new ideas. |

---

## Use Protocol

1. Confirm the current mode, and the design or Sprint the work belongs to.
2. Prefer a method whose Modes include the current mode and whose trigger matches the current work. A method from another mode is fine when its trigger fits the work — say which mode it comes from and why.
3. Before using the method, read its document under `methods/`. Never invoke a method only by name — state which method you are using and why it fits the current mode.
4. Treat the `Cleaned Transcription` section as source text.
5. Treat `Use Before`, `Use Notes`, and `Do Not Use When` as project-specific notes, not source text.
6. When the work needs a full design — from a challenge to a tested prototype — use the design-kernel skill; when findings must become planned, executable work, hand off to the sprint-kernel skill.
