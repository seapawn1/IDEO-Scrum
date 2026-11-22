# 审阅：overview.md（scrum-kernel）

每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。
读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。

本文件 17 条：改 10、留 7；另有 7 个非编号块（文末）。

---

### overview#1 · One product log

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 48–48 行

**旧规矩原文**

> 1. **One product log** — Start every project, new or old, from one product log.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 87bd0db fix(PBI-49)：overview 1 与 product-log 1 并成一处
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：⑦ 做了（product-log 1：老项目怎么写）

**建议**：留；去处：清单（一行）

**理由**：product-log#1 也声明并入本条，两条互指成环，且它标为不进 Memory；本条留作清单一行（每个项目，无论新旧，都从一份产品日志起步），product-log#1 的模板写法与老项目写法并入本条的说明里。

**与它重复或相邻**：product-log#1

**新行**

```text
- **one-product-log** Start every project, new or old, from one product log.
```

**备注**：product-log#1 keeps the how-to-write half as its own line (the verifiers found they are a split of rule and practice, not duplicates).

---

### overview#2 · Sprints and designs side by side

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 49–49 行 · 标记：Departs

**旧规矩原文**

> 2. **Sprints and designs side by side** — Treat Sprints and designs as peers under the product log: a Sprint, the Developer's, delivers an Increment; a design, the Designer's, delivers a prototype and conclusions. Open a design when an item needs design, when Sprint refinement hits a hard point, or for a blank page (`conventions/product-log.md`, convention 2); it is not part of a Sprint. Whether a question needs a design sprint or the five modes is `../ideo-kernel/conventions/ideo-log.md`, convention 1. Decide item by item whether design is needed; a design's conclusions still land through a Sprint; an Increment need not be code — the Definition of Done says what it is. This departs from the Scrum Guide: see Departures.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39)：overview 约定总览首次写入，三层与设计并列
- archive scrum/documents/sprint/sprint-08-design-kernel.md：设计内核独立，与冲刺并列

**建议**：改；去处：长文件

**理由**：Departures 表（overview.md:114）只覆盖设计不交付 Increment、可跨 Sprint、Designer 与 Developer 并列；开设计的三种时机（product-log.md:27-38）、设计不属于 Sprint、逐项决定、Increment 不必是代码、结论经冲刺落地都要保留，取舍见 ideo-log.md:22。细则多，放长文件。

**新行**（长文件 `layers-and-folders`）

```text
- **designs-beside-sprints** A design sits beside a Sprint, not in it: open one for an item that needs design. → long/layers-and-folders.md
```

**备注**：Long file must also carry: decide item by item; a design's conclusions still land through a Sprint; an Increment need not be code. The departure itself is in the departures long file.

---

### overview#3 · Three layers

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 50–60 行

**旧规矩原文**

> 3. **Three layers**
>
>    | Layer | File | Commitment | Accountable | Facilitates |
>    | --- | --- | --- | --- | --- |
>    | 1 | Product log | Product Goal | Product Owner, with the Scrum Master | — |
>    | 2 | Sprint log | Sprint Goal | Developer | Scrum Master |
>    | 2 | Design log | Design goal | Designer | Scrum Master |
>    | 3 | Increment: code or documents, as the Definition of Done says | Definition of Done | Developer | — |
>    | 3 | Prototype: built to learn, never in an Increment; a design’s prototype stays with its design evidence | Design questions | Designer | — |
>
>    The third layer is not a log and has no prescribed method; it relies on the skills of whoever does the work. Increments add up into the product. The design’s conclusions flow back; its working material, including the prototype, stays with the design and can be referenced by the Sprint that builds those conclusions (`../design-kernel/conventions/design-log.md`, convention 19). The standalone IDEO log has its own rule (`../ideo-kernel/conventions/ideo-log.md`, convention 4).

**出处与依据**：作者（把握：中）；种类：格式
- commit 9c9bd67 feat(PBI-39)：overview 三层表首次写入
- archive scrum/documents/sprint/sprint-10-conventions.md：约定总览谁做什么（角色表）

**建议**：改；去处：长文件

**理由**：三层表是框架图，属长文件内容，清单只留一行索引。改法：表保留；末段「The third layer is not a log…」与指向 design-log 19、ideo-log 4 的条号去掉，改成相对链接。

