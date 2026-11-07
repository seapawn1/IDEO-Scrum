# Sprint Backlog — Sprint 08（IDEO-Scrum 4.0 · 设计内核独立）

> 开工 2026-11-08 | 不写截止日：Sprint Goal 达成或 PO 叫停时收官（产品日志 2.2.5） | 分支：`sprint-08-design-kernel`（不开 worktree，PO 定） | PO：SeaPawn | Master 与 Developer：Claude，同一会话兼任（PO 2026-11-08 定）
> 对抗审查：Master 兼 Developer，不自审，交全新子代理（PO 可另指定）。拿不准的点找 PO 裁决（产品日志 2.2.3）。
> PBI 状态只写在产品日志，本文件只引用编号；流程见产品日志 2.2.5。

# 一、Why

## 1.1 Sprint Goal

**设计内核独立**：设计冲刺从 ideo-kernel 分出来，自成 design-kernel，按共情、定义、构思、原型、测试五个阶段写，能用原文就用原文；ideo-kernel 只留五模式和方法库，每个角色都先加载它；设计日志有了模板，开一份设计照着就能走完。

## 1.2 DoD（摘抄自产品日志 1.3，全部选入；整份 DoD 照样适用）

**Definition of Outcome Done**

| 度量 | 目标信号 |
| --- | --- |
| 一次会话走通方法论环节：完整引导（结构化、忠于原文） | 用户不反复追问 |

**Definition of Output Done**

| 维度 | 标准 |
| --- | --- |
| 内容忠实 | 忠于源材料（SGEP / d.school / Sprint）；方法论设计部分（融合、solo+AI）标注来源与依据 |
| 可导航 | 从 SKILL.md 入口 ≤2 跳到达任意 reference |
| 无死链 | 所有 markdown 内部链接可解析，无 404 |

通用验证（CLAUDE.md）：改动插件结构后过 plugin-validator；skill 改动过 skill-reviewer；迁移类改动全仓 grep 旧值至零；触发回归先写判定标准、单独提交，同日对照、两条路径。

# 二、What

## 2.1 PBI（摘抄自产品日志 3.1）

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 | 备注 |
| --- | --- | --- | --- | --- | --- |
| PBI-29 | ideo-kernel 收窄——只留 IDEO 五模式与方法库 | 作为熟手，我想要 ideo-kernel 只讲 IDEO 五模式和方法库，并且每个角色都先加载它，以便 Developer 冲刺卡住、Designer 做原型时，手边都有共情、定义、发散、原型、测试的方法 | 2.2.7 载体：ideo-kernel | M | 以现有 ideo-kernel 为底，删去设计冲刺部分（Two Schemes、Design Sprint 表、`design-sprint/` 目录，交 PBI-34）；描述保留 IDEO、five modes、design thinking 等触发词；PBI-25 ④ 随之解决；与 PBI-34 同版发，升大版本；验收草案：三个内核同日对照，两条路径的触发回归（以 PBI-22 的 5/5 为基线），SKILL.md 不变长；来源：2026-11-06 PO 精化（原「换主线」），2026-11-07 第三轮改为拆内核 |
| PBI-34 | 新建 design-kernel——设计冲刺 | 作为熟手，我想要设计冲刺有一套完整、照着就能做的方法，和原型、测试、发散的方法接上，以便设计日志里的研究有章可循，而不只靠五张单薄的阶段卡 | 2.2.7 载体：design-kernel；2.2.6 设计日志 | L | 从 `references/` 的原书扩充，原文优先、可带例图，太长的可删减（2.2.7）；按 IDEO 五阶段组织（共情、定义、构思、原型、测试），不按原书的五天（PO 2026-11-07）；和 ideo-kernel 重复的方法不再写；设计日志模板放它的 `conventions/`（PBI-28）；ATTRIBUTION.md 第 4 节随之更新（位置、使用范围），版权声明由 PO 定；名字是 v3 用过的旧名、意思变了（PO 接受），发版时在 README、CHANGELOG 说明；与 PBI-29 同版发，升大版本；验收草案：触发回归——「设计冲刺 / design sprint」进 design-kernel，「五模式 / design thinking」进 ideo-kernel；PO 深度参与；来源：2026-11-07 精化第三轮（PO 定新建） |
| PBI-28 | 设计日志约定 v1 | 作为熟手，我想要某条 PBI 需要设计时，有一份设计日志模板可以照着做，以便把难点研究清楚、结论回流产品日志和冲刺，而不是卡住或凭感觉做 | 2.2.6 设计日志（Map 的「设计」） | M | 放 design-kernel 的 `conventions/`，依赖 PBI-34；范围：设计日志模板（五章：共情、定义、构思、原型、测试）、设计文件夹与分支做法、收官（重写成 Review 文档归档 `docs/`）；分支从冲刺分支开还是从 main 开，用到时再定（分支名不能写成「冲刺分支名/xxx」：git 不允许 `a` 与 `a/b` 两个分支并存）；来源：2026-11-06 PO 精化口述（原「DesignBacklog 模板」），2026-11-07 改写（第一轮叫 Target 日志，第四轮改回设计日志、与冲刺平级） |
| PBI-36 | 角色命令按新规则加载内核 | 作为熟手，我想要每个角色一进入就加载该加载的内核，以便 Designer 手边有 design-kernel，各角色手边都有 IDEO 的方法 | 2.2.3 角色与主场 | S | Master 加载三个；Developer 加载 ideo + scrum；Designer 加载 ideo + design；Stakeholder 只加载 ideo；designer 命令第 9 行「设计冲刺五阶段见 ideo-kernel」改为指向 design-kernel；与 PBI-29、34 同版发；来源：2026-11-08 Sprint 08 Planning，从 PBI-32 切出 |

