# IDEO-Scrum for Codex

Design Thinking 与 Scrum Sprint 方法论插件。插件名：`ideo-scrum`，版本：`2.0.0`。

## 插件内容

| 内容 | 入口 |
|---|---|
| IDEO / d.school 五模式、设计方法库、设计冲刺五阶段 | [design-kernel](skills/design-kernel/SKILL.md) |
| Scrum Guide 2020、SGEP 扩展包、Artifact / Event / Roles 参考 | [scrum-kernel](skills/scrum-kernel/SKILL.md) |
| Scrum Master 角色模板 | [AGENTS.scrum-master.md](templates/AGENTS.scrum-master.md) |
| Designer 角色模板 | [AGENTS.designer.md](templates/AGENTS.designer.md) |
| Developer 角色模板 | [AGENTS.developer.md](templates/AGENTS.developer.md) |

本插件携带完整的方法论资料与三份角色模板，不依赖 Claude 插件目录。使用插件无需 Python、MCP 服务或额外脚本。

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

确认 Codex 能找到对应 skill 并按需读取参考资料。安装不会自动选用角色模板；两个方法论 skill 可以独立使用。

## 选择角色

角色由使用者项目根目录的 `AGENTS.md` 决定。入门可先选 Scrum Master：

| 模板 | 使用场景 |
|---|---|
| [Scrum Master](templates/AGENTS.scrum-master.md) | 组织 Sprint 事件、检视流程、移除障碍、协助 Product Owner |
| [Designer](templates/AGENTS.designer.md) | 用户研究、问题定义、方案探索与原型验证 |
| [Developer](templates/AGENTS.developer.md) | 制定 Sprint Backlog、实现 Increment、检查 DoD、Review 与 Retro |

1. 打开所选模板。可从本地仓库的 `codex/plugins/ideo-scrum/templates/` 获取；通过 Git 安装时，也可以在源仓库的 `codex` 分支中打开同名文件复制正文。
2. 项目没有 `AGENTS.md` 时，将模板复制到该项目根目录并命名为 **`AGENTS.md`**。
3. 项目已有 `AGENTS.md` 时，手动合并模板中的角色内容，保留项目原有的开发、测试和协作指令。
4. 切换角色时，替换原来的 IDEO-Scrum 角色部分，保留项目其他指令；同一时间只采用一份角色模板。
5. 在该项目重新启动 Codex CLI，或开启新的 app 会话，让项目指令重新加载。

模板使用的 `AGENTS.scrum-master.md` 等文件名仅用于区分角色；原样留在 `templates/` 中不会成为项目常驻指令。项目如果已有 `AGENTS.override.md`，它优先于同目录的 `AGENTS.md`，需要一并检查是否覆盖了所选角色。

选用后可在新会话中询问：

```text
请根据当前项目的 AGENTS.md，说明你的角色、我的角色，以及你负责哪些工作。
```

预期使用 Scrum Master 模板时，Codex 以 Scrum Master 协作，用户是 Product Owner；换用 Designer 或 Developer 模板后，应体现各自职责。

## 目录与维护

- `.codex-plugin/plugin.json`：Codex 插件清单。
- `skills/`：两个方法论 skill 及各自完整参考资料。
- `templates/`：三份可手动选用的角色模板。
- `LICENSE`、`ATTRIBUTION.md`：原创内容许可与第三方来源说明。

Codex 版本在 `codex` 分支持续维护，安装入口固定为该分支；Claude 版本继续使用 `main` 分支。Codex 分支保留 Claude 目录作为迁移来源，首版两个 skill 的内容相同。修改共享方法论时，需要同步检查两份内容和相对引用。分发本插件时应保留整个插件目录；仓库安装还需要根目录的 Codex marketplace 清单。

## 来源与授权

原创部分适用 [LICENSE](LICENSE)。方法论资料保留各自的许可条件，不统一适用 MIT；完整来源、修改说明与限制见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 官方参考

- [OpenAI：创建 Codex 插件](https://learn.chatgpt.com/codex/build-plugins)
- [OpenAI：项目 AGENTS.md 指令](https://developers.openai.com/codex/guides/agents-md/)
