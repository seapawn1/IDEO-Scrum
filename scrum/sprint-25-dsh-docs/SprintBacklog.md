# Sprint Backlog — Sprint 25 (dsh-docs)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: claude/sprint-25-dsh-docs-4f4070 | Product Owner: SeaPawn | Scrum Master: IDEO-Scrum Master | Developer: Sprint 25 Developer
> Now: Test（H4 开发者验证完成待 Master 复核；H5 挂起） — 2026-11-20 已完成隔离冒烟、`H4-A`（`0.6.3` 新装）与 `H4-B`（`v6.0.3 → 0.6.3` 迁移），两项均含 `/compact` 压缩后承诺复注原生 hook 取证；DSH 侧 `H5` 仍待 PO 明确安全入口。
> Waiting for PO: 1. 明确可安全使用的 DSH 0.2.2-rc.5 Web/Standard 启动入口，以决定 H5 放行及 DSH 压缩后补入取证口径
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。 |
| --- | --- |

<!-- The Product Owner decides it: this Sprint's one commitment (sprint-log.md, conventions 4 and 20). -->

这一步服务[产品目标「产品化」](../ProductBacklog.md#12-product-goal)：在各自宿主里，用户不必请作者解释就能开始。范围见[六期总表](../documents/sprint-roadmap.md)的 Sprint 25；F08、F12 都归 PBI-72。以已入 main 的 `b2679aa` 为验收基线，不重做 DSH 包。PO 已定两版目标均为 `0.6.3`；Why 定案时两份清单仍为 `6.0.3`。版本目标本身不是改号、实机安装或发布的授权。

已定边界：仓库共用规则收在 `AGENTS.md`，`CLAUDE.md` 只单向 `@AGENTS.md` 导入，不循环；改 `CLAUDE.md` 仍须 PO 直接授权。DSH 如何读取共用规则、是否支持项目级 Agent 待实查，不承诺原生支持，不替 Sprint 22 实现。

### 1.2 Definition of Done

<!-- The Product Owner picks them: the Definition of Done items that matter to this Sprint (convention 5 in `product-log.md`, in the scrum-kernel skill's `conventions/` folder). The chapter ends with the Product Owner's decision on the Sprint Goal (sprint-log.md, convention 24). -->

[产品日志 §1.3](../ProductBacklog.md#13-definition-of-done) 的完整 DoD 继续生效。下列是本期核验重点，未列到的标准并不豁免。

| 现行 DoD 中的本期重点 | 要有的证据 |
| --- | --- |
| 无死链 | 中英 README、快速上手、版本与维护说明的内部链接可解析。 |
| 插件校验 | Claude 严格校验留证。 |
| DSH 分发 | 自动回归、打包内容与实际安装、角色入口分别留证；两版继续共用方法论正文。 |

**目标达成还需的证据（不是新增通用 DoD）：** 两份清单与上述文档的版本、安装和迁移口径一致；实机会话里确实叫得出角色、承诺原文确实进入上下文；新装及已有 `6.0.3` 用户迁到 `0.6.3` 的适用路径都经验证。不能用包号相同或检查通过代替真实入口可用。PBI-72 的具体行为、验收条件和测试判据留到 What。

**已有证据的边界：** SeaPawn 冲刺日志 `Scrum/sprint-advisor-workspace/SprintBacklog.md` 的 PBI-061（103–114 行）记录了 Windows 上 DSH 宿主 `0.2.2-rc.5` 的 Web 安装、Standard 会话的 `/scrum-master` 入口、承诺注入和自动回归 6/6。压缩后补入只核对了宿主实现，未单独实跑；PO 真实任务试用未做，验收暂缓。复用旧证据前要核对适用环境与实现差异；它不是 `0.6.3` 的新测试报告。本期取证参考[无头回归测试手册](../documents/headless-testing.md)，本回合未运行。

PO 决定（2026-11-20，SeaPawn）：采纳 Sprint Goal「换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。」与本期 DoD 核验重点。PO 原话：「可以继续往下走吧。呃，放行，然后进入 what 阶段。」此次只放行 What。

## 2. What

### 2.1 Product Backlog Items

<!-- The Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little. The selected items, copied word for word from the product log (sprint-log.md, convention 5). -->

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-72 | DSH 分发：验收与跨宿主维护说明 | 作为用 DeepSeek Harness 的 solo 开发者，我想要同一套方法论也能装进 DSH，以便换宿主不换流程 | 分发：Claude Code + DSH | M |

### 2.2 Refinement

<!-- The Scrum Master leads. What refinement settled, each point with who decided it; the acceptance criteria; the tests' method and pass lines (sprint-log.md, conventions 6 and 13). The chapter ends with the Product Owner's decision that refinement is over (sprint-log.md, convention 24). -->

**已定范围（PO；见 §1、六期总表和产品日志）：** 以 `b2679aa` 为基线验收现有 bundle，补齐用户和维护说明；Claude Code 与 DSH 均用 `0.6.3`；保持一份共用方法论正文和一份共用仓库规则。不重做包、不改方法论。Sprint 25 只验安装后入口和上下文，Sprint 24 管加载规矩与 hook 优化；整合改变相关行为就重验。DSH 的项目级 Agent 能力结论交 Sprint 22 参考，本期不实现、两期不互等。

**证据缺口：** 现有 [DSH 适配器](../../dsh/index.js) 只注册角色、内核和承诺上下文，不负责查找 `AGENTS.md`。本轮未找到可核对的 DSH 宿主源码；`.agents/skills` 的旧记录也不是项目级 Agent 的证据，两项都不能先写成原生支持或不支持。

**精化视角：** 以 §2.1 的原条目为视角，用 IDEO 的 How Might We Questions 把「换宿主不换流程」落到四件事：怎样让新人第一次就找到入口？怎样让已安装的人迁移而不丢项目日志？怎样让维护者只改一次规则？怎样让读者分清实机验证与静态检查？用户要什么已有目标；宿主能不能做是待查事实，不另开设计。

**精化结果（Developer 拟，Master 审，PO 定案）。** 下列四块属于同一 PBI，不另增条目；已有实现可复用，先保留 `M`，验收若暴露需新增宿主功能则带证据回 PO 定范围，不静默扩做。

| 精化块 | 验收条件 | 后续取证与通过线 |
| --- | --- | --- |
| 1. 照说明装好、叫到角色 | 中英 README 和快速上手讲清两种宿主各自的前提、安装来源、会话类型与入口。候选版在各自宿主可新装；四个已公开角色可选，按指南叫 Scrum Master 可从示例项目进入 Planning，并在会话中取得承诺原文。 | Windows 隔离环境，每宿主至少验一条全新安装主路径：Claude Code 用与发布安装同样经过[版本缓存](https://code.claude.com/docs/en/plugins/loading#versions-and-updates)的 Git 市场夹具；DSH 走 Web 安装持久目录的本地 bundle，再开 Standard。记宿主版本、候选提交、实际加载位置及角色原生事件，逐字核承诺；文档若承诺压缩后补入，另留压缩后的证据。DSH Web 与 headless 证据不互代，模型复述不算取证。 |
| 2. 已装用户按文档迁移 | Claude Code 既有 `6.0.3` 市场安装和 DSH 旧本地 `6.0.3` link 各有可复现路径；迁移后加载的确是候选版，项目日志仍在。普通更新若不接受降号，说明只列实测成功的替代路径及影响；不把旧 DSH 本地包写成公开旧版。 | 每宿主至少验一条 `6.0.3 → 0.6.3` 完整迁移：Claude Code 以 `v6.0.3` 的市场安装为旧端，DSH 以 `b2679aa` 的旧本地安装为旧端。核前后实际加载版本与文件来源（Claude 缓存路径、DSH 实际链接或复制到的位置），重开会话再验角色和承诺，核对样例日志未变。Claude `--plugin-dir` 或本地目录市场不算市场迁移，DSH 只改清单或旧会话仍在用旧内容不算成功。 |
| 3. 一处维护仓库规则 | `AGENTS.md` 是共用规则的唯一正文；`CLAUDE.md` 单向 `@AGENTS.md`，无循环、不重复写、不丢规则。维护说明分别写清 Claude 的导入方式与 DSH 在所测版本如何使用这份文件；不把 `.agents/skills` 或插件角色入口当成项目 Agent。 | 在无私人配置的样例项目用不同标记确认两宿主实际读到哪份规则。DSH 若不自动读取，需验证能用同一文件的路径；若没有可行的单源路径，带证据回 PO，不把它判过。项目级 Agent 另列宿主版本、可追溯来源和已核结论，未证实就标明，不加功能。改本仓库 `CLAUDE.md` 仍须 PO 直接授权。 |
| 4. 版本与维护资料对得上 | 两份清单、中英 README 的插件版本和版本说明口径都是 `0.6.3`；双语快速上手及维护说明和实测路径一致，链接可达；明确 DSH 宿主号不是插件号。两版包都消费同一源正文，而不是维护第二份。 | 对同一候选留四份结果：Claude 严格校验通过、DSH 自动回归通过、DSH 打包清单包含入口和运行所需资源、文档对照与相关链接检查通过。核对 `CHANGELOG.md` 区分候选与已发布历史，不把改号当发布。对照打包清单与源码，旧 6/6 只当基线。 |

**Developer 复述：** 用户能按各自说明装好并迁移，叫出角色、看到同源方法论与承诺进入会话；维护者只改一份共用规则，也知道哪些 DSH 能力尚未验证。后续依[无头回归测试手册](../documents/headless-testing.md)在隔离环境取证，判据先定、结果出来不改通过线。旧实机记录只覆盖旧环境；文档若保留压缩后补入的说明，证据要与首次注入分开，未实跑不标成已验。此处仅拟判据，未测、未安装、未改号。

**Master 审阅（2026-11-20）：** 四块判据无必改项，目前没有须另请 PO 裁定的范围取舍。DSH 能力未经证实不写成已支持；若无共用规则单一来源的可行路径，或确需新增宿主功能，再带证据交 PO 定范围。

PO 决定（2026-11-20，Master 转达）：原话「可以，我觉得23、25可以结束 what，然后去放行到 how。」PBI-72 精化收口，放行 How 规划，不放行施工。决定时的 Sprint Goal 原文：「换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。」

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

以下每项至多一会话。H1–H3 等施工放行；H4–H5 等 PO 放行 Test。通过线沿用 §2.2。

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 核实宿主能力，备好双宿主取证环境 | DSH 规则读取与项目级 Agent 的版本化调查记录；隔离的 Windows 测试环境与旧版基线。 | Claude 市场旧版与 DSH 旧本地安装各有明确来源；环境不依赖作者配置或项目。区分 DSH 查到的事实和待实机确认的行为；项目级 Agent 的结论交 Sprint 22，不实现功能。 |
| H2 | 归并仓库规则，备齐用户和维护文档 | 一份 `AGENTS.md` 共用规则、单向导入，中英 README／快速上手及维护与迁移说明候选。 | 逐条核对既有规则无丢失、不重复、无互引；修改 `CLAUDE.md` 有 PO 对执行会话的直接授权。文档提纲及全文按约定交审；未证实的宿主行为不写成事实。 |
| H3 | 单独改号，锁定候选 | 两份清单和中英 README 版本同步为 `0.6.3`，版本说明与候选提交可追溯。 | 内容与改号分开提交；宿主版本与插件版本不混用，已有发布历史不改，候选不写成已发布。两宿主仍共用原方法论正文。 |
| H4 | 验 Claude Code 的新装与迁移 | Git 市场缓存安装、`6.0.3 → 0.6.3` 迁移、实际加载位置、角色／承诺与规则导入的证据，另有严格校验结果。 | 候选在干净和旧装环境都经市场路径实际加载；角色、承诺及项目日志保全按 §2.2 核对。不用本地目录市场或 `--plugin-dir` 代替迁移。 |
| H5 | 验 DSH 的新装与迁移，合并证据交审 | DSH Web／Standard 实机记录、回归与包清单；双语文档和完整 DoD 的核对摘要。 | 新装和旧本地安装迁移都确认来源、版本、角色、承诺及日志保全；两宿主能使用同一份规则，DSH 项目 Agent 能力单列。只发布经证据支持的说明；自动检查、打包与实机结果分别记录，交 Master 对照 §2.2 和 DoD 审阅。 |

**Key choices**

- 验收现有 bundle，不重造包。Claude 用经过版本缓存的 Git 市场夹具，DSH 用 Web 本地安装和 Standard 会话。安装前后查实际加载的文件与原生会话事件，不能靠包号或模型复述；压缩后补入若仍写在文档里，另留证据。
- `AGENTS.md` 持有共用正文，`CLAUDE.md` 只单向导入。中英 README 与快速上手只写实际用户路径，维护细节不塞进 README。Sprint 25 管分发、版本与安装文档；README／快速上手若涉及 Sprint 23 的约定表述或 Sprint 24 的角色加载、承诺行为，先与 Master 对齐相关改动及基线，不替其他期改规矩；整合后重验受影响项。

**Risks and open points**

- 两宿主是否接受降号尚无当期证据。普通路径失败先在隔离环境验替代路径；没有可重复的迁移路径，或 DSH 不能使用同一份共用规则，带证据回 PO，不降通过线、不擅自新增宿主功能。
- 旧 DSH 记录不是目标版本的证明。若没有可安全使用的 DSH Web／Standard 实机环境，报告缺口，不拿 headless 冒充，也不操作 PO 的常用配置。测试前锁定基线与判据，原始会话记录留在仓库外，日志只写结果摘要。

**Master 审阅（2026-11-20，`c568270`）：** H1–H5 与 §2.2 一致，无必改项。降号迁移、DSH 共用规则和实机取证的停点保留；未经验证的宿主能力和迁移路径只作候选，不写成公开承诺。即使获准施工，改 `CLAUDE.md` 仍须 PO 直接授权执行会话；改号只调候选，不改已发布历史；安装与实机测试另等 Test 放行。

Go-ahead（2026-11-20，SeaPawn）：原话「可以放行吧。」按已审计划放行本工作树 H1–H3 和相应本地检查点。`CLAUDE.md` 仍须直接授权；安装、正式测试及 H4–H5 另等 Test 放行。不合并、不打 tag、不推送、不发布。决定时的 Sprint Goal 原文：「换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。」

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

| 工作项 | 2026-11-20 检查点 |
| --- | --- |
| H1 | [宿主证据与验收样例](host-evidence.md)已记固定版本的官方源码（`dsh-v0.2.2-rc.5` 提交 `9c2670d`）、两条旧安装基线（`v6.0.3` `d681c69`、`b2679aa`），以及待批的 Test（H4–H5）隔离白名单、4 组运行矩阵（`H4-A`/`H4-B`/`H5-A`/`H5-B`）、完整样例夹具、外部原始留证路径（`S:\IDEO-Scrum-Archives\sprint-25-dsh-docs\test-runs\`）、预算上限（单次最多 6 轮、单步 ≤ 120 秒）、压缩后补入界定与停点。当前 `PATH` 无 `dsh`；专用 Web／Standard 环境未启动，不能以源码或旧实跑当本期实机证据。 |
| H2 | 1. **根规则原样迁移（PO 直接授权本执行会话，提交 `90aff9a`）**：`HEAD:CLAUDE.md` 原样迁至 [`AGENTS.md`](../../AGENTS.md)（5691 字节，blob `65e2c4e`，SHA-256 `f397cccd...`），[`CLAUDE.md`](../../CLAUDE.md) 仅留单向导入 `@AGENTS.md`（11 字节，blob `43c994c`，`AGENTS.md` 无 `@CLAUDE.md` 循环引用）。<br>2. **中英维护说明送审稿**：按 [docs-review.md](docs-review.md) 已审大纲（H1 + 4 H2）写成 [`docs/maintaining.md`](../../docs/maintaining.md) 与 [`docs/maintaining.zh-CN.md`](../../docs/maintaining.zh-CN.md)，严格区分官方源码、历史基线与待测项。中英 README 与双语快速上手保持未改，待 Master 审阅全文及实机 Test（H4–H5）通过后再落地。 |
| H3 | 单独提交 `2800cc0`：两份清单、中英 README 与 CHANGELOG 的 Unreleased 条目同步为 `0.6.3`；未改已发布历史或 DSH 宿主版本。等 H2 的文档全部定稿，再锁定最终取证候选。 |

静态与结构核验（未装插件、未跑实机模型测试）：`claude plugin validate --strict plugins/ideo-scrum`、`node --test scripts/check_dsh.mjs`、`npm pack --dry-run --json --ignore-scripts`、`python -X utf8 -I scripts/check_docs.py`（及 `--selftest` 与附带 `docs/maintaining*.md` 的对等／链接检查）、`python -X utf8 -I scripts/board_check/check.py selftest` 待最终提交前全部核验并留证于交付报告；H4–H5 安装、降号迁移与实机角色／承诺／规则加载取证仍未执行，待 Master 审阅并决定是否放行 Test。

**PO 委托（2026-11-20，UTC+8，Master 转达）：**「现在他们全部都开跑了，这样子我跟你讲。嗯，每一个对话，我现在给你权限，每一个对话，等到他们 review 之前向我报告就可以了。不意是每一个对话哦。因为他们现在都已经开始跑了。」

Sprint 21–25 的 Review 前阶段门和常规事项交 Master；本期安全隔离、安装前置与证据方案齐备后，请 Master 决定是否进入 Test。目前尚未放行。更改 Product Goal、取消 Sprint、推翻 PO 决定、PO 点名的品味、正式 Review／Retro／收官及推送发布仍交 PO；本仓库 `CLAUDE.md` 仍须 PO 直接授权实际执行会话。这不扩大任何工具权限或提交、安装范围。

**Master 审阅与 Test 阶段门裁定（2026-11-20，依 PO 对 Sprint 21–25 Review 前阶段门委托）：** 已审 `90aff9a`、`ab4061c` 与 `2800cc0`；核对静态／单元测试全过，`docs/maintaining*.md` 与 `host-evidence.md` 当前无必改项（草稿提示、`PAIRS` 并入、README／快速上手定稿同步留待 H2 最终收口）。决定时的 Sprint Goal 原文：「换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。」
- **放行 `H4`（仅 Claude Code 侧 `H4-A` 新装、`H4-B` `v6.0.3 → 0.6.3` 迁移与至少一组的 `/compact` 压缩后承诺复注取证）**：先跑最小隔离冒烟（确认 Git 市场仅写入独立 `CLAUDE_CONFIG_DIR` 零写入 `~/.claude`、`/context all` 无上级或用户指令文件、`claude-magpie` 白名单隔离、`commitments.sh` 显式设本轮独立 `TMPDIR` 且 `sh` 来自 Git for Windows 而非 WSL）；`H4-A`/`H4-B` 均走经过版本缓存的 Git 市场夹具（不用 `--plugin-dir` 或本地目录市场替代迁移），原始流存仓外 `S:\IDEO-Scrum-Archives\sprint-25-dsh-docs\test-runs\`，入仓只留脱敏汇总。
- **暂不放行 `H5`（DSH `0.2.2-rc.5` 侧）**：前置缺口已报 PO；在 PO 明确安全入口前，不探测或触碰 PO 常用 DSH 配置、不擅自安装 `dsh`、不用 `dsh --profile headless` 冒充 Web／Standard。H4 期间暂不修改 README／快速上手／`check_docs.py` 及 `CLAUDE.md`，不降通过线，不进正式 Review、合并、打 tag、推送或发布。

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->

### Developer Test · Claude Code `H4`（2026-11-20，待 Master 复核；DSH `H5` 挂起）

**结论：Claude Code 侧 `H4`（隔离冒烟、`H4-A` 新装 `0.6.3`、`H4-B` `v6.0.3 → 0.6.3` 迁移、两项 `/compact` 压缩后承诺复注、`AGENTS.md` 单向导入与 `scrum/` 逐字节保全）全部通过；常规 `claude plugin marketplace update ideo-scrum` + `claude plugin update ideo-scrum@ideo-scrum` 在 Claude Code `2.1.329` 上直接完成 `6.0.3 → 0.6.3` 降号更新，无需卸载重装。唯一剩余缺口为 DSH 侧 `H5`（待 PO 明确安全入口）。**

- **环境与模型口径**：被测提交 `119e4af`（`plugins/` 与 `ab4061c`/`2800cc0` 相同，候选 `0.6.3`）；旧基线 `d681c69`（`v6.0.3`）。宿主 Claude CLI `2.1.329`；模型通道 `claude-magpie`（magpie 的便宜模型，非 Haiku）；进程使用白名单环境变量、中性父目录 `C:\Users\Public\s25-test\`、各运行独立 `CLAUDE_CONFIG_DIR` 与 `TMPDIR`、仅放开 `Read,Grep,Glob,Skill`（禁用 `Bash,PowerShell,Write,Edit,Agent`）、`--strict-mcp-config --permission-mode dontAsk`，并在各配置目录 `settings.json` 挂载 `scripts/stranger_test/guard.py`（未传冲突 `--settings`）。仓外原始流与清单快照：`S:\IDEO-Scrum-Archives\sprint-25-dsh-docs\test-runs\H4-A\` 与 `H4-B\`。
- **冒烟与隔离实测纠偏**：
  1. **Git 市场形态**：本机用仅监听 `127.0.0.1` 的 `git-http-backend` 提供裸仓 URL（`known_marketplaces.json` 记为 `"source": "git"`），使 `add`/`update` 真实走 `git clone` 与版本缓存，区别于 `"source": "directory"`。
  2. **`--setting-sources` 与用户插件加载**：冒烟（`C:\Users\Public\s25-test\smoke-03\`）证实 `claude plugin install` 默认写 `user` 作用域（`CLAUDE_CONFIG_DIR\settings.json` 的 `enabledPlugins`）；若传 `--setting-sources project,local`，会话不会挂载 `ideo-scrum`。因本测试已完全隔离 `CLAUDE_CONFIG_DIR`，故先以 `--setting-sources user,project,local` 跑 `/context all` 证清白（`Memory Files: []`），再以同一隔离范围跑正式会话（与 `scripts/stranger_test/driver.py` 一致）。
  3. **POSIX `sh` 与状态文件隔离**：清洁 `PATH` 命中 `E:\GIT\Git\usr\bin\sh.EXE`（非 WSL）；`commitments.sh` 的 `.fp` 状态写入各运行独立 `CLAUDE_CONFIG_DIR\plugins\data\ideo-scrum-ideo-scrum\ideo-scrum-commitments\*.fp`，零触碰共享 `/tmp`。
  4. **真实 `~/.claude` 核对**：`H4-A` 全程 `plugins/` 与 `settings*.json` 差异为 `0`；`H4-B` 中真实 `~/.claude` 未出现 `0.6.3`、未改任何清单或设置（仅并行其他会话的两个短生命周期 PID 在宿主机原有插件缓存下留下了 `.in_use/` 锁文件）。

| 运行 | 隔离 `/context all` | 市场与缓存加载（来源／版本） | 角色、内核与原生 hook | `/compact` 压缩后复注 | 规则与日志保全 |
| --- | --- | --- | --- | --- | --- |
| `H4-A`（新装 `0.6.3`） | 放规则前 `[]`；放后仅加载 `proj\CLAUDE.md`（23 tok）与 `proj\AGENTS.md`（32 tok） | `git` 市场安装；`claude plugin list` 与会话 `init` 均指向 `...\H4-A\...\cache\ideo-scrum\ideo-scrum\0.6.3`（`0.6.3`，`d627d118`） | `init` 见 4 角色与 4 内核；`/ideo-scrum:scrum-master` 按序调 `Skill`（`ideo-kernel` → `scrum-kernel` → `sprint-kernel`）并进入 Why/Planning；`SessionStart:startup`（`exit_code: 0`）注入 3 条原文承诺 | `compact_boundary`（`manual`）后触发 `SessionStart:compact`（`exit_code: 0`），再次注入 3 条原文承诺；第 3 轮模型完整复核承诺与规则 | 回应原文引用 `S25-SHARED-RULE: Preserve the sample logs.`；`scrum/` 前后 SHA-256 一致、`git status` 干净 |
| `H4-B`（`v6.0.3` → `0.6.3` 迁移） | 放规则前 `[]`；放后仅加载 `proj\CLAUDE.md`（23 tok）与 `proj\AGENTS.md`（32 tok） | **迁移前**：`d681c69` 市场安装，`list` 与 `init` 为 `...\6.0.3`（`6.0.3`，`d2af0a6b`）。**迁移**：推 `0.6.3` 到夹具市场后跑 `marketplace update` + `plugin update`，直接返回 `updateOutcome: "updated"`（`6.0.3 → 0.6.3`）；`list` 与新会话 `init` 切至 `...\0.6.3`（`0.6.3`，`e2d99a21`），无需卸载重装 | 迁移前 `6.0.3` 与迁移后 `0.6.3` 新会话均可见 4 角色与 4 内核；新会话 `/ideo-scrum:scrum-master` 按序调 3 个内核并进入 Planning；`SessionStart:startup`（`exit_code: 0`）注入 3 条原文承诺 | `compact_boundary`（`manual`）后触发 `SessionStart:compact`（`exit_code: 0`），再次注入 3 条原文承诺；第 3 轮模型完整复核承诺与规则 | 新会话引用 `S25-SHARED-RULE: Preserve the sample logs.`；迁移及两段会话前后 `scrum/` SHA-256 逐字节一致、`git status` 干净 |
