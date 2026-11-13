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

- **2026-11-14 · Sprint 19 收官（主线），发版 v6.0.2（Sprint 18、19 一起，PO 定）**：Sprint Goal「看得见」达成（PBI-35、61）。看板第 1 版：scrum-kernel 的 `conventions/board.md`（16 条，兼给子代理的简报）与 `board-template.html`，单文件网页，产品卡、冲刺卡、设计卡，只读日志、不存状态，生成物 `scrum/Board.html` 不提交，由便宜的模型照约定生成；形式由 Master 定为网页（PO 交给 Master），块的顺序照 PO 的卡片设计。hook：`hooks/hooks.json` 与 POSIX sh 的 `commitments.sh`，开会话、恢复、压缩后各注一次承诺原文，承诺变了的那一轮再注（频率测试选 A4；不装 hook 也过线，约定是主力、hook 补位），`IDEO_SCRUM_COMMITMENTS=off` 可关；`.gitattributes` 让脚本保 LF；Codex 包同步 `hooks/`（用户要先在 `/hooks` 里信任）。已知限制四条进 PBI-68、62。PO 看过真实看板：「作为第1版来说，我觉得还不错」，要强审照他的品味重做，登记 PBI-68，开 Sprint 20。日志归档 `scrum/documents/sprint-19-board-hook.md`；tag `sprint-19-board-hook`、`v6.0.2`；main、tag 都还没推送。
- **2026-11-13 · Sprint 18 收官（副线），版本不动，仍 6.0.0**：Sprint Goal「规矩先顺」达成（PBI-66、65、60）。和主线 Sprint 19（看板、hook）同日并行：一个 Master 管两条线，两个 Developer 各在一个原生 worktree。PO 2026-11-13 全部放权：精化、关卡、放行都由 Master，改 Product Goal、推送、取消冲刺、推翻 PO 说过的话仍回 PO。增量：日志头部统一——承诺小表留在原节，格式只在 overview 第 17 条写定；冲刺、设计、IDEO 日志头部有 Now 加 Waiting for PO；工作块完成标 ✓；阶段决定前引用目标原文。scrum、sprint、design 三个内核召唤才来（角色命令、点名、建改插件日志三种），ideo 放开；Master 改成书面授权内代行，PO 助手身份写清，secretary 清零。测试用 magpie 的便宜模型（非 Haiku）：A 从 9/9 误加载降到 0/9，B 8/9（6 次超时照冻结原文技术补跑），D 过，C 3/9 没过，记成已知缺口 PBI-67（PO 定）；白纸项目的直接路径不再自动进设计冲刺，是 65 有意的结果。熟手卡 Review 后，README 改成照实写。日志归档 `scrum/documents/sprint-18-rules-first.md`；tag `sprint-18-rules-first`；main、tag 都还没推送。
- **2026-11-13 · Sprint 17 收官，发版 v6.0.0（Sprint 16、17 一起）**：Sprint Goal「约定改顺」达成（PBI-54、58、56、53、52，连同 46 ③）；题 9、题 10 的必答 ② 记成已知缺口，登记 PBI-59。PO 2026-11-12 把 Sprint 16、17 全权交给 Master：停点 ② PO 读审阅稿，说「OK，相当好」，并追加 IDEO 日志与模板，又要求补架构、写清五模式和设计冲刺的关系（「不能乱」）；停点 ③ PO 2026-11-13 取消，改为收官后自己看。增量：冲刺模板加 Now 行，写明什么算卡住、怎么判过时、照抄 2.1 时查够不够；设计目标写愿景，地图要粗，主线程陪 PO 聊（design-log 新第 12 条），草图简报不给现状；sprint-log 第 26 条写 Developer 在另一个会话或工具里时怎么协作；ideo-kernel 新开 `conventions/`——`ideo-log.md`（分界、关系、IDEO 日志、放哪与结束）和 IDEO 日志模板（`IdeoBacklog.md`，五章不分节）；overview 的图加分界节点；三份描述写明「IDEO 五阶段法」就是五模式。测试：两轮各 42 次。第 1 轮 9/14，题 10 三份都把五阶段法当成了设计冲刺；改描述后第 2 轮 10/14，行为栏没有一题退步，白纸题两条路径都过（PBI-52 结项），题 10 的内容三份都对。Review 时熟手、陌生人两张卡看过增量，陌生人的意见进 PBI-30。收官前查出第 2 轮的两份描述超过 1024 字符（ideo 1130、design 1191），压回 1013、1018；全新子代理审过，又跑了 15 次触发测试（题 3、4、9、10、11 直接路径），行为栏对第 2 轮没有退步。收官时 main 上多了别的会话的 `e810e43`（CLAUDE.md），已先合进冲刺分支。冲刺日志归档 `scrum/documents/sprint-17-conventions-rewrite.md`；tag `sprint-17-conventions-rewrite`、`v6.0.0`。按 PO 的安排，main、tag（连同 Sprint 16 的）和 SeaPawn-Memory 都还没推送，本机插件也还没更新，交 PO 的辅助会话做。
- 更早的状态（2026-08-31 至 11-12：#28 讨论定案各条、Sprint 07 收官、Sprint 08 撤销与产品日志精化出架构 v1、Sprint 08 收官发版 v5.0.0、Sprint 09 收官发版 v5.0.1、Sprint 10 收官发版 v5.1.0：流程全部进插件、Sprint 11 收官发版 v5.1.1：约定照 PO 审阅改定、Sprint 12 收官发版 v5.1.2：overview 挪到 scrum-kernel 根目录、Sprint 14 收官发版 v5.2.0：约定精调、Sprint 15 收官：反馈落地，PBI-55、Sprint 16 收官：四个内核、按需加载，PBI-44、57）见 `git log -p -- CLAUDE.md`；教训已蒸馏入记忆档 sprint-06-dual-kernel-refactor、sprint-07-roles-kernels。
- **1.x 已收官蒸馏**：旧目标（两内核结构对等）判定方向性错误，勿延续；教训见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（MEMORY.md 索引 + 五期档案）。

