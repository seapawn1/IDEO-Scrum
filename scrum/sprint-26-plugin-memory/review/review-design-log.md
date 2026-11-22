# 审阅：design-log.md（design-kernel）

每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。
读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。

本文件 27 条：删 2、并 3、改 13、留 9；另有 6 个非编号块（文末）。

---

### design-log#1 · Open a design for a question with no ready answer

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 25–25 行

**旧规矩原文**

> 1. **Open a design for a question with no ready answer** — When a question asks what people want or what counts as good, ask first whether a ready answer exists; if not, settle whether it needs a design sprint or the five modes (`../ideo-kernel/conventions/ideo-log.md`, convention 1); when it needs a design sprint, open a design and start with Empathize once the Product Owner authorizes it, not with solutions (convention 26). A blank page — the product and its Product Goal cannot be written yet — is a case of this: the design's conclusions fill the product log (`../scrum-kernel/conventions/product-log.md`, convention 2).

**出处与依据**：作者（把握：中）；种类：规矩
- commit 7e3e5b6 feat(PBI-49)：设计日志修订稿，PO 决定、Master 提议，加入「开设计」相关条（PBI-50）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 144 行：写明「Open a design for a question with no ready answer 写明什么时候必须开设计（PBI-50）」

**建议**：改；去处：清单（一行）

**理由**：行为规矩要留（先问有没有现成答案，再定走设计冲刺还是五模式）；但一条里塞了四件事（触发、先 Empathize、待 PO 授权、白纸项目），应拆短；白纸一句与第 19 条的收官选目标重叠，留一处即可。

**新行**

```text
- **question-needs-design** A question of what people want or what is good: look for a ready answer, else pick a design sprint or the five modes.
- **open-a-design** Open a design for a design sprint and start with Empathize on the PO's permission, never with solutions; a blank page is one.
```

**备注**：The pointers become handles: sprint-or-modes, stage-gates and blank-page. Line 1 is over the soft limit on purpose; it keeps the 'ready answer first' test.

---

### design-log#2 · Hard point, not the whole item

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 26–26 行

**旧规矩原文**

> 2. **Hard point, not the whole item** — From a Sprint, take out only the hard point that needs design; the rest of the Sprint goes on.

**出处与依据**：作者（把握：中）；种类：规矩
- commit b49278d feat(PBI-28)：设计日志约定 v1，设计与 Sprint 分开成两件事
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 75 行：流程测试题 2「为它开设计、只取出这个难点、从共情起」

**建议**：留；去处：清单（一行）

**理由**：一句话的行为规矩，写不进别处又很短，留着；它划出设计与 Sprint 的边界，删了会丢「其余 Sprint 照常」这层意思。

**新行**

```text
- **hard-point-only** From a Sprint, take out only the hard point that needs design; the rest of the Sprint goes on.
```

---

### design-log#3 · Who

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 27–27 行

**旧规矩原文**

> 3. **Who** — The Designer is accountable for the design, and the Scrum Master facilitates and records; what the Product Owner decides is listed in convention 21. Empathize and Define — the challenge, the design goal, the design questions, the map, and the How Might We questions — are settled by the Product Owner with the session that plays the Scrum Master, who writes them into the log; the Designer takes over at Ideate. A design often needs only one session; whether that session also plays the Scrum Master, or a separate Scrum Master session runs, is the Product Owner's call. When one session plays both roles, write the same name in both fields of the header; it settles Empathize and Define with the Product Owner itself.

**出处与依据**：作者（把握：中）；种类：规矩
- commit b49278d feat(PBI-28)：设计日志约定 v1，写入设计者负责、Scrum Master 记录的分工
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/design-line-po-in-the-room.md：共情和定义由 PO 与 Master 当面定，一个会话就定完，Designer 从 Ideate 接手
- archive scrum/documents/design/design-board.md 第 43 行：「共情、定义由 PO 和 Master 当面定，比交给一个新会话快、也准」

**建议**：改；去处：清单（一行）

**理由**：清单保留一行：共情与定义由 PO 与 Scrum Master 当面定，Designer 从 Ideate 接手，是否另设 Scrum Master 会话由 PO 定。同一会话兼两角色时在表头两栏写同一名字的写法仍缺，要补进 design-backlog-template.md 第 3 行；Designer 负责、SM 记录的分工见 commands/designer.md:15 与 commands/scrum-master.md:52、57。

**新行**

```text
- **design-roles** [po,sm,des] The PO and Scrum Master settle Empathize and Define; the Designer owns the design from Ideate on.
- **one-session-both-roles** [po,sm,des] The PO decides if one session plays Designer and Scrum Master; if so, write its name in both header fields.
```