**新行**（长文件 `layers-and-folders`）

```text
- **three-layers** Product log, then a sprint or design log, then the Increment or prototype. → long/layers-and-folders.md
```

**备注**：The table and the closing paragraph go to the long file; the convention numbers in the paragraph become handles.

---

### overview#4 · Folders

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 61–61 行

**旧规矩原文**

> 4. **Folders** — `scrum/` holds all of the Scrum work: `ProductBacklog.md`; `ScrumBoard.html`, the board written from the logs, which keeps no state of its own (`conventions/board-log.md`); `sprint-NN-<suffix>/` with `SprintBacklog.md` and its working files; `design-<suffix>/`, unnumbered, with `DesignBacklog.md`, prototypes, and other working material; `ideo-<suffix>/`, unnumbered, with `IdeoBacklog.md`, prototypes, and working files; and `documents/` (convention 5). The active folders may still hold work that ended and is awaiting Review; read the log’s `Now` before resuming. This is the author’s layout; use your project’s own places if it has them.

**出处与依据**：作者（把握：中）；种类：格式
- commit 9c9bd67 feat(PBI-39)：overview 文件与文档文件夹一节首次写入
- archive scrum/documents/sprint/sprint-10-conventions.md：文档文件夹的位置要 PO 定（Supplement 段）

**建议**：留；去处：长文件

**理由**：这是本仓库的目录布局，写在长文件里；清单只留一行索引。末句「use your project's own places」保留，它是给其他项目用的。

**与它重复或相邻**：overview#5

**新行**（长文件 `layers-and-folders`）

```text
- **scrum-folders** All Scrum work lives under scrum/; use your project's own places if it has them. → long/layers-and-folders.md
```

---

### overview#5 · Where files go

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 62–62 行

**旧规矩原文**

> 5. **Where files go** — A file that serves only one log usually stays in its working folder and can be cleaned up when that work ends. The design’s original working material is the exception: retain it with the design, then move it with its log into the existing `scrum/documents/` archive at Review (`../design-kernel/conventions/design-log.md`, convention 19; `../sprint-kernel/conventions/sprint-log.md`, convention 17). Files serving the whole Scrum also go into `scrum/documents/`, and the logs reference them. A project can use its existing archive subfolders. The project’s own documentation, such as a user manual or API notes, stays where the project keeps it, such as `docs/` at the root.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 8d4ca85 docs(Sprint 17)：收官——Review（冲刺日志归档）
- archive scrum/documents/sprint/sprint-17-conventions-rewrite.md：Review 收官时冲刺日志归档进 scrum/documents/sprint/

**建议**：改；去处：长文件

**理由**：保留全部行为要求：只服务一份日志的文件留在工作文件夹、用完可清；设计原件是例外，随设计保留并在 Review 随日志移入 scrum/documents/；服务整个 Scrum 的文件进 scrum/documents/ 并由日志引用；项目可用已有归档子文件夹；项目自己的文档留在原处。细则多，放长文件。

**与它重复或相邻**：overview#6

**新行**（长文件 `layers-and-folders`）

```text
- **where-files-go** One log's files stay in its folder; design originals and shared files go to scrum/documents/. → long/layers-and-folders.md
```

---

### overview#6 · Working material

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 63–63 行

**旧规矩原文**

> 6. **Working material** — Keep working material out of the log itself; link to the retained design originals as convention 5 says. Key material of general use can go into the project’s memory or instructions, and a large important file goes into `scrum/documents/`. Retro lessons go only where `../sprint-kernel/conventions/sprint-log.md`, convention 18, says, never in instructions.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39)：overview 工作材料一条首次写入
- archive AGENTS.md：Retro 只写记忆

**建议**：改；去处：清单（一行）

**理由**：工作材料不进日志、链接归档原件；通用的关键材料可进项目记忆或指令；重要大文件进 scrum/documents/（overview.md:63 的这两句必须保留）；Retro 教训末句改为指向 sprint-log.md:72 的 convention 18。

**与它重复或相邻**：overview#5、sprint-log#18

**新行**

