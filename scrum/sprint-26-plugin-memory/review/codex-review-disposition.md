# Codex 对抗审查的处置账（Sprint 26 行 10）

> 审的是提交 `5baeb1b`；Codex 原文在 `C:\Users\seapawn\AppData\Local\Temp\claude\711d0b41f4cde757\ab047f26-f78c-4a17-9341-013ff5ab79c9\tasks\bv3gndrcp.output`（仓外，Master 转来时的位置）。Master 2026-11-23：条条采纳、逐条改、逐条记、不等 PO。每一条：Codex 说什么、做了什么、现在的行或文件。另有三条是我自己在核查时发现的（S1–S3）。

## 总表

| # | 级别 | 位置 | 处理 |
| --- | --- | --- | --- |
| H1 | 高 | details/roles.md「What only the Product Owner decides, by stage」 | 标题改成「What goes to the Product Owner in any case, by stage」（旧约定原文就是「一定问 PO 的事」，没有「只有」） |
| M1 | 中 | details/design.md 第 7、24、35、43、50、58、66 行；details/design-ending.md 第 13 行 | 全改：模板 `../../template/design-backlog-template.md`，六处步骤 `../design-kernel/steps/…`，design-ending.md 第 13 行同 |
| M2 | 中 | 清单 `product-log-header` | 补「no Now or Waiting for PO line (other logs only)」 |
| M3 | 中 | 清单 `stakeholder-table` | 补回「the AI fills in details」和「short table」，去掉 `[sm]` |
| M4 | 中 | 清单 `architecture-map` | 补回「actors (AI too)」，并带上「subsections only if needed」（产品日志 #7 的后半句） |
| M5 | 中 | 清单 `items-with-sm` | 清单行补「too much or too little」并加 `Read details/product-log.md first.` |
| M6 | 中 | 清单 `where-refined-content` | 补「(Place links it)」并带上「linked in Notes」 |
| M7 | 中 | 清单 `fresh-at-review` | 细则 closing.md 新增一节「Fresh at every Review」放产品日志 #17 的原文（3.2 一行一条带来源、未完成回 3.1、删过时的架构与已解决的待定点、不留修订记录、整个 `scrum/` 保持新） |
| M8 | 中 | 清单 `select-items`、`new-work-registered` | 两行都补回 |
| M9 | 中 | 清单 `working-material` | 清单补「big files in scrum/documents/」，指向细则 folders.md |
| M10 | 中 | 清单 `rule-labels` 或开头说明 | 开头说明改成「when you override one, write what you did and why in the log's notes (a Sprint's Increment notes, or the chapter of the design log it concerns)」 |
| M11 | 中 | 清单 `ideo-log-home` | 两样都加 |
| L1 | 低 | 清单 `write-product-log` | 已加（「leaving history to version control」） |
| L2 | 低 | 清单 `templates-record-outputs` | 清单行加指针 |
| L3 | 低 | details/flow-maps.md 第 74、103、104、106 行附近 | 装配脚本 `assemble_memory.py` 在每个框里去重（同一个旧规矩的多条并到一个句柄时只写一次） |
| S1 | 自查 | 清单 `write-product-log` | write-product-log 里「usually the Scrum Master with the PO」没有出处 |
| S2 | 自查 | 清单 `outward-needs-po` | outward-needs-po 的「a stage permission never covers commit, merge or push」比出处强 |
| S3 | 自查 | 清单 `ask-the-po` | ask-the-po 丢了「谁不确定就问 PO，除非 PO 把这类问题交给了别处」 |

## 逐条

### H1（高）details/roles.md「What only the Product Owner decides, by stage」

- Codex：标题写「只有 PO 决定」，列表里却有「renegotiate the acceptance criteria」，跟 roles.md 第 36 行、goal-fixed.md 第 14 行、旧 sprint-log 第 86 行（Scrum Master 可在书面授权内重新谈）冲突；Master 要求核对我加的那句是否罩住整张清单，而不只是阶段许可。
- 处理：标题改成「What goes to the Product Owner in any case, by stage」（旧约定原文就是「一定问 PO 的事」，没有「只有」）；前言重写：两张清单的每一项都归 PO，除非书面授权把这类决定交给了 Scrum Master，由他决定并记录；明说「不只是阶段许可」，重新谈验收标准或范围就是 Scrum Master 可按授权接手的一项（`goal-fixed`）；规矩自己留给 PO 的两件单列：改承诺或取消 Sprint（`po-owns-commitments`），推送等对外动作要 PO 的同意（`outward-needs-po`）。

### M1（中）details/design.md 第 7、24、35、43、50、58、66 行；details/design-ending.md 第 13 行

