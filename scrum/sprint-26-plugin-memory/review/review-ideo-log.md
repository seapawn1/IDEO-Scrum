# 审阅：ideo-log.md（ideo-kernel）

每条旧规矩一节：先是原文（逐字），再是出处与依据、核验后的建议与理由，最后是它现在的样子（清单里的一行，或并到哪、删在哪）。
读法：只看「旧规矩原文」和「新行」两块就能审；出处、理由是我和核验员写的依据，供你判断「留不留、改得对不对」。

本文件 4 条：改 3、留 1；另有 3 个非编号块（文末）。

---

### ideo-log#1 · Design sprint or the five modes

`plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md` 第 22–22 行

**旧规矩原文**

> 1. **Design sprint or the five modes** — The Product Owner says which one a question gets. When they do not, the default split is: open a design sprint when a prototype must be tested with role cards before anyone dares to act; otherwise use the five modes; convention 3 says how to record them. When a chat turns up something to research, it can count as empathize material; if it calls for a design sprint, wait for the Product Owner’s permission to start Empathize, then still run that stage (`../design-kernel/conventions/design-log.md`, convention 26).

**出处与依据**：作者（把握：中）；种类：规矩
- commit 8e6dc95 docs(Sprint 17): 第 3 项——设计侧全文审阅稿与问题清单；记测试通道备忘（分界句首次出现，在 drafts/ 下的 design-sprint-or-five-modes.md）
- archive scrum/documents/sprint/sprint-17-conventions-rewrite.md：PBI-56 的分界（PO 指定；PO 没指定时，要先做原型、拿角色卡测过才敢动手的开设计冲刺，其余用五模式）

**建议**：改；去处：清单（一行）

**理由**：原句末「聊天里查到的东西可算 Empathize 素材」没有去处：design-kernel 的 design-log.md 第 1 条（第 25 行）与第 26 条（第 80 行）只写「PO 授权后才开 Empathize」，没有这句；全仓只在 ideo-log.md 第 22、26 行。改写成一行时把「聊到要研究的东西可算 Empathize 素材」留下。

**新行**

```text
- **sprint-or-modes** The PO picks a design sprint or the five modes; default to a design sprint only if a prototype must be tested with role cards.
```

**备注**：The tail 'a chat's research can count as Empathize material' is in research-as-empathize (drafted under ideo-log#2, which carries the same sentence); 'then still run that stage' (do not skip Empathize) is in open-a-design.

---

### ideo-log#2 · The five modes and the design sprint

`plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md` 第 26–26 行 · 标记：quote

**旧规矩原文**

> 2. **The five modes and the design sprint** — They share five names and are two different things. The five modes are modes, not stages: no fixed order, you can go back and forth, and they are the plugin's base and shared toolbox. The design sprint's five stages each stand on one mode, and add the book's steps, a Product Owner decision between stages, and a prototype tested with role cards — a heavy research module beside the Sprint. What a user calls "the IDEO five-stage method" is the five modes themselves, not the design sprint. Do not mix them: an IDEO log does not run the design sprint's steps (no map, Lightning Demos, or storyboard), and a design sprint does not open an IDEO log — its own log already has five chapters. If an IDEO log shows that a prototype must be tested with role cards before anyone dares to act, the IDEO log can count as empathize material. Start the design sprint with Empathize only once authorized (convention 1 above).

**出处与依据**：PO 原话（把握：中）；种类：规矩
- po scrum/documents/sprint/sprint-17-conventions-rewrite.md：「所以要注意区分，是ideo方法论还是design sprint」
- commit 3d823bd docs(Sprint 17): 补 IDEO 日志与模板——ideo-log 四条、IdeoBacklog 模板；分界改名与 8 处指向；架构图与关系条；Codex 同步（首次写成本条）

**建议**：改；去处：清单（一行）

