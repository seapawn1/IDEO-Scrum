# Sprint Backlog — Sprint 23 (log-rules)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-23-log-rules-4b3ec9` | Product Owner: SeaPawn | Scrum Master: Sprint 21–26 主会话 | Developer: Sprint 23 工作树会话
> Now: Increment · 2026-11-21 PO Review 前全权委托（原话见 §4），Master 二轮复核 18 份拟稿全部通过并放行 H10。18 份已审稿已逐字落源并作本分支本地提交（自检全绿）；最后一轮流程 Test 方案已拟、待 Master 冻结与放行，正式 Test 未运行。
> Waiting for PO: 1) 正式 Review 前的报告，含 Designer Identity 替换句的最终合入确认；2) 正式 Review／Retro／收官及合并、tag、推送、发布仍回 PO。当前无需 PO 立即处理的事项。
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md` in the scrum-kernel skill folder, convention 16).

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 照着日志接手：接手的人能分清承诺原文和定目标的理由，查到本期重点验什么、完整 DoD 是否满足，以及下一步是否已获 PO 放行；收尾后，能找回选定和否决方案的依据，也能在项目记忆里逐条找到 Retro 的重要教训。 |
| --- | --- |

<!-- The Product Owner decides it: this Sprint's one commitment (sprint-log.md, conventions 4 and 20). -->

这是项目级目标，不是六期汇总。接手者不必靠作者口述，就能接续已有的工作，呼应[产品目标](../ProductBacklog.md#12-product-goal)中让懂 Scrum 的人照文档走完第一个冲刺的方向。范围来自[六期总表的 Sprint 23 行](../documents/sprint-roadmap.md#六期分工)及[反馈对账](../documents/sprint-roadmap.md#反馈对账) F02、F09、F10、F11、F13。目标里的「完整 DoD 是否满足」要靠证据区分已核验与待核验，Planning 不预记为已通过。

### 1.2 Definition of Done

<!-- The Product Owner picks them: the Definition of Done items that matter to this Sprint (convention 5 in `product-log.md`, in the scrum-kernel skill's `conventions/` folder). The chapter ends with the Product Owner's decision on the Sprint Goal (sprint-log.md, convention 24). -->

[产品日志 §1.3](../ProductBacklog.md#13-definition-of-done) 的完整 DoD 持续生效：Outcome Done 衡量产品价值，Output Done 是整个增量的质量标准。本期沿用 Why 草案的取证重点，未列项不豁免，尚无测试结果。

| 核验重点 | 核验标准 |
| --- | --- |
| 内容忠实与一致 | 分清 Scrum 等来源原文、作者约定和 PO 决定；受影响的约定与模板说法一致。涉及第三方摘录，核对 `Source`、`License` 两行与 `ATTRIBUTION.md` 一致。 |
| 可导航、无死链 | 受影响的参考材料从 `SKILL.md` 入口至多两跳可达，相关 Markdown 内部链接可解析。 |
| 插件校验与 DSH 回归 | `claude plugin validate --strict plugins/ideo-scrum` 与 `node --test scripts/check_dsh.mjs` 均需通过；只有改动分发才专项验证实际安装与角色入口。 |

**2026-11-19 · Why 决定**：PO 原话「差不多这个goal，可以再明确些，然后放行 What」。Scrum Master 按 PO 要求定稿，PO 放行 What，不含 How 或施工。§1.1 承诺原文：「照着日志接手：接手的人能分清承诺原文和定目标的理由，查到本期重点验什么、完整 DoD 是否满足，以及下一步是否已获 PO 放行；收尾后，能找回选定和否决方案的依据，也能在项目记忆里逐条找到 Retro 的重要教训。」

## 2. What

### 2.1 Product Backlog Items

<!-- The Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little. The selected items, copied word for word from the product log (sprint-log.md, convention 5). -->

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-76 | DoD：区分质量标准与本期核验重点 | 作为 PO，我想在 Sprint 里挑出需要重点核验的项，同时明确整个增量的质量标准，以免漏选被当成豁免 | Map ④、⑦ | 待估 |
| PBI-77 | 进入或返回阶段前等 PO 放行 | 作为 PO，我想先组织这轮怎么发散，并在各阶段入口决定是否开始，以便 AI 不因我认可前一阶段就自行施工或做原型 | Map ④、⑤、设计阶段 | 待估 |
| PBI-78 | 日志：承诺的解释与 Goal 写法 | 作为熟手，我想分清承诺原文、它的理由和不同层级 Goal 的写法，以便接手日志时知道为何这样定 | Map ③、④、设计日志 | 待估 |
| PBI-79 | 设计收尾保留工作材料 | 作为 PO，我想重看被否决的方案和评审依据，以便新证据出现时能重新判断 | Map「设计冲刺」、⑧ | 待估 |
| PBI-69 | Retro 只存要点，一条一条进记忆 | 作为熟手，我想要 Retro 只把要点一条一条存进记忆、非要点丢掉，以便记忆里都是用得上的教训，不是每个冲刺一份大杂烩 | Map ⑨ | S～M |

### 2.2 Refinement

<!-- The Scrum Master leads. What refinement settled, each point with who decided it; the acceptance criteria; the tests' method and pass lines (sprint-log.md, conventions 6 and 13). The chapter ends with the Product Owner's decision that refinement is over (sprint-log.md, convention 24). -->

**PBI-76 · 首轮精化**

- **视角（§2.1 原文）**：「作为 PO，我想在 Sprint 里挑出需要重点核验的项，同时明确整个增量的质量标准，以免漏选被当成豁免」
- **精化问题**：怎么让接手的人查清本期重点验什么，同时看得出其他仍适用的质量标准有没有证据？
- **已定意图（PO，六期总表与产品日志）**：完整 DoD 继续适用；本期选的是取证重点，不是豁免。只对一个 PBI 成立的额外条件写进该 PBI 的验收条件，不新增通用 DoD。

**Master 判据（2026-11-19，据原文澄清，不是 PO 原话）**：

- 所有适用的 Output Done、本期条目验收，以及本次 Test 约定的审阅和验收，均须有有效证据且通过。如果事前未要求本次 Test 取得某个产品 Outcome 信号，可以写「本期增量检验通过；产品价值信号 X 待观察」。保留指标，可注明何时、据何观察。「待观察」不是已通过、不适用或价值已实现，也不能据此写「全套 DoD 已通过」。已有反证时，记为未达，说明影响，不写成待观察。
- 如果 Sprint Goal、明确的条目 Outcome Criteria 或 Acceptance Criteria、或其他事前约定的过线条件要求本次 Test 取得该信号，缺证据就是该要求待证，本期整体 Test 不能判通过，不能事后改成以后观察。有效证据若表明所有适用 Output Done 均已满足，增量质量仍可单列为通过。Test 即使通过，也不自动收官，仍由 PO 决定。

依据：SGEP 的[增量质量与后续价值验证](../../plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-increment.md#commitment-definition-of-output-done)、[产品成果的可观察证据](../../plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-product.md#commitment-definition-of-outcome-done)、[条目验收和结果判据](../../plugins/ideo-scrum/skills/scrum-kernel/references/scrum-artifact-product-backlog.md#acceptance-criteria)，以及[冲刺约定的 Test 第 13、15、16 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#test)。这些是本项的判据，不改产品 DoD。

| 核验场景（未运行） | 过线条件 |
| --- | --- |
| 正例：读同一份样本 Sprint 的 Planning 与 Test 记录 | 能追溯产品完整 DoD，区分本期需新取证和 Test 中实际取得的新证据；能查到哪些既有证据仍有效、证据在哪里、为何仍适用；对条件未触发的项明确写出条件和原因。遗漏、待核验、条件未触发、已通过彼此不能替代。 |
| 反例：样本中有一项仍适用的质量标准，没选为本期重点，也无有效证据 | Test 不得因没有选中该项而判通过；该项也不得写成「条件未触发」。 |
| 价值信号正例：只改日志说明，本期事前未要求重验「陌生人走完首个冲刺」 | 若其余过线条件均有有效证据且通过，可以记增量检验通过、该信号待观察。已有反证则记录未达及影响。 |
| 价值信号反例：本期目标或验收明确要求在 Test 证实「陌生人走完首个冲刺」，但未取得观察证据 | 该要求待证，不能报本期整体 Test 通过，不能事后延为待观察；增量质量可按有效证据单独判定。 |

- **Developer 暂估**：M（3～5 个工作会话）。两块验收边界：Planning 与 Test 能按同一质量标准解释取证；样本与反例能让接手者核对判定。§2.1 保留产品日志的原始规模。

**PBI-77 · 首轮精化（2026-11-20 Master 审阅无必改项）**

- **视角（§2.1 原文）**：「作为 PO，我想先组织这轮怎么发散，并在各阶段入口决定是否开始，以便 AI 不因我认可前一阶段就自行施工或做原型」
- **精化问题**：怎么让接手的人从日志看清哪些阶段可以开始、哪些还要停下来，不把已经放行的阶段内续接也拦住？
- **已定意图（PO，阶段门临时修正及总表 F09）**：首次进入或返回阶段前等 PO 明确放行；认可上一阶段不能自动放行下一阶段。Ideate 发散前先由 PO 组织本轮怎么发散。阶段门是本插件约定，不是 Scrum Guide 或《Sprint》的原文；不把 F09 记录里的页数、方法数和分线数建议加成放行条件。
- **验收边界建议**：覆盖 Sprint 的 Why、What、How、施工以及设计五个阶段，保留现有的 Sprint Test 入口和回退决定。跨阶段前，日志能查到目标阶段、放行依据和范围；没有明确放行就停在当前阶段，可以说明结果、提议本轮发散怎么组织或请求决定，但不产出下一阶段工作、不委派它。只授权选方案或审阅不等于授权过关；明确说出两件事的一条消息可同时认可上阶段并放行下一阶段。书面交接只按 PO 明确给出的范围执行，不从阶段内授权推断放行权。

| 核验场景（建议，未运行） | 可观察的通过线 |
| --- | --- |
| How → 施工 | PO 只认可计划，日志仍显示等施工放行，不改交付物、不启动施工会话；明确放行后才施工，且不越过授权的提交、合并、推送等边界。 |
| Increment → Sprint Test | 只认可增量，不启动 Sprint Test；PO 明确放行后才进入。施工授权范围内的自检不等于进入 Sprint Test。 |
| Define → Ideate | PO 只认可问题定义，或虽说开始 Ideate 但本轮发散组织仍未定，AI 先请 PO 定组织方式，不发散、不画草图、不派发构思任务；组织方式已明确且获放行后才开始。不以固定的方法数充当放行证据，也不在本项改写现有方法约定。 |
| 选方案 → Prototype | PO 只选定方案，可以记结果，不做原型；明确放行 Prototype 后才做原型，原型放行不等于施工。 |
| 返回已做过的阶段 | 测试结果显示需要回到另一个阶段时，先报问题并等 PO 决定要不要回、回哪一阶段，不拿上一次放行当本次授权；获明确放行后才返回并记录范围。已授权范围内的同阶段调整不算回退。 |
| 同阶段接手 | 只换会话、工作仍在已明确放行的同一阶段和范围内，可按日志继续；没有放行记录时，不把 `Now`、角色交接或审阅通过当作批准。 |

- **Developer 暂估**：M（3～5 个工作会话）。两块验收边界：Sprint 和设计日志能说清同一放行规则；首次进入、返回和同阶段接续的对照样本能查到行动与授权的先后。§2.1 保留原始规模，不预定模板新增字段或实现方式。

**PBI-78 · 首轮精化（阶段决定行语义已由 PO 确认）**

- **视角（§2.1 原文）**：「作为熟手，我想分清承诺原文、它的理由和不同层级 Goal 的写法，以便接手日志时知道为何这样定」
- **精化问题**：怎么让接手者读到同一份承诺和它的理由，同时分清汇总级条目与项目级统一目标，而不靠作者口头解释？
- **已定意图（PO，六期总表、产品日志及 F10、F13）**：承诺原文一份，表下允许解释设定理由，解释不是承诺的一部分；汇总级可按条目列，项目级写统一价值目标。两点分别核对；已有等价说明不重复添加，不要求每个承诺都写说明。
- **PO 决定（2026-11-20，Master 转达）**：PO 同意 Master 的建议：「承诺表是唯一权威来源，阶段决定行副本只是审计快照；保留阶段门先读、再核对，决定行留当时原文快照。」`overview.md` 第 17 条不在页头另存承诺，与 `sprint-log.md` 第 24 条、`design-log.md` 第 26 条在决定行保留当时原文不冲突。此前「只引用表格」的建议不采用。本日志既有 Why 决定行与插件源约定均不改。

| 核验场景（未运行） | 可观察的通过线 |
| --- | --- |
| 产品日志 §1.1、§1.2，Sprint 日志 §1.1，设计日志 §1.2：有解释与无解释两种样本 | 都能定位承诺表中的原文；有解释时能分清理由与承诺，无解释不判缺项。相关约定、三类日志模板对解释落点的说法一致；解释可留在承诺所在的小节，不因旧指引被强制移入 Increment notes；不要求新设解释小节。 |
| 只增删或改写表下解释，承诺未获变更授权 | 承诺原文逐字不变；不把解释里的愿望或范围扩展当成已批准的目标，不把解释并入承诺提取结果。 |
| 汇总／索引级与项目级 Sprint 对照 | 汇总级可以在同一承诺中按条目列清各线；项目级围绕一个统一价值目标，不把每个 PBI 分别立成互不相干的 Goal。不按句数、分号数或是否列点机械判定。 |
| Sprint 与设计的权威承诺、阶段决定行快照对照 | 承诺表是唯一权威来源；不在页头或说明里另立一份承诺，引用能回到承诺表。过阶段门前从表中逐字读取原文，再对照目标核对本阶段；决定行保留当时的原文，只作审计快照。读不到原文不能有效过关；只留链接或摘要不代替快照。若 PO 后来改变目标，旧快照仍保留当时文字，不替代当前承诺表。 |

- **Developer 暂估**：S～M（约 2～3 个工作会话）。两块验收边界：承诺与可选解释能清楚区分；两类 Goal、权威承诺及审计快照能用对照样本验证。§2.1 保留产品日志原始规模，不预定表格编码、模板新字段或提取实现。

**PBI-79 · 首轮精化（2026-11-20 Master 审阅无必改项）**

Master 审阅确认材料范围、归档节点与非 Increment 的边界；这是精化审阅结论，不是验收测试结果。

- **视角（§2.1 原文）**：「作为 PO，我想重看被否决的方案和评审依据，以便新证据出现时能重新判断」
- **精化问题**：怎么让收尾后接手的人找到选定与否决方案的原始依据，不因清理设计或承接 Sprint 的工作文件而丢失？
- **已定意图（PO，阶段材料临时修正、六期总表及 F11）**：设计中间材料全部保留，包括原型、速写、演示、评审、合成稿和被否方案；材料保留不等于列入正式 Increment。F11 中另加材料清单或「被否方案」章节的做法仍是助手建议，本项不据此预定新章节。
- **验收边界建议**：分别核对设计结束、首次归档该设计的 Sprint Review、承接其结论的 Sprint 收官。归档可以改变位置，但接手者仍能沿日志找到材料、读到原始内容；不能只剩摘要或一个要求从 git 历史恢复的 SHA。只覆盖设计材料和它们随结论转交的去向，不据此要求普通 Sprint 的所有工作文件永久保留。

| 核验场景（Developer 建议，未运行） | 可观察的通过线 |
| --- | --- |
| 设计结束：样本包含选定方案、被否方案、速写、演示、评审、合成稿与原型 | 对照样本原有文件，逐份仍可找到并读取，不能只保留胜出方案或最终结论；材料不必全文塞进日志。 |
| 首次归档 Review，以及承接 Sprint 收官后重新接手 | 两个节点分别核对材料仍存在、日志指向可解析；若移动了材料，引用随位置更新，不被通用「清理工作文件」规则再次删除。 |
| 原型有承接 Sprint／尚无承接 Sprint／结论不实施 | 三种情况下都保留设计材料；是否实施结论不决定其原始依据是否保留。 |
| 材料与交付物对照 | 保留的原型和被否方案不作为满足 DoD 的正式 Increment；真正实施的结论仍按 Sprint 的 Goal、条目验收和 DoD 检验。 |

- **现行约定待对齐（Developer 核对）**：`design-log.md` 第 19 条、`sprint-log.md` 第 17 条、`overview.md` 第 3、5 条仍有用完、归档或收官时删除的说法；设计模板也以删除后的 commit 作原型去向。不能只核对设计刚结束时没删。原型纳入保留范围有产品日志 PBI-79 的明确依据，不因总表未逐项列全而排除。
- **Developer 暂估**：M（3～5 个工作会话）。两块验收边界：跨设计与 Sprint 收尾的留存说法一致；归档前后的可找回性与非 Increment 身份分别验证。§2.1 保留产品日志原始规模；材料存放位置和迁移方式留给 How，不借此回改已完成 Sprint 的历史材料。

**PBI-69 · 首轮精化（2026-11-20 Master 确认兜底范围成立）**

Master 确认沿用现行 `sprint-log.md` 第 18 条的无宿主项目记忆兜底：仓库内逐条可找回，不建每 Sprint Retro 汇总，不写指令文件，不新增宿主能力。这里只记录范围成立，尚未运行验收。

- **视角（§2.1 原文）**：「作为熟手，我想要 Retro 只把要点一条一条存进记忆、非要点丢掉，以便记忆里都是用得上的教训，不是每个冲刺一份大杂烩」
- **精化问题**：怎么让没参加这期的人在项目记忆中逐条找到能用的教训，而不用读一份按 Sprint 打包的回顾？
- **已定意图（PO，Retro 临时修正、六期总表及 F02）**：只把重要教训一条一个存入项目记忆；不写 Retro 汇总文件，不在 Sprint 日志另设 Retro 章，不把教训写入指令文件。本仓库由 Master 列候选、PO 挑要点，一条一个记忆文件；不把本仓库的分工或路径直接写成所有项目的规则。项目教训不并入 Sprint 26 的插件约定 Memory（PBI-51）。
- **依据与验收边界**：[SGEP Retro](../../plugins/ideo-scrum/skills/sprint-kernel/events/scrum-event-sprint-retrospective.md#sprint-retrospective) 要求聚焦最有帮助的改进，并未指定存储方式；分条入记忆来自 PO 决定。[冲刺约定第 18 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#closing) 由 Developer 写教训为可复用的原则，且明确禁止 `CLAUDE.md`、`AGENTS.md` 等指令文件。无宿主项目记忆时，沿用该条允许的仓库教训笔记，不指定固定目录。

| 核验场景（Developer 建议，未运行） | 可观察的通过线 |
| --- | --- |
| 候选同时含重要教训和一般过程细节，另有一组无重要教训 | 前一组只保存重要教训，每条独立、可按主题找回；后一组不为交付而补写条目或汇总。本仓库样本按 Master 列候选、PO 挑要点。 |
| 新会话只读所需的一条项目记忆 | 能理解其适用情境、原因和可采取的原则，不依赖当期聊天或整份回顾。索引只提供逐条入口，不另存一份教训正文。 |
| 收尾后检查落点 | 不产生 Retro 汇总或 Sprint 日志的 Retro 章；即使只有一条，也不写进 `CLAUDE.md`、`AGENTS.md` 等指令文件。 |
| 同时存在设计材料和插件约定 Memory | 不以「非要点不入记忆」为理由删掉 PBI-79 要保留的设计依据；不把项目教训写入插件包或 PBI-51 的通用约定 Memory。 |
| 项目无宿主项目记忆能力（现行兜底的隔离样本） | 仓库内仍能独立找到每条教训；不按 Sprint 打包成统一 Retro 档案，不借用指令文件。用样本验证约定，不改宿主配置或真实记忆。 |

- **Developer 暂估**：S～M（约 2～3 个工作会话）。两块验收边界：只保存重要教训且能独立找回；项目记忆及现行兜底不产生汇总或混入插件 Memory。本轮只拟定判据，不对真实项目记忆执行 Retro、迁移或清理。

**2026-11-20 · What 决定（Master 转达）**：PO 原话「可以，我觉得23、25可以结束 what，然后去放行到 how。」对照 §1.1，五项精化覆盖日志接手与收尾的目标，Sprint 23 结束 What，放行 How 规划，不含施工、实测、合并、推送或发布。§1.1 当时原文快照：「照着日志接手：接手的人能分清承诺原文和定目标的理由，查到本期重点验什么、完整 DoD 是否满足，以及下一步是否已获 PO 放行；收尾后，能找回选定和否决方案的依据，也能在项目记忆里逐条找到 Retro 的重要教训。」

## 3. How

<!-- The Developer writes this chapter as a plan for making the selected items, short and not in detail (sprint-log.md, convention 7): the work items in order, each with its output and how to tell it is done; the key choices and why; the risks and open points. The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 定修订范围和交接基线 | 基于 `00c224b` 的受影响条款、模板、入口说明和跨期接口清单 | ✓ 2026-11-20 每处拟改文字能指到原文、作者约定或 PO 决定；对照命令、SKILL.md、双语 README、快速上手、词汇表与项目指令中的同义说法，标清改哪处、哪处只引用或不动。 |
| H2 | PBI-76：对齐 DoD 与取证写法 | 产品约定、Sprint 的 Why／Test 写法与模板的成套修订稿 | ✓ 2026-11-20 从同一份样本能追溯完整 DoD、需新取证、仍有效的旧证据与未触发条件。适用但缺证据不通过；Outcome 信号是否拦本期 Test 按事前约定判，不把待观察当通过或豁免。 |
| H3 | PBI-77：对齐通用阶段门与 Sprint 流程 | `overview.md` 与 Sprint 阶段门、模板的修订稿 | ✓ 2026-11-20 进入、返回与同阶段接手三种情况分得清；认可 How 不授权施工，认可增量不授权 Sprint Test；可追溯放行人、目标阶段与范围。 |
| H4 | PBI-77：对齐设计阶段门 | 设计约定与模板的修订稿 | ✓ 2026-11-20 进入和返回都须明确放行；书面交接仅在 PO 明授的范围内有效，不因 Prototype／Test 可以由 AI 承担而省略阶段门。Ideate 的组织方式由 PO 先定，选定方案与放行 Prototype 分开；不新增方法数门槛，不改设计日志既有字段。 |
| H5 | PBI-78：对齐承诺与解释 | 三类日志的承诺说明及项目级／汇总级 Sprint Goal 对照样本 | ✓ 2026-11-20 表内原文唯一权威，表下解释可选且不参与提取；过关先读再核对，决定行留当时原文快照。汇总级条目列在同一单行承诺格内；保留两列表形状和既有标题，不改解析器。 |
| H6 | PBI-79：设计结束时保留依据 | 设计材料的保留与交接规则、原型去向说明 | ✓ 2026-11-20 选定与否决方案、原型、速写、演示、评审及合成稿仍从日志可找回；是否有承接 Sprint 不决定删除，留存不计作正式 Increment。 |
| H7 | PBI-79：让归档和 Sprint 清理保住材料 | 设计归档与承接 Sprint 收尾的修订稿 | ✓ 2026-11-20 首次归档 Review 和承接 Sprint 收官后都能按有效引用读回原件；档案不被误认成开着的设计，通用「过期即删」和工作文件清理不再删去保留材料。本次规则约束以后收尾，不回迁历史。 |
| H8 | PBI-69：项目 Retro 分条入记忆 | Retro 约定修订稿与正常／兜底对照样本 | ✓ 2026-11-20 只保存重要教训且每条可独立找到；没有重要教训不凑数。无宿主项目记忆时沿用仓库教训笔记；通用工作材料规则不能让 Retro 教训写进指令文件，不建每期汇总，不混入插件约定 Memory。 |
| H9 | 交审成套修订稿 | 可圈阅的全文、§2.2 判据对照和跨期交接记录 | ✓ 2026-11-20 五项各有正反例或必要分支，受影响的说明一致，已让 Master 能逐项审；反馈按单会话工作块处理，不以交审代替批准。 |
| H10 | 将批准的改稿集中落源 | 可提检的共用方法论正文、模板和受影响说明 | ✓ 2026-11-21 经 Master 审阅与全新子代理对抗审查、依 PO Review 前全权委托由 Master 二轮复核核准的文字已逐字落源；PO 最终确认在 Review 前报告中；范围与批准稿一致，未改第三方原文，保留既有解析接口。开发自检和待核验证据已区分，供 PO 决定是否放行 Test。 |

**Key choices**

- 工作块按编号推进，每块按一个工作会话估量，审阅和 PO 等待另记。先审成套修订稿，不把讨论中的约定逐条改成生效规则；大改约定集中落源，不随手改 `CLAUDE.md`。
- 共用规则放在已有的 `overview.md` 条款，阶段细节留在 Sprint／设计约定，模板只提醒记录什么。只修相抵或缺失的说法，不替换 Scrum 等原文、不另建规则层，不先加字段、钩子或强制口令。
- 材料随相应的设计档案保存，沿现有 `scrum/documents/` 归档体系保留可读原件；设计结束至归档前保住原件与路径，归档后由日志及承接 Sprint 指向可用位置，不把唯一一份留在待清理的工作目录。Retro 只取可复用原则，不能拿它替代设计材料。
- 用能串起接手和收尾的隔离样本覆盖 §2.2 的反例与分支，以实际停留／继续、留下的日志与材料为证，不只看会话复述；不触及真实设计材料、项目记忆或用户配置。按[仓库测试手册](../documents/headless-testing.md)在运行前将样本、方法和通过线记入 §2.2 并单独提交，不改已定口径，不扩成自然触发专项。获准进入 Test 后，按 §5 留证，覆盖 §2.2、完整产品 DoD、Claude 严格校验和 DSH 既有回归；未改分发则不加实机重装专项。Test 通过也不自动收官。

**Risks and open points**

| 接口／风险 | 交接与回验 |
| --- | --- |
| Sprint 21：设计卡依赖日志 §1.2、§2.1、§3.1 和可选 §3.2；归档留材可能被误识别成开着的设计 | 保持既有章节、表格与 `Now` 表达，区分「宿主自身已结束但尚待归档」与「现在仍开放」。把拟改模板及收尾后的日志、材料路径样本交 Master 转 Sprint 21，合流时复核设计卡字段、开闭状态及 PBI-71 的归属；不新增强制字段，不在本期改看板或替 21 改判卷。 |
| Sprint 24：模板注释与阶段阅读指引可能改同一段；承诺快照不能成为注入来源 | 交接受影响的节与基线，区分本期的阶段门／日志语义和 24 的原文加载、角色入口及 hook 性能。整合后重验只从承诺表逐字取值，表下解释和决定行快照均不参与提取；不改频率或开关。 |
| Sprint 25／26：共用方法论正文与项目记忆容易被宿主或插件约定绑定 | 25 接收共用改动清单与 DSH 回归证据；本期不改打包、版本或安装方式。26 接收项目教训与插件约定 Memory 的边界，不等待该期、不接管其载体。 |
| 同一条约定在几处有不同表述，或归档后路径失效 | 交接注明基线提交、受影响段落、不得改变的接口和回验场景；Master 审过共用口径再转各期。发现冲突或需变更目标／验收，先报 Master 由 PO 定；不拉入其他分支，不把未合流的验证当作合流证据。 |

**2026-11-20 · How 计划审阅（Master）**：`b1995ec` 的 H1–H10 覆盖五项已定判据；先审成套全文再集中落源，保留原文与既有解析接口。计划无必改项，不等于施工放行。PO 强审由 Master 交整份文本供通读，不让 PO 逐条核对；施工放行由 Master 汇总后转请 PO。

Go-ahead: **2026-11-20（UTC+8）· PO 直接放行施工**。原话：「可以，我觉得23放行吧，可以开始做了。」已审 How 覆盖 §1.1 的日志接手与收尾目标；按 H1–H9 起草和交审，不把施工放行当成草稿批准。H10 只落经 Master 审、全新子代理对抗审查和 PO 通读强审后获准落源的文本。此次未单独授权提交（按第 22 条暂留未提交改动并记接手点；H10 落源、Test 前冻结及收官提交另请明确授权），不放行正式 Test 或收官，不授权合并、tag、推送或发布。§1.1 当时原文快照：「照着日志接手：接手的人能分清承诺原文和定目标的理由，查到本期重点验什么、完整 DoD 是否满足，以及下一步是否已获 PO 放行；收尾后，能找回选定和否决方案的依据，也能在项目记忆里逐条找到 Retro 的重要教训。」

Go-ahead: **2026-11-21（UTC+8）· H10 落源与本分支本地提交**。Master 依 PO 2026-11-21 Review 前全权委托（原话见 §4），二轮复核 18 份拟稿零必改项后放行：已审稿逐字落入生效路径、删除临时 `draft/`，作本分支本地提交；不改版本号、`CLAUDE.md`、hooks、`dsh/`，不合并、tag、推送或发布。H10 完成不等于正式 Test 放行：最后一轮流程 Test 方案另交 Master 审阅并冻结，Increment → Test 阶段门仍须单独放行。§1.1 当时原文快照：「照着日志接手：接手的人能分清承诺原文和定目标的理由，查到本期重点验什么、完整 DoD 是否满足，以及下一步是否已获 PO 放行；收尾后，能找回选定和否决方案的依据，也能在项目记忆里逐条找到 Retro 的重要教训。」

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

**H1 · 修订范围与交接基线（2026-11-20）**。对照 `00c224b`，插件、对外说明、DSH 与检查器均未变。按总表 F02、F09、F10、F11、F13 和 §2.2 已定判据执行；Developer 和三个独立只读核对覆盖以下表面的同义说法。这是拟修订范围，不是规则已变更。Master 同意将完整拟改稿放 `draft/<原相对路径>`，按落源位置核对引用，不改生效正文。归档写作 `scrum/documents/` 体系，兼容项目既有的分类子目录，不规定回迁方式。

| 工作块 | 拟改的旧说法和位置 | 依据；只引用或不动 |
| --- | --- | --- |
| H2 · DoD | `product-log.md` 第 5 条已说全套 DoD 生效，但「picks the items that matter」仍可能被读成缩小标准；对齐 `sprint-log.md` 第 4、13、16 条及 Sprint 模板 §1.2／§2.2／§5，写清重点、证据和判定。 | PBI-76、§2.2 与 SGEP Product／Increment／Product Backlog；不改产品日志 §1.3、不改正式验收何时需要 PO 的既有第 15 条、不改源文。 |
| H3 · Sprint 阶段门 | `overview.md` 图及第 12 条、`sprint-log.md` 图及第 3、8、22–24 条、Sprint 模板的页头提示与决定记录。`developer.md` 和 `scrum-master.md` 把「委托审 How」读成可替 PO 放行的句子要纠正；冲刺中途可发版的旧句也应指明仍须 PO 同意。 | PBI-77、阶段放行临时修正；保留书面授权，但审阅权／阶段内决定不等于阶段放行。说明起始无既定 Goal 的门、同阶段接手和 Test 原地修正与回退的区别。角色加载不动。 |
| H4 · 设计阶段门 | `design-log.md` 图、「三个环」、第 21、26、27 条及设计模板；`design-kernel/SKILL.md` 的 Use Protocol 不能靠「发现错了便回去」自行回退；`designer.md` 的原型例外不替代阶段许可。 | F09、PBI-77；保留《Sprint》章节、d.school 模式、现有第 9–15 条的方法写法和时机。独立 IDEO 五模式不是五个阶段，不增放行门；进入正式设计仍按正式设计的门。 |
| H5 · 承诺、解释与快照 | `overview.md` 第 16–17 条、承诺表下的三份模板注释、`sprint-log.md` 第 4、24 条、`design-log.md` 第 26 条；产品约定第 4 条已引用总规则，不再整条重写。 | F10、F13、PBI-78 与 PO 快照定案；表唯一权威，表下解释可选，历史决定行快照不替代表。保留一物理行的两列表、章节标题和纯文本；不改任何解析器。 |
| H6–H7 · 留材 | `design-log.md` 第 16、19、26 条、设计模板 §4／§5、`design-kernel/SKILL.md` Prototype 行、`designer.md` 与 `ideo-kernel/SKILL.md` 正文里的「用完丢掉」；`overview.md` 第 3–6 条和 `sprint-log.md` 第 17 条要免除设计原件被两次清理。独立 `ideo-log.md` 第 4 条只解除对变化了的设计交接条款的误引用。 | F11、PBI-79、§2.2；保留原型粗快、用于学习且不是增量；只改作者的保存约定，不改书中「disposable」原文，也不把独立 IDEO 日志或普通 Sprint 文件一律纳入。 |
| H8 · Retro | `sprint-log.md` 第 18 条仍说「a notes file」；把规则写成项目记忆中的独立要点，无宿主能力沿用仓库教训笔记。`overview.md` 第 6 条的指令文件用途不得盖过 Retro 专门规则。 | F02、PBI-69、SGEP Retro；仍无 Retro 章、不写汇总或指令文件、不并入 PBI-51；本项目现行的 Master 列候选、PO 挑要点仍在 `CLAUDE.md`，不推为通例。 |
| 对外说明 | README 双语的开场与会话例子不得把「定了」说成继续行动，也不得省略实际让用户放行 Test；快速上手双语 §§2–5／书面授权、词汇表对应行和常规入口用同一说法。 | 只改现有说明，不加教程层或变版本、命令形式、分发／加载表述。`CLAUDE.md` 仅核对不动；不回改历史日志。 |

| 交接 | 保留的接口；合流时回验 |
| --- | --- |
| 21 · 看板 | 设计 §1.2／§2.1／§3.1／可选 §3.2，原 `From`、`Now`、`Waiting for PO` 位置及表形状不动。当前 `board-log.md` 第 4 条和 `scripts/board_check/check.py` 的 `discover()` 按活动路径发现，设计分支上的活动日志也会被读；设计结束待归档要在既有 `Now` 表明已结束，归档后从活动路径移走并核对仍在的分支。21 回验待归档／已归档的展示；PBI-71 的 `For` 与已结束 IDEO 归属不在本期改。 |
| 24 · 加载和提取 | `commitments.sh:43–63`、`dsh/commitments.js:21–48` 和 `scripts/board_check/check.py:94–112` 只取承诺行；不能把判卷能识别的某个中文标题当作各宿主通用。三个模板的注释、设计内核 Use Protocol 和角色入口正文是合流点；保留阅读要求，不动 loading、hook 频率或开关。两宿主运行期输出（`commitments.sh:125–133`、`dsh/commitments.js:81–82` 与 `check_dsh.mjs:102`）本期未改，多日志仍报「开着」／「are open」，交 24／25 评估是否顺带改运行期措辞。 |
| 25 · DSH 与双语说明 | 交同一份正文和双语文档的改动段落；保留安装、入口、版本段和打包范围，不改分发。`check_docs.py` 依赖 README 的 Departures 表原样对应总览，拟不动该表；两份 README／快速上手保持结构和链接对应。待按批准范围回验 DSH。 |
| 26 · 约定 Memory | 项目 Retro 教训与插件约定是两个内容层，项目教训不进入分发包或 PBI-51；设计原件也不以教训摘要替代。 |

**H2–H9 · 成套审阅稿（2026-11-20，Developer 交审稿）**。`draft/` 下 18 份全文保留原路径层级；圈阅时以 `00c224b` 同路径为改前全文，链接按拟落源位置核对。以下是改动与场景，不是正式 Test 的方法、通过线或结果。沿用 H1 所列出处，未动生效约定、技能描述、角色加载正文、Scrum 和设计源材料、看板、两个宿主的承诺读取器与版本。

| 工作块 | 圈阅位置与建议 | 对照场景（未运行） |
| --- | --- | --- |
| H2 · PBI-76 | [产品约定第 5 条](../../plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md#each-part)、[Sprint 约定第 4、13、16 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#test)、[Sprint 模板](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-backlog-template.md)、[Developer](../../plugins/ideo-scrum/commands/developer.md#code-of-conduct)。一个地方设标准；Planning 定取证重点和 Test 的要求；Test 分记质量与价值。 | **同一份样本 Sprint** 的产品日志列三个 Output：文档新改链接有效、模板章节契约没有变、改分发才验安装；Outcome 有「陌生人走完首个冲刺」。§1.2 指回全部 DoD，重点查链接；§2.2 写定方法与过线。§5 以本次链接检查作新证据，以可追溯的旧样本和模板契约逐项相同说明旧证据仍有效；没改分发才允许写安装条件未触发。对照删掉模板旧证据：它仍适用，不能判通过。再对照同一个 Outcome：没列当期必须验证则记待观察，不报全套 DoD 已过；事前要求当期验证则缺证拦整体 Test。若有失败观察，记未达及影响，不写待观察。 |
| H3 · PBI-77 | [总览第 12 条](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md#who-does-what)、[Sprint 约定第 8、22、24 条和流程图](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md)、Sprint 模板和 [Master](../../plugins/ideo-scrum/commands/scrum-master.md#code-of-conduct)、Developer。先核真实授权、再行动；单收委托审 How 不得代发施工许可。 | 只说「计划不错」：留 How，不施工、不委派；说「计划通过，现在按这份 How 开始施工」：明确两件事，可进入。只看过增量：施工自检可做，不启 Sprint Test。发现要回去时先报目标阶段，不复用上次放行；同阶段同范围换会话看日志可续。首次明确启动 Why 时还没有 Sprint Goal，不把 `<Sprint Goal>` 当原文。 |
| H4 · PBI-77 | [设计约定第 21、24、26 条和流程图](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md)、[设计模板](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-backlog-template.md)、[设计内核正文](../../plugins/ideo-scrum/skills/design-kernel/SKILL.md#use-protocol)、[Designer](../../plugins/ideo-scrum/commands/designer.md#code-of-conduct)、[IDEO 约定第 1、2 条](../../plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md#the-boundary)。独立五模式不加门，只有转入正式设计才按正式设计的门。 | 认可 Define，或只说「开始 Ideate」但未定这轮怎么发散：不做 Lightning Demos、不发散、不画草图、不派构思；PO 明确本轮组织并放行才继续。只选方案不做原型；Prototype 试跑不是设计 Test。测试发现题目错了，记录依据、等 PO 放行返回 Define；交了选方案或审阅不算交了进 Prototype。 |
| H5 · PBI-78 | [总览第 16、17 条](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md#what-stays-fixed)、[产品模板](../../plugins/ideo-scrum/skills/scrum-kernel/conventions/product-backlog-template.md)、Sprint 和设计模板；两份阶段约定保留逐字快照，不把快照和表下理由接入承诺提取。已有等价规则不再重写。 | **项目 Sprint 目标格**：「找得回收件记录：接班的人能用订单号定位签收证明，不用找上一班问。」**汇总级目标格**：「交接索引：① 收件线定位签收证明；② 值班线交接未完成事项。」两例各是一物理行、一个承诺格，短名不变。产品、Sprint、设计的表下可另写或不写理由，例如「夜班交接时常找不到上一位」；改这句话不改目标。若 PO 后来改目标，旧决定行仍留当时文字；删去当前承诺表只剩理由或快照，下一次不能过门。 |
| H6–H7 · PBI-79 | [设计约定第 16、19 条](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md#ending)、设计模板、设计内核 Prototype 行、[IDEO 内核正文](../../plugins/ideo-scrum/skills/ideo-kernel/SKILL.md#ideo-design-thinking)、[Designer 的原型段](../../plugins/ideo-scrum/commands/designer.md#identity)、[总览第 3–6 条](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md#where-things-live)与 [Sprint 约定第 17 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#closing)。Designer 的旧 Identity 只换与 PBI-79 相抵的「用完即丢」句段，留作单独圈阅；书中低成本、可放弃的原型观不改，保留文件不等于交付。 | 设计结束时 `Now` 记已结束待归档，`sketches/a.md`、`sketches/b-rejected.md`、`demos/`、`review.md`、`synthesis.md`、`prototype/` 仍从设计日志可访问。第一次归档 Review 把日志及原件移到 `scrum/documents/` 下的设计档案，核对引用和活动路径；承接 Sprint 先后顺序及清理不删原件。另验没有承接者、结论不实施，材料仍在；只剩摘要或 `git show <sha>` 的失败。普通 Sprint 临时文件继续按原规则清理，不把保护扩到独立 IDEO 的原型。 |
| H8 · PBI-69 | [Sprint 约定第 18 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#closing)、总览第 6 条。项目记忆与仓库兜底都按单条可独立读取；例子不规定路径，现有项目的角色分工不升格为通例。 | 例：「交接时列新路径和旧路径」若能说明上次为何只发新路径导致承接误删，则写成一条可复用教训；「先开了两个窗口」只是一次过程细节，不存。无重要教训则不写；无项目记忆时写进仓库教训笔记的独立条目，仍不写当期汇总或指令文件。设计评审原件保留，不拿教训替代，不交插件 Memory。 |
| H9 · 对外说明与交接 | [README EN](../../README.md)／[中文](../../README.zh-CN.md)、[快速上手 EN](../../docs/quick-start.md)／[中文](../../docs/quick-start.zh-CN.md)、[词汇表](../../docs/glossary.md)。只改对应说法，Departures 表、安装命令和双语结构不变。交接按 H1，Sprint 21 的 PBI-71 不等于移除已结束待归档的宿主卡。 | 换会话按 `Now`、已记录的授权和承诺表追到当前阶段；仅有 hook 提示不算取得授权。归档后不留活动设计路径；发现别的分支还有旧活动日志，只汇报，23 不擅自改。 |

**H9 自检**：18 份草稿与基线逐份核对；三份日志模板的标题、页头字段与表格行未变，命令加载段、技能／命令 frontmatter 与源文署名未变；按拟落源位置静查 6 处新增跨文件指针及双语说明／词汇表的 103 个引用，无报错。未运行正式流程样本、Claude 严格校验或 DSH 回归，§5 不记通过；后续以获准落源后的文件、事前冻结的标准和单独的 Test 放行为准。

**2026-11-20 · Developer 交审**：成套全文、上表和交接位置已发 Master，待审阅。How 表中的完成标记只记这轮修订稿与交审动作，不是条目验收。当前检查点 `183d97d`；日志与审阅稿留在本工作树、未提交。下一步按 Master 审阅、全新子代理对抗审查、PO 通读强审的顺序推进；未获批准不做 H10，不进 Test。

**2026-11-20 · Master 首审修订**：只改拟稿中的两项；Designer 原 Identity 与拟替换句保留，单列待 PO 明批。

| 条目 | 修订与对照（未运行正式 Test） |
| --- | --- |
| PBI-76 | [总览 Test 节点](../../plugins/ideo-scrum/skills/scrum-kernel/overview.md#the-map)不再把 PO 端到端测试写成固定动作；Formal acceptance 仍按 Sprint 约定第 15–16 条。有写定要求才需要 PO 正式验收；两种情况都不省略独立审阅。 |
| PBI-79 | [设计约定第 19 条](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md#ending)、[Sprint 约定第 17 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#closing)与[设计模板](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-backlog-template.md)对齐：先收官的工作树拿不到完整设计日志或任一原件，就不跨树搬动，设计继续待归档。第一个在本检出能读全的 Review 才归档，并交接旧、新路径；承接方未读到新路径前保留可用引用，读到后再在本检出换链。其他分支的残留只报 Master，不代改；解析契约不变。 |

**2026-11-20（UTC+8）· Review 前委托（Master 转达）**。PO 原话：「现在他们全部都开跑了，这样子我跟你讲。嗯，每一个对话，我现在给你权限，每一个对话，等到他们 review 之前向我报告就可以了。不意是每一个对话哦。因为他们现在都已经开始跑了。」

- **Master 代定**：仅适用已开的 Sprint 21–25；各期正式 Sprint Review 前的阶段门和常规事项由 Master 定，各次决定仍按约定记录。
- **仍回 PO**：改 Product Goal、取消 Sprint、推翻既定决定、PO 指定的品味、正式 Review／Retro／收官、推送与发布。Sprint 23 的成套规则由 PO 通读强审；Designer Identity 的替换单独等 PO 明确批准。
- **当时停点（2026-11-20 审阅前）**：Master 已复核两处修订，18 份拟稿原样等待 Master 安排的全新子代理对抗审阅。独立审阅和 PO 强审之后，Master 按各自条件分别核准 H10 与正式 Test；本次记录委托不等于放行。未暂存、未提交、未落源、未进正式 Test。

**2026-11-20 · 对抗审阅整改与二次静态审计补正**。先按对抗审阅五点及既有 README 计数对齐修改第一批 9 份拟稿，随后经 5 个独立只读代理全量静态审计并补正——连同 [设计模板](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-backlog-template.md) 共修订 10 份拟稿（下列为文字修订与反例边界，非正式 Test 结果）：

| 点 | 拟稿修订位置与核对 | 对应反例／应有处理（未运行） |
| --- | --- | --- |
| 1 · PBI-79 合流后的引用 | [设计约定第 19 条](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md#ending)与 [Sprint 约定第 17 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#closing)：施工期间可暂留可读旧链。若设计归档已在 `main`、本检出或同行待合入分支，承接 Sprint 收官前对照该目标集成态核实际材料引用（含准备归档的承接 Sprint 日志）与原件，不能只凭旧工作树能读就收官；若各处尚均未归档（仍待首个可读全套的 Review 归档），则保留可用活动引用、记待归档并合入 `main`，由随后归档的 Review 在收官提交前全项目清扫旧路径并把未合入分支残留报 Master。不跨树代改，不改逐字历史承诺快照。 | A 将设计归档并合入 `main`；B 工作树仍有旧目录，旧链能读，但 B 准备合入的归档日志还指旧目录。应在目标集成态发现断链，换成新引用后才能收官。反序时若设计尚在 C 分支未归档、B 先收官合入 `main`，B 留可用旧引并在 `main` 等待 C 归档时按第 19 条第 1 步全项目替换；不留孤儿断链。 |
| 2 · PBI-77 续接、提交与设计 Git 许可 | [Sprint 约定第 22、26 条](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#throughout)限定会话交接／停顿时获准才提交，不豁免第 13 条 Test 前冻结提交或第 19 条收官提交——到门若无提交许可须先请示，不能跳过前置；[设计约定第 19、21、24、26 条](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md#throughout)与[设计模板页头](../../plugins/ideo-scrum/skills/design-kernel/conventions/design-backlog-template.md)明确定义设计侧 git 许可由 PO 另批并记入阶段／结束决定，进入或续接阶段不等于授权提交／合并／删分支／推送。 | 只获施工或设计阶段入口许可需要换会话：保存已有改动、日志记状态和接手点，不擅自 commit；正式 Test 冻结提交未完成时，不能以「提交未授权」作理由免除冻结而直接开测。 |
| 3 · PBI-77／79 两类设计边界 | [Designer CoC](../../plugins/ideo-scrum/commands/designer.md#code-of-conduct)、[README EN](../../README.md#your-first-sentence)／[中文](../../README.zh-CN.md#第一句话怎么说)及 [IDEO 共用技能正文](../../plugins/ideo-scrum/skills/ideo-kernel/SKILL.md#ideo-design-thinking)：正式设计先由 PO 定本轮发散安排且放行 Ideate，再出方案；入口前只谈如何发散。独立五模式不加阶段门；保留原件规则限定设计冲刺，独立 IDEO 原型仍照自己的去向规则。Identity 原句和拟替换句均不再改，仍单列待 PO 明批。 | 设计还在 Define，只有「帮我想想怎么发散」：可谈本轮安排，不画方案或派构思。反例不能反过来要求独立五模式每换模式都请放行，也不能据设计冲刺的留材规则取消独立 IDEO 的原型交接／清理。 |
| 4 · PBI-69 收官提交与记忆落点 | [Sprint 约定第 19 条第 2 步](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md#closing)、[快速上手 EN](../../docs/quick-start.md#5-close)／[中文](../../docs/quick-start.zh-CN.md#5-收官)与[词汇表](../../docs/glossary.md#process-流程)：收官提交只装 Review／Retro 实际产生的仓内改动；项目记忆在仓外不搬入，没有重要教训不凑条目。无宿主项目记忆时用仓库里逐条可找回的教训笔记，不写指令文件或每期 Retro 汇总；词汇表补回 Review「压缩并归档」、区分「每期 Retro 汇总」与归档摘要。 | 只有一条重要教训，实际已写仓外项目记忆：提交只含实际仓内 Review 等改动，不复制教训来凑齐两种文件。没有重要教训就不新建；无宿主记忆时有两条重要教训，则在仓库教训笔记中分别保存，而非造一个 Sprint Retro 汇总。 |
| 5 · PBI-76 未触发条件的原因 | [快速上手 EN §4](../../docs/quick-start.md#4-build-and-test)／[中文 §4](../../docs/quick-start.zh-CN.md#4-做和测)明确写清即使非本期重点也不豁免、并记录未适用原因，与 Sprint 第 16 条一致；顺手去掉中文示范块「把 定」多余空格。 | 样本只写「安装条件未触发」而未解释本期没有分发变更：证据记录仍缺原因；必须写清触发条件和未触发原因。仍适用的标准不能借此逃过核验。 |
| 既有 README 计数与运行期口径 | 双语 README 承诺段与其中 DSH 条目写明提醒按 `scrum/` 活动路径扫描（DSH 限当前检出），已结束待归档日志也可能仍在；并明示现行运行期多日志消息仍打印「开着」／`"open"`，不能把存在或数量当成开放或授权，仍查 `Now` 与记录许可。不改标题、承诺表及 `commitments.sh`／`dsh/commitments.js`／`check_dsh.mjs`。 | 当前检出下有一份仍在做和一份已结束待归档的设计日志：运行期提醒会报两份「开着」；不能据此认定两个设计都开放或获准继续，要查各自 `Now` 和许可。 |

- **二次静查与复核结果（2026-11-20，仅静态与叠加预检，未运行正式 Test）**：
  - 确定性静查与叠加校验：18 份 `draft/` 零 CR 字节、与基线 `00c224b` 逐份核对且生效源码与运行期读取器未改；新增相对路径 6 处、双语与词汇表 103 处引用、18 份拟稿与本日志共 151 处内部链接及锚点零错误；§2.1 逐字及三处 §1.1 快照核对一致；模板与承诺提取在 `board_check`、临时叠加（`check_docs.py`、`check_dsh.mjs`、`claude plugin validate --strict`、`commitments.sh == dsh/commitments.js`）均通过；仓库基准自检 `check_docs.py --selftest`（17 项）、`scripts/board_check/check.py selftest`（42 项）、`node --test scripts/check_dsh.mjs`（6/6）与 `claude plugin validate --strict plugins/ideo-scrum` 均通过。
  - 只读复核：独立 Haiku 子代理对二次静态审计全部 13 项发现逐项复核 13/13 通过（无新增冲突或回归）。
  - **当前停点**：18 份拟稿仍留 `draft/`，工作区未暂存、未提交、未落源（H10 未执行），未进入正式 Test；待交 Master 复核后送 PO 通读强审与 Designer Identity 裁定，并另请对应提交／落源授权。

**2026-11-21（UTC+8）· Review 前全权委托（Master 转达）**。PO 原话：「可以，先审 22、23、25 吧  后面这些，嗯，对话。他们到 review 之前再向我报告。就是后面的事情你都可以决定了，review 之前再向我报告。」

- **Master 代定**：Sprint 22、23、25 正式 Sprint Review 前的阶段门和常规事项由 Master 定；各次决定仍按约定记录。
- **仍回 PO**：改 Product Goal／Sprint Goal 承诺、取消 Sprint、推翻 PO 定案、PO 点名品味、改本仓库 `CLAUDE.md`、正式 Review／Retro／收官、合并、tag、推送、发布。
- 本委托不降验收线，不跳过 Increment → Test 阶段门与 Test 前冻结提交。

**2026-11-21 · Master 二轮复核与 H10 放行**。Master 逐份核对 18 份拟稿与基线 `00c224b` 的完整 diff，全部通过、零必改项：对抗审阅五点（合流后归档引用与反序清扫、交接提交不豁免第 13／19 条门及设计侧 git 许可、正式设计与独立五模式边界、PBI-69 收官提交与仓外记忆／兜底笔记、PBI-76 未触发原因）及 README 计数与运行期口径均已落实；零 CR 字节、零 frontmatter 修改、零受保护路径（`references/`、`IDEO-modes/`、`ATTRIBUTION.md`、`hooks/`、`dsh/`、`CLAUDE.md` 等）改动。核对 §1.1 承诺原文后，依 PO 委托放行 H10 落源与本分支本地提交；正式 Test 仍未放行。

- **Designer Identity 单句（单列，待 PO 在正式 Review 前最终确认）**：[Designer](../../plugins/ideo-scrum/commands/designer.md#identity) 的 Identity 仅将与 PBI-79 相抵的「用完即丢／转作规格」句段替换为「the prototype is for learning and stays with the design material; if a Sprint builds its conclusions, that Sprint uses it by reference as a specification, never as an Increment（design-log 第 19 条）」，其余原文一字未动。此前「原句与拟替换句均不再改」的停点记录由本条依 PO 委托更新；该句随 H10 落入本分支，正式 Review 前一并明示 PO 作最终合入确认。

**2026-11-21 · H10 落源与自检（正式 Test 未运行）**。18 份已审稿逐字节落入生效路径（SHA256 落源前后 18/18 一致），临时 `draft/` 目录已删除；本日志内原指向 `draft/` 的审阅链接改指生效路径，落源文字与当时审阅稿逐字相同。

- `python -X utf8 -I scripts/check_docs.py`：5 份文档、103 处链接、0 错误；`--selftest` 17/17。
- `python -X utf8 -I scripts/board_check/check.py selftest`：42/42。
- `node --test scripts/check_dsh.mjs`：6/6。
- `claude plugin validate --strict plugins/ideo-scrum`：Validation passed。
- 18 份生效文件零 CR 字节；`git diff 00c224b` 与已审稿 1:1（以落源前后哈希比对为证）。
- 本分支本地提交见紧接本条入库的 `git log`（提交信息 `docs(Sprint 23): H10 落源 18 份已审稿`）；未改版本号、`CLAUDE.md`、hooks、`dsh/` 或第三方原文，未合并、tag、推送或发布。
- **当前停点**：H10 已提交；最后一轮流程 Test 方案另交 Master 冻结与放行，未获放行前不运行正式 Test，Test 通过也不自动收官。

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again. The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
