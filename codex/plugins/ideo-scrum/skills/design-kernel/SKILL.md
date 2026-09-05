---
name: design-kernel
description: "Use when applying Design Thinking or a Design Sprint — Empathize, Define, Ideate, Prototype, Test; human-centered design, user interviews, journey mapping, POV, HMW questions, brainstorming, user testing; rapid prototype validation — when an idea must be checked quickly with a prototype that feels like a prototype (fast, informal, never a formal result, built to learn rather than ship); and when a challenge is still undefined and needs pre-research before any execution. The Design Sprint here is a fast research sprint — lock the target quickly, finish the design fast, clarify whether the problem is solvable and what the basic approach is — and its findings pave the way for, then hand off to, the scrum-kernel Sprint."
---

# Design Kernel

## IDEO design thinking

Design Thinking is a **human-centered approach to innovation** that integrates the needs of people, the possibilities of technology, and the requirements for business success. Originating from IDEO and formalized at Stanford's Hasso Plattner Institute of Design (the d.school, founded by David Kelley), it is an iterative, non-linear methodology for tackling complex, ill-defined problems. Its core ethos is **bias toward action** — learning by doing rather than analysis alone.

**Bias toward fast prototype validation.** The design work optimizes for speed of learning, not polish: a prototype must feel like a prototype — rough, quick, and disposable — built to learn, never a formal result.

IDEO's five-mode model:

| Mode | Focus | Key Action | Reference | Read when |
|---|---|---|---|---|
| **Empathize** | Understand users deeply | Observe, engage, immerse in users' lives to uncover real needs | `IDEO-modes/empathize.md` | When the user needs to understand people — observe, engage, immerse — to discover deep needs from human behavior and emotion |
| **Define** | Frame the right problem | Synthesize findings into a Point of View (user + need + insight) | `IDEO-modes/define.md` | When empathy findings are collected and a meaningful challenge needs framing — craft a Point of View (user + need + insight) |
| **Ideate** | Generate possibilities | Diverge — brainstorm radical alternatives beyond the obvious | `IDEO-modes/ideate.md` | When a POV is ready and a wide range of ideas is needed — diverge and explore, don't converge too early |
| **Prototype** | Make ideas tangible | Build low-cost artifacts to test; "build to think" | `IDEO-modes/prototype.md` | When selected ideas need low-cost prototypes — build, fail fast, iterate and learn; keep it fast and prototype-feeling — rough, quick, and disposable, built to learn, never a formal result |
| **Test** | Learn from users | Put prototypes in front of real users; iterate based on feedback | `IDEO-modes/test.md` | When prototypes are ready for user feedback — test in real contexts, continue learning about users |

The process is **not linear** — teams move back and forth between modes as insights emerge. Empathize and Ideate are divergent (opening up possibilities); Define and Prototype are convergent (narrowing toward solutions); Test feeds learning back into any mode.

## Design Sprint

A fast, structured sprint for the design side: lock the target quickly, finish the design fast, clarify whether the problem is solvable and what the basic approach looks like — the outcome paves the way for the scrum-kernel Sprint that follows. Five stages, no day-by-day script: move as fast as the work allows. Beyond the five stages, prototyping and testing ride on the Prototype and Test modes and the methods catalog above.