**理由**：一行里要留下原句「IDEO 日志可算 Empathize 素材」（全仓只在 ideo-log.md 第 22、26 行），并保留「no map, Lightning Demos, storyboard」这三个具体步骤名（只在第 26 行）。设计冲刺的阶段描述（各阶段立在一个模式上、书里的步骤、阶段间 PO 决定、角色卡测试）在 design-kernel/SKILL.md 第 3 行已有，可以删。

**新行**

```text
- **modes-are-not-the-sprint** Keep modes and sprint apart: an IDEO log runs no map, Lightning Demos or storyboard; a design sprint opens no IDEO log.
- **research-as-empathize** Chat or IDEO-log research can count as Empathize material, but a design sprint still starts on the PO's permission.
```

**别处已有**：What the five modes and the design sprint's stages are (stages stand on modes, the book's steps, a PO decision between stages, role-card tests) is in plugins/ideo-scrum/skills/design-kernel/SKILL.md and plugins/ideo-scrum/skills/ideo-kernel/SKILL.md.

**备注**：The annotation asked to keep 'IDEO log counts as Empathize material' and 'no map, Lightning Demos, storyboard'; both are kept. The old 'Do not mix them' lost its referent once the line stands alone, so the line now says what is kept apart.

---

### ideo-log#3 · When to open an IDEO log

`plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md` 第 30–30 行

**旧规矩原文**

> 3. **When to open an IDEO log** — Use one or two methods when that is enough; their output goes into the log they serve — a Sprint's Increment notes, the product log's Notes. When the five modes make a run of their own — more than one or two methods, or more than one session — open an IDEO log: `scrum/ideo-<suffix>/IdeoBacklog.md`, five chapters, one per mode, with no Product Owner gate between them (how this differs from a design sprint: convention 2). Each chapter holds what that mode produced, not every step taken. Before a mode, read its file in `IDEO-modes/`; before a method, read the method's file, as this skill's Use Protocol says.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 3d823bd docs(Sprint 17): 补 IDEO 日志与模板——ideo-log 四条、IdeoBacklog 模板；分界改名与 8 处指向；架构图与关系条；Codex 同步（首次写成本条）
- po scrum/documents/sprint/sprint-17-conventions-rewrite.md：「标准得五节，没有什么拆分」
- archive scrum/documents/sprint/sprint-17-conventions-rewrite.md：IDEO 日志并入 PBI-56（Master 定：五章一模式一章，模式之间没有 PO 关卡，可以来回走）

**建议**：留；去处：清单（一行）

**理由**：PO 要的「标准五节」与这条一致，开日志的规矩要留。「一两个方法就够、多于一两个或多于一次会话才开」的门槛是作者定的，PO 可再定。写法已够短；指向 IDEO-modes/ 与 convention 2 的尾巴保留。

**新行**

```text
- **open-ideo-log** One or two methods write into the log they serve; a longer run gets scrum/ideo-<suffix>/IdeoBacklog.md, five chapters, no PO gate.
- **read-mode-file** Read a mode's or method's file in the ideo-kernel before using it; a chapter holds what its mode produced.
```

**备注**：The threshold (one or two methods, or one session) is the author's; the PO may set it again.

---

### ideo-log#4 · Where it lives and how it ends

`plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-log.md` 第 31–31 行

**旧规矩原文**

> 4. **Where it lives and how it ends** — The log, the prototypes, and the working material live in `scrum/ideo-<suffix>/`. It has no commitment of its own: For holds the relative path to the product log or sprint log it serves, where the commitment is kept. Keep `> Now:` on its own header line with the current mode and next step, followed by `> Waiting for PO:` with the number and short question of each pending decision, separated by semicolons, or `None`. Update both with the log change that causes them; this adds no gate between modes. The conclusions flow back to the log that asked for it — the product log or the sprint log — and the Product Owner decides what changes. When the work is done, keep the log: the first Sprint Review after that archives it (`../sprint-kernel/conventions/sprint-log.md`, convention 17). A prototype whose conclusions will be built goes to the Sprint that builds them, as that Sprint’s specification. If that Sprint is not open yet, keep the prototype in the IDEO folder until handoff. Any other standalone IDEO prototype is deleted when the work is done.