**备注**：The old rule also pointed at the list of what the PO decides (design-log#21); that list is the stage-gates and design-stage lines. The loss lens found the 'same name in both fields' sentence only here, so it stays in a line.

---

### design-log#4 · Branch

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 28–28 行

**旧规矩原文**

> 4. **Branch** — A design opens its own branch when it opens; the on-the-spot decision is only its base — the Sprint branch or `main`. Do not name it `<sprint-branch>/<name>`: git cannot hold both `a` and `a/b` as branch names.

**出处与依据**：作者（把握：中）；种类：格式
- commit b49278d feat(PBI-28)：设计日志约定 v1，首次写入设计分支的开设规则
- commit 7e3e5b6 feat(PBI-49)：设计日志修订稿，「定分支排在填表头之前」

**建议**：改；去处：清单（一行）

**理由**：分支规则不能只留在模板：design-backlog-template.md 第 3 行只有 Branch 字段，没有「设计开自己的分支、基分支为 Sprint 分支或 main」，也没有「不要命名 <sprint-branch>/<name>」；convention 19 还引用 convention 4。清单留一行保留开分支、基分支与命名禁令。

**新行**

```text
- **design-branch** A design opens its own branch off the Sprint branch or main; never name it <sprint-branch>/<name> (git cannot hold a and a/b).
```

---

### design-log#5 · Open a design

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 29–29 行

**旧规矩原文**

> 5. **Open a design** — Pick a suffix that says what the design is about, with no number; create `scrum/design-<suffix>/`; copy the template into it as `DesignBacklog.md`; fill in the header: where the design came from, the branch (convention 4), the Product Owner, the Designer, the Scrum Master, and the Now and Waiting for PO lines (convention 24). The folder holds the log, the prototypes, and the working material — sketches, gathered ideas, a grid of reactions; prototypes and working material never go into an Increment.

**出处与依据**：作者（把握：中）；种类：规矩
- commit b49278d feat(PBI-28)：设计日志约定 v1 与模板（design-kernel/conventions/），首次写入设计文件夹与模板的开设步骤
- archive scrum/documents/sprint/sprint-09-design-template.md：设计模板的结构与开设约定

**建议**：改；去处：清单（一行）

**理由**：清单留一行：设计文件夹里放日志、原型和工作材料，原型与工作材料永不进 Increment。目录命名与复制见 SKILL.md:37，表头字段见 design-backlog-template.md:3-7，目录布局见 overview.md:61（overview#4 保留的长文件）；后缀「说明设计内容」只在 design-log.md:29，需并入 overview#4 的长文件。

**新行**

```text
- **design-folder** A design lives in scrum/design-<suffix>/ (a suffix saying what it is about, no number); its prototypes never go into an Increment.
```

---

### design-log#6 · Start from the people

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 37–37 行

**旧规矩原文**

> 6. **Start from the people** — Start Empathize with the people concerned. When the Product Owner is the person concerned, ask first for concrete experiences — what happened, what they did, what they said — and only then ask for the Product Owner's call on what it means; otherwise start with users the Product Owner can bring. Documents and role cards come after. Write each finding where it belongs — in the challenge, the design goal, or the design questions — with its source, and say whether it is first-hand (what a person said or did) or second-hand (a record made for another purpose, or a role card's reading). Write the design goal as a vision: why we are doing this, and where we want to be — not how; a sentence that tells how belongs to Ideate. Keep the goal's one-row commitment table in section 1.2, as `../scrum-kernel/overview.md`, *Goal fixed, plan flexible*, says.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 7e3e5b6 feat(PBI-49)：设计日志修订稿，新增「从当事人起」一条
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 144 行：列出「Start from the people」为设计日志条文之一

**建议**：改；去处：长文件

**理由**：先听当事人、一手与二手分开标留清单一行；PO 是当事人时先问具体经历再问其对含义的判断、否则先找 PO 能带来的用户，以及「文件与角色卡在后」这两条顺序要求只在 design-log.md:37，模板与 SKILL.md 的 Empathize 说明没有，应随本条进长文件，不能只归阶段说明。

**新行**（长文件 `design-stages`）

```text
- **design-stages** Details of each design stage: people first, experts if unclear, the map, ideas, prototype, role-card test. → long/design-stages.md
```

**备注**：The index line for the stage details. design-log#6: start Empathize with the people concerned; when the PO is the person concerned ask first for concrete experiences, then for their call on what it means, otherwise start with users the PO can bring; documents and role cards come after; mark each finding first-hand or second-hand; write the design goal as a vision, not a how; keep the one-row commitment table in 1.2.

---

### design-log#7 · Experts when needed

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 38–38 行

**旧规矩原文**

> 7. **Experts when needed** — Once you have heard the people concerned (convention 6), write the challenge, the design goal, and the design questions; ask experts and do research only when these are still unclear. The experts are the Product Owner, in the conversation, and the role cards (`../scrum-kernel/overview.md`, convention 7), each played by a fresh subagent. Before asking experts, draft a rough map (`steps/2-1-make-a-map.md`); the log keeps what changed, not each interview. After asking the experts or doing research, refine the challenge, the design goal, the design questions, and above all the map once more: fill the gaps and redraw the map.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 7e3e5b6 feat(PBI-49)：设计日志修订稿，写入「先定挑战与目标，再找专家和做研究」
- archive scrum/documents/ExpertNotes.md 第 21 行：「一条重要原则：先定 goal 和挑战，再做深度研究」

**建议**：留；去处：长文件

**理由**：行为规矩保留：先听当事人，再写挑战、设计目标与问题；只在仍不清楚时才找专家或做研究，并在之后精化目标与重画地图。专家构成、每张角色卡用新子代理、先画粗地图与「只记变化不记访谈」是细则，放长文件，清单留一行索引。

**新**：只在长文件 `design-stages`，清单里由 `design-stages` 一行索引。

**备注**：After hearing the people, write the challenge, the design goal and the design questions; ask experts (the PO in the conversation, role cards each played by a fresh subagent) and do research only if still unclear; draft a rough map first; the log keeps what changed, not each interview; afterwards refine all three and redraw the map.

---

### design-log#8 · Map and questions in the log

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 42–42 行 · 标记：Departs

**旧规矩原文**

> 8. **Map and questions in the log** — Draw the map as a Mermaid `flowchart TD`, actors at the top and the ending at the bottom, and keep it rough — five or six boxes and one loop. Draw the experience we want to reach, not what happens now: the way things are today, and where it hurts, go in chapter 1 with their sources (convention 6). *Departs from the book:* the book's step maps the situation as it is. Branches, exceptions, and solutions belong to the Ideate solution and storyboard, not in the map; if someone who never learned design cannot read it at a glance, a solution has been put inside. Write the How Might We questions against the map, with the challenge, the design goal, and the design questions of chapter 1 beside it. The map, together with the challenge, the design goal, and the design questions, is the point of view here; do not write a separate one. The Product Owner picks the How Might We questions that matter — no dot voting. There is no target step while the design runs; a design that began from a blank page picks its target when it ends (convention 19). If the map holds more than one design's worth of work, split the rest out into another design or into items (`steps/2-3-pick-a-target.md` shows how the book narrows a map).

**出处与依据**：作者（把握：中）；种类：格式
- commit b49278d feat(PBI-28)：设计日志约定 v1，写入地图与问题写在日志里的条文
- memory S:/SeaPawn-Memory/memory/GlobalMemory/mermaid-td-and-tables.md：Mermaid 一律 flowchart TD

