# 起草说明（Sprint 26 行 6–8：把旧规矩转成 Memory 的一行）

你是起草员。只读：不改仓库里任何文件，不联网；只写任务里给你的输出文件。

## 仓库根与路径

**仓库根**＝`S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory`。你的当前目录不是它，所以读文件、跑命令都写绝对路径（仓库根＋相对路径）。

## 背景

插件 `ideo-scrum`（给 Claude Code 用的 Design Thinking 与 Scrum 方法论）有六份“约定”文件，共 111 条编号规矩。本期把它们收成 **Memory**：一份短清单（一行一条规矩）加几个长文件；旧约定文件之后删掉，Memory 是唯一一份。Memory 有两个读者：

- **AI**：叫出一个角色（Developer、Scrum Master、Designer、Stakeholder）时带上它，照着守；
- **PO（产品负责人）**：会把每一条旧规矩和你写的新行**一条一条对着读、一条一条改**——所以你写的每一行都要经得起对照：不丢意思，不加原文没有的东西。

另一位标注员已经给每条旧规矩标了出处、依据、建议（留／改／并／删）和理由（已有人核对过）。你的活：按建议把它转成 Memory 里的一行。

## 你拿到什么

任务里给一组 id。对每个 id：

1. 看旧规矩原文：
   `python -X utf8 -I S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory/scrum/sprint-26-plugin-memory/scripts/show_rule.py <id 或 文件#起-止>`
2. 看它的标注：`S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory/scrum/sprint-26-plugin-memory/review/annotations/*.json`（用 Grep 搜 `"id": "<id>"` 找）。字段：`recommend`（留／改／并／删）、`merge_into`、`home`（清单／长文件／不进 Memory）、`kind`、`reason`、`dups`、`checked`（核验记录）。
3. 看有没有别的规矩并入了它：Grep 标注文件里 `"merge_into": "<你的 id>"`；有就用 show_rule.py 看那条，把它**独有的内容**并进你的行（别的内容不重复）。

## 一行怎么写（句型）

```
- **handle** [roles] 一句话规矩。 → long/<文件>.md
```

- **handle**：2–4 个英文词的 kebab-case 小名，全 Memory 里唯一；取自规矩的名字或它管的事（如 `go-ahead`、`ask-the-po`、`stage-gates`）。别用旧编号。
- **[roles]**：这条规矩管谁。全角色都管就省略；否则写 `dev`、`sm`、`des`、`stk`、`po` 里的几个，逗号隔开，如 `[dev,sm]`。拿不准就省略。
- **一句话**：英文，祈使句，**一行写完**（目标 ≤ 160 个字符，最多 220）；只写行为要求，不写背景、不写“为什么”（原因进长文件或不写）；用插件自己的词（Sprint Goal、go-ahead、PBI、product log、sprint log、Increment notes）；不写“convention N”“见某文件第几条”，要指别的规矩就写它的 handle，要指细则就写 `→ long/<文件>.md`。
- **长文件**：只有 `home` 是“长文件”，或你的一句话塞不下关键细节时才用；索引行写“它管什么、什么时候读”，末尾 `→ long/<文件>.md`。长文件名从下表选，选不到就写 `NEW:<建议名>` 并在 `note` 里说明。
- 原文里的引文（Scrum Guide、SGEP、d.school 等）和 PO 的原话**不进这一行**：它们进长文件，逐字不改。

长文件名（可选）：`roles-and-routing`、`stage-gates`、`goal-fixed`、`layers-and-folders`、`sprint-closing`、`sprint-refinement`、`design-ending`、`design-ideate`、`board-writing`、`departures`、`names`、`product-log-details`、`ideo-ending`、`sprint-handoff`。

**section**（这一行放哪一节）：`roles`（谁做什么、谁决定）｜`product-log`｜`sprint`｜`design`｜`ideo`｜`board`｜`meta`（约定本身、文件放哪、名词）。

## 每条怎么处理

| `recommend` | 你做什么 |
| --- | --- |
| 留 | 写一行（`line`）。意思不变，写短。 |
| 改 | 按 `reason` 里说的改法写一行。`reason` 说“拆成几条”就写几行（`lines` 是数组）。 |
| 并 | `line` 写 `null`，`merged_into` 写目标 id；把这条**独有**的内容写进 `adds_to_target`（一句话，给目标那一行的起草员用）。 |
| 删 | `line` 写 `null`；`where_else` 写“旧规矩说的那件事现在在哪”（文件与位置，或另一条规矩的 id）；说不出来就写 `"无"` 并在 `note` 里说明会丢什么——这样的删要回头给 PO 看。 |

别人并进你这一条的内容，写进你的 `line`，并在 `absorbed` 里列出并入的 id。

## 守则（PO 的尺度）

- **不丢意思，不加东西**：只转原文已有的要求；原文没写的不补。拿不准意思就保守地靠近原文，在 `note` 里说你拿不准的地方。
- **别搬原句**：原条文常常一条塞了几件事、带指路套话；你写的是“照着做”的一句。
- **别改变含义**：例如“不得”不要写成“尽量不”。
- **不确定写在 `note` 里**，别藏在措辞里。

## 输出

写到任务给你的输出文件：一个 JSON 数组，每条旧规矩一个对象，顺序照 id：

```json
{
  "id": "sprint-log#8",
  "line": "- **go-ahead** [dev,sm] Build only after the Product Owner's go-ahead; record it as the last line of the How with its date and reach (commit, merge, tag, release, push).",
  "lines": null,
  "section": "sprint",
  "long_file": null,
  "merged_into": null,
  "adds_to_target": null,
  "absorbed": [],
  "where_else": null,
  "note": ""
}
```

- `line` 与 `lines` 二选一：一行用 `line`（`lines` 写 `null`）；拆成几行用 `lines`（`line` 写 `null`）；并或删时两个都写 `null`。
- 其余字段没有就写 `null`（`absorbed` 写 `[]`，`note` 写 `""`）。
- 用 Write 一次写全；写完用 Read 读回，确认是合法 JSON、条数对。
