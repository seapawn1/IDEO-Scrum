# Sprint Backlog — Sprint 13 (codex)

> Started: 2026-11-09 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-13-codex` | Product Owner: SeaPawn | Scrum Master: Claude（Claude Code 主会话）| Developer: Codex（GPT，在 Codex 里跑）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).
> 归档：2026-11-09 开工、2026-11-10 收官，版本不动（仍 5.1.2）。Developer 在 Codex 里跑，与 Master 只靠本日志通讯，PO 传话。日志已压缩成关键决定；三轮测试的原始输出在仓库外（见 3.2）。

## 1. Why

### 1.1 Sprint Goal

**Codex 版跟上**：Codex 里的 IDEO-Scrum 与 Claude Code 版一致——三个内核、四个角色、约定与模板都在；以后发版能照样同步；在 Codex 里开 Developer，装上就能照约定干活。

### 1.2 Definition of Done

Output Done 三条：内容忠实、可导航、无死链（产品日志 1.3），用在 Codex 包上。Claude 侧的描述不动，不跑 Claude 的触发测试。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-43 | Codex 版——与 Claude Code 版一致 | 作为熟手，我想要 Codex 里装上的 IDEO-Scrum 与 Claude Code 版一致（三个内核、四个角色、约定与模板），以便在 Codex 里开的 Developer 也照同一套约定干活，和 Claude Code 里的 Master 靠冲刺日志协作 | Map ①（装插件，开会话） | M |

### 2.2 Refinement

**PO 定（2026-11-09）**
- 只选 PBI-43；Sprint Goal 如 1.1。
- Codex 版并入 main，不再单靠 `codex` 分支；前提是不影响 Claude Code 的使用。
- 本冲刺算在当前 Product Goal 之内。
- Developer 在 Codex 里跑（GPT），和 Master 只靠本日志通讯，PO 传话。
- Codex 里装着的旧版（3.2.0）冲刺期间不停用，收官时换成新版。

**协作办法**（Master 定）：通道只有本日志；两边共用 `S:\IDEO-Scrum` 这一个工作目录，所以轮流动手；每轮做完提交、在 3.2 记一行，Next 写明轮到谁，然后停下；PO 传话只说「轮到你了，读冲刺日志」；拿不准的事写进 Next 问 PO。

**验收标准**
1. 内容一致：Codex 包有三个内核的全部文件和四个角色 skill；内核文件与 `plugins/ideo-scrum/skills/` 逐字相同，角色正文与 `commands/*.md` 相同；改动只限工具说法，逐条登记。
2. Claude Code 不受影响：`plugins/ideo-scrum/` 与 `.claude-plugin/marketplace.json` 没改动（Master 核对）。
3. 同步能重跑：一条命令从 `plugins/ideo-scrum/` 生成 Codex 包；没有改动时重跑，`git status` 干净。
4. Codex 里能用：装上新版后四个角色都能调用；给 `$developer` 一个开冲刺的任务，它读到 `conventions/sprint-log.md`。
5. 无死链：包内 markdown 的内部链接都能解析。
6. README 同步：Codex 安装说明（不再要 `--ref codex`）和版本号。

**测试**（方法与过线标准先提交、后跑）：1、3、5 用脚本核对，过线是 0 处不一致（登记的工具说法除外）、重跑 0 改动、0 死链；4 由 Developer 在 Codex 里用便宜的模型跑五题（四个角色各一题，另给 `$developer` 一题开冲刺），题目不带引导词，不动 PO 的 Codex 安装，过线是角色 4/4 能调用、`$developer` 读到 `sprint-log.md`；2 由 Master 核对。

## 3. How

### 3.1 How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 生成 Codex 分发包 | `scripts/sync_codex.py`、`codex/plugins/ideo-scrum/`、`.agents/plugins/marketplace.json` | 一条命令生成三个内核和四个角色；只有登记的工具适配；Claude 源目录和 marketplace 不变 |
| 2 | 静态验收 | 内容、文件集合、链接、重跑的检查脚本和结果 | 验收 1、3、5 过线 |
| 3 | 隔离安装与五题验证 | 临时安装、逐题判定 | 验收 4 过线；PO 的安装未改 |
| 4 | README 与对外文字 | 根 README、包内 README、包清单的展示文字、四份角色界面文字 | 全文先给 Master 审，通过后落盘；验收 6 |
| 5 | 交审与修正 | 逐项 DoD 与证据 | Master 核对 Claude 侧不受影响并审增量 |

**Key choices**

- **目录与来源**：沿用旧包的 `codex/plugins/ideo-scrum/` 作独立生成物，与 Claude 包共存于 main；`.agents/plugins/marketplace.json` 只指向 Codex 包。单独镜像才能适配工具用语，也能脱离仓库安装。
- **一条同步命令**：`python scripts/sync_codex.py`。三个内核完整复制；四个角色由 `commands/*.md` 生成原生 skill（加 `name`，保留 description 和正文，只套用 3.2 登记的替换）；角色的 `agents/openai.yaml` 保持显式调用，内核保留自动触发。包内无时间戳，随源删除的旧文件一并清掉。
- **工具适配**：不全局替换 `ideo-scrum:` 或 `subagent`；只把「用 Skill 工具加载内核」这类句子改成直接读相邻内核的 `SKILL.md`，顺序和「已加载就跳过」不变。
- **检查办法**：`scripts/check_codex.py` 核对完整文件集合与内容、角色 frontmatter 与正文、清单与角色元数据；链接检查覆盖行内和引用式本地链接及锚点，包外目标算失败；先用缺文件、坏链接、改正文的样本自测。
- **隔离与证据**：每题开全新进程，临时项目加独立的 Codex 用户目录；凭据只写系统临时目录，测完删；不向当前 `~/.codex` 写插件或配置。

**Risks and open points**

- 旧版 design-kernel 与现行同名技能职责不同：以现行三内核的文件集合重建。
- 独立包可能丢掉仓库外的链接目标：在包内补齐署名等文件，不改 Claude 源文。
- 认证、插件发现或事件格式可能影响隔离测试：以实际加载和读取的证据验收，不拿本机已装 3.2.0 的结果代替。

Go-ahead: 2026-11-09，PO——在 `sprint-13-codex` 上提交；可以在系统临时目录装插件、跑测试；README 和对外文字要等 Master 审过全文再落盘；不推送，不打 tag，不合入 main，不改 `~/.codex`。合入、tag、发布、推送收官时再定。

### 3.2 Notes

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-09 | Planning：Master 写 1.1–2.2，PO 定只选 PBI-43 | 只选一条：第一次跨工具协作，范围小，Review 时分得清问题出在活本身还是通讯；不带 PBI-40，冲刺中途改约定会改变 Developer 照着做的规矩；Sprint Goal 加上「以后发版能照样同步」——旧 `codex` 分支就是手工同步，落后六次发版 | 产品日志 PBI-43；`codex` 分支停在 3.2.0 | Developer 复述验收、写 How |
| 2026-11-09 | Developer 复述六项验收、写 How；Master 审 How：通过，附两处必改 | ① 包清单的展示文字、四份 `openai.yaml`、README 先审全文再落盘（约定 13）；② 测试凭据只放系统临时目录，测完删，输出提交前查密钥。PO 放行，范围见 3.1。协作方式调整（PO）：Master 在 plan 模式里写审阅，PO 把文件路径转给 Developer，由它抄进日志 | 3.1；PO 的放行 | Developer 施工 |
| 2026-11-09 | 生成器、检查器、隔离测试脚本；生成初版 Codex 包 | 内核 80 个文件、角色 4、包 91 个文件；内容差异 0、死链 0、导航遗漏 0；原生 skill 格式校验 7/7；检查器自测过 | `scripts/sync_codex.py`、`scripts/check_codex.py` | 隔离安装，跑五题 |
| 2026-11-09 | 五题第一轮：全部 503，所选模型 `gpt-6-luna` 在提供方没有通道 | 模型取自本地模型缓存，提供方实际目录里没有；失败原样保留，不自动重跑、不改题 | 提供方实际目录；CLI 重连 5 次的记录 | 等 PO 指定模型 |
| 2026-11-09 | 第二轮：PO 指定 `gpt-5.6-terra`（low）；第三轮：原生 Skill 输入 | 第二轮模型可用，但只读权限拒读所有文件，不算过线；纯文本 CLI 里打 `$角色` 挂不上角色，第三轮改用 app-server 的原生 Skill 输入（与从 `$` 菜单选角色等效），在各自临时项目里放开命令权限。题目、过线标准没改。结果 5/5：四个角色注入的全文与生成包逐字一致（哈希）、回答各守其职；S1 读到新版 `conventions/sprint-log.md` 的正文 | 汇总判定与哈希在 `results/`（已删，见 git 历史）；原始输出在仓库外归档 | 对外文字全文交审 |
| 2026-11-09 | 原始输出含模型服务地址：备份到仓库外，改写未推送的冲刺历史 | 地址在第一轮的 503 报错里，不是密钥；仓库是公开的，合入 main 并推送就会留在公开历史里。PO 同意改写：72 个原始输出文件从 11 个提交里移除，汇总里的原始回答和命令全文删去，只留判定和哈希；扫描范围加上提供方地址和设置值，复扫 0 命中；备份在 `S:\IDEO-Scrum-Archives\sprint-13-codex-20261109-230117\`（含地址，只留本机，不推送） | 提交范围 `git log -p` 里提供方地址 0 处；没有备份引用 | 英文文字交审 |
| 2026-11-09 | Master 审增量与对外文字；Developer 落盘并重新生成 | 包通过。PO 定对外文字（包内 README、清单的展示文字、四份角色界面文字）用英文，根 README 仍中文。五处文字改动：根 README 写进 Codex；表里补 Codex 的角色形式；「自动介入」改成只描述设置（没测过 Codex 会不会自动调用内核）；给旧分支用户补迁移命令（对着 0.167.0 的 help 核对）；developer 简介改写。scrum-master 简介补不回「价值由 PO 决定」：补全超过 64 字符上限，保留 57 字符的原稿 | 3.2 其余行；`results/` 汇总 | Master Review |
| 2026-11-10 | 收官：Master 在全新克隆里重跑同步和检查，并召唤「陌生人」 | 见 4 Review。PO 定：版本与 Claude 一致（不升版本）；推送；旧 `codex` 分支退役；本机 Codex 改装新版（PO 授权这一步改 `~/.codex`） | 4 Review | — |

**工具适配清单（共 5 句，只在生成的 Codex 文件里）**

| 生成文件与位置 | 工具说法的改法 |
| --- | --- |
| `skills/developer/SKILL.md`、`designer/SKILL.md`、`scrum-master/SKILL.md`、`stakeholder/SKILL.md` 的首次加载句 | 用 Skill 工具调用 `ideo-scrum:<内核>` → 按顺序直接读相邻的 `../<内核>/SKILL.md`（相对本 skill 的目录），「已加载则跳过」不变；内核顺序：developer 是 ideo、scrum，designer 是 ideo、design，scrum-master 是 ideo、scrum、design，stakeholder 只读 ideo |
| `skills/design-kernel/SKILL.md` Use Protocol 第 1 条 | `invoke ideo-scrum:ideo-kernel` → 直接读 `../ideo-kernel/SKILL.md`，保留「尚未加载时才读」的条件 |

其余内核文件与角色正文逐字保留，description 不变；`subagent` 是两边都成立的分工用语，不替换。

## 4. Review

**增量**（PBI-43，版本不动，仍 5.1.2）：Codex 分发包 `codex/plugins/ideo-scrum/`（92 个文件：三个内核 80 个，四个角色 skill 各带 `agents/openai.yaml`，清单、README、LICENSE、ATTRIBUTION）并入 main；`.agents/plugins/marketplace.json` 指向它；`scripts/sync_codex.py` 一条命令从 `plugins/ideo-scrum/` 生成，`scripts/check_codex.py` 核对内容、链接、导航和重复生成；展示文字和包内 README 的生成源是 `scripts/codex_interface.json`、`scripts/codex_readme.md`；根 README 补了 Codex 入口、旧 `codex` 分支的迁移命令和两端的组件形式。冲刺里没动 Claude 侧文件和 `.claude-plugin/marketplace.json`。

**DoD 与验收**（Master 逐项核对，在全新克隆里重跑）：

| 项 | 结果 |
| --- | --- |
| 验收 1 内容一致；内容忠实 | 通过：ideo-kernel、scrum-kernel 逐字相同；design-kernel 只差 SKILL.md 一句；四个角色正文各只差加载内核那一句；正是登记的 5 句 |
| 验收 2 Claude 不受影响 | 通过：`plugins/`、`.claude-plugin/`、LICENSE、ATTRIBUTION.md 与冲刺前 0 差异 |
| 验收 3 同步能重跑 | 通过，附一个说明：Windows 上 `core.autocrlf=true` 的新克隆，第一次同步会把 6 个生成的 JSON/YAML 的换行从 CRLF 改成 LF，内容与已提交的相同（`git diff` 为空，`git add -A` 后没有暂存），之后写入 0；已写进 CLAUDE.md |
| 验收 4 Codex 里能用 | 通过：第三轮 5/5。测法因环境改过两次，题目和过线标准没改；Master 抽查原始输出，S1 读到 `conventions/sprint-log.md` 的正文，角色注入的是 Codex 版正文。**留给 PO 看的一点**：过线是第三轮才拿到的，前两轮（模型无通道、只读权限）的结果都留在记录里 |
| 验收 5 无死链；可导航 | 通过：10 个本地链接、77 份资源，错误 0，入口两跳内可达 |
| 验收 6 README | 通过：安装不带 `--ref codex`；两处版本号和两端清单一致（5.1.2）；迁移命令对着 codex-cli 0.167.0 的 help 核对过 |

**审阅发现**：How 通过，两处必改都改了；包通过，对外文字改成英文、五处文字改动已落盘；Developer 没越过放行（只在冲刺分支提交，没推送、没打 tag、没动 `~/.codex`，本机 Codex 仍是 3.2.0）。留下的小点：scrum-master 简介没补回「价值由 PO 决定」；内核在 Codex 里的自动触发没测，README 只写「设置允许」；同步脚本比较生成文件时不忽略换行差异（见验收 3）。

**利益相关者的看法**（「陌生人」卡，全新子代理，只给两份 README 和包内文件；这次它用的是 Codex）：按字面能装、能叫出角色，但选完角色无从开口，也不知道自己就是 PO，只能猜着起步。卡点：Codex 段没有首句示例（Claude 段有），各角色 `openai.yaml` 的示例又多半假定已有日志；两份 README 都没说「你是 PO，AI 演其余角色」，PO、PBI、DoD、SGEP、Increment、product log 没解释也没链；旧分支的迁移读得懂，但要先确认旧装的名字正是 `ideo-scrum@ideo-scrum`，没教怎么确认。核对不了：Codex 的最低版本、子代理在 Codex 里能不能用（`codex plugin` 子命令 Master 已对 0.167.0 的 help 核对过）。「五句话」的说法 diff 实测属实。结论：入口能用；满意度缺口在 PBI-30 的范围（首句、PO 身份、术语），不阻塞本冲刺，登记进 PBI-46 ⑤。

**产品日志**：PBI-43 移入 3.2；新增 PBI-46（Codex 版的后续小修）；PBI-30、40、44、45 的备注跟着改；1.1、1.2 补上 Codex。**Product Goal** 不变，Master 已提醒 PO：开下一个冲刺前，下一个冲刺和本目标不合就先定新目标。

**发布**：版本不动（PO：与 Claude 一致）；tag `sprint-13-codex`；推送后，旧 `codex` 分支退役（存档 tag `codex-v3.2.0`）、本机 Codex 改装新版——这两步的结果记入收官后的提交。