## 维护规约

**README 是文件索引与当前状态，Git 历史负责追溯过去。**

- README 面向外部读者：只陈述这里是什么、文件地图、来源授权；作者侧的当前状态不入 README——由本文件「当前状态」锚点与 `scrum/ProductBacklog.md`（产品日志）承担
- 提交前确认 README 是否需要同步更新——尤其是新增/删除/重命名文件、改动插件版本号时
- 若发现 README 已过期、可能误导新会话的 LLM，必须显式提醒用户更新，不要默默放过
- 追溯旧决策、文件演变、阶段状态时，放手查阅 Git 历史
- 多会话并行时，会话开头的 CLAUDE.md 只是快照：动手前先看 `git log --oneline -5` 和磁盘上的产品日志，差一个冲刺就按磁盘来；子代理核对现状时给路径让它读文件（2026-11-13：开头停在 Sprint 15，磁盘已是 16 收官、17 在 worktree）

**版本号与 tag**

- 主干分支是 `main`，永远指向最新状态
- 版本号用 tag 标记，不写进分支名
- 插件版本号在 `plugins/ideo-scrum/.claude-plugin/plugin.json`，改动时 README 的两处版本号需同步（首行与文件地图的插件清单行；归档行里的旧版本号不动）
- **Codex 包随版本一起提交**（PO 2026-11-09：版本与 Claude 一致）：改了 `plugins/ideo-scrum/` 或版本号，同一提交里跑 `python scripts/sync_codex.py`，再跑 `python scripts/check_codex.py`（需要 PyYAML）；Codex 清单的版本由脚本取自 Claude 清单，包内 README 的版本由清单生成。（Sprint 13：旧 `codex` 分支靠手工同步，落后六次发版。）
- Windows 上 `core.autocrlf=true` 时，新克隆后第一次跑同步，会把生成的 JSON/YAML 的换行从 CRLF 改成 LF，内容与已提交的一样：看 `git diff`，或 `git add -A` 后有没有暂存，别只看 `git status` 的 M。

**组件描述（attribute description）规约**

