# 维护 IDEO-Scrum

本页写给在 Claude Code 与 DeepSeek Harness（DSH）两个宿主之间维护本仓库的人。如果你是用插件做自己的项目冲刺，请看[快速上手](quick-start.zh-CN.md)、[README](../README.zh-CN.md) 和[词汇表](glossary.md)。([English](maintaining.md))

## 双宿主，正文只维护一份

`plugins/ideo-scrum/` 是两个宿主唯一的共用方法论正文来源。DSH 不另存生成包，也没有同步脚本。

| 部位 | Claude Code | DeepSeek Harness（DSH） |
| --- | --- | --- |
| 角色、内核、日志模板与看板文件（`plugins/ideo-scrum/commands/`、`plugins/ideo-scrum/skills/`、`plugins/ideo-scrum/template/`、`plugins/ideo-scrum/board/`） | 经 [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json)（`./plugins/ideo-scrum`）与 [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) 加载 | 由 [`dsh/index.js`](../dsh/index.js) 在运行时直接从 `plugins/ideo-scrum/` 注册 |
| 承诺上下文 | [`hooks.json`](../plugins/ideo-scrum/hooks/hooks.json) 在 `SessionStart` 与 `UserPromptSubmit` 用 POSIX `sh` 跑 [`commitments.sh`](../plugins/ideo-scrum/hooks/commitments.sh) | [`dsh/index.js`](../dsh/index.js) 通过 [`dsh/commitments.js`](../dsh/commitments.js) 注册 `systemPrompt.context`（`ideo-scrum:commitments`，`order: 130`，`interpolate: false`） |
| 打包与元数据 | [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) 与 [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) | [`package.json`](../package.json)（`@seapawn/ideo-scrum`）、[`cordis.patch.yml`](../cordis.patch.yml)、[`dsh/locale/en.json`](../dsh/locale/en.json)、[`dsh/locale/zh.json`](../dsh/locale/zh.json) 与 `plugins/ideo-scrum/icon.png` |

- **角色与内核注册（`dsh/index.js`）**：剥离 YAML frontmatter（要求单行双引号 JSON 兼容的 `description`，且 `SKILL.md` 的 `name` 与目录名一致），注册三个内核加 Memory 与四个用户可调用角色（`/scrum-master`、`/developer`、`/stakeholder`、`/supporter`，去掉 `ideo-scrum:` 前缀），在每个角色正文前加上 DSH 工具映射与路由提示，并按序预载 `ideo-kernel`、`scrum-kernel` 和 `memory` 原文，同时保持 `sprint-kernel` 按需加载；压缩后，若 Memory 的正文已不在对话里，命名上下文 `ideo-scrum:memory` 会提示重新加载。
- **打包白名单（`package.json`）**：`files` 只列 `cordis.patch.yml`、`dsh/`、`ATTRIBUTION.md`、`plugins/ideo-scrum/commands/`、`plugins/ideo-scrum/skills/`、`plugins/ideo-scrum/template/`、`plugins/ideo-scrum/board/` 与 `plugins/ideo-scrum/icon.png`（不包含 `hooks/` 和 `.claude-plugin/`），不带 `dependencies` 或 `scripts`，且 `engines.dsh` 写为 `>=0.2.2-rc.5 <0.3.0`。
- **承诺适配（`dsh/commitments.js`）**：在最近的 `.git` 边界内查找对应标题下的 `Commitment`（`承诺`）行（[Memory](../plugins/ideo-scrum/skills/memory/SKILL.md) 的 `goal-fixed`、`commitment-table`），跳过软链接的 `scrum/` 目录，多冲刺并存时只报数量，并遵循 `IDEO_SCRUM_COMMITMENTS=off`；压缩后补入依赖 DSH 对命名 `runtime-context` 的处理，在 DSH `0.2.2-rc.5` 配 `0.6.3` 上已实机验证（2026-11-21）：压缩后 `runtime-context` 快照逐字携带同样 3 条承诺。

## 仓库规则从哪里读

[`AGENTS.md`](../AGENTS.md) 是唯一的仓库共用规则正文。[`CLAUDE.md`](../CLAUDE.md) 只保留 `@AGENTS.md`——单向导入，且 `AGENTS.md` 中没有循环回引 `@CLAUDE.md`。维护者只更新 `AGENTS.md`；`CLAUDE.md` 仍只由 PO 直接授权的实际执行会话修改。