- Codex：路径写错：模板被写成在 design-kernel 的 `conventions/` 下，步骤写成 `design-kernel/steps/…`；从 memory 技能的目录出发应是 `../../template/design-backlog-template.md` 和 `../design-kernel/steps/…`。
- 处理：全改：模板 `../../template/design-backlog-template.md`，六处步骤 `../design-kernel/steps/…`，design-ending.md 第 13 行同；另外 product-log.md 第 16 行也是同一种写法（Codex 没列），一并改。新写 `scripts/check_paths.py`（自测过）：清单与细则里所有文件路径都按 memory 技能的目录解析，裸 `design-kernel/…`、`steps/…`、`conventions/…` 报错；现在全部解析得到。

### M2（中）清单 `product-log-header`

- Codex：漏了「也没有 Waiting for PO 行」，以及这两行只属于 Sprint、设计、IDEO 日志。
- 处理：补「no Now or Waiting for PO line (other logs only)」；「愿景行可省」在产品日志模板的注释里（分句核查记为 elsewhere）。
  - 现在：`- **product-log-header** Product statement (1.1) and Product Goal (1.2): one-row commitment tables; no Now or Waiting for PO line (other logs only).`

### M3（中）清单 `stakeholder-table`

- Codex：原文是「AI 补细节」，压成一行丢了；`[sm]` 标签不该有（旧约定没限定角色）。
- 处理：补回「the AI fills in details」和「short table」，去掉 `[sm]`。
  - 现在：`- **stakeholder-table** List stakeholders in 2.1 in a short table; a Stakeholder subagent gets one row, the AI fills in details; if empty, ask the PO.`

### M4（中）清单 `architecture-map`

- Codex：丢了「AI 角色也算」。
- 处理：补回「actors (AI too)」，并带上「subsections only if needed」（产品日志 #7 的后半句）。
  - 现在：`- **architecture-map** Open 2.2 with a Mermaid flowchart TD map: actors (AI too) on top, ending at the bottom, 5-15 steps; subsections only if needed.`

### M5（中）清单 `items-with-sm`

- Codex：丢了「太多或太少」里的「太少」、书面授权与记录、以 Sprint Goal 为尺（太长就放细则、清单指过去）。
- 处理：清单行补「too much or too little」并加 `Read details/product-log.md first.`；细则 product-log.md 新增一节「Items with the Scrum Master」，放产品日志 #12 的原文（授权与记录、Planning 的分工、尺是 Sprint Goal、与 Scrum Guide 的偏离）。清单行去掉了 `[sm,po]` 标签（装不下指针）；旧文没有限定角色。
  - 现在：`- **items-with-sm** The PO decides items with the Scrum Master; Scrum Master and Developer flag too much or little. Read details/product-log.md first.`

### M6（中）清单 `where-refined-content`

- Codex：丢了「Place 列指向它」。
- 处理：补「(Place links it)」并带上「linked in Notes」。
  - 现在：`- **where-refined-content** Splits become rows; long design in 2.2 (Place links it); notes in Notes; big files in scrum/documents/, linked in Notes.`

### M7（中）清单 `fresh-at-review`

- Codex：丢了：完成项要记来源，删过时的架构与已解决的待定点，整个 `scrum/` 都要保持新；建议放细则、清单指过去。
- 处理：细则 closing.md 新增一节「Fresh at every Review」放产品日志 #17 的原文（3.2 一行一条带来源、未完成回 3.1、删过时的架构与已解决的待定点、不留修订记录、整个 `scrum/` 保持新）；清单行加指针。
  - 现在：`- **fresh-at-review** At each Review move done items to 3.2 with source, unfinished to 3.1; delete outdated text. Read details/closing.md first.`

### M8（中）清单 `select-items`、`new-work-registered`

- Codex：`select-items` 丢了「缺的条目先进产品日志」；`new-work-registered` 丢了「范围可重新谈」。
- 处理：两行都补回；`select-items` 还补回「照搬到 2.1」。
  - 现在：`- **select-items** [po,sm] Copy items into 2.1 word for word; each serves the Sprint Goal: add a missing one to the product log first; never pad.`
  - 现在：`- **new-work-registered** New work goes in the product log first; the PO decides if it joins the Sprint; the Sprint Goal stays, scope is renegotiable.`

### M9（中）清单 `working-material`

- Codex：丢了「大而重要的文件进 `scrum/documents/`」；Retro 的去处应是「先项目记忆；没有就用仓库的教训笔记；绝不写进指令文件」。
- 处理：清单补「big files in scrum/documents/」，指向细则 folders.md；folders.md 新增「Working material」一节放旧原文（含 Retro 的去处）。
  - 现在：`- **working-material** Keep working material out of the log; big files in scrum/documents/; Retro lessons: memory only. Read details/folders.md first.`

### M10（中）清单 `rule-labels` 或开头说明

