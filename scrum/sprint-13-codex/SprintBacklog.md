# Sprint Backlog — Sprint 13 (codex)

> Started: 2026-11-09 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-13-codex` | Product Owner: SeaPawn | Scrum Master: Claude（Claude Code 主会话）| Developer: Codex（GPT，在 Codex 里跑）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).

## 1. Why

### 1.1 Sprint Goal

<!-- The Product Owner decides it: this Sprint's one commitment (sprint-log.md, convention 3). -->

**Codex 版跟上**：Codex 里的 IDEO-Scrum 与 Claude Code 版一致——三个内核、四个角色、约定与模板都在；以后发版能照样同步；在 Codex 里开 Developer，装上就能照约定干活。

### 1.2 Definition of Done

<!-- The Product Owner picks them: the Definition of Done items that matter to this Sprint (product-log.md, convention 5). -->

Output Done 三条：内容忠实、可导航、无死链（产品日志 1.3），用在 Codex 包上。Claude 侧的描述不动，不跑 Claude 的触发测试。

## 2. What

### 2.1 Product Backlog Items

<!-- The Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little. The selected items, copied word for word from the product log (sprint-log.md, convention 5). -->

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-43 | Codex 版——与 Claude Code 版一致 | 作为熟手，我想要 Codex 里装上的 IDEO-Scrum 与 Claude Code 版一致（三个内核、四个角色、约定与模板），以便在 Codex 里开的 Developer 也照同一套约定干活，和 Claude Code 里的 Master 靠冲刺日志协作 | Map ①（装插件，开会话） | M |

### 2.2 Refinement

<!-- The Scrum Master leads. What refinement settled, each point with who decided it; the acceptance criteria; the tests' method and pass lines (sprint-log.md, conventions 6 and 15). -->

**PO 定（2026-11-09）**
- 只选 PBI-43；Sprint Goal 如 1.1。
- Codex 版并入 main，不再单靠 codex 分支；前提是不影响 Claude Code 的使用。
- 本冲刺算在当前 Product Goal 之内（产品日志 1.2）。
- Developer 在 Codex 里跑（GPT），和 Master 只靠本日志通讯，PO 传话。
- Codex 里装着的旧版 ideo-scrum（3.2.0）不停用，Developer 可以用它进角色；收官时换成新版。

**怎么协作**（Master 定，PO 可改）
- 通道只有本日志。两边都在 `S:\IDEO-Scrum`、分支 `sprint-13-codex` 上干活，所以轮流：同一时间只有一方动仓库；动手前先读本日志的最新版。
- 分工照模板注释：Master 写 2.2 和审阅结果；Developer 写 3.1、3.2；PO 的放行写在 3.1 最后一行。
- 每轮做完：在冲刺分支提交，在 3.2 记一行，「Next」写明轮到谁、要对方做什么，然后停下。
- PO 传话只说一句：「轮到你了，读 `scrum/sprint-13-codex/SprintBacklog.md`。」
- 拿不准的事写进「Next」问 PO（overview 约定 9），停下等。

**Developer 先读**（以仓库里 5.1.2 的文件为准）
- 角色：`plugins/ideo-scrum/commands/developer.md`。文中「用 Skill 工具加载内核」，在 Codex 里改成直接读下面的 SKILL.md。
- 内核与约定：`plugins/ideo-scrum/skills/ideo-kernel/SKILL.md`、`skills/scrum-kernel/SKILL.md`、`skills/scrum-kernel/overview.md`、`skills/scrum-kernel/conventions/sprint-log.md`。
- 项目规矩：仓库根 `CLAUDE.md`。其中 plugin-validator、skill-reviewer、`reclaude`、Haiku 回归测试是 Claude Code 这边的工具，归 Master；Developer 用 Codex 自己的办法测。
- 旧版 `$developer`（3.2.0）和上面的文件说法不同时，照上面的文件。
- 上次同步（3.2.0）的做法在 codex 分支 `d307296`，可参考，不必照做。

**验收标准**
1. 内容一致：Codex 包里有三个内核（ideo、scrum、design）的全部文件和四个角色 skill。内核文件与 `plugins/ideo-scrum/skills/` 逐字相同；角色 skill 正文与 `plugins/ideo-scrum/commands/*.md` 相同。改动只限工具说法，逐条列在 3.2。
2. Claude Code 不受影响：Claude 侧装上后，技能与命令清单和 5.1.2 一样，plugin-validator 通过；`plugins/ideo-scrum/` 与 `.claude-plugin/marketplace.json` 没改动时视为满足（Master 核对）。
3. 同步能重跑：一条命令从 `plugins/ideo-scrum/` 生成 Codex 包；没有改动时重跑，`git status` 是干净的。
4. Codex 里能用：装上新版后，四个角色都能调用；给 `$developer` 一个开冲刺的任务，它读到 `conventions/sprint-log.md`。
5. 无死链：Codex 包里 markdown 的内部链接都能解析。
6. README 同步：Codex 的安装说明（不再要 `--ref codex`）和版本号（CLAUDE.md「维护规约」）。

**测试**（方法和过线标准先提交、后跑，跑完不改；sprint-log 约定 15）
- 1、3、5 用脚本核对。过线：0 处不一致（3.2 列出的工具说法除外）；重跑 0 改动；0 死链。
- 4 由 Developer 在 Codex 里用便宜的模型跑：四个角色各一题，再给 `$developer` 一题开冲刺；题目不带引导词（CLAUDE.md「回归测试」）。题目和模型先写进 3.1，Master 审过再跑。测的时候不动 PO 正在用的 Codex 安装。过线：角色 4/4 能调用，`$developer` 读到 `sprint-log.md`。
- 2 由 Master 核对。

**留给 How 的开放点**（Developer 在 3.1 提方案）
- Codex 包放在哪个目录；整份镜像，还是和 Claude 版共用一份源文件（以验收 2 为前提）。
- 哪些工具说法要改、怎么改：Skill 工具、`ideo-scrum:` 前缀、subagent 等。

**收官时再定**
- 版本号与发布；codex 分支怎么退役（推送前问 PO）。
- 本机 Codex 换装新版。
- Master 提醒 PO 核对 Product Goal（产品日志 1.2）。

**最后一步**：Developer 读完，先在 3.2 记一行，逐条复述验收标准、列出不清楚的地方；没有问题再写 3.1。

## 3. How

### 3.1 How

<!-- The Developer writes it (sprint-log.md, convention 7). The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 生成 Codex 分发包（一个会话以内） | `scripts/sync_codex.py`、`codex/plugins/ideo-scrum/`、`.agents/plugins/marketplace.json` | `python scripts/sync_codex.py` 生成三个内核及四角色；仅有 3.2 登记的工具适配；Claude 源目录和 marketplace 不变 |
| 2 | 静态验收（一个会话以内） | 内容、文件集合、链接、重跑检查脚本与结果 | 六项验收中的 1、3、5 过线：0 未登记差异、0 死链；重跑不产生改动；包内入口两跳可达各 reference |
| 3 | 隔离安装与五题验证（一个会话以内） | 新版临时安装、五份 JSONL 与逐题判定 | 四角色 4/4 可调用；开冲刺题实际读到新版 `conventions/sprint-log.md`；PO 的安装未改 |
| 4 | README 跟上（一个会话以内） | 根 README 的 Codex 安装、角色调用、包与同步命令索引；包内必要说明与署名文件 | 文案先在本日志给 Master 全文审，认可后落盘；默认分支安装无需 `--ref codex`；版本与源清单一致，若收官改版本再同步 |
| 5 | 交审与修正（一个会话以内） | 本节逐项 DoD、六项验收证据及改动摘要 | Master 核对 Claude 侧不受影响并审增量；缺项按日志反馈修正，之后交 Master 主持 Review 与收官 |

**Key choices**

- **目录与来源**：沿用旧包的 `codex/plugins/ideo-scrum/` 作为独立生成物，与 Claude 包共存于 main；`.agents/plugins/marketplace.json` 只指向 Codex 包。Claude 的 `plugins/ideo-scrum/` 和 `.claude-plugin/marketplace.json` 保持原样。单独镜像能适配工具用语，也便于脱离仓库安装。
- **一条同步命令**：`python scripts/sync_codex.py`。三个内核完整复制；四个角色由 `commands/*.md` 生成原生 skill：增加 `name`，保留 description 和正文，只套用 3.2 的明确替换；角色 `agents/openai.yaml` 保持显式调用，内核保留自动触发。包清单沿用已安装版可用的 `.codex-plugin/plugin.json` 格式，版本、作者等取 Claude 清单；包内带根 `LICENSE`、`ATTRIBUTION.md`。生成物无时间戳，旧的受管文件随源删除，手改生成物会被校验指出。
- **工具适配**：不全局替换 `ideo-scrum:` 或 `subagent`。加载内核的具体工具句改为直接读取相邻内核的 `SKILL.md`，顺序及跳过已读内核的规则不变；subagent 仍指独立子代理，保留职责与独立性要求。逐处清单见 3.2。
- **检查办法**：脚本分别核对源/包的完整文件集合与内容、角色 frontmatter/正文、manifest 和角色元数据；允许差异按 3.2 清单逐处还原后比较，未登记差异一律报错。链接检查覆盖行内与引用式本地链接、文件和锚点，包外目标算失败；不对网络链接发请求。重跑检查在已提交的干净副本运行同步命令两次，两次后 `git status --porcelain` 都须为空。检查脚本先用一份正确样本及人为缺文件、坏链接、改正文的样本自测，再检查包；这些样本放临时目录。
- **隔离与证据**：五题各开全新 `codex exec` 进程，使用临时项目和仅传给子进程的独立 Codex 用户目录、关闭共享 daemon；通过本机 `codex plugin marketplace add <临时根目录>`、`codex plugin add ideo-scrum@ideo-scrum` 安装生成包。测试目录中有最小产品日志、既有冲刺记录及「陌生人」角色卡，供题目自然使用；不附仓库的全局记忆、CLAUDE.md、测试答案或加载提示。不向当前 `~/.codex` 写插件/配置，不升级旧插件；若认证或环境阻止运行，把原始错误写进 3.2 交 Master，不能算通过。
- **测法依据**：已核对本机 `codex-cli 0.167.0` 的 `exec`、`plugin add`、`plugin marketplace add` 帮助，以及 [OpenAI 插件打包文档](https://developers.openai.com/plugins/build/plugins)。临时项目及安装细节在施工时验证；不会把本轮查 help 当作验收结果。
- **对外文字先审（Master 必改 ①）**：README、Codex 包清单 `interface` 的 displayName、shortDescription、longDescription、defaultPrompt，以及四份 `agents/openai.yaml` 的 display_name、short_description、default_prompt，全文写入 3.2，Master 审过再生成到交付文件。项 1–3 先生成无展示 `interface` 的最小 manifest、只含显式调用 policy 的角色 openai.yaml，测试技能加载与方法论行为；展示文字审批后补齐，并重做静态核对。
- **临时凭据（Master 必改 ②）**：隔离子进程只带当前模型提供方必需的设置与登录凭据，凭据只写系统临时目录；不复制插件、marketplace、hooks、MCP 等用户设置。用完立即删除临时凭据，异常退出也清理；不改当前用户目录。所有原始输出进仓库或提交前，按实际凭据值及密钥/令牌形态检查，有命中先处理，不提交秘密。
- **本轮停点（采纳 Master 建议）**：项 1–3 和全部对外文字草稿完成后，在 3.2 交证据及全文，提交并停下；Master 审过，再落盘对外文字和改审阅问题。收官时由 Master 将「发版前跑同步命令，Codex 包和版本号一起提交」写进 CLAUDE.md，本轮 Developer 不代办。

**五题与模型（Master 已审；运行结果记 3.2）**

全部用 `gpt-6-luna`、reasoning effort `low`，依据本机 `models_cache.json` 的可用列表与 fast/affordable 描述选便宜档；不自动换模型。每题独立运行一次，记录模型、输入、CLI 事件、读取路径及判定；失败不改题目、模型或判据，不自动重跑。确需另起一轮，先报 Master，另提交新测法再审再测；旧测法及结果原样保留，2.2 的过线标准不变。

| # | 输入原文 | 核对 |
| --- | --- | --- |
| R1 | `$scrum-master 帮我把这个项目接上 Scrum，先了解现状。` | 新版 scrum-master skill 被载入，按 Master 职责接手 |
| R2 | `$designer 我拿不准这个点子值不值得做，先研究一下。` | 新版 designer skill 被载入，进入研究而非交付实现 |
| R3 | `$developer 你接手这个项目，先了解现在要交付什么。` | 新版 developer skill 被载入，按 Developer 职责接手 |
| R4 | `$stakeholder 请以「陌生人」身份看看这个插件，指出第一次使用会卡在哪里。` | 新版 stakeholder skill 被载入，按产品日志中的角色卡看增量 |
| S1 | `$developer 我们要开下一个冲刺，准备给新用户加一份上手说明。` | 实际读取新版 scrum-kernel 的 `conventions/sprint-log.md`；用 Grep 读到文件内容也算 |

角色可调用的证据须能对应临时安装的角色 SKILL 与实际角色行为，不能只看回答自称哪个角色；S1 须有读取文件内容的工具记录，回答里只提文件名不算。原始输出与检查脚本放本冲刺工作文件夹，结论、失败及人工改判理由记 3.2；测试标准与本表先提交并经 Master 审，再运行。

**Risks and open points**

- 旧版 design-kernel 与现行同名技能职责不同：以当前三内核的文件集合重建，校验额外文件和缺失文件。
- 独立包可能丢掉仓库外的链接目标：在 Codex 包内补齐可分发的署名等必要文件，不修改 Claude 源文；发现无法同时满足一致性与 0 死链的项，写进 Next 交 Master / PO 定。
- CLI 的身份认证、插件发现或事件格式可能影响隔离测试：以实际加载、读取证据验收，不能拿本机已装 3.2.0 的结果代替；环境失败单列，不临时改过线标准。
- 版本号、发布、旧 codex 分支退役及本机换装仍按 2.2 留到收官。施工已获 PO 放行；外部模型服务等阻碍据实写入 3.2，由 Master 协调。

Go-ahead: 2026-11-09，PO——在 `sprint-13-codex` 上提交；可以在系统临时目录装插件、跑测试；README 和对外文字要等 Master 审过全文再落盘；不推送，不打 tag，不合入 main，不改 `~/.codex`。合入、tag、发布、推送收官时再定。

### 3.2 Notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 3 and 9). A session that picks up the Sprint reads these first. -->

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-09 | Planning 第 1、2 段：Master 写 1.1–2.2 | 见 2.2 | — | Developer：读本日志和「Developer 先读」，在 3.2 复述验收标准、列出不清楚的地方，再写 3.1；写完提交，停下等 Master 审 How、PO 放行 |
| 2026-11-09 | Developer 读完本日志及「Developer 先读」全部指定文件，先复述六项验收，再写 3.1 How 与五题测法 | ① Codex 包含三个完整内核、四个角色 skill，逐字对应 Claude 源文件，仅工具说法可改且逐条记在本节；② Claude 侧组件与 5.1.2 一致，核对归 Master；③ 一条命令生成 Codex 包，无源改动时重跑不产生 git 改动；④ 独立安装新版，四角色 4/4 可调用，另给 Developer 开冲刺题并确认它实际读到 sprint-log.md；⑤ 包内 markdown 内部链接 0 死链；⑥ README 补默认分支安装与一致的版本号。没有需要 PO 补定的需求疑点；包目录、工具适配和隔离测法按 2.2 留给 How 提方案，版本、发布、旧分支退役及本机换装留到收官 | 指定文件已读；旧包只经 git show / ls-tree 读取 d307296；本机 codex-cli 0.167.0 的 help、模型缓存及官方打包文档；3.1 为方案，所有验收测试均未运行；本轮仅本日志改动 | Master：审 3.1 的目录、生成方式、工具适配清单、五题与模型；PO：审后在 3.1 末尾写放行范围。Developer 已提交并停下，等 PO 传话；未改插件、未切分支、未推送、未打 tag |
| 2026-11-09 | Master 审 3.1 How（d404a00） | 协作方式调整（PO 2026-11-09）：Master 在 plan 模式里审阅时，意见写在 plan 文件里，PO 转给 Developer，由 Developer 照抄进日志。通过，附两处必改：① 包清单 `interface` 和四份 `openai.yaml` 的对外文字，随 README 一起先审全文；② 隔离测试的凭据只放系统临时目录，测完删；不带插件和 marketplace 设置；原始输出提交前查密钥。建议：项 1–3 和文字草稿做完后停一次交审 | 标题和模板一致，只追加了内容；插件里没有链到插件外的链接；工具说法只在 5 句里出现；描述最长 957 字符 | Developer：先把两处必改补进 3.1，再照放行施工 |
| 2026-11-09 | Developer 补两处必改；完成生成器、检查器和隔离测试脚本，生成初版 Codex 包，静态检查通过 | 采纳 Master 的停点建议；展示文字未审，manifest 暂无 interface，四份 openai.yaml 只有显式调用 policy。本机实查：提供方使用设置内的 bearer 凭据，requires_openai_auth 为 false，且无 auth.json；隔离脚本只取当前提供方设置，不复制插件/marketplace，凭据仍仅进系统临时目录。生成包不改 Claude 源；工具改动限下表五句 | `scripts/sync_codex.py`、`scripts/check_codex.py`、`run_codex_smoke.py`；`results/static.json`：内核 80 文件、角色 4、包 91 文件，内容差异 0、死链 0、导航遗漏 0（77 份），原生 skill 校验 7/7；检查器已用缺文件、改正文、坏链接自测；已保存输出凭据扫描 0 命中 | Developer：在干净副本验证两次重跑，隔离安装后五题各跑一次，写入全部对外文字草稿，再交 Master；此时未跑五题 |
| 2026-11-09 | Developer 完成项 1、2；临时安装成功，五题均被模型服务阻塞；全部对外文字全文已写在本节，交审停点到达 | 两次干净副本重跑均 0 改动。R1–R4、S1 各执行一次 CLI，提供方均返回 503「gpt-6-luna 无可用通道」，未执行模型工具调用；CLI 内部各重连 5 次，未手动重跑、未改题、未换模型、未改判据。提供方实际模型目录没有 gpt-6-luna。最初临时目录清理遇 WinError 145，已先删凭据再按 Windows 长路径完整清理，并修好清理函数、用长路径样本验证；以后遇共同的提供方错误也停止剩余题。本轮没有再跑题。对外文字仍只在日志，尚未写进产品文件 | `results/repeatability.json`：两次写入/删除 0、status 干净；`install.json`：新版 5.1.2；`behaviour-assessment.json` 与五题原始 JSONL：验收 4 阻塞；`provider-models.json`：实际目录；`smoke-summary.json`：临时目录及凭据已删、原配置与旧插件未变、原始输出凭据 0 命中；`cleanup-self-test.json`、`interface-render-self-test.json`：清理及展示元数据/版本生成样本通过 | Master：① 审下方根 README、包内 README、manifest interface 和四份 openai.yaml 全文；② 从提供方实际目录选定新一轮测试模型，先审并提交测法再跑，保留本轮失败。Developer：本轮提交后停下，等 PO 传话；验收 4、6 未完成，Sprint 未收官 |

**工具适配清单（已实施；仅生成的 Codex 文件变化）**

| 生成文件与位置 | 工具说法的改法 |
| --- | --- |
| `skills/developer/SKILL.md` 首次加载句 | Skill 工具调用 `ideo-scrum:ideo-kernel`、`ideo-scrum:scrum-kernel` → 按顺序直接读相邻 `../ideo-kernel/SKILL.md`、`../scrum-kernel/SKILL.md` |
| `skills/designer/SKILL.md` 首次加载句 | 同上，内核顺序为 ideo、design |
| `skills/scrum-master/SKILL.md` 首次加载句 | 同上，内核顺序为 ideo、scrum、design |
| `skills/stakeholder/SKILL.md` 首次加载句 | 同上，只读 ideo |
| `skills/design-kernel/SKILL.md` Use Protocol 第 1 条 | `invoke ideo-scrum:ideo-kernel` → 直接读 `../ideo-kernel/SKILL.md`，保留尚未加载时才读的条件 |

上述相对路径均从各自生成的 skill 目录起算。其余内核文件与角色正文逐字保留，description 不变；`subagent` 是两边都成立的角色分工用语，不做替换。若施工时发现还需适配，先逐条补在本节交 Master 审，不静默扩充例外。

**本轮 DoD 与验收证据（Developer 自检，待 Master 审）**

| 项 | 结果与证据 |
| --- | --- |
| 内容忠实 / 验收 1 | 三内核 80 文件、四角色；除上表五句工具适配外 0 差异。`results/static.json`、`static-after-recovery.json`；七份 skill 原生格式校验 7/7 |
| 可导航 | 三个内核下 77 份参考、方法、约定与模板均在入口两跳内可达，导航遗漏 0 |
| 无死链 / 验收 5 | 包内显式 Markdown 本地链接检查 1 处，缺文件或锚点 0；其余反引号文件导航另按上一行核对 |
| 验收 2 | Developer 对照：Claude 源目录及 marketplace 0 改动；README、CLAUDE.md 也未改。`results/source-and-criteria.json`；正式结论由 Master 核对 |
| 验收 3 | 干净的已提交副本连续运行同步命令两次，写入和删除均 0、git status 均干净；副本已删除。`results/repeatability.json` |
| 验收 4 | 阻塞：新版 5.1.2 在临时目录安装成功，但五题都在模型服务 503 处停止，没有工具执行，不能认作四角色或 sprint-log 读取通过。`results/behaviour-assessment.json` |
| 验收 6 与对外文字 | 待审：以下七段为全文；根 README、包 README、manifest interface、四份角色 UI 文字均尚未写入交付文件。包 README 的版本替换及展示元数据已用临时样本验证 |
| 测试纪律与凭据 | 题目及 2.2 的判据与 d404a00 相同；未换模型或重跑。原配置与旧插件指纹未变，临时目录和凭据已删除；原始输出提交前按实际凭据值和令牌形态扫描，结果另存 `results/secret-scan.json` |

**对外文字全文草稿（待 Master 审，未写入交付文件）**

以下是将落盘的全文；根 README 保留既有内容，只加 Codex 入口、文件地图及同步说明。包内 README 显示版本由清单生成；源模板中的版本位置使用占位符，生成后呈现为这里的 5.1.2。以下 JSON 的 interface 和四份 YAML 审过后，才进入生成源。

**README.md（全文）**

````markdown
# IDEO-Scrum

为 Claude Code 与 Codex 提供 Design Thinking 与 Scrum Sprint 方法论的插件。v5.1.2。

## 快速开始

### Claude Code

在 Claude Code 会话中安装：

```
/plugin marketplace add seapawn1/IDEO-Scrum
/plugin install ideo-scrum@ideo-scrum
/reload-plugins
```

装好后不需要记任何命令——描述你在做的事，相关方法论会自动介入：

```
帮我规划下个 Sprint，我们有 5 个待办项要排优先级
```
```
这个功能要不要做我拿不准，先做一轮用户访谈的设计
```

也可以显式进入某个角色工作（角色注入当前对话，不影响其他对话）：

```
/ideo-scrum:scrum-master     # Scrum Master：三大支柱、五项价值观、仪式优先
/ideo-scrum:designer         # Designer：设计结对——IDEO 五模式 + 设计冲刺，原型快速验证
/ideo-scrum:developer        # Developer：Sprint Backlog、DoD、Review、Retro
/ideo-scrum:stakeholder      # Stakeholder：一个命令多种身份——外部视角，或常驻做非源码杂务；源码归 Developer
```

### Codex

在终端中安装：

```
codex plugin marketplace add seapawn1/IDEO-Scrum
codex plugin add ideo-scrum@ideo-scrum
```

随后在新会话里进入角色：

```
$scrum-master   # Scrum Master
$designer       # Designer
$developer      # Developer
$stakeholder    # Stakeholder
```

四个角色需要显式调用，三个方法论内核按任务自动介入；它们和 Claude Code 版使用同一份源内容。需要区分同名技能时，可用插件命名空间，例如 `$ideo-scrum:developer`。

**插件提供什么**

| 组件 | 内容 |
|---|---|
| `ideo-kernel` skill | IDEO / d.school 五模式（Empathize → Test）、~40 个设计方法——整个插件共用的工具箱，也是设计各阶段的基础 |
| `design-kernel` skill | 设计冲刺：按 IDEO 五阶段（共情、定义、构思、原型、测试）组织的《Sprint》原文摘录，加设计日志约定与模板；设计与冲刺平级，结论回流产品日志 |
| `scrum-kernel` skill | Scrum Guide 2020 全文、SGEP 扩展包全文（含角色章）、Artifact / Event 分项引用 |
| 4 个 Claude Code command | Scrum Master / Designer / Developer / Stakeholder 四种角色视角，用 `/ideo-scrum:scrum-master` 等手动进入；进入时自动加载对应内核（都先加载 ideo-kernel） |

## 这里是什么

本插件将 Design Thinking（设计思维）和 Scrum Sprint（敏捷冲刺）两套方法论集成到 Claude Code 中，通过技能（skills）和斜杠命令（commands）提供结构化的协作流程。不做项目管理工具本身，不做 JIRA/Linear 集成，也不做团队协作平台——只提供方法论引导和流程框架。

## 文件地图

### 根目录

| 文件/目录 | 内容 |
|---|---|
| `LICENSE` | MIT — 覆盖本仓库原创部分 |
| `ATTRIBUTION.md` | 四个第三方来源的完整署名与授权条款 |
| `.claude-plugin/marketplace.json` | marketplace 清单，供 `/plugin marketplace add` 使用 |
| `.agents/plugins/marketplace.json` | Codex marketplace 清单，指向同一分支里的 Codex 分发包 |
| `scripts/sync_codex.py` | 从 Claude Code 源文件生成 Codex 包：`python scripts/sync_codex.py` |
| `scripts/check_codex.py` | 核对 Codex 内容一致性、内部链接、导航与重复生成；需要 PyYAML |
| `.claude/` | 项目配置——`settings.json`、`seapawn.md`（作者待办与私人笔记，不入库）；项目指令 `CLAUDE.md` 在仓库根目录，记忆在仓库外 `S:\SeaPawn-Memory\memory\IDEO-Scrum\` |

### Claude Code 插件

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/.claude-plugin/plugin.json` | 插件清单 v5.1.2 |
| `plugins/ideo-scrum/commands/designer.md` | Command `/ideo-scrum:designer` — 设计阶段结对（IDEO 五模式 + 设计冲刺，原型快速验证、拍板前不落地；进入时加载 ideo-kernel 与 design-kernel） |
| `plugins/ideo-scrum/commands/developer.md` | Command `/ideo-scrum:developer` — Developer 角色（Scrum Guide 2020 原文抄录＋2026 精炼补充；进入时加载 ideo-kernel 与 scrum-kernel） |
| `plugins/ideo-scrum/commands/scrum-master.md` | Command `/ideo-scrum:scrum-master` — Scrum Master 角色（Scrum Guide 2020 原文抄录＋2026 精炼补充；替 PO 派活、派子代理审阅；进入时加载三个内核） |
| `plugins/ideo-scrum/commands/stakeholder.md` | Command `/ideo-scrum:stakeholder` — Stakeholder（SGEP 角色章为底；一个命令多种身份：外部视角——按项目写定的身份看产品和增量，说出期望与现状的差距，反馈交 PO，独立评价由全新子代理给；也可作常驻会话做非源码杂务，如维护看板；源码归 Developer；进入时加载 ideo-kernel） |

### Codex 分发包

`codex/plugins/ideo-scrum/` 由 `python scripts/sync_codex.py` 生成，版本取 Claude Code 插件清单。修改三个内核或角色时，先改 `plugins/ideo-scrum/`，再运行同步命令；生成包中的工具用语适配由脚本统一处理。

| 文件/目录 | 内容 |
|---|---|
| `codex/plugins/ideo-scrum/.codex-plugin/plugin.json` | Codex 插件清单 |
| `codex/plugins/ideo-scrum/skills/ideo-kernel/`、`design-kernel/`、`scrum-kernel/` | 三个内核的全部文件，含约定、模板和源材料 |
| `codex/plugins/ideo-scrum/skills/scrum-master/`、`designer/`、`developer/`、`stakeholder/` | 四个原生角色 skill；各有 SKILL.md 和 agents/openai.yaml |
| `codex/plugins/ideo-scrum/README.md`、`LICENSE`、`ATTRIBUTION.md` | 包内说明及来源授权 |
| `scripts/codex_interface.json`、`scripts/codex_readme.md` | Codex 展示文字与包内 README 的生成源 |

### design-kernel skill

> `design-kernel` 是 v3 用过的名字（当时指设计冲刺与 IDEO 合在一起的内核，v4 改名 ideo-kernel）；v5 起重新启用，意思变了：专讲设计冲刺，IDEO 五模式与方法库留在 ideo-kernel。

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | Design Kernel 入口（设计冲刺按 IDEO 五阶段组织：每个阶段对应的 IDEO 模式、原书摘录、Use Protocol） |
| `plugins/ideo-scrum/skills/design-kernel/` 下 `empathize/`、`define/`、`ideate/`、`prototype/`、`test/` | 设计冲刺原书摘录（Knapp，原文只删不改，例图改画成 Mermaid 或文字）：共情 define-the-challenge / start-at-the-end / ask-the-experts；定义 make-a-map / how-might-we / pick-a-target；构思 remix-and-improve / sketch / decide / rumble / storyboard；原型 fake-it / prototype；测试 small-data / interview / learn |
| `plugins/ideo-scrum/skills/design-kernel/conventions/` | 设计日志约定 v1（design-log：设计放哪、谁定、各阶段怎么用子代理与角色卡、收官）与设计日志模板（design-backlog-template，五章） |

### ideo-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/ideo-kernel/SKILL.md` | IDEO Kernel 入口（整个插件共用的工具箱：IDEO 五模式表 + Method Catalog：按模式索引与合表 + Use Protocol） |
| `plugins/ideo-scrum/skills/ideo-kernel/IDEO-modes/` | IDEO Design Thinking 五模式 reference（Empathize / Define / Ideate / Prototype / Test，各含 WHAT/WHY/HOW + Transition） |
| `plugins/ideo-scrum/skills/ideo-kernel/methods/` | Design Thinking 方法库（~40 个方法，含 Use Before / Use Notes / Do Not Use When） |

### scrum-kernel skill

| 文件/目录 | 内容 |
|---|---|
| `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | Scrum Sprint 技能内核（Scrum Guide 概述 + Artifact / Event / Reference 目录表） |
| `plugins/ideo-scrum/skills/scrum-kernel/scrum-guide-2020.md` | Scrum Guide 2020 官方全文 |
| `plugins/ideo-scrum/skills/scrum-kernel/assets/scrum-guide-expansion-pack-2026.1.md` | SGEP 完整源文档（Theory / Values-OODA / Roles / 引用列表） |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-*.md` | 4 个 Artifact reference：Product / Increment / Product Backlog / Sprint Backlog |
| `plugins/ideo-scrum/skills/scrum-kernel/references/scrum-event-*.md` | 5 个 Event reference：Sprint / Sprint Planning / Daily Scrum / Sprint Review / Sprint Retrospective |
| `plugins/ideo-scrum/skills/scrum-kernel/overview.md` | 约定总览 v1（与 SKILL.md 并列）：三层、文件与文档文件夹、角色、会话分工、目标不变其余可调、与官方故意不同之处 |
| `plugins/ideo-scrum/skills/scrum-kernel/conventions/` | 约定 v1：product-log 与 product-backlog-template（产品日志）；sprint-log 与 sprint-backlog-template（冲刺日志） |

### 工作记录（scrum/）

| 文件/目录 | 内容 |
|---|---|
| `scrum/ProductBacklog.md` | 产品日志——一 Product / Product Goal / DoD；二 利益相关者表与 Map（流程见插件 scrum-kernel 的 conventions/）；三 PBI（3.1 当前、3.2 已完成附出处） |
| `scrum/documents/ExpertNotes.md` | 客户之声——作者使用流程已口述落盘（项目骨架→IDEO→design 文件→背景研究→target 四阶段，含与 SprintBacklog 同源表、分工原则、未决清单）；将作为方法论分享的素材 |
| `scrum/documents/PBI-27-bot-research.md` | Bot 工作方式研究（PBI-27）：Grok Bot、DeepSeekBot（pstack）、DS-Bot 等的可借鉴机制，带出处 |
| `scrum/documents/five-stage-mapping.svg` | Scrum 三阶段与 IDEO 五模式的对应图（2026-11-06，ExpertNotes 附录用） |
| `scrum/documents/sprint-08-design-kernel.md` | Sprint 08 冲刺日志归档（设计内核独立，v5.0.0）：关键决定、触发回归、审查与 Review |
| `scrum/documents/sprint-09-design-template.md` | Sprint 09 冲刺日志归档（设计日志模板改正，小冲刺，v5.0.1） |
| `scrum/documents/sprint-10-conventions.md` | Sprint 10 冲刺日志归档（流程全部进插件，v5.1.0）：关键决定、三轮测试、审查与 Review |
| `scrum/documents/conventions-review-log.md` | PO 逐段审阅约定 v1 的记录（2026-11-09，19 处，每条带状态）；当时对照的四份中文译文已删，见 `git show 6a2fd5e` |
| `scrum/documents/sprint-11-conventions-review.md` | Sprint 11 冲刺日志归档（约定照 PO 审阅改定，小冲刺，v5.1.1）：19 处的结论、审阅、design-log 读着别扭的地方 |
| `scrum/documents/sprint-12-overview-to-root.md` | Sprint 12 冲刺日志归档（总览挪到 scrum-kernel 根目录，小冲刺，v5.1.2） |
| **冲刺蒸馏 / 归档** | 1.x 五期与 Sprint 06、07 已蒸馏至 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`（MEMORY.md 索引 + 各期教训档案，含出处指向 git）；Sprint 08 起，冲刺日志压缩后归档进 `scrum/documents/` |

### 源参考

原始源材料（书籍原件、扫描配图等）**不入库**，仅保留在作者本地。插件内的所有摘录均带章节级署名，来源与授权条款见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 来源与授权

本仓库的**原创部分**（插件结构、skill 组织、工作记录 `scrum/`）以 [MIT](LICENSE) 发布。

插件内的方法论摘录来自四个外部来源，各自的许可条款不同：

| 来源 | 许可 |
|---|---|
| The Scrum Guide 2020 | CC BY-SA 4.0 |
| Scrum Guide Expansion Pack 2026.1 | CC BY-SA 4.0 |
| Stanford d.school Design Thinking Bootleg | CC BY-**NC**-SA 4.0 |
| *Sprint* (Knapp et al., 2016) | 全版权，仅记录方法流程 |

> ⚠️ 第三项含**非商业限制**，因此本仓库整体**不构成 OSI 定义下的开源软件**。商业场景使用前请阅读 [ATTRIBUTION.md](ATTRIBUTION.md)。

本仓库不包含任何书籍全文或原始出版物。若这些方法论对你有价值，请通过官方渠道支持原作者。
````

**codex/plugins/ideo-scrum/README.md（全文）**

````markdown
# IDEO-Scrum for Codex

v5.1.2。Design Thinking 与 Scrum Sprint 方法论插件，与 Claude Code 版共用源内容。

## 安装

```
codex plugin marketplace add seapawn1/IDEO-Scrum
codex plugin add ideo-scrum@ideo-scrum
```

安装后，在新会话中用 `$developer`、`$scrum-master`、`$designer` 或 `$stakeholder` 进入角色。三个内核按任务自动介入；角色需要显式调用。也可用插件命名空间，例如 `$ideo-scrum:developer`。

## 内容

| 入口 | 内容 |
| --- | --- |
| [ideo-kernel](skills/ideo-kernel/SKILL.md) | 共用的 IDEO 五模式与方法库 |
| [design-kernel](skills/design-kernel/SKILL.md) | 从挑战到经测试的原型和结论 |
| [scrum-kernel](skills/scrum-kernel/SKILL.md) | 规划、交付与审阅增量，附约定和模板 |
| [Scrum Master](skills/scrum-master/SKILL.md) | 协助 PO 精化、派活、跟踪与审阅 |
| [Designer](skills/designer/SKILL.md) | 研究问题、制作原型并验证 |
| [Developer](skills/developer/SKILL.md) | 制定 How、维护冲刺日志并交付增量 |
| [Stakeholder](skills/stakeholder/SKILL.md) | 按产品日志中的身份提供外部视角 |

## 来源与授权

原创部分见 [LICENSE](LICENSE)；第三方内容见 [ATTRIBUTION.md](ATTRIBUTION.md)。d.school 材料含非商业限制，《Sprint》摘录保留全版权条款。

本包由仓库的 `python scripts/sync_codex.py` 生成。工具用语适配之外，方法论内容与 Claude Code 版一致。
````

**codex/plugins/ideo-scrum/.codex-plugin/plugin.json 的 interface（全部）**

```json
{
  "displayName": "IDEO-Scrum",
  "shortDescription": "Design Thinking 与 Scrum Sprint 方法论",
  "longDescription": "提供 ideo-kernel、design-kernel、scrum-kernel 三个方法论 skill，以及 Scrum Master、Designer、Developer、Stakeholder 四个角色。IDEO 方法共用；设计交付原型与结论，冲刺交付增量；约定与模板随插件安装。",
  "developerName": "SeaPawn",
  "category": "Productivity",
  "capabilities": [
    "Interactive"
  ],
  "defaultPrompt": [
    "帮我规划下个 Sprint，明确 Sprint Goal 和交付范围。",
    "这个想法值不值得做，先研究并验证原型。",
    "帮我检查本次增量，准备 Sprint Review 和 Retrospective。"
  ]
}
```

**skills/scrum-master/agents/openai.yaml（全文）**

```yaml
interface:
  display_name: "Scrum Master"
  short_description: "守护 Scrum 流程，协助精化、派活、跟踪与审阅，价值取舍由 PO 决定"
  default_prompt: "$scrum-master 帮我了解项目现状，并准备下一次 Scrum 活动。"
policy:
  allow_implicit_invocation: false
```

**skills/designer/agents/openai.yaml（全文）**

```yaml
interface:
  display_name: "Designer"
  short_description: "结对研究问题、探索方案与测试原型，将结论交回产品日志，由 PO 定方向"
  default_prompt: "$designer 帮我研究这个问题，做出原型并验证方案。"
policy:
  allow_implicit_invocation: false
```

**skills/developer/agents/openai.yaml（全文）**

```yaml
interface:
  display_name: "Developer"
  short_description: "制定冲刺方案、维护冲刺日志、实现增量并交付 DoD 证据，等待 PO 放行"
  default_prompt: "$developer 先了解项目和冲刺日志，再提出实现方案。"
policy:
  allow_implicit_invocation: false
```

**skills/stakeholder/agents/openai.yaml（全文）**

```yaml
interface:
  display_name: "Stakeholder"
  short_description: "按产品日志中的身份评价增量或原型，指出期望与现状的差距，反馈交 PO"
  default_prompt: "$stakeholder 请按产品日志中的指定身份评价本次增量。"
policy:
  allow_implicit_invocation: false
```

## 4. Review

<!-- Written at close by the Product Owner, the Scrum Master, and the Developer: the Increment; the Definition of Done and the acceptance criteria, item by item; what the review found; the stakeholders' view; changes to the product log and the Product Goal (sprint-log.md, convention 18). -->
