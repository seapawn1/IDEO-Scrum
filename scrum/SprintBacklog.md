# Sprint Backlog — Sprint 07（IDEO-Scrum 4.0 · 角色与内核）

> 开工 2026-10-24 | 截止 2026-11-21（PO 不另定长度，按规约上限 4 周）| 分支：main | PO：SeaPawn | Scrum Master：Master 会话 | Developer：Claude（AI）
> 依据：2026-10-24 #28 讨论定案与 Sprint Planning——Product Goal 重定为「IDEO-Scrum 4.0」；冲刺拆分经 PO 同意，本冲刺做 PBI-21、PBI-20、PBI-22。PBI 状态只写在产品日志，本文件只引用编号。

## 一、Sprint Goal 与 DoD

### Sprint Goal

角色与内核就位：design-kernel 改名为 ideo-kernel 并分清两套「五步」，四个角色按 10-24 的新定义改写，调用角色命令就自动加载对应内核——给 Sprint 08 的流程参考与模板一套稳定的名字和角色。

### Definition of Done（摘抄自产品日志）

**Definition of Outcome Done**

| 度量 | 目标信号 |
| --- | --- |
| 一次会话走通方法论环节：完整引导（结构化、忠于原文），≤2 轮对话进入执行 | 用户不反复追问 |

**Definition of Output Done**

| 维度 | 标准 |
| --- | --- |
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 可导航 | 从 SKILL.md 入口 ≤2 跳到达任意 reference |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |

DoD 适用于下列每条 PBI；AC 只写 PBI 特有的标准。
通用验证：改动插件结构后过 plugin-validator；skill 改动过 skill-reviewer。

## 二、PBI 与验收标准（AC）

### PBI-21 ideo-kernel：改名并分清两套「五步」

- **21-1 改名**：技能目录 `skills/design-kernel/` 改为 `skills/ideo-kernel/`，frontmatter 的 name 同改；调用名变为 `ideo-scrum:ideo-kernel`。
- **21-2 迁移零残留**：插件内、README、ATTRIBUTION、CLAUDE.md 里的 design-kernel 全部改为 ideo-kernel；同一提交内 `git grep design-kernel` 只剩历史记录（产品日志修订记录、CLAUDE.md 历史锚点）。
- **21-3 两套五步分清**：ideo-kernel 的 SKILL.md 写明两套方案——IDEO 五模式（共情、定义、构思、原型、测试）和设计冲刺五阶段（挑战、目标与问题、问专家、地图、目标点），各自什么时候用；用户说「五模式」或「五阶段」时各走哪一套。
- **21-4 回归验证**：新起一个全新子代理，用 PO 10-24 的说法请它「用 IDEO 五模式」做一件事，产出按共情→定义→构思→原型→测试展开，不出现挑战、目标、地图的结构；结果记进进展记录。
- **21-5 L47 的取舍**：作者待办 L47（设计冲刺各阶段绑定 IDEO 模式）和「分清」方向相反，由 PO 在动手前定：采纳就落文，不采纳就在产品日志写明不做。
- **不在范围**：codex 分支不同步（PO 10-24：Codex 先放着）。

### PBI-20 角色重定义

- **20-1 只有 PO 必须是人**：写进插件——SM、Stakeholder、Designer、Developer 都可由 AI 担任；注明这是作者方法论设计，和 SGEP v2026.1 原文（PO、SM must be human）不同，不写成 SGEP 作者的主张。
- **20-2 Stakeholder 改写**：一个命令、多种身份（项目里写定）；可作子代理召唤，也可常驻会话；可做非源码杂务（如看板维护），源码只归 Developer；外部视角那部分保留。只改和新定义冲突的句子，其余逐字保留；改动逐句列给 PO 批。
- **20-3 Master 的职责**：scrum-master 命令写明——替 PO 派活、跟进度（转达 PO 选定的「做什么」，「怎么做」归 Developer），跟进度可交 stakeholder；审阅由 Master 派全新子代理做对抗审查。
- **20-4 Developer 完工交证据**：developer 命令写明完工时交 DoD 逐条结果和改动摘要，供审阅子代理核对（沿用 PBI-19 在 09-23 定案的 DoD 自检层）。
- **20-5 三个命令的措辞微调**（scrum-master / developer / designer）：Developer 先列微调清单，PO 逐条点头后才改。
- **不改的**：角色 description 里的否定句；「角色数量梯子」不写；命令名 scrum-master 不改（PO 10-24 定）。