```text
- **working-material** Keep working material out of the log and link to it; key general material may go to project memory, Retro lessons only there.
```

**备注**：The Retro half repeats what the retro line says; kept short here on purpose.

---

### overview#7 · Names

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 64–69 行

**旧规矩原文**

> 7. **Names** — The terms used in all the conventions are defined here once:
>    - the **product log** is the Product Backlog, kept in `ProductBacklog.md`; the **sprint log** is the Sprint Backlog, kept in `SprintBacklog.md`; the **design log** is kept in `DesignBacklog.md` — a file made from a template takes these names, whatever the template is called;
>    - an **IDEO log** is the log of a run of the five modes, kept in `IdeoBacklog.md`;
>    - a **product backlog item (PBI)** is one row of the product log's item table;
>    - a **role card** is one row of the product log's stakeholder table;
>    - a **fresh subagent** starts from its brief alone; a fork of a session, or a copy of one, does not count. When the tool has no subagents, a new session given only the brief is the equivalent.

**出处与依据**：作者（把握：中）；种类：说明
- commit 9c9bd67 feat(PBI-39)：overview 名词一节首次写入
- archive scrum/documents/sprint/sprint-10-conventions.md：要一张术语表（go-ahead、PBI、DoD、SGEP、role card）

**建议**：改；去处：长文件

**理由**：词条定义留在插件内的 Memory 长文件，不能移到插件包外的 docs/glossary.md（marketplace 只发 ./plugins/ideo-scrum，该目录无 docs）；fresh subagent 一句进清单一行；「模板文件一律用这些名字」的命名要求也保留。

**新行**（长文件 `names`）

```text
- **names** Use the plugin's own terms (product log, sprint log, design log, IDEO log, PBI, role card) as defined. → long/names.md
- **fresh-subagent** A fresh subagent starts from its brief alone; a fork or copy of a session does not count.
```

**备注**：The definitions stay inside the plugin (a long file), not in docs/glossary.md: the marketplace ships only plugins/ideo-scrum, which has no docs.

---

### overview#8 · Roles

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 73–85 行

**旧规矩原文**

> 8. **Roles** — On a Claude Code role command, invoke the kernels in the order shown before doing any role work.
>
>    | Role | Home turf | Accountable for | Claude Code entry kernels, in order |
>    | --- | --- | --- | --- |
>    | Product Owner | The product log and its handoffs | Value direction; the Product Goal and Sprint Goals; which items enter a Sprint; the go-ahead; the items, decided with the Scrum Master; stage results and permissions to start or return (convention 12) | — (a person) |
>    | Scrum Master | Sprint logs and design logs | Facilitating Planning and refinement; recording; tracking; reviewing the How and the Increment; serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded | ideo → scrum → sprint → design |
>    | Developer | The Sprint | The sprint log, the How, the Increment; the last check that nothing in refinement is unclear | ideo → scrum → sprint |
>    | Designer | The design | Ideas, prototypes, and tests for a design, from Ideate on (the Product Owner and the Scrum Master settle its research and definition); conclusions back to the product log and the Sprint that asked | ideo → scrum → design |
>    | Stakeholder | An outside view, or standing non-source chores | Looking as one row of the product log's stakeholder table; a PO assistant organizes logs, summarizes progress, relays settled work and maintains the board, but does not rank, decide, review or edit plugin files | ideo → scrum |
>
>    In Claude Code, use the Skill tool one at a time, wait for success, and skip only calls already successful in this conversation. Stop and report a failed load rather than substituting a file read. In DSH, native role entries instead preload ideo and scrum in order, then load sprint and design as needed for the work. Subagents a role dispatches load the ideo-kernel and scrum-kernel skills too.
>
>    The Product Owner, the Scrum Master, and the Developer keep the sprint log together; without a Developer, the Product Owner and the Scrum Master run the Sprint alone.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39)：overview 角色表首次写入
- commit 9ed7d6d feat: PBI-20 角色重定义——只有 PO 必须是人，SM 派活与审阅
- archive scrum/documents/sprint/sprint-10-conventions.md：谁做什么，角色表

**建议**：改；去处：长文件

