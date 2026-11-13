# Sprint Backlog — Sprint 18 (rules-first)

> Started: 2026-11-13 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: claude/youthful-payne-b1e139 | Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[support sprint] | Developer: Claude Code（本会话，youthful-payne-b1e139）
> Now: What：精化 · PO 2026-11-13 定 Sprint Goal
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 规矩先顺：日志头部统一，scrum、sprint、design 召唤才来，角色说明写清；看板和 hook 照着就能读，文档照着就能写。（PO 2026-11-13 定） |
| --- | --- |

### 1.2 Definition of Done

| 维度 | 标准 |
| --- | --- |
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 可导航 | 从 SKILL.md 入口 ≤2 跳到达任意 reference |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |
| 插件校验 | `claude plugin validate --strict plugins/ideo-scrum` 通过 |
| 描述长度 | 每个技能的 description 不超过 1024 字符 |
| Codex 包 | 改了插件就跑 `scripts/sync_codex.py`，`scripts/check_codex.py` 通过 |

PO 2026-11-13 定 Sprint Goal

## 2. What

### 2.1 Product Backlog Items

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 |
| --- | --- | --- | --- | --- |
| PBI-66 | 日志头部——承诺、Now、等 PO 的事，决定前引用目标 | 作为熟手（也是 PO），我想要每份日志的头部有固定的一块——承诺一行小表、Now 行、等 PO 的事——阶段决定前先引用目标原文，以便 hook 和看板读得到，AI 做决定时不丢目标 | Map ④ | M |
| PBI-65 | 加载边界——ideo 放开，其余召唤才来 | 作为熟手（也是 PO），我想要 ideo-kernel 在发散、定义问题、做原型、做测试这类请求时就加载，scrum、sprint、design 三个内核只在召唤时加载（用了角色命令，或明说要用），以便平时不被打扰、要用时可控 | Map ② | M |
| PBI-60 | 角色说明——PO 助手是谁，Master 能替你做到哪 | 作为熟手（也是 PO），我想要 stakeholder 命令写明它可以当我的助手——整理产品日志、汇总进度、照我的话派活、维护看板——Master 写明「服务 PO；经书面授权在范围内代行，问责仍在 PO」，以便我一眼找到对的角色，也不让 AI 自己拍板 | Map ② | S |

### 2.2 Refinement

**草稿，待 PO 定。** 当前只做七步的第 1–5 步；未完成复述确认（第 6 步），PO 未宣布精化结束（第 7 步）。PBI-62 不在本冲刺。

采用 IDEO Define 模式的 How Might We Questions：从各条用户故事拆出可讨论的小问题，不把方案藏进问题里。已读 ideo-kernel 的 `methods/how-might-we-questions.md`；产出记在本节，不另开设计或 IDEO 日志。

**PBI-66：先定给 Sprint 19 读的接口**

**1. 条目**：PBI-66；先于 PBI-65、60 定头部格式，供主线 PBI-35、61 使用。

**2. 观点原文**：作为熟手（也是 PO），我想要每份日志的头部有固定的一块——承诺一行小表、Now 行、等 PO 的事——阶段决定前先引用目标原文，以便 hook 和看板读得到，AI 做决定时不丢目标

**3–4. HMW、不清楚的点与归属（草稿）**

| 编号 | HMW / 不清楚的点 | 归谁 | Developer 建议，尚非决定 |
| --- | --- | --- | --- |
| 66-1 | HMW 让人和两个读取方找到同一份承诺，不各抄一份？小表留在原章节，还是集中在文件头？ | PO 定；Developer 提接口 | 建议集中在文件头；原有章节标题保留，正文不再复写承诺。Now 与 Waiting for PO 各一行；不加 YAML 或另一份状态文件。四种确切样式见下文 |
| 66-2 | HMW 让 IDEO 日志也能报现状，而不把五模式变成另一个设计冲刺？IDEO 日志没有自己的目标承诺，小表写什么？ | PO 定；Developer 核对现有约定 | 建议 IDEO 日志不造第五种承诺；保留 Question、For，并统一 Now、Waiting for PO。读取方沿 For 找所服务日志的承诺，不复制父日志原文 |
| 66-3 | HMW 在阶段决定前看见正在兑现的目标？是只引当前目标，还是每次连 Product Goal 一起引？ | PO 定 | 建议 Sprint 决定引本 Sprint Goal，设计冲刺决定引本设计目标，涉及产品方向时另引 Product Goal；IDEO 模式之间不添关卡。引用不出来就先补读，不能编造引用或把决定记成有效 |
| 66-4 | HMW 让头部显示事实，而不是另一份待办？Now、Waiting for PO 在哪里更新，等不到决定时怎么写？ | Developer 提方案 | 建议同一次日志提交更新两行：阶段 / 模式变化、PO 决定、出现或解除待拍板点时更新；Waiting for PO 只写事项编号与短句，无事写 None。具体选项、证据仍只写正文 |
| 66-5 | 既有日志与新模板如何交接，怎样让主线不猜字段？ | Developer 提方案 | 建议 PO 定下接口后先把确切格式交 Master，再改四份模板与相应约定；新写日志使用。已归档日志不回改，进行中的 Sprint 18 不整份迁移；主线据已定格式准备读取方 |