### PBI-22 加载机制——角色命令自动加载内核

- **22-1 自动加载**：调用 `/ideo-scrum:developer` 后，同一轮里 scrum-kernel 被加载，用户不用另说；designer 加载 ideo-kernel；scrum-master 两个都加载；stakeholder 不加载。
- **22-2 先核对写法**：动手前用 plugin-dev 和 claude-code-docs 核对「命令正文要求先调用技能」是否可靠、能否连续加载两个技能；结论记进 How 区。做不到就报 SM，与 PO 重谈范围。
- **22-3 流程靠描述常驻**：两个内核的 description 写清「IDEO 研究、Scrum 落地」的关系（PBI-16 已有，随 PBI-21 改名同步），长度不超过上限。
- **22-4 验证**：四个命令各在全新会话或全新子代理里调用一次，记录有没有自动加载；结果记进进展记录。

## 三、执行计划（How）

> **本区归 Developer 所有。** 细化 PBI、拆解任务、排执行顺序、记录进展，均由 Developer 在此进行，Sprint 期间自行更新；PO 与其他角色不在此区预设内容。

### 推进顺序与依赖

PBI-21 → PBI-20 → PBI-22 → 收尾。

- 21 先做：改名是迁移类改动，后面两条都要引用新名字。
- 20 再做：角色正文定稿。
- 22 最后：加载句写在命令正文里，和 20 改的是同一批文件，放在 20 之后避免改两遍。

工作方式：插件正文的改动先出稿，交 PO 批注后再落盘；每个工作项完成就提交，不推送。

### 工作项分解（每项 ≤1 天）

#### PBI-21

- 21-A 动手前问 PO：L47 的取舍（21-5）
- 21-B 改名迁移：`git mv` 目录、改 frontmatter、改全仓引用；grep 零残留；过 plugin-validator
- 21-C SKILL.md 分清两套五步：全文稿交 PO 批注后落盘；过 skill-reviewer
- 21-D 回归验证（21-4）

**21-D 方法与判定标准**（2026-10-25，跑之前写定）

- 方法：`reclaude -p --plugin-dir S:/IDEO-Scrum/plugins/ideo-scrum --model sonnet`，在一个空的临时目录里无头跑，禁用写文件和命令类工具，用 `--output-format stream-json --verbose` 留下工具调用记录。`--plugin-dir` 载入的同名插件会顶替本机已装的 v3.2.0（docs：plugins/loading「Name conflicts」第 2 条；`plugin details` 实测来源为 `ideo-scrum@inline`，含 ideo-kernel）。测得到 description 的触发和正文的结构。
- 题目（两组都是「如何让社区图书馆吸引更多年轻人」，只要工作大纲：每步标题加一两句，不写文件）：
  - A 组：「用 IDEO 五模式……」
  - B 组：「帮我做一个设计冲刺……」
- A 组判对：① 调用了 `ideo-scrum:ideo-kernel`；② 大纲的主干依次是共情、定义、构思、原型、测试；③ 主干里没有挑战、目标与问题、问专家、地图、目标点。任一条不满足判错。
- B 组判对：① 调用了 `ideo-scrum:ideo-kernel`；② 主干先依次是挑战、目标与问题、问专家、地图、目标点；③ 之后有 HMW（How Might We）一步，再接构思、原型、测试。任一条不满足判错。
- 局限：每组只跑一次，模型输出有随机性；用户级 CLAUDE.md 照常加载。

#### PBI-20

- 20-A 「只有 PO 必须是人」的落位与措辞稿 → PO
- 20-B stakeholder 改写：逐句对照稿 → PO
- 20-C scrum-master 的派活、审阅段；developer 的证据段 → PO
- 20-D 三个命令的措辞微调清单 → PO

#### PBI-22

- 22-A 核对加载写法（22-2）
- 22-B 四个命令加上加载句，并验证（22-4）

#### 收尾

- 全量验证：plugin-validator + skill-reviewer + 无死链
- 版本号与发版（PO 定）
- Sprint Review：Master 派审阅子代理核对增量，PO 或 Master 召唤 stakeholder 给外部视角 → Retro → 蒸馏闭环（四段式日志 + 记忆档 + 删除 SprintBacklog）

### 进展记录

