# IDEO-Scrum for Codex

Design Thinking 与 Scrum Sprint 方法论插件。插件名：`ideo-scrum`，版本：`3.1.0`。

## 插件内容

| 内容 | 入口 |
|---|---|
| IDEO / d.school 五模式、设计方法库、设计冲刺五阶段 | [design-kernel](skills/design-kernel/SKILL.md) |
| Scrum Guide 2020、SGEP 扩展包、Artifact / Event / Roles 参考 | [scrum-kernel](skills/scrum-kernel/SKILL.md) |
| Scrum Master 角色 skill | [skills/scrum-master/SKILL.md](skills/scrum-master/SKILL.md)（`$scrum-master` 显式调用） |
| Designer 角色 skill | [skills/designer/SKILL.md](skills/designer/SKILL.md)（`$designer` 显式调用） |
| Developer 角色 skill | [skills/developer/SKILL.md](skills/developer/SKILL.md)（`$developer` 显式调用） |
| Stakeholder 角色 skill | [skills/stakeholder/SKILL.md](skills/stakeholder/SKILL.md)（`$stakeholder` 显式调用） |

本插件携带完整的方法论资料与四份角色 skill，不依赖 Claude 插件目录。使用插件无需 Python、MCP 服务或额外脚本。

## 安装

需要支持 `codex plugin` 命令的 Codex CLI。可先运行 `codex plugin --help` 检查。通常使用下面的 Git 安装；本地安装供插件开发时选用，两种来源选一种即可。

### 从任意目录安装

Codex 版本在仓库的 **`codex` 维护分支**发布。打开终端，在任意目录（包括你自己的项目目录）运行，无需先克隆 IDEO-Scrum：

```powershell
codex plugin marketplace add seapawn1/IDEO-Scrum --ref codex
codex plugin add ideo-scrum@ideo-scrum
```

第一条命令注册远端仓库 `codex` 分支上的 marketplace，第二条命令安装其中的 `ideo-scrum` 插件。`--ref codex` 必须保留，以便获取专门维护的 Codex 版本。

### 从本地仓库安装（插件开发时可选）

若要验证本地修改，在 **IDEO-Scrum 仓库根目录**运行，根目录包含 `.agents/plugins/marketplace.json`：

```powershell
codex plugin marketplace add .
codex plugin add ideo-scrum@ideo-scrum
```

不要在当前插件子目录执行 `marketplace add .`，marketplace 清单位于仓库根目录。本地未提交或未推送的修改不会出现在 Git 安装中。

### 检查安装

```powershell
codex plugin list --marketplace ideo-scrum --json
```

确认结果中包含已安装的 `ideo-scrum`。然后重新启动 Codex CLI，或在 Codex app 中开启新会话，尝试：

```text
请使用 ideo-scrum 插件的 scrum-kernel，帮我规划下个 Sprint，并明确 Sprint Goal。
```

```text
请使用 ideo-scrum 插件的 design-kernel，帮我设计一轮用户访谈，验证这个功能是否值得做。
```

确认 Codex 能找到对应 skill 并按需读取参考资料。两个方法论 skill 可以独立使用；角色 skill 不自动介入会话，需以 `$scrum-master` 等显式调用。

## 选择角色

四个角色由四份角色 skill 承载。角色 skill 声明了 `allow_implicit_invocation: false`——不自动介入会话，显式调用才注入：

| 角色 skill | 调用 | 使用场景 |
|---|---|---|
| [scrum-master](skills/scrum-master/SKILL.md) | `$scrum-master` | 组织 Sprint 事件、检视流程、移除障碍、协助 Product Owner |
| [designer](skills/designer/SKILL.md) | `$designer` | 用户研究、问题定义、方案探索与原型验证 |
| [developer](skills/developer/SKILL.md) | `$developer` | 制定 Sprint Backlog、实现 Increment、检查 DoD、Review 与 Retro |
| [stakeholder](skills/stakeholder/SKILL.md) | `$stakeholder` | 独立核验 Increment：干净上下文＋证据包，出 verified / in doubt |

在会话中输入调用（可附带请求）：

```text
$scrum-master 帮我主持这次 Sprint Planning
```

角色 skill 与项目 `AGENTS.md` 互不冲突：`AGENTS.md` 继续承载项目自身的开发、测试和协作指令，角色契约只在调用时进入当前会话；同一时间采用一个角色，切换时改调用名即可。

调用后可在会话中询问：

```text
请说明你的角色、我的角色，以及你负责哪些工作。
```

预期使用 `$scrum-master` 时，Codex 以 Scrum Master 协作，用户是 Product Owner；调用 `$designer` 或 `$developer` 后，应体现各自职责。

## 目录与维护

- `.codex-plugin/plugin.json`：Codex 插件清单。
- `skills/`：两个方法论 skill、四份角色 skill 及各自完整参考资料。
- `LICENSE`、`ATTRIBUTION.md`：原创内容许可与第三方来源说明。

Codex 版本在 `codex` 分支持续维护，安装入口固定为该分支；Claude 版本继续使用 `main` 分支。Codex 分支保留 Claude 目录作为迁移来源，首版两个 skill 的内容相同。修改共享方法论时，需要同步检查两份内容和相对引用。分发本插件时应保留整个插件目录；仓库安装还需要根目录的 Codex marketplace 清单。

## 来源与授权

原创部分适用 [LICENSE](LICENSE)。方法论资料保留各自的许可条件，不统一适用 MIT；完整来源、修改说明与限制见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 官方参考

- [OpenAI：创建 Codex 插件](https://learn.chatgpt.com/codex/build-plugins)
- [OpenAI：项目 AGENTS.md 指令](https://developers.openai.com/codex/guides/agents-md/)
