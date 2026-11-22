# 审阅：sprint-log.md（sprint-kernel）

每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。
读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。

本文件 26 条：并 2、改 18、留 6；另有 5 个非编号块（文末）。

---

### sprint-log#1 · One branch, one folder

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 28–28 行

**旧规矩原文**

> 1. **One branch, one folder** — Give each Sprint one branch, with a separate working copy if wanted, and one folder, `scrum/sprint-NN-<suffix>/`: a two-digit number — the previous Sprint's plus one, starting at 01 — and a suffix saying what the Sprint is about. The folder's name is also the branch's name, and the tag's at close.

**出处与依据**：作者（把握：中）；种类：规矩
- commit be44889 feat(PBI-23): 冲刺日志约定 sprint-log.md 与模板 sprint-backlog-template.md
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 3 行头部：分支与 worktree 同名，一期一个文件夹

**建议**：留；去处：清单（一行）

**理由**：命名规则（两位编号、上一期加一、后缀、与分支同名、tag 随收官）在 Memory 一行写全；模板 sprint-backlog-template.md 第 3 行只记 Branch，没有目录或编号规则，目录布局见 overview.md 第 4 条（第 61 行）`sprint-NN-<suffix>/`，不能说「留模板」。

**新行**（长文件 `sprint-stages`）

```text
- **sprint-folder** One branch and folder per Sprint, scrum/sprint-NN-<suffix>/; the tag has the same name. → long/sprint-stages.md
```

**备注**：'With a separate working copy if wanted' is dropped (optional); the folder layout under scrum/ is in the layers-and-folders long file.

---

### sprint-log#2 · No end date

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 29–29 行 · 标记：Departs

**旧规矩原文**

> 2. **No end date** — Close a Sprint when its goal is met or the Product Owner stops it; the Product Owner watches at checkpoints for a Sprint that drags on. This departs from the Scrum Guide: see the Departures section of `../scrum-kernel/overview.md`.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 6017ae0 docs: Sprint 10 结构稿——五份文件的章节与约定短名（给 PO 看）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 3 行头部：「Closes when the Sprint Goal is met or the Product Owner stops the Sprint」

**建议**：改；去处：清单（一行）

**理由**：与 Scrum Guide 不同的做法是 PO 要看的核心，结束条件一句话写清；尾句「see the Departures section」只是指路，删掉，偏离理由保留在 overview.md 的 Departures 表第 119 行。

**新行**

```text
- **no-end-date** A Sprint closes when its goal is met or the PO stops it; the PO watches for one that drags on (departs from the Guide).
```

**备注**：The reason for the departure stays in the departures long file.

---

### sprint-log#3 · Small work, small Sprint

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 30–30 行

**旧规矩原文**

> 3. **Small work, small Sprint** — Open a Sprint even for work of half an hour to one session, each step shrunk to a line or two; the stage decisions and permissions, the review, and the close still happen (convention 24).

**出处与依据**：作者（把握：中）；种类：规矩
- commit be44889 feat(PBI-23): 冲刺日志约定 sprint-log.md 与模板 sprint-backlog-template.md（正文「开冲刺……小冲刺」）
- archive scrum/documents/sprint/sprint-15-feedback-loop.md 第 8 行：「每一步一两行」

**建议**：改；去处：清单（一行）

**理由**：规矩本身有依据，且已在 Sprint 15 实践。原括号里的「convention 24」现指本文件第 95 行「The Product Owner decides at the end of each stage」，并非指不到；但旧约定文件删除后编号会失指，Memory 里应改写为条名（该行为在 overview 第 12 条「Product Owner decides between stages」），不要留编号。

**新行**

```text
- **small-sprint** Even half an hour of work gets a Sprint, each step a line or two; stage gates, review and close still apply.
```

**备注**：The old '(convention 24)' becomes the handle stage-gates.

---

### sprint-log#4 · Set the Sprint Goal

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 36–36 行

**旧规矩原文**

> 4. **Set the Sprint Goal** — Set the Sprint Goal in the Product Owner’s own style. A project Sprint has one unifying value goal, even when it takes several items. A summary Sprint that serves as an index of different lines of work may list those lines within the same single-line commitment cell, not as separate commitments. The Product Owner leads, usually with the Scrum Master. In section 1.2, point to the full Definition of Done in the product log (§1.3) and name the checks to focus on this Sprint; leaving out a check here does not waive a standard. When even the Sprint Goal cannot be set, the ideo-kernel’s methods can help, as they can at any hard point (`../ideo-kernel/SKILL.md`). Share the goal and the checks with the Scrum Master and the Developer.

**出处与依据**：作者（把握：中）；种类：规矩
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/po-writing-style.md：替 PO 起草 Sprint Goal 时「模仿 PO 以前的写法」
- archive scrum/documents/sprint/sprint-10-conventions.md 第 1 章：Sprint Goal 的写法与 PO 定目标（1.1 节）

**建议**：改；去处：清单（一行）

**理由**：保留「PO 自己的写法、一个统合价值目标、PO 带 Master 定目标、把目标与检查分发给 Master 与 Developer」；总览式冲刺的例外与 DoD 指路、不降低标准已在 sprint-backlog-template.md 第 16、20 行，可归模板；ideo-kernel 兜底是说明，可删。分发这句模板没有（只在本条 sprint-log.md 第 36 行），必须留在清单。

**新行**

```text
- **sprint-goal** [po,sm] The PO sets the Sprint Goal in their own style, usually with the Scrum Master: one unifying value goal.
- **share-goal-and-checks** [po,sm] Share the Sprint Goal and the checks to focus on with the Scrum Master and the Developer.
```

**别处已有**：The summary-Sprint exception (several lines of work in one single-line commitment cell), the pointer to the full Definition of Done in section 1.3 and 'leaving out a check does not waive a standard' are in plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-backlog-template.md (lines 16, 20) and in dod-in-product-log.

**备注**：The ideo-kernel fallback sentence is dropped (explanation).

---

### sprint-log#5 · Select the items

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 40–40 行

**旧规矩原文**

> 5. **Select the items** — Select the items and copy each into section 2.1 word for word, five columns — number, title, user story, place, size. As you write the rows, check the set against the Sprint Goal: every item serves it; add what it still needs, drop what does not serve it — never one just to fill the Sprint. Add a missing item to the product log first.