**理由**：角色表与加载细则放长文件，清单一行写角色命令按序加载内核；overview.md:85 末句（PO、SM、Developer 共同维护冲刺日志，无 Developer 时 PO 与 SM 两人跑冲刺）也要收进长文件，不能只留在被删的 overview。

**新行**（长文件 `roles-and-routing`）

```text
- **role-entry** On a role command, load that role's kernels in order before any work; stop and report a failed load. → long/roles-and-routing.md
```

**备注**：Long file: the role table, the DSH variant, the subagent rule, and the last sentence (the PO, the Scrum Master and the Developer keep the sprint log together; without a Developer the other two run the Sprint). Sprint 27 changes the table (Supporter role); sync later.

---

### overview#9 · Only the Product Owner must be human

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 86–86 行 · 标记：Departs

**旧规矩原文**

> 9. **Only the Product Owner must be human** — The other roles may all be AI. This departs from the Scrum Guide Expansion Pack: see Departures.

**出处与依据**：作者（把握：高）；种类：规矩
- source plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md：「The Product Owner must be human.」
- commit 9ed7d6d feat: PBI-20 角色重定义——只有 PO 必须是人
- archive scrum/documents/sprint/sprint-10-conventions.md：「只有 PO 必须是人」那段改成一句，指向总览

**建议**：留；去处：清单（一行）

**理由**：这是本插件与 SGEP 的主要偏离（SGEP 原文要求 PO 与 SM 都必须是人），Departures 表已有同一条，清单必留一行，理由写在 Departures 表。

**新行**

```text
- **only-po-human** Only the Product Owner must be human; the other roles may all be AI.
```

---

### overview#10 · Ask the Product Owner

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 87–87 行

**旧规矩原文**

> 10. **Ask the Product Owner** — Whoever is unsure asks the Product Owner, unless the Product Owner has sent that kind of question elsewhere.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（当时在 conventions/overview.md，第 9 条标 Author's practice）
- archive scrum/documents/sprint/sprint-10-conventions.md：谁做什么一节写「拿不准就问 PO」

**建议**：留；去处：清单（一行）

**理由**：拿不准就问 PO 是每个角色都要守的规矩；它是通用版，sprint-log#25 只是冲刺里的具体问法，两条不冲突，保留本条。

**与它重复或相邻**：sprint-log#25

**新行**

```text
- **ask-the-po** Whoever is unsure asks the PO, unless the PO sent that kind of question elsewhere.
```

**备注**：Sprint 27 adds where each kind of question goes (a three-step routing); add that line when syncing.

---

### overview#11 · Product Owner as Developer

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 88–88 行

**旧规矩原文**

> 11. **Product Owner as Developer** — When the Product Owner builds, they take part as a Developer, and the How is worked out with them.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（第 10 条 Author's practice，引 Scrum Guide 原句）
- source plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-2020.md：「they participate as Developers」

**建议**：留；去处：清单（一行）

**理由**：PO 亲自施工时以 Developer 身份参与、How 与 PO 商量，是会影响日常分工的行为规矩；引文出自 Scrum Guide 2020，保留原句。

**新行**

```text
- **po-as-developer** When the PO builds, they take part as a Developer and the How is worked out with them.
```

---

### overview#12 · Product Owner decides between stages

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 89–89 行

**旧规矩原文**

> 12. **Product Owner decides between stages** — The Product Owner settles each stage’s result. Before starting or returning to a stage of a Sprint or a design sprint, wait for explicit permission for that stage and scope. Approving a result is not permission to move on, though one message can say both clearly. While waiting, record the result or why a return is needed, but do not start or delegate that stage’s work. A new session may resume the same stage within its recorded permission and scope; earlier permission does not carry over to a return. The Scrum Master acts for the Product Owner only within a written handover covering the particular decision; handing over a review or a choice inside a stage does not hand over a stage transition. Record who decided, the date and basis, and the stage and scope authorized, including the written handover if used. Keep the decision at the end of its stage chapter; if permission arrives later, add that dated decision without replacing the earlier one. Record first entry when opening the log. These are stage decisions, not reviews, formal acceptance, or approval of each step. Sprint decisions: `../sprint-kernel/conventions/sprint-log.md`, convention 24; design decisions: `../design-kernel/conventions/design-log.md`, convention 26.

