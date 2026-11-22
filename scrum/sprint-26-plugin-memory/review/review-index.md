# 审阅包入口（Sprint 26 行 9、行 10）

给 Master 审定用。先读这页，再按下表的顺序读。行 9 还没做完（结果表与档位已出，还差 27 同步后的几行，见末尾），所以这是**草稿阶段的审阅包**，不是终版。

## 怎么读

| 顺序 | 文件 | 是什么 | 状态 |
| --- | --- | --- | --- |
| 1 | `review/memory-outline.md` | 方案与大纲：位置与名字、带上方式（A1，PO 已定）、共用或分角色、一行句型与 5 条示范、长文件判据、图与 Departures 表去处、尺寸提议、落盘后果、被否的做法 | Master 审定 2026-11-23（行 3、5 已标 ✓） |
| 2 | `review/carrier-criteria.md`、`review/carrier-results.md` | 载体判据（已冻结）与 PO 选 A1 后的收窄；正式测的结果表 | 测完（2026-11-23）：A1 两档都过硬判据，建议尺寸上限 16,000 字符，等 Master 审定 |
| 3 | `memory-draft/MEMORY.md`、`memory-draft/details/` | 装配后的完整草稿：105 行、14,741 字符（上限 16,000）；15 个细则文件（原叫长文件，PO 认同改名）；写看板的 4 行直接指向 `plugins/ideo-scrum/board/board-log.md` | 27 已同步：三行「待 27」已重写，净增 `answers-back`、`po-word-relayed`、`relay-limits`；`roles.md` 已按约定 14 写定 |
| 4 | `review/review-<文件>.md` × 6（overview、product-log、board-log、sprint-log、design-log、ideo-log） | 每条旧规矩一节：旧文逐字｜出处与依据｜建议（留／改／并／删）｜新行｜备注｜待 27；每份文末是该文件的非编号块（引言、署名、图、表，六份共 29 个）的去向 | 111 条＋29 个块，全部有去向 |
| 5 | `review/map-old-new.md` | 旧→新、新→旧两张覆盖表 | 与草稿同步生成 |
| 6 | `review/dsh-test-page.md` | 给秘书会话的 DSH 测页（只测 A1） | 已测完，判据 ⑥ 过；结果在大纲第 10 节 |
| 7 | `review/s27-increment.md` | 27 增量表（行 11 的底稿）：27 改了哪些规矩对草稿的影响、board-log 的去处、Supporter 那块的草案 | 同步前的预读；A1 正式测已跑完，等 Master 说同步 main |

## 检查结果（我跑的，2026-11-23）

| 检查 | 结果 |
| --- | --- |
| `check_drafts.py check`：每条旧规矩有去向、每个新行对得上旧规矩、句柄唯一、`via` 与合并指向有效、细则文件都被指到、指向 board-log 的那几行路径真有这个文件 | 140 个条目（111 条规矩＋29 个块）、105 个句柄，0 个问题 |
| `assemble_memory.py`：占位符、句柄引用、长文件引用与写出是否一致 | 占位符 0 个未解；反引号里的名字都是句柄或长文件；被引用的长文件都已写出，写出的都被引用 |
| 引文逐字核对（`quote_check`，旧文里引号内的引文与 Departures 表） | 17 处里 16 处在装配后的 Memory 里逐字出现；另一处是 ideo-log#2 的「the IDEO five-stage method」，是用户的叫法，不是 PO 原话或原书文字，清单行没带，意思在 ideo-kernel、design-kernel 的描述里 |
| 行长（硬线 150 字符） | 无超线；62 行超过软线 130 |
| 核验（行 2）：13 块 × 2 个视角 ＝ 26 个文件，全部到齐 | 已用上；我覆盖核验的几处写在对应标注的 `reason` 里，见 SprintBacklog 第 4 章「核验结果用上」 |

## 已定与待定

已定（Master 2026-11-23）：`review/memory-outline.md` 审定，含尺寸上限（A1 过 ② 的最大一档与约 16,000 字符中小的）、子代理那句加 memory、一份共用清单加角色标签；④ 测一档；③ 与另测照跑、只报；A1 过不了 ② 时经 Supporter 报 PO、要不要补测 14,000 字符一档由 Master 定。

待 Master 定：

1. 我覆盖核验的几处（board-log#4、#5、#9 改回「留」；design-log#21、#24 并入 sprint-log 的两行）要不要认。
2. 抽查一批理由与事实（行 9 里写给你的）。

## 行 9 还差

- 载体测试已测完：结果表 `review/carrier-results.md`；档位与尺寸上限（20,000／16,000）等 Master 审定；Master 已审定（档位 20,000、上限 16,000）；行 6–8 的预算一项已核：14,741 字符在 16,000 内。
- 27 同步与改稿（行 11）已做完，结果在 `review/s27-increment.md` 最后一节；还差：DSH 副本按新基线重做、对抗审查（Master 排在内存够的时候发起 Codex）、PO 中途看一遍（经 Supporter 转意见，记在 `review/po-opinions.md`）。
