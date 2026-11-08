# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这个仓库是什么

两层结构，改动前先分清在哪一层：

| 层 | 位置 | 性质 |
|---|---|---|
| **插件本体** | `plugins/ideo-scrum/` | 交付物。别人安装的就是这里 |
| **工作记录** | `scrum/`（含 `scrum/documents/`） | 用本插件的方法论开发本插件的过程记录 |

`scrum/` 放 Scrum 的全部工作（产品日志 + `sprint-NN-后缀/` 冲刺 + `design-后缀/` 设计 + `documents/`）；`scrum/documents/` 放为整个 Scrum 服务的文档（ExpertNotes 客户之声、研究稿、收官归档的冲刺日志与设计 Review），日志里引用（2026-11-08，Sprint 10 从根目录的 docs 文件夹迁入）。1.x 的 sprint 日志是**历史记录**，教训已蒸馏入 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（原文 git 历史可追溯），不回改。除非发现事实错误，否则不要回头修改已完成 sprint 的内容。

## 当前状态（蒸馏锚点，随 Sprint 更新；只留最近三条，更早的见 `git log -p -- CLAUDE.md`）

- **2026-11-08 · Sprint 10 收官（流程全部进插件）**：Sprint Goal「流程全部进插件」达成（一天，Master 在主会话，Developer 由 Master 会话 fork 出来，不开 worktree）。PBI-39、31、23：scrum-kernel 新建 `conventions/`（总览 16 条、产品日志约定 18 条与模板、冲刺日志约定 21 条与模板）；PBI-37：design-kernel 补开设计、接手（文件头 Now 一行）与目标不变；PBI-32：四个命令跟上约定。PO 定：约定要短（砍字不砍规矩，一条规矩只写一处，引文只标故意不同之处）；约定不写工具机制；How 是方案不是步骤；目标不变其余可调；不要修订记录；PBI 编号 PBI-001；规模按会话数；文档文件夹 `scrum/documents/`（原根目录的 docs 文件夹迁入）；scrum-kernel 描述补 Product Backlog、Sprint Backlog（729 → 943 字符），描述可以改、重跑触发不变差。三轮测试（Haiku）最终全部过线；插件校验 PASS、对抗审查基本通过、技能审阅 21 项全改；「熟手」「陌生人」能用但有保留 → PBI-40、PBI-30。产品日志 2.2 精简为 Map（原文 `git show 3b24287:scrum/ProductBacklog.md`），修订记录删除。冲刺日志归档 `scrum/documents/sprint-10-conventions.md`。发版 v5.1.0，tag `v5.1.0`、`sprint-10-conventions`，未推送。Product Goal 这次不定（PO：以后可能要重构，下次再定）。待办：全局记忆先不删（Master 定）——推送并更新安装之前，别的项目用的还是已安装的 v4.0.0，现在删就断了规矩；v5.1.0 推送、装好以后，删「Sprint 收尾做法」，其余四条（压缩代替交接、会话角色分层、plan 视图审阅、派活分工）精简到只留 Claude Code 或 SeaPawn 特有的部分，记在 PBI-30 备注里，发布时一并做。下一步：PO 通读插件的约定和文档，提出一些小改动，到时开一个小冲刺来改。
- **2026-11-08 · Sprint 09 收官（小冲刺），发版 v5.0.1**：PO 发现 Sprint 08 交付的设计日志模板把原书和约定的每一步都开成了一节，与 PO 说的不同，单开小冲刺改正（PBI-38）：日志只记产出（共情 1.1～1.3；定义 Map、HMW；构思 3.1 方案、3.2 故事板可选；原型、测试不分节）；不设选靶（设计本身就是靶，一份装不下就拆出去另开）；构思写明 IDEO 构思的方法同样要用。Planning 并成一份 plan，PO 逐段看过改动全文后批准即放行；Master fork 出 Developer 施工，Master 与 PO 同时在主会话聊下一个冲刺；全新 Haiku 子代理对照 plan 核对，A～D 全部 verified；B 组触发（Haiku）脚本 4/5、人工改判后 5/5。路线顺延：10 冲刺流程进插件（PBI-23、31），11 角色接上约定（PBI-32、25）。冲刺日志归档 `scrum/documents/sprint-09-design-template.md`。tag `v5.0.1`、`sprint-09-design-template`，未推送。
- **2026-11-08 · Sprint 08 收官，发版 v5.0.0**：Sprint Goal「设计内核独立」达成（一天，Master 兼 Developer，不开 worktree）。PBI-34：新建 design-kernel，按 IDEO 五阶段放《Sprint》原文摘录（只删不改，与人机协作无关的删去，例图改画成 Mermaid 或文字），加设计日志约定 20 条与五章模板（PBI-28）；PBI-29：ideo-kernel 成为整个插件共用的工具箱、各阶段的基础，方法不限当前模式；scrum-kernel 的预研究改为开设计；PBI-36：四个命令都先加载 ideo-kernel。触发回归（Haiku，`claude -p`）A、B、C 5/5，命令全 2/2；validator、skill-reviewer、对抗审查（复核通过）、「熟手」Stakeholder（能用但有保留 → PBI-37）。冲刺日志压缩后归档 `scrum/documents/sprint-08-design-kernel.md`（第一份按新做法归档的冲刺）。产品日志 2.2.3 增「拿不准就问 PO」；DoD 删「≤2 轮进入执行」；路线：09 冲刺流程进插件（PBI-23、31），10 角色接上约定（PBI-32、25）。tag `v5.0.0`、`sprint-08-design-kernel`，未推送；codex 分支未同步（留到 PBI-30）。
- 更早的状态（2026-08-31 至 11-07：#28 讨论定案各条、Sprint 07 收官、Sprint 08 撤销与产品日志精化出架构 v1）见 `git log -p -- CLAUDE.md`；教训已蒸馏入记忆档 sprint-06-dual-kernel-refactor、sprint-07-roles-kernels。
- **1.x 已收官蒸馏**：旧目标（两内核结构对等）判定方向性错误，勿延续；教训见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（MEMORY.md 索引 + 五期档案）。

