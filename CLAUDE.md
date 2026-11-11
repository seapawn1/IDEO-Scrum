# IDEO-Scrum

为 Claude Code 与 Codex 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这个仓库是什么

三块，改动前先分清在哪一块：

| 块 | 位置 | 性质 |
|---|---|---|
| **插件本体** | `plugins/ideo-scrum/` | 交付物。Claude Code 用户安装的就是这里 |
| **Codex 分发包** | `codex/plugins/ideo-scrum/` | 生成物，不手改：由 `scripts/sync_codex.py` 从插件本体生成（2026-11-10，Sprint 13） |
| **工作记录** | `scrum/`（含 `scrum/documents/`） | 用本插件的方法论开发本插件的过程记录 |

`scrum/` 放 Scrum 的全部工作（产品日志 + `sprint-NN-后缀/` 冲刺 + `design-后缀/` 设计 + `documents/`）；`scrum/documents/` 放为整个 Scrum 服务的文档（ExpertNotes 客户之声、研究稿、收官归档的冲刺日志与设计日志），日志里引用（2026-11-08，Sprint 10 从根目录的 docs 文件夹迁入）。1.x 的 sprint 日志是**历史记录**，教训已蒸馏入 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（原文 git 历史可追溯），不回改。除非发现事实错误，否则不要回头修改已完成 sprint 的内容。

## 当前状态（蒸馏锚点，随 Sprint 更新；只留最近三条，更早的见 `git log -p -- CLAUDE.md`）

