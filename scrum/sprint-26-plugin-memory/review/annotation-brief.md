# 审读标注说明（Sprint 26 行 2）

你是审读标注员。只读，不改仓库里任何已有文件；只写你自己的输出文件。

## 背景（一分钟读完）

插件 `ideo-scrum`（Design Thinking 与 Scrum 的方法论，给 Claude Code 用）有六份“约定”文件，共 111 条编号规矩。本期要把它们收成 **Memory**：一份短清单（一行一条）加几个长文件，旧约定文件之后会删掉。Memory 里只留该留的规矩，所以要先对每一条旧规矩回答四件事：

1. **出处**：这条规矩从哪来；
2. **依据**：能指给人看的证据；
3. **建议**：留／改／并／删；
4. **理由**：为什么。

产品负责人（PO）的要求，也是你的判断尺度：

- 每条内容要有**可指的依据**，没有依据的 PO 不收（「没有依据我是不可接受的」）。找不到依据就写“无据”，**不要猜、不要编**。
- 作者自己定、没有来源标签的做法，不能默认当规范；PO 要逐条审去留（反馈 F05，`S:/SeaPawn-Memory/memory/FeedBack/IDEO-Scrum/2026-11-15-author-conventions-need-review.md`）。
- 原书摘录（Scrum Guide、Scrum Guide Expansion Pack 简称 SGEP、d.school Bootleg、《Sprint》）和 PO 的原话要逐字保留；AI 写的约定可以大改。
- 约定要最简：一行一条；写不进一句的，是步骤就归模板或流程文档，说不清就砍（PO 2026-11-10：「太复杂」）。

## 你拿到什么

一组规矩的 id（如 `sprint-log#7`）。看原文用：

```
python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py sprint-log#7
python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py sprint-log#1-13
```

它逐字打印规矩，并告诉你它在哪个文件、哪几行、哪一节。命令从仓库根目录（你的当前目录）运行。

## 标注哪些字段

每条规矩一个 JSON 对象：

```json
{
  "id": "sprint-log#7",
  "source": "作者",
  "basis": ["commit 1a2b3c4 提交标题", "archive scrum/documents/sprint/sprint-10-conventions.md：一句话说明"],
  "kind": "规矩",
  "home": "清单",
  "recommend": "留",
  "merge_into": null,
  "reason": "一两句话",
  "dups": [],
  "confidence": "高"
}
```

| 字段 | 取值 | 说明 |
| --- | --- | --- |
| `source` | `原文`｜`PO 原话`｜`作者`｜`补充`｜`无据` | 见下表 |
| `basis` | 字符串列表，至少一项 | 每项以类型词开头，见“依据怎么写”；`无据`时写 `["无据：查了什么、没找到"]` |
| `kind` | `规矩`｜`格式`｜`说明` | 规矩＝角色该照着做的行为；格式＝字段、列、模板结构的规定；说明＝解释、背景、指路 |
| `home` | `清单`｜`长文件`｜`不进 Memory` | 清单＝一行就能说清；长文件＝细则多，清单里留一行索引；不进 Memory＝该留在模板、命令或别处 |
| `recommend` | `留`｜`改`｜`并`｜`删` | 见下表 |
| `merge_into` | id 或 `null` | 只有 `并` 时填，指并入哪一条 |
| `reason` | 一两句中文 | 留的理由；改什么；并去哪；删了会丢什么 |
| `dups` | id 列表 | 与它说同一件事的其他规矩（可跨文件）；没有就 `[]` |
| `confidence` | `高`｜`中`｜`低` | 你对这条标注的把握；拿不准就写低，别硬标 |

### 出处（`source`）怎么判

| 取值 | 什么时候 |
| --- | --- |
| `原文` | 条文本身逐字摘自 Scrum Guide 2020、SGEP、d.school Bootleg、《Sprint》；要能在原书文件里找到那句 |
| `PO 原话` | 规矩出自 PO 明确说过的话，能在日志、归档或反馈里找到原句 |
| `作者` | 作者（插件的设计者）自己的做法，有可指的提交或归档日志；没有来源标签的默认是它（`overview#15`：“a convention with no label is the author's practice”） |
| `补充` | 条文里带 `*Supplement*`：助手推断、未经实践确认的；`*Decide on the spot*` 和 `*Departs from the book*` 是另一种标签，按内容判出处，并在 `reason` 里点出标签 |
| `无据` | 查完三处（见下）仍找不到可指的依据 |

