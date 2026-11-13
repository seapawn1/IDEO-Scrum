# Design Backlog — board

> Opened 2026-11-14 | From: PBI-68 看板改版——Sprint 20（`sprint-20-presentable`）的 68 等本设计的原型交接，再做 68-b；同日先开过一条设计线，PO 叫停、日志已删，这是重开 | Branch: `worktree-design-board`（PO 建的原生 worktree，基于 main） | Product Owner: SeaPawn | Designer: 原型和测试由 Designer 会话做，到 Prototype 时开；共情、定义、构思由 PO 和 Master 定、Master 落盘（PO 2026-11-14 的分工） | Scrum Master: 会话 IDEO # [master]-[main]-[management sprint]
> Now: Ideate：两个子代理各画一个方案（Haiku，互相看不见，各拿一份闪电演示材料）；同时 Master 和 PO 聊 PO 心里的画面
> Waiting for PO: 1 PO 心里有没有已经成形的画面
> Ends when the design questions are answered or the Product Owner stops the design (convention 19 in `design-log.md`); its conclusions flow back to the product log — a blank page's design fills it — and the first Sprint Review after that archives this file (convention 17 in `sprint-log.md`, in the sprint-kernel skill's `conventions/` folder).
> Methods: the stage excerpts in the design-kernel skill (excerpt paths below are relative to that skill's folder), and in every stage the ideo-kernel's IDEO mode and methods, as the design-kernel `SKILL.md` requires.
> This log records what each stage produced, not every step taken to get there (convention 22 in `design-log.md`).
> How to write this log: `design-log.md` in the design-kernel skill's `conventions/` folder.

## 1. Empathize

### 1.1 Challenge

一个人带着几个 AI 会话并行做项目，PO 想随时知道「现在走到哪了、每条线在做什么、哪里在等我」。现在只能问 AI、翻 git 历史、读日志：日志晦涩，历史不够明确，费时也看不清。第 1 版看板丑、不形象，看一次就不想再看第二次。

为什么是现在：Sprint 20 的目标是「拿得出手」，看板是其中最显眼的一块；今天 PO 同时开着 Master、Developer、Designer、助手四个会话，自己说「我们这次我都不知道在干嘛了」。

听到的（一手 = PO 自己说的，2026-11-14 在 Master 会话里答共情的提问，语音转写，方括号是 Master 补的字）：

- **怎么知道走到哪**（一手）：「打开这个项目啊，我就不知道就走到哪了，然后我就问 A[I]」；「主要是看一下 G[it] 的历史，然后还有……设计冲刺日志」；「日志的话太晦涩了，很难懂」「历史有时候也不够明确」；「花了一点点时间了，而且不是那么明确」。
- **几个会话一起跑**（一手）：「还是蛮多对话的，因为他们很多都让我来决策嘛……然后我也不知道他们做到哪儿了」。
- **第 1 版看板**（一手）：「太丑了，实在是太丑了」；「没有任何的……图像化、形象化」；「我看到之后我就不想再看第 2 次」。
- **竖屏挂着**（一手）：挂在另一块屏上，或者从这块屏「拆一点面积」给它，「一直是显示着……当前做到哪儿了」；「一般都是会和 stakeholder 的对话放在一块的，因为一般都是 stakeholder 的对话去维护他」；「过了半个小时……我看一眼，然后让这个[助手]更新一下」。
- **拍板**（一手）：「拍版就是在你这的呀。就是你问我……我才排版的呀。这个好像关系不是很[大]」。和 PBI-68 用户故事里的「拿它拍板」对不上：拍板发生在 Master 的会话里，看板管的是「知道走到哪」。

Master 的读法（PO 认了：「差不多」）：看板是一块挂着的「仪表」，不是打开来查的文件；它的活是让 PO 隔一阵瞄一眼就找回方位，尤其是几条线并行时；好看、形象是它能被一直挂着的前提；它旧不旧要看得出来，因为更新要靠助手。

### 1.2 Design goal

| Commitment | 一眼就知道：看板挂在 PO 的屏上，好看、形象；PO 隔一阵瞄一眼，就知道项目走到哪、每条线在做什么；不用再问 AI、翻 git、读日志，看着就想一直挂着。 |
| --- | --- |

### 1.3 Design questions

都从「它会怎么失败」反过来问；按 PO 说的轻重排（PO 2026-11-14 认）。

1. 好看、形象到 PO 愿意一直挂着吗？（PO：「最关键的」；第 1 版看一次就不想再看。）
2. 几条线并行时，每条在做什么，一眼分得清吗？（PO：「也很重要」。）
3. 隔一阵、离屏幕有段距离瞄一眼，看得出「走到哪」吗？还是要凑近读字？
4. 竖屏、电脑全屏、手机上都读得顺吗？（PO：「也很重要」。）
5. 条目很少、甚至一张白纸的项目，也像样吗？（PO：「条目很少的时候也得……有点这个样子」。）
6. 比起问 AI、翻 git、读日志，真的更省事、更清楚吗？晦涩的日志概括得出看得懂的样子吗？

PO 的决定和去掉的问题：

- **「在等 PO 的事」第一版不上看板**：PO 先说「当然要显示」，接着说：「如果是要显示这个的话，那就说明其他的点也要去更新看板，那其实我就不是那么喜欢……第一版可以先不写，因为只有 stakeholder 才会更新看板呀，所以它主要是要来同步整个过程。等我的……不如写个[hook]来提醒我呢……不如 stakeholder 他来提醒我直接」。设计目标里原有的「哪里在等他」据此去掉。这会动到 68-4 的照抄清单（Waiting for PO 不再上页面），交接时写给 Developer。
- **「过时了会不会骗人」不列为设计问题**：PO：「要靠 AI 更新了。不是那么关心」。生成时间照看板约定照样写在页面上。
- **拍板跟看板关系不大**：PO：「它做到哪儿了？我会用它辅助[拍板]。但是确实是一般，关系不是很大」。PBI-68 用户故事里的「拿它拍板」，设计结束、结论回流产品日志时改。

PO 的决定（2026-11-14）：课题照 Master 写的，PO 不审（「反正你直接写上去吧，我就是挑战，我就不用审了」）；设计目标、设计问题见上。「在等 PO 的事」由 hook 或助手提醒，不登记成 PBI（「不用登记成新的 [PBI]……他后碰到问题肯定会向我反映的」）。关卡：共情这一章行，进定义（「我觉得可以，可以往下走定义」）。

## 2. Define

### 2.1 Map

```mermaid
flowchart TD
    PO(["PO"])
    AS(["助手（维护看板）"])
    LN(["各条线的会话：Master、Developer、Designer"])
    LN --> A["各条线干活，写进日志"]
    AS --> B
    A --> B["助手照日志更新看板"]
    B --> C["看板挂在 PO 的屏上：竖屏、电脑或手机"]
    PO --> D
    C --> D["PO 抬头瞄一眼：好看、形象，看到项目走到哪、每条线在做什么"]
    D --> E["PO 心里有数，回到会话里接着做（拍板在会话里）"]
    E --> F["结局：PO 始终知道项目在哪，不用问 AI、翻 git、读日志"]
    E -. "工作往下走，日志又变了" .-> A
```

约定覆盖（PO 2026-11-14）：地图画想达到的愿景，不画现在发生的事（design-log 第 8 条写的是只画现在）；PO 在叫停的那条设计线里说：「你画现在的有什么意义呢」。愿景只写想达到的体验，不写做法；现在的样子（问 AI、翻 git、读晦涩的日志）和哪里疼，在第 1 章。

### 2.2 How Might We

对着 2.1 的地图和第 1 章写，按主题分，括号里是它对着地图的哪一步。PO 挑的打 ✓：2、3、4、5、9、11；没挑的不丢，当作做的时候要顾到的条件。

- 好看、形象（D）
  1. HMW 让 PO 第一眼看到的是一幅图，不是一串字？
  2. HMW 让它好看到 PO 愿意一直挂着，一眼不像模板？ ✓
  3. HMW 让这幅图本身就说出项目的结构：产品、条目、冲刺、设计怎么连着？ ✓
- 几条线并行（A、D）
  4. HMW 让每条线现在在做什么，一眼分得清？ ✓
  5. HMW 让每条线走到哪个阶段，像进度一样看得出来？ ✓
  6. HMW 让几条线同时跑也不乱？
- 瞄一眼（C、D）
  7. HMW 让隔着一段距离也看得清「走到哪」？
  8. HMW 让瞄一眼就够，不用凑近读字？
- 不同的屏（C）
  9. HMW 让同一页在竖屏、电脑、手机上都读得顺？ ✓
  10. HMW 让竖屏挂着看是主角，手机顺带？
- 少与空（D）
  11. HMW 让条目很少、甚至一张白纸的项目，看起来也像设计过？ ✓
- 概括（B）
  12. HMW 让晦涩的日志被概括成一眼看得懂的样子，又不加日志里没有的事？
  13. HMW 让想看某条线的细节时，一步就到日志里对应的地方？

PO 的决定（2026-11-14）：愿景地图行，挑 Master 建议的 6 个 HMW（2、3、4、5、9、11）——「认同，非常认同你的看法……这两个点我都同意」。关卡：定义这一章行，进构思（PO：「OK，我们后续的方案……」，并定画方案的子代理要拿现有材料）。

## 3. Ideate

### 3.1 Solution

（进行中。）画方案的子代理拿各自的一份闪电演示材料（PO 2026-11-14：「不给他现有的材料，他肯定……出不来好的方案」；第 11 条允许给「its own part of the gathered ideas」），不给第 1 版看板、约定和代码；只加载 ideo-kernel，不加载 scrum-kernel（第 11 条不给规矩，压过角色命令「子代理也加载两个内核」那句）。约定覆盖（PO 2026-11-14 认可 Master 的建议）：方案由 PO 和 Master 照调研材料画、照第 13 条定；另派 2 个互相看不见的 Haiku 子代理各画一个完整方案作对照，防止只在我们已有的想法里打转（第 11、12 条要的是几个子代理各画一个）。闪电演示（第 9 条）的材料：main 上的 `scrum/documents/PBI-68-board-references.md`、`PBI-68-board-research.md`。

### 3.2 Storyboard (optional)

（需要时写。）

## 4. Prototype

| Part | The design question it tests | Where it is |
| --- | --- | --- |

## 5. Test

（待做。）约定覆盖（PO 2026-11-14）：测试只由 PO 来——看板只给 PO 用，熟手卡就是他本人——不另派角色卡（第 17 条）；陌生人会在 Sprint 20 的 63 体验测试里读到看板。