- 收官发版：PBI-29、34、36 同版发，升大版本（v5.0.0）。
- 不在范围：codex 分支（PO：最后再说，归 PBI-30）；PBI-25 除 ④ 以外各项（拟 Sprint 10）；PBI-32 其余各项（拟 Sprint 10）。

## 2.2 精化

PO 2026-11-08 定，精化结束。要点：

- ideo-kernel 定位为整个插件共用的工具箱，设计和冲刺都用。design-kernel 每个阶段写明对应 IDEO 的哪个模式，链到 ideo-kernel，不重抄 IDEO 的内容（PO：「摘了也没用……它本来就加载了」）。
- 原书只摘和人机协作有关的：日程、周几、零食与休息、白板与用品、线下投票这类删去。方法句子里顺带提到的周几保留，design-kernel 的 SKILL.md 开头一句说明「原书按五天排；这里按阶段走，不按天」（PO：「肯定是没办法全部都删完的」）。
- 构思重在出方案、挑方案（PO：「挑方案很重要很重要」）；故事板收；闪电演示可收可不收。
- 测试用 Haiku（PO：「要用便宜的」）。

| 编号 | 内容 | 验收标准 |
| --- | --- | --- |
| 29-1 | 删去 SKILL.md 的「Two Schemes」「Design Sprint」两节；`design-sprint/` 交 34-1；Use Protocol 第 1 步只认五模式（PBI-25 ④） | `ideo-kernel/design-sprint` 全仓零残留（历史记录除外）；SKILL.md 比现在短 |
| 29-2 | 开头写明 ideo-kernel 是整个插件共用的工具箱；描述保留 IDEO、five modes、design thinking 与方法名，Design Sprint 与「先预研究」交 design-kernel | 「用 IDEO 五模式」「design thinking」加载 ideo-kernel |
| 29-3 | scrum-kernel「Working with the IDEO Kernel」一节与描述里那半句：要预研究就开一份设计（design-kernel）；IDEO 的方法（ideo-kernel）随时可用；其余不动 | scrum-kernel 的触发与改前同日对照不变差 |
| 34-1 | 新建 `skills/design-kernel/`：SKILL.md（描述；开头一句不按天；五阶段表：阶段 → 对应的 IDEO 模式（链到 ideo-kernel）→ 原书摘录 → 约定）；现有五份文件搬来按阶段归位 | 从 SKILL.md 两跳内到任何文件；无死链 |
| 34-2 | 共情、定义补齐：HMW（转成问题、整理；挑选由 PO 定）、选靶按原书补全 | 原文、标出处；只留和人机协作有关的 |
| 34-3 | 构思（对应 IDEO 构思）：四步草图（出方案）、Sticky Decision 与 Rumble（挑方案，PO 拍板为主，投票从简）、Storyboard；闪电演示可收 | 同上；出方案、挑方案两件事写足 |
| 34-4 | 原型（对应 IDEO 原型）：Fake It、Prototype | 同上 |
| 34-5 | 测试（对应 IDEO 测试）：Small Data、五幕访谈、Learn | 同上 |
| 34-6 | 每份文件头 Source/License；ATTRIBUTION 第 4 节改位置与使用范围（版权声明文字由 PO 定）；README 文件地图，并说明 design-kernel 是 v3 的旧名、意思变了 | 署名齐；README 与插件一致 |
| 28-1 | design-kernel `conventions/` 放设计日志模板：文件头 + 五章（产品日志 2.2.6 的表） | 照模板能建出一份空的设计日志 |
| 28-2 | 约定：何时开、谁负责、放哪、分支（用到时定，名字不写成「冲刺分支名/xxx」）、收官（整份重写成 Review 归档）；各阶段我们怎么做：专家＝PO 与 2.1 角色卡，出方案＝几个互不相通的子代理，PO 拍板，测试用角色卡召唤 Stakeholder、PO 也测；开头身份声明，每条标来源 | 全英文、自足；与官方不同处写明理由（设计可以不在冲刺里做） |
| 36 | 四个命令的加载句按产品日志 2.2.3 改；designer 第 9 行改为指向 design-kernel | 从每个命令进入，加载的内核与 2.2.3 一致 |

- 例图不放图片文件，改画成 Mermaid（flowchart TD）或写成文字（PO 2026-11-08，以前的 Map 文件就是这样做的）；只画讲方法的图。
- 不收：Team、Time and Space、按天的检查清单、FAQ。

