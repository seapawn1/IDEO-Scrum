---
name: plugin-guidance-vs-operational-content
description: IDEO-Scrum 内容分层原则——参考层只放操作型内容，指导型内容（角色定义等）留在源文档，不单独拆件
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0c2606bb-29eb-4a3c-b74e-868c157a2e8b
  modified: 2026-10-04T09:12:17.716Z
---

插件参考层（`references/`）只承载**操作型**内容——按冲刺节奏反复检索的东西（artifacts / events）。**指导型**内容（如 SGEP 角色定义）不另拆参考层，随源文档（`assets/`）提供；SKILL.md 里最多保留摘要。

**Why:** 2026-10-04 会话中，我（Claude）依 layout 工作流的结论先推荐把 roles 拆成 6 个参考文件（总论 + 5 角色），PO 先同意后又反思撤销：「这个其实是指导性质，我觉得没啥意义」——随后把 7ef9735 的摘录完全回滚：整章 227 行原文还回 asset，`scrum-roles.md` 及新拆文件全删，SKILL.md 的 Roles 条目删除。性质判断（操作 vs 指导）优先于对称性/同构对齐的考虑。

**How to apply:** 讨论参考层拆分时先问「操作型还是指导型」；指导型默认不拆、留源文档。相关：layout 形状 C（artifacts/events/roles 迁 skill 根分类目录）仅剩 artifacts/events 部分待议；roles 已明确不进参考层。
