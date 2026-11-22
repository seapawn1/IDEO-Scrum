# PO 中途看一遍：意见账（Sprint 26）

2026-11-23，PO 经 Master 定（Master 转述）：PO 有空，要和 Supporter 一起中途过目 Memory 草稿；本期「PO 免审」改成「PO 中途看一遍」，其余安排不变。

怎么记：

- PO 的意见由 Supporter 照原话、带上时间和会话名转给 Master 和我；意见用句柄指明是哪一行。
- 我在下面的表里逐条记（原话逐字、收到的时间与来源会话），照改，写明怎么改的；跟别的决定冲突的，报 Master 协调，状态写「报 Master」。记法照 `po-word-relayed`：`PO (via Supporter): 原话`，带日期与地点。
- 同步、改稿照常进行，不等 PO 看完。
- **不给句柄改号**；要改号（并、删）的，先在「句柄别名」表里留别名（旧句柄、新句柄、日期、原因），再改。

PO 可读的东西：`memory-draft/MEMORY.md`（清单，103 行）、`memory-draft/details/`（15 个细则文件）、`review/review-index.md`（入口）、`review/review-<文件>.md`（每条旧规矩的旧文、依据、建议、新行）。

## 这一批（2026-11-23，PO 审 Memory 草稿）

- **出处**：PO 在 Supporter 会话（`IDEO # [supporter]-[main]-[support PO]`）2026-11-23 02:55–03:4x 逐条审 `memory-draft/MEMORY.md`；Supporter 整理的原话在 `review/po-review-2026-11-23.md`（原样拷自 Supporter 的 `side-session-notes/…/memory-review-opinions.md`，那个目录不在仓库里，`cmp` 过逐字相同）；Master（`IDEO # [master]-[main]-[manage sprint]`）2026-11-23 转来并写了处置。下表「PO 原话」列照那份文件逐字摘，括号里的 § 是那份文件的章。
- **PO 的口径**（Master 转述；原文件头部）：**只要与 Memory 其它条目、各技能的说法不矛盾，就算过、就保留。** PO 不再看第二遍，Master 复核后进行行 12。
- 这一批改动（含下面 `relay-limits` 的更正）单独一个提交；没有推送、没有合 main。

## 意见账