- **2026-11-12 · Sprint 15 收官（小冲刺），版本不动，仍 5.2.0**：Sprint Goal「反馈落地」达成（PBI-55）。先开设计 design-feedback-loop（2026-11-11）：PO 用自己的产品时冒出的点，想到就交给手边的 AI，卡在每次要报一长串位置；PO 定反馈进全局记忆，用着就能验证。Master 兼 Designer 和 Scrum Master，另开的辅助会话在设计里用 Stakeholder 身份、在冲刺里当 Developer，落盘、发散、搭原型、跑测试，Master 写 plan 文件、用跨会话消息派活。三轮 Haiku 测试（各 33 次）问题 1–5 是，问题 6（产品改之前就照着做）还没有（2/3）；干净对照里那一行把地图从 16–23 个框收到 5–6 个。装在 S:\SeaPawn-Memory：SEAPAWN.md 加 Feedback 一节，全局记忆 MEMORY.md 末尾加 Feedback 一节，迁入 PO 的 6 个点；PO 看后改成全英文、产品表先只写 IDEO-Scrum，不再测试；Master 自己的两条发现进 PBI-54 ⑦⑧；登记 PBI-56（设计冲刺与 IDEO 五阶段法分清）。PO 事后说看晚了：原型出来、测试之前就该看。日志归档 scrum/documents/design-feedback-loop.md、sprint-15-feedback-loop.md；tag sprint-15-feedback-loop；PO 2026-11-12 同意推送 main、tag 和 SeaPawn-Memory。
- **2026-11-10 · Sprint 14 收官，发版 v5.2.0**：Sprint Goal「约定精调」达成（PBI-49，连同 47、48、50、40；当天开工当天收官）。Developer 是从 Master 会话 `/fork` 出的独立会话，在 worktree 里干活，与 Master 用跨会话消息直接通讯。PO 逐份强审四份约定（overview 17 条、product-log 18 条、sprint-log 25 条、design-log 26 条）和冲刺、设计两份模板，只改 Claude 侧：每份约定先一张图再一批约定，一条规矩只写一处；冲刺日志改成五章（Why、What、How、Increment、Test），设计日志同样五章；阶段之间由 PO 决定；Review 和 Retro 是收官动作、不设章，设计不单做 Review 和 Retro（设计日志由设计结束后的第一个冲刺 Review 归档，教训进那个冲刺的 Retro）；产品日志有「白纸」入口，从设计开始、结论回流；IDEO 在设计每个阶段都要用；约定不带版本标记。本冲刺自己的日志仍按 5.1.2 的四章写，新结构从 Sprint 15 起生效。验收：四轮 Haiku 流程测试，题 1、4、5 每轮 3/3，题 2 第二轮起 2/3 过线，题 3（白纸项目）四轮 0/3——缺口在触发和先读约定，登记 PBI-52；样板测试 14 对 15 没过线，PO 让往下走；对抗审查（全新子代理）7 处必改；plugin-validator 四次 PASS；「熟手」卡愿意照新版走，缺口登记 PBI-54，PBI-40 ⑧ 拆成 PBI-53。冲刺日志归档 `scrum/documents/sprint-14-conventions-tuning.md`；tag `v5.2.0`、`sprint-14-conventions-tuning`；PO 2026-11-10 同意收官后推送 main 与两个 tag，并更新本机 Claude Code 的插件；Codex 包已同步到 5.2.0，本机 Codex 的安装不动。
- **2026-11-10 · Sprint 13 收官（Codex 版），版本不动，仍 5.1.2**：Sprint Goal「Codex 版跟上」达成（PBI-43；2026-11-09 开工）。Developer 是 Codex（GPT），Master 在 Claude Code，只靠冲刺日志通讯，PO 传话。Codex 包 `codex/plugins/ideo-scrum/` 并入 main（不再单靠 `codex` 分支），由 `scripts/sync_codex.py` 从 `plugins/ideo-scrum/` 一条命令生成，`scripts/check_codex.py` 核对：三个内核逐字相同，四个角色由命令生成，只改加载内核的 5 句工具说法；Claude 侧文件零改动。验收 4 的五题在 Codex 里 5/5（gpt-5.6-terra，隔离安装）；测法因环境改过两次，题目和过线标准没改。对外文字用英文，根 README 仍中文，给旧 `codex` 分支的用户补了迁移命令。原始输出带了模型服务地址：备份到仓库外 `S:\IDEO-Scrum-Archives\`，改写了未推送的冲刺历史（PO 同意）。PO 定：版本与 Claude 一致。推送后旧 `codex` 分支已删（存档 tag `codex-v3.2.0`）：合入 main 后根目录有 `codex/` 目录，与分支同名，旧的 `--ref codex` 装法在 git 里有歧义、装不上；本机 Codex 已改装为 5.1.2（Codex 执行迁移命令，Master 核对）。冲刺日志归档 `scrum/documents/sprint-13-codex.md`；tag `sprint-13-codex`；main 与两个 tag 已推送。后续小修登记为 PBI-46；开下一个冲刺前核对 Product Goal（产品日志 1.2）。
- 更早的状态（2026-08-31 至 11-09：#28 讨论定案各条、Sprint 07 收官、Sprint 08 撤销与产品日志精化出架构 v1、Sprint 08 收官发版 v5.0.0、Sprint 09 收官发版 v5.0.1、Sprint 10 收官发版 v5.1.0：流程全部进插件、Sprint 11 收官发版 v5.1.1：约定照 PO 审阅改定、Sprint 12 收官发版 v5.1.2：overview 挪到 scrum-kernel 根目录）见 `git log -p -- CLAUDE.md`；教训已蒸馏入记忆档 sprint-06-dual-kernel-refactor、sprint-07-roles-kernels。
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
- **Codex 包随版本一起提交**（PO 2026-11-09：版本与 Claude 一致）：改了 `plugins/ideo-scrum/` 或版本号，同一提交里跑 `python scripts/sync_codex.py`，再跑 `python scripts/check_codex.py`（需要 PyYAML）；Codex 清单的版本由脚本取自 Claude 清单，包内 README 的版本由清单生成。（Sprint 13：旧 `codex` 分支靠手工同步，落后六次发版。）
- Windows 上 `core.autocrlf=true` 时，新克隆后第一次跑同步，会把生成的 JSON/YAML 的换行从 CRLF 改成 LF，内容与已提交的一样：看 `git diff`，或 `git add -A` 后有没有暂存，别只看 `git status` 的 M。

**组件描述（attribute description）规约**

写插件组件（skill / command）的 `description` 时：它是**触发条件**，不是自我介绍——用 "Use when..." + 具体场景词；同类组件描述必须有区分度（模板趋同 = embedding 空间互相叠影，系统无法选择）。plugin.json 的 description 是元数据（展示用），非触发主战场。（来源：Sprint 04。）角色命令可以在触发句之后追加一两句边界和相互关系（替谁做事、不做什么、谁召唤谁），让各角色在技能清单里互相知道；触发句保持在最前（2026-10-13，#14）。模型自以为懂的通用词（如 design sprint）容易不加载就直接答：描述里写明这里的版本和常见的不同、要照技能答，不凭记忆（2026-11-08，Sprint 08：B 组 2/5 → 5/5）。触发不足时，写明「什么情况下先加载」，不要只堆关键词（2026-10-25，PBI-22：ideo-kernel 的触发由 1/10 升到 5/5）。 描述可以改，改了就重跑触发测试，结果不能比改前差（PO 2026-11-08）。Scrum 的通用词（如 Product Backlog、Sprint Backlog）也要写进描述，并写明什么时候先加载：模型以为自己懂的事，不写就不加载（Sprint 10：P 组 3/5 → 5/5）。

**模板规约**（2026-11-08，Sprint 09 Retro）

模板的章按流程分，节只放产出；做法写在约定里，不在模板里一步开一节。交付新模板或新结构时，验收前把结构（章节清单）单独摆给 PO 看，不混在整份审阅里。（Sprint 08 的设计日志模板照产品日志 2.2.6 表里的每个活动各开一节，把做法写成了要记的东西；验收时没单独看结构，PO 第二天才发现。）约定的条同理按执行顺序排，被依赖的排前面（Sprint 14 样板测试：定分支排在填表头之后，模型照条号走，先填了表头）。

**冲刺收官与归档**（2026-11-07 改，原「冲刺蒸馏闭环」；2026-11-10 Sprint 14 改成新结构；Sprint 01–07 按旧做法蒸馏为记忆档，不回改）

- **Review 和 Retro 是收官时的动作，日志里不设章**（PO 2026-11-10，Sprint 14；新结构从 Sprint 15 起生效，Sprint 14 自己的日志仍按 5.1.2 写，有第 4 章 Review）。Review：备料（Master 兼 Developer 时，对抗审查交全新子代理，只核对做得对不对；另照产品日志 2.1 召唤角色卡看增量，回答好不好用——2026-11-08）→ 冲刺日志压缩成关键决定 → 改名为冲刺文件夹名（`sprint-NN-后缀.md`）移进 `scrum/documents/` → 删除冲刺目录里其余的中间文件 → 更新产品日志并保鲜（做完的 PBI 移入 3.2 并引用该文件，删掉过时内容；没做完的回 3.1；利益相关者的看法和 Product Goal 的变化写进产品日志）→ 整个 `scrum/` 过一遍，`documents/` 里过时的删掉（2026-11-09 改顺序：先写完再删中间文件）。已经结束、还在自己文件夹里的设计，它的日志同样压缩、改名 `design-后缀.md` 移进 `scrum/documents/`。
- **Retro**：教训写进记忆（`S:\SeaPawn-Memory\memory\IDEO-Scrum\`，路径以 `.claude/settings.json` 的 `autoMemoryDirectory` 为准）或本文件；写原则、不写故事；特别好的改进经 PO 同意写进 DoD。冲刺日志不设 Retro 章；设计不单做 Retro，设计结束时记在设计日志第 5 章末尾的一两句做法教训，由归档那份日志的冲刺的 Retro 整理。
- **收官**：项目健康看 `scrum/` 就够，其余一般只需同步 README；Review 与 Retro 只出一个提交；tag 与冲刺文件夹同名（同名分支随即删除）；合入 main，关分支与 worktree。

> 分工：**memory 管教训**（见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\MEMORY.md`），**`scrum/documents/` 管冲刺与设计原文**（压缩后的冲刺日志与设计日志），**git 管全部历史**，**`scrum/` 其余部分管现状**（产品日志、当期冲刺与设计）。完整流程见插件 scrum-kernel 的 `conventions/sprint-log.md`。

