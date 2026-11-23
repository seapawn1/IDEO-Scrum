# 行 14 验证结果（Sprint 26，Developer 自测；证据在仓外 `S:\IDEO-Scrum-Archives\sprint-26-plugin-memory\verify-14\`）

判据：`review/verify-criteria.md`（先写定提交 `1c1676a`，之后只加运行记录，没改过线）。两个臂：B＝`432807e` 的插件树（`c08f0dfd15`），C＝`054d0c5` 的插件树（`d744b2fc12`）；C 的插件树到收官树只差版本与文档。证据只认事件流。

## V1 角色入口（C，Claude Code）：15/15 过

五个入口 × 3 个新会话，都是头几个工具调用按入口顺序加载 Skill 且成功，Memory 正文（开头 `# IDEO-Scrum Memory`、结尾 `**departures**`）到达，Memory 之前没有别的工具调用。

| 入口 | 过数 |
| --- | --- |
| Developer | 3/3 |
| Scrum Master | 3/3 |
| Designer | 3/3 |
| Stakeholder | 3/3 |
| Supporter | 3/3 |

## V2 子代理（只报，C）：原句 0/3，改写后 1/3

- 原句（「Subagents you dispatch load the ideo-kernel, scrum-kernel and memory skills too.」）：3 个会话，三个子代理都没有调过任何 Skill，主会话把用户的「不带规矩、不带背景」原样转交。证据：`round1-old-sentence/`。
- 改写后（五个入口同一句：「A subagent you dispatch does not get these skills from you: begin its task with a line telling it to load the ideo-kernel, scrum-kernel and memory skills first, even when the task is small or was given to you word for word.」，提交 `054d0c5`）：3 个会话。1 个主会话在委托里写了「先加载」，子代理调了 ideo、scrum、memory 三个 Skill 并读了 memory 的 `details/sprint.md`；另 2 个子代理没有调 Skill（一个只 Glob，一个直接回答）。
- **取证方式的说明**：子代理的 Skill 正文不回显（流里只有「Launching skill」），所以按「Skill 调用成功」判，并以子代理随后读了 memory 细则作旁证；若按「正文到达」判，改写后是 0/3。这个取证方式是在看到改写后那一轮的流之后定的，已报 Master，由 Master 定认不认。
- 只报；Review 的待研点候选。

## V3 模型自己叫角色（只报，C）：1/3

消息「Please call the Skill tool now with the skill `ideo-scrum:developer`, then reply with the single word ready.」，3 个会话。1 个：模型叫了 developer，接着加载了 ideo、scrum、sprint、memory，Memory 正文到达，且在回复之前。2 个：模型叫了 developer 后直接回 ready，没有加载内核，也没有 Memory。
- 只报；Review 的待研点候选。

## V4 触发（B、C 各 54 次中的 54 次有效）

每格判据：C 的过数 ≥ B 的过数（第 28 行）。

| 题 | 路径 | B | C | 判 |
| --- | --- | --- | --- | --- |
| Q2 | 直接 | 3/3 | 3/3 | 过 |
| Q2 | 角色命令 | 3/3 | 3/3 | 过（B 第 3 次与 C 第 2 次超时后重跑通过） |
| Q3 | 直接 | 0/3 | 0/3 | 持平，过（改前 432807e 也是 0） |
| Q3 | 角色命令 | 3/3 | 3/3 | 过 |
| Q4 | 直接 | 3/3 | 3/3 | 过 |
| Q9 | 直接 | 3/3 | 3/3 | 过 |
| Q10 | 直接 | 3/3 | 3/3 | 过 |
| Q11 | 直接 | 5/6 | 4/6 | **没过**（按字面判，见下） |

B、C 各补到 6 次的只有 Q11 直接（C 低于 B 时按冻结规矩补 3 次）。

**失败的模式**（全部 9 次行为失败）：

| 臂 | 题 | 次 | 加载了什么 | 没加载什么 |
| --- | --- | --- | --- | --- |
| B | Q11 直接 | 4 | ideo-kernel（Skill）；Read 了 design-kernel 的 SKILL.md 与 `design-log.md` | design-kernel 的 Skill 调用 |
| B | Q3 直接 | 1、2、3 | ideo-kernel | scrum-kernel、design-kernel，没读 `product-log.md`、`design-log.md` |
| C | Q11 直接 | 1 | ideo-kernel（Skill）；Read 了 design-kernel 的 SKILL.md 与 steps，以及 memory 的 design、gates、roles 细则 | design-kernel 与 memory 的 Skill 调用 |
| C | Q11 直接 | 2 | ideo-kernel（Skill）；Read 了 ideo 的 journey-map、point-of-view 方法 | design-kernel、memory，没碰设计的文件 |
| C | Q3 直接 | 1、3 | ideo-kernel | scrum-kernel、design-kernel、memory |
| C | Q3 直接 | 2 | ideo-kernel、memory（Skill）；Read 了 memory 的 product-log 等细则 | scrum-kernel、design-kernel（名单要求其一） |

**Q11 直接，字面判与另一种读法**：字面的 ① 是「加载了可接受的内核（Skill 成功）」，按它判 C 4/6 对 B 5/6，没过。另一种读法（读到该题的约定文件就算，Sprint 17 的写法）：B 第 4 次变过，B 变 6/6；C 第 1 次要看算不算 memory 的细则，C 是 4 或 5/6；两种读法下 C 都低于 B。这个结论不取决于读法，只是 B 的数字取决于它。**我按字面判，不改判；请 Master 定读法。**

**Q3 直接的 C 第 2 次**：加载了 memory 并读了规矩，但没有 scrum-kernel 或 design-kernel 的 Skill。按名单判未过；不影响这一格（0 对 0）。

**超时**（技术失败，不计行为）：`trig-B-Q2-command-3` 与 `trig-C-Q2-command-2.attempt-1`，都是 600.7 秒到点，流里 12 个事件全是 `api_retry`（上游 502，`server_error`，重试到第 7 次，延迟最长约 38 秒），没有任何工具调用。两次都按规矩重跑一次，都过了（B 第 3 次 98.9 秒，C 第 2 次 66.1 秒）。

## V5 Sprint 24「首稿前读全」：B 12/12，C 12/12，24/24 过

题组与次数照旧，改后不比改前差（C ≥ B）。后台跑被系统因内存告急停掉（空闲时），没有部分试次计入；按 Master 指示改为前台分段续跑（`--skip-done`）。逐段记录在仓外 `verify-14\s24-seg*.log`，24 条均为 `pass=True`。

## V6 DSH：秘书会话（Supporter）在本机 DSH 0.2.3-alpha.2 上测完：五个入口各 3 次预载齐全 15/15；压缩后模型先重载 memory 3/3；子代理调了 memory 3/3。逐项与判定见第 4 章「行 14 V1–V4 的结果与偏离」第 ⑦ 条；原始页见 `dsh-test-page.md`、`dsh-verify-page.md`。

## V7 脚本检查：（收官时在收官树上再跑一遍，结果记入第 4 章）