| 日期 | 工作项 | 状态 | 备注 |
| --- | --- | --- | --- |
| 2026-10-24～25 | Sprint Planning 与 SprintBacklog 落盘 | 完成 | 选材 PBI-21、20、22；AC 基线成文，经 PO 批注 |
| 2026-10-25 | 21-A L47 的取舍 | 完成 | PO 定：不绑定也不割裂，诚实写明两者的关系——设计冲刺是更快的做法，前半段借《Sprint》的前几步（挑战、目标与问题、问专家、地图、目标点）快速定目标，后面仍用 IDEO 的模式（构思、原型、测试）；两套各是什么、何时用写清楚。落文归 21-C |
| 2026-10-25 | 21-B 改名迁移 | 完成 | `git mv` 目录、frontmatter `name`、标题；scrum-kernel 描述与正文、README、ATTRIBUTION 引用同改；`git grep -i design-kernel` 只剩日志与锚点里的历史记录。plugin-validator PASS（0 critical）；4 条 warning 均为改名前就有的：stakeholder 描述称自己为 skill（归 20-B 一并看）、IDEO-modes 五件许可行指向仓库根的 ATTRIBUTION.md、两个 SKILL.md 无 Source/License 头、SGEP asset 头格式，留到 Review 报给 PO。Master 审阅：无本次引入的偏离；21-2 计划里的「CLAUDE.md 全改」，历史锚点（第 18 行）除外 |
| 2026-10-25 | 21-C 两套五步写清 | 完成 | SKILL.md 新增「Two Schemes」一节（对照表 + 路由规则，作者设计 10-25）；设计冲刺五阶段之后先用 How Might We 问题打开构思（画完地图通常顺手就有），再接构思、原型、测试（PO 确认，第 28 行同改）；Use Protocol 新增第 1 步「先认清用户要哪套」。五阶段参考由 `IDEO-modes/` 迁到 `design-sprint/`——推翻 08-31 的落位，由 Master 依 PO 授权放行，理由是目录名把两套五步混在一起；迁移只改路径，五份文件「see ATTRIBUTION.md」的既有 warning 留到 Review。plugin-validator PASS；skill-reviewer 4 条必改已落：HMW 括注写明「地图与目标点代替 POV」（HMW 方法的触发是 POV 就绪）、路由规则补 HMW 与「两套都未点名时按 Use when 判断，仍不清就问用户」、「do not swap in」补 Ask the Experts；它指出的 description 与新节的张力归 22-3 |
| 2026-10-25 | 21-D 回归验证 | 部分通过 | 按事先写定的标准：**B 组判对**（调用 ideo-kernel；挑战→目标与问题→问专家→地图→目标点→HMW→构思→原型→测试）。**A 组判错**：首跑主干是共情→定义→构思→原型→测试、没混入设计冲刺结构（AC 21-4 原文满足），但没有调用 ideo-kernel，凭模型自身知识作答，第 ① 条不满足。加跑 A 组两次（只看触发率，不改判定）：两次都调用了 ideo-kernel，结构全对。结论：正文加载后 3/3 路由正确；「用 IDEO 五模式」的触发 3 次里有 1 次没触发，归 22-3（description）处理。原始输出存于本组会话共享笔记目录 `21-D/`（A、A2、A3、B 的 .md 与 .jsonl） |
| 2026-10-25 | PBI-21 收尾 | 完成 | Master 定：PBI-21 完成，待 Sprint Review 由 PO 验收；第 ① 条判定与 A 组判错照实保留；未触发问题记进产品日志 PBI-22 的 22-3 开放点。转入 PBI-20 |
| 2026-10-25 | PBI-20 角色重定义（20-A～20-D） | 完成 | 稿经 Master 审、PO 批准。scrum-kernel 的 Roles 段加作者注记（只有 PO 必须是人）；stakeholder 一个命令多种身份、可常驻做非源码杂务、源码归 Developer、独立外部视角仍由全新子代理给；scrum-master 加「派活跟进度」「派子代理审阅」；developer 加「完工交证据」与条件句「有 SM 派活时向它汇报、请放行」（Master 改为条件句，保插件自足）；designer 改「Test feeds back」、补设计冲刺先行一句。SG2020 原文两节与 Stakeholder Voices 节与改前逐字一致（脚本比对）。skill-reviewer 3 条必改与 1 条可选已落：注记补 SGEP「至少一名 Product Developer 应为人」；「跟进度」写明是问状态、报给 PO，步骤、顺序、节奏归 Developer；交给常驻 stakeholder 的限于维护看板；SM 给出或扣下放行。另一条可选（stakeholder 描述边界句偏多）为既有问题，留到 Review |