**出处与依据**：作者（把握：中）；种类：规矩
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/delegated-choice-not-gate.md：「方案还没经 PO 确认，是我越过了关卡」
- archive scrum/documents/sprint/sprint-23-log-rules.md：PO 原话「可以，我觉得23、25可以结束 what，然后去放行到 how。」
- commit 9734304 docs(Sprint 23): H10 落源 18 份已审稿（此提交起出现「Approving a result is not permission to move on」）

**建议**：留；去处：长文件

**理由**：sprint-log#24（sprint-log.md:95）与 design-log#26（design-log.md:80-90）只是回指本条，没有重述等待时只记录不动手、批准结果不等于放行、新会话只在已记录范围内续做、早先许可不带回返、SM 只在覆盖该具体决定的书面交接下代 PO 决定、记录谁决定/日期/依据/范围、后到许可另加不替换等要求；本条含多条行为要求，全文收入长文件，清单留一行索引。

**与它重复或相邻**：sprint-log#24、design-log#26

**新行**（长文件 `stage-gates`）

```text
- **stage-gates** Wait for the PO's explicit permission to start or return to a stage; approving a result is not permission. → long/stage-gates.md
```

**备注**：The whole rule goes to the long file: record the result while waiting but do not start or delegate; a new session resumes only inside the recorded scope; earlier permission does not carry over to a return; record who, when, basis, stage and scope; a later permission is added, not replaced; these are stage decisions, not reviews.

---

### overview#13 · One Scrum Master per project

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 93–93 行

**旧规矩原文**

> 13. **One Scrum Master per project** — Each project has one session as its Scrum Master, leading its Developer, Designer, and Stakeholders. A session above several projects only summarizes; each project's facts stay in its own logs.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（第 11 条 Author's practice）
- archive scrum/documents/sprint/sprint-10-conventions.md：约定分组里列出「会话分工」

**建议**：留；去处：清单（一行）

**理由**：每个项目只有一个 Scrum Master 会话，决定了谁带 Developer 和 Stakeholder，是会话分工的基础；保留，一行即可。依据只到 Sprint 10 的归档，PO 可再确认。

**新行**

```text
- **one-scrum-master** One Scrum Master session per project leads its other roles; a session above several projects only summarizes.
```

**备注**：The annotation says the basis reaches only Sprint 10's archive; the PO may want to confirm.

---

### overview#14 · Who gets which work

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 94–94 行

**旧规矩原文**

> 14. **Who gets which work** — Reviewing the work goes to the Scrum Master by default (`../sprint-kernel/conventions/sprint-log.md`, convention 14); when the Developer works in another session or tool, `../sprint-kernel/conventions/sprint-log.md`, convention 26, says how the two work together. Long-running upkeep — the board, summaries, tracking — goes to a standing Stakeholder session with a working identity the project writes down, such as PO assistant. That assistant relays only what the Product Owner or Scrum Master already decided; scope or item changes and go-aheads go through the Scrum Master, who chooses the receiving session. It does not rank, decide, review or edit plugin files; an independent outside view still comes from a fresh subagent. A small edit to one or two files the Scrum Master makes itself. Building goes to a new Developer session when a paragraph can brief it, or to a Developer that shares the Scrum Master's context when the work needs much of the discussion; such a Developer cannot review its own work.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（第 12 条 Author's practice，当时是一张分工表）
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/master-helper-division.md：「Master 做判断和决定，费 token 的活（发散、原型、测试、落盘）交给辅助会话」

**建议**：改；去处：长文件

**理由**：审阅（sprint-log.md:65 第14条）与长期维护（commands/stakeholder.md:34）各有去处，但「SM 自己做一两份文件的小改」和「施工交给新 Developer 会话，或交给共享 SM 上下文的 Developer，后者不能审自己的活」别处都没有；sprint-log#26（sprint-log.md:97）只讲跨会话协作，不含这套分工；全文收入长文件，清单留一行索引。 Sprint 27 正把「PO assistant」改成 Supporter 并加三级分流，合入后要照它同步。

**与它重复或相邻**：sprint-log#26

**新行**（长文件 `roles-and-routing`）

