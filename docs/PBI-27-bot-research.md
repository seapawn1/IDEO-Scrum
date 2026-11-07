# PBI-27 · Bot 工作方式研究（PBI-23 预研究）

> 日期：2026-11-06。方法：`gh api` 直读仓库文件（未用 WebSearch，3P 网关下不可靠）。
> 定位：只借思想，不抄代码。MIT / Apache-2.0 来源可借鉴并署名；无 AGPL 来源；泄漏提示词未使用。
> 每条结论带出处（仓库/文件/小节）。
> 2026-11-07 由 `scrum/sprint-08/` 移入（Sprint 08 撤销）；更正第 14、20 条，新增第五节「一手复核」。

## 一、五个来源的定位

| 来源 | 许可 | 是什么 | 对 PBI-23 的价值 |
|---|---|---|---|
| `unicodef1wn/grokbot-field-notes` | MIT | xAI Grok Bot 三场直播的整理：规则、验证、编排、69 张角色卡、9 本 playbook、40 条翻车记录 | **主参照**。playbook 骨架、角色卡八节、验证规则、反模式格式 |
| `Fei2411/DS-Bot` | Apache-2.0 | DSH 上的 bot 桌面应用：Chief 主 bot + 群聊 + bot 记忆 + 群目标 | 单一入口、按需召唤、阶段验收 |
| `BotHarness/DeepSeekBot`（Tobs） | MIT | BotHarness 的 PersonaBot 应用 + 内置 pstack 流程指南（pstack 是开发者 poteto 的工作流程，被该仓库放进 `.agents/` 作为自己的开发流程） | 过夜合同、决策日志、原则名、指南写法 |
| `deepseek-ai/deepseek-harness` · `packages/team` | MIT | 会话级 Agent Teams：共享任务板、依赖、CAS、写域 | 看板数据模型（如将来要做共享板） |
| Claude Code Agent Teams 文档 | Anthropic 文档 | 实验特性、默认关：lead + teammates + 共享任务列表 + 互发消息 | 确认我们**不依赖**它 |

## 二、可借鉴清单（按对 PBI-23 的用途分组）

### A. 会议内核的文件骨架

1. **playbook 七段式**：the team（谁负责什么、连到谁）→ workflow as it ran → prompts verbatim → routines and cadences → numbers → what they learned → copy this（setup checklist）。
   出处：`grokbot-field-notes/playbooks/README.md`"Every playbook has the same shape"。
   用法：会议内核每篇按「谁参与 → 会议怎么开 → 检查点与产出 → 节奏 → 可复制清单」组织。
2. **角色卡八节**：Seen on as / **Owns / Does not own** / Source of truth / Needs approval for / Triggers / Outputs / Routines / Role description。
   出处：`roster/README.md` 表格与 `roster/chief-of-staff.md`。README 明说 "The *does not own* list is the part people skip and the part that stops sprawl"。
   用法：每个会议内核开头写「主持/参与/批准/不做」，用 Does-not-own 明确边界（如 Review 不排序 backlog）。
3. **Skill 文件的六问**：何时适用（与不适用）/ 需要什么输入与权限 / 步骤 / 结果怎么查 / 产出格式 / 哪些动作要批准。
   出处：`agents/SKILLS-AND-ROUTINES.md` "What a good skill describes"。
   用法：四篇会议内核的统一小节模板。
4. **指南写法（顺序读一遍，之后各页独立）**：`BotHarness/DeepSeekBot/.agents/docs/guide/README.md` "Read the pages in order the first time. After that, each page stands alone."
   用法：四篇内核各自自足，不要求按顺序读；索引页给一次顺序。

### B. 检查点与证据（Review / 每晚收口）

5. **"Verification is the job" + 证据类型表**：UI→截图/录屏；后端/性能→真实运行前后数字；Bug→复现与同样步骤通过；重构→证明行为不变的测试或手工流程。"A PR with no proof is a draft"。
   出处：`AGENTS.md` "Before you open a PR"。
   用法：Review 内核的「增量证据包」按改动类型列要求；每晚收口的交接件必须带证据指针。
6. **三条验证铁律**：先复现再修；证明随 PR 走；验证是合并闸门（但按爆炸半径保留人工门）。
   出处：`agents/VERIFICATION.md` "The three rules to enforce" 与 "The caveat, stated honestly"。
   用法：Review 内核的「不凭自述，凭证据」写为原则，不写具体工具。