**建议**：改；去处：长文件

**理由**：地图画法与「只画想要达到的体验、五六框一个回环」留清单一行；「外行一眼读不懂就是塞了方案」「地图+挑战+目标+问题就是 point of view、不另写」「PO 选 HMW、不 dot voting」三条只在 design-log.md:42，必须随本条进长文件；分支与方案不进图在 design-backlog-template.md:36，目标选择见 steps/2-3-pick-a-target.md，步骤文件里没有这些。

**新**：只在长文件 `design-stages`，清单里由 `design-stages` 一行索引。

**备注**：Map: a Mermaid flowchart TD, actors at the top and the ending at the bottom, rough (five or six boxes, one loop), the experience we want not today's (today's goes in chapter 1 with sources; departs from the book); branches, exceptions and solutions are not in the map (a reader who never learned design who cannot read it at a glance means a solution is inside); the map with the challenge, goal and questions is the point of view; the PO picks the How Might We questions, no dot voting; no target step while the design runs; a blank-page design picks its target when it ends; split a map that holds more than one design's work.

---

### design-log#9 · Lightning Demos (optional)

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 46–46 行

**旧规矩原文**

> 9. **Lightning Demos (optional)** — When existing ideas would help, have subagents search for them in parallel; keep the list as working material, not part of the log. If subagents sketch (convention 11), the list is split among them, so that each starts from different ideas.

**出处与依据**：作者（把握：低）；种类：规矩
- commit c946ed7 feat(Sprint 20)：PBI-70 约定小修，首次出现「Lightning Demos (optional)」一条；未查到更早的出处

**建议**：改；去处：清单（一行）

**理由**：Lightning Demos 可选：需要现成想法时让子代理并行搜；清单只作工作材料、不进日志（已在 convention 10），子代理画方案时清单分开给（已在 convention 11）。并行搜这一条只在 design-log.md:46，步骤文件 3-1 是书里的轮流 tour，不能替代，应留清单一行。

**新**：只在长文件 `design-stages`，清单里由 `design-stages` 一行索引。

**备注**：Lightning Demos is optional: when existing ideas would help, have subagents search for them in parallel and keep the list as working material, not in the log; if subagents sketch, split the list among them so each starts from different ideas.

---

### design-log#10 · Diverge before you converge

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 47–47 行

**旧规矩原文**

> 10. **Diverge before you converge** — Whoever sketches a solution — a subagent (convention 11), or the main thread with the Product Owner (convention 12) — diverges first: use at least two methods, at least one of them from the ideo-kernel's Ideate methods, as `SKILL.md` requires (the first steps of the book's sketch, `steps/3-2-sketch.md` — notes, ideas, Crazy 8s — may be used alongside), go for quantity, and hold judgment back — and only then converge into a sketch. When you brief a subagent, tell it so. The ideas are working material; they do not go into the log.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 7e3e5b6 feat(PBI-49)：设计日志修订稿，「先发散后收敛」进入设计日志
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md 第 25 行：PBI-47「设计的构思——先发散后收敛」，要求每个草图至少两种方法发散

**建议**：留；去处：清单（一行）

**理由**：核心行为规矩：先发散、至少两种方法且其中一种来自 ideo-kernel、发散时不做判断，然后才收敛。删了会丢「不跳过发散直接出方案」的防线，故留。

**新行**（长文件 `design-stages`）

```text
- **diverge-first** Sketchers diverge first: two methods, one of them an ideo-kernel Ideate method, quantity, no judgment. → long/design-stages.md
```

**备注**：The sentence 'when you brief a subagent, tell it so' and 'the ideas are working material and stay out of the log' are in the design-stages long file (section Ideate: diverge before you converge).

---

### design-log#11 · Isolated solutions (optional)

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 51–52 行 · 标记：Decide on the spot

**旧规矩原文**

> 11. **Isolated solutions (optional)** — When several solutions that differ in approach are wanted, have several fresh subagents, unable to see one another, each sketch one complete solution in words or Mermaid. Give each its own materials — chapters 1 and 2 and its own part of the gathered ideas, or none until it has drawn — together with `steps/3-2-sketch.md` and the ideo-kernel Ideate methods, and give any summary apart too: one summary handed to all of them makes the sketches converge on one idea (in one design, two subagents given the same summary of reference examples both drew a subway map). Beyond chapters 1 and 2, give it nothing about how things are solved today — no current design, rules, or code — and tell it not to read the project's files. Each diverges first (convention 10). Some tools hand the project's instructions to every subagent anyway; when that happens, note it in the design log. Without subagents, the main thread and the Product Owner sketch together (convention 12).
>     *Decide on the spot:* whether to use subagents at all, how many, and on which model, within how the Product Owner chose to run this round (convention 26).

**出处与依据**：作者（把握：中）；种类：规矩
- commit c946ed7 feat(Sprint 20)：PBI-70 约定小修，首次出现「Isolated solutions (optional)」一条
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/design-line-po-in-the-room.md：两个子代理拿到同一份小结，方案趋同，材料连小结一起分开
- archive scrum/documents/design/design-board.md 第 43 行：「两个画方案的子代理拿到同一份「模式小结」，方案趋同成一个思路」

**建议**：改；去处：长文件

**理由**：隔离子代理互不可见、各拿自己的材料与小结、先发散、不提供当前设计/规则/代码并叫它别读项目文件，这些留清单一行；工具把项目指令传给每个子代理时记进设计日志，以及 Decide on the spot 由 PO 定是否用子代理/用几个/什么模型，随本条进长文件（design-ideate.md）；steps/3-2-sketch.md 是逐字书摘，不能承接这些。

**新**：只在长文件 `design-stages`，清单里由 `design-stages` 一行索引。