- **Claude Code（`0.6.3` 已实机验证，Claude Code `2.1.329`）**：读取 `CLAUDE.md` 并单向导入 `@AGENTS.md`。隔离测试会话（2026-11-20）中，加入规则文件前 `/context all` 不显示任何记忆文件，加入后只显示项目自己的 `CLAUDE.md` 与 `AGENTS.md`，没有来自用户设置或上级目录的内容。
- **DSH `0.2.2-rc.5`（固定源码事实，另有 `0.6.3` 实机验证）**：固定提交 `9c2670d3bce5275e0d1610272958121af87787bb` 显示 `dsh-base` 默认启用指令加载器，从 `.git` 根到工作目录读取 `AGENTS.md` 与 `CLAUDE.md` 并在同目录相同正文时去重（[`agent-instructions/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L30-L42)、[`config.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/src/config.ts#L11-L46)），且**不解析 `@path` 导入**（[`README.md#L223-L224`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L223-L224)）——因此 DSH 直接依赖 `AGENTS.md`，不经 `CLAUDE.md` 导入。实机验证（2026-11-21，隔离实例，DSH `0.2.2-rc.5` 配 `0.6.3`）：首轮只加载项目自己的 `AGENTS.md` 与 `CLAUDE.md`——digest 与磁盘文件一致——不重复、不串入上级目录或用户配置；新装与迁移后各验一次。
- **项目级 Agent 与命名 preset（未证实）**：上游 `dsh-v0.2.2-rc.5` 支持 Cordis 命名 preset 注册（[`agent-preset/src/index.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/preset/agent-preset/src/index.ts#L11-L29)）和受约束的进程内子代理 preset 选择（[`tool-subagent/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/subagent/tool-subagent/README.md#L50-L71)），这**不能**证明按项目自动发现 Agent 文件，也不同于 `.agents/skills` 或本包的 `/stakeholder`。DSH 项目级 Agent 支持目前未证实，也不属于本分发包范围。

## 已装用户怎样迁移

从 `6.0.3` 到 `0.6.3` 属于 SemVer 版本号下调（`6.0.3` > `0.6.3`）。**两个宿主的路径都已实机验证。** Claude Code：在 `2.1.329` 上（2026-11-20，隔离的 Git 市场夹具与版本缓存），`claude plugin marketplace update ideo-scrum` 后接 `claude plugin update ideo-scrum@ideo-scrum` 返回 `updateOutcome: "updated"`（`oldVersion` `6.0.3` → `newVersion` `0.6.3`），无需卸载重装；新会话加载 `0.6.3` 缓存目录，当时的四个角色、四个内核、承诺 hook 与 `/compact` 复注均通过，`scrum/` 逐字节未变。DSH `0.2.2-rc.5`：指向本地目录的链接在插件详情页没有原地更新，只有**卸载**；实测通过的 `6.0.3 → 0.6.3` 路径（2026-11-21，隔离实例）是：**卸载**旧链接，**添加插件**填新路径，重启 DSH，新开 **Standard** 会话——加载的 base 目录切到新检出，`/scrum-master`（预载 `ideo-kernel` → `scrum-kernel`）、3 条承诺与项目两份规则文件均从原生事件核验，`scrum/` 未变；原地更新链接仓库**未单独实测**。公开文档中须继续标明[安装说明](../README.zh-CN.md#安装)里的 DSH 宿主版本（`0.2.2-rc.5`）不是插件版本（`0.6.3`）。

| 宿主 | 旧版基线 | 升级路径与证据状态 |
| --- | --- | --- |
| Claude Code | `v6.0.3`（`d681c69`），通过[版本缓存](https://code.claude.com/docs/en/plugins/loading#versions-and-updates)从 `./plugins/ideo-scrum` 市场安装 | **已实机验证（2026-11-20，Claude Code `2.1.329`）**：`claude plugin marketplace update ideo-scrum` + `claude plugin update ideo-scrum@ideo-scrum` 直接接受降号（`6.0.3 → 0.6.3`，`updateOutcome: "updated"`）；`claude plugin list` 与新会话都指向 `0.6.3` 版本缓存路径；角色、内核、启动与 `/compact` 后承诺 hook 均已核验；`scrum/` 未变。 |
| DSH（`0.2.2-rc.5`） | 本地目录链接至提交 `b2679aa`（`@seapawn/ideo-scrum`，`private: true`，非公开注册表发布版） | **已实机验证（2026-11-21，隔离实例）**：插件详情页对本地链接没有原地更新，只有**卸载**；卸载后**添加插件**填新路径、重启、新开 **Standard** 会话，加载的 `0.6.3`（profile 的包条目与 Junction 均切换），`/scrum-master`（预载 `ideo-kernel` → `scrum-kernel`）、3 条承诺与项目两份规则文件均从原生事件核验；`scrum/` 未变。原地更新链接仓库**未单独实测**。 |
| Claude Code `0.7.0` | 从 `0.6.3` 过来，同一个市场路径 | 2026-11-23，本机 `claude plugin update` 从 0.6.3 到 0.7.0 成功，`claude plugin list` 显示 0.7.0 enabled；Claude Code 2.1.326；重开会话后的入口核对待做 |
| Claude Code `0.7.0` | 从 `6.0.3` 过来，同一个市场路径 | 未核 |
| DSH `0.7.0` | 从 `0.6.3` 的本地链接检出过来 | 2026-11-23，Supporter 用桌面端 profile 的临时副本核过（指向主检出的 0.7.0；桌面端本身未开；DSH `0.2.2-rc.5`，`npx @latest`）。菜单里五个角色与 `memory` 都在；`/developer` 会话预载 ideo、scrum、memory 三份。临时副本没有第三方 `node_modules`，启动时 `dshmarket` 跳过，与本核对无关。临时 profile 已删。 |

- **不要混淆两种旧基线**：Claude Code 有公开的 `v6.0.3` git tag 与市场发布版，而 DSH 的 `b2679aa` 只是本地仓库链接（不是旧公开 npm 或注册表包）。
- **核对实际加载来源与版本**：查看 Claude 生效的版本缓存目录或 DSH 链接的本地目录及原生会话事件，不要只看磁盘上的 `package.json`、`plugin.json`，也不要以模型自述为准。在 DSH 中重启后务必新开 **Standard** 会话，因为 Minimal 会话不挂载技能加载器，旧会话也可能残留旧上下文。
- **确认项目日志原样保留**：迁移前后核对 `scrum/ProductBacklog.md` 以及开着的 `scrum/sprint-*/SprintBacklog.md`、`scrum/ideo-*/IdeoBacklog.md` 未发生改动。

## 候选如何核验

保持 `plugins/ideo-scrum/.claude-plugin/plugin.json` 与 [`package.json`](../package.json) 的候选版本号一致（`0.7.0`），中英 README 顶部版本号与 [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) 对齐，[`CHANGELOG.md`](../CHANGELOG.md) 中 `## [Unreleased]` 与已发布历史严格分开（不改已发布历史、不把改号当发布），内容改动与改号分开提交，并在打 tag、合并或推送前取得 PO 明确授权。

```sh
claude plugin validate --strict plugins/ideo-scrum
node --test scripts/check_dsh.mjs
npm pack --dry-run --json --ignore-scripts
python -X utf8 -I scripts/check_docs.py
python -X utf8 -I scripts/check_docs.py --selftest
python -X utf8 -I scripts/board_check/check.py selftest
```

- **静态与打包检查不代替实机测试**：`claude plugin validate --strict`、[`check_dsh.mjs`](../scripts/check_dsh.mjs)、`npm pack --dry-run`、`check_docs.py` 与 [`board_check/check.py`](../scripts/board_check/check.py) 只核验清单、适配器注册、打包白名单、双语结构对等与看板脚本，不能证明实机安装、降号迁移或宿主运行时行为。[`check_docs.py`](../scripts/check_docs.py) 也把本页及其中文对页纳入与 README、快速上手相同的标题、命令与链接检查。
- **实机隔离要求（[`headless-testing.md`](../scrum/documents/headless-testing.md)）**：测试放在上级目录无任何指令文件的中性目录（Claude Code 用 `/context all` 核实），使用互不复用的 `CLAUDE_CONFIG_DIR`、`DSH_HOME` 与 `DSH_AGENTS_HOME`（[`home-paths`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/util/home-paths/src/index.ts#L127-L152)），Claude Code 走经过版本缓存的 Git 市场夹具（迁移不用 `--plugin-dir` 或本地目录市场），DSH 走持久目录的 Web 安装加 Standard 会话（不用 `dsh --profile headless` 冒充 Web／Standard）；原始会话日志放仓库外，严禁泄露或提交凭据与提供方配置。
- **实机取证门槛**：记录宿主版本、实际加载的缓存或链接路径、角色调用、原生 hook／`skill-invocation`／`runtime-context`（`ideo-scrum:commitments`）事件、清晰的 `AGENTS.md` 标记加载证据以及未变动的项目日志；不把模型复述、文件在盘上或入口出现在列表里算作注入证明。
- **相关维护资料**：[`AGENTS.md`](../AGENTS.md)（仓库共用规则）、[Memory](../plugins/ideo-scrum/skills/memory/SKILL.md)（各角色共用的规矩；与官方指南的差异在它的 `details/departures.md`）、[`board-log.md`](../plugins/ideo-scrum/board/board-log.md)（看板约定）与 [`ATTRIBUTION.md`](../ATTRIBUTION.md)（第三方来源与许可条款）。
