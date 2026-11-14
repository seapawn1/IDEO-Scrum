# Sprint Backlog — Sprint 20 (presentable)

> Started: 2026-11-14 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `worktree-sprint-20-presentable`（原生 worktree `sprint-20-presentable`）| Product Owner: SeaPawn | Scrum Master: 会话 IDEO # [master]-[main]-[management sprint]（2026-11-14 关闭，此后 PO 全权交 Developer）| Developer: IDEO # [developer]-[sprint-20]-[do presentable]
> Now: 收官 · 2026-11-14，Sprint Goal 达成，发版 v6.0.3
> Waiting for PO: None
> 归档：2026-11-14 一天做完。日志已压缩成关键决定，逐条原文见 `git show 980407f:scrum/sprint-20-presentable/SprintBacklog.md`；体验测试的原始输出在仓库外 `S:\IDEO-Scrum-Archives\sprint-20-presentable\stranger-test\`；看板生成、配色截图在 `S:\IDEO-Scrum-Archives\sprint-20-presentable\board-gen\`、`board-theme\`。

**三条线**：设计线（另一个 worktree，`scrum/design-board/`）做看板原型，PO 全程参与；建造线做不依赖看板的块；设计 2026-11-14 结束，分支 `worktree-design-board` 合进本分支（`c268bd8`），此后由 Developer 照原型做模板。分工一度改为 Master 兼 Developer，PO 当天改回。

**CLAUDE.md 未改**（PO 2026-11-14：「最后不要更新到claude.md里面记得」）：本冲刺的现状记在产品日志与这份日志；教训按 PBI-69 一条一个记忆文件进 `S:\SeaPawn-Memory\memory\IDEO-Scrum\`。

**PO 的决定与授权**（原话见下方各条）：进 Sprint 20 的 PBI 与 Goal；PBI-70 破例在冲刺进行中改约定、登记和精化全权交 Developer；提前同意 63-b 过线就收官、推送、发 6.0.3、更新本机插件；Retro 要点提前交 Master（Master 关闭后由 Developer 自己挑）；Master 会话关闭后「全部权限授予你……拥有决策权」。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 拿得出手：看板改版，好看、好读；README、快速上手、词汇表讲清规矩，发布包装补齐；懂 Scrum 的人照着就能装上、走完第一个冲刺，不问作者。 |
| --- | --- |

### 1.2 Definition of Done

Outcome Done：懂 Scrum 的陌生人走完第一个冲刺，不问作者、没有卡死的点。Output Done：内容忠实（第三方摘录带 Source / License 两行，与 ATTRIBUTION.md 一致）、无死链、`claude plugin validate --strict` 通过、Codex 包同步且 `check_codex.py` 通过。

## 2. What

### 2.1 Product Backlog Items

PBI-68 看板改版、PBI-64 发布包装、PBI-62 教学（README、快速上手、词汇表）、PBI-63 体验测试（最后做）、PBI-70 约定小修（七处，PO 破例进本冲刺）。

### 2.2 Refinement

- **63-a 标准**：两个便宜模型会话（S 陌生人、P 带插件的 Claude Code），驱动脚本在中间传话；卡住四条、过线五条、五个产出；正式只跑一组 3 次、一个接一个，过线就停，最多修一轮。正式跑之前改了三处：陌生人的任务（不带引导地「说说项目现在走到哪」）、过线第 5 条（看板过 68-4 的检查、S 据看板可见文字说出的现状和日志一致）、砍轻（一组 3 次、最多修一轮）。
- **PBI-70 七处**：原型跟着结论走；过关卡前读承诺原文并写进日志那一行决定，不当面念；设计的共情、定义由 PO 和担任 Scrum Master 的会话定；地图画想达到的体验；测试只请相关的角色卡，东西只给 PO 用就 PO 本人测；闪电演示和子代理方案可选；Retro 的教训只写进项目的记忆，不写指令文件。英文为准，只改条里的话，不删条不改号。

## 3. How

18 个块（表见原文）：开场包、设计线、CHANGELOG 与图标、三份大纲、README、快速上手与词汇表、63-a 标准、63-a 脚本与冒烟、看板模板、看板约定与检查、便宜模型生成并核对、看板与 hook 的说明、正式跑、修与再跑、发版准备、PBI-70 三块。执行顺序 9 → 10 → 11 → 16 → 17 → 18 → 12 → 13 → 14 → 15。

**关键选择**：看板做成「固定页面 + 一块数据」——好看在固定的页面里，便宜的模型只填数据，核对变成「数据对日志」；文档先大纲后全文、三份大纲一次给 PO 看；图标三张候选给 PO 挑；63 的原始输出放仓库外，仓库里只留判定汇总；PBI-70 排在 12 之前（它改到 README 和快速上手的说法）、排在 13 之前（陌生人测的要是新约定）。

**风险**：便宜的模型能不能稳定填好数据（概括的部分脚本查不了）；设计线的节奏由 PO 定；看板配色要随系统（PO 2026-11-14 中途提出）。

## 4. Increment notes

- **看板**：`scrum-board-template.html`（原 `board-template.html`，PO 定改名）照设计线故事板第 3 版：总览流向图 + 三层卡片，三档屏，离线，跟着系统的深浅色。`board-log.md`（原 `board.md`）重写成 19 条。`scripts/board_check/check.py`：数据对日志逐项核、页面对模板逐字比、`--render` 用无头 Edge 核画出的条目。便宜的模型两次生成，第 2 次一条提醒也没有；PO 看过真实看板说「非常好」（68-6）。
- **配色随系统**（PO 2026-11-14 中途加）：「看板得颜色，就是随系统变换，不要默认深色」。用 `prefers-color-scheme`，没有偏好时亮色，系统深色时用原来那套深色（逐像素不变）；亮、暗两套截图给 PO 看，PO 说「不错，很好」。
- **PBI-70 七处**改到一致：design-log、sprint-log、overview、ideo-log、两份设计模板、design-kernel 的 SKILL.md、三个角色命令、词汇表、快速上手；三份 description 不动；条号不改。全新子代理审出八处，改三处、其余写明不动的理由。
- **发布包装**：`CHANGELOG.md` 的 6.0.3 一节；图标 `plugins/ideo-scrum/icon.png`（PO 从三张候选里挑的）；README 的升级、授权、反馈；Codex 包同步。
- **教学**：README（中英）、`docs/quick-start*.md`（一页 80 行）、`docs/glossary.md`、README 的「看板和 hook」一节。PO 通读过全文（62-1）。
- **体验测试（63）**：标准和脚本先写、单独提交。正式跑一组 3 次。第 1 次（旧）作废：测试台把作者的 `~/.claude/CLAUDE.md` 经上级目录读进了会话，P 去读了作者的记忆；另有两处判卷错（裸 `bash` 命中的是 WSL 启动器、检查脚本不认中文标题）。修完重跑：第 1 次没有文档的卡点、五个产出都在，但 P 受陌生人指示动了作者真实的家目录（已清理，守卫钩子此后拦下），记作测试台的事故、不算文档的卡点；第 2 次五个产出全 ✓（一处看板 IDEO 判错，改判为测试台的毛病，检查脚本修好）；第 3 次见 Test。测试台在过程中补了五样：运行放公共目录并开跑前用 `/context all` 核实没装进指令文件、判卷用 Git 的 bash 和一次性 HOME、检查脚本认中文标题、S 的通道加「只有一台电脑」、守卫钩子加临时目录清理和家目录快照。
- **授权的记录**：PO 提前同意收官（63-b 过线）；Retro 要点提前交 Master；Master 会话关闭后由 Developer 全权收口。「收官不改 CLAUDE.md，一个字都不动」，合 main 时以 main 的为准。

## 5. Test

- **68-6**：PO 看过便宜的模型照 `board-log.md` 写的真实看板，说「非常好」。
- **62-1**：PO 通读 README、快速上手、词汇表全文，没提意见。
- **插件校验**：`claude plugin validate --strict` 通过；全新子代理（Haiku）审过 PBI-70 的改动，plugin-validator 无必问项。
- **63 报告（结论先写）**：**过线**。一组 3 次里两次走完，没有文档的卡点，问作者 0 次，每次运行的隔离都核实过、碰作者的路径 0 次，走完的两次看板都过 68-4 的检查、陌生人据看板说出的现状和日志一致。
  - **文档的卡点**：无。
  - **模型的失误**：第 1 次把日志标题译成中文（无碍）；第 2 次在自己的家目录里装好工具，试探要装到作者家目录时被守卫拒绝、明确说不绕；都不算文档的。
  - **测试台的事故与修补**（记在这里，供以后的同类测试看）：① 旧的第 1 次作废——运行在系统临时目录下，Claude Code 把上级目录里的作者 `~/.claude/CLAUDE.md` 当项目指令读进了会话；改成运行放公共目录、开跑前用 `/context all` 核实。② 判卷的裸 `bash` 命中 System32 的 WSL 启动器；改用 Git 的、并给一次性 HOME。③ 检查脚本不认中文标题；改认「产品」「产品目标」「冲刺目标」「设计目标」。④ 陌生人被问「用哪个家目录」时替一台不存在的机器做主，会话于是在作者真实家目录里装了工具和 `.bashrc`（已清理）；S 的通道加「只有一台电脑」，P 的会话加守卫钩子（拒绝点名作者家目录、记忆目录、本仓库的调用），跑完清真实临时目录里的草稿。⑤ 检查脚本比约定严（要求画服务产品日志的、已收尾的 IDEO 日志）；改脚本，约定那一句登记 PBI-71。
  - **花费与时间**：四次运行合计约 $49.6；正式测试加修测试台约 2 小时 40 分。原始输出在 `S:\IDEO-Scrum-Archives\sprint-20-presentable\stranger-test\`。第 3 次被杀是系统因内存紧张停的后台任务，宿主规则不许自己重跑；按冻结的标准「一组 3 次里至少 2 次走完」不阻塞。