**备注**：Isolated solutions (optional, Decide on the spot): several fresh subagents that cannot see one another each sketch one complete solution in words or Mermaid, each with its own materials (chapters 1 and 2 and its own part of the ideas, or none until it has drawn) and its own summary (one summary for all makes them converge: two subagents given the same summary both drew a subway map), nothing about how things are solved today and told not to read the project's files; each diverges first; some tools hand the project's instructions to every subagent anyway and then that is noted in the design log; without subagents the main thread and the PO sketch together. Whether to use subagents, how many and on which model is decided within how the PO chose to run this round.

---

### design-log#12 · Talk with the Product Owner

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 53–53 行

**旧规矩原文**

> 12. **Talk with the Product Owner** — Whether or not subagents sketch, the main thread asks the Product Owner whether they have ideas and talks them over, diverging first (convention 10), without rushing to converge. If the Product Owner has no idea, the main thread sketches one direction on their behalf, as one of the lines. All the lines — the subagents' sketches if there are any, the Product Owner's ideas, the main thread's own — come back to the main thread, are merged, and only then does it converge (convention 13).

**出处与依据**：作者（把握：中）；种类：规矩
- commit c946ed7 feat(Sprint 20)：PBI-70 约定小修，首次出现「Talk with the Product Owner」一条（-S 查到的最早提交；同类条文在 design-log 中的位置随后由 7e3e5b6 调整）

**建议**：留；去处：清单（一行）

**理由**：行为规矩：不论有没有子代理，主线程都先和 PO 谈想法，所有路线回到主线程合并后才收敛。删了会丢「PO 没想法时由主线程替他画一个方向」的规矩，故留。

**新行**

```text
- **talk-with-po** The main thread talks ideas over with the PO and merges all lines before converging; with none from the PO, it sketches one.
```

---

### design-log#13 · Choosing is the key step

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 54–54 行

**旧规矩原文**

> 13. **Choosing is the key step** — Run the book's decision (`steps/3-3-decide.md`) in the conversation, led by the Scrum Master; have role-card Stakeholders give a straw poll if the Product Owner wants one. The Product Owner makes the final call, with no search for consensus. Put only the chosen solution into section 3.1.

**出处与依据**：作者（把握：中）；种类：规矩
- commit b49278d feat(PBI-28)：设计日志约定 v1与模板，「Choosing is the key step」一条首次出现（-S 查到的最早提交）

**建议**：改；去处：清单（一行）

**理由**：PO 拍板、不求共识，且由 Scrum Master 主持（书里的 Facilitator）；PO 想要时由角色卡 Stakeholder 做一次非约束性的 straw poll。步骤细节归 steps/3-3-decide.md，「只把选中方案写进 3.1」归 design-backlog-template.md:46，但主持人与 straw poll 这两条要留在清单一行。

**新行**

```text
- **choose-with-po** [po,sm] The Scrum Master leads the choice and the PO decides, no consensus hunt; a role-card straw poll only if the PO asks.
```

**备注**：Only the chosen solution goes into 3.1 (the template has it).

---

### design-log#14 · Combine or rumble

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 55–55 行

**旧规矩原文**

> 14. **Combine or rumble** — Combine winners that fit together; when two conflict, prototype both and let the test decide (`steps/3-4-rumble.md`). The Product Owner decides which.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 664bf46 精简四份约定（design-log 条文已是现在的写法，合并或 Rumble 的分岔由 PO 定）
- source plugins/ideo-scrum/skills/design-kernel/steps/3-4-rumble.md：「Sometimes, there are many winners, but they all fit together.」（书中 Rumble 一节的做法，本条是约定化的改写，非逐字）

**建议**：留；去处：清单（一行）

**理由**：留：合并还是 Rumble 是设计里的分岔，PO 定；删了这一条，Ideate 收尾就没有对战规则。条文是书的改写，不算原文。

**新行**

```text
- **combine-or-rumble** Combine winners that fit; when two conflict, prototype both and let the test decide; the PO decides which.
```

---

### design-log#15 · Storyboard

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 56–56 行

**旧规矩原文**

> 15. **Storyboard** — Write a storyboard of about fifteen steps in section 3.2 (`steps/3-5-storyboard.md`) only when the solution needs one before the prototype; the Designer writes it.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 7e3e5b6 feat(PBI-49): 设计这块的修订稿（分镜只在需要时写、由设计者写，为该次定稿）
- source plugins/ideo-scrum/skills/design-kernel/steps/3-5-storyboard.md：「about ten to fifteen panels, all tightly connected into one cohesive story」（书中分镜是十到十五格，约定取其中的十五步）

**建议**：留；去处：清单（一行）

**理由**：留：说清了何时写分镜、谁写、写多长，一行够用。与模板 3.2 的注释一致。

**新行**

```text
- **storyboard** Write a storyboard of about fifteen steps in 3.2 only when the solution needs one before the prototype; the Designer writes it.
```

---

### design-log#16 · Just enough prototype

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 60–61 行 · 标记：Supplement、Decide on the spot

**旧规矩原文**

> 16. **Just enough prototype** — *Supplement.* Build in the design folder, following the chosen solution, real enough for honest reactions (`steps/4-1-fake-it.md`): made quickly for learning, not for production, while the surface the tester sees appears real. Keep it as design evidence under convention 19; keeping it does not make it an Increment. Subagents can build the parts while one session stitches them together; do a trial run against the solution and the design questions before testing, and write what it found in chapter 5. List each part of the prototype in chapter 4 with the design question it tests.
>     *Decide on the spot:* how real the prototype must be when the product has no screen — a document, a service, a process; agree it with the Product Owner.

**出处与依据**：补充（把握：中）；种类：规矩
- commit 100f7d0 fix(PBI-29, PBI-34): 问专家前先画草图地图；「原型感」与「看起来要真」的调和（PO 定）
- memory S:/SeaPawn-Memory/memory/IDEO-Scrum/design-line-po-in-the-room.md：原型用静态故事板，PO 说原型「根本都不需要把那个网页做出来」；本条的“真到什么程度”要和 PO 当面定

**建议**：改；去处：清单（一行）

