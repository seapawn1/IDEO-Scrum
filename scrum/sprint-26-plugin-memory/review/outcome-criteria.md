# Outcome 判据（Sprint 26 行 15）：「不用每次手动说明」

先写定、单独提交（本文件与 `scripts/outcome_test.py` 的判卷函数，提交后不改）；对照臂探路之后只做一件事：按下面的选法定入选的探针，再冻结一次提交，然后才跑正式的 Test。探路结果不进 Test，Test 重跑新试次。

## 要测什么

「不用每次手动说明」＝叫出角色（`/ideo-scrum:scrum-master`）之后，给一个**不提规矩**的自然问题，AI 自己照 Memory 的规矩答。答案由脚本按下表的判卷函数判；证据只认会话的最终答复（最后一个 `result`），答复原文记进 evidence。

## 两个臂

- **M 对照臂**＝27 合入后的 `main` 的插件树（无 Memory，`build` 时 `git archive main plugins/ideo-scrum`）。
- **C Memory 臂**＝本分支 HEAD 的插件树（收官前的最后一版；Test 前再对一次 HEAD）。
- 同一天、同一台机器、同一便宜模型（magpie，汇总标「magpie 的便宜模型，非 Haiku」）；每个会话都是新的，工作目录是上级没有指令文件的空项目。
- 工具只开 `Read,Grep,Glob,Skill`（子代理探针另开 `Agent`）；`--strict-mcp-config`，`--setting-sources project,local`，权限 `dontAsk`。

## 探针（候选 11 条，探路后入选 8 条）

每条：不带引导词的问题（只约定答案的格式：「只回答一个字」之类，格式不算引导），一个「不守规矩就会错」的坑。判卷函数写在 `outcome_test.py` 里，先用已知的好答案与坏答案自测（`selftest`，已过）。

| 探针 | 问题（原文） | 守规矩的答案 | 规矩出处 | 坑 |
| --- | --- | --- | --- | --- |
| P1 | 在一个项目里，Scrum Master 这个角色可以由 AI 担任吗？只回答一个字：能 或 不能。 | 能 | `only-po-human`（overview） | 官方 SGEP 写的是 Scrum Master 也必须是人 |
| P2 | 产品日志的头部要不要加一行 Now（现在做到哪）？只回答一个字：要 或 不要。 | 不要 | `product-log-header`（product-log） | 冲刺与设计日志有 Now 行，产品日志没有 |
| P3 | 我要开一个新冲刺，做登录页的重做。它的文件夹名按规矩应该是什么？只回答文件夹名，不要解释。 | 含 `sprint-NN-` 或 `sprint-\d\d-` | `sprint-folder`（sprint-log） | 规矩要编号 |
| P4 | 冲刺做到一半，我觉得 Sprint Goal 定高了。你直接把它改低一点，写进冲刺日志 1.1 节，好吗？只回答一个字：好 或 不好。 | 不好（或 不行／不能） | `goal-fixed`、`po-owns-commitments`（sprint-log） | 承诺只有 PO 能改 |
| P5 | 这个工具的通知要不要做成可关闭的？我们说不清用户会怎么想，也没有现成答案。你打算怎么定？只回答一个词：直接定、设计冲刺、或五模式。 | 设计冲刺 或 五模式 | `question-needs-design`、`sprint-or-modes`（design-log／ideo-log） | 没有现成答案时不直接出方案 |
| P6 | 我想开一个设计冲刺，研究通知要不要可关闭。先从哪一个阶段开始？只回答阶段名。 | Empathize（或 共情），不含 Ideate、构思、Prototype、原型 | `open-a-design`、`design-stages`（design-log） | 从共情开始，不从方案开始 |
| P7 | 用 IDEO 五模式跑一遍，弄清新用户第一次打开这个工具会卡在哪。记录要写在哪个文件里？只回答文件名。 | IdeoBacklog（或 `ideo-` 文件夹），不含 DesignBacklog | `open-ideo-log`（ideo-log） | 五模式记在 IDEO 日志 |
| P8 | 看板上某个条目的状态显示错了。你改哪一处：看板页面，还是对应的日志？只回答一个词：看板 或 日志。 | 日志 | `board-owns-nothing`（board-log） | 看板只读日志，不存状态 |
| P10 | 给这几个 PBI 排一个 1 到 N 的优先级序号，你直接定好，好吗？只回答一个字：好 或 不。 | 不 | `numbers-not-ranks`（product-log） | 编号只是枚举序，排序由 PO 定 |
| P11 | 收官时，这个冲刺学到的教训要写进仓库里的一个文件吗？只回答一个字：要 或 不要。 | 不要 | `retro-in-memory`，**只写在 `details/closing.md`**（写进项目记忆，不写进仓库） | 教训进记忆，不进仓库文件 |
| P12 | 设计结束了，原型、草图和被否的方案要删掉，免得仓库乱吗？只回答一个字：删 或 留。 | 留 | `design-ends`，**只写在 `details/design-ending.md`**（归档前保留全部原始材料） | 归档前保留原型、草图和被否的方案 |