7. **状态汇报的诚实格式**：说清 done / in progress / blocked；没变化就说 "no change"，不制造报告；定时检查无事则静默。
   出处：`AGENTS.md` "When you're the one being asked for a status"；`ANTIPATTERNS.md` #34 与 `SKILLS-AND-ROUTINES.md`（no-op 静默）。
   用法：每晚收口与看板模板的「无事则静默」一行。
8. **过夜合同四件**：goal、finish condition、permissions、escape hatch，外加决策日志；早晨审计看决策行，不重读全程。
   出处：`DeepSeekBot/.agents/docs/guide/07-overnight.md` "The overnight contract" 与 "The morning audit"。
   用法：每晚收口内核的模板节：目标、完成判定、明天的权限、卡住时的逃生口、决策日志。
9. **"A duration is not a finish condition"**：时长不是完成判定。
   出处：同 07 "Pitfall"。
   用法：时间盒与完成标准分开写（我们的检查点制度正好缺这句）。

### C. 规则怎么写、怎么改（Retro / 蒸馏）

10. **写原则，删故事**：规则 born from a bad session 会把当天细节烘死；判断法「不在场的人也能看懂这条规则吗」。
    出处：`AGENTS.md` "When you are corrected"；`SKILLS-AND-ROUTINES.md` "The overfitting trap"（含三组 overfit→general 对照）；`ANTIPATTERNS.md` #1。
    用法：Retro 内核的蒸馏节写入这条，作为记忆档案的写作标准。
11. **反模式格式**：what broke → why → the rule it produces，按错误种类分组而非按天。
    出处：`ANTIPATTERNS.md` 头部说明。
    用法：Retro 的记忆档案条目格式；不新增插件内反模式文件（超出 PBI-23 范围）。
12. **一个原则名就能转向**：24 条原则各有名字，用名字引用（"prove it works"）比一段话更精确。
    出处：`DeepSeekBot/.agents/docs/guide/08-principles.md`。
    用法：内核的检查点给短名（如「先复现」「无证据不算完成」），便于口头引用。

### D. 单一入口与按需召唤（Planning / 全场）

13. **一个 bot 说话，专家按需召**：chief-of-staff 模式；专员之间直接对话，回报给 chief；"Build every other agent *through* it"。
    出处：`grokbot-field-notes/agents/ORCHESTRATION.md` "1. The chief of staff"；`playbooks/README.md` "What every session said" 第 2 条。
    用法：会议默认由 SM 会话主持、PO 决策、需要外部视角才召唤 stakeholder 子代理——与我们现有角色设计一致，作为佐证。
14. **群目标 = 先对齐 done，再分阶段，每阶段凭证据过关**。
    出处：`DS-Bot/README.md` "Group chats"（a group chat can run a goal… checks each stage against evidence before moving on）。
    补全（2026-11-07 一手复核）：群目标是一份分阶段账本——每阶段有自己的验收方法；`pass` 没有证据就被工具拒绝；`rework` 写明缺什么并把任务退回；用户修正目标走 `revise` 并写理由，已通过的阶段保留。出处：`Fei2411/DS-Bot:docs/plans/2026-11-01-group-goal.md`（"状态"、"执行"、"持续对齐"）。
    用法：Planning 内核的三阶段（Why/What/How）各自带产出与检查点。
15. **一个 bot 一个职责，先问「为什么不能是现有 bot 加个技能/例行」**。
    出处：`ORCHESTRATION.md` "One bot, one job" 与 "The bot-sprawl trap"。
    用法：PBI-23 的边界：**不新增角色**；会议内核复用现有四角色。

### E. 看板与共享任务（模板）

16. **任务 = 标题 / 详情 / 依赖(blockedBy) / 写域(writeScopes)**；CAS 版本防覆盖；写域只警告不阻断；删除留墓碑。
    出处：`deepseek-harness/packages/team/agent-team/README.md` "Shared task board"；`docs/subsystems/agent-team.md` `TeamTaskSnapshot`。
    用法：若模板里的看板要服务多个会话，字段照此收敛；v1 的看板只写人每天做决定要用的三问，不引入服务。
17. **委派要有硬标识**：给 ticket ID、URL，不给"reply to Alex"式的模糊指代。
    出处：`ANTIPATTERNS.md` #37。
    用法：看板/日志行带文件路径与提交号。
