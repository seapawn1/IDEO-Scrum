# Sprint Backlog — Sprint 25 (dsh-docs)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: claude/sprint-25-dsh-docs-4f4070 | Product Owner: SeaPawn | Scrum Master: IDEO-Scrum Master | Developer: Sprint 25 Developer
> Now: How — 2026-11-20 PO 结束 What、放行 How 规划；计划已拟，待 Master 审阅。
> Waiting for PO: 1. Master 审阅后，是否给 §3 计划施工 Go-ahead；2. 是否单独直接授权修改本仓库 CLAUDE.md
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。 |
| --- | --- |

<!-- The Product Owner decides it: this Sprint's one commitment (sprint-log.md, conventions 4 and 20). -->

这一步服务[产品目标「产品化」](../ProductBacklog.md#12-product-goal)：在各自宿主里，用户不必请作者解释就能开始。范围见[六期总表](../documents/sprint-roadmap.md)的 Sprint 25；F08、F12 都归 PBI-72。以已入 main 的 `b2679aa` 为验收基线，不重做 DSH 包。PO 已定两版目标均为 `0.6.3`；两份清单仍为 `6.0.3`，版本目标不是改号、实机安装或发布的授权。

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

Go-ahead: 待 PO 明确放行施工并注明范围。目前只放行 How 及本期日志的本地检查点；不改号、不改 `CLAUDE.md` 或其他交付物、不安装、不作正式测试、不合并、不打 tag、不推送、不发布。

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again (sprint-log.md, convention 16). The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