| 收到的时间 | 来源会话 | 句柄 | PO 原话（逐字） | 我怎么处理 | 状态 |
| --- | --- | --- | --- | --- | --- |
| 2026-11-23（审阅 02:55–03:4x；Master 转来） | PO 在 `[supporter]-[main]-[support PO]`，Master 转 | 引言「不合用的可以改」（§一） | PO (via Supporter): 「好像我们这个插件是封闭系统啊，AI 没有办法去修改这个东西啊对不对？那他怎么去修改呢？」 | 引言与 `details/names.md` 的一节里「override」改成「depart from」：规矩不合用就偏离它，并在日志备注写明做了什么、为什么，不是改插件文件。`override` 还在这几处，行 13 迁引用时一并改成 depart from、grep 到零：`board/board-log.md` 首行、`design-kernel/SKILL.md`、`sprint-kernel/SKILL.md`（其余在要删的旧约定里） | 已改（清单）；行 13 待做 |
| 同上 | 同上 | `ask-the-po`（§一） | PO (via Supporter): 「这里我觉得应该说交给 PO 或者 supporter。」 | 清单行：只有 PO 能定的问题「交给 PO 或 Supporter」；`details/roles.md` 第三步同改 | 已改 |
| 同上 | 同上 | `diverge-first`（§一） | PO (via Supporter): 「什么叫其中一种。用两种方法真的很奇怪。」 | 补回「至少」：at least two methods, at least one ideo-kernel Ideate method（旧规矩原文就是 at least；上一稿压成「two methods, one…」丢了） | 已改 |
| 同上 | 同上 | `sprint-or-modes`（§一） | PO (via Supporter): 「不是说只有原型必须用角色卡的时候才默认……完整的设计一般都是设计冲刺……五阶段法……是零散着用……它是一切的基础」 | 按 PO 的意思重写：由 PO 说用哪种；完整的设计一般走设计冲刺；五模式是一切的基础、零散着用；「只有原型必须拿角色卡测才默认设计冲刺」三处一起删（清单行、flow-maps 的虚线、没有别处）；`details/names.md` 新写一节「The five modes and the design sprint」放五模式是基础、设计冲刺的阶段站在模式上、「IDEO 五阶段法」是五模式本身 | 已改 |
| 同上 | 同上 | `modes-are-not-the-sprint`（§一） | PO (via Supporter): 「谁说的 ideo 不做闪电演示啊，不做故事板啊，这些都不对啊。……这个不对。」 | Master 定整条删（含「IDEO 日志不做 map、Lightning Demos、storyboard」，清单与细则里都清了）。还对的两点用正面说法挪走：①「IDEO 五阶段法」指五模式本身→`details/names.md`；②在设计里用的方法，产出写进那个阶段的设计日志章节→`ideo-in-every-stage`，`open-ideo-log` 加「在设计之外」，免得在设计里「方法多了就开 IDEO 日志」误触发。旧规矩 ideo-log#2 那句记成 dropped，理由「PO 2026-11-23 反对」 | 已改 |
| 同上 | 同上 | `ideo-log-home`（§一；Master 加：IDEO 日志这一节去重） | PO (via Supporter): 「这个不是重复了吗，和上面有一条。你这个 IDU 日志写的有点多了……稍微有点乱」 | IDEO 日志这一节由 7 行收成 4 行：`sprint-or-modes`、`research-as-empathize`、`open-ideo-log`、`ideo-log-ends`。`ideo-log-home` 并入 `open-ideo-log`（指针指到 `details/ideo-ending.md`）；`read-mode-file` 删（先读模式与方法的文件，ideo-kernel 的 Use Protocol 里有；章里放什么写在细则）；文件夹、For 格、无承诺都在 `details/ideo-ending.md`，文件夹清单在 `details/folders.md`，不再两行说同一件事。一个分句都没丢（分句核查通过） | 已改 |
| 同上 | 同上 | `acceptance-when-written`（§一） | PO (via Supporter): 「什么叫只在这个地方让我验收，这不就是前后矛盾吗」「只要不矛盾的话，那这个就可以留……不能和我们其他的记忆，或者说我们的技能什么的出现矛盾」 | 去掉 only：PO 验收照 DoD 和验收条件来；那里没要求的，PO 看一眼就够。与 `reviewer-required`、`record-the-tests`（「any required PO acceptance」）、`review-at-close` 对过，不矛盾 | 已改 |
| 同上 | 同上 | `ideate-arrangement`（§二、§四） | PO (via Supporter): 「先提方案可以不写……但是需要等我放行，这个是要说……只需要强调后面这个就可以……让 master 来判断吧」 | Master 判：这一行只强调关卡，不写「先提方案」——Before the PO's go-ahead for Ideate, nobody gathers ideas, sketches or sends out subagents。`details/gates.md` 里的旧文照留，不矛盾 | 已改 |
| 同上 | 同上 | 新加一行（§二，原挂在 `design-conclusions`） | PO (via Supporter): 「每个冲刺就是说他们有异议的点吗，或者说需要很有研究性的点。我可以在 review 和 Retro，阶段分别选择可以落盘到 documents 或者说记忆当中。这个还挺重要的」 | 新行 `disputed-points`，放在 `review-at-close` 后面（收官那几行旁边），不加标签（PO 2026-11-23 定的，算作者的做法）：每期 Sprint 或设计里有异议的点、要深入研究的点，Review 和 Retro 时由 Scrum Master 列出，PO 挑落进 `scrum/documents/` 还是记忆；`details/closing.md` 新一节写全，并写明要做的事照样先进产品日志、开成条目（`no-tbd`、`new-work-registered`）。反向核查里记「PO 2026-11-23 新加」 | 已改 |
| 同上 | 同上 | `facts-then-questions`（§三） | PO (via Supporter): 「可以，这样也可以」 | 保留，不改 | 保留 |
| 同上 | 同上 | `check-script-misses`（§三） | PO (via Supporter): 「既然他有说法的话，那就留着吧虽然我没看懂」 | 保留；写得好懂些、意思不变：When a check script judges wrongly (false alarm or miss), go through the cases one by one and write down why；`details/sprint.md` 里那句也补了「its false alarms and its misses」 | 已改 |
| 同上；又在 Master 会话（2026-11-23）、对 Supporter 说 | 同上；PO 亲口在 Master 会话 | `relay-limits`（§四） | PO (via Supporter): 「可以 support 说，就是或者受得到授权的 supporter。我觉得这样好一点。」（审 Memory 时，Supporter 会话，2026-11-23 02:5x）；PO (via Supporter): 「我刚才说 supporter 转发的其实算是对的，只要得到了 PO 的授权。」（对 Supporter，之后）；PO (in Master's session): 「我授权之后，然后我让 supporter 去发，那实际上也认为是我的意见」（2026-11-23，Master 转来） | **放宽，照 PO 的意思**（Master 先说「不放宽」，随后更正：PO 已明确定了，不是交 Master 判）：工具权限与设置、`CLAUDE.md`／`AGENTS.md`、推送与发布这几类，经 PO 授权的 Supporter 转达也算 PO 的话，不再写「要 PO 亲口」；转达要写明 PO 何时、在哪里授权这个 Supporter。清单行 `relay-limits`（句柄不改）改成 Permissions, settings, CLAUDE.md/AGENTS.md, pushes, releases: only an authorized Supporter may relay（行尾带 Read details/roles.md first.，授权的时间、地点要写明放在细则；Master 2026-11-23 的小改：原句「say when and where that was」指代不清）；`details/roles.md` 三处对齐（`ask-the-po` 第三步「needs the PO in person」那半句、`po-word-relayed` 那一条、「What goes to the PO in any case」的前言），并写了宿主这一层：宿主只认动手会话里用户确认的事，宿主要确认的（权限提示、设置、`CLAUDE.md`），由 PO 到那个会话确认，Claude Code 就是这样，这样插件不跟宿主冲突。分句核查里记 reworded，理由「PO 2026-11-23 改」。落盘时要同步改 `commands/supporter.md`（第 2、25、34 行）；`overview.md` 约定 12、14 随旧约定转成 Memory，行 12 之后那段如果还在就同步改 | 已改；`commands/supporter.md` 待行 12／13 |
| 同上 | 同上 | §五 机制问答：`role-entry`、`product-log-header`、`dod-in-product-log`、`acceptance-written-once`、`read-the-goal`、`developer-elsewhere`、`fresh-subagent`、「落地」、内核引用 | PO (via Supporter): （PO 问的是「什么意思」「没看懂」，原话与回答要点在 `review/po-review-2026-11-23.md` §五） | 已解释，无需改（Supporter 已答）；`read-the-goal`、`developer-elsewhere`、`fresh-subagent` 的措辞 PO 说没看懂，意思对、PO 口径是不矛盾就留，没有改 | 无需改 |
| 同上 | 同上 | §六 题外：删两个 PBI | PO (via Supporter): 「既然我现在对这些条目都省略了，那我们有一个 PPI 就可以删掉了」（PBI-91 决定不做；另一条未点名） | 不是这份草稿的事：产品日志的改动由 Master／Supporter 做，我没动；另一条哪个，要 PO 确认 | 交 Master／Supporter |

## 句柄别名

| 旧句柄 | 新句柄 | 日期 | 原因 |
| --- | --- | --- | --- |
| `modes-are-not-the-sprint` | （删）；还对的两点：`sprint-or-modes`＋`details/names.md`「The five modes and the design sprint」（IDEO 五阶段法＝五模式）、`ideo-in-every-stage`（设计里用的方法，产出写进阶段章节） | 2026-11-23 | PO 反对「IDEO 日志不做 map、Lightning Demos、storyboard」；Master 定整条删 |
| `read-mode-file` | （删）：ideo-kernel 的 Use Protocol；章里放什么、先读模式与方法的文件→`details/ideo-ending.md`「When to open an IDEO log」 | 2026-11-23 | 与 `ideo-in-every-stage`、ideo-kernel 的 Use Protocol 重复（Master） |
| `ideo-log-home` | `open-ideo-log`（指针到 `details/ideo-ending.md`）；文件夹等在 `details/ideo-ending.md`「Where it lives」 | 2026-11-23 | PO：与上面一条重复，IDEO 日志这一节偏多偏乱 |
| （新）`disputed-points` | — | 2026-11-23 | PO 新加（Review 与 Retro 时列出有异议、要深入研究的点） |

清单现在 103 个句柄（原 105，删 3、加 1）。

## 待 PO 看（我带上的开放点，Supporter 陪 PO 审时一并带上）

| 句柄与位置 | 是什么 | 我现在的做法 |
| --- | --- | --- |
| 设计清单里「git 动作须明确许可」（`details/roles.md`「What goes to the Product Owner in any case, by stage」设计那张，关联 `outward-needs-po`、`log-is-the-handoff`、`stage-gates`） | 旧的设计规矩要求 commit、merge、删分支、push 在执行前都要 PO 明确许可，比旧的冲刺规矩严（冲刺只要求提交在放行范围内） | 转换时不改含义，照旧文保留；PO 若要冲刺与设计一样，在这里说（2026-11-23 Master 定） |
