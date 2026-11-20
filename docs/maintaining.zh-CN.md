# 维护 IDEO-Scrum

本页写给在 Claude Code 与 DeepSeek Harness（DSH）两个宿主之间维护本仓库的人。如果你是用插件做自己的项目冲刺或设计，请看[快速上手](quick-start.zh-CN.md)、[README](../README.zh-CN.md) 和[词汇表](glossary.md)。([English](maintaining.md))

> **送审草稿状态（Sprint 25，`0.6.3` 候选）。** 宿主内部机制的说明引自固定版本的官方源码（`dsh-v0.2.2-rc.5`）；历史记录（`v6.0.3` 与 `b2679aa`）只作旧基线。`0.6.3` 的实机新装、`6.0.3 → 0.6.3` 迁移及运行时规则／承诺读取仍待 Test 放行，暂不作为已确认的用户指引。

## 双宿主，正文只维护一份

`plugins/ideo-scrum/` 是两个宿主唯一的共用方法论正文来源。DSH 不另存生成包，也没有同步脚本。

| 部位 | Claude Code | DeepSeek Harness（DSH） |
| --- | --- | --- |
| 角色与内核（`plugins/ideo-scrum/commands/`、`plugins/ideo-scrum/skills/`） | 经 [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json)（`./plugins/ideo-scrum`）与 [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) 加载 | 由 [`dsh/index.js`](../dsh/index.js) 在运行时直接从 `plugins/ideo-scrum/` 注册 |
| 承诺上下文 | [`hooks.json`](../plugins/ideo-scrum/hooks/hooks.json) 在 `SessionStart` 与 `UserPromptSubmit` 用 POSIX `sh` 跑 [`commitments.sh`](../plugins/ideo-scrum/hooks/commitments.sh) | [`dsh/index.js`](../dsh/index.js) 通过 [`dsh/commitments.js`](../dsh/commitments.js) 注册 `systemPrompt.context`（`ideo-scrum:commitments`，`order: 130`，`interpolate: false`） |
| 打包与元数据 | [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) 与 [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) | [`package.json`](../package.json)（`@seapawn/ideo-scrum`）、[`cordis.patch.yml`](../cordis.patch.yml)、[`dsh/locale/en.json`](../dsh/locale/en.json)、[`dsh/locale/zh.json`](../dsh/locale/zh.json) 与 `plugins/ideo-scrum/icon.png` |

