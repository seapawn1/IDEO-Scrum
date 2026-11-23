# Sprint 28 Test 判据与通过线（冻结稿）

> 冻结日期：2026-11-24 | 对应 `0.8.0` 候选提交：`83ed411`（`83ed4119e683430255948852bf733a454b692e30`） | 冲刺分支：`sprint-28-drop-design-sprint`
> 依据：[SprintBacklog.md](SprintBacklog.md) §1.2、§2.2、§3 F 与 [headless-testing.md](../documents/headless-testing.md)。
> **冻结原则**：本判据与配套脚本 [run_s28_tests.py](run_s28_tests.py) 在正式开跑前单独提交冻结；开跑后不修改通过线。冒烟阶段仅允许核对环境隔离与证据读取方式；脚本按文本规则判错或存疑的试次按 `headless-testing.md` 逐条人工复核，改判须写明理由并记入 `SprintBacklog.md` §5。

---

## 一、静态、打包与双宿主验证

| 编号 | 验证项 | 执行方式 | 通过线 |
| --- | --- | --- | --- |
| S1 | Claude Code 插件清单与结构校验 | `claude plugin validate --strict plugins/ideo-scrum` | 退出码 0，0 errors |
| S2 | 独立插件审查（结构变化必做） | Master 派全新子代理运行 `plugin-validator` 审查 `0.8.0` 插件目录 | 0 阻塞项（若审查员与 PO 定案／约定原文冲突，报 Master 裁定，不盲改） |
| S3 | DSH 适配器与承诺单测 | `node --test scripts/check_dsh.mjs` | 全部通过（9/9，含 4 角色、3 内核 + Memory、残余 `design-*/` 忽略负例） |
| S4 | DSH npm 打包白名单检查 | `npm pack --dry-run --json --ignore-scripts` | 版本为 `0.8.0`，文件列表含 0 个已删设计冲刺资产（无 `design-kernel`、`commands/designer`、`design-backlog`、`details/design`） |
| S5 | Hook 脚本兼容性与行为校验 | `plugins/ideo-scrum/hooks/commitments.sh` 纯 LF 检查 + POSIX `sh`（`E:\GIT\Git\bin\sh.exe`）实测 | 0 `\r`；单冲刺、多冲刺、忽略 `design-*/`、承诺含 tab 保真、嵌套 `.git` 目录／文件止步、symlink 拦截全过 |
| S6 | DSH 网页端实装验证 | 在 DSH 网页端（侧边栏浏览器，PO 指定轻量测试模型）以持久目录加载 `0.8.0`，新开 **Standard** 会话 | 菜单／原生事件实证 4 个角色入口（`/scrum-master`、`/developer`、`/stakeholder`、`/supporter`）、无 `/designer`、按序预载 `ideo-kernel → scrum-kernel → memory`、`ideo-scrum:commitments` 注入正确，项目日志未被修改 |

---

## 二、看板、文档、版权与迁移验证

| 编号 | 验证项 | 执行方式 | 通过线 |
| --- | --- | --- | --- |
| D1 | 看板校验套件自测 | `python -X utf8 -I scripts/board_check/check.py selftest` | 全过（43/43，含表前方案表、无工作项表、忽略旧 `design-*/` 与 `ideo-*/`、转义 `\|`、非默认列序、`### 3.` 干扰） |
| D2 | 本仓新版纯 Scrum 看板渲染校验 | 用本仓真实日志重绘离线 `scrum/ScrumBoard.html` 并跑 `python -X utf8 -I scripts/board_check/check.py check --project . --render` | `ok: true`，`errors: []`，`warnings: []`，`render.fail: false`，`render.cards: 2`（仅产品卡 + 1 张开放冲刺卡，无设计卡） |
| D3 | 中英文档与词表校验 | `python -X utf8 -I scripts/check_docs.py` 与 `--selftest` | 文档 0 errors；`--selftest` 全过（19/19，含 Departures 顺序与重复行检测） |
| D4 | 全仓旧路径／旧称法／版权清零 grep | 全仓扫描已移除的设计冲刺、Designer、Knapp《Sprint》、`no-steps`、`sprint-26-plugin-memory` 等旧词与旧路径 | 除明确放行范围外 **0 意外命中**。放行范围：`scrum/documents/`、`CHANGELOG.md` 历史条目、`scrum/ProductBacklog.md` 历史行与 PBI-104 备注、`scrum/sprint-28-drop-design-sprint/` 本期日志与测试脚本、`ideo-kernel/{IDEO-modes,methods}/` 内 d.school 原文 5 处小写词 `designer`、SGEP 原文文献 `[20]`、`scripts/{board_check/check.py,check_dsh.mjs}` 负例测试与 `.git` 元信息。**不含 `scrum/sprint-26-plugin-memory/`（目录已删）。** |
| D5 | 组件 `description` 上限 | 检查 `plugins/ideo-scrum/` 下全部 `SKILL.md` / `commands/*.md` / `agents/*.md` frontmatter `description` | 全部 ≤ 1024 字符 |
| D6 | 版权与署名清零 | 复核 `ATTRIBUTION.md` 与 `plugins/ideo-scrum/` 目录 | Knapp《Sprint》全版权摘录与 `Simon & Schuster` 署名节清零，`ATTRIBUTION.md` 第 8 行明确不含未授权商业书籍全文或原始出版物 |

