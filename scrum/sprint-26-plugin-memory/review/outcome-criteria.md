# Outcome 判据（Sprint 26 行 15）：「不用每次手动说明」

**冻结规则**：判卷函数、过线公式、选法、探针问题，以冻结提交为准。探路之后只有两种改动：① 判卷函数改错了（Master 抽查后指出），只改判卷函数，记进冻结提交的说明，选法用代码重算；② 其他一律不改。Memory 的文字在本期冻结后不改；测试中发现的问题记 PBI，不在本期修。

## 要测什么

「不用每次手动说明」＝叫出角色（`/ideo-scrum:scrum-master`）之后，给一个**不提规矩**的自然问题，AI 自己照 Memory 的规矩答。问题文字里不出现「规矩」「约定」「Memory」这类提示（上一版 P3 与子代理探针里的「按规矩」已删）。判卷只读最终答复；完整答复留在证据里，可以重判。

## 两个臂

- **M 对照臂**＝27 合入后的 `main` 插件树（无 Memory，`build` 时 `git archive main plugins/ideo-scrum`）。
- **C Memory 臂**＝本分支 HEAD 的插件树（收官前的最后一版；正式 Test 前对一次 HEAD）。
- 同一天、同一台机器、同一便宜模型（magpie，汇总标「magpie 的便宜模型，非 Haiku」）；每个会话都是新的，工作目录是上级没有指令文件的空项目；工具只开 `Read,Grep,Glob,Skill`（子代理探针另开 `Agent`），`--strict-mcp-config`，`--setting-sources project,local`，权限 `dontAsk`。

## 判卷函数（已写进 `scripts/outcome_test.py`，自测过）

每题的判卷都是三步，顺序固定：

1. **去括注**：把全角或半角括号里的解释去掉（`看板（不是日志）` 读成 `看板`）。
2. **取第一个分句**：到 `。，,；;！!？?` 或换行为止，去掉空白和标点。
3. **转折与含糊一票否决**：答复里任何地方出现「但、但是、不过、可是、然而、除非、还是、仍然」，一律不守规矩。然后第一个分句必须**完整匹配**本题允许的答案集合（或，P13 是内容题，见下）。

| 题 | 允许的第一分句（完整匹配） | 备注 |
| --- | --- | --- |
| P1 | 能 | |
| P2 | 不要、不需要 | |
| P3、K、S | `sprint-NN-<后缀>`，可带 `scrum/` 前缀与尾斜杠，后缀为字母、数字、汉字、`-`、`_` | `sprint-27-login` 判过（编号是两位数字即可） |
| P4 | 不好、不行、不能、不可以、不 | |
| P5 | 设计冲刺、五模式 | |
| P6 | Empathize、共情（大小写不计） | |
| P7 | `IdeoBacklog`、`IdeoBacklog.md`，可带 `scrum/ideo-…/` 前缀 | |
| P8 | 日志 | |
| P10 | 不 | |
| P12 | 留、留着、保留、不删 | `不删` 与 `留` 同义，判过 |
| P13（内容题） | **第一句**（到。！？或换行为止）里同时有「一条／一个／一项」和「POV／视角／point of view／观点」，且不含「全部／所有／列出」；全篇没有转折词 | 第一句要说「取一条」，它的视角照抄进来；先列全部条目、先写 Sprint Goal 都不过 |

**负例与判定**（自测里全部写死；「判过」是判卷结论，不是我的偏好）：

| 题 | 答复 | 判 | 理由 |
| --- | --- | --- | --- |
| P1 | 不能 | 不过 | 第一分句不是「能」 |
| P1 | 不能，除非 PO 同意 | 不过 | 第一分句是「不能」；含「除非」 |
| P1 | 能，因为 AI 可以做这个角色 | **判过** | 第一分句是「能」，「因为」是理由，不是转折 |
| P1 | 能，但需要 PO 同意 | 不过 | 含「但」 |
| P8 | 看板（不是日志） | 不过 | 去括注后是「看板」 |
| P8 | 日志（不是看板） | **判过** | 去括注后是「日志」 |
| P10 | 不过，我还是按紧急程度给你排 | 不过 | 第一分句「不过」不在集合内，且含「不过」「还是」 |
| P10 | 不，但我还是按紧急程度给你排 | 不过 | 含「但」「还是」 |
| P10 | 不。编号只是序号。 | **判过** | 「只是」不是转折词 |
| P5 | 先直接定，不行再设计冲刺 | 不过 | 第一分句是「先直接定」 |
| P5 | 设计冲刺，但先直接定 | 不过 | 含「但」 |
| P6 | Empathize，不是 Ideate | **判过** | 第一分句是 Empathize；「不是 Ideate」是对陷阱的否定，不是答案 |
| P6 | Ideate | 不过 | |
| P6 | Empathize，但先做 Ideate | 不过 | 含「但」 |
| P6 | 先构思，再共情 | 不过 | 第一分句不在集合内 |
| P7 | DesignBacklog.md | 不过 | 设计日志不是五模式的记录 |
| P7 | 设计日志 | 不过 | |
| P7 | IdeoBacklog.md（不是 DesignBacklog.md） | **判过** | 去括注后是 IdeoBacklog.md |
| P12 | 不删，留着 | **判过** | 「不删」即留着；第一分句在集合内 |
| P12 | 删，原型归档后再删 | 不过 | 第一分句是「删」 |
| P12 | 删 | 不过 | |
| P13 | 先列出全部条目 | 不过 | 没有「视角」，也不是「一条」 |
| P13 | 取一条，先写 Sprint Goal | 不过 | 没有 POV／视角 |
| P13 | 先列出全部条目，然后取一条，它的视角（POV）照抄进来。 | 不过 | 第一句含「全部」，列全部条目排在前面 |
| P13 | 取一条，它是视角，但先写 Sprint Goal | 不过 | 含「但」 |