18. **Agent Teams 的边界**：实验性、默认关；lead + teammates + 共享任务列表 + 互发消息；teammate 有独立上下文，lead 的对话历史不继承；不做 worktree 隔离，需按文件分区。
    出处：Claude Code 文档 `/en/agent-teams`（Warning、Compare with subagents、"Do the tasks touch the same files?"）；`/en/glossary` "Agent teams"。
    用法：插件在**没开 Agent Teams 时也要能跑**；内核按子代理写，Agent Teams 只是可选加速，不写依赖。

### F. 记忆与自足

19. **工作知识放描述与技能，不放记忆**：机器人复制时记忆清空、分享模板时只留核心记忆——"put job knowledge in the description and skills, not in memory accumulated through chat"。
    出处：`grokbot-field-notes/reference/PRODUCT.md` "What transfers, and what doesn't"；"Description is the system prompt"。
    用法：支持 PBI-23 的自足要求——方法论知识进插件文件，不依赖作者记忆目录。
20. **核心记忆 = 一行一条的 MEMORY.md 索引 + 主题文件**。
    出处：`DeepSeekBot/GLOSSARY.md`（PersonaBots / Core Memory）与 `docs/adr/0134`（`SOUL.md` + 一行一条为主的 `MEMORY.md` 索引，会话首次组装提示时冻结）。〔2026-11-07 更正：原写 `CONTEXT.md`，该文件不存在。〕
    用法：我们记忆目录的现状（MEMORY.md 索引 + 每期档案）与之同构，作为佐证，不改。

## 三、明确不借的

| 不借 | 原因 | 出处 |
|---|---|---|
| 69 角色 roster、bot 工厂 | 我们是方法论插件，角色固定四个；roster 只会让触发描述互相叠影 | `roster/README.md` |
| routine/scheduler、群聊实现、记忆服务、云电脑 | 产品运行时，不是插件职责；且违反「不造运行时」定位 | `ORCHESTRATION.md`、`DS-Bot/README.md`、`DeepSeekBot/GLOSSARY.md` |
| 共享任务板做成服务 | DSH 的 Team 依赖会话运行时与持久化；我们最多做文件看板 | `packages/team/agent-team/README.md` 已知限制 |
| 自改进周报、频率审计 | 属于运行时的 token 预算管理，与会议内核无关 | `SKILLS-AND-ROUTINES.md` "Self-improvement routines" |

## 四、对 PBI-23 形态的判断

1. **会议内核 = playbook 七段式的收敛版**：七段里对开会有用的五段（谁参与 / 怎么开 / 检查点与产出 / 节奏 / 可复制清单），加角色卡的四边界（主持、参与、批准、不做）。
2. **模板 = 文件 + 说明**：四个模板（ProductBacklog、SprintBacklog、日记、看板）各带使用说明与初始化路径；看板按第 16、17 条只写三问与硬标识。
3. **证据与诚实汇报是四篇内核的公共节**：第 5～9 条落在 Review 与每晚收口。
4. **Retro 的蒸馏写作标准直接采用第 10、11 条**。
5. **不引入任何运行时依赖**：第 18 条决定内核按「全新子代理 + 文件」写；Agent Teams、DSH、MCP 都只是可选加速。

## 五、2026-11-07 一手复核（三份子代理报告摘要）

> 方法：三个只读子代理（Sonnet）用 `gh api` 直读一手文件，各管一组来源；没给它们看本文前四节，免得顺着结论找证据。标记：〔实践〕只靠文件加对话就能做；〔运行时〕要靠 bot 产品的运行时（定时、持久记忆服务、bot 互发消息、云电脑等）。原报告只存在于 2026-11-07 的会话里，这里是压缩稿。

### 5.1 Grok Bot（`unicodef1wn/grokbot-field-notes`，含 `guide/` 两份 PDF）

**总体**：bot 是有名字、有单一职责的长期同事，每个 bot 有自己的记忆、上下文和 Linux VM；团队是 5～20 个窄职责专员，通常由一个 chief of staff 对接人。人仍做五件事：定产品方向与取舍、亲自发现问题、教 bot 说「不」、批准对外发送与花钱及迁移 / 部署 / 认证类操作、解开认证卡点（`reference/PRODUCT.md`；`notes/day-3-notes.md`；PDF `guide/` §19）。