**Sprint 节律**（2026-10-24，Sprint 06 Retro；2026-11-07 改）

- **按 Sprint Goal 收官**（2026-11-07 改，原「按时间盒收官」）：Sprint Goal 达成或 PO 叫停时收官，做 Review + Retro（单提交）；冲刺日志不写截止日（AI 按会话工作，日期没有意义；与官方定长不同，理由见插件 scrum-kernel 的 `conventions/sprint-log.md` 的 No end date）；期间发版照常，记进当期日志，不结束 Sprint；之后的新工作开新 Sprint、新日志；日志当日记，不事后补录。
- **没做完的回产品日志**：收官时没做完的 PBI 回产品日志，不顺延。（原「时间盒写在日志头」，2026-11-07 删去截止日。）
- **计划外工作先登记**：作者待办或对话中定下的新工作，先在产品日志登记 PBI，再由 PO 定是否进当前 Sprint（范围可重谈，Sprint Goal 不变）；不进则等下个 Sprint。
- **小活单开小冲刺**（PO 2026-11-08，Sprint 09）：半小时到一个会话做得完的活也开冲刺，正常流程照走，每一步缩到一两行；放行、审阅、收官照做（插件 scrum-kernel 的 `conventions/sprint-log.md` 的 Small work, small Sprint）。
- **fork 出来的 Developer**（2026-11-08，Sprint 09、10；2026-11-10 Sprint 14 补）：有两种 fork，别混。① Agent 工具派出的 fork 子代理（Sprint 09、10）：它是主会话的子代理，主会话一进 plan 模式，它就停下、写不了文件，Developer 干活时主会话别切 plan 模式；它不能再派子代理，审阅、插件校验、角色召唤都由 Master 派。② `/fork` 复制出的会话（Sprint 14）：它是独立会话，能派子代理，不受主会话 plan 模式影响；Master 与它用跨会话消息直接通讯，不经 PO 转，长的审阅写在 plan 文件里、消息里给路径。两种都带着 Master 的上下文，但活是 Developer 干的：审阅照常由 Master 做，也可以派全新子代理（PO 2026-11-09，插件 sprint-log 的 A reviewer is required；Sprint 12 起生效）。Master 自己兼 Developer 时，审阅仍交全新子代理。派子代理一律显式写 `model`（Haiku），见用户级 CLAUDE.md（Sprint 14：四次 plugin-validator 没写 model，继承了主会话的 Sonnet，每次约 22 到 27 万 token）。
- **Developer 在别的工具里（Codex，Sprint 13）**：通道只有冲刺日志；两边共用一个工作目录，轮流动手：每轮提交、在 3.2 记一行并在 Next 写明轮到谁，然后停下；PO 只传一句「轮到你了，读冲刺日志」。Master 的审阅意见写在 plan 文件里，PO 把路径转给 Developer，由它抄进日志（日志才是记录）。放行要写明能做到哪一步：Codex 在 `approval_policy = never`、完全访问下，能自己推送、打 tag、改本机配置。停点要少：把彼此独立的活一次做完再交审，PO 的传话和等待是主要耗时。
- **约定大约每周集中改一次**（PO 2026-11-09，原插件总览的一条约定；那是作者维护插件的节奏，不是用户的规矩，挪到这里，Sprint 14 强审时 PO 又把插件里的那条删了）：平时记下约定不合适的地方，攒着集中改，登记成 PBI、开冲刺改；改动从下一个冲刺起生效，冲刺进行中不改。约定不带版本标记，PBI 标题也不带版本号（PO 2026-11-10：以后更新都是重构，不要版本这种标志）；下一次集中修订是 PBI-54。
- **PBI 状态只写产品日志**：SprintBacklog 引用 PBI 编号，不复写状态；进展写在 3.2 笔记。
- **工作区留着别的改动时，`git add` 逐个写文件**，不按目录加（2026-11-08，Sprint 08 误带过一次，撤回重提）。
- **迁移类改动全仓 grep**：路径、位置、名称迁移时，同一提交内全仓 grep 旧值至零残留（README、CLAUDE.md、日志都算）。
- **改规矩先找它的其他说法**（2026-11-09，Sprint 11 Retro）：一条规矩改了，精化时就全仓 grep 它在模板、命令、两份 SKILL.md、CLAUDE.md 里的其他说法，列成连带改动一起改（Sprint 11 一处审阅意见牵出五组连带改动；删一条带编号的约定要改号，用脚本把每处「convention N」对到短名；Sprint 14：内容改动与改号分开提交，改号后把引用换成短名、去掉条号，改号前后逐行相同才算对，三次改号都是 0 错；脚本只保证引用的条存在，不保证指得对，要逐处读所指的条是不是真有那句话，product-log 17 曾误指向 overview 5；对抗审查的七处必改，多数是同一条规矩在别处的另一种说法）。
- **对着译文审阅，先分清改哪边**（2026-11-09，Sprint 11 Retro）：PO 对着中文译文提的意见，逐条先判是英文原文的问题还是译文的措辞；只是译文的，英文不动，在审阅记录里写明（Sprint 11：overview 第 2 处后半）。
- **大改约定的审阅顺序**（2026-11-10，Sprint 14 Retro）：Developer 起草 → Master 审 → 对抗审查（全新子代理，只核对做得对不对）→ PO 强审 → 最后一轮流程测试 → 收官。对抗审查放在 PO 强审之前，先清掉重复、错指和前后矛盾（Sprint 14：七处必改），PO 的强审才用在方向和口味上（两批共五处）；插件文字改了，流程测试整轮重跑，所以会改文字的审阅都排在最后一轮测试之前，PO 的意见攒齐了再跑（Sprint 14 跑了四轮）。

