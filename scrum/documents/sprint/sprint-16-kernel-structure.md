# Sprint Backlog — Sprint 16 (kernel-structure)

> Started: 2026-11-12 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-16-kernel-structure`（worktree `.claude/worktrees/wizardly-almeida-5485e1`）| Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[start sprint] | Developer: IDEO # [developer]-[sprint-16]-[执行冲刺]
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md`, convention 16).
> 归档：2026-11-12 开工并收官，版本不动（仍 5.2.0；v6.0.0 等 Sprint 17 一起发）。日志已压缩成关键决定，逐条原文见 `git show 561a68f:scrum/sprint-16-kernel-structure/SprintBacklog.md`；测试原始输出与基线插件副本在仓库外 `S:\IDEO-Scrum-Archives\sprint-16-kernel-structure\`。

**委托**：PO 2026-11-12 把 Sprint 16、17 全权交 Master；只在三处停等 PO——两个冲刺的 How 一起放行（已「全部放行」）、PO 整份读 Sprint 17 的审阅稿、最后 PO 亲手试一次后 Master 发版。改目标或取消冲刺仍归 PO。

**两个冲刺并行**：本冲刺改结构与加载，Sprint 17 改约定内容；本冲刺先合入 main，Sprint 17 等它合入后从新 main 搬稿。

## 1. Why

### 1.1 Sprint Goal

**结构统一、按需加载**：四个内核各是一个技能，下面带几个文件夹；IDEO 和 Scrum 每个角色都加载，设计和冲刺用到才加载；打开技能就知道该读哪份。

（Master 照 PO 的写法代拟，PO 2026-11-12 说没问题；在 Product Goal「优化现有插件」之内——sprint-kernel 是从 scrum-kernel 拆出来的，不是新功能。）

### 1.2 Definition of Done

- 内容忠实：原文摘录逐字不变，只挪不改；约定的条文只改路径和加载说法；署名照 ATTRIBUTION.md。
- 可导航：从每个技能的 SKILL.md 入口 ≤2 跳到达它的任意文件。
- 无死链：插件和 Codex 包里所有内部链接和路径都解析得到。

Master 2026-11-12（PO 委托）：Sprint Goal 定。

## 2. What

### 2.1 Product Backlog Items

PBI-44（内核结构统一，L）、PBI-57（加载分层，S）、PBI-52（白纸入口，S～M）、PBI-25（插件小修，带 ①②⑥⑦⑧）、PBI-46（Codex 小修，带 ①④）。条目原文见产品日志 3.2 与该提交的产品日志。

### 2.2 Refinement

- **布局**（PBI-44，PO 2026-11-12）：scrum-kernel 的 `SKILL.md` 与 `overview.md` 留在根目录，`assets/` 放两份源材料，`conventions/` 放产品日志的约定和模板，`references/` 放四个工件；新建 sprint-kernel，`conventions/` 放冲刺日志的约定和模板，`events/` 放从 references 挪来的五个事件；design-kernel 五个阶段文件夹合成 `steps/`，16 份文件名带「阶段-步骤」序号；ideo-kernel 的 `conventions/` 由 Sprint 17 建（PBI-56）。
- **引用写法**（`convention N`、`../` 路径）不改，只把路径改对；约定的内容与条号不动，留给 Sprint 17（两个冲刺不改同一处）。
- **加载**（PBI-57）：每个角色（包括 Stakeholder）与派出去的子代理都加载 ideo-kernel 与 scrum-kernel；design-kernel 与 sprint-kernel 在「工作涉及时」加载——Master 2026-11-12 定，依据 PO 原话（Feedback 2026-11-12）「需要 Sprint 的时候才去加载 Sprint……其他两个看需求」。
- **旧路径**全仓 grep 到零（历史归档与产品日志 3.2 不动）；版本号不动（v6.0.0 等两个冲刺做完一起发）。
- **验收** 9 条 + 测试口径：题 1–7 × 直接说/角色命令两条路径 × 3 次；基线 5.2.0 用 `git archive 9769bd6` 解出；过线 ①–④（行为栏不少于基线减 1、无题从过线跌下、白纸题两条路径各 ≥2/3、加载冒烟 8 次全中）。
- 新布局的文件清单写进 How，Sprint 17 照它写审阅稿。

Master 2026-11-12：精化到此（Developer 复述，没有疑问）。

## 3. How

- 13 个工作项：测试题与判定 → 冒烟 → 拆 sprint-kernel → design-kernel 进 `steps/` → 加载分层 → 描述与 25/46 小修 → Codex 适配 → 文档同步 → 自检与校验 → 审阅 → 基线 → 新版 → 收官准备。
- 关键选择：sprint-kernel 的约定表与事件章只挪不改（SGEP 原文不动）；scrum-kernel 的描述让出冲刺用词；design-kernel 步骤按 SKILL.md 五阶段表的顺序编号，`pick-a-target` 排 2-3；测试题先提交后跑、跑后不改；基线固定在 `9769bd6` 的 archive 副本。
- Go-ahead: 2026-11-12，PO（停点 ①，原话「全部放行」）；范围：在冲刺分支上提交；验收和审阅过后由 Master 收官——打 tag、合入 main、关 worktree、删分支；版本号不动；推送在停点 ③ 之后，随 v6.0.0 一起由 Master 做。

## 4. Increment notes

- **结构**（`4a58693`、`7d5a769`）：sprint-kernel 建好（events 五份、sprint-log 与模板移入）；scrum-kernel 的 SKILL.md 让出事件章与两行约定表、指向 sprint-kernel；`scrum-guide-2020.md` 进 `assets/`；design-kernel 16 份改名进 `steps/`（1-1 到 5-3）；全插件路径与技能名说法改对。
- **加载**（`31b23ef`）：四个命令同一段说明——ideo 与 scrum 全加载，design、sprint 在工作涉及时加载，子代理同；overview 第 8 条同改。
- **描述与小修**（`9a42b61`）：三个 SKILL.md 加 Source/License 头；16 份摘录的许可行自足；25 ⑦ 的括号与裸路径、marketplace 顶层说明；25 ⑥ 查明 v2026.1 标签本来就对——`git show e8056d0:...assets/scrum-guide-expanded-2026.1.md`（821 行）是全文，带 Artifacts、Events 两章，29f0e65 把这两章抽走后 assets 只剩其余部分，Sprint 10 的「2025.6」判断是误判；两章与 9 份 reference 对全文逐段核过（规范引号、去引用号后 0 段低 0.97）；改掉 SKILL.md 与 ATTRIBUTION 里「assets 是全文」的说法，CLAUDE.md 那句错的也改了。
- **Codex**（`08fbc86`）：sync/check 适配四个内核与新的加载句；46 ① 只差换行不算差异；idempotency 不再写死分支；重生成后 sync 再跑 0 变化、check 0 错、idempotency 两轮 clean。
- **文档**（`4e1acf3`）：README 文件地图按四内核与新布局改；CLAUDE.md 三处 sprint-log 指向改到 sprint-kernel。
- **自检**：`check_paths.py`（先自测）197 条路径、2 条链接、140 处 convention 引用，0 缺；`claude plugin validate --strict` 插件与 marketplace 都过；Codex sync/check 0 错。
- **审阅三批**：plugin-validator（Haiku）两处必改——ATTRIBUTION 第 1 节把 SGEP 摘录记在 2020 版名下、ideo-kernel 跨 skill 路径；建议也照改（三处引用、四命令说法、两个描述压到 1024 内），`check_paths.py` 收紧（`e6ac751`）。Master 审一处必改——「只在开冲刺时加载」改成「work involves a Sprint — opening, running, resuming, or closing one」，overview、描述、interface、Codex 加载句同改；46 ④ 文案批用；sprint-kernel 描述补「与教材版不同」（`1ecea3b`）。对抗审查 4 处必改——sprint-log.md 里 10 处裸 `overview.md`、2 处 `product-log.md` 改成 `../scrum-kernel/...`；scrum-kernel 描述只留路由一句；冲刺模板的 product-log 引用改成文字定位；overview 第 8 条开头改成两个都加载；`check_paths.py` 收紧到模板以外的裸文件名解析不到就算错（`28876de`）。
- **测试通道**：`claude -p`，起子进程时去掉 `CLAUDE_CODE_HOST_AUTH_ENV_VAR`、`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`、`ANTHROPIC_BASE_URL`；模型 claude-haiku-5-5；只开 Read、Grep、Glob、Skill；基线插件用 `git archive 9769bd6` 解到仓库外；每次调用给一个新的空 TEMP/TMP 与工作目录（冒烟时模型会翻到同级旧测试目录）。

## 5. Test

- 基线与新版同日各 42 次，加加载冒烟 8 次；题目与判定先提交后跑，跑后未改；汇总两张表与原始输出在仓库外（见顶部）。
- **过线 ① ✓**：行为栏 路径一 20/21、路径二 18/21（线 18、18）。
- **过线 ②③ ✗**：题 3（白纸）路径二基线 2/3 → 新版 1/3。两次回答只写「现在不写产品日志，也不开 Sprint」「第一步是开一个设计……而不是直接写产品日志」，没写必答 ③「设计的结论会流回产品日志」；一次写了「设计的结论再填进产品日志」，算过。题 3 路径一 0/3 → 2/3，触发改善。
- 题 2 路径二 0/3（基线 1/3）：三次只 Glob 空项目目录，没读约定；内容却是中的。
- **过线 ④ ✓**：加载冒烟 8/8（四个命令各 2 次，都只加载 ideo 与 scrum，没有 design/sprint）。脚本第一次判成 0/8，原因是比对没去 `ideo-scrum:` 前缀，逐条看过原始输出后改判，理由已写在汇总里。
- 一次回答算过：路径一 19/21（基线 17），路径二 16/21（基线 18）。

Master 2026-11-12（PO 委托）：测试结果选 (a)——不改判、不补跑，②③ 记为已知缺口，PBI-52 移到 Sprint 17 接着做。理由：题 3 两条路径的行为栏都 3/3，触发这一块做成；缺口在内容，是约定的写法，归 Sprint 17；路径二 2/3→1/3 只差一次，样本 3 次分不清噪声；只补跑一题违反「插件文字改了就整轮重跑」；Sprint 17 的流程测试本来包含题 3 与题 2 两条路径。**收官。**
