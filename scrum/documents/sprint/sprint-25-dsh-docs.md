# Sprint Backlog — Sprint 25 (dsh-docs)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-25-dsh-docs-4f4070` | Product Owner: SeaPawn | Scrum Master: IDEO-Scrum Master | Developer: Sprint 25 Developer
> Now: 已收官 · 2026-11-21，PO 确认 Review 通过；Claude Code 与 DSH 本地候选均为 `0.6.3`，未推送、未发布。
> Waiting for PO: None
> 归档：在办日志全文见 `8772923` 树中的 `SprintBacklog.md`；[文档交审](sprint-25-dsh-docs-docs-review.md)、[宿主证据和夹具说明](sprint-25-dsh-docs-host-evidence.md)就近保留。隔离会话原始记录在 `S:/IDEO-Scrum-Archives/sprint-25-dsh-docs/test-runs/`。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。 |
| --- | --- |

### 1.2 Definition of Done

[完整产品 DoD](../../ProductBacklog.md#13-definition-of-done) 继续生效。重点核对同源正文、导航与链接、插件校验、DSH 分发和版本；两宿主的新装和迁移另以实机证据逐项验，不以模型复述代替原生事件。

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-72 | DSH 分发：验收与跨宿主维护说明 | 作为用 DeepSeek Harness 的 solo 开发者，我想要同一套方法论也能装进 DSH，以便换宿主不换流程 | 分发：Claude Code + DSH | M |

### 2.2 Refinement

以 `b2679aa` 的 DSH 实现为基线，不重造分发包。Claude Code 走隔离的 Git 市场及版本缓存；DSH 走 Web 本地链接与 Standard 会话。新装、旧版迁移分别核加载来源、版本、原生入口、承诺、规则和日志不变。两宿主共用 `plugins/ideo-scrum/` 正文。DSH 的项目级 Agent 发现能力不在本期实证范围。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | 宿主能力与取证准备 | 固定版本来源、旧端与隔离矩阵 | ✓ 2026-11-20 两宿主测试起点和证据来源明确。 |
| H2 | 共用仓库规则及双语说明 | 唯一规则正文、安装／迁移／维护说明 | ✓ 2026-11-21 单源规则、文档与实测路径一致。 |
| H3 | 单独改号 | 两份清单、中英 README 和未发布条目 | ✓ 2026-11-20 本地候选均 `0.6.3`，与内容分开提交。 |
| H4 | Claude Code 新装及迁移 | 实际缓存、入口、承诺与规则证据 | ✓ 2026-11-20 `H4-A`／`H4-B` 过线。 |
| H5 | DSH 新装及迁移 | Web／Standard 原生事件与静态对账 | ✓ 2026-11-21 `H5-A`／`H5-B` 过线，完成 5/5。 |

## 4. Increment notes

- `90aff9a`：PO 直接授权该执行会话把原仓库规则原样迁入 `AGENTS.md`；`CLAUDE.md` 单向导入，不重写规则。`2800cc0` 单独同步候选版号，未写作已发布。
- `7ae0b49` 留 Claude Code `H4` Git 市场安装证据。DSH 实机在单独隔离实例由 Stakeholder 操作，未触碰 PO 的日常实例；原始记录不入仓。
- `6c57907` → `b52adac`：回填 DSH 安装、迁移和压缩说明，复核只实调一个原生角色并纠正前稿表述。`8772923` 补完成标记。
- **PO 收官授权（2026-11-21，本会话直接原话）**：「可以，后面你自主决定，收口所有分支，我都review认为通过」。委托本批 Review／Retro、归档、产品日志、本地 tag、合入及清理。改 Product Goal／Sprint Goal、取消 Sprint、推翻 PO 定案、PO 点名品味、另行修改 `CLAUDE.md` 及推送发布仍归 PO。

## 5. Test

| 宿主 | 实机结果及边界 |
| --- | --- |
| Claude Code `2.1.329` | `H4-A` Git 市场新装；`H4-B` 常规市场与插件更新直接由 `6.0.3` 降至 `0.6.3`，无需卸载重装。重开新会话核版本、原生入口、规则、承诺及压缩后复注；项目日志逐字节未变。 |
| DSH `0.2.2-rc.5` | `H5-A` Web 新装后在 Standard 核规则与承诺，压缩后复注；`H5-B` 分离环境由旧链接卸载后重加候选、重启、新开 Standard，核实际链接和原生事件。两组各自只实调 `/scrum-master`，四角色见于菜单；不把菜单写成四个实调，也不宣称同路径原地更新。 |

**Output DoD 对账**：两宿主共用正文；未新增第三方摘录，Sprint 21 既有署名欠项仍独立追踪。Sprint 25 候选的严格校验、DSH 6/6、187 链零错、文档自测 17/17、看板 42/42 通过；`npm pack --dry-run` 的候选清单为 100 个文件。以上实机结果对应各自隔离候选，不当作合流版本重测。完整陌生人首个冲刺 Outcome 未重跑。

**合流对账（`63b0f1e`）**：Claude 严格校验通过；双语文档 193 链零错、自测 17/17、看板自测 79/79、DSH 7/7。离线打包预检为 `0.6.3`、100 个文件，不含 Claude 专用 Agent、Skill 或 hook；合流未改 Sprint 25 的 DSH 适配器与包入口，也未另跑宿主实机。

**PO 决定收官（2026-11-21）**：PO 认定 Review 通过，批准本地收口；不发布候选。核对承诺原文：「换宿主不换规矩：使用 Claude Code 或 DSH 的人，照各自的说明就能装好 0.6.3、叫出角色，用上同一套方法论；已装 6.0.3 的人知道怎样迁移，维护者只需维护一份共用规则。」