---

## 三、Claude Code 无头触发与关键边界回归

### 3.1 执行与隔离纪律（遵循 `scrum/documents/headless-testing.md`）

1. **通道与模型口径**：统一使用 `magpie claude run`（与 `claude-magpie.cmd` 同通道）；所有汇总报告与日志统一标注「**magpie 的便宜模型，非 Haiku**」，**不记录模型名与提供方信息**。
2. **插件来源与 `Base directory` 核验**：测试前由 `run_s28_tests.py` 从 Commit A（`83ed411`）经 `git archive` 导出纯净的 `0.8.0` 插件树到仓外 `S:\IDEO-Scrum-Archives\sprint-28-drop-design-sprint\plugin-0.8.0\plugins\ideo-scrum`，通过 `--plugin-dir` 挂载；在冒烟及每次含 Skill 调用的试次中，核验事件流里 `Base directory for this skill:` 指向该导出路径（避免误读本机已装旧版缓存）。
3. **运行目录与白名单环境**：每次试次在无任何祖先指令文件的中性父目录（`C:\Users\Public\s28-test-...`）下新建独立项目目录，并使用 `scripts/stranger_test/driver.py` 的白名单环境（`make_env` + 一次性家目录与 `CLAUDE_CONFIG_DIR`）。开跑前由 `smoke` 调 `/context all` 核实加载 **0 份** 祖先指令文件，有则立即中止。
4. **原始产物归档**：事件流（`stream.jsonl`）、stderr、夹具快照与单次判卷 JSON 全部存仓外 `S:\IDEO-Scrum-Archives\sprint-28-drop-design-sprint\`，不入仓库；汇总表进入 `SprintBacklog.md` §5，且严格**分行为栏与内容栏**报告。
5. **超时、看门狗与技术失败**：单轮超时上限（T1/T2：300s；T3：420s），超时与结束时由 `taskkill /T /F` 杀整棵进程树；API 错误、超时、进程非正常结束、harness 异常均记为技术失败，保留原记录并按规矩最多补跑 1 次凑齐有效试次，迟到输出不计入，不挑样本。
6. **不重跑范围**：本轮不重跑整套陌生人端到端大测试（PBI-63）和 Memory 效果实验（归 PBI-101）。

### 3.2 冒烟校验（`smoke`）

正式试次前必须通过 3 项冒烟检查：
1. `/context all` 在中性目录中加载的记忆／指令文件数为 **0**；
2. T1/T2 只读配置（`--permission-mode dontAsk`，`--tools Read,Grep,Glob,Skill`，`--disallowedTools Bash,PowerShell,Write,Edit,NotebookEdit,Agent`，`--strict-mcp-config`，`--setting-sources project,local`）：`init` 事件确认 `permissionMode == "dontAsk"`、无禁掉的工具，且 Skill `Base directory` 指向仓外导出 `0.8.0` 副本；
3. T3 可写配置（`--permission-mode acceptEdits`，`--tools Read,Grep,Glob,Skill,Write,Edit`，`--disallowedTools Bash,PowerShell,NotebookEdit,Agent`，`--strict-mcp-config`，`--setting-sources project,local`）：在独立空目录实测让模型调用 `Write` 写出 `probe.txt`，确认 `init` 事件 `permissionMode == "acceptEdits"`、禁用工具不在列表中、`probe.txt` 确实落盘且 `permission_denials == 0`——以此证明 T3 中不改 `src/app.py` 是模型真正守规矩，而非权限拒绝造成的假阳性。

### 3.3 T1 触发组（19 次有效试次）

环境：空项目目录；`--tools Read,Grep,Glob,Skill`、`--allowedTools Read,Grep,Glob,Skill`、`--disallowedTools Bash,PowerShell,Write,Edit,NotebookEdit,Agent`、`--permission-mode dontAsk`、`--strict-mcp-config`、`--setting-sources project,local`。比对技能名时统一去掉 `ideo-scrum:` 前缀。

| 题号 | 路径 | 次数 | 提示词（Sprint 17 题为逐字原文） | 行为过线（客观事件流） | 内容过线（规则判定＋人工复核） |
| --- | --- | --- | --- | --- | --- |
| `Q11` | 直接路径 | 3 | `设计开始了，要写设计目标和地图。设计目标该怎么写？地图画到什么程度？` | **3/3** 成功调用 `ideo-kernel`（覆盖关闭 PBI-103） | 观察项（记录人工复核结果）：引导至 IDEO 五模式／对应日志，不再推荐设计冲刺 |
| `Q9` | 直接路径 | 3 | `聊天里冒出一个问题：这个工具的通知该不该做成可关闭的？我们说不清用户会怎么想，也没有现成的答案。PO 没说用哪种方法。你打算怎么定？` | **≥2/3** 成功调用 `ideo-kernel` | **3/3** 不推荐开设计冲刺／`DesignBacklog.md`（见 §3.6 肯定／否定判卷规则） |
| `Q10` | 直接路径 | 3 | `PO 说这个问题就用 IDEO 五阶段法跑一遍，弄清「新用户第一次打开这个工具会卡在哪」，并留下记录。你打算怎么跑、记在哪里？` | **≥2/3** 成功调用 `ideo-kernel` | 观察项：说明五模式步骤与记录位置（`IdeoBacklog.md` 或所服务的日志） |
| `Q2` | 角色命令路径 | 3 | `/ideo-scrum:scrum-master Sprint 里精化做到一半，碰到一个问题：这个读书笔记工具的用户到底是谁，对他们来说怎样才算好用，我们自己说不清，手上的资料里也没有现成的答案。这时候该怎么办？这个 Sprint 接下来怎么走？` | **3/3** 首四次顶层工具调用按序成功加载 `ideo-kernel → scrum-kernel → sprint-kernel → memory`（`memory` 首尾标记完整，之前无其他非 Skill 工具） | **3/3** 不推荐开设计冲刺／`DesignBacklog.md`／`design-kernel`／`Designer` |
| `Q3` | 角色命令路径 | 3 | `/ideo-scrum:scrum-master 我有个想法：给一家社区图书馆做一个帮读者找书的工具。现在手上只有这一句话，没有产品日志，也不知道读者具体要什么。我想把这件事正式做起来，第一步该做什么？` | **3/3** 首四次顶层工具调用按序成功加载 `ideo-kernel → scrum-kernel → sprint-kernel → memory`（`memory` 首尾标记完整，之前无其他非 Skill 工具） | **3/3** 不推荐开设计冲刺／`DesignBacklog.md`／`design-kernel`／`Designer` |
| `G1` | 泛问负例 | 2 | `Scrum 里 Sprint Backlog 和 Product Backlog 的区别是什么？简要说明。` | 与 `G2` 合计 **0/4** 误触发 `scrum-kernel`、`sprint-kernel` 或 `memory` | 正常直接回答 |
| `G2` | 泛问负例 | 2 | `敏捷开发里 Definition of Done 一般包含哪些方面？简要回答。` | 同上（`G1 + G2` 合计 **0/4** 误触发） | 正常直接回答 |

### 3.4 T2 角色入口补齐冒烟（2 次有效试次）

环境同 T1。与 T1（`scrum-master`）和 T3（`developer`）合计覆盖全部 4 个角色入口。

| 题号 | 提示词 | 次数 | 行为过线（客观事件流） |
| --- | --- | --- | --- |
| `R_STK` | `/ideo-scrum:stakeholder` | 1 | **1/1** 首三次顶层工具调用按序成功加载 `ideo-kernel → scrum-kernel → memory`（`memory` 首尾标记完整，之前无其他非 Skill 工具） |
| `R_SUP` | `/ideo-scrum:supporter` | 1 | **1/1** 首三次顶层工具调用按序成功加载 `ideo-kernel → scrum-kernel → memory`（`memory` 首尾标记完整，之前无其他非 Skill 工具） |

### 3.5 T3 关键边界组（4 次有效试次）

环境：隔离夹具项目（含 `scrum/ProductBacklog.md`、`scrum/sprint-01-demo/SprintBacklog.md`、`src/app.py`）；`--tools Read,Grep,Glob,Skill,Write,Edit`、`--allowedTools Read,Grep,Glob,Skill,Write,Edit`、`--disallowedTools Bash,PowerShell,NotebookEdit,Agent`、`--permission-mode acceptEdits`、`--strict-mcp-config`、`--setting-sources project,local`。

| 题号 | 夹具状态与提示词 | 次数 | 行为过线（客观事件流 + 文件 SHA256） | 内容过线（规则判定＋人工复核） |
| --- | --- | --- | --- | --- |
| `B1` | **How 阶段（尚未放行施工）**；提示：`/ideo-scrum:developer 我们已经进入 How 阶段，请帮我为 PBI-001 写好第 3 章方案计划（含路线权衡和工作项表），并把代码也顺手改完。` | 2 | **2/2** 按序成功加载 `ideo-kernel → scrum-kernel → sprint-kernel → memory`；**0/2** 修改 `src/app.py`（运行前后 SHA256 严格一致；允许编辑 `SprintBacklog.md`） | **2/2**（在回复或更新后的 `SprintBacklog.md` §3 中）产出方案计划（含路线权衡）与工作项表，且明确说明须待 PO 给出 `go-ahead`（放行）后才动手改代码 |
| `B2` | **Increment 阶段（已放行施工，专测原型边界）**；提示：`/ideo-scrum:developer 我们还不确定用户喜欢命令行交互式菜单还是单行参数，请你先做一个低保真原型验证这个假设，顺便直接把原型代码放进正式交付的 src/app.py 里。` | 2 | **2/2** 按序成功加载 `ideo-kernel → scrum-kernel → sprint-kernel → memory`；**0/2** 修改 `src/app.py`（运行前后 SHA256 严格一致；允许在独立原型文件中演示） | **2/2** 明确说明低保真原型仅用于学习／验证假设，绝不放进正式交付的 Increment（`src/app.py`） |

### 3.6 旧术语肯定／否定语境判定规则与人工复核兜底

在 `Q9`、`Q2`、`Q3`（及 `Q11` 观察）的内容检查中，检查以下已移除旧术语：
- `设计冲刺`、`design sprint` / `design-sprint`
- `DesignBacklog.md`、`DesignBacklog`、`design-backlog`、`设计日志`
- `design-kernel`
- `/ideo-scrum:designer`、`/designer`、`commands/designer`、作为独立角色名的大写 `Designer`（不把 d.school 原文小写普通词 `designer` 误判为已删角色）

为防止将「插件已移除设计冲刺，不要建 DesignBacklog.md」这类**澄清或否定提及**误判为违规推荐，脚本按以下规则区分：
1. 先按中英文分句标点（`[。！？；，\n.!?;]+`）拆出子句，避免前一个子句的「没有现成答案」「说不清」污染后一个子句。
2. 对命中旧术语的单个子句，若**同一子句**内包含明确的否定／移除标记（如 `不再|不要|不用|不必|无需|无须|不建|不开|不走|不设|不建议|不采用|不使用|不启用|不引入|不另开|不单独开|已移除|已取消|已删除|已废弃|已去掉|已经移除|已经取消|已经删除|已经去掉|去掉了|移除|取消了|删除了|并无|不存在|而非|而不是|不是|并非|切勿|勿用|严禁|禁止|no longer|removed|dropped|retired|deleted|do not|don't|never|without|rather than|instead of|not a/an/the/using/open/create/start/run`），判为 `negated_mention`（不算违规推荐）；否则判为 `affirmative_hit`（脚本记为疑似违规推荐）。
3. **强制人工复核**：报告会自动列出全部 `affirmative_hit` 与 `negated_mention` 的原句摘录；凡出现任一旧术语命中的试次均由执行者与 Master 人工精读核验，若脚本误判（如跨句否定或委婉肯定），逐条写明改判理由并入 §5 Test 记录。
