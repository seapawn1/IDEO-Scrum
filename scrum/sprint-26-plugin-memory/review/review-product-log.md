# 审阅：product-log.md（scrum-kernel）

每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。
读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。

本文件 18 条：改 4、留 14；另有 5 个非编号块（文末）。

---

### product-log#1 · One product log

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 26–26 行

**旧规矩原文**

> 1. **One product log** — Write the product log from the template (`overview.md`, convention 1). For an old project, write it from what already exists — the README, the open issues, the old plans — and leave the history in version control; what cannot be written yet follows convention 2.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 87bd0db fix(PBI-49): 照 Master 审停点 2 改七处——…overview 1 与 product-log 1 并成一处
- commit 0122f8e feat(PBI-31): 产品日志约定 product-log.md 与模板 product-backlog-template.md

**建议**：留；去处：清单（一行）

**理由**：overview#1 只说新老项目都从一份产品日志起步；本条另有老项目怎么写（从 README、未结 issue、旧计划起步，历史留在版本控制，写不出的按约定 2），并过去会丢。改为本条留在清单，overview#1 并入本条，破掉成环。

**与它重复或相邻**：overview#1

**新行**

```text
- **write-product-log** Write the product log from the template, usually the Scrum Master with the PO; for an old project, from its README, issues and old plans.
```

**备注**：The sentence 'what cannot be written yet follows the blank-page rule' is the blank-page line. overview#1 keeps the one-product-log rule.

---

### product-log#2 · Blank page

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 27–38 行

**旧规矩原文**

> 2. **Blank page** — Write into the product log what you can define; replace what you cannot with the matching item of a design, and let the design answer it. When the product and its Product Goal cannot be written, the IDEO methods alone will not make them clear; start from a design (design-kernel skill), which adds the design sprint, a prototype, and a test to those methods (the boundary between the design sprint and the five modes: `../ideo-kernel/conventions/ideo-log.md`, convention 1). The design's items stand in for the product log's like this:
>
>     | The design log | Product log |
>     | --- | --- |
>     | The challenge | 1.1 Product |
>     | The design goal | 1.2 Product Goal |
>     | The design questions, once the test has answered them | 1.3 Definition of Done (the Outcome Done measures); the ones not answered become items |
>     | The people at the top of the map | 2.1 Stakeholders |
>     | The map | 2.2 Map |
>     | The target (`../design-kernel/steps/2-3-pick-a-target.md`) | 3 Product Backlog Items, each placed on a step of the map |
>
>     In a section a design is answering, say which design answers it and link to it; do not copy the design log. The stakeholder table can be written first, because a design uses role cards from its first stage.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）
- archive scrum/documents/conventions-review-log.md 表第 1 行（约定 2 白纸）：「不说用 IDEO 弄清楚，改成做一次设计」

**建议**：留；去处：长文件

**理由**：写不出产品和目标时改做一次设计，是 PO 审约定时定的走向，要留；但六行映射表和「链接设计、不抄设计日志」是细则，应进长文件，清单只留一行索引。

**新行**（长文件 `product-log-details`）

```text
- **blank-page** If the product cannot be written yet, start from a design and let its conclusions fill the log. → long/product-log-details.md
```

**备注**：Long file: the six-row table (design log to product log), the IDEO methods alone not being enough, the stakeholder table written first because a design uses role cards from its first stage.

---

### product-log#3 · Facts first, then questions

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 39–39 行 · 标记：Supplement

**旧规矩原文**

> 3. **Facts first, then questions** — *Supplement.* Have the Scrum Master look up the facts itself; what the Product Owner must decide goes into one message, numbered, each question with a recommended answer.

**出处与依据**：补充（把握：低）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：*Supplement* 只标来源，不等于可删；「SM 自己查事实、PO 要定的合成一条编号消息、每问带建议答案」是一条行为规矩，别处没有，应在清单留一行（source 仍为补充、confidence 低）。

**新行**

```text
- **facts-then-questions** [sm] *Supplement.* Look up facts yourself; ask the PO in one numbered message, each with a recommended answer.
```

