# PO 中途看一遍：意见账（Sprint 26）

2026-11-23，PO 经 Master 定（Master 转述）：PO 有空，要和 Supporter 一起中途过目 Memory 草稿；本期「PO 免审」改成「PO 中途看一遍」，其余安排不变。

怎么记：

- PO 的意见由 Supporter 照原话、带上时间和会话名转给 Master 和我；意见用句柄指明是哪一行。
- 我在下面的表里逐条记（原话逐字、收到的时间与来源会话），照改，写明怎么改的；跟别的决定冲突的，报 Master 协调，状态写「报 Master」。
- 同步、改稿照常进行，不等 PO 看完。
- **不给句柄改号**；要改号的，先在「句柄别名」表里留别名（旧句柄、新句柄、日期、原因），再改。

PO 可读的东西：`memory-draft/MEMORY.md`（清单，105 行）、`memory-draft/details/`（15 个细则文件）、`review/review-index.md`（入口）、`review/review-<文件>.md`（每条旧规矩的旧文、依据、建议、新行）。

## 意见账

| 收到的时间 | 来源会话 | 句柄 | PO 原话（逐字） | 我怎么处理 | 状态 |
| --- | --- | --- | --- | --- | --- |
| — | — | — | （还没有收到意见） | — | — |

## 句柄别名

| 旧句柄 | 新句柄 | 日期 | 原因 |
| --- | --- | --- | --- |
| — | — | — | （没有改过句柄） |

## 待 PO 看（我带上的开放点，Supporter 陪 PO 审时一并带上）

| 句柄与位置 | 是什么 | 我现在的做法 |
| --- | --- | --- |
| 设计清单里「git 动作须明确许可」（`details/roles.md`「What only the Product Owner decides」设计那张，关联 `outward-needs-po`、`log-is-the-handoff`、`stage-gates`） | 旧的设计规矩要求 commit、merge、删分支、push 在执行前都要 PO 明确许可，比旧的冲刺规矩严（冲刺只要求提交在放行范围内） | 转换时不改含义，照旧文保留；PO 若要冲刺与设计一样，在这里说（2026-11-23 Master 定） |