## 维护规约

**README 是文件索引与当前状态，Git 历史负责追溯过去。**

- README 面向外部读者：只陈述这里是什么、文件地图、来源授权；作者侧的当前状态不入 README——由本文件「当前状态」锚点与 `scrum/ProductBacklog.md`（产品日志）承担
- 提交前确认 README 是否需要同步更新——尤其是新增/删除/重命名文件、改动插件版本号时
- 若发现 README 已过期、可能误导新会话的 LLM，必须显式提醒用户更新，不要默默放过
- 追溯旧决策、文件演变、阶段状态时，放手查阅 Git 历史

**版本号与 tag**

- 主干分支是 `main`，永远指向最新状态
- 版本号用 tag 标记，不写进分支名
- 插件版本号在 `plugins/ideo-scrum/.claude-plugin/plugin.json`，改动时 README 的两处版本号需同步

**组件描述（attribute description）规约**

写插件组件（skill / command）的 `description` 时：它是**触发条件**，不是自我介绍——用 "Use when..." + 具体场景词；同类组件描述必须有区分度（模板趋同 = embedding 空间互相叠影，系统无法选择）。plugin.json 的 description 是元数据（展示用），非触发主战场。（来源：Sprint 04。）角色命令可以在触发句之后追加一两句边界和相互关系（替谁做事、不做什么、谁召唤谁），让各角色在技能清单里互相知道；触发句保持在最前（2026-10-13，#14）。模型自以为懂的通用词（如 design sprint）容易不加载就直接答：描述里写明这里的版本和常见的不同、要照技能答，不凭记忆（2026-11-08，Sprint 08：B 组 2/5 → 5/5）。触发不足时，写明「什么情况下先加载」，不要只堆关键词（2026-10-25，PBI-22：ideo-kernel 的触发由 1/10 升到 5/5）。 描述可以改，改了就重跑触发测试，结果不能比改前差（PO 2026-11-08）。Scrum 的通用词（如 Product Backlog、Sprint Backlog）也要写进描述，并写明什么时候先加载：模型以为自己懂的事，不写就不加载（Sprint 10：P 组 3/5 → 5/5）。

**模板规约**（2026-11-08，Sprint 09 Retro）

模板的章按流程分，节只放产出；做法写在约定里，不在模板里一步开一节。交付新模板或新结构时，验收前把结构（章节清单）单独摆给 PO 看，不混在整份审阅里。（Sprint 08 的设计日志模板照产品日志 2.2.6 表里的每个活动各开一节，把做法写成了要记的东西；验收时没单独看结构，PO 第二天才发现。）

**冲刺收官与归档**（2026-11-07 改，原「冲刺蒸馏闭环」；Sprint 01–07 按旧做法蒸馏为记忆档，不回改）

