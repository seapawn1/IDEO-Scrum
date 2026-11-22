# 审阅包入口（Sprint 26 行 9、行 10）

给 Master 审定用。先读这页，再按下表的顺序读。行 9 还没做完（缺结果表与档位，见末尾），所以这是**草稿阶段的审阅包**，不是终版。

## 怎么读

| 顺序 | 文件 | 是什么 | 状态 |
| --- | --- | --- | --- |
| 1 | `review/memory-outline.md` | 方案与大纲：位置与名字、带上方式（A1，PO 已定）、共用或分角色、一行句型与 5 条示范、长文件判据、图与 Departures 表去处、尺寸提议、落盘后果、被否的做法 | 等 Master 审定（行 5） |
| 2 | `review/carrier-criteria.md` | 载体判据（已冻结）与 PO 选 A1 后的收窄 | 已提交；结果要等正式测 |
| 3 | `memory-draft/MEMORY.md`、`memory-draft/long/` | 装配后的完整草稿：102 行、14,148 字符；16 个长文件 | 3 行（`ask-the-po`、`who-gets-which-work`、`board-writer`）与 `roles-and-routing` 标「待 27」 |
| 4 | `review/review-<文件>.md` × 6（overview、product-log、board-log、sprint-log、design-log、ideo-log） | 每条旧规矩一节：旧文逐字｜出处与依据｜建议（留／改／并／删）｜新行｜备注｜待 27；每份文末是该文件的非编号块（引言、署名、图、表，六份共 29 个）的去向 | 111 条＋29 个块，全部有去向 |
| 5 | `review/map-old-new.md` | 旧→新、新→旧两张覆盖表 | 与草稿同步生成 |
| 6 | `review/dsh-test-page.md` | 给秘书会话的 DSH 测页（只测 A1） | 等 Master 经 Supporter 请 PO 开 DSH |

## 检查结果（我跑的，2026-11-23）

| 检查 | 结果 |
| --- | --- |
| `check_drafts.py check`：每条旧规矩有去向、每个新行对得上旧规矩、句柄唯一、`via` 与合并指向有效、长文件都被指到 | 140 个条目（111 条规矩＋29 个块）、102 个句柄，0 个问题 |
| `assemble_memory.py`：占位符、句柄引用、长文件引用与写出是否一致 | 占位符 0 个未解；反引号里的名字都是句柄或长文件；被引用的长文件都已写出，写出的都被引用 |
| 引文逐字核对（`quote_check`，旧文里引号内的引文与 Departures 表） | 17 处里 16 处在装配后的 Memory 里逐字出现；另一处是 ideo-log#2 的「the IDEO five-stage method」，是用户的叫法，不是 PO 原话或原书文字，清单行没带，意思在 ideo-kernel、design-kernel 的描述里 |
| 行长（硬线 150 字符） | 无超线；62 行超过软线 130 |
| 核验（行 2）：13 块 × 2 个视角 ＝ 26 个文件，全部到齐 | 已用上；我覆盖核验的几处写在对应标注的 `reason` 里，见 SprintBacklog 第 4 章「核验结果用上」 |

## 要 Master 定的

1. 行 5：`review/memory-outline.md` 里的尺寸提议（上限取「A1 过 ② 的最大一档」与「每技能 5,000 token 线的 80%，约 16,000 字符」中小的）、子代理那句加 memory、一份共用加角色标签。
2. 载体测试的范围：Master 写「①②④⑤ 两档」，我读作 ①② 两档、④ 一档（冻结条文：与尺寸无关的只测一档），要 ④ 也两档就加 6 个会话；③ 与另测（9 个会话，只报）跑不跑。
3. 我覆盖核验的几处（board-log#4、#5、#9 改回「留」；design-log#21、#24 并入 sprint-log 的两行）要不要认。
4. 抽查一批理由与事实（行 9 里写给你的）。

## 行 9 还差

- 载体测试的结果表与档位（等你说空闲内存 ≥ 3 GB 开跑）；之后「预算」一项才有可比的线，行 6–8 括号里的那一项也在这时核。
- 27 合入后同步「待 27」的几行与 `roles-and-routing`（行 11）。