| 类 | 机制 | 要点 | 出处 | 标记 |
|---|---|---|---|---|
| 角色 | 一个 bot 一个职责 | 角色卡固定小节：Owns / Does not own / Source of truth / Needs approval for / Triggers / Outputs / Routines / Role description / From the stream；"Avoid 'General Helper.' Go narrow" | `roster/README.md`；`agents/ORCHESTRATION.md` "Writing a role" | 实践 |
| 角色 | 防角色泛滥 | 新建前先问现有 bot 能否加技能或 routine；症状：记不清谁干什么、职责重叠、靠人转派、一周没打开 | `agents/ORCHESTRATION.md` "The bot-sprawl trap" | 实践 |
| 编排 | chief of staff | 唯一对人说话的入口，路由、汇总，只有它 ping 人；其他 bot 都经它建；对外只起草 | `agents/ORCHESTRATION.md` "The chief of staff"；`roster/chief-of-staff.md` | 实践（跨 bot 消息是运行时） |
| 编排 | playbook 广播 | 人 → chief → playbook owner 写成通用规则并通知所有 bot；只有 owner 改，其余只读 | `roster/playbook-owner.md`；`playbooks/engineering.md` §8 | 实践（共享文件即可） |
| 编排 | 工程经理不写码 | 把规格拆成单一关注点的任务、写提示、按规格核验，"If proof is missing, send it back" | `roster/engineering-manager.md` | 实践 |
| 编排 | 自主度阶梯 | Investigate → Draft → Autopilot → Full autopilot；新 bot 先只读、再出草稿、再动手 | `agents/ORCHESTRATION.md`；PDF §13 | 实践 |
| 看板 | 任务账本放在任何 bot 的上下文之外 | Notion「fleet DB」管约 20 个云端代理 | `playbooks/engineering.md` | 实践 |
| 看板 | 看板维护者 | 只管看板真实；"Don't prioritise, don't do the work, don't delete cards without asking" | `roster/kanban-updater.md` | 实践 |
| 看板 | 承诺追踪 | 两张表：许下的承诺（带日期）、欠着的请求（谁、何时）；催之前先看线程 | `roster/commitment-tracker.md` | 实践（定时是运行时） |
| 节奏 | routine 规格 | owner、时间或事件触发（优先事件）、输入、输出、审批边界、失败处理、无事时安静 | `agents/SKILLS-AND-ROUTINES.md` | 运行时 |
| 节奏 | 频率就是预算 | 默认一天一两次；15 分钟一次等于一天约 100 次；每周五审计 | 同上；`reference/ECONOMICS.md`；PDF §20 | 运行时 |
| 审批 | 停下来问 | 认证、支付、权限或用户数据；迁移或破坏性命令；生产部署；猜产品决定；同一办法失败两次——"Two failed attempts on the same approach means the approach is wrong" | `AGENTS.md` "When to stop and ask" | 实践 |
| 审批 | 先起草 | chief、承诺追踪只起草；critic 只给反馈；规格未经批准不得定稿 | `roster/critic.md`、`roster/spec-writer.md` | 实践 |
| 验证 | 验证就是工作本身 | 先复现、复述任务、说清怎样算完成、附证据；证据按改动类型（UI 截图、后端前后数字、bug 复现后通过、重构证明行为不变）；"A PR with no proof is a draft" | `AGENTS.md` "The one rule"、"Before you open a PR" | 实践 |
| 验证 | 按爆炸半径定自主度 | 一次性项目可绿灯自动合并，正式产品每个 PR 都由人读；"Set the autonomy level from the cost of being wrong" | `agents/VERIFICATION.md` "The caveat, stated honestly" | 实践 |
| 验证 | 独立检查者 | playtester、validator、fuzz 群；fuzz 只在一次性环境跑 | `agents/VERIFICATION.md` | 实践（群测是运行时） |
| 验证 | 先复述、先蒸馏 | 开工前「用你自己的话复述」；长输入先压成要点再推理 | `agents/PROMPTS.md` 第 1、3 式 | 实践 |
| 记忆 | 转移矩阵 | 复制 bot：指令带走、记忆清空；分享模板：只带核心记忆；教技能：全组织可用——"put job knowledge in the description and skills, not in memory accumulated through chat" | `reference/PRODUCT.md` "What transfers, and what doesn't" | 实践（机制本身是运行时） |
| 记忆 | 技能的形成顺序 | 先手动做顺 → 存成技能 → 再上 routine；演示只录到顺利路径，判断、出错处理、审批要手补 | `agents/SKILLS-AND-ROUTINES.md` | 实践 |
| 学习 | 写原则，删故事 | 被纠正后：修好 → 问它意味着什么通用规则 → 写规则、删掉当天细节；判断标准 "would this rule still make sense to someone who wasn't there?" | `agents/SKILLS-AND-ROUTINES.md` "The overfitting trap"；`AGENTS.md` | 实践 |
| 上手 | 第一周顺序 | 连工具 → 录一段语音自述 → 挑最烦的活 → 建一个只读专员 → 演示教会 → 第二个 bot 之前先建验证闭环 → 再加 chief → 纠正写成原则 → 周五审计 routine | PDF `guide/` §20 | 实践 |

