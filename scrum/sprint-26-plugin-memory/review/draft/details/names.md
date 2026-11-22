# Names

The plugin's own terms, defined once. Read this file when a rule uses a term and you are not sure what it names, when you write a file from a template (a file made from a template takes these names, whatever the template is called), or when you override a rule. The list lines that point here are `names`, `rule-labels` and `templates-record-outputs`.

## Logs and their files

| Term | What it is | Kept in |
| --- | --- | --- |
| product log | The Product Backlog | `ProductBacklog.md` |
| sprint log | The Sprint Backlog | `SprintBacklog.md` |
| design log | The log of one design | `DesignBacklog.md` |
| IDEO log | The log of a run of the five modes | `IdeoBacklog.md` |

## Parts of the product log

- A **product backlog item (PBI)** is one row of the product log's item table.
- A **role card** is one row of the product log's stakeholder table.

## Subagents

- A **fresh subagent** starts from its brief alone; a fork of a session, or a copy of one, does not count. When the tool has no subagents, a new session given only the brief is the equivalent.

## Two things with five names (`modes-are-not-the-sprint`)

- The five modes and the design sprint's five stages share five names and are two different things. What a user calls "the IDEO five-stage method" is the five modes themselves, not the design sprint.

## Labels, templates and overriding (`rule-labels`, `templates-record-outputs`)

- The rules are reference, not law. Each has a short name (its handle in the list), for use in conversation, and only the exceptions carry a source label: a rule with no label is the author's practice — how the author works; **Supplement** — inferred by the author's assistant, not yet confirmed in practice; **Decide on the spot** — no fixed rule, decide when it comes up.
- When you override a rule, write what you did and why in the log's notes: the sprint log's Increment notes, or the chapter of the design log it concerns.
- The templates carry the flow; the rules say how, and when a step may be skipped. They describe roles and steps, not the mechanics of any tool.
- A template's chapters follow the flow, and its sections hold only what each step produced; how to do a step belongs in the rules, not in the template.
- A log made from a template keeps all of the template's headings, including the chapters filled in later, and adds no sections of its own; put work remarks in the sprint log's Increment notes or the relevant design chapter.
- An optional explanation below a commitment table belongs in the commitment's own section (`commitment-table`).

## Open points for the Product Owner

- The definitions stay inside the plugin (here), not in `docs/glossary.md`: the marketplace ships only `plugins/ideo-scrum`, which has no `docs/`. The glossary can keep its longer, bilingual version for readers of the repository.
