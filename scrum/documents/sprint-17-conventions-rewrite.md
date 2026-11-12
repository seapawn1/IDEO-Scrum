# Sprint Backlog — Sprint 17 (conventions-rewrite)

> Started: 2026-11-12 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `sprint-17-conventions-rewrite`（worktree `.claude/worktrees/awesome-pare-fb64d7`）| Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[start sprint] | Developer: IDEO # [developer]-[sprint-17]-[执行冲刺]
> How to write this log: `sprint-log.md` in the sprint-kernel skill's `conventions/` folder.
> Keep every heading, even the ones filled later; add none — remarks go in chapter 4, Increment notes (`overview.md`, convention 16).
> 归档：2026-11-12 开工，2026-11-13 收官，发版 v6.0.0（Sprint 16、17 一起发）。日志已压缩成关键决定，逐条原文见 `git show 2a0697b:scrum/sprint-17-conventions-rewrite/SprintBacklog.md`；审阅稿、改动点清单、测试题与汇总在同一提交的 `scrum/sprint-17-conventions-rewrite/` 里；测试原始输出在仓库外 `S:\IDEO-Scrum-Archives\sprint-17-conventions-rewrite\`（`round1/`、`round2/`）。

**委托**：PO 2026-11-12 把 Sprint 16、17 全权交给 Master，原定三个停点：
- ① 两个冲刺的 How 一起放行：已放行，PO 原话「全部放行」。
- ② PO 整份读本冲刺的审阅稿：PO 读后说「OK，相当好」，并追加 IDEO 日志与模板。
- ③ PO 亲手试：PO 2026-11-13 取消，改为收官后自己看。

推送和更新本机插件交 PO 的辅助会话。改 Sprint Goal、改 Product Goal、取消冲刺，仍由 PO 定。

**两个冲刺并行**：本冲刺先在 `drafts/` 里按 Sprint 16 的新布局写全文审阅稿，不碰 `plugins/`。Sprint 16 合入 main（`72d398f`）后，再从新的 main 搬进插件。

## 1. Why

### 1.1 Sprint Goal

**约定改顺**：攒下的反馈都改进约定；设计冲刺和五阶段法分清；熟手照着就能走。

（Master 照 PO 的写法代拟，PO 2026-11-12 说没问题；在 Product Goal「优化现有插件」之内——只改约定，不加新功能。）

### 1.2 Definition of Done

- 内容忠实：PO 的原话、已批准的命令 Identity 和原书摘录逐字不变；约定是作者写的，可以大改，不在原文上打补丁。
- 可导航：从每个技能的 SKILL.md 入口，≤2 跳到达它的任意文件。
- 无死链：所有内部链接、路径和「convention N」都解析得到，而且指对。

Master 2026-11-12（PO 委托）：Sprint Goal 定。

## 2. What

### 2.1 Product Backlog Items

本冲刺做的条目（原文见产品日志 3.2）：
- PBI-54：产品日志与冲刺约定修订，S。
- PBI-58：设计约定修订，M。
- PBI-56：设计冲刺与 IDEO 五阶段法分清，带上 IDEO 日志与模板，M。
- PBI-53：Developer 在别的工具里怎么协作，S。
- PBI-46：只带 ③，S。
- PBI-52：白纸入口，S～M，2026-11-12 从 Sprint 16 移来。

### 2.2 Refinement

- **收进的点**：
  - PBI-54 四点：① Now 行；② 什么算卡住；③ Review 怎么判过时；④ 照抄 2.1 时对照 Sprint Goal 查够不够。
  - PBI-58 ①–⑧：「测试前 PO 先看原型」不进插件；Designer 兼不兼 Master 由 PO 定。
  - PBI-56 的分界：PO 指定；PO 没指定时，要先做原型、拿角色卡测过才敢动手的，开设计冲刺；其余用五模式。
  - PBI-53：写成角色和步骤，工具做法只当例子。
  - PBI-46 ③：核对「派全新子代理」在 Codex 里怎么做。
- **做法**：
  - 先写稿、后搬。
  - 大改约定照 CLAUDE.md 的审阅顺序：大纲 → 全文 → Master 审 → 对抗审查 → 停点 ② → 搬运 → 最后一轮流程测试 → 收官。
  - 内容与改号分开提交。
- **PBI-52 并入**（Master 2026-11-12）：Sprint 16 改描述之后，题 3 的触发已经解决；剩下的缺口在约定写法上，归本冲刺。验收加第 8 项：题 3 两条路径各至少 2/3。
- **IDEO 日志并入 PBI-56**（停点 ②）。PO 原话：

  > OK，相当好，但是差了一件事情，我不知道有没有补充完毕，什么呢，就是说ideo-kernel，没有出现模板，我希望可以出一个文件IdeoBacklog.md，虽然我觉得基本不会用到，然后里面就是标准得五节，没有什么拆分（这时候一般是不上design-kernel得，所以一般不会读哪个kernel，所以要注意区分，是ideo方法论还是design sprint），然后conventions得log，你看着稍微写一写就好，我估计很少，主要是区分一下就可以，对然后就可以了，也就是说差一个文件夹conventios，里面得log和模板。你看sprint17好不好补充，这样最好，，思考一下这个问题。应该如何更好的处理

  Master 定：照另三个内核，在 `conventions/` 放日志约定和模板。原来的分界约定 `design-sprint-or-five-modes.md` 并进 `ideo-log.md`，当第 1 条。IDEO 日志放在 `scrum/ideo-<suffix>/`；模式之间没有 PO 关卡，可以来回走；结论流回提问的那份日志；下一次 Sprint Review 照设计日志的办法归档。

- **架构与关系**（PO 2026-11-13）。PO 原话：

  > 是的，冲刺16没问题，其余你都自己决定住就可以了。是的，但是这个log也需要一个架构也要补充上去。其余的我觉得没啥问题了，但是还是那句话，要说明ideo五阶段法和设计冲刺之间得关系，不能乱，这个东西很容易乱得。其余得我觉得都没啥问题。

  Master 定：
  - overview 的图加一个分界节点，分出两支。
  - `ideo-log.md` 的图画出五模式的三种用法。
  - 两者的关系只写在 `ideo-log.md` 第 2 条。
  - 混着说的两句改掉：design-kernel `SKILL.md` 的「five IDEO stages」，design-log 第 20 条的「Run the design sprint as the IDEO five-stage method」。

- **停点 ③ 取消**（PO 2026-11-13）。PO 原话：

  > OK，最后全部完成即可，我就不进行审阅了，全部完成，推送更新先不做，到时候我给辅助对话去做。你只需要监督全部完成，做完review retro，然后你直接相关得活全部完成即可。最后我审阅后没问题，我会推送更新，不会找你，会直接归档掉你，如果有问题，我再会找你。ok，权限全部交给你

- **验收**（9 项）：
  1. 每一点都对到约定的文件和条；
  2. 一条规矩只写一处；
  3. 引用都指得到，而且指对；
  4. 停点 ②；
  5. 最后一轮流程测试过线；
  6. 校验通过；
  7. 停点 ③（已取消）；
  8. PBI-52 的题 3；
  9. IDEO 日志。
- **测试口径**：
  - 跑法：12 题都走直接说；题 2、题 3 另走 `/ideo-scrum:scrum-master`；每条路径 3 次，各自至少 2/3 过。
  - 判定：照 Sprint 14 的写法，判定不比被测的那句话严；先提交、后跑，跑后不改。
  - 汇总：分行为、内容两栏。

Master 2026-11-12：精化到此（Developer 复述，没有疑问）。

## 3. How

- **14 个工作项**：改动点清单 → 大纲 → 设计侧全文 → 冲刺侧全文 → 连带改动与引用核对 → Master 审与对抗审查 → 停点 ② → 搬运 → 测试题 → 最后一轮流程测试 → 校验 → 停点 ③（取消）→ 收官准备；第 14 项补 IDEO 日志与模板。
- **关键选择**：
  - 先写稿、后搬。
  - 53 写成角色和步骤（overview 第 15 条）。
  - 58 ⑦ 照 Claude Code 文档写目标和通用的局限，工具细节记笔记。
  - 46 ③ 照实查过再写。
  - 改号脚本对到短名，再逐处读。
- **放行**：Go-ahead 2026-11-12，PO（停点 ①，「全部放行」）。2026-11-13 改：停点 ③ 取消；收官和 v6.0.0 的本地发版由 Master 做；main、tag、记忆库都不推送，推送和更新本机插件交 PO 的辅助会话。

## 4. Increment notes

- **审阅稿**（`8e6dc95`、`cb2e6be`）：
  - 设计侧：design-log 27 条，新增第 12 条「While they sketch, talk with the Product Owner」，原第 12–26 条顺延；设计模板两处注释；ideo-kernel 的分界约定。
  - 冲刺侧：sprint-log 改第 5、6、10、17、22 条，新增第 26 条「Developer in another session or tool」；冲刺模板加 Now 行；product-log 改第 2、12、17 条；overview 改第 2、7、12、14 条。
  - Master 两批审阅，必改 8 + 4 处，例如：第 1 条补回「没有现成答案」；第 11 条整条重写；模板不用 `../` 路径；第 26 条拆成两种情况。
  - 对抗审查（全新 Haiku 子代理）收 5 处。
- **46 ③ 的依据**：`codex-cli 0.167.0` 没有子代理——`agents` 只是浏览会话，`exec fork` 是复制会话。所以「全新子代理」定义成只从简报起步，fork 和复制都不算；没有子代理的工具，开一个只给简报的新会话（overview 第 7 条）。
- **58 ⑦ 的依据**：Claude Code 文档的 sub-agents 一页 *What loads at startup*。非 fork 的子代理默认带着各级 CLAUDE.md 和 git 状态快照；Explore、Plan 两样都不带；`omitClaudeMd` 去不掉受管策略。约定只写「简报不给现状」和通用的局限。
- **搬运**（main 合入 `18f9202`，内容 `9ffb765`，改号 `d5c0e6a`，Codex `4212a2a`）：
  - Sprint 16 改过的地方都保留了。
  - Master 用短名对照核对改号：旧引用全部指回原来那一条。
  - 一处必改：设计模板第 7 行丢了 Sprint 16 加的「in `design-log.md`」，`3a69305` 补回。
- **IDEO 日志**（`3d823bd`，审阅后 `d9533bf`、`d4ac082`）：
  - 新文件：`ideo-log.md`，一张图加四条；`ideo-backlog-template.md`，五章不分节，头部写明「不是设计冲刺的日志」。
  - 指向和连带：8 处指向改了名；overview 的图、开头的文件列表和第 3、4、5、7 条，sprint-log 第 17 条，README 都跟着改。
  - Master 审出 8 处必改，例如：「in sequence」和「不分先后」矛盾；分界处六个「on the spot」把 IDEO 日志排除在外；图里的连线连错了节点。对抗审查 9 条收 3 条，驳回的 6 条理由记在原日志。
- **第 1 轮测试后的改动**（`47733c8`、`1e524be`）：
  - 三份描述：ideo-kernel 写明「IDEO 五阶段法」就是五模式，并加上「没有现成答案」时的触发；design-kernel 写明它不是五阶段法，「Five stages」改成「Five design-sprint stages」；scrum-kernel 改成先照分界定。
  - design-kernel `SKILL.md` 开头加一句指向 ideo-kernel。
  - 白纸：overview 图里的白纸改回连设计冲刺，这是 Master 先前让一起连到分界节点、连错了的；design-log 第 1 条和设计模板头部带上白纸的要旨。
  - sprint-log 第 6 条写明由 PO 照分界定。
  - plugin-validator（Haiku）PASS。
- **描述压回 1024 以内**（`c67940e`，收官前）：
  - 起因：第 2 轮的两份描述超过了 1024 字符的上限（ideo-kernel 1130、design-kernel 1191）。这个上限来自 Agent Skills 规范，plugin-validator 会报，Codex 也照它。Master 审第 2 轮时只对了 Claude Code 的 1536，漏了 Sprint 16 已经定下的 1024。
  - 处理：Dev 会话已关，由 Master 兼 Developer 压到 1013、1018。全新子代理（Haiku）审出 1 处必改：原型验证的触发条件在压缩时被删掉了，已补回。
  - 收官时 main 上多了别的会话的 `e810e43`（CLAUDE.md），已先合进分支（`1732a11`）。
- **测试通道**：本机 `claude -p`，起子进程时去掉网关和认证变量（`ANTHROPIC_BASE_URL`、`CLAUDE_CODE_USE_GATEWAY`、`CLAUDE_CODE_HOST_AUTH_ENV_VAR`、`ANTHROPIC_AUTH_TOKEN`、`CLAUDE_CODE_OAUTH_TOKEN` 等），子进程才会走本机登录；reclaude 不可用。冒烟时核对过：加载的是 worktree 版本；`--debug` 里没有技能清单超出预算的警告。

## 5. Test

- **第 1 轮**（42 次）：9/14 过。没过的：题 2 直接 0/3；题 3 两条路径都是 1/3；题 9 0/3，一个技能都没加载；题 10 0/3，三份都把「IDEO 五阶段法」当成了设计冲刺，正是 PO 说的「乱」。
- **第 2 轮**（改描述后，同一天、同一条通道，第 1 轮当基线）：10/14 过，行为栏没有一题退步。
  - 题 2：3/3 和 3/3。
  - 题 3：2/3 和 3/3，验收第 8 项满足。
  - 题 9：直接 0/3，仍然多半不加载技能，直接定成做验证或做原型。
  - 题 10：直接 0/3。三份都用五模式、都开 `IdeoBacklog.md`、都写了结论回流，r3 还说出了什么时候转开设计冲刺；只缺必答 ②（模式之间没有 PO 关卡、不按固定顺序、先读模式和方法文件，三者任一）。判定照旧，不改判。
- **触发测试**（描述压缩后，15 次：题 3、4、9、10、11 直接路径各 3 次，同一条通道；原始输出在 `round3-trigger/`）：行为栏对第 2 轮依次是 2/3→2/3、3/3→3/3、0/3→0/3、3/3→3/3、3/3→3/3，没有退步。
- **验收**：
  - 第 1、2、3、6 项过：对照表齐；两轮审查的必改都清零；引用 198 处 0 缺，并逐处读过；validate 通过，plugin-validator PASS，Codex 0 不一致，四份描述都在 1024 字符以内。
  - 第 4 项过：PO「OK，相当好」。
  - 第 7 项：取消。
  - 第 8 项过。
  - 第 5、9 项没满足：题 9，以及题 10 的必答 ②。
- **DoD**：
  - 忠实：PO 原话、命令 Identity、原书摘录都没动；scrum-master 命令只改了 Code of Conduct 一行，Master 同意过。
  - 可导航：ideo-kernel 入口 → `conventions/`，一跳。
  - 无死链：引用核对 0 缺。
- **Review 的外部视角**（全新 Haiku 子代理，照产品日志 2.1 的角色卡）：
  - 熟手：照着走、要提醒的地方少了；Now 行、四种卡住、2.1 查够不够都顺手；五模式和设计冲刺分得清，也知道各自记在哪。风险是默认分界靠判断，PO 不点名时 AI 可能选错——进 PBI-59。
  - 陌生人：两者同名，要读两遍才分清。README 第 69 行仍写「按 IDEO 五阶段组织」，SGEP 没展开——收官时改了；role cards 等术语找不到解释——进 PBI-30。

Master 2026-11-13（PO 委托）：收官。题 9 和题 10 的必答 ② 记成已知缺口，登记 PBI-59，不跑第 3 轮。理由有三：
1. PO 担心的「混着说」已经没有了。
2. 题 2、题 3 都改好了。
3. 题 9 属于直接路径、问题里没有关键词的触发缺口，同一类缺口在题 3 上从 Sprint 14 拖到了本冲刺；再跑多半只是在追判定。