**66 的头部具体提案（草稿，待 PO 定）**

以下是未来模板的候选头部，不是本冲刺已施行的约定。每块接回原模板的全部章节，章节标题不增删。字段名是固定的 `Now`、`Waiting for PO`；承诺小表左格固定「承诺」，右格逐字放原文，不加粗。`Product:`、`Product Goal:`、`Sprint Goal:`、`Design goal:` 是表的类型标签，不是新章节；目标原文保留自己的短名。承诺在头部只存一份，原有目标节只保留说明和头部指引。英文模板里的「承诺」是否保留为中文，包含在 66-1 的接口审定中；建议本轮先沿用 PO 已定的字面值，不擅译成另一个读取键。

产品日志：

```markdown
# Product Backlog — <product>

> Product Owner: <name> | Started: <date>
> Now: <当前工作；最近一次 PO 决定>
> Waiting for PO: <待拍板事项编号与短句；无则 None>

Product:
| 承诺 | <Product 原文> |
| --- | --- |

Product Goal:
| 承诺 | <Product Goal 原文> |
| --- | --- |
```

冲刺日志：

```markdown
# Sprint Backlog — Sprint <NN> (<short name>)

> Started: <date> | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: <branch> | Product Owner: <name> | Scrum Master: <who> | Developer: <who>
> Now: <当前阶段；最近一次 PO 决定>
> Waiting for PO: <待拍板事项编号与短句；无则 None>

Sprint Goal:
| 承诺 | <Sprint Goal 原文> |
| --- | --- |
```

设计日志：

```markdown
# Design Backlog — <suffix>

> Opened <date> | From: <来源> | Branch: <branch> | Product Owner: <name> | Designer: <who> | Scrum Master: <who>
> Now: <当前阶段；最近一次 PO 决定；下一步>
> Waiting for PO: <待拍板事项编号与短句；无则 None>

Design goal:
| 承诺 | <设计目标原文> |
| --- | --- |
```

IDEO 日志：

```markdown
# IDEO Backlog — <suffix>

> Opened <date> | Question: <本日志回答的问题> | For: <所服务日志的相对路径> | Product Owner: <name> | Who runs it: <who>
> Now: <当前模式；下一步>
> Waiting for PO: <待拍板事项编号与短句；无则 None>
```

IDEO 的例外待 66-2 决定：现行 `ideo-log.md` 只给它 Question、For，没有第五个目标或模式间关卡。建议不为表面一致而编一张本级承诺表。四块之后保留各模板原有的写法 / 来源 / 结束说明；上面只列共享读取接口，不删那些说明。

**5. 切块与验收草稿**

| 块 | 产出 | 验收草稿 |
| --- | --- | --- |
| 66-A（一个会话） | PO 定下的四种头部接口；四份模板与对应约定的修改稿；发给 Master 的接口位置 | 四个现有承诺各有一个明确的原文位置；四种日志的 Now / Waiting for PO 能定位；不另存状态，不新增 IDEO 目标；主线按已定稿而非猜测准备读取方 |
| 66-B（一个会话） | 决定前引用目标的约定稿与场景测试汇总 | Sprint 与设计冲刺的阶段决定前引出相应目标原文；没读到先补读，不伪造有效决定；IDEO 日志不增加模式间关卡；全仓相关说法一致，历史日志不回改 |

**测试方法与过线草稿**：测试题、样本和判定标准先写在本节，PO 定后单独提交，再运行。静态样本至少覆盖四种日志、Waiting for PO 为 None / 多事项、目标未定；逐项核对读取位置与原文，不用另写 hook 或看板来替代接口验收。动态样本包括 Sprint 阶段决定、设计阶段决定、目标没读到、IDEO 模式切换四种场景，各跑 3 次 Haiku；行为（读目标 / 不加 IDEO 关卡）与内容（原文引用 / 正确停下）分栏，建议每题各 3/3。通过与否由冻结标准判，不因看到结果而改门槛。具体题干在精化定案时补齐。

**PBI-65 / PBI-60**：待补精化草稿；尚无决定。

## 3. How

待 PO 宣布精化结束后由 Developer 起草；当前不先写施工方案。

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

待 How 阶段。

**Risks and open points**

待 How 阶段；2.2 的未定点不在此复写。

Go-ahead: 尚未施工放行；Master 2026-11-13 仅交代开日志、起草精化、在本分支提交，不改插件。

## 4. Increment notes

- 分支名没照约定 1，因为是原生 worktree 生成的名字；收官时 tag 用文件夹名 `sprint-18-rules-first`。

## 5. Test

尚未运行测试；2.2 中都是待 PO 定的测试草稿，不能当作已冻结标准或测试结果。
