# 核验说明（Sprint 26 行 2 的核验）

你是核验员。另一位标注员给 111 条旧规矩各写了一份标注（出处、依据、建议、理由）。依据里的提交、路径、引文已由脚本核对过真实存在，**你不用再核这些**。你要核的是**判断对不对**：理由里说的事实对不对，建议会不会让规矩悄悄丢掉。

只读，不改仓库里任何已有文件；只写你自己的输出文件。

## 背景

插件 `ideo-scrum` 有六份“约定”文件，共 111 条编号规矩。本期要把它们收成 **Memory**：一份短清单（一行一条）加几个长文件，旧约定文件之后会**删掉**，Memory 是唯一一份。所以：建议“删”或“不进 Memory”的内容，必须真的在别处有同样的内容，否则就是丢了。别处指：模板文件（`plugins/ideo-scrum/skills/*/conventions/*-template.*`）、检查脚本（`scripts/`）、SKILL.md、命令（`plugins/ideo-scrum/commands/`）、或另一条保留的规矩。**插件要给别的用户用**：不能以“作者私人的记忆文件里有”（`S:/SeaPawn-Memory/...`）为由删——别的用户没有那些文件。

## 你拿到什么

一组 id（如 `sprint-log#1-13`）。看旧规矩原文和标注：

```
python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/show_rule.py sprint-log#1-13
```
标注在 `scrum/sprint-26-plugin-memory/review/annotations/*.json`（每条一个对象，字段见 `scrum/sprint-26-plugin-memory/review/annotation-brief.md`；用 Grep 按 `"id": "sprint-log#7"` 找，或 Read 整个文件）。

## 对每条规矩判四件事

1. **理由里的事实对吗**：理由里凡是说“某处已有”“已重复”“编号指不到”“出自某书”“PO 定的”，都去对原文或文件。说错的记下来。
2. **会不会丢规矩**：建议是删、并、不进 Memory、或“改成一行”时，旧规矩里有没有一句**行为要求**会因此消失、又没写进理由里的去处？有就记下是哪一句。
3. **出处对吗**：`source` 与旧规矩的实际来源相符吗（比如条文自带 `*Supplement*` 标签、引了书的原句、写了 `Departs`）？
4. **类别与去处合理吗**：`kind`（规矩／格式／说明）、`home`（清单／长文件／不进 Memory）有没有明显不合理的。

## 输出

写到你的输出文件：一个 JSON 数组，**每条规矩一个对象**，顺序照 id：

```json
{ "id": "sprint-log#3", "verdict": "ok", "issues": [], "fix": null }
```

- `verdict`：`ok`（没问题）｜`fix`（有错，你给出改法）｜`doubt`（拿不准，要人看）。
- `issues`：字符串列表，每项一句话，指出哪里不对、对着原文哪一句。
- `fix`：`verdict` 是 `fix` 时，写成一个对象，只放要改的字段，例如 `{"reason": "…新的理由…", "recommend": "留", "home": "清单", "source": "作者", "confidence": "中"}`。`reason` 保持一两句中文。不要改 `basis`、`id`。
- 没问题就写 `ok`，别硬找毛病；有问题也别客气。

## 守则

- 只读命令与 Read、Grep、Glob；不改已有文件；不联网。只写你的输出文件，分几次覆盖写也行。
- 全部做完，只回一句话：写了哪个文件、共几条、其中 ok／fix／doubt 各几条。