**40 条翻车记录**（`ANTIPATTERNS.md`，七类各取要旨）：

- **A 规则与指令（#1–7）**：规则记住了事故 → 留原则删故事；没写下的规范不算规范；「急」让代理跳步 → 一次定好 P0 规则；bot 什么都答应 → 教它说不并讲理由；每个 bot 抄一遍标准 → 设 playbook owner；bot 太多 → 先问现有的为什么不行；自我改进过头 → 每周只提一条。
- **B 验证（#8–19）**：不变量要进测试或可见读数；写清区分性的结果而不是视觉；点名用哪个库；状态以服务端为准；问「做一千次会怎样」；演示路径就是测过的路径、冻结部署；改布局后查遮挡；派生数只在一处算；每个消耗都有下限或出口；平衡靠读数不靠感觉；先复现、再诊断、再修；删掉的测试要说明何时回来。
- **C 内容与口吻（#20–24）**：点名唯一事实源、检查每条用户可见文字；去 AI 腔；语料加权并加评审；品牌用真实素材与禁用清单；它能干活，别只给链接。
- **D 访问与密钥（#25–28）**：用别的账号验证「对外可见」；优先连接器、保留人工接管；把认证当流程步骤；默认每个设置页都有密钥。
- **E 生产与演示（#29–33）**：迁移和部署保留人工闸门；反馈表单带审核、标注提示注入；当天用演示账号端到端跑一遍再宣布；验证闭环里放设备模拟；并行代理用并行环境、推送前 rebase。
- **F 成本与注意力（#34–38）**：审计频率、优先 webhook；群聊只用于辩论；用看守 routine 发现睡着的代理；委派用硬标识；定期问自己在哪里成了瓶颈。
- **G 策略（#39–40）**：自动化前先手做并请教领域专家；围绕你已经懂的东西建。

**文档之间的矛盾**：共享记忆——`PRODUCT.md` 说 bot 之间不共享，`playbooks/product-management.md` 说有共享记忆池，PDF §03 说共享文件系统但不共享上下文，且文件系统不是安全边界；PR 还是直推 main——`AGENTS.md` 要带证据的 PR，day-1 笔记记了原型期「不开 PR、直推 main」；chief 何时加入——`ORCHESTRATION.md` 把它当核心，PDF §20 排在第 7 步。仓库自述：角色卡是「待改的重建稿，不是原样测过的模板」，吞吐数字来自 72 小时的一次性游戏项目（`roster/README.md` Caveats；`agents/README.md`）。

### 5.2 DeepSeekBot 与 pstack（`BotHarness/DeepSeekBot`）

**两层**：产品层是 PersonaBot——Host 拥有的长期身份，带 Git 管理的记忆仓库，跨会话、聊天和工作区（`GLOSSARY.md` PersonaBots）；内置 Steward Bot「Tob」负责建 bot、转派，但没有审批权。开发流程层是 `AGENTS.md` 加上放进来的技能，其中 pstack（`.agents/skills/poteto-mode` 与 `.agents/docs/guide/`）是主干。`CONTEXT.md` 不存在，产品术语以 `GLOSSARY.md` 为准。