**插件验证**

Claude 插件无 build/test；Codex 包由 `scripts/sync_codex.py` 生成、`scripts/check_codex.py` 核对（内容与源逐字相同、链接、导航、可重复生成）。改动插件后：官方命令能做的先用命令，不派子代理（PO 2026-11-10）——收官改完版本号后跑一次 `claude plugin validate --strict plugins/ideo-scrum`；只改了文字、结构没变时，它没报问题就够了；它报问题，或改了结构、清单、frontmatter，才派 Agent 类型 `plugin-dev:plugin-validator`，并显式写 `model`（Haiku）。涉及 skill 质量时用 `plugin-dev:skill-reviewer`（两者经 Agent 工具调用，非 slash command）。marketplace 清单在 `.claude-plugin/marketplace.json`；对它跑 `--strict` 会因缺顶层 description 退出 1（警告，Sprint 14 之前就有，见产品日志 PBI-25 ⑦）。

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
- 「不少于改前」这类过线，改前可能满分时要留余量或加次数，并且在跑之前定（Sprint 14 样板：改前 15/15，改后 14，少 1 次就没过线，也测不出结构的好处）。
- 汇总里把行为（有没有触发、读没读约定）和内容（答得对不对）分两栏列，别混成一个分数；缺口出在哪一栏，改法才对得上（Sprint 14：题 3 的内容渐渐答对，缺的一直是触发和先读约定，登记 PBI-52）。
- Windows 上无头测试要连 PowerShell 一起禁（只禁 Bash 拦不住）；要写文件的测试不放在 `~/.claude` 下，那里会被权限系统拦写，改用系统临时目录。
- 测试的原始输出放仓库外，仓库里只留判定汇总；提交前按提供方地址、凭据值、令牌形态、设置值扫一遍（Sprint 13：原始输出带了模型服务地址，只好改写未推送的冲刺历史）。
- 正式测之前先冒烟：一次最简单的调用，确认模型在提供方的实际目录里（不看本地模型缓存）、读文件的权限正常（Sprint 13：第一轮模型无通道，第二轮只读权限拒读，各白跑一轮）。
- 在 Codex 里测角色：`codex exec` 里裸打 `$角色` 挂不上角色，要用 app-server 的原生 Skill 输入；隔离安装用独立的用户目录，不动本机 `~/.codex`。当时的脚本在 `git show sprint-13-codex~1:scrum/sprint-13-codex/run_codex_smoke.py`（Sprint 13）。
- 原型说明里举例，别用正在测的那个点：它等于把那个点又写了一遍，会混进对照（Sprint 15 设计第二轮）。
- 对照组跑之前先确认真的去掉了那样东西：检查最终喂给模型的文件，不只看源文件（Sprint 15：脚本先内联后删行，第一次对照没隔开）。
- 判定标准照被测的那句话写，别比它更严：被测那一行允许「一个环」，标准写成「没有判断分支」，第三轮就有一次卡在这里（Sprint 15）。

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

插件会运行在别人的 Claude Code 或 Codex 里，那里没有本仓库的上下文，也没有作者的全局配置。

**写插件内容时，不要依赖任何未在插件内言明的约定。** 例如「用 mermaid 画图」必须同时说明方向（`flowchart TD`），否则在他人环境中行为不一致。