**出处与依据**：作者（把握：中）；种类：规矩
- commit be44889 feat(PBI-23): 冲刺日志约定 sprint-log.md 与模板 sprint-backlog-template.md（Planning 选项目的做法）

**建议**：改；去处：清单（一行）

**理由**：「逐条对照 Sprint Goal，缺的补、不服务的删、不为凑数而加」留；五列与逐字复制在模板 sprint-backlog-template.md 第 26-28 行。最后「Add a missing item to the product log first」模板没有，应留在清单，或明确并入 sprint-log#21 并保留选条目时补缺的语境。

**新行**

```text
- **select-items** [po,sm] Check each item against the Sprint Goal: add what it lacks, drop what does not serve it, never pad.
```

**备注**：The five columns and word-for-word copy are in the sprint log template (lines 26-28). This is the line product-log#12 refers to.

---

### sprint-log#6 · Refine in seven steps

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 41–48 行

**旧规矩原文**

> 6. **Refine in seven steps** — Refine the items one at a time, led by the Scrum Master with the Product Owner; the Developer joins. Write into section 2.2 what was settled and who decided it, the acceptance criteria, and the tests. Take these seven steps:
>     1. Take one item; it is the point of view.
>     2. Confirm the point of view, copied from the goal or the item without change.
>     3. Open the item into How Might We questions and unclear points.
>     4. Place each point: the Product Owner decides it, the Developer proposes a solution, or it needs research — a question about what people want or what counts as good, with no ready answer — which the Product Owner settles by the boundary in the ideo-kernel's conventions (`../ideo-kernel/conventions/ideo-log.md`, convention 1): a design sprint, or the five modes.
>     5. Cut the item into items of a few sessions at most, with acceptance criteria.
>     6. Check that no questions are left — the Developer's about what is meant, the Product Owner's about what will be built: the Developer restates each point, and the Product Owner agrees.
>     7. The Product Owner says when refinement is over.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 5 章 sprint-log 段：「七步精化并入 Refine in seven steps」
- archive scrum/documents/sprint/sprint-10-conventions.md 第 1 章：「精化定下的内容都写进 scrum-kernel 的约定」

**建议**：改；去处：长文件

**理由**：七步是步骤，按约定「是步骤就归模板或流程文档」，移出 sprint-log 清单；清单留一行：精化由 Master 带、PO 定，问题清零后 PO 宣布结束。

**新行**（长文件 `sprint-refinement`）

```text
- **refinement** [sm,po] The Scrum Master leads refinement with the PO; seven steps; the PO says when it is over. → long/sprint-refinement.md
```

**备注**：Long file: the seven steps word for word, what is written into section 2.2 (what was settled and who decided, acceptance criteria, tests), and step 4's pointer to the design-sprint-or-five-modes boundary as the sprint-or-modes handle.

---

### sprint-log#7 · How is a plan, not steps

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 52–52 行 · 标记：Departs、quote

**旧规矩原文**

> 7. **How is a plan, not steps** — The Developer writes chapter 3 as a plan for making the selected items: the work items in order, each done within one session, each with its output and how to tell it is done; the key choices and their reasons; the known risks and open points. Write it to the level of approach, not steps: no step-by-step instructions, no file contents, no polishing of the plan; if you can write the steps, do the work. It is not the solution a design chose: if a design gave a solution, the plan is how to build it. The Scrum Guide's measure, "decomposing Product Backlog items into smaller work items of one day or less", becomes one session here. The Scrum Master and the Product Owner check the plan. This departs from the Scrum Guide: see the Departures section of `../scrum-kernel/overview.md`.

**出处与依据**：作者（把握：中）；种类：规矩
- commit be44889 feat(PBI-23): 冲刺日志约定 sprint-log.md 与模板 sprint-backlog-template.md（Planning 三个阶段：How 是方案，不是步骤）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 5 章 sprint-log 段：「How 写成 plan」

**建议**：改；去处：清单（一行）

**理由**：一行保留「方案到做法层级、每个工作项一个 session」；模板 sprint-backlog-template.md 第 37 行、commands/developer.md 第 33 行与 overview.md 第 116 行已覆盖方案内容、无分步和检查人。但「no file contents、不润色方案、能写出步骤就去做」和「设计给的是方案时，How 是把它造出来」只在原条（sprint-log.md 第 52 行），要留在清单或写进 developer.md 的 How 段。

**新行**（长文件 `sprint-stages`）

```text
- **how-is-a-plan** [dev] The How is a plan of work items, each done within one session, each with its output and a done test. → long/sprint-stages.md
- **no-steps** [dev] Keep the How at the level of approach: no steps, no file contents, no polishing; if you can write the steps, do the work.
```

**别处已有**：What the How holds (key choices and reasons, known risks and open points) is in the sprint log template (line 37) and commands/developer.md (line 33).

