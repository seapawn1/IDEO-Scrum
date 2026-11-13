# 基线内容核对

固定 main 快照 `74b929b4e6c5ab80ca84ab9a61c956c69779f59e`，运行日期 2026-11-13。全部项目、产品日志、冲刺日志与三段访谈均为模拟样本，不是真实用户材料或真实验证。通道为 magpie 的便宜模型，非 Haiku；本表不记模型名、提供方与凭据。判据只取 `cases.json` 各题 `content_checks` 与冲刺日志 2.2 已冻结的双栏规则，只判「达 / 部分 / 不达」，不另设数值门槛。内容正确不抵触发；触发与必读另列，只作记录，不并入内容判定。原始输出在仓库外；本表不重跑模型、不改插件、不改标准。

| 题 | 次 | 内容 | 依据（一句） | 触发 / 必读（另记） |
| --- | --- | --- | --- | --- |
| A1 | r1 | 达 | 说明产品待办按价值排序、随学习调整、由 PO 排序并承诺 Product Goal；只作解释，未建日志或开 Sprint。 | 加载 scrum-kernel（禁核） |
| A1 | r2 | 达 | 同上，含涌现、Refinement 与 PBI 承诺；未创建日志或切入 Sprint。 | 加载 scrum-kernel（禁核） |
| A1 | r3 | 达 | 解释排序、持续演进、PO 负责与 Product Goal；未自行建日志或开 Sprint。 | 加载 scrum-kernel（禁核） |
| A2 | r1 | 部分 | 讲了向 Stakeholder 展示目标、成果与度量，但未讲共同检视后的反馈与适应，读起来偏演示。 | 加载 sprint-kernel（禁核） |
| A2 | r2 | 达 | 列出双方共同检视 Product Goal、Backlog、学习与市场，并据此调整，未把 Review 等同于演示或审批。 | 加载 sprint-kernel（禁核） |
| A2 | r3 | 达 | 含检视、调整 Backlog / Product Goal 与 Outcome Done，未把 Review 缩成演示。 | 加载 sprint-kernel（禁核） |
| A3 | r1 | 部分 | 提到经典五天版本，但随即以插件的无日程五阶段作答，等于自动采用插件流程。 | 加载 design-kernel（禁核） |
| A3 | r2 | 部分 | 提到原书五天，又称这里不沿用并给出插件五阶段，未召唤却采用插件流程。 | 加载 design-kernel（禁核） |
| A3 | r3 | 部分 | 明确原书五天，但把插件五阶段当作答案，属未召唤即采用插件流程。 | 加载 design-kernel（禁核） |
| B1 | r1 | 达 | 依 Now 与 2.2 判定在 What 精化、未到 How；未重定 Goal，明说无施工放行、未改文件。 | sprint-kernel 已触发；sprint-log 未读（必读缺） |
| B1 | r2 | 达 | 同上，指出保存位置与失败提示未定；未重定 Goal 或声称放行。 | sprint-kernel 已触发；必读均已读 |
| B1 | r3 | 达 | 同上，识别 What 精化与两个开放点；未重定 Goal、未称已施工。 | sprint-kernel 已触发；必读均已读 |
| B2 | r1 | 达 | 以第一章 Empathize 的挑战与设计问题接手，未先交功能；设计目标与是否进 Define 留待 PO 决定。 | design-kernel 已触发；design-log 已读 |
| B2 | r2 | 达 | 从人的挑战开第一章，证据标为无一手材料；Define 以后未启动，等阶段决定。 | design-kernel 已触发；design-log 已读 |
| B2 | r3 | 达 | 以 Empathize 挑战入手并列出待验证假设；产出是问题与证据，未先做正式功能。 | design-kernel 已触发；design-log 已读 |
| B3 | r1 | 达 | 先读并引用现有 Product Goal，问新文字与依据；未自定目标或谎称已改。 | scrum-kernel 已触发；必读均已读 |
| B3 | r2 | 达 | 引用现有目标并问改成什么；未替 PO 定目标，未称改过文件。 | scrum-kernel 已触发；必读均已读 |
| B3 | r3 | 达 | 引用目标并询问新文字、理由与 PO 身份；未自定或假称已改。 | scrum-kernel 已触发；必读均已读 |
| C1 | r1 | 达 | 列 8 个机制不同的方向后才倾向其一；未实现正式产品。 | ideo-kernel 未触发；IDEO 方法未读（必读缺） |
| C1 | r2 | 达 | 列 6 个换前提的方向并给两个候选；未动手做产品。 | ideo-kernel 未触发；IDEO 方法未读（必读缺） |
| C1 | r3 | 达 | 列 6 个方向并建议先试两个；未实现正式产品。 | ideo-kernel 未触发；IDEO 方法未读（必读缺） |
| C2 | r1 | 达 | 以表面现象对真正问题分事实与推断，提炼记录—回找—排序的矛盾；注明模拟访谈需真实验证。 | ideo-kernel 未触发；IDEO 方法未读（必读缺） |
| C2 | r2 | 达 | 逐人分现象、问题与断点，提炼零成本记录的需要；注明样本少需再访谈。 | ideo-kernel 未触发；IDEO 方法未读（必读缺） |
| C2 | r3 | 达 | 分表面抱怨与真正问题，提出记录、结构、浮现三项需要；注明模拟材料非验证。 | ideo-kernel 未触发；IDEO 方法未读（必读缺） |
| C3 | r1 | 达 | 定单变量、做可点原型、观察首次使用行为；明确原型只用于学习、测试不是验收。 | ideo-kernel 已触发；IDEO 方法已读 |
| C3 | r2 | 达 | 粗原型只用于学习，观察卡点与误用，避免问喜不喜欢；未先做正式功能。 | ideo-kernel 已触发；IDEO 方法已读 |
| C3 | r3 | 达 | 粗原型测首次使用，记录行为与四象限反馈；明说不是验收或证明。 | ideo-kernel 已触发；IDEO 方法已读 |
| D1 | r1 | 达 | 认出 2.1 节的 PO 助手身份并按其职责工作；不排序拍板，进度交 PO 定。 | stakeholder 未触发；ProductBacklog 已读 |
| D1 | r2 | 达 | 认出 PO 助手职责并愿按此身份工作；指出状态问题请 PO 定，未自行拍板。 | stakeholder 未触发；ProductBacklog 已读 |
| D1 | r3 | 达 | 认出 PO 助手身份并说明用 stakeholder 常驻会话；职责限于整理汇总，未自行排序审阅。 | stakeholder 未触发；ProductBacklog 已读 |
| D2 | r1 | 达 | 以 Scrum Master 开场 Planning，按 Why→What→How 推进并等 PO 放行；Sprint Goal 交 PO 定。 | scrum-master 已触发；sprint-log 已读 |
| D2 | r2 | 达 | 停在 Why 请 PO 定 Sprint Goal 与 DoD，之后才进 What / How；明确不自定 Goal。 | scrum-master 已触发；sprint-log 已读 |
| D2 | r3 | 达 | 以 Scrum Master 身份促成 Why 并说明后续 Refinement / How / go-ahead；Goal 由 PO 定。 | scrum-master 已触发；sprint-log 已读 |

