# Design Backlog — feedback-loop

> Opened 2026-11-11 | From: PBI-55（PO 2026-11-11 口述：用插件时冒出很多想法，很快就忘掉；想要一个自我反馈机制，产品才能越来越适合自己） | Branch: design-feedback-loop（从 main 开） | Product Owner: SeaPawn | Designer: IDEO # [master]-[main]-[研究反馈机制]（主对话，兼 Scrum Master；PO 2026-11-11 定）；辅助：IDEO # [designer]-[main]-[辅助设计]（Stakeholder 身份：落盘、发散、原型、测试） | Scrum Master: IDEO # [master]-[main]-[研究反馈机制]
> Now: Test — 判定标准已写，辅助会话跑 33 次测试
> Ends when the design questions are answered or the Product Owner stops the design (convention 18 in `design-log.md`); the first Sprint Review after that archives this file (convention 17 in `sprint-log.md`, in the scrum-kernel skill's `conventions/` folder).
> Methods: 各阶段的原文见 design-kernel skill；每个阶段同时用 ideo-kernel 的 IDEO 模式与方法（design-kernel `SKILL.md` 的要求）。
> This log records what each stage produced, not every step taken to get there (convention 21).
> How to write this log: `design-log.md` in the design-kernel skill's `conventions/` folder.

## 1. 共情（Empathize）

### 1.1 挑战

PO 用自己做的产品时，随时会冒出改进的点，而且很多（访谈 一-3，一手）。他想到就立刻交给手边正在干活的 AI 记下来，不会等（访谈 二-1，一手），等更新产品时再看（访谈 三-3，一手）。他说「很快就忘掉」，可他实际是想到就交出去，所以会忘的只是没交出去的那些；卡住的是交出去的这一步（访谈 一-3 与 二-1 对照，Master 的判断）：每一次都要用语音说出记到哪里，路线长、别扭，而且常常这样（访谈 二-4、三-2，一手）。语音还会把名字认错：本次对话里，IDEO-Scrum 被识别成「Ido Scrum」，main 成了「MNN」，Designer 成了「desire」（Master 观察 PO 的语音输入，一手）。

记在哪里不限，不一定在产品的仓库里，更新产品时能一起拿出来就行（访谈 三-5，PO 的判断）。现在的办法能用，PO 也觉得不坏，但他想要更优雅的办法，不想顺着现在的做法改（访谈 二-4、三-4，一手）。哪个产品不重要：他做的任何产品都需要这样的自我反馈（访谈 三-1；开设计时的口述，一手）。

为什么是现在：插件就是靠这些点一轮轮改进的，PBI-47～50 都是这样来的（产品日志，二手）；点越多，这一步走得越勤。

### 1.2 设计目标

我做的每一个产品，都照我自己用它时的想法一轮轮改进，越来越适合我。

（PO 2026-11-11 定。出处：开设计时的口述「越来越适合自己」、访谈 三-1。原稿写成了怎么做，修正记录见 `scrum/documents/design-goal-vision.md`。）

### 1.3 设计问题

1. 不说位置时，手边的 AI 记下的每一个点，更新那个产品时都找得回来吗？（访谈 二-4、三-1、三-5）
2. 交出一个点，能不能一句话就完，不打断手上的活？（访谈 二-1）
3. PO 记完不回头查，记下的东西靠得住吗？内容够不够让后来的人看懂？（访谈 二-2）
4. 更新产品时，攒下的点能不能找全、读得懂，直接拿来定要改什么？（访谈 一-4、三-3）
5. 换成别的产品，同一个办法照样能用吗？（访谈 三-1）
6. 记下的点在产品改之前，会话里能不能马上照着做？（PO 2026-11-11 确认方案时提出：点要马上用起来，用着才知道对不对）

PO 2026-11-11：第 1 章定；设计目标改写成愿景；不找专家、不另做研究（Master 建议，PO 同意），进 Define。

## 2. 定义（Define）

### 2.1 地图

```mermaid
flowchart TD
    PO(["PO"]) --> Use["用自己的产品，冒出一个点"]
    AI(["手边的 AI"]) --- Note
    Use --> Hand["用语音交给手边的 AI，说清记到哪里"]
    Hand --> Note["AI 记下"]
    Note --> Keep["攒着"]
    Keep --> Update["更新产品时拿出来用"]
    Update --> Better(["产品改进，越来越适合 PO"])
    Better -. "下一次用" .-> Use
```

（只画现在发生什么：五六个框、一个环；做法照 `scrum/documents/design-map-rough.md`。）

### 2.2 How Might We

- **交出去**：★① HMW 让交出一个点，和随口说一句话一样轻？★② HMW 让 PO 根本不用说记到哪里？③ HMW 让说错、听错的名字也不碍事？④ HMW 让交出去这一步不打断手上的活？★⑤ HMW 让没说出口的点也不白想？
- **记下和攒着**：★⑥ HMW 让 PO 记完不查也放心？⑦ HMW 让一个点隔了一周再看也看得懂？⑧ HMW 让每个产品都有地方攒它的点？
- **更新时**：★⑨ HMW 让更新产品时，攒下的点一次拿全？⑩ HMW 让攒下的点拿来就能定要改什么？
- **环**：⑪ HMW 让 PO 看得到哪个点已经变成了改进？

PO 2026-11-11：地图定；How Might We 由 Master 代挑（PO 授权）：①②⑤⑥⑨，①② 是现在卡住的地方，⑤ 对应 PO 最初说的「AI 自动记」，⑥ 因为 PO 记完不查，⑨ 因为记录在更新产品时才用；进 Ideate。

## 3. 构思（Ideate）

### 3.1 方案

**记一下就够：全局说明管路线，反馈进全局记忆**

（PO 2026-11-11 定。底子是 PO 的方案 E；从 A–D 拿了别名表、一行回执、待认领、盘点四个点子；会话矿工（B、F）留作以后。A–D 同属一路——中央收件箱、事后归属——E 和 F 补上了不同的两路（design-log 第 25 条的关卡）。草图见 `sketches.md`。）

1. **一次搭好**：SEAPAWN.md 加一节「Feedback」，写明下面几条，附一张产品表：正式名、文件夹名、语音别名和常见的误识别（如 IDEO-Scrum ←「Ido Scrum」）。全局记忆的 MEMORY.md 末尾加一节「Feedback」：普通条目照旧在前面，反馈一行一条放在这一节；每条的文件放 `GlobalMemory/feedback/<产品>/`，拿不准是哪个产品的放 `feedback/待认领/`。
2. **交出去**：PO 说「记一下：……」，不说位置。
3. **记下**：手边的 AI 照产品表判断是哪个产品，不拿当前项目当默认；拿不准就放待认领，不硬猜；是做事的规矩、不是产品反馈的，照普通记忆写。一个点一个文件：日期、在哪个项目的会话里、原话、当时在做什么、它理解的意思；Feedback 一节加一行。已经有的点不重复记，把新的原话补进原来的文件。回一行「记下了 · IDEO-Scrum · 可改」，不追问，回到手上的活。
4. **马上用起来**：Feedback 一节每个会话都加载，产品还没改，AI 就照着做；用着用着，PO 才知道这个点对不对。
5. **更新时拿出来**：开始更新一个产品时（精化产品日志、开冲刺之前），那个产品的会话先读它的 Feedback 行和待认领，按主题列给 PO；PO 定下要做的进产品日志；处理过的点删掉那一行和文件，git 留着。

取舍（PO 定）：放进全局记忆，会多占每个会话的上下文；换来的是点能马上用、用着验证，回路才闭得上。每周更新时处理掉，就不会越积越多。

PO 2026-11-11：方案定为 3.1——反馈进全局记忆（MEMORY.md 加 Feedback 一节，文件放 GlobalMemory/feedback/<产品>/），为的是点能马上用、用着验证；原型和测试交给辅助会话自动做，中间不用 PO 参与，最后把结果给 PO；进 Prototype。（上一版这一行写着「进 Prototype」，没经 PO 确认，Master 越过了关卡，已改。）

### 3.2 故事板（可选）

## 4. 原型（Prototype）

| 部件 | 检验哪个设计问题 | 在哪 |
| --- | --- | --- |
| 「Feedback」一节的草稿，含产品表 | 1、2、3、5、6 | 设计文件夹 `prototype/feedback-section.md` |
| 测试用的全局记忆（Feedback 一节和五个种子） | 4、6 | 测试时建在系统临时目录；说明见 `prototype/sandbox.md` |
| 十一个测试场景 | 1–6 | `prototype/cases.md` |

原型只在测试里用：草稿和测试用的全局记忆通过临时项目的 CLAUDE.md 加载，路径换成系统临时目录；真的 SEAPAWN.md 和 S:\SeaPawn-Memory 不动（design-log 第 15 条）。

Master 2026-11-11（PO 说原型和测试交给辅助会话自动做，中间不参与）：原型定；进 Test。

## 5. 测试（Test）
