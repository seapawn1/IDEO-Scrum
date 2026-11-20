# Sprint Backlog — Sprint 23 (log-rules)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-23-log-rules-4b3ec9` | Product Owner: SeaPawn | Scrum Master: Sprint 21–26 主会话 | Developer: Sprint 23 工作树会话
> Now: Planning · How。2026-11-20，Master 转达 PO 决定：What 精化结束，放行 How 规划；计划待 Master 审阅，尚未放行施工或实测。
> Waiting for PO: None
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
| H1 | 定修订范围和交接基线 | 基于 `00c224b` 的受影响条款、模板、入口说明和跨期接口清单 | 每处拟改文字能指到原文、作者约定或 PO 决定；对照命令、SKILL.md、双语 README、快速上手、词汇表与项目指令中的同义说法，标清改哪处、哪处只引用或不动。 |
| H2 | PBI-76：对齐 DoD 与取证写法 | 产品约定、Sprint 的 Why／Test 写法与模板的成套修订稿 | 从同一份样本能追溯完整 DoD、需新取证、仍有效的旧证据与未触发条件。适用但缺证据不通过；Outcome 信号是否拦本期 Test 按事前约定判，不把待观察当通过或豁免。 |
| H3 | PBI-77：对齐通用阶段门与 Sprint 流程 | `overview.md` 与 Sprint 阶段门、模板的修订稿 | 进入、返回与同阶段接手三种情况分得清；认可 How 不授权施工，认可增量不授权 Sprint Test；可追溯放行人、目标阶段与范围。 |
| H4 | PBI-77：对齐设计阶段门 | 设计约定与模板的修订稿 | 进入和返回都须明确放行；书面交接仅在 PO 明授的范围内有效，不因 Prototype／Test 可以由 AI 承担而省略阶段门。Ideate 的组织方式由 PO 先定，选定方案与放行 Prototype 分开；不新增方法数门槛，不改设计日志既有字段。 |
| H5 | PBI-78：对齐承诺与解释 | 三类日志的承诺说明及项目级／汇总级 Sprint Goal 对照样本 | 表内原文唯一权威，表下解释可选且不参与提取；过关先读再核对，决定行留当时原文快照。汇总级条目列在同一单行承诺格内；保留两列表形状和既有标题，不改解析器。 |
| H6 | PBI-79：设计结束时保留依据 | 设计材料的保留与交接规则、原型去向说明 | 选定与否决方案、原型、速写、演示、评审及合成稿仍从日志可找回；是否有承接 Sprint 不决定删除，留存不计作正式 Increment。 |
| H7 | PBI-79：让归档和 Sprint 清理保住材料 | 设计归档与承接 Sprint 收尾的修订稿 | 首次归档 Review 和承接 Sprint 收官后都能按有效引用读回原件；档案不被误认成开着的设计，通用「过期即删」和工作文件清理不再删去保留材料。本次规则约束以后收尾，不回迁历史。 |
| H8 | PBI-69：项目 Retro 分条入记忆 | Retro 约定修订稿与正常／兜底对照样本 | 只保存重要教训且每条可独立找到；没有重要教训不凑数。无宿主项目记忆时沿用仓库教训笔记；通用工作材料规则不能让 Retro 教训写进指令文件，不建每期汇总，不混入插件约定 Memory。 |
| H9 | 交审成套修订稿 | 可圈阅的全文、§2.2 判据对照和跨期交接记录 | 五项各有正反例或必要分支，受影响的说明一致，已让 Master 能逐项审；反馈按单会话工作块处理，不以交审代替批准。 |
| H10 | 将批准的改稿集中落源 | 可提检的共用方法论正文、模板和受影响说明 | 仅将经过 Master 审阅、全新子代理对抗审查与 PO 强审的文字按授权落盘；范围与批准稿一致，未改第三方原文，保留既有解析接口。开发自检和待核验证据已区分，供 PO 决定是否放行 Test。 |

**Key choices**

- 工作块按编号推进，每块按一个工作会话估量，审阅和 PO 等待另记。先审成套修订稿，不把讨论中的约定逐条改成生效规则；大改约定集中落源，不随手改 `CLAUDE.md`。
- 共用规则放在已有的 `overview.md` 条款，阶段细节留在 Sprint／设计约定，模板只提醒记录什么。只修相抵或缺失的说法，不替换 Scrum 等原文、不另建规则层，不先加字段、钩子或强制口令。
- 材料随相应的设计档案保存，沿现有 `scrum/documents/` 归档体系保留可读原件；设计结束至归档前保住原件与路径，归档后由日志及承接 Sprint 指向可用位置，不把唯一一份留在待清理的工作目录。Retro 只取可复用原则，不能拿它替代设计材料。
- 用能串起接手和收尾的隔离样本覆盖 §2.2 的反例与分支，以实际停留／继续、留下的日志与材料为证，不只看会话复述；不触及真实设计材料、项目记忆或用户配置。按[仓库测试手册](../documents/headless-testing.md)在运行前将样本、方法和通过线记入 §2.2 并单独提交，不改已定口径，不扩成自然触发专项。获准进入 Test 后，按 §5 留证，覆盖 §2.2、完整产品 DoD、Claude 严格校验和 DSH 既有回归；未改分发则不加实机重装专项。Test 通过也不自动收官。

**Risks and open points**

| 接口／风险 | 交接与回验 |
| --- | --- |
| Sprint 21：设计卡依赖日志 §1.2、§2.1、§3.1 和可选 §3.2；归档留材可能被误识别成开着的设计 | 保持章节与承诺表形状；把拟改模板及收尾后的日志、材料路径样本交 Master 转 Sprint 21，合流时复核设计卡字段、开闭状态及 PBI-71 的归属，不在本期改看板。 |
| Sprint 24：模板注释与阶段阅读指引可能改同一段；承诺快照不能成为注入来源 | 交接受影响的节与基线，区分本期的阶段门／日志语义和 24 的原文加载、角色入口及 hook 性能；整合后重验从承诺表逐字取值，不把解释或快照注入，不改频率或开关。 |
| Sprint 25／26：共用方法论正文与项目记忆容易被宿主或插件约定绑定 | 25 接收共用改动清单与 DSH 回归证据；本期不改打包、版本或安装方式。26 接收项目教训与插件约定 Memory 的边界，不等待该期、不接管其载体。 |
| 同一条约定在几处有不同表述，或归档后路径失效 | 交接注明基线提交、受影响段落、不得改变的接口和回验场景；Master 审过共用口径再转各期。发现冲突或需变更目标／验收，先报 Master 由 PO 定；不拉入其他分支，不把未合流的验证当作合流证据。 |

Go-ahead: 未获施工或实测放行。当前仅获准形成和审阅本期 How 规划，不授权合并、tag、推送或发布。

## 4. Increment notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 9 and 20). A session that picks up the Sprint reads these first. The chapter ends with the Product Owner's decision that the Increment can go into testing (sprint-log.md, convention 24). -->

## 5. Test

<!-- Record here the Developer's tests, the reviewer's check (by default the Scrum Master), the Product Owner's end-to-end test, and the result of each Definition of Done item and acceptance criterion. Fix a problem on the spot and test again. The chapter ends with the Product Owner's decision: close, or go back (sprint-log.md, convention 24). -->