**备注**：The departure (the Scrum Guide's 'one day or less' becomes one session) is in the sprint-stages long file, where the rule is kept in full, and in the departures table. 'The Scrum Master and the PO check the plan' is covered elsewhere (review-handover, the role commands) and not repeated.

---

### sprint-log#8 · Go-ahead

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 53–53 行

**旧规矩原文**

> 8. **Go-ahead** — Start building only after the Product Owner's go-ahead; approving a plan is not a go-ahead. Write it as the last line of chapter 3, with the date and how far it reaches: commit, merge, tag, release, push. The Product Owner may hand the review of the How, of new structures, and of full texts to the Scrum Master; write the handover in the log. The right to review the How is not the right to give the go-ahead (convention 24).

**出处与依据**：作者（把握：高）；种类：规矩
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/delegated-choice-not-gate.md：PO 叫停时的原话「方案还没经 PO 确认，是我越过了关卡」（2026-11-11）

**建议**：留；去处：清单（一行）

**理由**：「审方案不等于放行，放行只能 PO 给」是 PO 叫停过的事，必须留；后半句「PO 可把 How、新结构、全文的审阅交 Master，并把交接写进日志」模板 sprint-backlog-template.md 第 46 行没有，overview.md 第 12 条（第 89 行）只讲一般书面交接，应一并留在清单，不能「归模板」。

**新行**（长文件 `sprint-stages`）

```text
- **go-ahead** Build only on the PO's go-ahead, with its date and reach (commit … push); approving a plan is not one. → long/sprint-stages.md
- **review-handover** [po,sm] The PO may hand the review of the How, new structures and full texts to the Scrum Master in writing; not the go-ahead.
```

**备注**：A thing the PO stopped in an earlier Sprint, so both halves stay.

---

### sprint-log#9 · Notes as you go

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 57–57 行

**旧规矩原文**

> 9. **Notes as you go** — Keep chapter 4, Increment notes, as the full record, so a new session can pick the Sprint up from the log alone. A session that picks up the Sprint goes by the notes and does not work everything out again. The notes take whatever form helps; they need not be a running account of what was done. The How in chapter 3 is a note too, and chapter 4 may refine it. When a work item is done, prefix its Done when cell in the chapter 3 table with `✓ <date>`, keeping the completion condition after it; an unmarked row is not done.

**出处与依据**：作者（把握：中）；种类：规矩
- commit be44889 feat(PBI-23): 冲刺日志约定 sprint-log.md 与模板 sprint-backlog-template.md（施工：笔记、检查点）

**建议**：改；去处：清单（一行）

**理由**：保留「第四章是完整记录、新会话靠日志接手且不从头重算」；「笔记形式随意」与「chapter 4 may refine the How」模板 sprint-backlog-template.md 第 50 行已有，可删。但「Done when 格加 ✓ 日期、保留完成条件、未标=未完成」模板没有（第 37-46 行），board-log.md 第 29 行与 scripts/board_check/check.py 第 265 行只读取该标记，必须留在清单。

**新行**

```text
- **increment-notes** [dev] Keep chapter 4 as the full record, so a new session can pick the Sprint up from the log alone.
- **mark-done** [dev] Mark a finished work item by prefixing its Done when cell with ✓ <date>; an unmarked row is not done.
```

**别处已有**：That the notes take any form and that chapter 4 may refine the How is in the sprint log template (line 50).

**备注**：The board reads the done mark (board-log, and the board check script), so mark-done must stay in the list.

---

### sprint-log#10 · Checkpoints, not stand-ups

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 58–58 行 · 标记：Departs

**旧规矩原文**

> 10. **Checkpoints, not stand-ups** — Stop and check the work against the Sprint Goal at the end of each stage (convention 24), whenever the AI is stuck, and whenever the Product Owner asks how things stand. Stuck means one of these: waiting for a decision or a piece of information only the Product Owner can give, a block from outside the team, the same approach tried twice and failed, or the current How no longer showing how to reach the Sprint Goal; anything else is an adjustment inside the plan. This departs from the Scrum Guide's Daily Scrum: see the Departures section of `../scrum-kernel/overview.md`.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 利益相关者的看法一节：写「whenever the AI is stuck」，没说什么算卡住，已登记 PBI-54
- archive scrum/documents/sprint/sprint-10-conventions.md：「检查点没有固定的触发时机」

**建议**：改；去处：清单（一行）

**理由**：检查点的触发与「卡住」的定义已补全，规矩留。要改的是尾句「This departs from the Scrum Guide's Daily Scrum: see the Departures section ...」，是指路，删掉。

**新行**（长文件 `sprint-stages`）

```text
- **checkpoints** Check the work against the Sprint Goal at each stage end, when stuck, and when the PO asks (a departure). → long/sprint-stages.md
```

**备注**：Long file: what stuck means (waiting for a decision or information only the PO can give, a block from outside the team, the same approach tried twice and failed, or the current How no longer showing how to reach the Sprint Goal; anything else is an adjustment inside the plan). The pointer 'see the Departures section' is dropped; the reason is in the departures long file.

---

### sprint-log#11 · Outline before full text

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 59–59 行

**旧规矩原文**

> 11. **Outline before full text** — Before writing a new lasting document or a new template, show its outline to whoever reviews it (convention 8): the headings at every level, each with one line on what its part will hold. Write the full text once the reviewer agrees; for a new template, the outline is its chapter list.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 5 章 sprint-log 段：「写新的长期文档或新模板之前先给大纲」（PO 强审后第一阶段，commit aa473c6）
- commit aa473c6 （同一文件 2026-11-10 记录的第一阶段提交）

**建议**：留；去处：清单（一行）

**理由**：写长期文档前先给大纲，PO 强审时加入，有依据，留。与 #12 同一流程的两步，#12 是全文审阅。

**新行**

```text
- **outline-first** For a new lasting document or template, first show the reviewer its outline (headings, one line each); write it once they agree.
```

---

### sprint-log#12 · Full text for review

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 60–60 行

**旧规矩原文**

> 12. **Full text for review** — Put a new lasting document's full text — word for word, not an outline — where the reviewer (convention 8) can annotate it, with the problems you found and a recommendation for each; change the source files only after approval. The version on disk wins: read before you overwrite.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/sprint/sprint-10-conventions.md 第 2 节 3 段：「先交结构：五份文件的章节和约定短名，Master 审过才写全文」

**建议**：留；去处：清单（一行）

**理由**：全文给审阅人标注、改源文件须经批准、以磁盘版本为准，三件事都是规矩，留。问题与建议的格式可归模板。

**新行**

```text
- **full-text-review** Give the reviewer the full text to annotate, with problems and advice; edit sources only after approval; the disk version wins.
```

**备注**：'The problems and recommendations format' can live in a template; the three rules stay in the line.

---

### sprint-log#13 · Tests: criteria first

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 64–64 行

**旧规矩原文**

> 13. **Tests: criteria first** — In section 2.2, set the method and pass lines: what needs fresh evidence, what earlier evidence is expected to still hold, and which outcome signals must be shown in this Test. Commit the method and pass lines before running the Test; do not change them after seeing results. Check a script’s wrong calls one by one and write down why.

**出处与依据**：作者（把握：中）；种类：规矩
- archive scrum/documents/sprint/sprint-10-conventions.md 第 3 节：「测试判定标准每次都先写、单独提交再跑，跑过的标准不改。」
- commit d85f6e5 （Sprint 10 判定标准先提交的一例，见该归档第 3 节）

**建议**：改；去处：清单（一行）

**理由**：「先写标准、先提交、跑过不改」有依据，留；第二句「检查脚本的错误调用逐条记下原因」拆成独立一条进 Memory。headless-testing.md 在 scrum/documents/，第 3 行说「插件不要求用户照做」，不能作去处。

**新行**

```text
- **tests-criteria-first** Before the Test, set the method and pass lines in 2.2 and commit them; do not change them after seeing results.
- **check-script-misses** Check a script's wrong calls one by one and write down why.
```

**备注**：The annotation asked to split the second sentence into a rule of its own (or move it to the headless testing notes); it is a line here. The detail of what the pass lines hold (what needs fresh evidence, what earlier evidence still holds, which outcome signals must be shown) is in sprint-stages.

---

### sprint-log#14 · A reviewer is required

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 65–65 行 · 标记：Departs

**旧规矩原文**

> 14. **A reviewer is required** — Have someone other than the builder review: the Scrum Master by default, or a Stakeholder or a fresh subagent when the Product Owner names one. A Stakeholder named as reviewer checks the work item by item against the Definition of Done and the acceptance criteria. When the Scrum Master also built the work, a fresh subagent reviews, checking only whether the work was done right. When the Developer only shares the Scrum Master's context, the Scrum Master still reviews: a shared context does not make it the builder. Brief a review subagent with the task, the project's rules, and the decisions already issued. The Scrum Master may send a subagent to do the review or to read a long diff, and still owns the conclusion. This departs from the Scrum Guide: see the Departures section of `../scrum-kernel/overview.md`.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 6017ae0 docs: Sprint 10 结构稿——五份文件的章节与约定短名（给 PO 看）
- archive scrum/documents/sprint/sprint-11-conventions-review.md：第 44 行，sprint-log 4 成立：SM 自己构建则全新子代理审；只共享上下文则 SM 照常审

**建议**：改；去处：长文件

**理由**：核心行为有依据，但条文过长。清单留一行：SM 默认审；SM 自己构建则全新子代理审；PO 点名的 Stakeholder 按 DoD 与验收标准逐条核；共享 SM 上下文的 Developer 不因此使 SM 成为构建者，SM 仍审；SM 可派子代理审阅或读长 diff，仍对结论负责（commands/scrum-master.md:58 有前半）。子代理简报等细则随全文进长文件 long/roles-and-routing.md。

**新行**（长文件 `sprint-stages`）

```text
- **reviewer-required** The builder never reviews: the Scrum Master does, or a fresh subagent if the Scrum Master built it. → long/sprint-stages.md
```

**备注**：Long file keeps: a Stakeholder or fresh subagent when the PO names one, and a named Stakeholder checks item by item against the Definition of Done and the acceptance criteria; a fresh subagent that reviews work the Scrum Master built checks only whether it was done right; a Developer that only shares the Scrum Master's context does not make the Scrum Master the builder; how to brief a review subagent (the task, the project's rules, the decisions already issued); the Scrum Master may send a subagent to review or read a long diff and still owns the conclusion.

