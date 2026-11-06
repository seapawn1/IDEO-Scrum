# Sprint 08 · 交接（2026-11-06 凌晨落盘）

> 这份文件是给「重开对话后接手的人」看的。原会话反复报 `error_during_execution` 并卡在重试（两个会话都一样），PO 决定重启后重开。以下内容来自那两次会话已经推进到的状态，没有丢。

## 一、已经定下来的

| 项 | 结论 | 谁定的 |
|---|---|---|
| Sprint 08 选材 | **只做 PBI-23「流程化参考与文件模板」** | PO，11-05 晚 |
| 顺带项 | PBI-25 的小修碰到先问 PO，可能多数不做 | PO |
| 不做 | PBI-12（方法论分享）、PBI-26（两轮进入执行）、codex 侧 | PO |
| Sprint Goal | **「会议内核可复用」**：新对话准确接住方法论；Planning、Review、Retro 各有可复用的会议内核与模板；开新会话不用人重复解释，照着就能走 | 阶段 1 收口，PO 认可 |

## 二、精化草案（未定稿，等 PO 点头）

| 项 | 草案 |
|---|---|
| 故事 | 作为开新项目或新会话的我，我想插件自带会议内核与模板，开新会话不用人重复解释，照着就能把会开好 |
| 需要 | ① **会议内核**：Planning（三阶段）、Review、Retro、每晚收口——各写清为什么开、成功的样子、步骤与检查点、角色、产出；Review / Retro 以「合并提交 + 蒸馏 + tag 写成果 + 项目约定优先」那套为底；每条指出处，我们的增补单独标明<br>② **模板**：ProductBacklog、SprintBacklog、日记、看板——「说明 + 模板」三件套照 pomodoro 样例；看板只放每天做决定要用的东西（三问：现在在做什么？今天要做什么？下一个检查点是哪天？）<br>③ **承载分层**：常驻只加触发描述，内核正文短，细节与模板按需读，新项目有初始化路径<br>④ **自足**：内容不依赖插件之外的记忆或配置 |
| 验收 | ① 空目录照模板跑通一轮 Planning 到每晚收口<br>② 冷启动测试：新对话不用人重复解释，按内核开会；同日对照、两条路径（角色命令进入 / 直接说）<br>③ 常驻增量可量化：描述占比与内核正文不膨胀，以 Sprint 07 的 0.9% 为基线<br>④ 对抗审查 verified；Sprint 08 Review 通过 |
| 边界 | ① 生效且不呆板：内核写判断点与检查点，不写死步骤<br>② 现有角色命令与内核行为不动，要动先问 PO<br>③ PBI-25 顺带项先问 PO；PBI-12、PBI-26、codex 不做<br>④ 第一批范围待定，其余件同法迭代，做不完回产品日志 |

## 三、PO 当时要的下一步

他最后说的是：「OK，我们继续。嗯，发表一下你的观点。」——**精化草案还差一次讨论**：接手的人要先给出自己对这份草案的判断（哪里同意、哪里不同意、缺什么），再和 PO 一起定稿。

定稿之后才建 Developer 会话做对抗审查。精化阶段不动代码。

## 四、这条线上还有一条待办

**PBI-36（SeaPawn 的编号）：用 Grok Bot 的思想指导 IDEO-Scrum 的改革。**

- 不是「结合」，是「指导」——用它的思想指导改革，不是把两个东西拼起来。
- 起因：PO 和人聊天时弄清 Grok Bot 是什么，觉得它的做派和 IDEO-Scrum 想做的很像，收进了一个 PDF。
- PDF 的位置和内容还没给到。做 PBI-23 时把这条考虑进来，但别自己往下推。

## 五、可直接借鉴的做法（SeaPawn 刚做完的）

- 三件套：`S:\SeaPawn\Scrum\pomodoro\` 下的 `kernel.md`（逐字抄权威源 + 本轮采用/暂缓对照）、`README.md`（怎么用）、`_template.md`（当天模板）。
- 流程约定：`S:\SeaPawn\Scrum\sprint\SprintBacklog.md` 第三部分——How 归 Developer，SM 只定检查点与时间盒；对抗审查不看自述只看文件，结论只有 verified / in doubt，in doubt 一并退回；交付必须带真跑记录。

## 六、环境备注

- 原会话 `Scrum # [master]-[main]-[准备sprint会议]`：583 条消息后开始反复 `error_during_execution`，重试 10 次仍失败。
- 接手会话 `IDEO-Scrum Sprint 08（接手）`：124 条后同样报错。
- 两个会话的模型都是 `claude-sonnet-5[1m]`、effort max；同时另一个 6.7MB 的会话（SeaPawn）一直正常，所以**不是体量问题**，原因未查明。
- PO 计划重启机器后重开对话。

## 七、2026-11-06 讨论结论（本次会话）

> 本节是 2026-11-06 凌晨到清晨的讨论结果；前六节是重启前的状态，仍然有效。