**理由**：清单留做法一句：在设计文件夹里按选定方案做、真到能引起诚实反应、为学得快不为上线；「没有屏幕时原型要多真」随本条进长文件，不要并进 #21（#21 计划删清单，门的 #26 不含此决定）；部件清单已在 design-backlog-template.md:58-60 的第4章表，trial run、子代理分件与缝合、设计证据不算 Increment 分别在 SKILL.md:25、模板:67 与保留的 #19（design-log.md:70），理由要写明。Supplement 标签保留。

**新**：只在长文件 `design-stages`，清单里由 `design-stages` 一行索引。

**备注**：Supplement. Build in the design folder from the chosen solution, real enough for honest reactions, made quickly for learning not production while the surface the tester sees appears real; keep it as design evidence, which does not make it an Increment; subagents can build parts while one session stitches; do a trial run against the solution and the design questions before testing and write what it found in chapter 5; list each part in chapter 4 with the design question it tests. Decide on the spot: how real the prototype must be when the product has no screen, agreed with the PO.

---

### design-log#17 · Role-card test

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 65–65 行

**旧规矩原文**

> 17. **Role-card test** — Test with role cards, each a fresh subagent given only its card, the prototype, and the tasks; the Product Owner tests too. The Designer runs the Five-Act Interview (`steps/5-2-interview.md`); a grid of reactions is working material; chapter 5 keeps who tested, what showed up, and the answer to each design question. The book tests five customers; here, test with the role cards the prototype is about — those who would meet it — and leave out the rest, and add runs while the patterns are unclear. When the thing is for the Product Owner alone, the Product Owner testing it is enough: do not make up a role card.

**出处与依据**：作者（把握：中）；种类：规矩
- commit b49278d feat(PBI-28): 设计日志约定 v1 与模板（角色卡测试首次成文）
- source plugins/ideo-scrum/skills/design-kernel/steps/5-1-small-data.md：「Is talking to just five customers worthwhile?」（书测五个顾客，本条按角色卡改写）

**建议**：改；去处：清单（一行）

**理由**：改：测试对象、取舍、只有 PO 时的例外、五个顾客的对照混在一条里。清单留「用角色卡测，每张是新子代理，只给卡、原型和任务」一句；其余（五个顾客的对照、增加轮数、只有 PO 时的例外）移到长文件或模板注释。

**新**：只在长文件 `design-stages`，清单里由 `design-stages` 一行索引。

**备注**：Test with role cards, each a fresh subagent given only its card, the prototype and the tasks; the PO tests too; the Designer runs the Five-Act Interview; a grid of reactions is working material; chapter 5 keeps who tested, what showed up, and the answer to each design question; test with the role cards the prototype is about, add runs while patterns are unclear (the book tests five customers); when the thing is for the PO alone, the PO testing it is enough and no role card is made up.

---

### design-log#18 · Write the criteria before the test

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 66–66 行

**旧规矩原文**

> 18. **Write the criteria before the test** — Before testing, write down in chapter 5 what would count as a yes, a no, or a not yet for each design question, and what role cards cannot show: they are subagents reading a card, not real people.

**出处与依据**：作者（把握：高）；种类：规矩
- commit 7e3e5b6 feat(PBI-49): 设计这块的修订稿（正文「测前写判据」为该次定稿）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：Master 对设计日志的提议第 5 条「测试前先写判据，写明角色卡测试的局限」，后定稿为 Write the criteria before the test

**建议**：留；去处：清单（一行）

**理由**：留：测前写判据、写明角色卡不能测什么，是设计测试的硬要求，一行可说清；删了就没有判定标准。

**新行**

```text
- **criteria-before-test** Before testing, write what counts as a yes, a no or a not yet for each design question, and what role cards cannot show.
```

---

### design-log#19 · When the design ends

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 70–70 行

**旧规矩原文**

> 19. **When the design ends** — End the design when the Product Owner decides its questions are answered, or stops it (conventions 21 and 26). Write the conclusions into the product log as `../scrum-kernel/conventions/product-log.md`, convention 2, says, and pass them to the Sprint that asked; for a blank page, pick the target (`steps/2-3-pick-a-target.md`), split it into items, and let the Product Owner order them. Mark the design concluded and awaiting archival in its existing `Now` line. Keep the log and all original design working material together until archival: prototypes, sketches and rejected options, demos, reviews, synthesis, and other material used in the design. From the relevant chapter, link to the originals or the folder that holds them; a summary or a commit ID alone is not enough. If a Sprint builds the conclusions, link from that Sprint to the prototype as a specification; do not leave its only copy in a Sprint working folder. Keep the material whether or not a Sprint will build the conclusions. It is design evidence, never an Increment. When the Product Owner explicitly permits the commit, merge, and branch cleanup, handle the branch as `../sprint-kernel/conventions/sprint-log.md`, convention 19, says: merge into its base (convention 4), then delete it; pushing and other outward actions require the Product Owner's explicit consent. A design has no Review or Retro of its own. After it ends, the first Sprint Review that can read its complete log and all original material in its own checkout archives them (sprint-log convention 17). A Review without that complete set leaves the design pending archival; it does not move material from another worktree. Hand off changed paths to any receiving Sprint, which updates its references only once it can read the originals at the new path in its own checkout. A usable old reference may remain while building, not as the closing check: when the design is already archived on the target base (`main`), in this checkout, or in an integration branch ready alongside it, before that receiving Sprint closes check its actual material references — including those in its log being archived — and the originals against that combined target state, rather than trusting an old link just because it still works in the current worktree; update broken links before closing. If the receiving Sprint closes while the design is still pending archival everywhere, keep the usable active reference, note the pending archival, and merge to `main`; the later archiving Review searches the whole project before its closing commit (sprint-log convention 19 step 1) so those archived Sprint references are updated too, and reports any unmerged branches still holding stale active paths to the Scrum Master. Do not close with broken material links or rewrite verbatim historical commitment snapshots. Next to the ending decision, leave a line or two on what the design taught about how to work, as input to the Retrospective of the Sprint that archives it, not as the Retro record itself.