**备注**：Kept with its Supplement label: inferred by the assistant, never confirmed in practice. The PO decides whether it stays.

---

### product-log#4 · Product and Product Goal

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 43–43 行

**旧规矩原文**

> 4. **Product and Product Goal** — Keep the product statement in section 1.1 and the Product Goal in section 1.2, each in its own one-row commitment table as the template shows (`overview.md`, *Goal fixed, plan flexible*); the vision line is optional. The product log has no Now or Waiting for PO line: it has no stage; those lines belong to the Sprint, design, and IDEO logs.

**出处与依据**：作者（把握：低）；种类：格式
- commit 1e347b4 feat(Sprint 18): H2 交付 PBI-66 日志读取接口、目标引用与工作块完成标记（git -S 最早命中，与本条内容关系弱）
- archive scrum/documents/sprint/sprint-10-conventions.md 第 174 行：Product Goal 这次不定，1.2 不动

**建议**：改；去处：清单（一行）

**理由**：模板 product-backlog-template.md 第 8-20 行已有一行承诺表和可选 Vision 行，格式部分可归模板；但「产品日志没有阶段、不写 Now 或 Waiting for PO 行，那些行属于 Sprint、设计、IDEO 日志」在模板里没有明说，约定又会被删，应改成清单一行留下。

**新行**

```text
- **product-log-header** Keep the product statement (1.1) and Product Goal (1.2) each in a one-row commitment table; no Now line.
```

**备注**：The optional vision line is dropped from the list (the template has it).

---

### product-log#5 · Two kinds of Done

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 44–44 行

**旧规矩原文**

> 5. **Two kinds of Done** — Outcome Done is evidence of value the product delivers to its stakeholders; Output Done is the quality standard for the whole Increment. The full Definition of Done stays in section 1.3. A Sprint chooses where to focus its checks, not which standards apply. Write standards precisely and keep only requirements that hold across the product, not ones that merely came up this time. Put item-specific or tentative requirements in the item’s acceptance criteria instead.

**出处与依据**：作者（把握：低）；种类：规矩
- source plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-increment.md：「The Definition of Output Done is the overall quality standard for the whole Increment, not the specific standard for each item」
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：改；去处：清单（一行）

**理由**：Outcome Done 与 Output Done 的定义可删（原文见 plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-increment.md 第 37 行）；但「完整 DoD 留在 1.3、Sprint 只选检查重点而不改适用标准」以及「标准写准确、只留跨产品的要求、单条要求进验收标准」都是规矩，要合成清单一行保留。

**新行**

```text
- **dod-in-product-log** Keep the full Definition of Done in 1.3; a Sprint picks where to focus checks, never which standards apply.
- **dod-standards** Write standards precisely; keep only what holds across the product, the rest goes in acceptance criteria.
```

**别处已有**：The two definitions (Outcome Done, Output Done) are in plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-increment.md.

---

### product-log#6 · Stakeholders in a short table

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 45–45 行

**旧规矩原文**

> 6. **Stakeholders in a short table** — List the stakeholders in section 2.1 in a short table, not a long profile per person. A Stakeholder subagent gets one row as its identity, and the AI fills in the details. If the table is empty, ask the Product Owner who belongs in it, and add the rows.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：短表而非人物简介、表空时问 PO，直接影响 Stakeholder 子代理的身份来源，Memory 里需要。

**新行**

```text
- **stakeholder-table** [sm] List stakeholders in 2.1, one row each; a Stakeholder subagent gets one row; if empty, ask the PO.
```

---

### product-log#7 · Architecture as a map

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 46–46 行

**旧规矩原文**

> 7. **Architecture as a map** — Start section 2.2 with one map, drawn as `../design-kernel/steps/2-1-make-a-map.md` describes: actors on top, AI roles included, the ending at the bottom, five to fifteen steps between, as a Mermaid `flowchart TD`. Add a subsection only for a step that needs more words.

**出处与依据**：作者（把握：中）；种类：格式
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：改；去处：清单（一行）