```text
- **who-gets-which-work** The Scrum Master reviews; a standing helper does upkeep; a Developer builds and never reviews its own work. → long/roles-and-routing.md
```

**备注**：Long file keeps all five assignments: review, the other-session or other-tool Developer, upkeep, the Scrum Master's own small edit, and building. The words PO assistant are gone; Sprint 27 replaces them with the Supporter and adds the question routing: sync later.

---

### overview#15 · Working conventions

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 98–98 行 · 标记：Supplement、Decide on the spot

**旧规矩原文**

> 15. **Working conventions** — Reference, not law. Each convention has a short name, for use in conversation, and only the exceptions carry a source label: a convention with no label is the author's practice — how the author works; **Supplement** — inferred by the author's assistant, not yet confirmed in practice; **Decide on the spot** — no fixed rule, decide when it comes up. When you override a convention, write what you did and why in the log's notes: the sprint log's Increment notes, or the chapter of the design log it concerns. The templates carry the flow; the convention files say how, and when a step may be skipped. They describe roles and steps, not the mechanics of any tool.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（第 13 条 Author's practice，写明标签与短名）
- archive scrum/documents/sprint/sprint-10-conventions.md：约定本身一节写「约定本身：标签与短名」

**建议**：改；去处：清单（一行）

**理由**：标签定义（无标签即作者做法、Supplement、Decide on the spot）压成一行留清单；但「覆盖约定时在日志里写下做了什么与为什么（冲刺日志 Increment notes 或设计日志相应章）」是行为要求，必须一起保留；「reference, not law」等背景句可删。

**新行**

```text
- **rule-labels** No label: the author's practice; *Supplement*: inferred, unconfirmed; *Decide on the spot*: no fixed rule.
```

**备注**：Dropped as background: reference, not law; the templates carry the flow; no tool mechanics.

---

### overview#16 · Templates record outputs

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 99–99 行

**旧规矩原文**

> 16. **Templates record outputs** — A template's chapters follow the flow, and its sections hold only what each step produced; how to do a step belongs in the conventions. A log made from a template keeps all of the template's headings, including the chapters filled in later, and adds no sections of its own; put work remarks in the sprint log’s Increment notes or the relevant design chapter. An optional explanation below a commitment table belongs in the commitment’s own section (convention 17).

**出处与依据**：作者（把握：中）；种类：格式
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（第 15 条 Author's practice）
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/template-structure.md：「模板的章按流程分，节只放产出」

**建议**：改；去处：清单（一行）

**理由**：标题保留、不加节、工作备注位置的具体要求在 sprint-backlog-template.md:7、ideo-backlog-template.md:7、design-log.md:76（第22条）；但「模板的章按流程、节只放产出、做法归约定」只在此条与作者私人记忆（S:/SeaPawn-Memory/.../template-structure.md），私人记忆不能作为删除依据，应留清单一行或先写进模板约定。

**新行**

```text
- **templates-record-outputs** Keep every template heading and add none; sections hold only what each step produced.
```

**备注**：The optional explanation under a commitment table is covered by goal-fixed.

---

### overview#17 · Goal fixed, plan flexible

`plugins/ideo-scrum/skills/scrum-kernel/overview.md` 第 103–105 行 · 标记：quote、CJK

**旧规矩原文**

> 17. **Goal fixed, plan flexible** — Each log has one fixed commitment: the Product Goal, the Sprint Goal, the design goal; the Definition of Done is not weakened either. Everything under a commitment — items, refinement points, acceptance criteria, the How, the chosen design solution — may change as you learn, and each log records what changed and why. Only the Product Owner changes a commitment, and only the Product Owner cancels a Sprint whose goal can no longer be met.
>     Keep the product statement in the product log's section 1.1, the Product Goal in its section 1.2, the Sprint Goal in the sprint log's section 1.1, and the design goal in the design log's section 1.2. Each has one one-row table: the first cell is `Commitment` (`承诺` in a Chinese log), the second is the exact text, without bold. Keep one copy, not another at the file’s top; its section heading identifies it. The table is the only source of the current commitment. Optional reasons can follow below it; they are not part of the commitment or what a reader extracts from the table. Exact text on a stage decision line is a snapshot of the commitment at that time, not a second source; do not update it when the current goal changes. Give each goal one short name and keep using that name. An IDEO log has no commitment of its own: its For field points to the log it serves.
>     The Scrum Guide says it this way. On the Product Goal: "They must fulfill (or abandon) one objective before taking on the next." During the Sprint: "No changes are made that would endanger the Sprint Goal", "Quality does not decrease", and "Scope may be clarified and renegotiated with the Product Owner as more is learned." And: "Only the Product Owner has the authority to cancel the Sprint."

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（第 16 条 Author's practice，引 Scrum Guide 原句）
- commit ccd8257 feat(PBI-37): 设计日志开设计与接手——Open a design、Now 一行、Resume from the header、目标不变其余可调

