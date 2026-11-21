# Sprint Backlog — Sprint 22 (project-agents)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-22-project-agents-b09bf1` | Product Owner: SeaPawn | Scrum Master: 项目 Scrum Master | Developer: Sprint 22 Developer
> Now: 已收官 · 2026-11-21，Sprint Goal 达成，PO 确认 Review 通过；版本仍为 `6.0.3`，未推送、未发布。
> Waiting for PO: None
> 归档：在办日志全文及逐项证据见 `3ca6b21` 树中的 `SprintBacklog.md`；原始测试记录在仓外 `S:\IDEO-Scrum-Archives\sprint-22-project-agents\`。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。 |
| --- | --- |

这一点服务于[产品化](../../ProductBacklog.md#12-product-goal)：让用户不用借作者的项目配置，也能在自己的项目里拿到独立反馈、继续走流程。

### 1.2 Definition of Done

完整产品 DoD 继续生效（[产品日志 §1.3](../../ProductBacklog.md#13-definition-of-done)），本期重点核验角色职责与方法依据写准、用户能从产品日志找到角色定义、Claude 插件校验与 DSH 现有回归通过。DSH 回归通过不等于已支持项目 Agent。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-73 | 参谋：独立提供第二意见的 Agent | 作为用插件干活的 solo 开发者，我想要在拍板、选方案、评审设计时叫一个只读的子代理独立看一眼，以便拿到第二判断，而不是自己再想一遍 | Map ②、设计冲刺收敛 | S～M |
| PBI-75 | 各项目按角色卡注册 Stakeholder Agent | 作为项目 PO，我想把常用 Stakeholder 角色配置成本项目可复用的 Agent，以便子代理或 Workflow 按名召唤独立反馈 | Map ③、设计测试、⑧ | 待估 |

### 2.2 Refinement 要点

- **PBI-73**：三个意见场景（材料足以纠正前提／原方案有充分依据／缺少关键材料）；取证从不带旧评议的新上下文核对材料、理由与原件、调用记录及被评议产物前后状态，不以意见是否不同作为过线依据。PO 原定「默认 Fable，可另选」；2026-11-20 PO 更新为本轮先用可用模型验证核心功能，具体型号与三态取证留后续配置项，原决定原文保留不改。
- **PBI-75**：四个验收场景（接受配置／拒绝配置／角色卡变更或同名／角色职责与召唤权）；双入口门槛为普通子代理与 Workflow 各自按名命中同一份仅在本项目注册的角色定义并留证；任一入口缺证据记「未验证」，不从另一入口外推。

## 3. How

| # | Work item | Output |
| --- | --- | --- |
| H3 | 参谋 agent 与手动入口 | `plugins/ideo-scrum/agents/advisor.md`；`claude-skills/second-opinion/SKILL.md`（只读、非 fork、默认请求 `fable`、明确请求才召唤） |
| H4–H5 | 项目 Stakeholder 登记、拒绝、更新与双入口复用 | `claude-skills/project-stakeholder/SKILL.md`（按语义读角色卡、预览后成对写入、同名不覆盖、保留 Review 召唤权） |
| H6 | 导航与清单 | `plugin.json` 追加 `skills`；`docs/project-agents.md` 与 `.zh-CN.md` |
| H7 | 正式 Test | 7 个隔离无头场景 + Master 交互双入口补跑；完整 DoD 对账 |

**关键取舍**：参谋用插件专用只读 agent，由手动入口调用；Stakeholder 的一份定义只属于用户项目，登记和引用作为一项变更确认；H2 先查宿主能否提供关键证据，缺证据就停在对应线，不改验收线。

## 4. Increment notes

**PO 收官授权（2026-11-21，用户本人直接消息，逐字）**：「可以，后面你自主决定，收口所有分支，我都review认为通过」

- **授权范围**：Master 自主决定并收口 Sprint 22–25 已开分支，包括 Review 归档、选择与记录 Retro 要点、刷新产品日志、打本地 tag、合入 `main`、清理已合入工作树与分支。
- **排除项（仍归 PO）**：更改 Product Goal／Sprint Goal、取消 Sprint、推翻 PO 已定案、PO 点名品味、修改本仓库 `CLAUDE.md`、对外推送与发布。

**主要过程**：

- **2026-11-20 · H2 前置核验**：PBI-73 首轮 0 样本、US$0.00，记录取证与隔离条件缺口，不进 H3；后经 Master 冻结通道 2 重跑，3/3 完成、415.0 秒、客户端估算 US$0.9527。
- **2026-11-21 · PBI-75 H2**：Master 交互会话完成双入口最小验证；同轮不热注册、下一轮用户消息边界生效；Workflow 会透传触发当轮原话。
- **2026-11-21 · H3–H6 施工**：`a9c3eaa` 参谋与入口、`dcf2fd2` 项目 Stakeholder、`c4f578e` 清单与文档、`b88a79b` 按审阅意见修订。
- **2026-11-21 · H7**：7 个隔离无头场景跑完，4 次作废均为夹具／守卫缺陷。Master 用场景 S4 的真实成品在交互会话核验双入口；S1 留作登记与无头行为证据。
- **收官文案修正（`27a75e3`）**：两份说明只承诺向宿主请求模型；说明与登记技能均把新定义生效限于已验证的交互情境。`3ca6b21` 已补明 Sprint Review 的外部视角只由 PO 或 Scrum Master 召唤。

## 5. Test

**PO Review 结论（2026-11-21）**：PO 已审读全部材料、认为不错，Review 通过，授权收口所有分支。H7 全项闭环：Developer 7 个隔离场景全过，Master 交互双入口（普通 `Agent` 与单代理 `Workflow`）均按名命中、各自新上下文、按序加载内核；PBI-73 三场景 3/3，PBI-75 登记、拒绝、更新与同名冲突、职责与 Review 召唤权全过。

| 项 | 结果 |
| --- | --- |
| 有效样本／费用 | 7 个，830.3 秒，客户端估算 US$2.457；另 4 次作废共 US$1.887；合计 US$4.345，未超 US$6.00／30 分钟 |
| 插件校验 | `claude plugin validate --strict` 通过（6 skills／4 commands／1 agent） |
| DSH 回归 | `node --test scripts/check_dsh.mjs` 6/6 |
| 文档 | `check_docs.py` 7 文档／103 链／0 错；`--selftest` 17/17 |
| 描述长度 | 11 个组件均 ≤1024 |

**未验证边界（不得记全 DoD 通过）**：

- **模型三态**（默认 `fable`／明确另选／所选不可用）：单列后续配置项，本期未重测；样本使用通道可用模型，未验证默认路径。
- **Product Outcome 全流程**：「懂 Scrum 的陌生人不问作者走完第一个冲刺」本期未重跑，局部验证不代替。
- **无头 `-p` 的注册边界**：新建定义不在同轮热注册，无头流式会话下一轮边界也不可达；交互会话边界已由 Master 双入口闭环。

**Review 非阻塞意见（9 条，均不阻塞，留待后续）**：① 另选模型缺少具体传参写法；② 角色卡无「何时召唤」栏时缺后续路径；③ 用户召唤 Agent 的示例是内部工具语法，可后续改成 @-mention 或自然语言（若改须按 Review 流程批准并验证）；④ `/project-stakeholder` 命令无参数提示；⑤ `.claude/` 写入另有权限确认；⑥ 新 docs 未进 README／quick-start 导航，等 Sprint 25 合流后统一挂接；⑦ 两入口／三条列项措辞不一致；⑧ `context is clean` 等绝对措辞考虑弱化；⑨ Advisor Fable access 需提醒。

**产品日志去向**：已验收的功能移入产品日志 §3.2；PO 助手角色的写入职责与生成定义的只读边界留给独立的 PO 秘书议题，本期不扩大工具权限。

**PO 决定收官（2026-11-21）**：Review 通过，独立「熟手」审阅无功能阻塞；只修两处宿主／模型说明，不改验收范围。核对承诺原文：「独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。」