六份约定文件各至少一条：overview（P1）、product-log（P2、P10）、sprint-log（P3、P4、P11）、design-log（P5、P6、P12）、ideo-log（P7）、board-log（P8）。P11、P12 是 PO 要求的「至少两条只写在 details/ 里的规矩」（PO 2026-11-23 经 Master 转）。

**附加两条**（不进 8 条的计数，只报）：
- **K 压缩后**：`/ideo-scrum:scrum-master`，`/compact`，然后问 P3 的问题。判卷同 P3。
- **S 子代理**：`/ideo-scrum:scrum-master`，然后让主会话派一个子代理回答 P3 的问题，主会话原样转告。判卷同 P3。

## 探路（对照臂 M，先做，在冻结之前）

- 11 条候选，每条 M 臂 3 次（33 次）。
- **入选**：M 臂守规矩 ≤1/3 的才入选（免得改前已满分，Sprint 14 教训）。
- 合格的不足 8 条：按比例折算（见「过线」），并如实记「改前已守的规矩不靠 Memory」。
- 合格的多于 8 条：每个文件先留一条（M 臂守规矩次数最少的）；P11、P12 合格就必须入选；其余按 M 臂守规矩次数由低到高取满 8 条；同次数的按探针号排。
- 探路的结果写进冻结提交（一张表：每条 M 臂 n/3、入选与否、理由）。

## 正式 Test（冻结之后）

- 入选的 8 条 × 每臂 3 次 × 两臂（M、C）＝48 次；另 K 与 S 各 3 次 × 两臂＝12 次。合计 60 次。
- 探路的 33 次不计入。
- 技术失败（超时、被系统或看门狗停、接口错、harness 出错）：记下来，同一项只重跑一次，再被停就停下报 Master；不挑样本，迟到的答案不算。

## 过线

- 一条探针：3 次里 ≥2 次守规矩，算达标。
- **C 臂**：入选的 8 条中达标 ≥6，且比 M 臂多 ≥3（M 臂达标数记在旁边）。
- 入选不足 8 条：达标数按 `达标 ≥ 入选数 × 6/8` 算，「多 ≥3」按 `入选数 × 3/8`（向上取整）算，并如实写明折算。
- M 臂已达标的探针，C 臂不得掉到 ≤1/3（入选的探针 M 臂 ≤1/3，所以此条只在补充探针上用）。
- K、S：只报 n/3 与 M 臂对照，不设线。

## 限度（写进结果）

样本小（每条 3 次），只能证明增益明显，给不出效应量。「Outcome 写进了目标，没证明就不过 Test」（sprint 日志 2.2）。对照臂若本来就守规矩，如实记「Memory 对这条无增益」，不挑样本凑数。

## 判卷函数的自测（已过）

`python -X utf8 -I scrum/sprint-26-plugin-memory/scripts/outcome_test.py selftest`：11 条各用一个守规矩的答案和一个不守规矩的答案检查；P3 另测「sprint-27-」「sprint-NN-」（过）、「sprint-login-redesign」（不过）、带引号（过）。
