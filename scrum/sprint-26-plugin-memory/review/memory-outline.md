# Memory 的方案与大纲（Sprint 26 行 3、行 5）

Developer 提，Master 审定。PO 2026-11-23 定了 A1（「26那就选择A1把，然后dsh要支持要记得」）；下面是行 5 剩下要定的几项，每项给提议、理由和被否的做法。载体测试的结果（①②④ 与档位）出来后补在第 10 节。

## 1 位置与名字

- `plugins/ideo-scrum/skills/memory/SKILL.md`：名字就叫 `memory`（PO 11-17 的设想）；正文就是清单，现在装配后 14,148 字符、102 行，加 frontmatter 约 14.7k。
- `plugins/ideo-scrum/skills/memory/long/<文件>.md`：16 个长文件；清单里指向它们的行写 `→ long/<文件>.md`（相对技能目录）。
- 描述 353 字符（上限 1024），与三个内核同一写法，召唤才来：「Use only when summoned: an ideo-scrum role command tells you to load it, or the user asks for the plugin's Memory (the shared rules every role follows). When summoned, invoke this skill before answering, even for a short request. General questions about Scrum or design that do not name this plugin are not a summons: answer normally without loading it.」落盘后重跑触发测试，不能比改前差。

## 2 带上方式：A1，写进角色入口，Memory 排最后

每个角色入口的加载序列末尾多一步 `ideo-scrum:memory`（用户打 `/ideo-scrum:<角色>`，入口按序调 Skill，与现在调内核同一路）：

| 角色 | 现在 | 改后 |
| --- | --- | --- |
| Scrum Master | ideo → scrum → sprint → design（4） | … → memory（5） |
| Developer | ideo → scrum → sprint（3） | … → memory（4） |
| Designer | ideo → scrum → design（3） | … → memory（4） |
| Stakeholder | ideo → scrum（2） | … → memory（3） |

- **为什么排最后**：自动压缩后，技能从最近调用的开始重新附上，所以最后调用的最先保住。PO 说的「先加载 memory」读作「在做任何角色工作之前加载」，入口本来就写「回复或开始别的工作之前先调」，所以不冲突。
- **压缩后的余量**（每个技能取前 5,000 token、合计 25,000；英文约 4 字符一个 token，估）：

| 角色 | 技能数 | 14.7k 字符的清单：保住的 token／余量 | 20,000 字符（5,000 token 封顶）：保住的 token／余量 |
| --- | --- | --- | --- |
| Scrum Master | 5 | 15,356／39% | 16,689／33% |
| Developer | 4 | 13,086／48% | 14,419／42% |
| Designer | 4 | 12,538／50% | 13,871／45% |
| Stakeholder | 3 | 10,268／59% | 11,601／54% |

  余量都 ≥ 20%，按冻结判据②的条文不另测调用顺序。真清单约 3,700 token，离每技能 5,000 token 的线还有约 26%；两档测试就是试这条线。
- **子代理**：角色入口里「派出的子代理也加载 ideo-kernel、scrum-kernel」那句加上 memory。被否的「只放相关几行」：靠派发者挑行，漏挑了就没有规矩。代价：每个子代理多约 3.7k token。③ 实测（可选，只报）看有没有用。

## 3 共用还是分角色：一份共用，行上带角色标签

- 一份清单，所有角色都加载；行首 `[dev,sm]` 之类的标签（`dev` `sm` `des` `stk` `po`）标出只约束哪些角色，没有标签的行约束每个角色。现在 102 行里 85 行不带标签，17 行带（`dev` 5、`sm` 3、`sm,po` 7、`po,sm,des` 2）。
- 理由：A1 整份加载；分角色要拆多个技能、多份描述、入口再指定读哪份，多一跳。标签让 Developer 的 DoD 核对、Scrum Master 的阶段门各自看得出归谁。⑦ 的报告看 ① 的会话里每个角色带上了什么。
- 被否：每角色一份（`memory-dev` 等）：多 4 条描述，共用的规矩要抄四遍。

## 4 一行的句型