**理由**：地图画法大部分已在模板 product-backlog-template.md 第 47 行（actors 在上、结尾在下、五到十五步、flowchart TD、按需加小节），但「AI 角色也算进 actor」只在原条里，删了就丢；且 steps/2-1 说的是 actors 在左、结尾在右，不能替代。改成清单一行保留 AI 角色这一句，其余照模板。

**新行**

```text
- **architecture-map** Start 2.2 with one Mermaid flowchart TD map: actors on top, the ending at the bottom, five to fifteen steps.
```

**备注**：The verifier found that steps/2-1 draws actors on the left and the ending on the right, so this line cannot just point there. 'Add a subsection only for a step that needs more words' is dropped as detail.

---

### product-log#8 · No TBD

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 47–47 行

**旧规矩原文**

> 8. **No TBD** — Turn an unclear point into an item; a Sprint or a design works it out.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/conventions-review-log.md 表第 1 行（约定 2 白纸）：「不写 TBD，免得和约定 8 冲突」
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：不留 TBD、把不清楚的点变成条目，是一句话的规矩，在 PO 审约定时保留过。

**新行**

```text
- **no-tbd** Turn an unclear point into an item; a Sprint or a design works it out.
```

---

### product-log#9 · Technical design stays out

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 48–48 行

**旧规矩原文**

> 9. **Technical design stays out** — Keep technical design out: modules and interfaces are the Developer's; they live in the Increment.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：一句话划清界线：模块与接口归 Developer、不进产品日志，是 Memory 里需要的边界。

**新行**

```text
- **no-technical-design** Keep technical design out of the product log; modules and interfaces live in the Increment.
```

---

### product-log#10 · Seven columns

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 52–62 行 · 标记：quote

**旧规矩原文**

> 10. **Seven columns**
>
>     | Column | What goes in it |
>     | --- | --- |
>     | # | PBI- and three digits, counting up: PBI-001, PBI-002, and so on |
>     | Title | A short name |
>     | User story | "As <someone from section 2.1>, I want …, so that …" |
>     | Place | A step of the map, or a subsection of section 2.2 |
>     | Status | Where the item stands: waiting, in Sprint NN, in a design |
>     | Size | S — one or two sessions; M — three to five sessions; L — more than five sessions, to be split when refining |
>     | Notes | Source, open points, draft acceptance criteria, refinement notes |

**出处与依据**：作者（把握：高）；种类：格式
- commit 63d7c82 feat(PBI-32): 四个角色命令跟上约定；scrum-kernel SKILL.md 加约定短表；PBI 编号与冲刺日志 2.1 的写法

**建议**：留；去处：长文件

**理由**：七列的定义只在原文；product-backlog-template.md 第 51–56 行只有列名与 PBI 编号提示，没有用户故事句式、Place/Status 取值、Size 的 S/M/L 界线与 Notes 内容，删了会丢。改为进长文件，清单留索引。

**新行**（长文件 `product-log-details`）

```text
- **item-columns** An item has seven columns: #, Title, User story, Place, Status, Size, Notes. → long/product-log-details.md
```

**备注**：The table is kept word for word in the long file: the template has only the column names.

---

### product-log#11 · Numbers, not ranks

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 63–63 行

**旧规矩原文**

> 11. **Numbers, not ranks** — Number items to count them, and keep every number unique; ranking is another matter — moving an item up the list — and the Product Owner does it when an order is needed.

**出处与依据**：作者（把握：高）；种类：规矩
- archive scrum/documents/conventions-review-log.md 表第 3 行（约定 11 编号不是排名）：「编号必须唯一、排名即往上提」
- archive scrum/documents/sprint/sprint-11-conventions-review.md 表：product-log 3「成立：编号唯一，排名是往上挪」

**建议**：留；去处：清单（一行）

**理由**：编号唯一、排名归 PO，PO 审约定时确认过，是 Memory 里需要的一行。

**新行**

```text
- **numbers-not-ranks** Number items only to count them, every number unique; the PO ranks when an order is needed.
```