写插件组件（skill / command）的 `description` 时：它是**触发条件**，不是自我介绍——用 "Use when..." + 具体场景词；同类组件描述必须有区分度（模板趋同 = embedding 空间互相叠影，系统无法选择）。plugin.json 的 description 是元数据（展示用），非触发主战场。（来源：Sprint 04。）角色命令可以在触发句之后追加一两句边界和相互关系（替谁做事、不做什么、谁召唤谁），让各角色在技能清单里互相知道；触发句保持在最前（2026-10-13，#14）。scrum、sprint、design 三个内核只在召唤时加载：角色命令叫它加载、用户点名插件或内核、或者要建改本插件的日志；泛问通用词不加载，不再靠「与常见版本不同、先加载再答」强拉触发（PO 2026-11-13 改方向，替换 Sprint 08 的强触发规约）。触发不足时，写明「什么情况下先加载」，不要只堆关键词（2026-10-25，PBI-22：ideo-kernel 的触发由 1/10 升到 5/5）。 描述可以改，改了就重跑触发测试，结果不能比改前差（PO 2026-11-08）。Scrum 的通用词（如 Product Backlog、Sprint Backlog）不再单凭出现就触发三个受控内核；描述要列清三种召唤，ideo-kernel 则对发散、定义问题、原型、用户研究与测试放开；回归照新边界比行为，负向题的少触发才是改进（PO 2026-11-13 改方向，替换 Sprint 10 的强触发规约）。 改触发边界时，「何时来」和「来了先做什么」分开写：给受控内核删强触发句时，开放的 ideo 要留着「先加载再答」（Sprint 18：一并删掉，C 组从 3/9 掉到 0/9，加回后回到 3/9）；光靠描述，够不到没有领域词的「发散」「定义问题」这类说法（PBI-67）。

**模板规约**（2026-11-08，Sprint 09 Retro）

模板的章按流程分，节只放产出；做法写在约定里，不在模板里一步开一节。交付新模板或新结构时，验收前把结构（章节清单）单独摆给 PO 看，不混在整份审阅里。（Sprint 08 的设计日志模板照当时产品日志模板里的活动表每个活动各开一节，把做法写成了要记的东西；验收时没单独看结构，PO 第二天才发现。）约定的条同理按执行顺序排，被依赖的排前面（Sprint 14 样板测试：定分支排在填表头之后，模型照条号走，先填了表头）。

**冲刺收官与归档**（2026-11-07 改，原「冲刺蒸馏闭环」；2026-11-10 Sprint 14 改成新结构；Sprint 01–07 按旧做法蒸馏为记忆档，不回改）

