# 来源与授权

本仓库是方法论插件，内容分为两类：

1. **原创部分** —— 插件结构、skill 组织方式、agent 定义、工作记录（`scrum/`，含 `scrum/documents/`）。以 [MIT](LICENSE) 发布。
2. **第三方摘录** —— 来自下列公开方法论材料。各自的许可条款以本文件所列为准，**不受 MIT 覆盖**。

本仓库**不包含任何书籍全文或原始出版物**。所有第三方内容均为带署名的方法摘录。若这些方法论对你有价值，请通过官方渠道获取原作。

---

## 1. The Scrum Guide (November 2020)

| 项 | 内容 |
|---|---|
| 作者 | Ken Schwaber, Jeff Sutherland |
| 版权 | © 2020 Ken Schwaber and Jeff Sutherland |
| 许可 | **CC BY-SA 4.0** — https://creativecommons.org/licenses/by-sa/4.0/legalcode |
| 原始出处 | https://scrumguides.org/ |
| 本仓库位置 | `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-2020.md`（全文）<br>`plugins/ideo-scrum/commands/scrum-master.md`、`plugins/ideo-scrum/commands/developer.md`（角色命令主体抄录）<br>`plugins/ideo-scrum/skills/memory/details/`（`roles.md`、`goal-fixed.md`、`sprint.md`、`departures.md` 里的嵌入引用，文件头与句中注明出处） |
| 修改说明 | 2020 版全文随源文件提供，未作节选；Artifact 与 Event 的分项摘录来自 SGEP，登记在本档第 2 节。角色命令主体为原文抄录，署名统一在本档登记（命令不设文件头）。 |

**ShareAlike 提示**：若你基于上述文件制作衍生作品并分发，衍生部分同样须以 CC BY-SA 4.0 发布。

---

## 2. Scrum Guide Expansion Pack (2026.1)

| 项 | 内容 |
|---|---|
| 作者 | Ralph Jocham, John Coleman, Jeff Sutherland |
| 版权 | © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland |
| 许可 | **CC BY-SA 4.0** — https://creativecommons.org/licenses/by-sa/4.0/legalcode |
| 原始出处 | https://scrumexpansion.org/scrum-guide-expanded/ |
| 本仓库位置 | `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md`（v2026.1 除 Artifacts、Events 两章以外的部分）<br>`plugins/ideo-scrum/skills/scrum-kernel/references/`（Artifacts 两章拆成的 4 份摘录）<br>`plugins/ideo-scrum/skills/sprint-kernel/events/`（Events 两章拆成的 5 份摘录）<br>`plugins/ideo-scrum/skills/scrum-kernel/SKILL.md`、`plugins/ideo-scrum/skills/sprint-kernel/SKILL.md`（SGEP 句的嵌入引用）<br>`plugins/ideo-scrum/commands/scrum-master.md`、`plugins/ideo-scrum/commands/developer.md`（角色命令的 2026 精炼补充）<br>`plugins/ideo-scrum/commands/stakeholder.md`（Stakeholder 角色内容——SGEP 角色章精炼改写）<br>`plugins/ideo-scrum/commands/supporter.md`（Supporter 角色内容——SGEP 的 Supporter 一节与开篇概述，精炼改写并含原文短语；只取「照请求做事」一面，为作者的取舍）<br>`plugins/ideo-scrum/skills/memory/details/`（`departures.md` 里的嵌入引用，文件头与句中注明出处） |
| 修改说明 | v2026.1 的 Artifacts、Events 两章抽成 `references/` 与 `events/` 的单份文件，`assets/` 里是其余部分；原文措辞未改动。`sprint-kernel/SKILL.md` 的加载正文逐字带入 Sprint Backlog 节（含 Sprint Goal 子节），并指向原摘录。角色命令（scrum-master / developer / stakeholder / supporter）中的 SGEP 内容为精炼改写（含原文短语），署名统一在本档登记。 |

**注意**：Scrum Guide Expansion Pack 由上述三位作者编写，托管于 scrumexpansion.org，**并非 Scrum.org 出品**。该站点上另有一份 "AI and Scrum" 文档采用 CC BY-NC-ND 许可，本仓库未使用。

---

## 3. Stanford d.school — Design Process Mini-Guide (2010) 与 Design Thinking Bootleg (2018)