---

### product-log#12 · Items with the Scrum Master

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 64–64 行 · 标记：Departs

**旧规矩原文**

> 12. **Items with the Scrum Master** — Let the Product Owner decide the items together with the Scrum Master, who serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded. At Planning the Product Owner leads the selection, and the Scrum Master and the Developer say when it is too much or too little; the measure is the Sprint Goal, and the check when the rows are written is `../sprint-kernel/conventions/sprint-log.md`, convention 5. This departs from the Scrum Guide: see the Departures section of `overview.md`.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/conventions-review-log.md 第 53 行：「Product Owner 与 Scrum Master 一起定条目」
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：这是对官方指南的偏离（条文自标 Departs from the Scrum Guide，偏离表里已有对应行），PO 与 Master 一起定条目是我方选择，需要留在 Memory 里。

**新行**

```text
- **items-with-sm** [sm,po] The PO decides the items with the Scrum Master; the Scrum Master and Developer say when it is too much.
```

**备注**：A departure from the Scrum Guide (the Developers select the items); the departure is in the departures long file. The check when the rows are written is the sprint line select-items.

---

### product-log#13 · Status lives here

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 65–65 行

**旧规矩原文**

> 13. **Status lives here** — Write an item's status in the product log only; a sprint log names items by number.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：状态只写产品日志、冲刺日志只引编号，避免两处不一致，是一句话的规矩。

**新行**

```text
- **status-lives-here** An item's status lives in the product log only; a sprint log names items by number.
```

---

### product-log#14 · Refine any time, finish in the Sprint

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 69–69 行

**旧规矩原文**

> 14. **Refine any time, finish in the Sprint** — Refine in the product log only to add detail; finish the refinement in the sprint log's section 2.2 (`../sprint-kernel/conventions/sprint-log.md`, convention 6). The product log has no refinement section.

**出处与依据**：作者（把握：低）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：产品日志里只补细节、精化在冲刺日志 2.2 完成，属于流程归属，不算格式；把握不高，因为条文里有指路成分。

**新行**

```text
- **refine-in-sprint** In the product log only add detail; finish refinement in the sprint log's 2.2.
```

**备注**：Low confidence in the annotation: part of the original is signposting.

---

### product-log#15 · Seven steps

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 70–70 行

**旧规矩原文**

> 15. **Seven steps** — Refine one item at a time in the seven steps of `../sprint-kernel/conventions/sprint-log.md`, convention 6. Acceptance criteria already written in full here are not repeated in the sprint log.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：改；去处：清单（一行）

**理由**：前半只是指向 sprint-log 约定 6 的指路，删掉；后半「已在此写全的验收标准不在冲刺日志里重复」是规矩，保留并写成一行。

**新行**

```text
- **acceptance-written-once** Acceptance criteria already in the product log are not repeated in the sprint log.
```

**别处已有**：The seven steps themselves are in the sprint-refinement long file.

---

### product-log#16 · Where refined content goes

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 71–71 行

**旧规矩原文**

> 16. **Where refined content goes** — Put refined content where it belongs: a split-off item becomes a new row; long design content goes into the architecture, and the Place column points to it; short notes go into Notes; large material goes into `scrum/documents/` (`overview.md`, convention 5), referenced from Notes.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）

**建议**：留；去处：清单（一行）

**理由**：精化内容放哪（新行、架构、Notes、scrum/documents）是给 Master 的落点规矩，Memory 里留一行即可。

**新行**

```text
- **where-refined-content** Split-off items are new rows; long design content goes in 2.2, notes in Notes, big files in scrum/documents/.
```

---

### product-log#17 · Fresh at every Review

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 75–75 行

**旧规矩原文**

> 17. **Fresh at every Review** — At every Review, move done items to section 3.2, one line each, with the source, usually the archived sprint log in `scrum/documents/`; delete outdated architecture text and resolved open points — what counts as outdated is `../sprint-kernel/conventions/sprint-log.md`, convention 17; send unfinished items back to section 3.1. Keep no revision record; version control keeps the history. Fresh means more than the items: the Review keeps the rest of `scrum/` fresh too (`../sprint-kernel/conventions/sprint-log.md`, convention 17).

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）
- commit cbed055 docs(Sprint 14): 收官——Review、产品日志保鲜、Retro，发版 v5.2.0

