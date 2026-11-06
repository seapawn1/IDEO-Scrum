# PBI-27 · Bot 工作方式研究（PBI-23 预研究）

> 日期：2026-11-06。方法：`gh api` 直读仓库文件（未用 WebSearch，3P 网关下不可靠）。
> 定位：只借思想，不抄代码。MIT / Apache-2.0 来源可借鉴并署名；无 AGPL 来源；泄漏提示词未使用。
> 每条结论带出处（仓库/文件/小节）。

## 一、五个来源的定位

| 来源 | 许可 | 是什么 | 对 PBI-23 的价值 |
|---|---|---|---|
| `unicodef1wn/grokbot-field-notes` | MIT | xAI Grok Bot 三场直播的整理：规则、验证、编排、69 张角色卡、9 本 playbook、40 条翻车记录 | **主参照**。playbook 骨架、角色卡八节、验证规则、反模式格式 |
| `Fei2411/DS-Bot` | Apache-2.0 | DSH 上的 bot 桌面应用：Chief 主 bot + 群聊 + bot 记忆 + 群目标 | 单一入口、按需召唤、阶段验收 |
| `BotHarness/DeepSeekBot`（Tobs） | MIT | BotHarness 的 PersonaBot 应用 + 内置 pstack 流程指南 | 过夜合同、决策日志、原则名、指南写法 |
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
    出处：`DeepSeekBot/CONTEXT.md` "Core Memory" / "Topic file"。
    用法：我们记忆目录的现状（MEMORY.md 索引 + 每期档案）与之同构，作为佐证，不改。

## 三、明确不借的

| 不借 | 原因 | 出处 |
|---|---|---|
| 69 角色 roster、bot 工厂 | 我们是方法论插件，角色固定四个；roster 只会让触发描述互相叠影 | `roster/README.md` |
| routine/scheduler、群聊实现、记忆服务、云电脑 | 产品运行时，不是插件职责；且违反「不造运行时」定位 | `ORCHESTRATION.md`、`DS-Bot/README.md`、`CONTEXT.md` |
| 共享任务板做成服务 | DSH 的 Team 依赖会话运行时与持久化；我们最多做文件看板 | `packages/team/agent-team/README.md` 已知限制 |
| 自改进周报、频率审计 | 属于运行时的 token 预算管理，与会议内核无关 | `SKILLS-AND-ROUTINES.md` "Self-improvement routines" |

## 四、对 PBI-23 形态的判断

1. **会议内核 = playbook 七段式的收敛版**：七段里对开会有用的五段（谁参与 / 怎么开 / 检查点与产出 / 节奏 / 可复制清单），加角色卡的四边界（主持、参与、批准、不做）。
2. **模板 = 文件 + 说明**：四个模板（ProductBacklog、SprintBacklog、日记、看板）各带使用说明与初始化路径；看板按第 16、17 条只写三问与硬标识。
3. **证据与诚实汇报是四篇内核的公共节**：第 5～9 条落在 Review 与每晚收口。
4. **Retro 的蒸馏写作标准直接采用第 10、11 条**。
5. **不引入任何运行时依赖**：第 18 条决定内核按「全新子代理 + 文件」写；Agent Teams、DSH、MCP 都只是可选加速。
