---
name: second-opinion
description: "Use only when the user runs /ideo-scrum:second-opinion: package one pending question, its constraints and the exact files to read, then hand them to a fresh read-only advisor and bring back its independent verdict. It never runs on its own and never forwards the earlier discussion — no draft opinions, no leanings, no summary of what was already said. Arguments: the question; the constraints; the file paths to read."
disable-model-invocation: true
argument-hint: "<question> | constraints: <...> | files: <paths> | model: <optional>"
---

# Second Opinion

The user asked for an independent second view. Your whole job is to hand a clean brief to a new `ideo-scrum:advisor` and bring its answer back unchanged. Everything that makes the opinion independent — a fresh context, no earlier leanings, only the originals — is decided here, before the call.

## 1. Package the question

From `$ARGUMENTS`, take only these things:

- **The question**: the decision that is still open, in one or two sentences, as the user put it.
- **The constraints**: what the user said the answer must respect.
- **The materials**: the exact paths the user named. Use those paths as given; do not rewrite their contents into the brief and do not add files the user did not name.
- **The model**, only if the user named one: written `model: <name>`, for example `model: opus`. Section 3 says what to do with it.

If the user named no materials, stop and ask which originals the advisor should read — an advisor without sources can only restate the question.

## 2. Keep the brief clean

- **Leave out everything said earlier in this conversation**: earlier drafts, your own opinion, the user's leanings, and any summary of the discussion so far. If you have already formed a view, it does not travel with the brief.
- Do not tell the advisor what answer is expected, which option is favoured, or that a previous answer existed.

## 3. Summon the advisor

Call the `Agent` tool:

- `subagent_type`: `"ideo-scrum:advisor"`
- A **new, ordinary instance**: never resume, continue or fork an earlier one.
- `prompt`: the question, the constraints, and the named paths — plus an instruction to read those files itself and answer from them. Nothing else.

**Model**: the advisor's definition asks for `fable`, which needs access on the user's account. If the user named another model for this call, pass it as the `model` parameter of the `Agent` call — for example `model: "opus"` — for this call only; do not change the session or any saved setting. If the host reports that `fable` is not available to the account, say so and ask which model to use; do not pick one yourself.

## 4. Deliver the answer honestly

- **Return the advisor's verdict with its evidence**, in its own terms. You may format it; you do not soften, extend or overrule it.
- **Say what you actually got.** If the call failed, or the advisor could not read a named file, report that plainly and stop — do not answer in its place.
- **Do not present the answer as a specific model's when that was not established.** The definition requests `fable`, but whether the host honoured that request is not something this entry can confirm on its own; if the user needs that guarantee, tell them it is unverified rather than implying it.
- **The decision stays with the user.** Close with the advisor's conclusion and its stated gaps, not with a recommendation of your own.

## Not for this entry

- A review of work already done, an outside Stakeholder view, or a routine design or Scrum question — those have their own entries.
- Reusing an earlier advisor answer instead of summoning a new instance.