- Codex：丢了「覆盖约定时要写做了什么、为什么、写在哪」。
- 处理：开头说明改成「when you override one, write what you did and why in the log's notes (a Sprint's Increment notes, or the chapter of the design log it concerns)」；names.md 新增一节「Labels, templates and overriding」放旧原文；`rule-labels` 与 `templates-record-outputs` 两行加指针。
  - 现在：`- **rule-labels** No label: author's practice; *Supplement*: inferred, unconfirmed; *Decide on the spot*: no fixed rule. Read details/names.md first.`

### M11（中）清单 `ideo-log-home`

- Codex：要加「working material」和 `Read details/ideo-ending.md first.`（细则文件开头就写着这行指向它，行上却没有指针）。
- 处理：两样都加；「For 格指向它服务的日志」留在细则里。
  - 现在：`- **ideo-log-home** An IDEO log, its prototypes and working material live in scrum/ideo-<suffix>/; no commitment. Read details/ideo-ending.md first.`

### L1（低）清单 `write-product-log`

- Codex：要加「历史留在版本控制」。
- 处理：已加（「leaving history to version control」）；同时见 S1。
  - 现在：`- **write-product-log** Write the product log from the template; for an old project, from README, issues, plans, leaving history to version control.`

### L2（低）清单 `templates-record-outputs`

- Codex：要加「怎么做属于约定；模板只记产出」。
- 处理：清单行加指针；names.md 的新一节写明：怎么做属于规矩、不属于模板；日志保留模板全部标题含后面才填的章；工作备注进 Increment notes 或设计章；承诺表下的说明放在承诺自己的一节。
  - 现在：`- **templates-record-outputs** A template section holds only what its step produced; keep every heading, add none. Read details/names.md first.`

### L3（低）details/flow-maps.md 第 74、103、104、106 行附近

- Codex：同一个框里重复写同一个句柄。
- 处理：装配脚本 `assemble_memory.py` 在每个框里去重（同一个旧规矩的多条并到一个句柄时只写一次）；检查：没有重复的框。103、104 两框各有 `board-rules` 是两个不同的框，不算。

## 自查发现（分句核查与反向核查时）

### S1 write-product-log 里「usually the Scrum Master with the PO」没有出处（反向核查发现）

- 处理：旧产品日志 #1 只说「照模板写；旧项目从 README、议题、旧计划写，历史留在版本控制」，没有谁来写；这半句是我起草时加的。按「内容须有依据」删掉。
  - 现在：`- **write-product-log** Write the product log from the template; for an old project, from README, issues, plans, leaving history to version control.`

### S2 outward-needs-po 的「a stage permission never covers commit, merge or push」比出处强

- 处理：出处（旧 sprint-log #24，现在 gates.md 第 15 行）是「does not by itself authorize」。改回「alone does not cover」。
  - 现在：`- **outward-needs-po** Push, release and other outward actions need the PO's consent; a stage permission alone does not cover commit, merge or push.`

### S3 ask-the-po 丢了「谁不确定就问 PO，除非 PO 把这类问题交给了别处」

- 处理：旧 overview #10 整句；清单行装不下，放回 details/roles.md「Where a question goes」开头（行本身是三步分流，`Read details/roles.md first.` 已在）。
  - 现在：`- **ask-the-po** Decide what is yours; process questions go to the Scrum Master; PO-only questions go to the Supporter. Read details/roles.md first.`

## 分句核查时补回的内容

Master 要求对 111 条逐一做分句覆盖核查（`scripts/clause_coverage.py`，结果在 `review/clause-coverage.md`，决定在 `review/clause-decisions.json`）。下面是这一轮从分句核查里补回或改写的清单行（每条都已核到 ≤ 150 字符）：

- `increment-notes`：接手的会话照记录走、不再重推一遍（sprint-log #9）
  - 现在：`- **increment-notes** [dev] Keep chapter 4 as the full record: a new session goes by the notes alone and does not work everything out again.`
- `mark-done`：完成条件留在 ✓ 日期后面（sprint-log #9）
  - 现在：`- **mark-done** [dev] Mark a finished work item by prefixing its Done when cell with ✓ <date>, keeping the condition; an unmarked row is not done.`
- `outline-first`：模板的大纲就是章列表、全文等审阅者同意（sprint-log #11）；原文进 sprint.md 新一节
  - 现在：`- **outline-first** Before a new lasting document or template, show the reviewer its outline; write it once they agree. Read details/sprint.md first.`
- `full-text-review`：全文逐字而不是大纲、让审阅者批注并附问题与建议、磁盘上的版本为准（sprint-log #12）；原文进 sprint.md 新一节
  - 现在：`- **full-text-review** Give the reviewer the full text, word for word, to annotate; edit sources only after approval. Read details/sprint.md first.`