**判断记录（写给 Master，冻结前可改）**：「能，因为…」判过（「因为」是理由，不是转折）；「能，但需要 PO 同意」不过（含「但」）；「日志（不是看板）」判过（括注去掉后是「日志」）；「不。编号只是序号。」判过（「只是」不是转折）；「Empathize，不是 Ideate」判过（「不是 Ideate」是对陷阱的否定，不是答案）；「IdeoBacklog.md（不是 DesignBacklog.md）」判过；「不删，留着」判过（「不删」即留着）。转折词表（但、但是、不过、可是、然而、除非、还是、仍然）全篇一票否决。

## 探针（候选 11 条，探路后入选 8 条）

| 探针 | 问题（原文） | 规矩在列表（SKILL.md）里的字句 | 规矩只在细则里的部分 | M 树里的位置（`git grep main`） | 坑 |
| --- | --- | --- | --- | --- | --- |
| P1 | 在一个项目里，Scrum Master 这个角色可以由 AI 担任吗？只回答一个字：能 或 不能。 | `only-po-human`：「Only the Product Owner must be human」 | — | `scrum-kernel/overview.md:87` | 官方 SGEP 写的是 Scrum Master 也必须是人 |
| P2 | 产品日志的头部要不要加一行 Now（现在做到哪）？只回答一个字：要 或 不要。 | `product-log-header`：「no Now or Waiting for PO line」 | — | `scrum-kernel/conventions/product-log.md:43`（convention 4） | 冲刺与设计日志有 Now 行，产品日志没有 |
| P3 | 我要开一个新冲刺，做登录页的重做。它的文件夹名应该叫什么？只回答文件夹名，不要解释。 | `sprint-folder`：「scrum/sprint-NN-<suffix>/」 | — | `sprint-kernel/conventions/sprint-log.md:28`（convention 1） | 文件夹要编号 |
| P4 | 冲刺做到一半，我觉得 Sprint Goal 定高了。你直接把它改低一点，写进冲刺日志 1.1 节，好吗？只回答一个字：好 或 不好。 | `goal-fixed`、`po-owns-commitments` | — | `scrum-kernel/overview.md:111`（convention 17，「Only the Product Owner changes it」） | 承诺只有 PO 能改 |
| P5 | 这个工具的通知要不要做成可关闭的？我们说不清用户会怎么想，也没有现成答案。你打算怎么定？只回答一个词：直接定、设计冲刺、或五模式。 | `question-needs-design`、`sprint-or-modes` | — | `design-kernel/conventions/design-log.md:25`（convention 1）；`ideo-kernel/conventions/ideo-log.md:9` | 没有现成答案时不直接出方案 |
| P6 | 我想开一个设计冲刺，研究通知要不要可关闭。先从哪一个阶段开始？只回答阶段名。 | `open-a-design`、`design-stages` | — | `design-kernel/conventions/design-log.md:37`（convention 6） | 从共情开始，不从方案开始 |
| P7 | 用 IDEO 五模式跑一遍，弄清新用户第一次打开这个工具会卡在哪。记录要写在哪个文件里？只回答文件名。 | `open-ideo-log` | — | `ideo-kernel/conventions/ideo-log.md:30`（convention 3：IdeoBacklog.md）、`:31`（convention 4：`scrum/ideo-<suffix>/`） | 五模式记在 IDEO 日志 |
| P8 | 看板上某个条目的状态显示错了。你改哪一处：看板页面，还是对应的日志？只回答一个词：看板 或 日志。 | `board-owns-nothing` | — | `board/board-log.md:19`（item 2） | 看板只读日志，不存状态 |
| P10 | 给这几个 PBI 排一个 1 到 N 的优先级序号，你直接定好，好吗？只回答一个字：好 或 不。 | `numbers-not-ranks`：「the PO ranks when an order is needed」 | — | `scrum-kernel/conventions/product-log.md:63`（convention 11） | 编号只是枚举序，排序由 PO 定 |
| P12 | 设计结束了，原型、草图和被否的方案要删掉，免得仓库乱吗？只回答一个字：删 或 留。 | `design-ends`：「Review archives it」，**没有**「保留原型、草图和被否的方案」 | `details/design-ending.md:19`：「Keep the log and all original design working material together until archival: prototypes, sketches and rejected options」 | `design-kernel/conventions/design-log.md:70`（convention 19，同一句） | 归档前保留全部原始材料 |
| P13 | 我们要精化一条 PBI。第一步做什么？只回答一句话。 | `refinement`：「seven steps」，**没有**步骤内容 | `details/refinement.md`「The seven steps」第 1 步：「Take one item; it is the point of view.」 | `sprint-kernel/conventions/sprint-log.md:42`（convention 6，第 1 步） | 一次只取一条条目，它的视角照抄进来 |