- **Review 和 Retro 是收官时的动作，日志里不设章**（PO 2026-11-10，Sprint 14；新结构从 Sprint 15 起生效，Sprint 14 自己的日志仍按 5.1.2 写，有第 4 章 Review）。Review：备料（Master 兼 Developer 时，对抗审查交全新子代理，只核对做得对不对；另照产品日志 2.1 召唤角色卡看增量，回答好不好用——2026-11-08）→ 冲刺日志压缩成关键决定 → 改名为冲刺文件夹名（`sprint-NN-后缀.md`）移进 `scrum/documents/` → 删除冲刺目录里其余的中间文件 → 更新产品日志并保鲜（做完的 PBI 移入 3.2 并引用该文件，删掉过时内容；没做完的回 3.1；利益相关者的看法和 Product Goal 的变化写进产品日志）→ 整个 `scrum/` 过一遍，`documents/` 里过时的删掉（2026-11-09 改顺序：先写完再删中间文件）。已经结束、还在自己文件夹里的设计，它的日志同样压缩、改名 `design-后缀.md` 移进 `scrum/documents/`。
- **Retro**：教训写进记忆（`S:\SeaPawn-Memory\memory\IDEO-Scrum\`，路径以 `.claude/settings.json` 的 `autoMemoryDirectory` 为准）或本文件；写原则、不写故事；特别好的改进经 PO 同意写进 DoD。冲刺日志不设 Retro 章；设计不单做 Retro，设计结束时记在设计日志第 5 章末尾的一两句做法教训，由归档那份日志的冲刺的 Retro 整理。
- **收官**：项目健康看 `scrum/` 就够，其余一般只需同步 README；Review 与 Retro 只出一个提交；tag 与冲刺文件夹同名（同名分支随即删除）；合入 main，关分支与 worktree。

> 分工：**memory 管教训**（见 `S:\SeaPawn-Memory\memory\IDEO-Scrum\MEMORY.md`），**`scrum/documents/` 管冲刺与设计原文**（压缩后的冲刺日志与设计日志），**git 管全部历史**，**`scrum/` 其余部分管现状**（产品日志、当期冲刺与设计）。完整流程见插件 sprint-kernel 的 `conventions/sprint-log.md`。

**Sprint 节律**（2026-10-24，Sprint 06 Retro；2026-11-07 改）

- **按 Sprint Goal 收官**（2026-11-07 改，原「按时间盒收官」）：Sprint Goal 达成或 PO 叫停时收官，做 Review + Retro（单提交）；冲刺日志不写截止日（AI 按会话工作，日期没有意义；与官方定长不同，理由见插件 sprint-kernel 的 `conventions/sprint-log.md` 的 No end date）；期间发版照常，记进当期日志，不结束 Sprint；之后的新工作开新 Sprint、新日志；日志当日记，不事后补录。
- **没做完的回产品日志**：收官时没做完的 PBI 回产品日志，不顺延。（原「时间盒写在日志头」，2026-11-07 删去截止日。）
- **计划外工作先登记**：作者待办或对话中定下的新工作，先在产品日志登记 PBI，再由 PO 定是否进当前 Sprint（范围可重谈，Sprint Goal 不变）；不进则等下个 Sprint。
- **小活单开小冲刺**（PO 2026-11-08，Sprint 09）：半小时到一个会话做得完的活也开冲刺，正常流程照走，每一步缩到一两行；放行、审阅、收官照做（插件 sprint-kernel 的 `conventions/sprint-log.md` 的 Small work, small Sprint）。
- **fork 出来的 Developer**（2026-11-08，Sprint 09、10；2026-11-10 Sprint 14 补）：有两种 fork，别混。① Agent 工具派出的 fork 子代理（Sprint 09、10）：它是主会话的子代理，主会话一进 plan 模式，它就停下、写不了文件，Developer 干活时主会话别切 plan 模式；它不能再派子代理，审阅、插件校验、角色召唤都由 Master 派。② `/fork` 复制出的会话（Sprint 14）：它是独立会话，能派子代理，不受主会话 plan 模式影响；Master 与它用跨会话消息直接通讯，不经 PO 转，长的审阅写在 plan 文件里、消息里给路径。两种都带着 Master 的上下文，但活是 Developer 干的：审阅照常由 Master 做，也可以派全新子代理（PO 2026-11-09，插件 sprint-log 的 A reviewer is required；Sprint 12 起生效）。Master 自己兼 Developer 时，审阅仍交全新子代理。派子代理一律显式写 `model`（Haiku），见用户级 CLAUDE.md（Sprint 14：四次 plugin-validator 没写 model，继承了主会话的 Sonnet，每次约 22 到 27 万 token）。
- **worktree**：用原生方式建（`.claude/worktrees/`），不裸跑 `git worktree add`；根目录 `.worktreeinclude` 决定带过去的文件。
- **两条线并行**（2026-11-13，Sprint 18、19）：一个 Master 管两个冲刺，两个 Developer 各在一个原生 worktree；按「改已有内核」和「加新东西」分线，撞文件的地方就少。两条线共用的接口（如日志头部格式）由改约定的那条线先交，Master 审过当天转给另一条；后收官的那条先把 main 合进来。
- **PO 全部放权时**（2026-11-13）：PO 的原话逐字记进每份日志的第 4 章，并写明仍回 PO 的事——改 Product Goal、推送发布、取消冲刺、推翻 PO 说过的话、PO 点名要亲自看的口味（如看板形式）。这时等的是 Master：Now 写「等 Master」，Waiting for PO 写 None（Sprint 18 熟手 Review：只写 None，看不出在等谁）。
- **审阅看分支 diff**（Sprint 18）：改的是已有文件、又在分支上没合入时，直接审提交的 diff，不另写审阅稿；sprint-log 第 12 条「先审后改源文件」在分支上就做到了。
- **CLAUDE.md 由有直接授权的会话改**（Sprint 18）：别的会话凭跨会话消息不能改 CLAUDE.md（宿主规则，不是 Developer 不配合）；要么 PO 在那个会话里直接点头，要么收官时由 Master 在 PO 的会话里改。
- **Developer 在别的工具里（Codex，Sprint 13）**：通道只有冲刺日志；两边共用一个工作目录，轮流动手：每轮提交、在 3.2 记一行并在 Next 写明轮到谁，然后停下；PO 只传一句「轮到你了，读冲刺日志」。Master 的审阅意见写在 plan 文件里，PO 把路径转给 Developer，由它抄进日志（日志才是记录）。放行要写明能做到哪一步：Codex 在 `approval_policy = never`、完全访问下，能自己推送、打 tag、改本机配置。停点要少：把彼此独立的活一次做完再交审，PO 的传话和等待是主要耗时。
- **约定大约每周集中改一次**（PO 2026-11-09，原插件总览的一条约定；那是作者维护插件的节奏，不是用户的规矩，挪到这里，Sprint 14 强审时 PO 又把插件里的那条删了）：平时记下约定不合适的地方，攒着集中改，登记成 PBI、开冲刺改；改动从下一个冲刺起生效，冲刺进行中不改。约定不带版本标记，PBI 标题也不带版本号（PO 2026-11-10：以后更新都是重构，不要版本这种标志）；PBI-54（产品日志与冲刺）、PBI-58（设计）已在 Sprint 17 做完（2026-11-13）；下一次集中修订，等新的意见攒够了再登记。
- **PBI 状态只写产品日志**：SprintBacklog 引用 PBI 编号，不复写状态；进展写在 3.2 笔记。
- **工作区留着别的改动时，`git add` 逐个写文件**，不按目录加（2026-11-08，Sprint 08 误带过一次，撤回重提）。
- **迁移类改动全仓 grep**：路径、位置、名称迁移时，同一提交内全仓 grep 旧值至零残留（README、CLAUDE.md、日志都算）。
- **改规矩先找它的其他说法**（2026-11-09，Sprint 11 Retro）：一条规矩改了，精化时就全仓 grep 它在模板、命令、两份 SKILL.md、CLAUDE.md 里的其他说法，列成连带改动一起改（Sprint 11 一处审阅意见牵出五组连带改动；删一条带编号的约定要改号，用脚本把每处「convention N」对到短名；Sprint 14：内容改动与改号分开提交，改号后把引用换成短名、去掉条号，改号前后逐行相同才算对，三次改号都是 0 错；脚本只保证引用的条存在，不保证指得对，要逐处读所指的条是不是真有那句话，product-log 17 曾误指向 overview 5；对抗审查的七处必改，多数是同一条规矩在别处的另一种说法）。
- **对着译文审阅，先分清改哪边**（2026-11-09，Sprint 11 Retro）：PO 对着中文译文提的意见，逐条先判是英文原文的问题还是译文的措辞；只是译文的，英文不动，在审阅记录里写明（Sprint 11：overview 第 2 处后半）。
- **大改约定的审阅顺序**（2026-11-10，Sprint 14 Retro）：Developer 起草 → Master 审 → 对抗审查（全新子代理，只核对做得对不对）→ PO 强审 → 最后一轮流程测试 → 收官。对抗审查放在 PO 强审之前，先清掉重复、错指和前后矛盾（Sprint 14：七处必改），PO 的强审才用在方向和口味上（两批共五处）；插件文字改了，流程测试整轮重跑，所以会改文字的审阅都排在最后一轮测试之前，PO 的意见攒齐了再跑（Sprint 14 跑了四轮）。

**插件验证**

Claude 插件无 build/test；Codex 包由 `scripts/sync_codex.py` 生成、`scripts/check_codex.py` 核对（内容与源逐字相同、链接、导航、可重复生成）。改动插件后：官方命令能做的先用命令，不派子代理（PO 2026-11-10）——收官改完版本号后跑一次 `claude plugin validate --strict plugins/ideo-scrum`；只改了文字、结构没变时，它没报问题就够了；它报问题，或改了结构、清单、frontmatter，才派 Agent 类型 `plugin-dev:plugin-validator`，并显式写 `model`（Haiku）。涉及 skill 质量时用 `plugin-dev:skill-reviewer`（两者经 Agent 工具调用，非 slash command）。marketplace 清单在 `.claude-plugin/marketplace.json`（Sprint 16 补了顶层 description，`--strict` 现在通过，PBI-25 ⑧）。 插件带 hook（Sprint 19 起）：声明用 shell 形式 `sh "${CLAUDE_PLUGIN_ROOT}/hooks/<脚本>"; exit 0`，不靠可执行位；`.gitattributes` 让 `*.sh` 保 LF；MSYS 的 awk 自己吃掉 ``、Linux 的不吃，去 CR 要在 Linux（WSL）里测；脚本别用 `find`（Windows 自带同名的 `find.exe`）；改了 `hooks/` 是结构变化，跑完 `--strict` 再派 plugin-validator。

**回归测试**（2026-10-25，Sprint 07 Retro）

- 判定标准先写、单独提交，再跑；出结果后不改标准。
- 用便宜的模型跑（PO 2026-11-08）。要另起 Claude CLI 时用 `claude-magpie`（用户级规矩，2026-11-13）：它把 `--model` 固定映射到 magpie 自己的便宜模型，写什么都一样，不是 Haiku；汇总标「magpie 的便宜模型，非 Haiku」，不写模型名和提供方。
- 脚本按关键词判断大纲顺序会误判；判错的逐条人工看，改判写明理由，验收时摆给 PO（2026-11-08）。
- 触发测两条路径：从角色命令进入，和直接说。
- 比较描述效果，同日同环境对照，带改前基线。
- 无头测法（Sprint 18、19 定）：`claude-magpie.cmd -p --plugin-dir <插件 Windows 路径>`（Git Bash 里要带 `.cmd`）。子进程环境用白名单，不从宿主逐个删：宿主除了认证和网关，还注入模型重映射与模型目录（Sprint 18：`haiku` 被解析成宿主的模型名，上游 502）、AUTO_COMPACT_WINDOW、跨会话消息的套接字与令牌、会话编号。只带 SystemRoot、PATH、USERPROFILE、APPDATA、LOCALAPPDATA、HOMEDRIVE、HOMEPATH、ComSpec、PATHEXT，再设 TEMP、TMP（每次全新的空目录）、CLAUDE_CODE_GIT_BASH_PATH、MSYS_NO_PATHCONV；额外的开关只用 `--env` 明着给。magpie 默认 bypassPermissions，`--allowedTools` 只是免询问、限不住工具：用 `--tools Read,Grep,Glob,Skill` 限工具，`--disallowedTools` 另禁 Bash、PowerShell、Write、Edit、Agent，`--strict-mcp-config` 去掉 MCP；加 `--permission-mode dontAsk` 也不够，用户 settings 里宽泛的 allow 规则照样放行，要再加 `--setting-sources project,local` 把用户 settings 挡在外面，白名单才真生效（Sprint 19）；冒烟时核 init 里的实际工具和模型（只比布尔，不记值）。比对技能名时去掉 `ideo-scrum:` 前缀；同一轮只用一条通道；路径用 `cygpath -w`；`--resume` 会让 SessionStart 每轮都触发，要测会话里的行为，就在同一进程里用 `--input-format stream-json` 一条一条发，等上一条的 result 再发下一条（一次发多条会并成一轮；`/compact` 也能这样发）；核对 hook 用 `--include-hook-events` 的流，不靠模型复述。查变量只列名字，不打印值。
- Windows 上超时要杀整棵进程树（`taskkill /T /F`）：只杀 cmd，CLI 会接着跑，写出迟到的答案。API 自动重试能拖过超时，超时不等于模型没调用：看重试事件和 API 耗时。技术失败照冻结的标准补齐有效试次，不挑样本，迟到的答案不算（Sprint 18：B 组 6 次超时，修好后补跑 6/6）。
- 验证用的子进程先核对它真的被限制了：看 init 事件的 `permissionMode`，也看 `permission_denials` 出没出现过——一次都没有，多半是限制没生效，不是模型守规矩（Sprint 19）。
- 量 token 要成对比：文档 MCP 开场连没连上，同一个提示的输入就差约 1300 token；两个臂拿连接状态相同的一对来减（Sprint 19）。
- 选定规则要把限定词写全：「选最省的过线臂」要写成「在带 SessionStart 的过线臂里」，字面读会选出一个自己没过线的配置；判「过期」看明细，模型可能是发现了不一致、照日志做了对的决定（Sprint 19）。
- 检查脚本独立读日志时，路径锚在顶层（后缀匹配会把测试夹具里的假日志当成开着的），别假定编号写法（Sprint 18 的工作块是 `H1`）；夹具放真仓库才有的形状，并先拿真仓库的状态过一遍（Sprint 19）。
- 便宜的模型逐字抄长文会丢字（地图里丢一个 `-`、删掉 `<br/>`）：逐字的规矩要配核对；权限放宽时模型自己写脚本拷贝就不丢，收紧时只能手抄（Sprint 19）。
- 工具审查员（skill-reviewer 等）的必改项，落盘前先对一遍 PO 的定案和约定原文；冲突就报 Master，不照改。（Sprint 18：审查员要把 stakeholder 的「never the builder」改回旧说法，与 sprint-log 第 17 条原文冲突，没采纳。）
- 测试记录先写结论（过没过、缺口在哪），细节和编号放后面（Sprint 18 熟手 Review：结论埋在近万字里）。
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
- 描述有 1024 字符上限（Agent Skills 规范，plugin-validator 会报，Codex 也照它）；Claude Code 技能清单每条显示到 1536，但以 1024 为准。现在最长的是 ideo-kernel，1023 字符（Sprint 18），已经顶线；改描述时先量长度（Sprint 16；Sprint 17 第 2 轮一度超到 1191，收官前压回）。

## 源材料与授权

插件内所有第三方摘录必须带署名。新增摘录时：

1. 文件顶部标注 `> Source:` 与 `> License:` 两行，License 须与 [ATTRIBUTION.md](ATTRIBUTION.md) 中记录的条款一致
2. 若引入新来源，先在 ATTRIBUTION.md 中登记，再写摘录

> 例外：命令类组件（`commands/*.md`）的抄录主体不设文件头两行；其署名义务由 ATTRIBUTION.md 的登记承担。

**原文优先**（PO 2026-11-07）：写方法流程时能用原文就用原文；原书例图改画成 Mermaid（flowchart TD）或写成文字，不放图片文件（PO 2026-11-08）；不是原文的写法写进 `conventions/`，标为约定建议。删减的标准：和人机协作无关的删去（日程、周几、零食与休息、白板与用品、线下投票这类；PO 2026-11-08）。只删不改的摘录用脚本按行号从原书取；删完查一遍悬空的句子：指向已删图片的引导句（like this:）、指向原书其他章的句子、没了指代的句子（2026-11-08，Sprint 08 对抗审查查出十几处）。 引文以插件里带的原文为准：SGEP 以 `assets/` 里的 v2026.1 为准，references/ 里的句子先核对原文再引；`assets/` 里只有 v2026.1 除 Artifacts、Events 两章以外的部分，这两章在 `references/`、`sprint-kernel/events/` 与两份 SKILL.md 里（Sprint 10 曾记两章来自 2025.6，是误判；Sprint 16 拿 v2026.1 全文核过，见 PBI-25 ⑥）。

**已知的授权约束：**

- Scrum Guide 2020 / SGEP —— CC BY-SA 4.0，可摘录、可商用
- Stanford d.school Bootleg —— CC BY-**NC**-SA 4.0，含非商业限制
- 《Sprint》(Knapp) —— 全版权；版权由 PO 负责，发布前声明（PO 2026-11-07）。写流程原文优先、例图改画成 Mermaid 或文字（见上）

根目录的 `references/` 是源材料原件，**不入库**（`.gitignore` 已拦截），仅存于作者本地；插件里 `skills/*/references/` 的工件摘录照常入库。

## 插件内容的自足性

插件会运行在别人的 Claude Code 或 Codex 里，那里没有本仓库的上下文，也没有作者的全局配置。

**写插件内容时，不要依赖任何未在插件内言明的约定。** 例如「用 mermaid 画图」必须同时说明方向（`flowchart TD`），否则在他人环境中行为不一致。引用别的技能的文件写 `../<kernel>/file.md`，不裸写文件名：裸文件名只在同一技能里解析得到（模板里用文字定位；Sprint 16）。
