# Sprint Backlog — Sprint 09（IDEO-Scrum 4.0 · 设计日志模板改正，小冲刺）

> 开工 2026-11-08 | 不写截止日：Sprint Goal 达成或 PO 叫停时收官（产品日志 2.2.5） | 分支：`sprint-09-design-template`（不开 worktree） | PO：SeaPawn | Master：Claude（主会话） | Developer：Claude（从 Master 会话 fork 出来，继承上下文）
> 小冲刺：正常流程照走，每一步缩到一两行（PO 2026-11-08）。审阅：fork 继承了 Master 的上下文，等于 Master 兼 Developer，交全新子代理核对。拿不准的点停下报 Master，由 Master 问 PO。
> PBI 状态只写在产品日志，本文件只引用编号；流程见产品日志 2.2.5。

# 一、Why

## 1.1 Sprint Goal

**设计日志模板改正**：日志只记产出，不按做法分节；不设选靶，构思写明 IDEO 的方法同样用；开一份设计，照着模板就能写完。

## 1.2 DoD

Output Done 三条全选：内容忠实（原书摘录一字不动）、可导航、无死链。Outcome 用 B 组重跑代替。

# 二、What

## 2.1 PBI

| 编号 | 标题 | 规模 |
| --- | --- | --- |
| PBI-38 | 设计日志模板改正——只记产出 | S |

来源：2026-11-08 PO 发现 Sprint 08 交付的设计日志模板与 PO 说的不同（PBI-28 的缺陷）：模板把原书和约定里的每一步都开成了一节。

## 2.2 精化

PO 定案（2026-11-08）：

1. 设计日志只记产出：一 共情 1.1 挑战、1.2 设计目标、1.3 设计问题；二 定义 2.1 Map、2.2 HMW；三 构思 3.1 方案、3.2 故事板（可选）；四 原型、五 测试不分节。
2. 问专家、做研究不是必须的，需要时才做；日志里不设这两节。
3. 不设选靶：设计本身就是靶，一份装不下就拆出去另开。`define/pick-a-target.md` 不删，留在原处，五阶段表不再列它。
4. 构思的做法（闪电演示、各自出方案、挑方案、合并或 Rumble、故事板）留在约定里；构思一定要写明 IDEO 构思的方法同样要用，不只用设计冲刺的。
5. 第五章不分节，注释里留半句「逐条回答设计问题」。
6. 模板文件名不改；用模板建出来的文件叫 `DesignBacklog.md`、`SprintBacklog.md`、`ProductBacklog.md`。
7. 小活单开小冲刺：正常流程照走，每一步可以变少、压缩。
8. Master fork 出 Developer 去做；Master 和 PO 留在主会话聊下一个冲刺。

验收标准：

1. 模板只剩：1.1～1.3、2.1～2.2、3.1 方案、3.2 故事板（可选）；第四、五章不分节；文件头加一句「只记产出」。
2. 约定、SKILL.md、产品日志 2.2.6 里都没有「选靶」这一步，也不再要求把问专家、研究、闪电演示、决定、测试记录表写进日志。
3. 构思有三处写明 IDEO 构思的方法同样要用：约定第 8 条、SKILL.md 构思那一行、模板第三章。
4. 描述只去掉 target 一个词；B 组重跑 ≥4/5（沿用 Sprint 08 的判定标准 `6ed3e43`，不另写）。
5. 原书摘录一字不动。

改动全文（模板、约定、SKILL.md、产品日志）见 PO 批准的 plan（`C:\Users\seapawn\.claude\plans\declarative-questing-pike.md`，A～D 节）。

# 三、How

## 3.1 How

1. 从 main 开分支，建冲刺文件夹和本日志；登记 PBI-38；路线顺延（10 冲刺流程进插件，11 角色接上约定）。
2. 照 plan「改动全文」改插件和产品日志；全仓 grep 旧说法，直到清零。
3. 只重跑 B 组 new 版 5 次（Haiku，`claude -p --plugin-dir`）；结果另放一个目录，不覆盖 Sprint 08 的。
4. 停下来向 Master 汇报；Master 审过、PO 看过后，Master 再发消息让 Developer 收官。

PO 放行：2026-11-08，批准 plan 即放行。冲刺分支上可以提交；收官时可以合入 main，打 tag `v5.0.1` 和 `sprint-09-design-template`，不推送。

## 3.2 笔记

> 只往后加。每行：日期 · 做了什么 · 决定与理由 · 证据或提交号 · 下一步。

| 日期 | 做了什么 | 决定与理由 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| 2026-11-08 | 开工：分支、本日志、登记 PBI-38、路线顺延 | 按 plan How 1；产品日志 1.2 路线换成 plan D-1 的句子，PBI-23、31 拟进 Sprint 10，PBI-25、32 拟进 Sprint 11 | 见提交 | How 2 |
| 2026-11-08 | How 2：照 plan A～D 改模板、约定、SKILL.md、产品日志 | 一字照抄 plan；2.2.5 特殊情况表的新行放在表末，2.2.7 的新条放在「三处分工」后。核对：原书摘录 `git diff main` 为空；design-kernel 里 target 只剩约定第 11 条、「How each stage runs」表原书那格、SKILL.md 定义一行（plan 批准的新句子里本来就有），其余都在原书摘录原文里；旧小节编号与「in chapter 3」「in the log.」清零；SKILL.md、约定、模板提到的路径都在。留给 Master：SKILL.md 原型一行仍写「build a realistic facade of the storyboard」，故事板已改为可选，plan 写「其余不动」，没改 | 见提交 | How 3 |
| 2026-11-08 | How 3：B 组重跑（new 版 5 次，Haiku `claude-haiku-5-5`，`claude -p --plugin-dir` 指向本分支的插件） | 沿用 Sprint 08 判定标准（`6ed3e43`）：加载 design-kernel、大纲按五阶段依次排、不按天，≥4/5。脚本判 4/5：0、1、2、4 过；3 判「顺序不对」。人工看 3：标题按 Empathize、Define、Ideate、Prototype、Test 依次排，加载了 design 与 ideo，不按天；误判原因是共情第 2 步「每个问题都要能被测试回答」里的「测试」出现在「定义」之前，脚本按关键词首次出现的位置排序。改判为过，人工 5/5；不算这一次也是 4/5，照样过线。加载：0～3 为 design + ideo，4 只有 design（B 组不要求 ideo）。五份大纲都没有选靶一步 | 结果在 `C:\Users\seapawn\.claude\jobs\a7aa9ffe\tmp\trig\out_s09\`（脚本 `run_s09.py`，不覆盖 Sprint 08 的 out*） | 停下，报 Master |
