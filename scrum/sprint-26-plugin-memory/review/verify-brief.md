# 核验说明（Sprint 26 行 2 的核验）

你是核验员。另一位标注员给 111 条旧规矩各写了一份标注（出处、依据、建议、理由）。依据里的提交、路径、引文已由脚本核对过真实存在，**你不用再核这些**。你要核的是**判断对不对**：理由里说的事实对不对，建议会不会让规矩悄悄丢掉。

只读：不改仓库里任何文件，不联网；只写任务里给你的那个输出文件。

## 仓库根与路径

**仓库根**＝`S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory`。你的当前目录**不是**它，所以读文件、跑命令都写绝对路径（仓库根 + 相对路径）；git 用 `git -C S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory …`。下面和标注里写的 `plugins/…`、`scrum/…`、`scripts/…` 都是相对仓库根的。

## 背景

插件 `ideo-scrum` 有六份“约定”文件，共 111 条编号规矩。本期要把它们收成 **Memory**：一份短清单（一行一条）加几个长文件，旧约定文件之后会**删掉**，Memory 是唯一一份。所以：建议“删”或“不进 Memory”的内容，必须真的在别处有同样的内容，否则就是丢了。别处指：模板文件（`plugins/ideo-scrum/skills/*/conventions/*-template.*`）、检查脚本（`scripts/`）、SKILL.md、命令（`plugins/ideo-scrum/commands/`）、或另一条保留的规矩。**插件要给别的用户用**：不能以“作者私人的记忆文件里有”（`S:/SeaPawn-Memory/…`）为由删——别的用户没有那些文件。

## 你拿到什么

任务里给一组 id（如 `sprint-log#1-9`）。看旧规矩原文用：

```
python -X utf8 -I S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory/scrum/sprint-26-plugin-memory/scripts/show_rule.py sprint-log#1-9
```

标注在 `S:/IDEO-Scrum/.claude/worktrees/sprint-26-plugin-memory/scrum/sprint-26-plugin-memory/review/annotations/*.json`（每条一个对象；用 Grep 搜 `"id": "sprint-log#7"` 找，或 Read 整个文件）。字段含义：

| 字段 | 取值 |
| --- | --- |
| `source` | `原文`｜`PO 原话`｜`作者`｜`补充`｜`无据` |
| `basis` | 依据列表（提交、归档路径、PO 原话、原书引文），已核实存在 |
| `kind` | `规矩`（该照着做的行为）｜`格式`（字段、列、模板结构）｜`说明`（解释、指路） |
| `home` | `清单`（一行说清）｜`长文件`（细则多，清单留索引）｜`不进 Memory`（留在模板、命令或别处） |
| `recommend` | `留`｜`改`｜`并`｜`删`；`并` 时 `merge_into` 指并入哪一条 |
| `reason` | 标注员的理由（你要核的主要对象） |
| `dups` | 与它说同一件事的其他规矩 |
| `confidence` | `高`｜`中`｜`低` |

## 四件要核的事（任务会告诉你这一轮看哪两件）

1. **理由里的事实对吗**：理由里凡是说“某处已有”“已重复”“编号指不到”“出自某书”“PO 定的”，都去对原文或文件。说错的记下来。
2. **会不会丢规矩**：建议是删、并、不进 Memory、或“改成一行”时，旧规矩里有没有一句**行为要求**会因此消失、又没写进理由里的去处？有就记下是哪一句。
3. **出处对吗**：`source` 与旧规矩的实际来源相符吗（比如条文自带 `*Supplement*` 标签、引了书的原句、写了 `Departs`）？`PO 原话` 必须真是 PO 说的话，不是助手或 Master 写的。
4. **类别与去处合理吗**：`kind`、`home` 有没有明显不合理的，或与 `recommend`、`reason` 自相矛盾（例如 `home` 写“清单”而理由说“归模板”）。

## 已知容易出错的地方（先查这几类）

- **互相并入成环**：A 并入 B，B 又并入 A。并只能单向：一条留，另一条并入它。
- **“别处已有”没核实**：理由说“模板或检查脚本已覆盖”就必须打开那个模板或脚本，指出文件和位置，确认真有同样的要求；一个只读那一处的人真能照着做吗？说不出来的，记为 `fix`，建议改为留或进长文件。
- **编号指路说错**：理由说“旧编号指不到任何一条”，要对着文件确认（约定文件里的 `convention N` 常指真存在的条）。
- **以作者私人记忆为由删**：不行（见“背景”）。
- **并入的目标并不真说同一件事**：打开目标那一条，对照原文。
- **一条里装了几件事，却只写了一件的去处**：其余几件去了哪里？

## 输出

写到任务给你的输出文件：一个 JSON 数组，**每条规矩一个对象**，顺序照 id：

```json
{ "id": "sprint-log#3", "verdict": "ok", "issues": [], "fix": null }
```

- `verdict`：`ok`（这一轮看的事没问题）｜`fix`（有错，你给出改法）｜`doubt`（拿不准，要人看）。
- `issues`：字符串列表，每项一句话，指出哪里不对、对着原文哪一句（写出文件与位置）。
- `fix`：`verdict` 是 `fix` 时，写成一个对象，只放要改的字段，例如 `{"reason": "…新的理由…", "recommend": "留", "home": "清单", "source": "作者", "confidence": "中"}`；可改字段：`reason`、`recommend`、`merge_into`、`home`、`kind`、`source`、`confidence`。`reason` 保持一两句中文。不要改 `basis`、`id`。
- 没问题就写 `ok`，别硬找毛病；有问题也别客气。
- 用 Write 一次写全；写完用 Read 读回，确认是合法 JSON、条数对（没有漏条、重复条）。

## 守则

- 只读命令（`python … show_rule.py`、`git -C … log/show/grep`）与 Read、Grep、Glob；不改已有文件；只写你的输出文件。
- 不知道就写 `doubt`，别猜；写 `fix` 时要有你亲眼看到的依据（文件与位置）。