### 建议（`recommend`）怎么判

- **留**：行为规矩，有依据，不与别条重复，Memory 里需要它。
- **改**：想法该留，写法要改：用词过时（如 Codex、“PO assistant”）、引用了已不存在的东西、过长要拆、与实际做法不符。`reason` 写要改什么。
- **并**：与另一条说同一件事，并入哪一条写进 `merge_into`。
- **删**：已不成立、纯解释背景、只是“指路”的套话（如“This departs from the Scrum Guide: see Departures”这类每条都有的尾巴），或工具细节该留在模板里。`reason` 写删了会丢什么；若删了会丢重要内容，别删，写“改”或“留”。
- 无依据的条目，默认建议 `删`，`reason` 写“无据，请 PO 定”；除非它明显是别条的必要前提。

## 依据怎么写（`basis` 每项以类型词开头）

| 开头 | 格式 | 例子 |
| --- | --- | --- |
| `commit` | `commit <7位以上哈希> <提交标题>` | `commit 6e4a2c1 Sprint 17：约定改顺` |
| `archive` | `archive <仓库内路径> <章节或一句话>` | `archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 2 章：…` |
| `po` | `po <路径>：「PO 原话」` | `po scrum/documents/conventions-review-log.md：「…」` |
| `memory` | `memory <路径>：一句话` | `memory S:/SeaPawn-Memory/memory/IDEO-Scrum/conventions-minimal-shape.md：…` |
| `source` | `source <路径>：「逐字引文」` | `source plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-2020.md：「…」` |

校验脚本会检查：哈希真的存在；路径真的存在；引号「」里的话真的在那个文件里（空白和换行不计）。**编的依据会被查出来，整条作废**。

## 去哪里找依据（顺序）

1. **提交历史**：先挑这条规矩里最有辨识度的一句（15 个字以上），查最早是哪个提交写进来的：
   `git log -S"那一句" --oneline --reverse`（不要加 `-C`，不要限定路径，规矩在内核重构时搬过家）。用 `git show <哈希> --stat` 看提交说明。提交说明常写着是哪期冲刺、哪个 PBI。
2. **归档日志**：`scrum/documents/sprint/sprint-NN-*.md`（每期冲刺的关键决定）、`scrum/documents/design/`、`scrum/documents/conventions-review-log.md`（PO 审约定的记录）、`scrum/ProductBacklog.md`（产品日志，备注里常有 PO 原话）。用 Grep 搜规矩的关键词。
3. **PO 的记忆与反馈**：`S:/SeaPawn-Memory/memory/IDEO-Scrum/`（每条一个文件，`MEMORY.md` 是索引）和 `S:/SeaPawn-Memory/memory/FeedBack/IDEO-Scrum/`。
4. **原书**（判 `原文`）：`plugins/ideo-scrum/skills/scrum-kernel/assets/`、`references/`，`plugins/ideo-scrum/skills/sprint-kernel/events/`，`plugins/ideo-scrum/skills/ideo-kernel/`、`design-kernel/` 下的摘录文件。

一条规矩可以有几项依据；至少要有一项能让别人顺着找到。

## 守则

- 只读：只允许 `git log`、`git show`、`git grep` 之类读命令，和 Read、Grep、Glob。不要 `git commit`、`checkout`、`reset`、`stash`，不要联网，不要改任何已有文件。
- 只写你自己的输出文件（路径在任务里给）。分几次写也行：每标完三四条就**覆盖写一次**，避免做到一半丢了。
- 每条规矩都要有一个对象，顺序照 id；不跳条。
- 你的判断是建议，PO 会逐条过目，不用替 PO 圆场，也不用写得漂亮：短、准、可查。
- 拿不准就把 `confidence` 写低，写下你查了什么。不要为了“有结果”而编。
- 全部做完，只回一句话：写了哪个文件、共几条、其中几条 `无据`、几条 `confidence` 低。