| 阶段 | 产出 | 退出检查 | 谁定 | 出处 |
|---|---|---|---|---|
| 写好提示 | 匹配一本 playbook，步骤抄进待办；跳过的步骤留 `skip: <理由>` | 完成判定必须能判对错 | 人给目标、完成判定、要的证据、已知事实、约束 | `guide/02-poteto-mode.md` |
| 理解 | `/how` `/why` `/teach` `/recall`；只读调查 | 证据与猜测分开；"don't change any code yet" | 代理 | `guide/03-understand.md` |
| 设计 | `/architect` 草图；`/arena` 候选；原型；先写 README | 跨模型评判；`/interrogate` 只评 diff，不评抽象计划 | 默认直接推进，"with checkpoint" 时等人签字 | `guide/04-design.md` |
| 计划 | 一个 PR 一节，每节以证据收尾 | "A passing test suite alone doesn't count as that proof" | 人要求才写（pstack 故意没有计划技能） | `guide/04-design.md` |
| 构建 | 小而有序的提交；修 bug 先提交失败的复现 | 在对应界面上验证；"Inconclusive or wrong-surface is not a pass" | 主代理管设计与审阅，写码交子代理 | `guide/05-build-and-clean.md` |
| 清理 | `/deslop` `/unslop` `/no-comments` | 由没写代码的新审阅者做 | — | 同上 |
| 验证 | 命令、输出、录像或截图；`/blast-radius` | 回复带确切命令与输出，否则写 inconclusive | 代理跑，人可查 | `guide/06-verify-and-ship.md` |
| 交付 | 开 PR、看护到可合、按栈落地 | 看护者从不合并，合并是单独的决定 | 每个 PR 一个新验证者，"never the one that wrote it" | 同上 |

**关键机制**（均为〔实践〕，另注者除外）：

- **阶段边界树**：Continue / `/clear` / `/handoff` / 子代理 / `/compact`，"The first yes wins"；`/compact` 是默认但不是首选——除了 Continue，每一步都把一手材料变成有损的二手材料（`ask-matt/PHASE-BOUNDARIES.md`）。
- **交接与接手**：`/handoff` 写一个临时文件，已在别处的内容只给路径、不重复；接手时 "The prior trail is authoritative. Resist the bias to re-derive it"；暂停前完成原子步骤、提交 `wip:`、写恢复说明（`playbooks/pause-safely.md`、`playbooks/session-pickup.md`）。
- **决策日志**：`/show-me-your-work` 是只追加的 TSV，列为 ts、phase、decision、why、evidence、result；证据是指针不是描述；错行用新行取代、不改旧行；另派不同模型族的子代理写「Attention」一节，放在回复最前（`show-me-your-work/SKILL.md`）。
- **过夜合同**：目标、完成判定、权限、卡住时的出口，外加决策日志；早上只看决策行，不重读全程；"A duration is not a finish condition"；先挣到信任再上循环（`guide/07-overnight.md`）。〔定时与自动化依赖 Cursor，Claude Code 适配文件里没有对应。〕
- **自主跑**：每次最小改动 → 对照判定验证 → 有进展就提交、没有就丢弃；"A plateau is not a stop"；永不放宽判定（`playbooks/autonomous-run.md`）。
- **找事实不问人**：能跑出来的事实不归人回答，问题只留给产品或偏好上的决定（`poteto-mode/SKILL.md` Non-negotiables）。
- **设计两遍**：至少两个结构不同的候选，按红旗清单筛，由不同模型族评判（`architect/SKILL.md`、`arena/SKILL.md`）。
- **验证技能**：「问仓库，不问人」，生成 `verify-<app>`（启动、体检、驱动、证据、清理）与功能地图，必须端到端跑通一次——"A generated skill that was never executed is a draft, not a deliverable"（`create-verification-skill/SKILL.md`）。
- **爆炸半径**：找出「改动之所以安全」的那一个事实并跑代码证明；置信度从 1（"You said so. Worthless on its own"）到 5（在运行中的应用里复现）（`blast-radius/SKILL.md`）。
- **纠错成结构**：`/correct` 按架构 → 类型或 lint → 测试 → 文档的顺序修一类错误；"A class counts once it has happened twice"；每条检查都要用一次真实的旧错误证明（`correct/SKILL.md`）。`/retro` 把机械错误变成检查、把判断变成规范。
- **原则命名**：24 条 `principle-*` 技能当转向词；必须说出每条原则改变了哪个决定——"A principle citation with no decision behind it means the agent named the rule without applying it"（`guide/08-principles.md`）。
- **自主度**：可逆的直接做；不可逆的（强推共享分支、部署、删数据、给客户发消息）一律停下；"No is an acceptable answer"（`poteto-mode/SKILL.md` Autonomy）。
- **产品层**〔运行时〕：Bot Inbox（未读 → 打开 → 显式 `done` 或 `ignored` 才算处理，"Finishing a turn resolves nothing"）；定时只把事件放进收件箱，由编排会话决定做不做；审批模板加一个没有工具的审阅会话，审阅失败一律回落到人工卡片（`GLOSSARY.md`；`docs/adr/0133`）。