*(Author's methodology design for solo + AI teams, 2026-08; stage steps adapted from Knapp, Zeratsky & Kowitz, _Sprint_ (2016), cited per file.)*

| File | Purpose | Read when |
|---|---|---|
| `IDEO-modes/define-the-challenge.md` | What makes a challenge sprint-worthy (high stakes, deadline, stuck) and how to size it — solve the surface first | Stage 1 — Challenge; also the entry point when starting a design sprint |
| `IDEO-modes/start-at-the-end.md` | Set the long-term goal (optimistic) and list sprint questions (pessimistic) — assumptions turned into answerable questions | Stage 2 — Goal and Questions |
| `IDEO-modes/ask-the-experts.md` | One-at-a-time expert interviews (strategy, customer voice, how things work, previous efforts) with a five-step script | Stage 3 — Ask the Experts / deep research |
| `IDEO-modes/make-a-map.md` | Draw the map: actors on the left, ending on the right, words and arrows in between — five to fifteen steps | Stage 4 — Map |
| `IDEO-modes/pick-a-target.md` | Choose the most important customer and the critical moment of their experience; align the target with sprint questions | Stage 5 — Target |

| Stage | Steps |
|---|---|
| **Challenge** | Define the big challenge for this sprint. Use a sprint when the stakes are high, when there's not enough time, or when you're just plain stuck. Full method: `IDEO-modes/define-the-challenge.md` |
| **Goal and Questions** | Set a long-term goal — get optimistic: why are we doing this project, where do we want to be? Then list sprint questions — get pessimistic: how could we fail? Turn fears into questions this sprint can answer. Full method: `IDEO-modes/start-at-the-end.md` |
| **Ask the Experts** | One-at-a-time interviews with your team, your company, and outside specialists; revise goal, questions, and map as you learn. Full method: `IDEO-modes/ask-the-experts.md` |
| **Map** | List customers and key players on the left; draw the ending, with the completed goal, on the right; words and arrows in between — keep it to five to fifteen steps. Full method: `IDEO-modes/make-a-map.md` |
| **Target** | Choose the most important customer and the critical moment of their experience — the Product Owner makes the call. Full rationale: `IDEO-modes/pick-a-target.md` |

<small>这五个阶段都是为了快速明确背景、快速定义问题、缩小范围用的。These five stages exist to quickly clarify the background, define the problem, and narrow the scope.</small>

---

## Method Catalog

### Empathize

| Method | Document | Trigger |
| --- | --- | --- |
| Assume a beginner's mindset | `methods/assume-beginners-mindset.md` | Use before interviews, observation, or source review when prior expertise may bias interpretation. |
| What? How? Why? | `methods/what-how-why.md` | Use when observations are too abstract or when the user gives conclusions without scene-level detail. |
| Interview Preparation | `methods/interview-preparation.md` | Use before a scheduled or intercept interview. |
| Interview for Empathy | `methods/interview-for-empathy.md` | Use when the work needs lived stories, choices, and behavior rather than opinions about a solution. |
| Extreme Users | `methods/extreme-users.md` | Use when average cases hide strong needs, constraints, or workarounds. |
| Story Share-and-Capture | `methods/story-share-and-capture.md` | Use after fieldwork to preserve stories before synthesis. |
| Journey Map | `methods/journey-map.md` | Use when the experience unfolds across time, roles, handoffs, or emotional shifts. |
| Prototype for Empathy | `methods/prototype-for-empathy.md` | Use when making something can reveal user behavior, emotion, or context. |
| Empathetic Data | `methods/empathetic-data.md` | Use when research or test material needs evidence separated from interpretation. |
| Empathy Probe | `methods/empathy-probe.md` | Use when participants can capture lived evidence over time without you present. |
| Analogous Empathy | `methods/analogous-empathy.md` | Use when the direct domain is stuck and analogous human experiences may reveal patterns. |
| Shooting Video | `methods/shooting-video.md` | Use when video can preserve behavior, setting, emotion, or interaction evidence. |
| Editing Video | `methods/editing-video.md` | Use when video material must be turned into a shareable learning artifact. |

### Define

| Method | Document | Trigger |
| --- | --- | --- |
| What? How? Why? | `methods/what-how-why.md` | Use when observations are too abstract or when the user gives conclusions without scene-level detail. |
| Extreme Users | `methods/extreme-users.md` | Use when average cases hide strong needs, constraints, or workarounds. |
| Story Share-and-Capture | `methods/story-share-and-capture.md` | Use after fieldwork to preserve stories before synthesis. |
| Journey Map | `methods/journey-map.md` | Use when the experience unfolds across time, roles, handoffs, or emotional shifts. |
| Powers of Ten | `methods/powers-of-ten.md` | Use when the problem frame may be too narrow or too broad. |
| 2x2 Matrix | `methods/two-by-two-matrix.md` | Use to compare observations, users, insights, or concepts along two meaningful dimensions. |
| Why-How Laddering | `methods/why-how-laddering.md` | Use to move between concrete needs and deeper purpose. |
| Point of View | `methods/point-of-view.md` | Use only when user, need, and insight are grounded in empathy material. |
| Design Guidelines | `methods/design-guidelines.md` | Use when insights should become constraints for later ideation. |
| How Might We Questions | `methods/how-might-we-questions.md` | Use when a POV is ready to open an ideation space. |
| Storytelling | `methods/storytelling.md` | Use when others need to understand a user, problem, or prototype experience. |
| Review Your Portfolio | `methods/review-your-portfolio.md` | Use when multiple artifacts, prototypes, or evidence points need review. |
| Surprise-to-Insights Leap | `methods/surprise-to-insights-leap.md` | Use when material contains surprise, contradiction, or unexpected behavior. |

### Ideate

| Method | Document | Trigger |
| --- | --- | --- |
| Powers of Ten | `methods/powers-of-ten.md` | Use when the problem frame may be too narrow or too broad. |
| Why-How Laddering | `methods/why-how-laddering.md` | Use to move between concrete needs and deeper purpose. |
| Design Guidelines | `methods/design-guidelines.md` | Use when insights should become constraints for later ideation. |
| How Might We Questions | `methods/how-might-we-questions.md` | Use when a POV is ready to open an ideation space. |
| Stoke | `methods/stoke.md` | Use before divergent work when energy is low or judgment is premature. |
| Brainstorming | `methods/brainstorming.md` | Use after an HMW is clear and many varied ideas are needed. |
| Facilitate a brainstorm | `methods/facilitate-a-brainstorm.md` | Use when a group needs structure, pace, and guardrails for ideation. |
| Brainstorm selection | `methods/brainstorm-selection.md` | Use after a pool of ideas exists and prototype candidates must be chosen. |
| Impose Constraints | `methods/impose-constraints.md` | Use when ideas are too broad or a prototype needs focus. |
| I Like, I Wish, What If | `methods/i-like-i-wish-what-if.md` | Use to gather constructive feedback while keeping possibility open. |
| Describe Your Concept | `methods/describe-your-concept.md` | Use when a concept must become clear enough to build, compare, or test. |
| Yes, And! Brainstorm | `methods/yes-and-brainstorm.md` | Use when ideas are killed too early or need collaborative build-up. |
| Analogous Empathy | `methods/analogous-empathy.md` | Use when the direct domain is stuck and analogous human experiences may reveal patterns. |

### Prototype

| Method | Document | Trigger |
| --- | --- | --- |
| Brainstorm selection | `methods/brainstorm-selection.md` | Use after a pool of ideas exists and prototype candidates must be chosen. |
| Impose Constraints | `methods/impose-constraints.md` | Use when ideas are too broad or a prototype needs focus. |
| Prototype for Empathy | `methods/prototype-for-empathy.md` | Use when making something can reveal user behavior, emotion, or context. |
| Improvise to Life | `methods/improvise-to-life.md` | Use when a service or interaction can be made tangible through enactment. |
| Scenes/Props/Roles | `methods/scenes-props-roles.md` | Use when testing an experience rather than a static artifact. |
| Prototype to Decide | `methods/prototype-to-decide.md` | Use when alternatives need concrete comparison. |
| Identify a Variable | `methods/identify-a-variable.md` | Use when a prototype or test tries to validate too many things at once. |
| User-Driven Prototyping | `methods/user-driven-prototyping.md` | Use when participant modification or assembly can reveal needs and preferences. |
| Wizard of Oz Prototyping | `methods/wizard-of-oz-prototyping.md` | Use when the visible experience can be simulated before the backend exists. |
| Describe Your Concept | `methods/describe-your-concept.md` | Use when a concept must become clear enough to build, compare, or test. |

### Test

| Method | Document | Trigger |
| --- | --- | --- |
| Scenes/Props/Roles | `methods/scenes-props-roles.md` | Use when testing an experience rather than a static artifact. |
| Testing with Users | `methods/testing-with-users.md` | Use when a low-resolution prototype is ready for behavior-based user learning. |
| Prototype to Decide | `methods/prototype-to-decide.md` | Use when alternatives need concrete comparison. |
| Identify a Variable | `methods/identify-a-variable.md` | Use when a prototype or test tries to validate too many things at once. |
| User-Driven Prototyping | `methods/user-driven-prototyping.md` | Use when participant modification or assembly can reveal needs and preferences. |
| Wizard of Oz Prototyping | `methods/wizard-of-oz-prototyping.md` | Use when the visible experience can be simulated before the backend exists. |
| Feedback Capture Matrix | `methods/feedback-capture-matrix.md` | Use after a test to structure feedback, questions, positives, and new ideas. |
| Storytelling | `methods/storytelling.md` | Use when others need to understand a user, problem, or prototype experience. |
| I Like, I Wish, What If | `methods/i-like-i-wish-what-if.md` | Use to gather constructive feedback while keeping possibility open. |
| Empathetic Data | `methods/empathetic-data.md` | Use when research or test material needs evidence separated from interpretation. |
| Review Your Portfolio | `methods/review-your-portfolio.md` | Use when multiple artifacts, prototypes, or evidence points need review. |
| Shooting Video | `methods/shooting-video.md` | Use when video can preserve behavior, setting, emotion, or interaction evidence. |
| Editing Video | `methods/editing-video.md` | Use when video material must be turned into a shareable learning artifact. |

---

## Use Protocol

1. Confirm the current mode or the active docs.
2. Choose a method only if the trigger matches the current work.
3. Before using the method, read its document under `methods/`. Never invoke a method only by name — state which method you are using and why it fits the current mode.
4. Treat the `Cleaned Transcription` section as source text.
5. Treat `Use Before`, `Use Notes`, and `Do Not Use When` as project-specific notes, not source text.
6. When research concludes and findings must become planned, executable work, hand off to the scrum-kernel skill.