```text
- **<句柄>** [<角色>] <一句话，英文，≤150 字符，软线 130>。→ long/<文件>.md [pending S27]
```

- 句柄：2–4 个英文词、短横线连接，全清单唯一，只起名字作用；别的行、长文件、旧「convention N」引用迁成句柄，用反引号引。
- 角色标签可无；`→` 只在细节在长文件时写；`[pending S27]` 只在等 Sprint 27 的行上，27 合入后去掉。
- 一行只管一件事、照着能做；理由与例外进长文件，不进清单。
- 示范（新行逐字取自 `memory-draft/MEMORY.md`；括号里是旧规矩，原文逐字在对应的 `review/review-<文件>.md`）：
  1. `- **role-entry** On a role command, load that role's kernels in order before any work; stop and report a failed load. → long/roles-and-routing.md`（overview#8）
  2. `- **stage-gates** Wait for the PO's explicit permission to start or return to a stage; approving a result is not permission. → long/stage-gates.md`（overview#12）
  3. `- **outward-needs-po** Push, release and other outward actions need the PO's consent; a stage permission never covers commit, merge or push.`（sprint-log#19）
  4. `- **facts-then-questions** [sm] *Supplement.* Look up facts yourself; ask the PO in one numbered message, each with a recommended answer.`（product-log#3）
  5. `- **board-writer** A cheap model writes scrum/ScrumBoard.html when the PO wants to look or a log changed. [pending S27]`（board-log#3）

## 5 长文件的判据

- 进长文件、清单留一行索引：规矩带表、图、步骤清单或分情形细则；或只在做某件事时才要读（写看板、设计各阶段、冲刺收官）。一句话说得清的留在清单。
- 一个主题只服务一种活的（如 board-log 的 19 条），规矩全进长文件，由一行索引：草稿里写 `via`，被指的规矩没有自己的行，由索引行的句柄指它。
- 核验得来的一条：别处没有的内容，不能因为「模板或脚本已有」就删——例如 `scripts/board_check/check.py` 在仓库根，装插件的人没有。
- 16 个长文件：`names`、`layers-and-folders`、`departures`、`goal-fixed`、`sprint-refinement`、`product-log-details`、`ideo-ending`、`handoff`、`stage-gates`、`sprint-closing`、`design-ending`、`board-writing`、`sprint-stages`、`design-stages`、`flow-maps`、`roles-and-routing`（最后一个是 27 现状的版本，27 合入后重写）。

## 6 图与 Departures 表去处

- 图：六张流程图合进 `long/flow-maps.md`（Mermaid `flowchart TD`），框里写句柄，图上每一步指到适用的规矩；清单一行 `flow-maps` 指过去。
- Departures 表（`overview.md` 的「与 Scrum Guide 不同之处」）：整表逐字进 `long/departures.md`，清单一行 `departures`；README「How it differs」与它逐字对表并链到它的锚点，`check_docs.py` 的对表来源与锚点跟着改（行 13）。
- 署名行：随含摘录的文件走；行 12 核「带摘录的文件有 Source／License 两行且与 `ATTRIBUTION.md` 一致」。

## 7 尺寸

- 提议：不再沿用 ≤8,000 字符（那是写草稿前的估计）。上限取两条里小的：A1 在测试里过 ②（压缩后开头与结尾都在）的最大一档；每技能 5,000 token 线的 80%，约 16,000 字符，给 token 估算的误差留余量。现在的 14.1k 在内。
- 超了怎么办：往长文件挪；仍装不下，报 Master。

## 8 落盘时的后果（行 12–14）

- 新描述 ≤1024 并测触发；四个角色入口各加一步、子代理那句加 memory；加载数 4/3/3/2→5/4/4/3（Sprint 24 的 F07 口径跟着改）。
- DSH：`dsh/index.js` 3 行加 3 行删、`scripts/check_dsh.mjs` 4 行加 2 行删（⑥ 在副本上已过：改前改后都 7/7）；`SKILL.md` 的 `description` 要写成单行双引号字符串，适配器的 `readEntry` 只认这个形状（三个内核也是）；秘书会话在 DSH 里实测，页在 `review/dsh-test-page.md`。
- `claude plugin validate --strict`；结构有变（新技能目录、入口命令）就派 `plugin-dev:plugin-validator`（Haiku）。
- 版本号与 README 中英首行；`docs/`、glossary 等处的「convention N」引用迁成句柄，`AGENTS.md` 第 44、56 行指向 `conventions/` 的路径改成指向 Memory（PO 2026-11-22 已点头，只改这两处）；迁完全仓 grep 旧值到零（行 13）。

