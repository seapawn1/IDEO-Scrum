# PBI-72 · 宿主证据与验收样例

这是 Sprint 25 的工作材料，不是 `0.6.3` 的测试报告。以下记录已查实的源码、旧端和供 Test 使用的样例；`H4`（Claude Code）与 `H5`（DSH）均已跑完，结果见 [SprintBacklog §5](SprintBacklog.md#5-test)；H5 在 PO 提供的隔离实例上由 Stakeholder 代操，未触碰 PO 日常实例。

| 要核的事 | 已有证据 | 仍待实机验证 |
| --- | --- | --- |
| DSH 读取共用规则 | [DSH `dsh-v0.2.2-rc.5`](https://github.com/deepseek-ai/deepseek-harness/tree/9c2670d3bce5275e0d1610272958121af87787bb) 的[指令加载器说明](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L30-L42)及[候选配置](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/src/config.ts#L11-L46)：`dsh-base` 默认启用；以 `.git` 为根，从根到工作目录读取 `AGENTS.md`、`CLAUDE.md`，同目录相同正文去重，`.local.md` 是叠加项。[不解析 `@path` 导入](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L223-L224)。因此 DSH 的共用正文来自 `AGENTS.md` 本身，不靠 `CLAUDE.md` 导入；Claude 仍用单向导入。 | 隔离的 Web／Standard 会话在首次请求中显示 `AGENTS.md` 的实际来源与正文；两个宿主都读同一规则正文，不从用户目录或父目录误取，也不重复加载。 |
| DSH 项目级 Agent | [Cordis 预设注册](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/preset/agent-preset/src/index.ts#L11-L29)与[子代理预设选择](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/subagent/tool-subagent/README.md#L50-L71)分别证明宿主能声明命名 preset、受配置约束让进程内 spawn 选 preset。它们不证明按项目自动发现 Agent 文件，也不等于 `.agents/skills` 或本 bundle 的 `/stakeholder`。 | 项目级自动发现或注册目前未证实；将有版本的结论交 Sprint 22 参考，不替该期实现。 |
| `6.0.3 → 0.6.3` | Claude 旧端为 `v6.0.3`（`d681c69`），Git 市场相对源 `./plugins/ideo-scrum`；DSH 旧端为 `b2679aa`，根包 `@seapawn/ideo-scrum` 为 private 的本地 bundle。DSH 的[注册表更新候选](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/boot/plugin-manager/src/versions.ts#L32-L48)只列 SemVer 更高项，不能用它推断本地目录链接重启后加载哪一版。 | Claude 查市场缓存中新旧实际路径；DSH 查 Web 安装后链接／加载来源和新 Standard 会话。常规路径失败才单独查替代路径；两端都要保全项目日志。 |

**隔离条件与环境白名单。** 当前 Windows 有 Claude CLI、Git、Node `v26.13.0`、npm；`PATH` 未找到 `dsh`，未检查用户配置。固定的 [`@deepseek-ai/dsh@0.2.2-rc.5` 元数据](https://registry.npmjs.org/@deepseek-ai%2Fdsh/0.2.2-rc.5)要求 Node `>=24.9.0`。进入 H4–H5 前必须满足以下隔离硬条件（参考[无头回归测试手册](../documents/headless-testing.md)）：

- **中性父目录**：所有测试仓库与隔离配置均放在上级目录不含任何 `CLAUDE.md`／`AGENTS.md` 的中性路径（如 `C:\Users\Public\s25-test\`），严禁放在 `%TEMP%` 或作者家目录下，也不得指向本工作树或主仓库。
- **Claude 隔离**：按运行分别准备互不复用的 `CLAUDE_CONFIG_DIR`（零写入 `~/.claude`）；子进程环境变量采用白名单（`SystemRoot`、去除了作者家目录仅保留工具目录的 `PATH`、独立 `HOME`/`USERPROFILE`/`APPDATA`/`LOCALAPPDATA`、全新空 `TEMP`/`TMP`、`CLAUDE_CODE_GIT_BASH_PATH`、`MSYS_NO_PATHCONV`、`GIT_CONFIG_GLOBAL` 空文件、`GIT_CONFIG_NOSYSTEM=1`）；禁用 shell 时同时禁用 `Bash` 与 `PowerShell`；带 `--strict-mcp-config`、`--permission-mode dontAsk`、`--setting-sources user,project,local`（`claude plugin install` 把 `enabledPlugins` 写进用户级设置，缺 `user` 则不挂载插件；冒烟见 SprintBacklog §5）；若用 `scripts/stranger_test/guard.py`，不得再传入与 `claude-magpie` 冲突的额外 `--settings`。每次模型调用前先运行 `/context all`，一旦加载任何上级或用户指令文件立即停机。
- **DSH 隔离**：按运行分别设置独立的 `DSH_HOME`、`DSH_AGENTS_HOME`（由[宿主路径实现](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/util/home-paths/src/index.ts#L127-L152)确认），绝不复用 PO 常用目录；Web/Standard 与 `headless` profile 严格分开；本地 bundle 从测试目录持久拷贝安装，不链接作者工作树。H5 已由 PO 提供的隔离实例执行（`npx --offline @deepseek-ai/dsh@next web`，独立 homes，未全局安装 `dsh`，未触碰 PO 日常实例）；H5-A 与 H5-B 各用一套互不复用的 homes 与独立样例项目。
- **脚本与凭据卫生**：脚本内统一写 Git for Windows 的绝对路径 `bash.exe`，超时使用 `taskkill /T /F` 杀整棵进程树；测试凭据／提供方配置仅以隔离环境注入，绝不打印环境变量值，也绝不将任何提供方地址、密钥或用户设置写入仓库。

**运行矩阵（`H4`、`H5` 均已跑完）。** 四组运行各用独立夹具仓库与配置快照，禁止跨新装／迁移复用状态；结果见 SprintBacklog §5：

| 编号 | 宿主与基线 | 安装／迁移路径 | 必核项 |
| --- | --- | --- | --- |
| `H4-A` | Claude Code 新装 `0.6.3` | 隔离 Git 市场夹具（经[版本缓存](https://code.claude.com/docs/en/plugins/loading#versions-and-updates)），不用 `--plugin-dir` | `/context all` 清白；4 角色可见；`/ideo-scrum:scrum-master` 入 Planning；原生 hook 与 `S25-SHARED-RULE` 首轮入上下文。 |
| `H4-B` | Claude Code 迁移 `v6.0.3`（`d681c69`）→ `0.6.3` | 隔离 Git 市场先装 `v6.0.3` 留证，再跑常规更新；若拒降号则验干净替代路径及影响 | 前后实际缓存路径与版本、`claude plugin list`、新会话角色与承诺原文、`scrum/` 日志逐字节未改。 |
| `H5-A` | DSH `0.2.2-rc.5` 新装 `0.6.3` | Web **Plugins → Add plugin** 装持久测试目录，开新 **Standard** 会话 | 4 角色可选；`/scrum-master` 原生 `skill-invocation`（`ideo-kernel` 先于 `scrum-kernel`）；`runtime-context`（`ideo-scrum:commitments`）；`AGENTS.md` 标记首轮入上下文且无重复／越界。 |
| `H5-B` | DSH `0.2.2-rc.5` 迁移 `b2679aa` → `0.6.3` | Web 先链接持久目录 `b2679aa` 留证，再试原地更新加重启；必要时验 **Uninstall** 后重加，开新 **Standard** 会话 | 前后链接目录与加载版本、新 Standard 会话原生事件、承诺与 `AGENTS.md` 标记、`scrum/` 日志逐字节未改。 |

**样例项目输入（各隔离仓库共用）。** 在隔离位置初始化 Git 仓库，项目根放 `AGENTS.md`、`CLAUDE.md` 和 `scrum/`。下列正文只在测试项目里使用，不作为当前仓库的指令：

| 文件 | 样例内容 |
| --- | --- |
| `AGENTS.md` | `S25-SHARED-RULE: Preserve the sample logs.` |
| `CLAUDE.md` | `@AGENTS.md` |
| `scrum/ProductBacklog.md` | `## 1.1 Product` 与 `## 1.2 Product Goal` 下各放一行承诺表，精确值分别为 `S25-FIXTURE-PRODUCT`、`S25-FIXTURE-PRODUCT-GOAL`；`## 1.3 Definition of Done` 放最小条目，`## 3.1 Product Backlog Items` 放 `PBI-001`（`waiting`）供 Planning 选用。 |
| `scrum/sprint-01-sample/SprintBacklog.md` | `## 1. Why` 中 `### 1.1 Sprint Goal` 下放一行承诺表，精确值为 `S25-FIXTURE-SPRINT-GOAL`。 |

**预算、原始留证与停点。**

- **预算上限**：使用便宜的测试模型（`headless-testing.md`）；按 SprintBacklog §3 的会话预算控制规模，单次运行最多 6 轮对话、CLI 单步超时 ≤ 120 秒。
- **原始输出存放**：原始会话流、hook JSON、DSH 事件日志与截图全部存于仓库外 `S:\IDEO-Scrum-Archives\sprint-25-dsh-docs\test-runs\`，入仓只保留脱敏后的判定汇总。
- **压缩后补入边界**：`H4-A`／`H4-B` 已各实跑一次手动 `/compact`，取得 `compact_boundary` 与 `SessionStart:compact` 复注承诺原文的证据；DSH `H5-A` 已实跑压缩，`agent-instructions` 与 `runtime-context`（`ideo-scrum:commitments`）在压缩后逐字复注；`H5-B` 环境未再单独测（SprintBacklog §5）。
- **硬通过线与上报停点**：每条证据记宿主版本、实际插件来源／缓存或链接路径、角色入口、原生事件（DSH：`skill-invocation` + `runtime-context` `ideo-scrum:commitments`；Claude：`--include-hook-events`／原生技能事件）、前后 `scrum/` diff 与 `S25-SHARED-RULE` 证据；拒绝以模型复述、文件在盘上或列表出现代替。若 `dsh` 无安全实机环境、`/context all` 串入父目录规则、任一宿主没有可复现的 `6.0.3 → 0.6.3` 降号路径、或 DSH `0.2.2-rc.5` 无法单源读取 `AGENTS.md`，立即停机并带证据回 PO，不降通过线、不擅自改宿主功能。H4／H5 已完结，待 Master 终审与 PO 正式 Review。
