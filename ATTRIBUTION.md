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
| 本仓库位置 | `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-2020.md`（全文）<br>`plugins/ideo-scrum/skills/scrum-kernel/references/`（按 Artifact 拆分的摘录）<br>`plugins/ideo-scrum/skills/sprint-kernel/events/`（按 Event 拆分的摘录）<br>`plugins/ideo-scrum/commands/scrum-master.md`、`plugins/ideo-scrum/commands/developer.md`（角色命令主体抄录）<br>`plugins/ideo-scrum/skills/scrum-kernel/conventions/`（约定里的嵌入引用，句中注明出处） |
| 修改说明 | 全文按 Scrum 的 Artifact 与 Event 拆分重排为独立文件，供 agent 按需检索。原文措辞未改动；角色命令主体为原文抄录，署名统一在本档登记（命令不设文件头）。 |

**ShareAlike 提示**：若你基于上述文件制作衍生作品并分发，衍生部分同样须以 CC BY-SA 4.0 发布。

---

## 2. Scrum Guide Expansion Pack (2026.1)

| 项 | 内容 |
|---|---|
| 作者 | Ralph Jocham, John Coleman, Jeff Sutherland |
| 版权 | © 2025 Ralph Jocham, John Coleman, and Jeff Sutherland |
| 许可 | **CC BY-SA 4.0** — https://creativecommons.org/licenses/by-sa/4.0/legalcode |
| 原始出处 | https://scrumexpansion.org/scrum-guide-expanded/ |
| 本仓库位置 | `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md`（v2026.1 除 Artifacts、Events 两章以外的部分）<br>`plugins/ideo-scrum/skills/scrum-kernel/references/`（Artifacts 两章拆成的 4 份摘录）<br>`plugins/ideo-scrum/skills/sprint-kernel/events/`（Events 两章拆成的 5 份摘录）<br>`plugins/ideo-scrum/skills/scrum-kernel/SKILL.md`、`plugins/ideo-scrum/skills/sprint-kernel/SKILL.md`（SGEP 句的嵌入引用）<br>`plugins/ideo-scrum/commands/scrum-master.md`、`plugins/ideo-scrum/commands/developer.md`（角色命令的 2026 精炼补充）<br>`plugins/ideo-scrum/commands/stakeholder.md`（Stakeholder 角色内容——SGEP 角色章精炼改写）<br>`plugins/ideo-scrum/skills/scrum-kernel/conventions/`（约定里的嵌入引用，句中注明出处） |
| 修改说明 | v2026.1 的 Artifacts、Events 两章抽成 `references/` 与 `events/` 的单份文件，`assets/` 里是其余部分；原文措辞未改动。角色命令（scrum-master / developer / stakeholder）中的 SGEP 内容为精炼改写（含原文短语），署名统一在本档登记。 |

**注意**：Scrum Guide Expansion Pack 由上述三位作者编写，托管于 scrumexpansion.org，**并非 Scrum.org 出品**。该站点上另有一份 "AI and Scrum" 文档采用 CC BY-NC-ND 许可，本仓库未使用。

---

## 3. Stanford d.school — Design Thinking Bootleg

| 项 | 内容 |
|---|---|
| 出品 | Hasso Plattner Institute of Design at Stanford University (d.school) |
| 许可 | **CC BY-NC-SA 4.0** — https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode |
| 原始出处 | https://dschool.stanford.edu/tools/design-thinking-bootleg |
| 本仓库位置 | `plugins/ideo-scrum/skills/ideo-kernel/IDEO-modes/`（五模式 WHAT/WHY/HOW；设计冲刺的原书摘录在 `design-kernel/`，属第 4 节 Knapp 来源）<br>`plugins/ideo-scrum/skills/ideo-kernel/methods/`（方法库） |
| 修改说明 | 五模式内容重组为 WHAT / WHY / HOW 三层结构并补充模式间衔接；方法库条目补充 Use Before / Use Notes / Do Not Use When 字段。 |

> **⚠️ NonCommercial 提示**
>
> 上述文件采用的许可**含非商业限制**。这意味着以本仓库的 `ideo-kernel` 内容为主要目的的商业使用（如作为付费咨询或培训的交付物）不在该许可授权范围内。
>
> 本仓库整体因此**不构成 OSI 定义下的开源软件**。若你的使用场景涉及商业用途，请自行评估或直接联系 d.school。

---

## 4. Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days

| 项 | 内容 |
|---|---|
| 作者 | Jake Knapp, with John Zeratsky and Braden Kowitz |
| 出版 | Simon & Schuster, 2016 |
| 许可 | **全版权保护**（All Rights Reserved），无开放许可 |
| 官方网站 | https://www.thesprintbook.com/ |
| 本仓库位置 | `plugins/ideo-scrum/skills/design-kernel/steps/`（设计冲刺原书摘录，按 IDEO 五阶段编号：`1-1`～`1-3` 共情 define-the-challenge、start-at-the-end、ask-the-experts；`2-1`～`2-3` 定义 make-a-map、how-might-we、pick-a-target；`3-1`～`3-5` 构思 remix-and-improve、sketch、decide、rumble、storyboard；`4-1`～`4-2` 原型 fake-it、prototype；`5-1`～`5-3` 测试 small-data、interview、learn；例图改画成 Mermaid 或文字） |
| 使用范围 | 设计冲刺各章的**原文摘录**：只删不改，删去与 solo + AI 团队无关的段落（日程、场地与用品、部分长例子）；各文件标注章节出处。原书例图改画成 Mermaid 或文字，不含图片文件。术语保留原文（Decider、Facilitator 等）；对应到本插件角色的写法、作者的做法另放 `design-kernel/conventions/`，标为约定。 |

> **请支持正版**
>
> 本仓库摘录了该书讲方法的多章原文（有删节），不含书中图片文件，也不含全书。摘录无法替代原书。
> 若 Design Sprint 方法对你有用，请购买原书：https://www.thesprintbook.com/

---

## 侵权处理

若你是上述任一材料的权利人，认为本仓库的使用超出了许可范围，请通过 GitHub Issue 联系，我会及时移除或修改相关内容。

---

## 免责声明

上述各来源的原作者与出品方**未对本仓库作任何形式的背书**，亦不对本仓库内容的准确性或适用性承担责任。本仓库是独立的第三方整理，与 Scrum.org、scrumexpansion.org、Stanford d.school、IDEO、Simon & Schuster 均无关联。