- **Review**：备料（Master 兼 Developer 时，对抗审查交全新子代理，只核对做得对不对；另照产品日志 2.1 召唤角色卡看增量，回答好不好用——2026-11-08）→ 冲刺日志压缩成关键决定、补上 Review 章 → 改名为冲刺文件夹名（`sprint-NN-后缀.md`）移进 `scrum/documents/` → 删除冲刺目录里其余的中间文件 → 更新产品日志并保鲜（做完的 PBI 移入 3.2 并引用该文件，删掉过时内容；没做完的回 3.1）→ 整个 `scrum/` 过一遍，`documents/` 里过时的删掉（2026-11-09 改顺序：先写完 Review 再删中间文件）。
- **Retro**：教训写进记忆（`S:\SeaPawn-Memory\memory\IDEO-Scrum\`，路径以 `.claude/settings.json` 的 `autoMemoryDirectory` 为准）或本文件；写原则、不写故事；特别好的改进经 PO 同意写进 DoD。冲刺日志不设 Retro 章。
- **收官**：项目健康看 `scrum/` 就够，其余一般只需同步 README；Review 与 Retro 只出一个提交；tag 与冲刺文件夹同名（同名分支随即删除）；合入 main，关分支与 worktree。
- **设计收官**（2026-11-07）：设计问题答完或 PO 叫停时，整份设计日志重写成 Review 文档，改名 `design-后缀.md` 移进 `scrum/documents/`，原型等文件删除，产品日志保鲜；Retro 同冲刺。

> 分工：**memory 管教训**（见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\MEMORY.md`），**`scrum/documents/` 管冲刺与设计原文**（压缩后的冲刺日志、设计 Review），**git 管全部历史**，**`scrum/` 其余部分管现状**（产品日志、当期冲刺与设计）。完整流程见插件 scrum-kernel 的 `conventions/sprint-log.md`。

**Sprint 节律**（2026-10-24，Sprint 06 Retro；2026-11-07 改）

- **按 Sprint Goal 收官**（2026-11-07 改，原「按时间盒收官」）：Sprint Goal 达成或 PO 叫停时收官，做 Review + Retro（单提交）；冲刺日志不写截止日（AI 按会话工作，日期没有意义；与官方定长不同，理由见插件 scrum-kernel 的 `conventions/sprint-log.md` 第 2 条）；期间发版照常，记进当期日志，不结束 Sprint；之后的新工作开新 Sprint、新日志；日志当日记，不事后补录。
- **没做完的回产品日志**：收官时没做完的 PBI 回产品日志，不顺延。（原「时间盒写在日志头」，2026-11-07 删去截止日。）
- **计划外工作先登记**：作者待办或对话中定下的新工作，先在产品日志登记 PBI，再由 PO 定是否进当前 Sprint（范围可重谈，Sprint Goal 不变）；不进则等下个 Sprint。
- **小活单开小冲刺**（PO 2026-11-08，Sprint 09）：半小时到一个会话做得完的活也开冲刺，正常流程照走，每一步缩到一两行；放行、审阅、收官照做（插件 scrum-kernel 的 `conventions/sprint-log.md` 第 4 条）。
- **fork 出来的 Developer**（2026-11-08，Sprint 09、10）：它是主会话的子代理，主会话一进 plan 模式，它就停下、写不了文件，Developer 干活时主会话别切 plan 模式；它不能再派子代理，审阅、插件校验、角色召唤都由 Master 派；它带着 Master 的上下文，但活是它干的：审阅照常由 Master 做，也可以派全新子代理（PO 2026-11-09，插件 sprint-log 约定 16；Sprint 12 起生效）。Master 自己兼 Developer 时，审阅仍交全新子代理。
- **约定大约每周集中改一次**（PO 2026-11-09，原插件总览约定 14 的前半句；那是作者维护插件的节奏，不是用户的规矩，挪到这里）：平时记下约定不合适的地方，攒着集中改，登记成 PBI、开冲刺改；改动从下一个冲刺起生效，冲刺进行中不改。
- **PBI 状态只写产品日志**：SprintBacklog 引用 PBI 编号，不复写状态；进展写在 3.2 笔记。
- **工作区留着别的改动时，`git add` 逐个写文件**，不按目录加（2026-11-08，Sprint 08 误带过一次，撤回重提）。
- **迁移类改动全仓 grep**：路径、位置、名称迁移时，同一提交内全仓 grep 旧值至零残留（README、CLAUDE.md、日志都算）。