## 9 被否的做法（PO 选 A1，不是测出来的）

- **A2 并入 `scrum-kernel`**：不新增文件，但 `scrum-kernel`（约 13.2k 字符）与清单共用 5,000 token，清单的尾部可能被截；Stakeholder 也带上；名字不叫 memory。
- **B hook**：不靠模型自觉、能按角色选段，但 Claude Code 与 DSH 各写一份，要再补一条 `PreToolUse` 才覆盖「模型自己调 Skill 叫角色」。
- **C 合用**：A1 加压缩后补注的 hook；A1 若在实际尺寸上过不了 ② 才用得上，所以不先做；真过不了经 Supporter 报 PO，不自行改用。

## 10 载体测试结果

### ⑥ DSH 能否等价：过（2026-11-23，秘书会话实测，Master 转述）

环境：DSH 0.2.3-alpha.2，包 0.6.3；临时 profile `a1test` 指向我的副本（`dsh-a1-copy`），没动 web profile，测完已删；原始日志在 `~/.dsh/sessions/--S-IDEO-Scrum--/`（仓外）。

| 题 | 结果 | 证据 |
| --- | --- | --- |
| 1 预载是否完整 | 是 | `user/message`（skill-invocation，30,386 字符）里，ideo、scrum 两个内核原文的首行和末尾 100 字符逐字命中 |
| 2 压缩后还在吗 | **只剩摘要** | DSH 压缩后用 `compaction/summary`、`compact-checkpoint`（3,047 字符）替换原文，不像 Claude Code 那样重新附上技能；压缩后模型自己调了 `skill(memory)`（tool/call seq 48）重新载回；配置里没找到单个技能或预载总量的上限 |
| 3 `long/` 走得通吗 | 是 | 按 `Base directory` 读 `scrum-kernel/references/…`，seq 29，`isError:false` |
| 4 技能清单 | 每条描述截到 500 字符 | 四个内核都被截（`scrum-kernel` 原文 968 字符）；memory 的 353 字符放得下；清单总长 5,166 → 5,212。截断影响现有内核在 DSH 的触发，不是本期的事，Master 另登记 |
| 5 子代理是否继承角色正文 | 否 | DSH 的子代理（origin:subagent）只拿到委托消息、技能清单和运行时上下文 |
| A1 真跑 | 过 | 预载按 ideo → scrum → memory 成功（45,673 字符，开头 `# IDEO-Scrum Memory` 与结尾的 departures 行都在）；压缩后原文不在，模型调 `skill(memory)` 重载后，两行答案与原句逐字一致 |

结论：DSH 做得出等价，没有新机制，只是压缩后行为不同：要靠模型重新加载 Memory。后果（Master 定）：DSH 的路由说明里加一句「对话压缩之后，继续前先重新调用 memory 技能」，与 `dsh/index.js` 那几行一起做；子代理那条照报：DSH 的子代理要靠委托消息里写明去加载 memory。

我的一个担心，记在这里留给行 12、14：路由说明在角色正文里，而 DSH 压缩会把角色正文一起换成摘要，这句话压缩后可能跟着没了；所以行 14 的 DSH 验证要测「压缩后没人问起清单内容时，模型会不会自己重载」，不够稳再改放进 DSH 会一直回放的命名上下文里。

### ①②④ 与档位、③、另测、⑦、⑧

待正式测：被系统因内存紧张停掉（第 1 批 4/12 个试次完成）；Master 安排等 27 收官、内存腾出后并发 1 续跑，⑧ 的 `validate --strict` 在那之后跑。
