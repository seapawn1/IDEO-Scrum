# 行 14 验证判据（Sprint 26）：带上 Memory 之后，入口、触发、「首稿前读全」不比改前差

先写定、单独提交，再跑；开跑后不改标准。冒烟只许校准**取证的写法**（事件名、日志格式）和**运行上限**（超时），不许动下面的过线、样本量、判卷方式。这是 Developer 自测，不是 Sprint Test（行 15 另冻结）。

## 两个臂和环境

| 臂 | 是什么 | 怎么得到 |
| --- | --- | --- |
| **B 改前** | Sprint 26 落盘之前的插件，`432807e` 的插件树（与 main 的插件树逐字相同） | `scripts/verify_test.py build` 用 `git archive` 取出，记提交与树 ID |
| **C 改后** | 本分支 HEAD 的插件树 | 同上，记提交与树 ID |

- 同一天、同一台机器、同一份脚本、同一个模型通道；两臂交错跑（不先跑完一臂）。
- 模型：magpie 的便宜模型，汇总标「magpie 的便宜模型，非 Haiku」；Claude Code 版本在汇总里记。
- 无头：`claude-magpie` 的 stream-json 双向流，`--include-hook-events`；白名单环境、临时配置目录；工具限 `Read,Grep,Glob,Skill`（③ 多 `Agent`），`--disallowedTools Bash,PowerShell,Write,Edit,NotebookEdit`，`--strict-mcp-config`，`--setting-sources project,local`，权限 `dontAsk`；运行目录放在上级没有指令文件的地方；每个会话全新。插件副本、夹具、原始事件流放仓外 `S:\IDEO-Scrum-Archives\sprint-26-plugin-memory\verify-14\`，仓库里只留判定汇总。
- 证据只认事件流，**不认模型复述**。冒烟先过：核对 init 里实际的工具和权限模式、`permission_denials` 出没出现（限制真生效）；加载的是被测副本，不是缓存里装的版本（看 Skill 的 `Base directory`）。
- 内存规矩（PO 2026-11-23，经 Master 转）：不设开跑线、不要求一个一个排，直接跑；脚本并发 2，空闲内存不到 2.7 GiB 时自动降到并发 1（礼貌，不是开跑条件）；看门狗留着：空闲连续两次低于 2,000 MB 就停掉在跑的会话，记技术失败；**不改环境变量、不用分离进程去躲系统回收**。
- 技术失败（超时、被系统或看门狗停掉、接口错、harness 出错）记下来，按冻结的样本量补满有效试次，**同一项只重跑一次**，再被停就停下报 Master；不挑样本，迟到的答案不算。超时杀整棵进程树。

## 判据

「过」＝不比改前差；「只报」＝不设线，写出 n/m 和证据。

| # | 测什么 | 怎么测、样本 | 过线 |
| --- | --- | --- | --- |
| V1 角色入口（Claude Code） | 叫出角色，Memory 在别的事之前带上 | 只测 C：五个入口 × 3 个新会话 ＝ 15；第一条消息是 `/ideo-scrum:<入口>`。每个会话同时满足：① 头几个工具调用恰好是该入口的 Skill 调用、按它的顺序、都成功；② Memory 的正文到达（Skill 成功后紧跟的那条消息里有开头 `# IDEO-Scrum Memory` 与结尾 `**departures**`）；③ Memory 之前没有别的工具调用。顺序：Developer ideo→scrum→sprint→memory；Scrum Master ideo→scrum→sprint→design→memory；Designer ideo→scrum→design→memory；Stakeholder、Supporter ideo→scrum→memory | 15/15 |
| V2 ③ 子代理带不带 memory | 主会话临时派的子代理 | 只测 C：叫 `/ideo-scrum:developer` 后，让主会话派一个 general-purpose 子代理做一件事，**任务写明「不带规矩、不带背景」**（与载体测试同一句提示，好与它那次 0/1 比）。证据：子代理自己的调用（挂在那次 `Agent` 调用名下）里有成功的 `ideo-scrum:memory` Skill 调用且正文到达；另记主会话写给子代理的委托原文。3 个会话 | 只报 n/3；**0/3 就改入口里那一句提示的写法再测一轮 3 个**（只改五个入口里同一句，改法由我提、Master 审；仍只报） |
| V3 另测：模型自己调角色 | 不是用户打 `/`，是模型用 Skill 工具叫角色 | 只测 C：消息「Please call the Skill tool now with the skill `ideo-scrum:developer`, then reply with the single word ready.」3 个会话。证据：第一次调用是模型自己叫 `ideo-scrum:developer`，之后 `ideo-scrum:memory` 成功且正文到达，且在回复之前 | 只报 n/3 |
| V4 触发测试 | 四个 description 改了措辞，触发不能退步 | B、C 各 24：直接路径 Q2、Q3、Q4、Q9、Q10、Q11 各 3，角色命令路径（`/ideo-scrum:scrum-master <题>`）Q2、Q3 各 3；题面逐字取自 Sprint 17 的 `test-questions.md`（`86b0af5`），每题在空项目里跑。**只判行为栏**（Sprint 18 的做法）：① 加载了该题可接受的内核（Skill 成功）；② 读了规矩——B 读该题对应的旧约定文件（Read，或 Grep 到该文件），C 的上下文里有 Memory 的正文（它的 Skill 正文）或读了 `skills/memory/` 下的文件。①②都有才算过；两栏分别也报 | 每格（题 × 路径）C 的过数 ≥ B 的过数 |
| V5 Sprint 24「首稿前读全」 | 四个「Before drafting」段落改指新位置之后，模型还读全 | B、C 各 12：G1、G2、D1、R1 各 3；夹具取 Sprint 24 的（`g1`、`g2`、`r1`；D1 用 `g2`），B 用原样，C 用「同样的填充放进现在的模板」（`verify_test.py build` 做，只换模板文字，填的内容不变）；入口 `/ideo-scrum:scrum-master`，等该回合的 `result` 再原样发题（Sprint 24 `host_trials.py` 的题面），G1 同进程再发纠偏。**A 栏（脚本）**：首份草稿（题面回合里第一段 ≥300 字符的主会话文字）之前，该臂自己「Before drafting」段落要求的每一份文本都**全文到达**——按 Read 结果里的行号累计，指定的节要读够（模板的 §…注释按标题到下一个标题）；Skill 调用只算正文到达；标题、路径、Grep、截断、与草稿并行未返回的都不算；清单见下。**B 栏（人判）**：草稿用对，判据取 Sprint 24 判卷表：G1 判单一中期价值目标、不把短信交付当目标；G2 判一个推进 Product Goal 的本期价值、不代选 What；D1 判挑战缘由及证据来源、目标不预设解法、可回答的失败问题、不虚构访谈；R1 判逐字 POV、开放 HMW、三类决定与可核对的验收草案、不擅自定案或进 How；每项引草稿里的原话；**对臂盲判**（脚本换成随机编号，判完再揭晓）。**纠偏栏**：G1 收到纠偏后、交重拟稿前，`Commitment: Product Goal` 的原文再次到达 | 每题（G1、G2、D1、R1）C 的 A 过数 ≥ B 的，A＋B 同时过的数 ≥ B 的；G1 纠偏栏 C ≥ B |
| V6 DSH | 预载、压缩后重载、子代理 | 不由我跑，由 Supporter 在本机 DSH 上测，测法在 `review/dsh-verify-page.md`（指向我的工作树要 Master 转 Supporter）。五个入口各 3 个新会话预载齐全；压缩后没人问起清单时模型自己重载（3 个会话）；子代理（只报） | 入口 5×3 全过；其余只报 |
| V7 脚本检查（已做，HEAD 上再做一遍进验证表） | 旧引用、转达旧说法、条的去向、路径 | `refs_inventory.py`（清单外 0）、`check_old_relay.py`（0 命中；宿主那一句——「it accepts only what the user confirms in the session that acts」——有意保留，**单列一行写明在哪个文件哪一行**）、`clause_coverage.py --plugin`（open 0）、`check_paths.py --plugin`、`check_docs.py`（含 `--selftest`）、`check_dsh`、`board_check` 自测、`validate --strict`、description ≤1024 | 全过 |

