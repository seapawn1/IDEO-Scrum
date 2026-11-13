# Sprint Backlog — Sprint 19 (board-hook)

> Started: 2026-11-13 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `worktree-golden-orbiting-bachman`（原生 worktree `golden-orbiting-bachman`）| Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[support sprint] | Developer: IDEO # [developer]-[sprint-19]-[do sprint 19]
> Now: 收官 · Master 2026-11-14 定收官（PO 授权）
> Waiting for PO: None
> 归档：2026-11-13 开工，2026-11-14 收官，发版 v6.0.2（Sprint 18、19 一起，PO 定）。日志已压缩成关键决定，逐条原文见 `git show 1bf5a94:scrum/sprint-19-board-hook/SprintBacklog.md`；原型、测试标准与脚本（`board_check.py`、`frequency_test.py`、`hook_cases.py`）见 `git show 1bf5a94:scrum/sprint-19-board-hook/`；原始输出在仓库外 `S:\IDEO-Scrum-Archives\sprint-19-board-hook\`。

**并行与分工**：主线。副线 Sprint 18 同日并行，先交日志头部接口（PBI-66），Master 审过当天转来；Sprint 18 收官后把 main 合进本分支（`853d406`），按合并后的原文复核。

**PO 授权**（2026-11-13，原话）：「其实精化我一般让你做的，你的上下文最多，其实你可以详细的告诉他们得，怎么写精化啥得对不对，我把整个权限全放开了，也就是告诉你，后面你的权限拉满，除非必要，我来做决定，否则你都可以直接决定」。看板的形式（35-2）留给 PO，PO 又交给 Master：「可以，这些你可以来决定」。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 看得见：看板把产品日志和开着的冲刺、设计浓缩成卡片，hook 把承诺放进上下文；PO 照着就能一眼看清进度，AI 照着就不忘目标。（PO 2026-11-13 定） |
| --- | --- |

### 1.2 Definition of Done

Outcome Done：用户不反复追问。Output Done：无死链、插件校验、Codex 包（hook 能同步就同步）。

## 2. What

### 2.1 Product Backlog Items

PBI-35 看板、PBI-61 目标常驻（hook）。

### 2.2 Refinement

精化由 Master 定案。

- **接口**：照抄 Sprint 18 的 66 读取规则；工作块完成读 Done when 格前的 ✓（Developer 问出来的缺口，Master 定归 66-8，主线不改约定）。
- **35 看板**：不另开设计，第一块工作就用真实数据做产品卡原型；形式做两版给 PO 挑——Master 定网页版（看板不提交，Markdown 能 diff 的长处用不上），块的顺序照 PO 的卡片设计（上承诺、中架构图、下条目，「等 PO 拍板」在最上），地图默认收起。卡片三种：产品卡、冲刺卡、设计卡；IDEO 日志在它服务的卡下占一行。只读日志、不存状态，别的分支读已提交的版本并注明提交；生成物 `scrum/Board.html` 不必进版本控制（本仓库 .gitignore）；由便宜的模型照插件里的约定加模板生成。路线图只放 2.1 的条目和产品日志里的状态，不推算完成度。
- **61 hook**：只注承诺原文（产品、Product Goal、当前目录开着的冲刺或设计），写事实不写指令；两个以上开着的冲刺只注一行计数；没有产品日志、出错、关掉时一律不注；SessionStart 必注，UserPromptSubmit 的频率由测试定。

## 3. How

十个工作块：原型 → hook 研究 → 频率测试标准（先提交）→ hook 脚本与直接运行测试 → 频率测试的跑法与冒烟 → 正式跑与选定 → 看板约定与模板 → 夹具与核对脚本 → 生成 → 接入插件。Master 2026-11-13 放行：本分支提交；合并、tag、发版在 Review 定；不推送。审阅都看分支上的 diff。

## 4. Increment notes

- **hook 研究推翻了 2.2 的一条线索**：Claude Code 不再强制装 Git Bash。定成 shell 形式 `sh "${CLAUDE_PLUGIN_ROOT}/hooks/commitments.sh"; exit 0`，POSIX sh 加 awk、sed 等；根目录加 `.gitattributes` 让 `*.sh` 保持 LF。Codex 支持插件 hook（要用户先在 `/hooks` 里信任），所以同步脚本加了复制 `hooks/`。
- **频率测试**：五臂各 3 次（不装、只 SessionStart、再加每轮、再加每 N 轮、再加只在承诺变了时），一场 14 个提示，中途改一次 Sprint Goal，再 `/compact` 一次，两个探针分别考「过期」和「忘了」。不装 hook 也过线——「决定前引用目标原文」这条约定会让模型自己去读日志，压缩摘要也带着原文；只在 SessionStart 注入的臂过期 2/3。按标准在带 SessionStart 的过线臂里选最省的：A4（开会话、恢复、压缩后各注一次，承诺变了的那一轮再注），一场注 3 次（每轮注是 16 次），每次约 96 token。结论：约定是主力，hook 补位。
- **看板**：约定 `board.md`（16 条，兼给子代理的简报）和模板 `board-template.html`（`data-fact` 标记，地图首次打开才画，离线展开源码）。四批生成：链接写成 `../` 的死链、地图里 `<br/>` 被删、长文手抄丢一个字符——都被检查脚本抓到，规矩补进约定（链接相对 `scrum/`；`<br/>` 转义保留；长文机械拷贝，写完读回对照）；检查脚本自己读错的几处（编号 `H1`、测试夹具里的假冲刺、空状态）也修了。最后一批本仓库现状 2/2 通过，两页事实一致。
- **测试通道**：白名单环境（11 个变量，两个冲刺统一）；magpie 默认 bypassPermissions，加 `--permission-mode dontAsk` 仍被用户 settings 的宽泛 allow 放行，要再加 `--setting-sources project,local` 白名单才真生效。
- **已知限制**（Master 2026-11-14 定，进产品日志）：① 看板生成后插件里没有自动核对，手抄长文仍可能丢字；② hook：没装 Git for Windows 的 Windows 用户不生效，macOS 未实测，Codex 里触发未实测；③ 频率测试用 magpie 的便宜模型、会话不算很长，只分得出大差别；④ 地图靠 CDN，离线只见源码；本仓库现状生成一次 15～25 分钟。

## 5. Test

- **hook**：直接运行测试本机 31/31；WSL 的 dash 配 gawk、mawk 各 26/26；改坏脚本的六种里本机抓到五种、WSL 抓到剩下那种（不去 CR）。真实会话里 startup 注入逐字等于三句承诺；Master 在本仓库实跑，输出三句原文，exit 0，标签跟着日志的语言走。
- **看板**：检查脚本自测 54 条全过；夹具 A、B 各 3 次全过且事实一致；本仓库现状 2/2 通过。
- **DoD**：`claude plugin validate --strict` 通过，plugin-validator（Haiku）无必改项；Codex 同步后 99 个文件，内容、链接、导航 0 错；无死链。
- **审阅**：Master 2026-11-14 审过块 1～10 的提交，复核 strict、Codex 与 hook 实跑。
- **PO**：看过本仓库现状生成的真实看板（第 4 批 real-1），2026-11-14 说「作为第 1 版来说，我觉得还不错」；看板要按他的品味强审重做，登记 PBI-68，开 Sprint 20 做。发版定 v6.0.2。

Master 2026-11-14 定收官（PO 授权）。