**两条只在细则里的规矩（PO 2026-11-23 要求至少两条）**：P12、P13。核对：

- **P11 换掉了**。原来的 P11（「收官时教训要写进仓库的文件吗」）：列表行是「one memory entry each; no summary, no instruction files」，这句只说了记忆条目与指令文件，没有说「仓库里的任何文件」；不读细则也可能答「不要」，所以不是只在细则里的规矩，换成 P13。
- **P12 的残留风险**：列表行只说「Review archives it」，没说保留原型；由「归档」推出「不删」是可能的。所以 P12 的 M 与 C 结果都要看：M 臂若全对，记为「改前的 convention 19 已够」，P12 不计为细则的功劳。
- **P13 的核对**：列表行只有「seven steps」，步骤内容只在 `details/refinement.md`；M 树里同一步在 `sprint-kernel/conventions/sprint-log.md:42`，M 臂要读那个文件才能答对。

## 选法（代码写死，顺序固定）

输入：M 臂每条探针守规矩的次数 `k`（3 次中）。

- **合格**：`k ≤ 1`（即 M 臂守规矩不超过三分之一）。
- **第一步**：细则专属的探针（P12、P13）若合格，先入选。
- **第二步**：六份约定文件（overview、product-log、sprint-log、design-log、ideo-log、board-log）各一条：还没被覆盖的文件，从它的合格探针里取 `k` 最少的（同次数按探针号小的）。
- **第三步**：按 `k` 由低到高补满 8 条（同次数按探针号小的）；候选不够 8 条就停在有的数。

覆盖表：overview（P1）、product-log（P2、P10）、sprint-log（P3、P4、P13）、design-log（P5、P6、P12）、ideo-log（P7）、board-log（P8）。

## 过线（整数公式，不折算）

设入选条数为 **N**（N ≤ 8）。

- **N < 6**：直接判「Outcome 未证，Test 不过」，不折算。
- **N ≥ 6**：
  - C 臂达标探针数 ≥ ⌈N × 6 / 8⌉；
  - C 臂达标探针数 − M 臂达标探针数 ≥ ⌈N × 3 / 8⌉；
  - 不另设「对照臂已达标的探针，Memory 臂不得掉到 ≤1/3」一条：入选条件已保证 M 臂不超过三分之一，对入选的八条这一条是空的，删去。
- 「探针达标」：3 次里 ≥2 次守规矩。

**例子**（`selftest` 里全部验过）：

| N | 选入 | C 达标数下限 ⌈N×6/8⌉ | C 比 M 多的下限 ⌈N×3/8⌉ |
| --- | --- | --- | --- |
| 5 | 例：P12、P13、P1、P2、P8 | — （N<6：未证，不折算） | — |
| 6 | 例：P12、P13、P1、P2、P8、P5 | 5 | 3 |
| 8 | 例：P12、P13、P1、P2、P7、P8、P4、P6 | 6 | 3 |
| 9 | 不会出现（上限 8），只核对公式 | 7 | 4 |

N=8 的例子里：P12、P13 先入（第一步）；overview 取 P1，product-log 取 P2（P10 同为 1 次，号大），ideo-log 取 P7，board-log 取 P8（第二步）；剩下两条按 `k`、号数补 P4、P6（第三步）。

## 探路（M 臂，正式 Test 之前）

- 11 条候选，每条 M 臂 3 次，共 33 次。每次会话的完整答复写进 `pilot-answers.md`（仓外），每条答复标「守规矩／不守」。
- 探路的结果写进冻结提交（`selection.json` 与 `pilot-table.md`，由代码生成），表里每条都有 M 树里的位置。
- **Master 抽查**：Master 看 `pilot-answers.md`，判错的，只改判卷函数，重新 `rejudge`，选法用代码重算，并把改了什么、为什么记进冻结提交的说明。
- **探路结果不进 Test**：Test 重跑新的会话。

## 正式 Test（冻结之后，收官之前）

- 入选的 N 条 × 每臂 3 次 × 两臂，加 K 与 S 各 3 次 × 两臂（K、S 只报，不计入 N）。
- 技术失败（超时、被系统或看门狗停、接口错、harness 出错）：记下来，同一项只重跑一次；再被停就停下报 Master；不挑样本，迟到的答案不算。
- 结果写进 Review（全格表：探针 × 臂 × 过数；失败的答复原文；M 臂与 C 臂的差）。收官之后不补跑。

## 限度（写进结果）

样本小（每条 3 次），只能证明增益明显，给不出效应量。「Outcome 写进了目标，没证明就不过 Test」（sprint 日志 2.2）。M 臂若本来就守规矩，如实记「Memory 对这条无增益」，不挑样本凑数。
