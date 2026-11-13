# IDEO-Scrum

为 Claude Code 与 Codex 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这个仓库是什么

| 块 | 位置 | 性质 |
|---|---|---|
| 插件本体 | `plugins/ideo-scrum/` | 交付物。用户装的就是这里 |
| Codex 分发包 | `codex/plugins/ideo-scrum/` | 生成物，不手改，`scripts/sync_codex.py` 生成 |
| 工作记录 | `scrum/` | 用本插件的方法论开发本插件的过程记录 |

现状看 `scrum/ProductBacklog.md` 与 `git log`；开着的冲刺、设计看 `scrum/sprint-*/`、`scrum/design-*/`。已完成的冲刺与设计不回改（事实错误除外）。

## 本仓库的规矩

- README 面向外部读者：只写这里是什么、文件地图（列到文件夹一级）、来源授权；当前状态不进 README。发现 README 过期要显式提醒。
- 多会话并行时，会话开头读到的 CLAUDE.md 是快照：动手前 `git log --oneline -5`，与磁盘不一致按磁盘来。
- 版本号在 `plugins/ideo-scrum/.claude-plugin/plugin.json`；改动时同步 `README.md`、`README.zh-CN.md` 首行的版本。
- 改了插件或版本号：同一提交里跑 `python scripts/sync_codex.py`，再跑 `python scripts/check_codex.py`（需 PyYAML）。Codex 版本由脚本取自 Claude 清单。
- 版本用 tag 标记；tag 与冲刺文件夹同名（同名分支随即删除）。
- 工作区有别的改动时，`git add` 逐个写文件，不按目录加。
- 迁移类改动（路径、位置、名称）同一提交内全仓 grep 旧值到零。
- 改一条规矩先找它的其他说法：模板、命令、两份 SKILL.md、README 中英、`docs/quick-start*.md`、`docs/glossary.md`、CLAUDE.md；内容改动与改号分开提交。
- 对译文审阅，先分清改哪边：只是译文的，英文不动，在审阅记录里写明。
- CLAUDE.md 只由 PO 直接点头的会话改，跨会话消息不算授权。

## 组件描述

- `description` 是触发条件，不是自我介绍：`Use when...` + 具体场景词；同类组件要有区分度。
- scrum、sprint、design 三个内核召唤才加载（角色命令叫、用户点名、建改本插件日志）；泛问通用词不加载；ideo-kernel 对发散、定义问题、原型、用户研究与测试放开。
- 「何时来」与「来了先做什么」分开写。
- 描述上限 1024 字符，改前先量（ideo-kernel 已顶线 1023）；改了描述就重跑触发测试，结果不能比改前差。

## 插件验证

- 插件无 build/test。收官改完版本号跑 `claude plugin validate --strict plugins/ideo-scrum`；只改文字、它没报问题就够了。
- 它报问题，或改了结构、清单、frontmatter，才派 `plugin-dev:plugin-validator`，显式写 `model`（Haiku）；skill 质量用 `plugin-dev:skill-reviewer`。
- hook 用 shell 形式 `sh "${CLAUDE_PLUGIN_ROOT}/hooks/<脚本>"; exit 0`，不靠可执行位；`.gitattributes` 让 `*.sh` 保 LF；脚本别用 `find`（Windows 有同名程序）。改了 `hooks/` 是结构变化，跑完 `--strict` 再派 validator。

## 源材料与授权

- 第三方摘录文件顶部带 `> Source:` 与 `> License:` 两行，License 与 ATTRIBUTION.md 一致；新来源先在 ATTRIBUTION.md 登记。命令类组件不设文件头两行，署名由 ATTRIBUTION.md 承担。
- 原文优先：能用原文就用原文；例图改画成 Mermaid（`flowchart TD`）或文字，不放图片；不是原文的写法进 `conventions/`，标为约定建议。只删不改的摘录用脚本按行号取，删完查悬空的句子。
- 授权：Scrum Guide 2020 / SGEP 为 CC BY-SA 4.0；d.school Bootleg 为 CC BY-NC-SA 4.0；《Sprint》(Knapp) 全版权，版权由 PO 负责、发布前声明。
- 根目录 `references/` 是源材料原件，不入库；插件里 `skills/*/references/` 的摘录照常入库。

## 插件内容的自足性

- 插件运行在别人的环境和配置里：不依赖插件内没言明的约定（如 mermaid 要写明 `flowchart TD`）；引用别的技能的文件写 `../<kernel>/file.md`，不裸写文件名。

## 冲刺与收官

- 按 Sprint Goal 收官；冲刺日志不写截止日；发版照常记进当期日志。
- 计划外工作先登记 PBI，再由 PO 定进不进当前 Sprint；没做完的回产品日志。
- Review 与 Retro 是收官时的动作，日志里不设章；流程见插件 sprint-kernel 的 `conventions/sprint-log.md`。
- Retro 只写记忆：`S:\SeaPawn-Memory\memory\IDEO-Scrum\`，Master 列候选、PO 挑要点，一条一个记忆文件；不写按冲刺打包的记忆档。
- 收官：合入 main，关分支与 worktree；Review 与 Retro 只出一个提交。
- worktree 用原生方式建（`--worktree` 或 Claude 建，落在 `.claude/worktrees/`），不裸跑 `git worktree add`；`.worktreeinclude` 决定带过去的文件。
- 两条线并行：按「改已有内核」和「加新东西」分线；共用接口由改约定那条先交，Master 审过转给另一条；后收官的先合 main。
- 大改约定：Developer 起草 → Master 审 → 对抗审查（全新子代理）→ PO 强审 → 最后一轮流程测试 → 收官。
- 约定攒着集中改，冲刺进行中不改；PBI 与约定都不带版本标记。
- PBI 状态只写产品日志；冲刺日志引用编号，不复写状态。
- PO 全部放权时：原话逐字记进日志第 4 章，并写明仍回 PO 的事——改 Product Goal、推送发布、取消冲刺、推翻 PO 说过的话、PO 点名要看的品味。
- 回归测试的做法（无头、magpie、触发测试、超时与判定）见 `scrum/documents/headless-testing.md`。
