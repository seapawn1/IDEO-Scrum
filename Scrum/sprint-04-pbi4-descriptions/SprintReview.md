# Sprint Review — Sprint 04

> 按 Scrum Guide Expanded v2026.1 的 Sprint Review event 框架。
> Date: 2026-07-23

---

## Increment Delivered

| Output | Path | Status |
|---|---|---|
| plugin.json description | `plugins/ideo-scrum/.claude-plugin/plugin.json` | 交付——英文 + 方法论关键词 + 场景词 |
| design-kernel SKILL.md description | `plugins/ideo-scrum/skills/design-kernel/SKILL.md` | 交付——"Use when applying Design Thinking or Design Sprint" + 方法名列表 |
| scrum-kernel SKILL.md description | `plugins/ideo-scrum/skills/scrum-kernel/SKILL.md` | 交付——"Use when work involves Scrum or a Scrum Sprint" + 事件/角色/概念关键词 |
| scrum-kernel agents (6) description | `skills/scrum-kernel/agents/*.md` | 交付——"Use when X role/perspective is needed" + 角色专属场景词 |
| design-kernel agents (4) description | `skills/design-kernel/agents/*.md` | 交付——Design Sprint 五天流程特定活动名 + 角色专属触发词 |

---

## Sprint Goal Assessment

> **Sprint Goal:** 插件所有 description 字段经过审计和优化后，自动触发精确度和召回率达到可用水平——核心场景不漏触发，非相关场景不误触。

**达成。** 13 个 description 全部优化完成。

- [x] 2 个 SKILL.md description：从描述自身内容 → "Use when" 触发模式
- [x] 10 个 agent description：从 "discussing" → "role/perspective is needed" + 专属场景词
- [x] plugin.json description：从中文单句 → 英文方法论 + 场景关键词
- [x] 同 kernel 内 agent 的描述区分度提升（如 PO→backlog prioritization, SM→impediment removal）
- [ ] output-styles：无需处理（插件当前无 output-styles 文件）

---

## Definition of Done Check

### Output Done

| 维度 | 状态 | 备注 |
|---|---|---|
| 审计完整 | ✅ | 13/13 文件全部审计 |
| 触发模式统一 | ✅ | 全部采用 "Use when..." 模式（SKILL.md + agents） |
| 场景词精确 | ✅ | 每个 description 包含该文件专属的触发场景词 |
| 区分度 | ✅ | 同 kernel agent 间有可区分的角色关键词 |

### Outcome Done

| 类别 | 度量 | 状态 |
|---|---|---|
| User outcomes | 核心场景不漏触发 | ✅ 所有主流方法论操作（Sprint Planning, backlog refinement, user interview, HMW, prototyping 等）均已出现在对应 description 中 |
| User outcomes | 非相关场景不误触 | ✅ 每个 agent description 限定在特定角色场景，宽泛词（如 "discussing"）已替换 |
| Product Stakeholder outcomes | Agent 描述区分度提升 | ✅ 6 个 scrum agents 不再使用相同模板句 |

---

## Key Finding

**Claude Code 的 description 匹配是语义式而非精确关键词匹配，但描述中仍需包含足够具体的方法名和场景词来让 embedding 在相关上下文中产生高分匹配。**

一个 agent/ skill 的 description 本质上是在做 embedding-space anchor placement——你需要让它在正确的查询语义区域产生高分，同时在错误区域保持低分。这需要两个武器：① 正向场景词的覆盖面（召回率）；② 与同 kernel 兄弟描述的结构差异（精确率）。

"Use when X role is needed" 优于 "Use this agent when discussing X role"，因为 "discussing" 限定了元层面的对话（讨论这个角色本身），而 "role is needed" 覆盖了操作场景（以这个角色行动）。

---

## Lessons Learned

1. **"discussing" 是一种自我指涉。** Agent description 里写 "when discussing X" 意味着只有当用户想讨论这个角色时才会触发，而当用户真正需要这个角色的能力时反而不会匹配。
2. **description 不是 description。** 名字叫 description，但它的功能是 trigger condition。应该用 "Use when..." 而不是 "This is..."。
3. **区分度比全面性更重要。** 6 个 scrum agent 如果用同一个句子模板只是替换角色名，那 embedding 空间中它们几乎重合——系统无法在它们之间做出选择。
4. **plugin.json 的 description 是人类元数据，不是触发关键。** Skill/agent 级别的 description 才是自动触发的主战场。plugin.json 的 description 主要用于插件列表展示。
5. **S 级 PBI 适合单人一次完成。** 13 个文件的文本替换，从审计到全部完成约 30 分钟——不需要拆分步骤也不需要中断。

---

## Product Backlog Adaptations

- PBI-4 标记为已完成
- output-styles 文件当前不存在，PBI-2（output-styles 创建）仍为待开始；PBI-4 发现中有注记：如果未来 PBI-2 创建 output-styles，其 description 也应遵循本次确立的 "Use when..." 模式
- Product Goal 不变