**出处与依据**：作者（把握：中）；种类：规矩
- commit f495298 fix(PBI-49): 照 PO 的两点改设计这块（设计不做 Review 和 Retro，18 改成 When the design ends）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：「设计不做 Review 和 Retro」，PO 定「设计是整个 Scrum 工作里的子集，不单独收尾」

**建议**：改；去处：长文件

**理由**：改：一条约一千五百字，混了结束决定、产出去向、归档、git 许可、教训五件事。清单留一行：设计由 PO 决定结束，日志与原始材料由结束后第一个冲刺 Review 归档；细则（产品日志写法、分支处理、断链检查）移长文件。删了会丢归档的时点和材料不能丢的规矩，所以不删。

**与它重复或相邻**：sprint-log#17、sprint-log#19

**新行**（长文件 `design-ending`）

```text
- **design-ends** A design ends when the PO says its questions are answered or stops it; the next Review archives it. → long/design-ending.md
- **design-conclusions** At its end, write the conclusions into the product log and pass them to the Sprint that asked. → long/design-ending.md
```

**备注**：Long file: the whole of the old rule, word for word, with the convention numbers replaced by handles (blank page: pick the target and let the PO order the items; mark the design concluded and awaiting archival in its Now line; keep the log and all original working material together until archival and link to the originals, a summary or a commit ID alone is not enough; if a Sprint builds the conclusions link to the prototype as a specification, never leave its only copy in a Sprint folder; the material is design evidence, never an Increment; with the PO's explicit permission merge the design branch into its base and delete it, pushing needs consent; a design has no Review or Retro of its own, the first Review that can read its complete log and material in its own checkout archives it; and the rest of the rule, which the ledger holds in full).

---

### design-log#20 · IDEO in every stage

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 74–74 行

**旧规矩原文**

> 20. **IDEO in every stage** — Each stage of the design sprint stands on one IDEO mode: take the methodology from the mode the stage maps to, as `SKILL.md` requires. (The five modes are not the design sprint: `../ideo-kernel/conventions/ideo-log.md`, convention 2.)

**出处与依据**：作者（把握：高）；种类：规矩
- commit f495298 fix(PBI-49): 照 PO 的两点改设计这块（贯穿全程加 IDEO in every stage）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：design-log 与设计日志模板一条「IDEO in every stage」

**建议**：留；去处：清单（一行）

**理由**：留：每个阶段都要从一个 IDEO 模式取方法，是设计线的基本要求，一行。括号里的指路（五模式不是设计冲刺）保留，与 ideo-log#2 呼应。

**新行**

```text
- **ideo-in-every-stage** Each design stage takes its methods from the IDEO mode it stands on.
```

---

### design-log#21 · Ask the PO

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 75–75 行

**旧规矩原文**

> 21. **Ask the PO** — Ask the Product Owner whenever you are unsure (`../scrum-kernel/overview.md`, convention 10), and to settle each stage result and authorize entry or return, including how this round of Ideate will diverge (convention 26); set or change the design goal (convention 25); pick the How Might We questions that matter (convention 8); choose the solution and decide between combining and a rumble (conventions 13–14); agree how real the prototype must be (convention 16); decide that the design ends (convention 19); and explicitly permit git actions (commit, merge, branch deletion, push) before they run (conventions 19, 24, and 26).

**出处与依据**：作者（把握：中）；种类：规矩
- commit b49278d feat(PBI-28): 设计日志约定 v1 与模板（「Ask the PO whenever you are unsure」首次成文）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：阶段之间由 PO 决定的一段（PO 决定清单的来源）

**建议**：并 → overview#10；去处：不进 Memory

**理由**：Developer 改（Master 2026-11-22 要合并重叠）：并入 overview#10（ask-the-po），不再并入 sprint-log#25（它自己也并进 overview#10 了）。设计特有的几项（各阶段结果与进出、Ideate 怎么发散、设计目标、挑 How Might We 问题、选方案与合并/Rumble、原型要多真、设计结束、git 许可）随并入带进 roles-and-routing 长文件。

**与它重复或相邻**：design-log#14、design-log#16、design-log#19、design-log#26、overview#10

**新**：并入 `overview#10`。这条独有、要带过去的内容：Design decisions the PO makes: each stage result and entry or return (including how this round of Ideate will diverge), set or change the design goal, pick the How Might We questions that matter, choose the solution and decide between combining and a rumble, agree how real the prototype must be, decide that the design ends, and explicitly permit git actions (commit, merge, branch deletion, push) before they run.

---

### design-log#22 · Five chapters, not five days

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 76–76 行

**旧规矩原文**

> 22. **Five chapters, not five days** — Write one chapter per stage — Empathize, Define, Ideate, Prototype, Test — not the book's Monday to Friday, and no notes section. Each chapter records what its stage produced, not the steps taken.

**出处与依据**：作者（把握：高）；种类：格式
- commit 7e3e5b6 feat(PBI-49): 设计这块的修订稿（设计日志五章即五个阶段）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：「设计日志同理，五章就是五个阶段」

**建议**：删；去处：不进 Memory

**理由**：删：章节结构是模板的事，模板已有五章，并在第 8 行写明只记产出、不记步骤，本条与之重复。删了不丢内容；Memory 里不需要格式规定。

**新**：不进清单。去处或不要的理由：plugins/ideo-scrum/skills/design-kernel/conventions/design-backlog-template.md has the five chapters, one per stage, and says each records what its stage produced, not the steps taken (line 8).

---

### design-log#23 · Renamed terms

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 77–77 行

**旧规矩原文**

> 23. **Renamed terms** — See the first paragraph of `SKILL.md`.

**出处与依据**：作者（把握：高）；种类：说明
- commit b49278d feat(PBI-28): 设计日志约定 v1 与模板（术语改名首次成文）
- archive plugins/ideo-scrum/skills/design-kernel/SKILL.md 开头第一段：书的 long-term goal、sprint questions、Decider、Facilitator 分别改称 design goal、design questions、Product Owner、Scrum Master

**建议**：删；去处：不进 Memory

**理由**：删：纯指路（「见 SKILL.md 第一段」），术语对照已在 SKILL.md 开头写明；删了不丢内容，读 design-kernel 时自然会读到。

**新**：不进清单。去处或不要的理由：plugins/ideo-scrum/skills/design-kernel/SKILL.md, first paragraph, lists the renamed terms.

---

### design-log#24 · Resume from the header

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 78–78 行

**旧规矩原文**

> 24. **Resume from the header** — Keep `> Now:` in the header with the stage and next step, followed immediately by `> Waiting for PO:` with each pending decision's number and short question, separated by semicolons, or `None`. Update both with the log change that causes them; a session that picks up the design reads them first, then checks the recorded permission for its stage and scope (convention 26) and any recorded git permission (convention 21). Neither `Now` nor permission to enter or resume a stage authorizes committing, merging, or pushing by itself. Before a session ends or its context is shortened, write the half-finished work into the chapter it belongs to and update the header. Commit within the authorized scope only if the Product Owner explicitly recorded commit permission for it; otherwise keep the uncommitted changes and record that status and where to resume.

**出处与依据**：作者（把握：中）；种类：规矩
- commit ccd8257 feat(PBI-37): 设计日志开设计与接手（Now 一行、Resume from the header 首次成文）
- archive plugins/ideo-scrum/skills/design-kernel/conventions/design-backlog-template.md 第 4 行：> Now 行与等待 PO 行的格式

**建议**：并 → sprint-log#22；去处：不进 Memory

**理由**：Developer 改：并入 sprint-log#22（log-is-the-handoff）：冲刺日志、设计日志、IDEO 日志的头部与交接是同一件事。设计特有的（断线前把半成品写进所属章；Now 与阶段许可都不单独授权提交、合并、推送；只在 PO 明确记录提交许可时才提交，否则保留未提交并记下状态与续做点）并进交接长文件；核验指出这些别处没有，所以不能只说「归模板」。

**与它重复或相邻**：design-log#26

**新**：并入 `sprint-log#22`。这条独有、要带过去的内容：In a design, write the half-finished work into the chapter it belongs to and update the header before a session ends or its context is shortened; Now and permission to enter or resume a stage do not by themselves authorize committing, merging or pushing; commit only if the PO explicitly recorded commit permission for it, otherwise keep the changes uncommitted and record the status and where to resume.

---

### design-log#25 · Goal fixed, plan flexible

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 79–79 行

**旧规矩原文**

> 25. **Goal fixed, plan flexible** — Sharpen the design goal during Empathize; once it is set, only the Product Owner changes it. The questions, the map, and the solution may change with what the work shows; write what changed and why in the chapter it belongs to (`../scrum-kernel/overview.md`, convention 17).

**出处与依据**：作者（把握：高）；种类：规矩
- commit 9c9bd67 feat(PBI-39): scrum-kernel 约定总览 overview.md（目标不变其余可调）

**建议**：并 → overview#17；去处：不进 Memory

**理由**：并进 overview#17，但 overview#17（overview.md:103-105）现文只有通用句，必须把设计特有的「Empathize 中精化设计目标」和「变动写进所属章」两句一并补进它的长文件，否则会丢；overview#17 自身是改/长文件、不并出，无环。

**与它重复或相邻**：overview#17

**新**：并入 `overview#17`。这条独有、要带过去的内容：Sharpen the design goal during Empathize; once it is set, only the PO changes it. The questions, the map and the solution may change with what the work shows; write what changed and why in the chapter it belongs to.

---

### design-log#26 · Gates between stages

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 80–90 行

**旧规矩原文**

> 26. **Gates between stages** — Wait for explicit permission to enter or return as `../scrum-kernel/overview.md`, *Product Owner decides between stages*, says. Record permission to start Empathize when opening; if there is no design goal yet, do not record a placeholder as a commitment. Stage entry or return permission covers only that stage's design work and does not by itself authorize a commit, merge, or push; if git actions are permitted, record how far that permission reaches (for example, commit on the design branch; merge at ending decided separately; no push) on the stage or ending decision line. Before starting Ideate, the Product Owner settles how this round will diverge. Until that and entry are clear, do not gather ideas for the round, diverge, sketch, or delegate those tasks. Record the arrangement in chapter 3 before the solution section. Choosing a solution is not permission for Prototype, and a trial run is not permission for design Test. When the stage first sets a design goal, put its exact text in the §1.2 table. Before recording that decision and before each later stage decision, read the exact design goal from the table — and the Product Goal when product direction is at issue — then check the work against it and the table below. If the required text cannot be read, stop at that gate. Keep the exact wording on the dated decision line as a record of the goal at the time. Show the text to the Product Owner only when the goal has changed, when product direction is at issue, or when they ask. When a stage shows an earlier answer was wrong, report it and wait for permission to return; after Test the Product Owner decides whether to end the design or authorizes the return.
>
>     | Stage | The log holds | The check |
>     | --- | --- | --- |
>     | Empathize | the challenge, the design goal, and the design questions, with the source of each finding | The findings come from the people concerned — what they did, what they said, where the two differ — not from a pile of facts |
>     | Define | the map and the How Might We questions the Product Owner picked | The How Might We questions were written against the map and the challenge, the goal, and the questions of chapter 1 |
>     | Ideate | the chosen solution, and the storyboard if one was written | Whoever sketched diverged before converging, and when several sketches were drawn, they differ in approach, not only in detail |
>     | Prototype | the parts of the prototype, each with the design question it tests | It is rough and quick: built to learn, not to deliver |
>     | Test | the criteria written beforehand, what the trial run found, who tested and what showed up, and an answer to each design question with where it flows back | The answers come from real reactions, and "we were wrong" counts as an answer |
>
>     At each gate ask: would someone who never learned design have produced the same thing? If so, the stage missed its focus.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 7e3e5b6 feat(PBI-49): 设计这块的修订稿（阶段之间的门、测完由 PO 决定、测前与测后的判据，为该次定稿）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：第 37 行「阶段之间由 PO 决定」；第 118 行 2026-11-10「PO 新定（Master 转述）」

**建议**：改；去处：长文件

**理由**：改：条文约一千五百字加一张四行表，是本设计最关键的门，留。但清单只留一行：阶段之间等 PO 明确许可，许可只覆盖该阶段的设计工作，不含提交、合并、推送；表与「读设计目标」的细则移长文件。删了会丢门的标准，不删。

**与它重复或相邻**：design-log#21、design-log#24

**新行**（长文件 `stage-gates`）

```text
- **ideate-arrangement** Before Ideate, the PO settles how the round diverges; until then no gathering, sketching or delegating. → long/stage-gates.md
```

**备注**：The old first line design-gates (a stage permission covers only that stage's design work, not a commit, merge or push) is folded into outward-needs-po and the stage-gates long file. Long file: the four-row table (what the log holds and the check at each stage) word for word, and 'would someone who never learned design have produced the same thing?'; record permission to start Empathize when opening and no placeholder goal as a commitment; record how far git permission reaches on the stage or ending decision line; record the Ideate arrangement in chapter 3 before the solution section; choosing a solution is not permission for Prototype and a trial run is not permission for Test; the goal's exact text goes in the 1.2 table and is read before each stage decision (the Product Goal too if direction is at issue), stop if it cannot be read, the wording on the dated decision line is a record not a source, show it to the PO only when the goal changed, direction is at issue or they ask; when a stage shows an earlier answer was wrong, report it and wait for permission to return; after Test the PO decides whether to end the design or return.

---

### design-log#27 · A small design is still a design

`plugins/ideo-scrum/skills/design-kernel/conventions/design-log.md` 第 91–91 行

**旧规矩原文**

> 27. **A small design is still a design** — Whether a question opens a design at all is settled by `../ideo-kernel/conventions/ideo-log.md`, convention 1. When the Product Owner opens a design that is small — about one session of work — still keep the log, shrink each stage to a line or two, and still keep the stage decisions and permissions under convention 26. Skip no stage, least of all Empathize and divergence (convention 10).

**出处与依据**：作者（把握：高）；种类：规矩
- commit 7e3e5b6 feat(PBI-49): 设计这块的修订稿（正文「小设计」为该次定稿，条内「不跳阶段」由 PO 定）
- archive scrum/documents/sprint/sprint-14-conventions-tuning.md：Master 对设计日志的提议第 4 条「小设计」，后并入约定

**建议**：留；去处：清单（一行）

**理由**：留：小设计也要留日志、不跳阶段、保留门上的许可，防止小设计被当成随手做。与 ideo-log#1 的分界是指路，不重复。

**新行**

```text
- **small-design** A small design is still a design: keep the log, shrink each stage to a line or two, skip no stage, keep the stage permissions.
```

---

## 非编号块（引言、署名、图、表）

### design-log@1 · quote（第 3–3 行）

> > Working conventions: reference, not law — follow what fits, override what doesn't, note why. Source labels and the rest: `../scrum-kernel/overview.md`, convention 15. A convention with no label is the author's practice.

**新**：不进清单。去处或不要的理由：The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes.

---

### design-log@2 · paragraph（第 5–5 行）

> The design log template is `design-backlog-template.md` in this folder. Paths here are relative to the design-kernel skill folder; the stages, the book's excerpts, and the methods are listed in this skill's `SKILL.md`. Where an excerpt describes the book's room — whiteboards, sticky notes, dot voting, a team at a table — these conventions say how a solo + AI team does that step, and they apply.

**新**：不进清单。去处或不要的理由：The first section of long/design-stages.md: the template, and where the book describes its room (whiteboards, sticky notes, dot voting, a team at a table) these rules say how a solo + AI team does that step.

---

### design-log@3 · fence:mermaid（第 7–17 行）

> ```mermaid
> flowchart TD
>     A["Opening<br/>conventions 1–5"] -- "PO authorizes Empathize" --> B["Empathize<br/>conventions 6–7"]
>     B -- "PO authorizes Define" --> C["Define<br/>convention 8"]
>     C -- "PO settles how to diverge and authorizes Ideate" --> D["Ideate: diverge<br/>conventions 9–10"]
>     D --> E["Ideate: converge<br/>conventions 11–15"]
>     E -- "PO chooses; separately authorizes Prototype" --> F["Prototype<br/>convention 16"]
>     F -- "PO authorizes Test" --> G["Test<br/>conventions 17–18"]
>     G -- "PO decides" --> H["Ending<br/>convention 19"]
>     G -. "PO authorizes a return" .-> R["Resume the stage that needs work<br/>convention 26"]
> ```

**新**：不进清单。去处或不要的理由：Drawn in long/flow-maps.md, with the handles in the boxes; the list line flow-maps points there.

---

### design-log@4 · paragraph（第 19–19 行）

> **The three loops.** Empathize and Define: the Product Owner and the Scrum Master settle the research and definition together; the Scrum Master records it, and the Designer takes over when Ideate is authorized (convention 3). Diverge and converge: the Product Owner first settles how to open up ideas; the AI can do the work, and a person picks the solution. Prototype and Test: the AI can do the work once each stage is authorized. Any stage decision handed to the Scrum Master still has to be within the written handover and recorded (`../scrum-kernel/overview.md`, convention 12).

**新**：不进清单。去处或不要的理由：The section The three loops of long/design-stages.md, word for word.

---

### design-log@5 · paragraph（第 21–21 行）

> Conventions 20–27 hold at every step; see Throughout, below. Apply the entry and return rules in convention 26 at each transition.

**新**：不进清单。去处或不要的理由：Dropped: a pointer to 'Throughout'; the entry and return rules at each transition are the stage-gates line and long/stage-gates.md.

---

### design-log@6 · paragraph（第 33–33 行）

> The conventions under Stages cover only what differs from the book or adds what it leaves out; for everything else, follow the excerpts.

**新**：不进清单。去处或不要的理由：The first section of long/design-stages.md: these rules cover only what differs from the book or adds what it leaves out; for the rest follow the book's excerpts.

---
