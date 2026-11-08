# Sprint Backlog — Sprint 12 (overview-to-root)

> Started: 2026-11-09 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-12-overview-to-root` | Product Owner: SeaPawn | Scrum Master: Claude（主会话）| Developer: Claude（Master 兼任）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).

## 1. Why

### 1.1 Sprint Goal

**总览提到入口**：overview.md 挪到 scrum-kernel 根目录，与 SKILL.md 并列；所有说它在哪的地方都改对；从 SKILL.md 一眼就看到总览。

### 1.2 Definition of Done

Output Done 三条：内容忠实、可导航、无死链。描述不动，不跑触发测试。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-42 | 总览挪到 scrum-kernel 根目录 | 作为熟手，我想要总览和 SKILL.md 并列，以便打开技能就先看到它，不用进 `conventions/` 去找 | 插件 scrum-kernel | S |

### 2.2 Refinement

- PO 定（2026-11-09）：overview.md 挪到 scrum-kernel 根目录，与 SKILL.md 并列；推送并发新版。
- Master 定：按名字引用的「`overview.md`, convention N」不改（文件名唯一）；product-log、sprint-log 第一行写明它在技能根目录；总览自己列的其他文件改成 `conventions/…`；`scrum/documents/` 里的归档是历史，不改。
- 验收：插件、README、CLAUDE.md 里没有 `conventions/overview.md`；改过的每条路径都在；条号引用都对到短名。

## 3. How

### 3.1 How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 挪文件、改路径 | overview.md 在根目录；两份 SKILL.md、四个命令、design-log、两份模板、product-log、sprint-log、README 的说法 | 脚本：路径 0 缺、条号 0 错 |
| 2 | 审阅 | 全新子代理核 diff | 无必改项 |
| 3 | 收官发布 | 归档、产品日志、CLAUDE.md、v5.1.2、tag、合入、推送、更新插件 | 本机插件 5.1.2 |

**Key choices**

- 小冲刺，Master 兼 Developer，审阅交全新子代理。

**Risks and open points**

- 模型照旧到 `conventions/` 里找总览：两份 SKILL.md 和四个命令都直接写了新位置。

Go-ahead: 2026-11-09，PO（「我真的想这样做。然后想让你重新再推送」）——冲刺分支上可以提交；收官时合入 main，打 tag `v5.1.2` 与 `sprint-12-overview-to-root`，推送，更新本机插件。

### 3.2 Notes

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-09 | 工作项 1：`git mv` 挪文件，改 15 处说法，版本 5.1.2 | 见 2.2 | 路径 85 + 13 处都在；条号 64 处 0 错；全仓无 `conventions/overview` | 工作项 2 |

## 4. Review

<!-- Written at close by the Product Owner, the Scrum Master, and the Developer: the Increment; the Definition of Done and the acceptance criteria, item by item; what the review found; the stakeholders' view; changes to the product log and the Product Goal (sprint-log.md, convention 18). -->