# 三、How

## 3.1 How

只给方向，细节施工时定。

1. 先做 34-1、29（含 29-3），同一个提交：搬家和收窄一起，中间不会出现两个内核都有、或都没有设计冲刺。
2. 按阶段写 34-2～34-5；共情与定义写完、构思写完、原型与测试写完，各停一次给 PO 看（PBI-34：PO 深度参与）。
3. 再做 28、36、34-6。
4. 触发回归：判定标准先写、单独提交；用 Haiku 跑；三个内核同日对照，两条路径（角色命令、直接说）。
5. plugin-validator、skill-reviewer；对抗审查交全新子代理（Master 兼 Developer，不自审）；PO 验收。
6. Review、Retro，发 v5.0.0。

PO 放行：2026-11-08，可在冲刺分支上提交（含 Planning 落盘与记忆仓库的新增条目）；合入 main、打 tag、发版等 Review 时再定；不推送。

## 3.2 笔记

> 只往后加。每行：日期 · 做了什么 · 决定与理由 · 证据或提交号 · 下一步。

| 日期 | 做了什么 | 决定与理由 | 证据 | 下一步 |
| --- | --- | --- | --- | --- |
| 2026-11-08 | 工作区 | 先按 PO 上一条开了 worktree；PO 定这个冲刺不用（Master 兼 Developer 直接做），退出并删除，在主目录切到本分支。worktree 配置留着，以后并行时用：从本地 HEAD 开、`.worktreeinclude` 复制 `.env`、本地设置与 `references/`（Windows 下 symlinkDirectories 没建出链接） | `3dd410d`（main）、`f010a8d` | — |
| 2026-11-08 | Planning 阶段 1 | PO 定：Sprint Goal 照 PO 以前的行文风格写；选入 PBI-29、34、28，设计日志模板一起做；从 PBI-32 切出 PBI-36（内核加载：Master 三个，Developer、Designer 各两个，Stakeholder 只加载 ideo-kernel）；DoD 全选，「≤2 轮进入执行」PO 看不懂、删去；冲刺路线拟为 08～10（09、10 也可合并）；新增「拿不准就问 PO」 | 产品日志修订记录 2026-11-08 | Planning 阶段 2：精化 |
| 2026-11-08 | Planning 阶段 2、3 | PO 定精化结束（见 2.2）、How 方向（3.1）、放行；我提的两问：原文里的周几保留、SKILL.md 一句说明；scrum-kernel 改与 IDEO 衔接的一节。后面两个冲刺拟另开 Developer（PO：本冲刺上下文最全、后面要等它，所以 Master 兼 Developer） | 产品日志 1.2、2.2.7 | 施工：34-1 + 29 |
| 2026-11-08 | 34-1 + 29（含 29-3） | design-kernel 骨架与五阶段表；ideo-kernel 改成工具箱、删设计冲刺两节；scrum-kernel 预研究改指 design-kernel；designer 第 9 行顺带改（不然指向已删的内容），加载句留给 36 | `885bf1b` | 34-2 |
| 2026-11-08 | 34-2 共情、定义 | 五份旧文件和新的 how-might-we 全部改成原书原文：脚本按行号从原书取，只删不改写（修了转换造成的断字和脚注标记）。删去：开头的 Blue Bottle 整段故事、Flatiron 背景、记 HMW 的便利贴与马克笔、投票的贴点规则、零食与休息。保留：例子里讲方法的部分、9 张方法图（地图、HMW、选靶，共 840K）。旧文件里作者加的话（「solo 时你就是 PO」、Decider 改成 Product Owner）不进原文，改到 28 的约定里写。ATTRIBUTION 第 4 节「不含插图、只记方法流程」的说法已不符，34-6 改 | `d5e79d2` | 给 PO 看共情、定义 |
| 2026-11-08 | 检查点：共情、定义 | PO：不放图片，改画成 Mermaid 或写成文字（以前就是这样做的）；示范例子按推荐保留。9 张图改画：地图与选靶用 Mermaid，目标与问题、HMW 便签写成文字；`images/` 删除；2.2.7、CLAUDE.md、记忆里的「可带例图」一并改 | `7f91c34` | 34-3 构思 |
| 2026-11-08 | 34-3 构思 | 五份原文：Remix and Improve（闪电演示，可选）、Sketch（各自出方案，四步草图）、Decide（挑方案：Sticky Decision 与「Make honest decisions」）、Rumble（两个赢家冲突时都做原型；含 Note-and-Vote）、Storyboard。删去：Slack 公司前史、贴胶带布展、折纸计时、起飞玩笑、各章脚注；原书 Note-and-Vote 最后一句在转换稿里就断了，删去断掉的半句。挑方案的步骤原样保留（PO：挑方案很重要），贴点投票的细节到 28 的约定里换成我们的做法（子代理出方案、Master 讲评、PO 拍板）。四步草图画成 Mermaid | 本次提交 | 给 PO 看构思 |

# 四、Review

（收官时补。）