**建议**：改；去处：长文件

**理由**：只有 PO 改承诺、其余随学习可变并记变动这一核心保留，全文归长文件、清单留一行索引；章节位置与承诺表格式确在 product-backlog-template.md:10/17、sprint-backlog-template.md:13、design-backlog-template.md:21 与 board-log.md:26，但「只留一份、标题即标识」「表是当前承诺的唯一来源」「给每个目标一个短名并一直沿用」别处没有，必须随全文留下；Scrum Guide 三段引文逐字保留。

**新行**（长文件 `goal-fixed`）

```text
- **goal-fixed** Each log's commitment (a Goal, the Definition of Done) stays fixed; the plan under it may change. → long/goal-fixed.md
- **po-owns-commitments** Only the PO changes a commitment or cancels a Sprint whose goal can no longer be met.
- **commitment-table** Keep each commitment in a one-row table, the only source of it. → long/goal-fixed.md
```

**备注**：Long file carries the Scrum Guide quotations word for word with Source and License. The commitment-table line is relied on by the commitments hook, the board and the check script. sprint-log#20 adds: acceptance criteria may be renegotiated with the PO or the Scrum Master, changes and reasons go in the Increment notes. design-log#25 adds: sharpen the design goal during Empathize, then only the PO changes it.

---

## 非编号块（引言、署名、图、表）

### overview@1 · quote（第 3–3 行）

> > These are working conventions — the author's reading of Scrum and design thinking for solo + AI teams. They are less precise than the official guides. Use them as reference: follow what fits, override what doesn't, and note why. Where a convention departs from the official guide on purpose, the Departures section says so and gives the reason.

**新**：不进清单。去处或不要的理由：The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes.

---

### overview@2 · quote（第 5–6 行）

> > Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland) and the Scrum Guide Expansion Pack v2026.1 (Ralph Jocham, John Coleman, Jeff Sutherland), marked where they appear; the rest is the author's working conventions.
> > License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland; © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland).

**新**：不进清单。去处或不要的理由：The Source and License lines are at the top of each long file that quotes a guide (departures, goal-fixed, sprint-stages); ATTRIBUTION.md holds the registry.

---

### overview@3 · paragraph（第 8–8 行）

> Source labels and short names are explained in convention 15.

**新**：不进清单。去处或不要的理由：The line rule-labels explains the labels; the pointer to a convention number goes with the numbers.

---

### overview@4 · paragraph（第 10–10 行）

> The other files: `conventions/product-log.md` and `conventions/product-backlog-template.md`; `../sprint-kernel/conventions/sprint-log.md` and `../sprint-kernel/conventions/sprint-backlog-template.md`; for designs, `../design-kernel/conventions/design-log.md` and `../design-kernel/conventions/design-backlog-template.md`; for the five modes, `../ideo-kernel/conventions/ideo-log.md` and `../ideo-kernel/conventions/ideo-backlog-template.md` (paths are relative to the scrum-kernel skill folder, where this file sits beside `SKILL.md`; the Sprint files belong to the sprint-kernel skill, the design files to the design-kernel skill, the IDEO files to the ideo-kernel skill — read them when you open or resume a design, a Sprint, or a run of the five modes).

**新**：不进清单。去处或不要的理由：A pointer list to the other convention files and templates; the sections and long files of MEMORY.md replace it. The templates stay in their skills' conventions/ folders.

---

### overview@5 · fence:mermaid（第 14–42 行）

