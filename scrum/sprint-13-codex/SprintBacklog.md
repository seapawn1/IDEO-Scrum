# Sprint Backlog — Sprint 13 (codex)

> Started: 2026-11-09 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-13-codex` | Product Owner: SeaPawn | Scrum Master: Claude（Claude Code 主会话）| Developer: Codex（GPT，在 Codex 里跑）
> How to write this log: `sprint-log.md` in the scrum-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled at close; add none — remarks go in 3.2 Notes (`overview.md`, convention 15).

## 1. Why

### 1.1 Sprint Goal

<!-- The Product Owner decides it: this Sprint's one commitment (sprint-log.md, convention 3). -->

**Codex 版跟上**：Codex 里的 IDEO-Scrum 与 Claude Code 版一致——三个内核、四个角色、约定与模板都在；以后发版能照样同步；在 Codex 里开 Developer，装上就能照约定干活。

### 1.2 Definition of Done

<!-- The Product Owner picks them: the Definition of Done items that matter to this Sprint (product-log.md, convention 5). -->

Output Done 三条：内容忠实、可导航、无死链（产品日志 1.3），用在 Codex 包上。Claude 侧的描述不动，不跑 Claude 的触发测试。

## 2. What

### 2.1 Product Backlog Items

<!-- The Product Owner leads the selection; the Scrum Master and the Developer say when it is too much or too little. The selected items, copied word for word from the product log (sprint-log.md, convention 5). -->

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-43 | Codex 版——与 Claude Code 版一致 | 作为熟手，我想要 Codex 里装上的 IDEO-Scrum 与 Claude Code 版一致（三个内核、四个角色、约定与模板），以便在 Codex 里开的 Developer 也照同一套约定干活，和 Claude Code 里的 Master 靠冲刺日志协作 | Map ①（装插件，开会话） | M |

### 2.2 Refinement

<!-- The Scrum Master leads. What refinement settled, each point with who decided it; the acceptance criteria; the tests' method and pass lines (sprint-log.md, conventions 6 and 15). -->

**PO 定（2026-11-09）**
- 只选 PBI-43；Sprint Goal 如 1.1。
- Codex 版并入 main，不再单靠 codex 分支；前提是不影响 Claude Code 的使用。
- 本冲刺算在当前 Product Goal 之内（产品日志 1.2）。
- Developer 在 Codex 里跑（GPT），和 Master 只靠本日志通讯，PO 传话。
- Codex 里装着的旧版 ideo-scrum（3.2.0）不停用，Developer 可以用它进角色；收官时换成新版。

**怎么协作**（Master 定，PO 可改）
- 通道只有本日志。两边都在 `S:\IDEO-Scrum`、分支 `sprint-13-codex` 上干活，所以轮流：同一时间只有一方动仓库；动手前先读本日志的最新版。
- 分工照模板注释：Master 写 2.2 和审阅结果；Developer 写 3.1、3.2；PO 的放行写在 3.1 最后一行。
- 每轮做完：在冲刺分支提交，在 3.2 记一行，「Next」写明轮到谁、要对方做什么，然后停下。
- PO 传话只说一句：「轮到你了，读 `scrum/sprint-13-codex/SprintBacklog.md`。」
- 拿不准的事写进「Next」问 PO（overview 约定 9），停下等。

**Developer 先读**（以仓库里 5.1.2 的文件为准）
- 角色：`plugins/ideo-scrum/commands/developer.md`。文中「用 Skill 工具加载内核」，在 Codex 里改成直接读下面的 SKILL.md。
- 内核与约定：`plugins/ideo-scrum/skills/ideo-kernel/SKILL.md`、`skills/scrum-kernel/SKILL.md`、`skills/scrum-kernel/overview.md`、`skills/scrum-kernel/conventions/sprint-log.md`。
- 项目规矩：仓库根 `CLAUDE.md`。其中 plugin-validator、skill-reviewer、`reclaude`、Haiku 回归测试是 Claude Code 这边的工具，归 Master；Developer 用 Codex 自己的办法测。
- 旧版 `$developer`（3.2.0）和上面的文件说法不同时，照上面的文件。
- 上次同步（3.2.0）的做法在 codex 分支 `d307296`，可参考，不必照做。

**验收标准**
1. 内容一致：Codex 包里有三个内核（ideo、scrum、design）的全部文件和四个角色 skill。内核文件与 `plugins/ideo-scrum/skills/` 逐字相同；角色 skill 正文与 `plugins/ideo-scrum/commands/*.md` 相同。改动只限工具说法，逐条列在 3.2。
2. Claude Code 不受影响：Claude 侧装上后，技能与命令清单和 5.1.2 一样，plugin-validator 通过；`plugins/ideo-scrum/` 与 `.claude-plugin/marketplace.json` 没改动时视为满足（Master 核对）。
3. 同步能重跑：一条命令从 `plugins/ideo-scrum/` 生成 Codex 包；没有改动时重跑，`git status` 是干净的。
4. Codex 里能用：装上新版后，四个角色都能调用；给 `$developer` 一个开冲刺的任务，它读到 `conventions/sprint-log.md`。
5. 无死链：Codex 包里 markdown 的内部链接都能解析。
6. README 同步：Codex 的安装说明（不再要 `--ref codex`）和版本号（CLAUDE.md「维护规约」）。

**测试**（方法和过线标准先提交、后跑，跑完不改；sprint-log 约定 15）
- 1、3、5 用脚本核对。过线：0 处不一致（3.2 列出的工具说法除外）；重跑 0 改动；0 死链。
- 4 由 Developer 在 Codex 里用便宜的模型跑：四个角色各一题，再给 `$developer` 一题开冲刺；题目不带引导词（CLAUDE.md「回归测试」）。题目和模型先写进 3.1，Master 审过再跑。测的时候不动 PO 正在用的 Codex 安装。过线：角色 4/4 能调用，`$developer` 读到 `sprint-log.md`。
- 2 由 Master 核对。

**留给 How 的开放点**（Developer 在 3.1 提方案）
- Codex 包放在哪个目录；整份镜像，还是和 Claude 版共用一份源文件（以验收 2 为前提）。
- 哪些工具说法要改、怎么改：Skill 工具、`ideo-scrum:` 前缀、subagent 等。

**收官时再定**
- 版本号与发布；codex 分支怎么退役（推送前问 PO）。
- 本机 Codex 换装新版。
- Master 提醒 PO 核对 Product Goal（产品日志 1.2）。

**最后一步**：Developer 读完，先在 3.2 记一行，逐条复述验收标准、列出不清楚的地方；没有问题再写 3.1。

## 3. How

### 3.1 How

<!-- The Developer writes it (sprint-log.md, convention 7). The last line is the go-ahead (sprint-log.md, convention 8). -->

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

Go-ahead: （待 PO）

### 3.2 Notes

<!-- Whoever does the work writes the notes, in whatever form helps: each change and its reason, and what a new session needs to pick the Sprint up; they may refine the How (sprint-log.md, conventions 3 and 9). A session that picks up the Sprint reads these first. -->

| Date | What was done | Decision and reason | Evidence | Next |
| --- | --- | --- | --- | --- |
| 2026-11-09 | Planning 第 1、2 段：Master 写 1.1–2.2 | 见 2.2 | — | Developer：读本日志和「Developer 先读」，在 3.2 复述验收标准、列出不清楚的地方，再写 3.1；写完提交，停下等 Master 审 How、PO 放行 |

## 4. Review

<!-- Written at close by the Product Owner, the Scrum Master, and the Developer: the Increment; the Definition of Done and the acceptance criteria, item by item; what the review found; the stakeholders' view; changes to the product log and the Product Goal (sprint-log.md, convention 18). -->