五模式（`IDEO-modes/`）由 d.school 的两份材料合并而成：2010 年的 *Design Process Mini-Guide* 是底本，2018 年的 *Design Thinking Bootleg* 补料。两份的许可版本不同，分列如下；方法库（`methods/`）只来自 2018 年的 Bootleg。

### 3.1 Design Process Mini-Guide（2010，五模式的底本）

| 项 | 内容 |
|---|---|
| 出品 | Hasso Plattner Institute of Design at Stanford University (d.school)；PDF 封面题 *An Introduction to Design Thinking — Process Guide*，所在维基页题 *Design Process MiniGuide* |
| 许可 | **CC BY-NC-SA 3.0 Unported** — https://creativecommons.org/licenses/by-nc-sa/3.0/legalcode |
| 许可依据 | d.school「Design Resources」维基首页的声明：「The resources in this wiki by Hasso Plattner Institute of Design at Stanford are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.」声明在维基首页（覆盖该维基里的资源），不在该页或 PDF 内；原站已下线，以下面的存档为证；未另向 d.school 取得书面确认。 |
| 原始出处 | 维基页 https://dschool.stanford.edu/groups/designresources/wiki/36873/Design_Process_MiniGuide.html（已下线）。存档：[维基首页（2016-03-15）](https://web.archive.org/web/20160315073719/https://dschool.stanford.edu/groups/designresources/)、[PDF `ModeGuideBOOTCAMP2010L.pdf`（2016-01-18）](https://web.archive.org/web/20160118010517/https://dschool.stanford.edu/sandbox/groups/designresources/wiki/36873/attachments/74b3d/ModeGuideBOOTCAMP2010L.pdf) |
| 本仓库位置 | `plugins/ideo-scrum/skills/ideo-kernel/IDEO-modes/`（五个文件的底本） |
| 修改说明 | 五模式内容重组为 WHAT / WHY / HOW 三层结构并补充模式间衔接。 |

### 3.2 Design Thinking Bootleg（2018，五模式的补料与方法库）

| 项 | 内容 |
|---|---|
| 出品 | Hasso Plattner Institute of Design at Stanford University (d.school) |
| 许可 | **CC BY-NC-SA 4.0** — https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode |
| 原始出处 | https://dschool.stanford.edu/tools/design-thinking-bootleg（许可标注在这个页面上；它指向的 PDF 本身没写许可，第 90 页标 Bootleg 2018） |
| 本仓库位置 | `plugins/ideo-scrum/skills/ideo-kernel/IDEO-modes/`（五模式的补料，见下表）<br>`plugins/ideo-scrum/skills/ideo-kernel/methods/`（方法库） |
| 修改说明 | 方法库条目补充 Use Before / Use Notes / Do Not Use When 字段。 |

五模式里 2018 补料的对应（对 2018 PDF 逐词比对）：

| 模式 | 补料文本块 | 2018 PDF 页 | 当前文件里的情况 |
| --- | --- | --- | --- |
| Empathize | 8 | 3–4 | Immerse 一段由两块拼接，不声称原件有这一整段 |
| Define | 6 | 5–6 | 其中一处由两项合并改写，不是逐字抄录 |
| Ideate | 9 | 7–8 | 含两处拼接 |
| Prototype | 7 | 9–10 | 含两处压缩改写 |
| Test | 8 | 11–12 | 合并结果没有保留 2018 的独有表述，正文以 2010 底本为本 |

> **⚠️ NonCommercial 提示**
>
> 上述两份许可都**含非商业限制**。这意味着以本仓库的 `ideo-kernel` 内容为主要目的的商业使用（如作为付费咨询或培训的交付物）不在该许可授权范围内。
>
> 本仓库整体因此**不构成 OSI 定义下的开源软件**。若你的使用场景涉及商业用途，请自行评估或直接联系 d.school。

---

## 侵权处理

若你是上述任一材料的权利人，认为本仓库的使用超出了许可范围，请通过 GitHub Issue 联系，我会及时移除或修改相关内容。

---

## 免责声明

上述各来源的原作者与出品方**未对本仓库作任何形式的背书**，亦不对本仓库内容的准确性或适用性承担责任。本仓库是独立的第三方整理，与 Scrum.org、scrumexpansion.org、Stanford d.school、IDEO 均无关联。