---

### sprint-log#15 · Product Owner acceptance when written

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 66–66 行

**旧规矩原文**

> 15. **Product Owner acceptance when written** — Ask for formal acceptance only when the Definition of Done or the acceptance criteria call for it; sometimes a glance is enough.

**出处与依据**：作者（把握：低）；种类：规矩
- commit be44889 feat(PBI-23): 冲刺日志约定 sprint-log.md 与模板 sprint-backlog-template.md

**建议**：改；去处：清单（一行）

**理由**：来源只有作者的一句做法；正式验收只在 DoD 或验收标准要求时请，其余不必正式验收，但「有时瞥一眼即可」要保留，不要改成一律不请。

**与它重复或相邻**：sprint-log#25

**新行**

```text
- **acceptance-when-written** Ask the PO for formal acceptance only when the DoD or acceptance criteria call for it; sometimes a glance is enough.
```

**备注**：The verifiers asked to keep 'sometimes a glance is enough' (the author's sentence) rather than turn it into 'never otherwise'; kept as written.

---

### sprint-log#16 · Record the tests

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 67–67 行

**旧规矩原文**

> 16. **Record the tests** — In chapter 5, keep the Developer’s tests, the independent check, and any required Product Owner acceptance. Show the result of every Output Done standard and item acceptance criterion: link the new evidence or cite the old evidence and why it still holds. When a stated condition did not arise, record it and why it did not apply. An applicable standard without valid evidence does not pass, even if it was not a focus. Record the result of each Outcome Done signal separately from Output Done. An outcome required for this Test by the Sprint Goal, an item’s outcome or acceptance criteria, or another pass line set beforehand blocks a Test pass if unmet or unproven. Otherwise record a signal without evidence as not yet observed; report contrary evidence as not met and explain its effect. Do not claim the full DoD has passed on those signals. The Increment’s quality can pass on its own evidence; the Sprint Test passes only when all its required checks, review, and acceptance pass. Fix a problem within Test and test again; a return to an earlier stage needs a decision under convention 24.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 87bd0db fix(PBI-49): 照 Master 审停点 2 改七处（sprint-log 加 25 Ask the PO 等）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：第 142 行，sprint-log 新增 Record the tests

**建议**：改；去处：长文件

**理由**：有依据（Sprint 14 新增）。清单留一行：每条完成标准和验收标准都要有有效证据，否则不算过；未观察到的信号记为未观察，反证记为未达并说明影响。其余细则（Outcome 与 Output 分开记、必需项未满足即拦下、不得声称整个 DoD 已通过、Sprint Test 须全部检查/审阅/验收通过、Test 内修复重测、退回上一阶段按阶段决定）逐条进长文件 long/stage-gates.md。

**新行**（长文件 `sprint-stages`）

```text
- **record-the-tests** [dev] In chapter 5, show valid evidence for every applicable standard and criterion, else no pass. → long/sprint-stages.md
```

**备注**：Long file keeps the whole rule: chapter 5 keeps the Developer's tests, the independent check and any PO acceptance; the result of each Output Done standard and item acceptance criterion, with the new evidence linked or the old evidence cited and why it still holds; a condition that did not arise is recorded with why it did not apply; Outcome Done signals are recorded apart from Output Done (an outcome required by the Sprint Goal, an item or a pass line set beforehand blocks the pass if unmet or unproven; otherwise a signal without evidence is 'not yet observed', contrary evidence 'not met' with its effect; do not claim the full DoD passed on those signals); the Increment's quality can pass on its own evidence, the Sprint Test passes only when all its required checks, review and acceptance pass; fix within Test and test again, a return to an earlier stage needs a stage decision.

---

### sprint-log#17 · Review

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 71–71 行

**旧规矩原文**

> 17. **Review** — Close with a Review: compress the sprint log to its key decisions, rename it `sprint-NN-<suffix>.md`, and move it into `scrum/documents/` or the project’s existing archive subfolder there. An ended design is archived by the first Review that can read its complete log and all original material in its own checkout. Without that complete set, leave the design pending archival and do not move its log or material from another worktree. Archive its log as `design-<suffix>.md` and keep its original material together in a folder beside it, out of the active design path. Preserve the decision trail and verify that the archive is readable before updating references in this checkout. Hand off the old and new paths to any receiving Sprint working elsewhere; that Sprint first checks that the originals are readable at the new path in its own checkout, then updates its references there. While building, keep a readable old reference until the new one is available in that checkout. When the design is already archived on the target base (`main`), in this checkout, or in an integration branch ready alongside this Sprint, before the receiving Sprint closes check its actual material references — including those in its log being archived — and the originals against that combined target state, and update broken links before closing; an old link that works only in the current worktree is not sufficient. If the receiving Sprint closes while the design is still pending archival everywhere, keep the usable active reference, note the pending archival, and merge to `main`; the later archiving Review searches the whole project before its closing commit (convention 19 step 1) so those archived Sprint references are updated too, and reports any unmerged branches still holding stale active paths to the Scrum Master. Leave verbatim historical commitment snapshots unchanged. Report stale active paths on other branches to the Scrum Master, rather than changing those branches. Archive ended IDEO logs as `ideo-<suffix>.md`, using `../ideo-kernel/conventions/ideo-log.md`, convention 4, for their prototypes. Clean up ordinary working files in `scrum/`, including outdated ones in `scrum/documents/`; check that this does not remove design originals or break links to them, even when the receiving Sprint closes. Write the Stakeholders’ views and any changes to the product log or Product Goal into the product log and refresh it (`../scrum-kernel/conventions/product-log.md`, convention 17). For an outside view, the Product Owner or the Scrum Master — never the builder — summons Stakeholders from the product log’s table.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：第 38 行，Review 和 Retro 不设章，是收官动作

**建议**：改；去处：长文件

**理由**：有依据，但条文混了冲刺日志压缩归档、设计归档与接力、IDEO 日志归档、清理 scrum/ 工作文件、Stakeholders 看法写入产品日志、outside view 的召唤六件事，远超一行。清单留一行：收官时用 Review 压缩、归档、刷新产品日志；其余细则全部进长文件 long/sprint-closing.md，尤其保留清理工作文件（勿删设计原件或断链）与 IDEO 日志以 ideo-<suffix>.md 归档；outside view 由 PO 或 SM 而非构建者召唤（commands/stakeholder.md:2 已有）。

**与它重复或相邻**：sprint-log#18、sprint-log#19

**新行**（长文件 `sprint-closing`）

```text
- **review-at-close** At close, a Review: compress the sprint log to key decisions, archive it, refresh the product log. → long/sprint-closing.md
```

**备注**：Long file: the whole Review rule word for word (the archiving of ended designs and IDEO logs, the relay to a Sprint working elsewhere, the checks before updating references). The product-log freshening is fresh-at-review.

---

### sprint-log#18 · Retrospective

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 72–73 行 · 标记：Supplement

**旧规矩原文**

> 18. **Retrospective** — Hold it as an action at close, with no chapter in the log. The Developer saves only the important, reusable lessons, one independently findable entry per lesson, in the project’s memory. Write enough to use each principle on its own: what broke or worked, why, and what to do next time. If the tool has no project memory, use the repository notes the project keeps for lessons, still one separately findable entry per lesson. Do not write a Sprint Retro summary, put lessons in `CLAUDE.md` or `AGENTS.md` or any other instructions file, or mix them with the plugin’s conventions. An index may point to the entries, not copy their text. If there is no important lesson, write no entry. Discard the rest: one-off session details, passing friction, and notes without a demonstrated reusable reason are not lessons; do not infer a cause to turn every remark into a principle. An especially good improvement goes into the Definition of Done with the Product Owner’s consent. Check whether the product log is still fresh.
>     *Supplement:* ask where the Product Owner held up the AI — waiting for a decision, waiting for a go-ahead.

**出处与依据**：补充（把握：中）；种类：规矩
- commit 9734304 docs(Sprint 23): H10 落源 18 份已审稿
- archive scrum/documents/sprint/sprint-23-log-rules.md：第 37 行，PBI-69：重要、可复用教训一条一条独立可找回；非要点丢弃

**建议**：改；去处：长文件

**理由**：正文有依据（PBI-69）。清单留一行：重要、可复用的教训一条一条独立可找回地进项目记忆；没有就不写，不写 Retro 汇总，不进 CLAUDE.md/AGENTS.md 等指令文件。其余细则进长文件 long/sprint-closing.md：工具无项目记忆时用仓库的教训笔记、每条写清什么坏了/为什么/下次怎么做、索引只指不抄、特别好的改进经 PO 同意进 DoD、检查产品日志是否保鲜。条末 *Supplement*（问 PO 在哪里卡住 AI）未经实践确认，作待 PO 确认的条目放进同一长文件，不要无声删去。

**与它重复或相邻**：sprint-log#17

**新行**（长文件 `sprint-closing`）

```text
- **retro-in-memory** Retro saves only important reusable lessons, one memory entry each; no summary, no instruction files. → long/sprint-closing.md
```

**备注**：Long file keeps: no chapter in the log; the Developer saves; enough to use each principle alone (what broke or worked, why, what to do next time); with no project memory use the repository notes, still one entry per lesson; do not mix lessons with the plugin's conventions; an index may point to the entries but not copy them; discard one-off details, passing friction and notes without a demonstrated reusable reason, and infer no cause to make a remark a principle; an especially good improvement goes into the Definition of Done with the PO's consent; check whether the product log is still fresh. The *Supplement* sentence (ask where the PO held up the AI) goes there too, labelled.

---

### sprint-log#19 · One closing commit

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 74–82 行

**旧规矩原文**

> 19. **One closing commit** — Close in this order:
>     1. Before the closing commit, search the whole project for old paths until none remain; the fixes go into that same commit.
>     2. Make one closing commit with the changes Review and Retro actually made inside the repository. If project memory is outside it, or there is no important lesson, do not copy outside memory or create a Retro file to make the commit appear to contain both.
>     3. Tag it with the Sprint folder's name; the tag's message says what the Sprint achieved.
>     4. Merge into the main branch.
>     5. Close the working copy.
>     6. Delete the branch of the same name.
>
>     Judge the project's health by `scrum/` alone: it holds all of the Scrum work (`../scrum-kernel/overview.md`, convention 4); elsewhere, usually only the README needs updating. Pushing and other outward actions need the Product Owner's consent.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 72e08a2 fix(PBI-23, PBI-31, PBI-32, PBI-37, PBI-39): 照三份审查的 21 项清单修改
- commit cbed055 docs(Sprint 14): 收官——Review、产品日志保鲜、Retro，发版 v5.2.0

**建议**：改；去处：长文件

**理由**：一个收官提交、先全仓 grep 旧路径有依据。六步顺序与条末「以 scrum/ 判断项目健康、通常只需更新 README」都进 sprint-kernel 长文件（含第 2 步不得复制外部记忆或造 Retro 文件充数、第 3 步 tag 消息写本期成就）；清单只留一行：收官只做一个提交，先清旧路径，再打 tag、合 main、关工作区、删分支；推送要 PO 同意。

**与它重复或相邻**：sprint-log#17

**新行**（长文件 `sprint-closing`）

```text
- **one-closing-commit** Close with one commit after clearing old paths project-wide; then tag, merge, delete the branch. → long/sprint-closing.md
- **outward-needs-po** Push, release and other outward actions need the PO's consent; a stage permission never covers commit, merge or push.
```

**备注**：Long file: the six steps in order; the closing commit holds only what Review and Retro changed in the repository (no copying of outside memory, no Retro file made up to fill it); the tag's message says what the Sprint achieved; the project's health is judged by scrum/ alone, usually only the README needs updating.

---

### sprint-log#20 · Goal fixed, plan flexible

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 86–86 行

**旧规矩原文**

> 20. **Goal fixed, plan flexible** — Hold the Sprint Goal and the Definition of Done (`../scrum-kernel/overview.md`, convention 17). The How may change at any time; refinement points and acceptance criteria may be renegotiated with the Product Owner, or with the Scrum Master, who serves the Product Owner; acts for them within a written handover, and the accountability stays with the Product Owner; decisions made under it are recorded. Write each change and its reason in chapter 4, Increment notes.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 46959b6 docs: Sprint 10 结构稿第二版——How 是方案、目标不变其余可调、约定不写工具机制

**建议**：并 → overview#17；去处：不进 Memory

**理由**：与 overview#17 同名同义（Goal fixed, plan flexible）。Sprint 特有的部分（验收标准可与 PO 或 SM 重谈、改动和原因写进第 4 章）并入 overview#17 或冲刺模板，本条删去。

**与它重复或相邻**：overview#17、design-log#25、product-log#18

**新**：并入 `overview#17`。这条独有、要带过去的内容：Acceptance criteria and refinement points may be renegotiated with the PO, or with the Scrum Master within a written handover; write each change and its reason in chapter 4, Increment notes.

**备注**：Goes into the goal-fixed long file.

---

### sprint-log#21 · New work gets registered

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 87–87 行

**旧规矩原文**

> 21. **New work gets registered** — New work goes into the product log as an item first; the Product Owner decides whether it enters this Sprint. The scope can be renegotiated; the Sprint Goal stays.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 664bf46 refactor(PBI-23, PBI-31, PBI-37, PBI-39): 精简四份约定——砍字不砍规矩

**建议**：留；去处：清单（一行）

**理由**：有依据，行为清楚：新工作先登记为产品日志条目，PO 定是否进本期；范围可重谈，Sprint Goal 不变。一行即可，与 25 的 PO 事项清单有重叠，见 25。

**与它重复或相邻**：sprint-log#25

**新行**

```text
- **new-work-registered** New work goes into the product log first; the PO decides whether it enters this Sprint; the Sprint Goal stays.
```

---

### sprint-log#22 · The log is the handoff

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 88–88 行

**旧规矩原文**

> 22. **The log is the handoff** — The header carries `> Now:` with the stage the Sprint is in and the last decision the Product Owner made, followed immediately by `> Waiting for PO:` with each pending decision's number and short question, separated by semicolons, or `None`. Update both with the log change that causes them; a session that picks up the Sprint reads them first, then checks the recorded permission for the stage and scope; the header is not itself permission to act (convention 24). Write no separate handoff documents: before a session ends or its context is shortened, write what matters into the log and update the header. At handoff or pause, commit within the authorized scope only if that commit is permitted; otherwise keep the uncommitted changes and record that status and where to resume. This handoff rule does not waive the required pre-Test freeze commit (convention 13) or the closing commit (convention 19): if commit permission is not recorded for those gates, ask for it before running the Test or closing. Stop at a complete point.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 9a4e950 docs: Sprint 10 结构稿第四版——补完 Master 审结构提出的六处，结构通过
- archive scrum/documents/sprint/sprint-18-rules-first.md：第 33 行，冲刺、设计、IDEO 日志头部有 Now 和紧跟的 Waiting for PO

**建议**：改；去处：长文件

**理由**：有依据（Sprint 18 统一头部）。头部 Now/Waiting for PO 的字段与接手先读已在 sprint-backlog-template.md 第 4-5 行，格式归模板；清单留一行：头部随日志同步更新、头部不是授权，暂停时把要紧的写进日志。其余行为——不另写交接文件、暂停时按授权提交否则保持未提交并记下续点、不得借此跳过测试前冻结与收官提交、在完整处停下——进冲刺长文件。

**与它重复或相邻**：sprint-log#24

**新行**（长文件 `handoff`）

```text
- **log-is-the-handoff** Keep a log's header current and write what matters into it before a session ends. → long/handoff.md
```

**别处已有**：The Now and Waiting for PO header fields and reading them first are in the sprint log template (lines 4-5).

**备注**：Merged with design-log#24 (same rule for the design log). Long file keeps: a session that picks up reads the header first, then checks the recorded permission; no separate handoff documents; at a pause commit within the authorized scope only if permitted (otherwise keep changes uncommitted and record the status and where to resume); this does not waive the pre-Test freeze commit or the closing commit; stop at a complete point. design-log#24 adds: in a design, write the half-finished work into the chapter it belongs to before a session ends; Now and permission to enter a stage do not by themselves authorize committing, merging or pushing; commit only if the PO explicitly recorded commit permission for it.

---

### sprint-log#23 · Special cases

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 89–94 行

**旧规矩原文**

> 23. **Special cases** — Two cases need a rule of their own:
>
>     | Case | What happens |
>     | --- | --- |
>     | Something outside the team blocks the work | The Scrum Master tells the Product Owner at once |
>     | A release is ready mid-Sprint | Release it with the Product Owner’s consent for outward actions (convention 19); the Sprint does not end |

**出处与依据**：作者（把握：中）；种类：规矩
- commit 6017ae0 docs: Sprint 10 结构稿——五份文件的章节与约定短名（给 PO 看）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：第 142 行，特殊情况表删去重复的五行

**建议**：留；去处：清单（一行）

**理由**：表里剩两种没有别条覆盖的情况：外部阻塞立即告诉 PO；中途发版经 PO 同意，Sprint 不结束。有依据，保留，可写成一行。

**与它重复或相邻**：sprint-log#19

**新行**

```text
- **outside-blocker** [sm] When something outside the team blocks the work, tell the PO at once.
- **mid-sprint-release** A release ready mid-Sprint goes out with the PO's consent; the Sprint does not end.
```

**备注**：The two rows of the old table, one line each.

---

### sprint-log#24 · The Product Owner decides at the end of each stage

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 95–95 行

**旧规矩原文**

> 24. **The Product Owner decides at the end of each stage** — Follow `../scrum-kernel/overview.md`, *Product Owner decides between stages*, at entry and on return. Record explicit permission to start Why when opening; if no Sprint Goal is set yet, do not record a placeholder as a commitment. The Product Owner sets the goal before What, ends refinement before How, authorizes building with the go-ahead (convention 8), authorizes Sprint Test separately from approving the Increment, and after Test decides to close or authorizes a return to the stage that needs work. A Developer’s checks while building are not Sprint Test. For the decision that sets the goal, put the exact text in the §1.1 table; before that decision is recorded and before each later stage decision, read the exact Sprint Goal from the table, and the Product Goal too if product direction is at issue. Check the work against what you read. If the required text cannot be read, stop at that gate. Keep the exact wording on the dated decision line as a record of the goal at the time, not a source for future decisions. Show the text to the Product Owner only when the goal has changed (including when Why sets it), when product direction is at issue, or when they ask.

**出处与依据**：作者（把握：中）；种类：规矩
- commit a8095ef feat(PBI-49): scrum 这边的修订稿——overview、product-log、sprint-log、分工一节（条号还没重排）
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/delegated-choice-not-gate.md：授权做选择不等于授权过关卡，阶段结束仍停下等 PO 说进下一阶段

**建议**：改；去处：长文件

**理由**：overview#12 只有通用阶段门规，本条还含无 Sprint Goal 时不得记占位承诺、逐次读取目标原文（读不到即停）、仅在目标变化/产品方向有争议/PO 要求时展示目标等行为；且 overview#12 的标注计划删掉「记录谁、日期、依据、范围」并误称已在本条。故不并入，作为冲刺长文件保留，清单留一行：每个阶段结束等 PO 明说才进下一阶段。

**与它重复或相邻**：overview#12、sprint-log#22

**新行**（长文件 `stage-gates`）

```text
- **read-the-goal** Before each stage decision, read the exact goal (Sprint or design) from its table; if you cannot, stop. → long/stage-gates.md
```

**备注**：The old first line sprint-stage-decisions (the PO sets the goal before What, ends refinement before How, gives the go-ahead before building, authorizes Test apart from approving the Increment, then decides close or return) is the umbrella stage-gates line plus the Sprint section of the stage-gates long file. Long file: no placeholder is recorded as a commitment while no Sprint Goal is set; the goal's exact text goes in the section 1.1 table; its wording is kept on the dated decision line as a record, not as a source; show the text to the PO only when the goal changed, direction is at issue, or they ask; after Test the PO decides to close or to return; a Developer's checks while building are not Sprint Test.

---

### sprint-log#25 · Ask the PO

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 96–96 行

**旧规矩原文**

> 25. **Ask the PO** — Ask the Product Owner whenever you are unsure (`../scrum-kernel/overview.md`, convention 10), and in any case to: set the Sprint Goal (convention 4); select the items (`../scrum-kernel/conventions/product-log.md`, convention 12); say when refinement is over (convention 6); give the go-ahead (convention 8); decide at the end of each stage (convention 24); renegotiate the acceptance criteria (convention 20); decide whether new work enters the Sprint, and renegotiate the scope (convention 21); give formal acceptance, when it is written (convention 15); consent to outward actions such as a push (convention 19); and cancel a Sprint whose goal can no longer be met (`../scrum-kernel/overview.md`, convention 17).

**出处与依据**：作者（把握：中）；种类：规矩
- commit 87bd0db fix(PBI-49): 照 Master 审停点 2 改七处（sprint-log 加 25 Ask the PO 等）
- archive scrum/documents/sprint/sprint-08-design-kernel.md：第 40 行，团队做法：拿不准就问 PO

**建议**：并 → overview#10；去处：不进 Memory

**理由**：Developer 改（Master 2026-11-22 要合并重叠）：并入 overview#10（ask-the-po）。PO 决定清单的索引与各条规矩里的决定重复，且 Sprint 27 要改「问谁」的分流；清单只留 ask-the-po 一行，清单本身放 roles-and-routing 长文件。核验说「overview#10 不含清单所以不能并」，现在清单随并入带过去，不丢。设计版的索引（design-log#21）同样并入 overview#10。

**与它重复或相邻**：overview#10、overview#12、sprint-log#15、sprint-log#20、sprint-log#21、sprint-log#24

**新**：并入 `overview#10`。这条独有、要带过去的内容：What goes to the PO: whenever you are unsure, and in any case to set the Sprint Goal, select the items, say when refinement is over, give the go-ahead, decide at the end of each stage, renegotiate the acceptance criteria, decide whether new work enters the Sprint and renegotiate the scope, give formal acceptance when it is written, consent to outward actions such as a push, and cancel a Sprint whose goal can no longer be met.

**备注**：The index of what the PO decides. Merged into ask-the-po with the design version (design-log#21); each decision still has its own line (sprint-goal, select-items, refinement, go-ahead, new-work-registered, acceptance-when-written, outward-needs-po, po-owns-commitments), so the index adds nothing to the list. Marked for the 27 sync with ask-the-po.

---

### sprint-log#26 · Developer in another session or tool

`plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md` 第 97–97 行

**旧规矩原文**

> 26. **Developer in another session or tool** — The Developer may work in another session or another tool. When the two sessions can talk directly — another session in the same tool, or a Developer forked from the Scrum Master's session — they talk directly; a long review is written as a file and the message gives its path; the sprint log is still the record. When they cannot — the Developer is in another tool — the sprint log is the only channel: the two keep one working copy and take turns; whoever holds the turn commits within the authorized scope only if permitted — otherwise keeps the changes uncommitted (convention 22) — writes in the notes what was done, and says whose turn is next; what the reviewer finds goes to the Developer as a file the Product Owner passes on, and the Developer copies it into the log; the Product Owner carries only the word that it is the other side's turn. (These are examples, not rules.)

**出处与依据**：作者（把握：中）；种类：规矩
- commit 7426b3d docs(Sprint 17): 冲刺侧 4 处必改照改；第 5 项连带改动与引用核对（171 处 0 缺）
- archive scrum/documents/sprint/sprint-13-codex.md：第 35 行，协作办法：通道只有本日志；两边共用同一个工作目录，所以轮流动手

**建议**：改；去处：长文件

**理由**：有依据（Sprint 13 与 Codex 协作办法）。改写时去掉工具名，但保留行为：同一工具内的会话（含从 Scrum Master 会话 fork 的 Developer）直接对话，长评审写成文件并给路径，日志仍是记录；另一工具只经日志轮流动手、共用一个工作副本，轮到的按授权提交、否则保持未提交（conv 22）并在笔记写做了什么、说明轮到谁，评审发现写成文件由 PO 转交、Developer 抄进日志，PO 只传话。细则进长文件，清单留一行。

**与它重复或相邻**：sprint-log#22

**新行**（长文件 `handoff`）

```text
- **developer-elsewhere** With a Developer elsewhere, the sprint log stays the record: talk directly if you can, else take turns. → long/handoff.md
```

**备注**：Long file, without tool names: sessions that can talk (another session in the same tool, or a Developer forked from the Scrum Master's session) talk directly, a long review is a file and the message gives its path; otherwise one working copy and turns, the one with the turn commits only within the authorized scope and if permitted, writes what was done in the notes and says whose turn is next, the reviewer's findings reach the Developer as a file the PO passes on, which the Developer copies into the log, and the PO carries only the word that it is the other side's turn. 'These are examples, not rules.'

---

## 非编号块（引言、署名、图、表）

### sprint-log@1 · quote（第 3–3 行）

> > Working conventions: reference, not law — follow what fits, override what doesn't, note why. Source labels and short names are explained in convention 15 of `../scrum-kernel/overview.md`, in the scrum-kernel skill folder, beside its `SKILL.md`. A convention with no label is the author's practice.

**新**：不进清单。去处或不要的理由：The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes.

---

### sprint-log@2 · quote（第 5–6 行）

> > Source: quotations from The Scrum Guide 2020 (Ken Schwaber & Jeff Sutherland), marked where they appear.
> > License: the quotations are CC BY-SA 4.0 (© 2020 Ken Schwaber and Jeff Sutherland).

**新**：不进清单。去处或不要的理由：long/sprint-stages.md carries the Scrum Guide quotation (rule 7) with its Source and License lines.

---

### sprint-log@3 · paragraph（第 8–8 行）

> A Sprint turns selected items into an Increment. Its template is `sprint-backlog-template.md`; each section's comment says who writes it. Paths starting with `../` are relative to the sprint-kernel skill folder.

**新**：不进清单。去处或不要的理由：Dropped: the sprint log template's section comments say who writes each section; that a Sprint turns selected items into an Increment is the Scrum Guide's own definition.

---

### sprint-log@4 · fence:mermaid（第 10–22 行）

> ```mermaid
> flowchart TD
>     A["Opening<br/>conventions 1–3"] -- "PO authorizes Why" --> W["Why<br/>convention 4"]
>     W -- "PO sets the goal and authorizes What" --> H["What<br/>conventions 5–6"]
>     H -- "a hard point" --> D["Choose: a design sprint with its own gates, or IDEO methods"]
>     D -. "what was learned" .-> H
>     H -- "PO ends refinement and authorizes How" --> P["How<br/>conventions 7, 8"]
>     P -- "PO gives the go-ahead" --> I["Increment<br/>conventions 9–12"]
>     I -- "PO authorizes Sprint Test" --> T["Test<br/>conventions 13–16"]
>     T -- "fix on the spot, test again" --> T
>     T -- "PO decides: close" --> C["Closing<br/>conventions 17–19"]
>     T -. "PO authorizes a return to building" .-> I
> ```

**新**：不进清单。去处或不要的理由：Drawn in long/flow-maps.md, with the handles in the boxes; the list line flow-maps points there.

---

### sprint-log@5 · paragraph（第 24–24 行）

> Conventions 20–26 hold at every step; see Throughout, below. Read each stage transition with convention 24; closing is a separate decision.

**新**：不进清单。去处或不要的理由：long/stage-gates.md, Sprint part: closing is a separate decision from the stage transitions.

---
