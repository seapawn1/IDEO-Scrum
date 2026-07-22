# Sprint Review — Sprint 05

> 按 Scrum Guide Expanded v2026.1 的 Sprint Review event 框架。
> Date: 2026-07-23

---

## Increment Delivered

| Output | Path | Status |
|---|---|---|
| agent-designer output-style | `plugins/ideo-scrum/output-styles/agent-designer.md` | 交付——IDEO 五模式打底，agent 设计结对风格（seapawn=Decider, Claude=Facilitator），结论先行，先发散后收敛 |
| developer output-style | `plugins/ideo-scrum/output-styles/developer.md` | 交付——Developer 角色，Sprint Backlog/DoD/Daily Scrum/Sprint Review/Retro 完整节律，行为准则 |
| scrum-master output-style | `plugins/ideo-scrum/output-styles/scrum-master.md` | 交付——Scrum Master 角色，服务 Team+PO，守护三大支柱+五项价值观，仪式优先 |

---

## Sprint Goal Assessment

> **Sprint Goal:** 插件新增 output-styles——3 个角色型输出风格放入插件 `output-styles/` 目录，可通过 `/config` 切换。

**达成。** 3 个 output-style 文件就位，格式正确，可通过 `/config` 选择。

- [x] 3 个文件放入 `plugins/ideo-scrum/output-styles/`
- [x] frontmatter 格式正确（name, description, keep-coding-instructions）
- [x] "ClaudeDream" 项目引用已修正为 "当前项目"

---

## Definition of Done Check

### Output Done

| 维度 | 状态 | 备注 |
|---|---|---|
| 格式正确 | ✅ | 全部使用 frontmatter + markdown body 格式 |
| 可发现 | ✅ | 位于 `plugins/ideo-scrum/output-styles/`，符合插件标准布局 |
| keep-coding-instructions | ✅ | 三个文件均设为 `true`——角色风格在编码场景中使用，保留编码指令合理 |
| 项目引用 | ✅ | "ClaudeDream" → "当前项目" |

### Outcome Done

| 类别 | 度量 | 状态 |
|---|---|---|
| User outcomes | 用户可通过 `/config` 切换风格 | ✅ 三个风格均可在设置中选择 |
| User outcomes | 切换后行为调性与角色一致 | ✅ 每个风格文件包含完整的身份、职责、行为准则 |

---

## Lessons Learned

1. **output-style 有两种形态**：模式型（改变探索/综合/发散的行为倾向）和角色型（定义职责、节律、边界）。本次交付的是角色型——比模式型更高承诺，不只是改变语气，而是定义了一整套行为契约。
2. **项目名引用要通用化**：`developer.md` 和 `scrum-master.md` 原始内容包含 "ClaudeDream 项目"——插件文件应使用通用引用（"当前项目"）。

---

## Product Backlog Adaptations

- PBI-2 标记为已完成
- Product Goal 不变