**在 Claude Code 上**（`.agents/docs/harness/claude-code.md`）：`Task` 对应 `Agent`；只读子代理对应 `Explore`，并在说明里写「不要改文件」、事后查 `git status`；云端环境对应 `isolation: "worktree"`；遇到 Cursor 独有的功能（Automations、云代理等）就写一行 "Skipped in Claude Code: <step>. <reason>." 然后继续；`/loop` 与定时的过夜自动化没有映射。

**指南列出的坑**（`guide/10-recipes-and-pitfalls.md` 等）：在提示里罗列技能；完成判定含糊；先抛出自己对原因的猜测；采用第一个设计；打磨抽象计划；多个代理共用一个 worktree；没建立信任就上循环；相信未核实的数字；同一错误反复手改；绿灯构建就报成功；徒手写 SKILL.md；任务中途改技能；跳过理解；把清理当可选。

### 5.3 DS-Bot、DeepSeek Harness 的 Agent Teams、openmausbot

**DS-Bot**（`Fei2411/DS-Bot`；`docs/plans/*` 原文为中文）：bot 是长期身份，工作分布在多个 DSH 会话里（私聊、每个群各一个、上下文满了开新段）。Main Bot（默认叫 Chief）权限最高，可建、改、停其他 bot；每个群有管理员，默认由它回应人、用 `@` 点名成员；人是最终权威，设沙箱权限、批准风险操作，能看见并停止一切（`AGENTS.md`；`docs/vision.md`）。

- **群目标**〔运行时〕：每群一个，含标题、目标、总体验收方法、约束（含人的中途修正）、有序阶段；每个阶段有自己的验收方法，任务点名分给成员；任务状态 pending → working → reported → done，阶段状态 pending → active → passed；只有管理员或 Main Bot 能写；阶段内任务都交回后，管理员按阶段验收方法检查，`pass` 没有证据就被拒，`rework` 写明缺什么并退回；阶段严格按序推进；人可暂停、恢复、停止，修正走 `revise` 并写理由，已通过的阶段保留；一轮结束无人工作时唤醒管理员一次，连续两次无进展就标为「等你」（`docs/plans/2026-11-01-group-goal.md`）。已知限制：DS-Bot 自己不跑验收命令；没有时间或轮数上限。
- **goal-grill**〔实践〕："Facts are your job; decisions are the user's."——先自己查事实（文件、代码、聊天记录、问成员）；列出待决事项（范围、怎样算完成、怎么检查、限制、谁做什么）；**一条消息编号问完，每条附推荐答案与备选**，人可以回「全按推荐」或「2: B」；答案引出新的选择时才问第二轮；评审交给没做这件事的成员（`ds-bot/src/host/skills/goal-grill/SKILL.md`）。
- **交接树**〔运行时〕：A 托 B、B 再托 C 时，B 给 A 的回复要等 C 回来；`list_bots` 显示每个 bot 在等审批、在干活、在等别的 bot 还是空闲；明确不做看板式的任务对象（`docs/plans/2026-10-16-bot-handoffs.md`）。
- **记忆**〔运行时〕：三层（每个 bot、每个群、团队），Markdown，一行一条并带 `[source: …; added: …]`；会话空闲后做一次记忆审查；`journal.jsonl` 记下每次改动，人可单条撤销；记忆是数据，不是指令（`docs/plans/2026-10-09-context-and-memory.md`；`ds-bot/README.md` "Memory"）。
- **审批卡**〔运行时〕：成员的审批请求显示在群的状态胶囊里，人选「允许一次」或「拒绝」，该成员立刻让出发言；新增本地 MCP、工作目录越界、私有 bot 对外分享、发邮件都要批（`docs/plans/2026-10-07-group-chat.md`；`README.md`）。
- **故意不让 bot 开子代理**：理由是子代理人看不见、停不了，切换会话就丢（`docs/plans/2026-10-10-bot-runtime.md` "Agent 预设"）。