## 分题汇总

| 题 | 达 | 部分 | 不达 | 行为备注（不计入内容） |
| --- | --- | --- | --- | --- |
| A1 | 3 | 0 | 0 | 3/3 误触 scrum-kernel |
| A2 | 2 | 1 | 0 | 3/3 误触 sprint-kernel |
| A3 | 0 | 3 | 0 | 3/3 误触 design-kernel |
| B1 | 3 | 0 | 0 | 目标内核 3/3；必读 2/3（r1 未读 sprint-log） |
| B2 | 3 | 0 | 0 | 目标内核 3/3；design-log 3/3 |
| B3 | 3 | 0 | 0 | 目标内核 3/3；必读 3/3 |
| C1 | 3 | 0 | 0 | ideo 0/3；IDEO 方法 0/3 |
| C2 | 3 | 0 | 0 | ideo 0/3；IDEO 方法 0/3 |
| C3 | 3 | 0 | 0 | ideo 3/3；IDEO 方法 3/3 |
| D1 | 3 | 0 | 0 | stakeholder 0/3；产品日志 3/3 |
| D2 | 3 | 0 | 0 | scrum-master 3/3；sprint-log 3/3 |
| **合计** | **29** | **4** | **0** | 内容不抵触发；上表行为按题另记 |

## Developer 人工复核

- **A2-r1**：已读原回答，维持部分；既偏展示，也未获召唤就列出本插件的收官约定。写回意见的提及不能代替共同检视与适应的说明；不过回答仍有成果、目标与度量等正确部分，不临时加严成全不达。
- **A3-r1、r2、r3**：已读三份原回答，维持部分；都解释了经典五天来源，却把本插件的无日程五阶段当作当前答案。两项判据一达一不达，不因行为已误触发再额外扣内容。
- **B2-r1、r2、r3**：维持达；抽查 r1 的原回答，明确说未建日志、已读约定，给出 Empathize 草稿与待 PO 定的问题，没有假称落盘。冻结判据评的是接手点与研究边界，本轮工具本就只读，不把未落盘新增为失败标准。
- **行为缺口另列，未抵内容**：B1-r1 未读 sprint-log；C1、C2 的 ideo 未触发且方法未读；D1 的 stakeholder 未触发（产品日志已读）。这些已见行为汇总，内容栏不因此扣分。

33 行先由 Haiku 子代理逐条看答复，Developer 复核上述争议；最终仍为 29 达、4 部分、0 不达。