**插件验证**

本仓库无 build/test。改动插件后，用 Agent 类型 `plugin-dev:plugin-validator` 校验插件结构/plugin.json；涉及 skill 质量时用 `plugin-dev:skill-reviewer`（两者经 Agent 工具调用，非 slash command）。marketplace 清单在 `.claude-plugin/marketplace.json`。

**回归测试**（2026-10-25，Sprint 07 Retro）

- 判定标准先写、单独提交，再跑；出结果后不改标准。
- 用 Haiku 跑（PO 2026-11-08：测试要用便宜的模型）。
- 脚本按关键词判断大纲顺序会误判；判错的逐条人工看，改判写明理由，验收时摆给 PO（2026-11-08）。
- 触发测两条路径：从角色命令进入，和直接说。
- 比较描述效果，同日同环境对照，带改前基线。
- 无头测法：`reclaude -p --plugin-dir <插件 Windows 路径>`（顶替已装同名插件；reclaude 不可用时用本机 `claude -p`，参数相同，PO 2026-11-08）；Git Bash 下 `/` 开头的提示加 `MSYS_NO_PATHCONV=1`，路径用 `cygpath -w`。
- 工具审查员（skill-reviewer 等）的必改项，落盘前先对一遍 PO 的定案；冲突就报 Master，不照改。
- 测试题不带引导词（如「按插件的约定」）：引导词等于叫模型去加载插件，测不到用户自然的说法；题里也别有会限制它行动的话（「先别看东西」被当成「别读文件」）（2026-11-08，Sprint 10）。
- 判对不只看加载了哪个技能，还要看读没读该读的约定（Sprint 10：加载了 scrum-kernel 却只读 references，答出两周冲刺）；用 Grep 读到文件内容也算读了。
- 判定脚本先拿一两份已知结果自测再用（Sprint 10：正则里混进一个退格符，三份对的回答全被判错）。
- Windows 上无头测试要连 PowerShell 一起禁（只禁 Bash 拦不住）；要写文件的测试不放在 `~/.claude` 下，那里会被权限系统拦写，改用系统临时目录。

## 源材料与授权

插件内所有第三方摘录必须带署名。新增摘录时：

1. 文件顶部标注 `> Source:` 与 `> License:` 两行，License 须与 [ATTRIBUTION.md](ATTRIBUTION.md) 中记录的条款一致
2. 若引入新来源，先在 ATTRIBUTION.md 中登记，再写摘录

> 例外：命令类组件（`commands/*.md`）的抄录主体不设文件头两行；其署名义务由 ATTRIBUTION.md 的登记承担。

**原文优先**（PO 2026-11-07）：写方法流程时能用原文就用原文；原书例图改画成 Mermaid（flowchart TD）或写成文字，不放图片文件（PO 2026-11-08）；不是原文的写法写进 `conventions/`，标为约定建议。删减的标准：和人机协作无关的删去（日程、周几、零食与休息、白板与用品、线下投票这类；PO 2026-11-08）。只删不改的摘录用脚本按行号从原书取；删完查一遍悬空的句子：指向已删图片的引导句（like this:）、指向原书其他章的句子、没了指代的句子（2026-11-08，Sprint 08 对抗审查查出十几处）。 引文以插件里带的原文为准：SGEP 以 `assets/` 里的 v2026.1 为准，references/ 里的句子先核对原文再引（Sprint 10 查出 SKILL.md 与 references/ 把 2025.6 版的内容标成了 v2026.1，见 PBI-25 ⑥）。

**已知的授权约束：**

- Scrum Guide 2020 / SGEP —— CC BY-SA 4.0，可摘录、可商用
- Stanford d.school Bootleg —— CC BY-**NC**-SA 4.0，含非商业限制
- 《Sprint》(Knapp) —— 全版权；版权由 PO 负责，发布前声明（PO 2026-11-07）。写流程原文优先、例图改画成 Mermaid 或文字（见上）

`references/` 是源材料原件，**不入库**（`.gitignore` 已拦截），仅存于作者本地。

## 插件内容的自足性

插件会运行在别人的 Claude Code 里，那里没有本仓库的上下文，也没有作者的全局配置。

**写插件内容时，不要依赖任何未在插件内言明的约定。** 例如「用 mermaid 画图」必须同时说明方向（`flowchart TD`），否则在他人环境中行为不一致。