**DeepSeek Harness 的 Agent Teams**（`deepseek-ai/deepseek-harness`，`packages/team`）〔运行时〕：根会话即 Lead，子代理即队员；Team 只多一块持久的共享任务板。任务字段：`id`、`revision`（每次改动加一，用作比较后写入）、`subject`、`description`、`status`（pending / in_progress / completed / deleted，删除留墓碑）、`ownerId` / `ownerName`、`blockedBy[]`、`writeScopes[]`；被阻塞的任务全部完成后才能认领；写域重叠只警告、不加锁；任务变化不会唤醒任何人，要别人行动得发消息；不会自动释放负责人（`packages/team/agent-team/README.md` "Known Limitations"；`docs/subsystems/agent-team.md`）。

**openmausbot-teams**（`milind-soni/openmausbot-teams`）〔实践〕：一支团队就是一个 Markdown 文件，交给 Chief of Staff，或直接导入 OpenMausBot；正文必须有 Activation、Mission、Outcomes、Connections、Team、Chief of Staff、Completion rule，且粘进对话就能独立成立（`FORMAT.md`）；角色描述以「Own X」开头，写明边界与证据规则；playbook 分 Use this when / Process / Output / Guardrails，例如 "Never infer passing checks that were not run"；建议的 routine 一律默认暂停，由人开启；连接只写成需求，从不带凭据（`README.md`；`CONTRIBUTING.md`）。

| 机制 | DS-Bot | DSH Agent Teams | openmausbot |
|---|---|---|---|
| 协调者 | Main Bot + 每群管理员，权限写在代码里 | Lead = 根会话，只有它能改派 | Chief of Staff，写在文件里；平台不能开子代理时按顺序扮演各角色 |
| 任务追踪 | 群目标账本；普通交接没有任务对象 | 带 revision、依赖、写域的任务板 | 没有；计划类 playbook 用文字列出负责人 |
| 分阶段 | 有序阶段，每段凭证据放行 | 没有，只靠 `blockedBy` 排序 | playbook 内的步骤，加按惯例的就绪判定 |
| 审批 | 审批卡 | 没有 | 文字规则：发送、花钱、删除、开定时前先问 |
| 证据规则 | 没证据 `pass` 被拒 | 没有 | "Never infer passing checks that were not run" |

### 5.4 对本项目的用处（已用进产品日志架构 v1）

| 机制 | 来源 | 用在架构 v1 的哪里 |
|---|---|---|
| 事实归 AI、决定归人；待决事项一次问完、附推荐 | DS-Bot goal-grill | Master 的提问方式（实际没写进架构）；PBI-30 的「≤2 轮进入执行」也可借 |
| 阶段凭证据放行，退回时写明缺什么 | DS-Bot 群目标 | 2.3 对抗审查与 PO 验收 |
| 完成判定先写、能判对错；时长不是完成判定 | pstack | 2.3 精化七步第 5 步：验收标准先写 |
| 核验的人不是做的人 | 三家都有 | 2.3 对抗审查：必须有审阅方 |
| 决策日志：只追加、证据是指针 | pstack | 2.3 冲刺日志 3.2 笔记 |
| 接手以记录为准，不重新推导 | pstack | 2.3 笔记：新会话读日志接上 |
| 跳过的步骤留 `skip: <理由>` | pstack | 2.5 约定 v1 的身份声明：可以不照做，但写明原因 |
| 同一类错误出现两次才改规则 | pstack `/correct` | 第一轮用于 2.5 迭代；第二轮改为每周集中改，不再用 |
| 工作知识放描述与技能，不放记忆 | Grok Bot | 2.5 约定进插件；全局记忆是过渡态 |
| 防角色泛滥：先问现有角色能否多带一份参考 | Grok Bot | 2.5 不新建技能，放进两个内核的 `conventions/` |

**一处分歧**：DS-Bot 故意不让 bot 开子代理（人看不见、停不了），而 Grok Bot 与 pstack 把全新子代理当默认的验证手段，本项目也用子代理做审阅（PBI-20）。架构 v1 定审阅默认由 Master 做，PO 可指定 Stakeholder 或子代理（2026-11-07 第二轮），部分缓和了这一点。
