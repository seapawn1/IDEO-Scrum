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

**五题与模型（待 Master 审；未运行）**

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
- 当前没有待 PO 补定的需求疑点。版本号、发布、旧 codex 分支退役及本机换装仍按 2.2 留到收官；本轮只提交本日志，后续施工等 Master 审 How、PO 放行。

Go-ahead: （待 PO）

### 3.2 Notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 3 and 9). A session that picks up the Sprint reads these first. -->

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-09 | Planning 第 1、2 段：Master 写 1.1–2.2 | 见 2.2 | — | Developer：读本日志和「Developer 先读」，在 3.2 复述验收标准、列出不清楚的地方，再写 3.1；写完提交，停下等 Master 审 How、PO 放行 |
| 2026-11-09 | Developer 读完本日志及「Developer 先读」全部指定文件，先复述六项验收，再写 3.1 How 与五题测法 | ① Codex 包含三个完整内核、四个角色 skill，逐字对应 Claude 源文件，仅工具说法可改且逐条记在本节；② Claude 侧组件与 5.1.2 一致，核对归 Master；③ 一条命令生成 Codex 包，无源改动时重跑不产生 git 改动；④ 独立安装新版，四角色 4/4 可调用，另给 Developer 开冲刺题并确认它实际读到 sprint-log.md；⑤ 包内 markdown 内部链接 0 死链；⑥ README 补默认分支安装与一致的版本号。没有需要 PO 补定的需求疑点；包目录、工具适配和隔离测法按 2.2 留给 How 提方案，版本、发布、旧分支退役及本机换装留到收官 | 指定文件已读；旧包只经 git show / ls-tree 读取 d307296；本机 codex-cli 0.167.0 的 help、模型缓存及官方打包文档；3.1 为方案，所有验收测试均未运行；本轮仅本日志改动 | Master：审 3.1 的目录、生成方式、工具适配清单、五题与模型；PO：审后在 3.1 末尾写放行范围。Developer 已提交并停下，等 PO 传话；未改插件、未切分支、未推送、未打 tag |

**工具适配清单（拟，未施工；仅生成的 Codex 文件变化）**

| 生成文件与位置 | 工具说法的改法 |
| --- | --- |
| `skills/developer/SKILL.md` 首次加载句 | Skill 工具调用 `ideo-scrum:ideo-kernel`、`ideo-scrum:scrum-kernel` → 按顺序直接读相邻 `../ideo-kernel/SKILL.md`、`../scrum-kernel/SKILL.md` |
| `skills/designer/SKILL.md` 首次加载句 | 同上，内核顺序为 ideo、design |
| `skills/scrum-master/SKILL.md` 首次加载句 | 同上，内核顺序为 ideo、scrum、design |
| `skills/stakeholder/SKILL.md` 首次加载句 | 同上，只读 ideo |
| `skills/design-kernel/SKILL.md` Use Protocol 第 1 条 | `invoke ideo-scrum:ideo-kernel` → 直接读 `../ideo-kernel/SKILL.md`，保留尚未加载时才读的条件 |

上述相对路径均从各自生成的 skill 目录起算。其余内核文件与角色正文逐字保留，description 不变；`subagent` 是两边都成立的角色分工用语，不做替换。若施工时发现还需适配，先逐条补在本节交 Master 审，不静默扩充例外。

## 4. Review

<!-- Written at close by the Product Owner, the Scrum Master, and the Developer: the Increment; the Definition of Done and the acceptance criteria, item by item; what the review found; the stakeholders' view; changes to the product log and the Product Goal (sprint-log.md, convention 18). -->