**出处与依据**：作者（把握：中）；种类：规矩
- commit 1e347b4 feat(Sprint 18): H2 交付 PBI-66 日志读取接口、目标引用与工作块完成标记（Now 与 Waiting for PO 行进入 ideo-log）
- archive scrum/documents/sprint/sprint-18-rules-first.md：日志头部（PBI-66）——冲刺、设计、IDEO 三种日志头部有 Now 与 Waiting for PO
- commit 9734304 docs(Sprint 23): H10 落源 18 份已审稿（「原型的去留」两句与归档句落入本条）

**建议**：改；去处：长文件

**理由**：格式写法不在 overview（scrum-kernel/overview.md 第 61、104 行都没有 Now/Waiting 格式），在 ideo-backlog-template.md 第 4-5 行，删格式细节安全；归档句已由 sprint-log.md 第 71 行第 17 条覆盖（不必写成「并入」）。原条「结论流回、PO 决定改什么」与「原型作建它的 Sprint 的规格、未开则留在 IDEO 文件夹到交接」只在 ideo-log.md 第 31 行，SKILL.md 还把原型交接指回本条，必须收进长文件；本条细则多，home 改为长文件。

**与它重复或相邻**：sprint-log#17

**新行**（长文件 `ideo-ending`）

```text
- **ideo-log-home** An IDEO log lives in scrum/ideo-<suffix>/ with its prototypes; it has no commitment, its For cell names the log it serves.
- **ideo-log-ends** Conclusions flow back to the log that asked and the PO decides; archive at the next Review. → long/ideo-ending.md
```

**别处已有**：The Now and Waiting for PO header format is in plugins/ideo-scrum/skills/ideo-kernel/conventions/ideo-backlog-template.md (lines 4-5); the archiving of an IDEO log is also in sprint-log#17 (the Review rule).

**备注**：Long file keeps the prototype handoff word for word: a prototype whose conclusions will be built goes to the Sprint that builds them, as that Sprint's specification; if that Sprint is not open yet it stays in the IDEO folder until the handoff; any other standalone IDEO prototype is deleted when the work is done. ideo-kernel's SKILL.md points back to this rule.

---

## 非编号块（引言、署名、图、表）

### ideo-log@1 · quote（第 3–3 行）

> > Working conventions: reference, not law — follow what fits, override what doesn't, note why. Source labels and the rest: `../scrum-kernel/overview.md`, convention 15. A convention with no label is the author's practice.

**新**：不进清单。去处或不要的理由：The MEMORY.md header carries it: working conventions, follow what fits, override what doesn't, say why in the log's notes.

---

### ideo-log@2 · paragraph（第 5–5 行）

> Paths here are relative to the ideo-kernel skill folder. The five modes and the method catalog are this skill's; the design sprint is the design-kernel skill's.

**新**：不进清单。去处或不要的理由：Dropped: the paths are relative to the skill folders; which kernel owns what is in the SKILL.md files.

---

### ideo-log@3 · fence:mermaid（第 7–18 行）

> ```mermaid
> flowchart TD
>     Q["A question comes up"] --> P{"Design sprint or the five modes?<br/>(convention 1)"}
>     P -- "a design sprint" --> DS["Design sprint:<br/>five stages, each standing on one mode<br/>(design-kernel, DesignBacklog.md)"]
>     P -- "the five modes" --> FM["The five modes"]
>     FM --> SEQ["A run of its own:<br/>an IDEO log<br/>(IdeoBacklog.md, five chapters, no gates)"]
>     FM --> SPOT["One or two methods,<br/>recorded in the log they serve"]
>     DS --> R["Conclusions flow back to<br/>the log that asked"]
>     SEQ --> R
>     SPOT --> R
>     SEQ -. "a prototype must be tested<br/>with role cards first" .-> DS
> ```

**新**：不进清单。去处或不要的理由：Drawn in long/flow-maps.md, with the handles in the boxes; the list line flow-maps points there.

---
