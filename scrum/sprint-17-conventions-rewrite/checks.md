# 第 5 项：连带改动与引用核对

> 照 checklist.md 第三节。脚本 `check_refs.py` 先拿已知结果自测（`11`、`13–14`、`9 and 11–15`、`6–7` 四条断言），再跑草稿。

## 一、引用核对

- 草稿里共 **171 处**「convention N」引用，**0 处指到不存在的条**（脚本输出 0 问题）。
- 跨文件的引用逐处读过，所指的条确有所引的那句话：

| 引用 | 指向 | 读过的结论 |
| --- | --- | --- |
| sprint-log → overview 15 / 17 / 10 | Working conventions；Goal fixed；Ask the PO | 对：来源标签、目标固定、问 PO |
| sprint-log → product-log 17 / 12 | Fresh at every Review；Items with the Scrum Master | 对：刷新产品日志、选条目 |
| sprint-log → ideo 1 | Design sprint or the five modes | 对：第 6 条第 4 步的分界 |
| sprint-backlog-template → sprint-log 22 / 20 / 24 / 16 / 5 / 6 / 13 / 7 / 9 | 各条 | 对：Now、承诺、拍板、记录测试、选条目、精化、测试先写、How、笔记 |
| sprint-backlog-template → overview 16 | Templates record outputs | 对 |
| product-log → sprint-log 6 / 5 / 17 | Refine、Select、Review | 对 |
| product-log → overview 1 / 5 / 17 / 15 | One product log、Where files go、Goal fixed、Working conventions | 对 |
| product-log → ideo 1 | Design sprint or the five modes | 对：白纸 |
| overview → product-log 2 / 12 | Blank page；Items with the Scrum Master | 对 |
| overview → ideo 1 | Design sprint or the five modes | 对：第 2 条 |
| overview → sprint-log 17 / 24 / 14 / 26 / 7 / 10 / 2 | 各条 | 对：Review、拍板、审阅、跨工具、How、卡住、无截止日 |
| overview → design-log 26 | Gates between stages | 对：改号后的门 |
| design-log → overview 15 / 12 / 7 / 10 / 17 | 各条 | 对：来源标签、拍板、角色卡、问 PO、目标固定 |
| design-log → ideo 1（两处） | Design sprint or the five modes | 对：第 1、27 条 |
| design-log → product-log 2（两处） | Blank page | 对：白纸、结论回流 |
| design-log → sprint-log 19 / 17 | One closing commit；Review | 对：分支、归档 |
| design-template → design-log 24 / 19 / 22 / 6 / 7 / 8 / 10 / 14 / 16 / 18 / 26 | 各条 | 对：Now、收官、五章、共情、专家、地图、发散、合并、原型、判据、门 |
| design-template → sprint-log 17 | Review | 对：归档 |
| scrum-kernel SKILL.md → ideo 1 / product-log 2 / overview 9 | 各条 | 对：分界、白纸、只有 PO 必须是人 |
| ideo 约定 → overview 15 | Working conventions | 对 |

## 二、路径核对

- 草稿里的 `steps/…` 16 个文件名与 Sprint 16 的清单逐一相同；`../scrum-kernel/…`、`../sprint-kernel/…`、`../ideo-kernel/…` 按技能文件夹解析，草稿树里都对得上。
- 已知的例外（不是错）：`drafts/scrum-kernel/SKILL.md` 里 `scrum-guide-2020.md` 两处还是现行写法，Sprint 16 会改成 `assets/`；`product-log.md` 里 `product-backlog-template.md` 是没复制的原件；模板与约定里少数 `overview.md`、`product-log.md`、`sprint-log.md`、`SKILL.md` 是文字说明（写明哪个技能的哪个文件夹），不是路径。

## 三、连带改动

**这一项里查出并已改的两处：**

1. `product-log.md` 第 7 条的地图路径还是旧的 `../design-kernel/define/make-a-map.md` → 改 `../design-kernel/steps/2-1-make-a-map.md`（Sprint 16 的路径）。
2. `overview.md` 的 Departures 表里裸写的 `product-log.md` → 改 `conventions/product-log.md`（PBI-25 ⑦ 的那类写法）。

**搬运时（Sprint 16 合入后）要做的：**

- `design-kernel/SKILL.md` 五阶段表的条号：conventions 6–7、8、9 and 11–14、15、16–17、18、20 → 6–7、8、9 and 11–15、16、17–18、19、21；Use Protocol 第 2 条的 convention 5、23 → 5、24；第 6 条的 convention 20 → 21；第 7 条的 convention 18 → 19。
- `commands/scrum-master.md` 第 48 行「When refinement hits a hard point that needs research, open a design for it (design-kernel skill)」——56 之后这里也是「什么时候开设计」的另一种说法。**Master 2026-11-12 同意改**：改成「…settle whether it needs a design sprint or the five modes (the ideo-kernel's conventions, convention 1)」。只改正文、不动描述，不用跑触发测试。这一行在 Code of Conduct 里，不属于定稿的 Identity。**搬运时在 Sprint 16 的版本上加这一行，不整份替换。**
- `README.md` 的 ideo-kernel 一节（文件表）加一行 `plugins/ideo-scrum/skills/ideo-kernel/conventions/`（新约定）；README 由 Sprint 16 主改，搬运时加。
- `CLAUDE.md` 的「当前状态」与「下一次集中修订是 PBI-54、PBI-58」——收官时更新。

**查过、不改的：**

- 四个命令里的「fresh subagent」都是使用，定义只在 overview 第 7 条；命令不动。
- `sprint-log.md` 第 14 条（46 ③ 的定义在 overview 7）；`scrum-kernel/SKILL.md` 与 `design-kernel/SKILL.md` 的 description 不改（56 的定案）；命令里的加载行归 Sprint 16。
- `codex_readme.md` 只列技能、不列技能内的文件夹，新约定随 `sync_codex.py` 自动带上，说明不用改。

## 四、旧说法残留

- 草稿里：改过的规矩（分界、卡住、过时、Now、跨工具、全新子代理、地图要粗、设计目标是愿景、每份草图拿不同点子）的旧说法 **0 处**（grep 特征句逐一核过）。
- 现行插件里还是旧文本：Sprint 17 没碰 `plugins/`，搬运时整份替换。