**建议**：留；去处：清单（一行）

**理由**：每次 Review 把完成的条目移到 3.2、未完成的退回 3.1，是收官动作，Sprint 14 收官时定下；留一行。

**新行**

```text
- **fresh-at-review** At each Review move done items to 3.2, send unfinished ones back to 3.1, delete outdated text; keep no revision record.
```

**备注**：'Fresh means more than the items: the Review keeps the rest of scrum/ fresh too' goes with the Review rule in the sprint-closing long file.

---

### product-log#18 · Goal fixed, plan flexible

`plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md` 第 79–79 行

**旧规矩原文**

> 18. **Goal fixed, plan flexible** — Refine items and acceptance criteria at any time; let only the Product Owner change the Product Goal, and only on evidence against it. Write an item's change and its reason in its Notes, and a Product Goal change with its date and reason in section 1.2 (`overview.md`, convention 17).

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md——三层、文件与文档文件夹、角色、会话分工、约定本身、目标不变
- archive scrum/documents/sprint/sprint-10-conventions.md 第 174 行：Product Goal 这次不定，PO 说以后可能要重构，1.2 不动

**建议**：留；去处：清单（一行）

**理由**：与 overview 17 同讲「目标固定、其余可变」，但本条给出产品日志的落点：条目改动与理由进 Notes、Product Goal 改动与日期理由进 1.2；overview 17（overview.md 第 103–105 行）没有写出这些落点，故保留本条，清单一行。

**与它重复或相邻**：overview#17

**新行**

```text
- **product-log-changes** Write item changes in Notes; a Product Goal change goes in 1.2 with date and reason, and needs evidence against the old one.
```

**备注**：overview#17 covers 'only the PO changes a commitment'; this line adds where the changes are written and the evidence condition.

---

## 非编号块（引言、署名、图、表）

### product-log@1 · quote（第 3–3 行）

> > Working conventions: reference, not law — follow what fits, override what doesn't, note why. Source labels and short names are explained in convention 15 of `overview.md`, in the skill folder, beside `SKILL.md`. A convention with no label is the author's practice.

**新**：不进清单。去处或不要的理由：The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes.

---

### product-log@2 · quote（第 5–6 行）

> > Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland), marked where they appear.
> > License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland).

**新**：不进清单。去处或不要的理由：long/goal-fixed.md carries the Scrum Guide quotations with their Source and License lines.

---

### product-log@3 · paragraph（第 8–8 行）

> The product log is the first layer. Its template is `product-backlog-template.md`; the Scrum Master usually writes it with the Product Owner. Paths starting with `../` are relative to the scrum-kernel skill folder.

**新**：不进清单。去处或不要的理由：The line write-product-log (the template; the Scrum Master usually writes the product log with the PO).

---

### product-log@4 · fence:mermaid（第 10–20 行）

> ```mermaid
> flowchart TD
>     A["Starting<br/>conventions 1–3"] --> B["Each part<br/>conventions 4–9"]
>     A -- "the product cannot be written yet" --> D["A design answers it (design-kernel skill)"]
>     D -- "conclusions flow back" --> B
>     B --> C["Items<br/>conventions 10–13"]
>     C --> E["Refinement<br/>conventions 14–16"]
>     E --> C
>     C -- "each Review" --> F["Keeping it fresh<br/>convention 17"]
>     F --> C
> ```

**新**：不进清单。去处或不要的理由：Drawn in long/flow-maps.md, with the handles in the boxes; the list line flow-maps points there.

---

### product-log@5 · paragraph（第 22–22 行）

> Convention 18 holds at every step; see Throughout, below.

**新**：不进清单。去处或不要的理由：Dropped: a pointer to 'Throughout', which the numbering of the old file made.

---