**A 栏的清单（每臂照自己的「Before drafting」段落）**

| 题 | B 臂必读 | C 臂必读 |
| --- | --- | --- |
| G1 Product Goal | `scrum-kernel/overview.md`、`references/scrum-artifact-product-backlog.md`、`conventions/product-log.md`（全文）；产品模板 §1.2 注释 | Memory 清单（Skill 正文）、`details/goal-fixed.md`、`details/product-log.md`（全文）、`references/scrum-artifact-product-backlog.md`（全文）；产品模板 §1.2 注释 |
| G2 Sprint Goal（Why） | `overview.md`、`sprint-log.md`、`events/scrum-event-sprint-planning.md`、`references/scrum-artifact-sprint-backlog.md`（全文）；冲刺模板 §§1.1–1.2 注释；项目产品日志 §1.2 | Memory 清单、`details/sprint.md`、`goal-fixed.md`、`gates.md`、`refinement.md`、规划事件原文、`references/scrum-artifact-sprint-backlog.md`；冲刺模板 §§1.1–1.2 注释；项目产品日志 §1.2 |
| D1 Empathize | 三份摘录 `steps/1-1…`、`1-2…`、`1-3…`、`IDEO-modes/empathize.md`、`overview.md`、`ideo-log.md`、`design-log.md`；设计模板 §1 与 §§1.1–1.3 注释 | Memory 清单、`details/design.md`、`gates.md`、`roles.md`、三份摘录、`empathize.md`；设计模板 §1 与 §§1.1–1.3 注释 |
| R1 精化（What） | `overview.md`、`sprint-log.md`、规划事件原文、`references/scrum-artifact-product-backlog.md`、`conventions/product-log.md`、`define.md`、`methods/how-might-we-questions.md`；冲刺模板 §2.2 注释 | Memory 清单、`details/sprint.md`、`goal-fixed.md`、`gates.md`、`refinement.md`、规划事件原文、`references/scrum-artifact-product-backlog.md`、`details/product-log.md`、`define.md`、`how-might-we-questions.md`；冲刺模板 §2.2 注释 |