- `one-scrum-master`：各项目的事实留在各自的日志里（overview #13）
  - 现在：`- **one-scrum-master** One Scrum Master session per project leads its roles; one above projects only summarizes; facts stay in each project's logs.`
- `open-ideo-log`：「多于一个会话」也算一个独立的 IDEO 日志（原来只写了「多于一两个方法」）、一两个方法记进所服务的日志的例子（ideo-log #3）
  - 现在：`- **open-ideo-log** 1-2 methods in one session: note them in the log served (Increment notes, Notes); more: an IDEO log, five chapters, no PO gate.`
- `design-roles`：Designer 负责设计、Scrum Master 主持并记录，Empathize 与 Define 的五项由 PO 与扮演 Scrum Master 的会话定（design-log #3）；原文进 design.md
  - 现在：`- **design-roles** [po,sm,des] The PO and Scrum Master settle Empathize and Define; the Designer takes over at Ideate. Read details/design.md first.`
- `one-session-both-roles`：一个设计常常一个会话就够（design-log #3）
  - 现在：`- **one-session-both-roles** [po,sm,des] A design often needs one session; the PO decides if it plays both roles; its name goes in both header fields.`
- `design-folder`：原型与工作材料都不进 Increment（design-log #5）
  - 现在：`- **design-folder** A design lives in scrum/design-<suffix>/ (suffix: subject, no number); prototypes and working material never go into an Increment.`
- `choose-with-po`：只把选中的方案写进 3.1、用角色卡 Stakeholder 做的投票只在 PO 想要时（design-log #13）；原文进 design.md 新一节「Ideate: choose」
  - 现在：`- **choose-with-po** [po,sm] The Scrum Master leads the choice, the PO decides, no consensus hunt; role-card poll if asked; only the choice in 3.1.`
- `dod-standards`：条目专属或暂定的要求放进该条目的验收标准（product-log #5）
  - 现在：`- **dod-standards** Write standards precisely; keep only what holds across the product; item-specific or tentative ones go in acceptance criteria.`
- `refine-in-sprint`：产品日志没有细化一节（product-log #14）
  - 现在：`- **refine-in-sprint** In the product log only add detail (it has no refinement section); finish refinement in the sprint log's 2.2.`
- `sprint-goal`：没改：「目标定不下来时 ideo-kernel 的方法能帮忙」记为 elsewhere（scrum-kernel/SKILL.md 有同一条一般规矩）
  - 现在：`- **sprint-goal** [po,sm] The PO sets the Sprint Goal in their own style, usually with the Scrum Master: one unifying value goal.`

## 改完之后的检查

| 检查 | 结果 |
| --- | --- |
| `check_drafts.py check` | 140 条（111 规矩＋29 块）、105 个句柄、0 个问题 |
| `assemble_memory.py` | 清单 105 行、15,151 字符（上限 16,000，不用再往细则挪）；无未解占位符、无死链；细则里的句柄都对得上 |
| `check_paths.py` | 清单与细则里所有文件路径都从 memory 技能的目录解析得到 |
| 引文逐字核对 | 18 处，18 处在装配后的 Memory 里逐字出现（前一次是 17/18，那处例外现在写进 names.md 了） |
| `clause_coverage.py` | 714 个分句（109 条规矩，另 2 条 overview#9、design-log#23 是纯表格或图）：覆盖 640，部分 30，缺 44；不够的 74 个全有决定：reworded 33、elsewhere 33、added 4、dropped 3、整条规矩有意不进清单 1（design-log#22，见其 `where_else`）；其中 18 条用了 `force`（脚本从指向的位置读不出足够的词，我写了理由）。决定指的位置都会被读回核对 |
| `clause_coverage.py --reverse` | 反向：清单行里有 17 段在它自己的旧规矩里找不到对得上的句子；逐段看过，都有出处或是概括：汇总或改写的 14 段（如 `flow-maps`、`departures`、`names`、`three-layers`、`item-columns`、`design-stages`、`blank-page`、`choose-with-po` 的概括句），`ask-the-po` 的三步分流 2 段出自 overview#14（它不是并入 ask-the-po 的规矩，所以脚本没找到），`outward-needs-po` 的后半句出自阶段许可那条（gates.md 第 15 行），已按出处改回（S2）。S1 是我写这个检查之前读行时发现的，已删 |

## 没有做的与要 Master 知道的

- 细则文件里各有「Open points for the Product Owner」一节，里面有仓库层面的路径（`scripts/check_docs.py`、`docs/glossary.md`）。那是给 PO 的待定点，不该进插件；行 12 落盘时要删（PO 的待定点另在 `review/po-opinions.md` 与 `review/review-index.md`）。
- 分句核查是词的重合，不是含义的判断：判了「覆盖」的分句仍可能写歪，那要靠读审阅文件；reworded 的 33 条与 force 的 18 条请 Master 抽读。