> ```mermaid
> flowchart TD
>     PO["Product Owner"]
>     SM["Scrum Master"]
>     DEV["Developer"]
>     DES["Designer"]
>     SH["Stakeholders"]
>     PO --> A["Write the product log: product, architecture, items<br/>product-log.md"]
>     SM --> A
>     A -- "an item needs design" --> X0["A design question: design sprint or the five modes?<br/>ideo-log.md"]
>     BP["A blank page<br/>product-log.md"] -- "PO authorizes Empathize" --> X
>     A -- "PO authorizes Why" --> S1["Why: the Sprint Goal<br/>sprint-log.md"]
>     S1 -- "PO authorizes What" --> S2["What: the items, refined<br/>sprint-log.md"]
>     S2 -- "refinement hits a hard point" --> X0
>     S2 -- "PO authorizes How" --> S3["How: a plan<br/>sprint-log.md"]
>     S3 -- "PO gives the go-ahead" --> S4["Increment: build, with notes<br/>sprint-log.md"]
>     DEV --> S4
>     S4 -- "PO authorizes Test" --> S5["Test: tests, review, PO acceptance when required<br/>sprint-log.md"]
>     S5 -. "PO authorizes a return to building" .-> S4
>     S5 -- "PO decides: close" --> V["Close: Review (archive the logs, refresh the product log) and Retro<br/>sprint-log.md"]
>     DES --> X
>     SH --> X
>     SH --> V
>     X0 -- "PO authorizes starting a design sprint" --> X["Design sprint: five stages, each standing on one IDEO mode<br/>design-log.md"]
>     X0 -- "the five modes" --> X2["The five modes: one or two methods, recorded in the log they serve;<br/>or an IDEO log for a run of its own<br/>ideo-log.md"]
>     X -- "conclusions flow back — a blank page's design fills the product log" --> A
>     X2 -- "conclusions flow back" --> A
>     V --> E["End: Sprint Goal met, Increment delivered, Product Goal one step closer"]
> ```

**新行**（长文件 `flow-maps`）

```text
- **flow-maps** Process maps of the whole flow and of each log, with the lines that apply at each step. → long/flow-maps.md
```

---

### overview@6 · paragraph（第 109–109 行）

> Each departure is stated here once, with its reason; the convention named in the last column points back to this table.

**新**：不进清单。去处或不要的理由：In long/departures.md, as its intro.

---

### overview@7 · table（第 111–119 行）

> | Here | The official guide | Why | See |
> | --- | --- | --- | --- |
> | Only the Product Owner must be human | SGEP: the Product Owner and the Scrum Master "must be human", and "At least one Product Developer should be human" | One person works with AI and keeps the value decisions | Convention 9 |
> | Designs sit beside Sprints | Scrum Guide: all the work "happen within Sprints" | A design delivers no Increment, may span several Sprints, and the Designer and the Developer are peers | Convention 2 |
> | The Product Owner decides the items with the Scrum Master | Scrum Guide: "the Developers select items from the Product Backlog" | The Product Owner sets the value direction, and the others say how much fits | `conventions/product-log.md`, convention 12 |
> | The How is a plan, and building waits for the go-ahead | Scrum Guide: how to build is "at the sole discretion of the Developers" | The Scrum Master and the Product Owner check the plan, because AI may drift | `../sprint-kernel/conventions/sprint-log.md`, conventions 7 and 8 |
> | Checkpoints replace the Daily Scrum | Scrum Guide: the Daily Scrum is "a 15-minute event for the Developers" | AI works by session, not by day | `../sprint-kernel/conventions/sprint-log.md`, convention 10 |
> | A reviewer is required | Scrum Guide: the Developers are accountable for "Instilling quality by adhering to a Definition of Done" | A Developer may drift, and a second look catches it | `../sprint-kernel/conventions/sprint-log.md`, convention 14 |
> | No Sprint end date | Scrum Guide: Sprints are "fixed length events of one month or less" | AI works by session, so the Product Owner watches at checkpoints for a Sprint that drags on | `../sprint-kernel/conventions/sprint-log.md`, convention 2 |

**新行**（长文件 `departures`）

```text
- **departures** The plugin departs from the Scrum Guide on purpose in seven places, each with its reason. → long/departures.md
```

---