- **角色与内核注册（`dsh/index.js`）**：剥离 YAML frontmatter（要求单行双引号 JSON 兼容的 `description`，且 `SKILL.md` 的 `name` 与目录名一致），注册四个内核与四个用户可调用角色（`/scrum-master`、`/developer`、`/designer`、`/stakeholder`，去掉 `ideo-scrum:` 前缀），在每个角色正文前加上 DSH 工具映射与路由提示，并按序预载 `ideo-kernel` 和 `scrum-kernel` 原文，同时保持 `sprint-kernel` 与 `design-kernel` 按需加载。
- **打包白名单（`package.json`）**：`files` 只列 `cordis.patch.yml`、`dsh/`、`ATTRIBUTION.md`、`plugins/ideo-scrum/commands/`、`plugins/ideo-scrum/skills/` 与 `plugins/ideo-scrum/icon.png`（不包含 `hooks/` 和 `.claude-plugin/`），不带 `dependencies` 或 `scripts`，且 `engines.dsh` 写为 `>=0.2.2-rc.5 <0.3.0`。
- **承诺适配（`dsh/commitments.js`）**：在最近的 `.git` 边界内查找对应标题下的 `Commitment`（`承诺`）行（[`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md) 第 17 条），跳过软链接的 `scrum/` 目录，多冲刺或多设计并存时只报数量，并遵循 `IDEO_SCRUM_COMMITMENTS=off`；压缩后补入依赖 DSH 对命名 `runtime-context` 的处理，而 `0.6.3` 实机压缩后补入仍待 Test 验证。

## 仓库规则从哪里读

[`AGENTS.md`](../AGENTS.md) 是唯一的仓库共用规则正文。[`CLAUDE.md`](../CLAUDE.md) 只保留 `@AGENTS.md`——单向导入，且 `AGENTS.md` 中没有循环回引 `@CLAUDE.md`。维护者只更新 `AGENTS.md`；`CLAUDE.md` 仍只由 PO 直接授权的实际执行会话修改。

- **Claude Code**：读取 `CLAUDE.md` 并单向导入 `@AGENTS.md`（`0.6.3` 测试会话的 `/context all` 隔离核验列入 Test 清单）。
- **DSH `0.2.2-rc.5`（已查官方源码与待实机验证区分）**：固定提交 `9c2670d3bce5275e0d1610272958121af87787bb` 显示 `dsh-base` 默认启用指令加载器，从 `.git` 根到工作目录读取 `AGENTS.md` 与 `CLAUDE.md` 并在同目录相同正文时去重（[`agent-instructions/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L30-L42)、[`config.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/src/config.ts#L11-L46)），且**不解析 `@path` 导入**（[`README.md#L223-L224`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L223-L224)）——因此 DSH 直接依赖 `AGENTS.md`，不经 `CLAUDE.md` 导入。隔离 Web 与 Standard 会话首轮确实加载 `AGENTS.md`、不重复且不串入上级目录的实机证据，仍待 Sprint 25 Test。
- **项目级 Agent 与命名 preset（未证实）**：上游 `dsh-v0.2.2-rc.5` 支持 Cordis 命名 preset 注册（[`agent-preset/src/index.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/preset/agent-preset/src/index.ts#L11-L29)）和受约束的进程内子代理 preset 选择（[`tool-subagent/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/subagent/tool-subagent/README.md#L50-L71)），这**不能**证明按项目自动发现 Agent 文件，也不同于 `.agents/skills` 或本包的 `/stakeholder`。DSH 项目级 Agent 支持目前未证实，也不属于本分发包范围。

## 已装用户怎样迁移

从 `6.0.3` 到 `0.6.3` 属于 SemVer 版本号下调（`6.0.3` > `0.6.3`），而**两个宿主的降号迁移路径目前尚未经过 Sprint 25 实机 Test**。面向用户的迁移指引只有在隔离实机 Test 通过后才会落入 [README](../README.zh-CN.md#升级) 和[快速上手](quick-start.zh-CN.md)；公开文档中须继续标明[安装说明](../README.zh-CN.md#安装)里的 DSH 宿主版本（`0.2.2-rc.5`）不是插件版本（`0.6.3`）。

| 宿主 | 旧版基线 | 升级差异与实机 Test 必核项 |
| --- | --- | --- |
| Claude Code | `v6.0.3`（`d681c69`），通过[版本缓存](https://code.claude.com/docs/en/plugins/loading#versions-and-updates)从 `./plugins/ideo-scrum` 市场安装 | 实测 `claude plugin update ideo-scrum@ideo-scrum` 是否接受降号，或是否需要干净替代路径（如卸载后重装）；核对实际命中的版本缓存路径、`claude plugin list`、角色入口、承诺 hook 与未改动的 `scrum/` 日志。 |
| DSH（`0.2.2-rc.5`） | 本地目录链接至提交 `b2679aa`（`@seapawn/ideo-scrum`，`private: true`，非公开注册表发布版） | 上游 [`versions.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/boot/plugin-manager/src/versions.ts#L32-L48) 只列出注册表中更高的 SemVer 候选，无法推断本地目录链接重启后加载哪一版；对比原地更新加重启与**卸载**后重新**添加插件**，再在**新的 Standard 会话**里核对 `0.6.3` 原生事件与未改动的 `scrum/` 日志。 |

- **不要混淆两种旧基线**：Claude Code 有公开的 `v6.0.3` git tag 与市场发布版，而 DSH 的 `b2679aa` 只是本地仓库链接（不是旧公开 npm 或注册表包）。
- **核对实际加载来源与版本**：查看 Claude 生效的版本缓存目录或 DSH 链接的本地目录及原生会话事件，不要只看磁盘上的 `package.json`、`plugin.json`，也不要以模型自述为准。在 DSH 中重启后务必新开 **Standard** 会话，因为 Minimal 会话不挂载技能加载器，旧会话也可能残留旧上下文。
- **确认项目日志原样保留**：迁移前后核对 `scrum/ProductBacklog.md` 以及开着的 `scrum/sprint-*/SprintBacklog.md`、`scrum/design-*/DesignBacklog.md` 未发生改动。

## 候选如何核验

保持 `plugins/ideo-scrum/.claude-plugin/plugin.json` 与 [`package.json`](../package.json) 的候选版本号一致（`0.6.3`），中英 README 顶部版本号与 [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) 对齐，[`CHANGELOG.md`](../CHANGELOG.md) 中 `## [Unreleased]` 与已发布历史严格分开（不改已发布历史、不把改号当发布），内容改动与改号分开提交，并在打 tag、合并或推送前取得 PO 明确授权。

```sh
claude plugin validate --strict plugins/ideo-scrum
node --test scripts/check_dsh.mjs
npm pack --dry-run --json --ignore-scripts
python -X utf8 -I scripts/check_docs.py
python -X utf8 -I scripts/check_docs.py --selftest
python -X utf8 -I scripts/board_check/check.py selftest
```

- **静态与打包检查不代替实机测试**：`claude plugin validate --strict`、[`check_dsh.mjs`](../scripts/check_dsh.mjs)、`npm pack --dry-run`、[`check_docs.py`](../scripts/check_docs.py) 与 [`board_check/check.py`](../scripts/board_check/check.py) 只核验清单、适配器注册、打包白名单、双语结构对等与看板脚本，不能证明实机安装、降号迁移或宿主运行时行为。注：用户文档最终整合时需把 `docs/maintaining.md` 与 `docs/maintaining.zh-CN.md` 加入 [`check_docs.py`](../scripts/check_docs.py) 的 `PAIRS`。
- **实机隔离要求（[`headless-testing.md`](../scrum/documents/headless-testing.md)）**：测试放在上级目录无任何指令文件的中性目录（Claude Code 用 `/context all` 核实），使用互不复用的 `CLAUDE_CONFIG_DIR`、`DSH_HOME` 与 `DSH_AGENTS_HOME`（[`home-paths`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/util/home-paths/src/index.ts#L127-L152)），Claude Code 走经过版本缓存的 Git 市场夹具（迁移不用 `--plugin-dir` 或本地目录市场），DSH 走持久目录的 Web 安装加 Standard 会话（不用 `dsh --profile headless` 冒充 Web／Standard）；原始会话日志放仓库外，严禁泄露或提交凭据与提供方配置。
- **实机取证门槛**：记录宿主版本、实际加载的缓存或链接路径、角色调用、原生 hook／`skill-invocation`／`runtime-context`（`ideo-scrum:commitments`）事件、清晰的 `AGENTS.md` 标记加载证据以及未变动的项目日志；不把模型复述、文件在盘上或入口出现在列表里算作注入证明。
- **相关维护资料**：[`AGENTS.md`](../AGENTS.md)（仓库共用规则）、[`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md)（流程总览与官方指南差异）、[`board-log.md`](../plugins/ideo-scrum/skills/scrum-kernel/conventions/board-log.md)（看板约定）与 [`ATTRIBUTION.md`](../ATTRIBUTION.md)（第三方来源与许可条款）。