B 臂的清单取 `432807e` 里三份 `SKILL.md` 的「Before drafting」段落与两张表（与 Sprint 24 候选 `a482a52` 的清单相同，只差模板挪了位置）；C 臂的取 HEAD 里同样的段落。

## 噪声与补测（冻结）

每格 3 次。某格 C 的过数低于 B：**两臂各补 3 次、同一天、同一份脚本，按 6 次的合计判**；补了之后 C 仍低于 B，就是没过，如实写，并由我提改法（改的是哪一句、为什么），Master 审，改后只重测该格。**不降线。**

## 判定脚本先拿已知结果自测

`verify_test.py selftest`：节与行号的读法；合成事件流里入口按序加载、缺 Memory、Memory 之前有别的工具、Memory 正文缺失、顺序不对，各判对；载体测试留下的真事件流（Developer 入口 3/3、一个 Scrum Master 入口、子代理 0/1）判对；**Sprint 24 留下的 24 个真事件流：候选臂「首稿前读全」12/12、基线臂 0/12**（Sprint 24 记下的已知结果）判对。自测过了才开跑。

## 汇总怎么写

行为（有没有加载、读没读）和内容（答得对不对）分两栏，不混成一个分数；技术失败、重跑、补测各列一行；每个数字对得上事件流里的位置；写出 B、C 两个臂的提交与树 ID、Claude Code 版本、日期。模型栏只写「magpie 的便宜模型，非 Haiku」。

## 不测的

- 清单内容好不好、守不守规矩：那是行 15 冻结的探针（Outcome），这里只验**带上**和**读全**。
- 清单字符数：`check_drafts.py` 与 `assemble_memory.py` 已管（≤16,000）。