### 三条线

1. **PBI-23**：流程化参考与文件模板（Sprint 08 交付线）。
2. **PBI-12**：方法论分享（最后一条）。
3. **PBI-27**：Bot 工作方式研究——PBI-23 的预研究，已登记进产品日志。

### PBI-27 参考（已写进产品日志）

- `unicodef1wn/grokbot-field-notes`（主参照，MIT）：69 个角色、9 个 playbook、40 条翻车记录、AGENTS.md、验证/编排文档。
- `Fei2411/DS-Bot`（5.7k 星）：Chief 主 bot + 群聊 + bot 记忆。
- `BotHarness/DeepSeekBot`（Tobs，643 星）：GrokBot 开源平替，多 bot 团队。
- `milind-soni/openmausbot-teams`：社区团队模板与 skill playbook。
- `deepseek-ai/deepseek-harness` 的 `packages/team`：内置 Agent Teams（共享任务板 + 子代理树，MIT）。

### 关键判断

- **Grok Bot / DS Bot** 是「持久 bot 产品」：身份、每个 bot 的记忆、云电脑、Routine、审批卡。
- **DSH Agent Teams / Claude Code Agent Teams** 是「会话级协调」：lead + teammates + 共享任务列表 + 互相发消息。Claude Code 的 Agent Teams 是实验性、默认关闭（`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`）。
- **我们的定位**：Claude Code 上的方法论插件——不造运行时，不依赖 DSH；运行时能力只作为可选加速，插件要能在没开 Agent Teams 时也跑。
- **记忆**：角色笔记暂不做。项目记忆 + Sprint/产品日志 + Retro 蒸馏已经覆盖连续性；等出现「角色私有、不该进项目记忆」的具体需求再加。
- **流程**：不做完整设计冲刺。先学习（PBI-27）→ 精化定范围/验收/架构约束 → Sprint 08 做 v1 → Review 收集意见 → v2。How 在 Sprint 内，由 Developer 定；精化只定 What/Why/验收。

### 下一步

- **明天**：开 Sprint 08；精化时借鉴上面的 Bot 方案，定出增量范围与验收。
- 方案定后：开一个 Developer 会话，PO + SM + Developer 一起做。
- 工作区：`scrum/ProductBacklog.md` 已更新 PBI-27（未提交）；本交接件未入库，Sprint Planning 后折进 SprintBacklog 再删除。

## 八、2026-11-06 会议收口（Planning 暂停）

> PO 2026-11-06：内核太复杂，今天先停；下次再定具体内核。Planning 会议本质上失败。

### 已定

- Sprint Goal：会议内核可复用。
- 选材：PBI-23、PBI-27、PBI-25③④、PBI-28（DesignBacklog，选入）。
- PBI-29（ideo-kernel 两模式重构）：登记，不选入。
- 角色卡重构：PBI-27 子项（Owns / Does not own / Needs approval）。
- 模板四份：ProductBacklog、SprintBacklog（How 区含日记节）、DesignBacklog、看板。
- 看板：PO 的单一视图，一个看板了解所有；设计重要。
- 精化条件：问题复杂先做设计冲刺（DesignBacklog）；能定出产品 / 产品目标则跳过。
- 过程规则：SM 不擅自开新会话 / 派活；精化结束由 PO 说；边界写角色命令，不写记忆。

### 未定（下次继续）

- 内核架构：Planning、Review、Retro、每晚收口、精化五篇的步骤、检查点、角色、产出。
- 模板细节：四份模板的章节与填写方式。
- 验收测法：冷启动、空目录、常驻增量、对抗审查的具体判定。
- PBI-25③ 的新 Trigger 文字。
- Grok Bot 等 Bot 方案的借鉴（PBI-27）如何落进内核与模板；PBI-29 的 ideo-kernel 两模式重构。
- 整个优化之路很难，不是一次会议能定完；下次一条一条来。

### 教训

- SM 过早开 Developer 会话、过早派活；计划批准 ≠ 开工授权。
- 精化被拖成 meta 讨论；内核复杂度超出一次会议。
- 下次：PO 主讲内核，SM 只记录与追问；不派活、不开新会话。

### 精化方法（下次用）

1. 取一条 PBI（PBI 就是 POV，不再另做 POV）。
2. 确认 POV：从 Goal/PBI 抄来，不改。
3. 把 PBI 打开成 HMW / 不明白的点。
4. 每个点归位：PO 决定 / Developer 方案 / 研究任务。
5. 切片：能几天做完的小 PBI + AC。
6. Readiness：两个「不用再问」——Developer 能开工，PO 能验收。
7. 精化结束由 PO 说。

### 归档

- 两个会话（Master、Developer）已归档；状态以本交接件、`scrum/ProductBacklog.md` 与 `scrum/sprint-08/SprintBacklog.md` 为准。
- plan 文件是工作副本，归档后不依赖它。
