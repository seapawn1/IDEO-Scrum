# PBI-72 · 文档候选交审

本页是冲刺工作材料。中英维护说明全文（[`docs/maintaining.md`](../../docs/maintaining.md)、[`docs/maintaining.zh-CN.md`](../../docs/maintaining.zh-CN.md)）已按下方大纲写成送审稿，现有用户文档（中英 README、双语快速上手）的拟措辞保持待定，等待 Master 审稿与 H4–H5 实机 Test 证据后再落盘；本页不是发布文档，也不是已通过的迁移说明。宿主事实、隔离要求与待批 Test 前置见 [host-evidence.md](host-evidence.md)。

**需审的改动**

| 位置 | 问题 | 建议与当前状态 |
| --- | --- | --- |
| 中英 README 的安装、升级两节 | DSH 宿主号容易和插件号混淆；现有普通升级说明没有覆盖这次版本号下调。 | 保留两宿主的安装入口，标清版本号分别指什么。升级节链接到迁移说明；只把通过实机的路径写成操作指引。**当前未改 README。** |
| 双语快速上手的「开始之前」 | 现在只有「已安装」的前提；从旧版来的读者可能找不到版本迁移说明。 | 在原来的一条前提里同时链安装与升级，不重复命令，不动角色入口和流程。**当前未改快速上手。** |
| 新维护说明 | 规则和方法论为何都只有一份、两宿主怎样读取，以及接手维护者怎么复核，目前缺一个落点。 | 已写成 [`docs/maintaining.md`](../../docs/maintaining.md) 与 [`docs/maintaining.zh-CN.md`](../../docs/maintaining.zh-CN.md) 送审稿，严格对应下方大纲（H1 + 4 H2）及 `check_docs.py` 结构对等规则；待 Master 审阅全文及实机 Test 通过后再随 H2 合入 `check_docs.py` 的 `PAIRS`（中英 README 文件地图仍只列 `docs/`）。 |
| 本仓库共用规则 | 复制现有 `CLAUDE.md` 正文而不改原文件，会留下两套生效规则。 | **已完成原样迁移（2026-11-20，PO 直接授权本执行会话）**：将 `HEAD:CLAUDE.md` 原样迁至根 [`AGENTS.md`](../../AGENTS.md)（5691 字节，blob `65e2c4e`，保留原文及授权边界），[`CLAUDE.md`](../../CLAUDE.md) 仅留单向导入 `@AGENTS.md`（11 字节，blob `43c994c`，无循环引用）。 |

**现有用户文档拟用文字**

| 位置 | English | 中文 |
| --- | --- | --- |
| README · DSH 安装的版本说明 | The number in the DSH install instructions is the DSH host version, not the IDEO-Scrum plugin version. | DSH 安装说明里的版本号是 DSH 宿主版本，不是 IDEO-Scrum 插件版本。 |
| Quick start · 开始之前 | Install IDEO-Scrum for your host, or follow the upgrade instructions if you already have it. | 按你的宿主安装 IDEO-Scrum；已经装过的，请看升级说明。 |

第二行分别链接对应中英 README 的「安装」与「升级」。不把实机待验的市场降号、重新安装或 DSH 重启步骤写成已确认的迁移指引。

**新维护说明大纲（中英同结构）**

| 层级与标题 | 写什么 |
| --- | --- |
| H1 · 维护 IDEO-Scrum / Maintaining IDEO-Scrum | 说明适用对象是维护这份仓库的人，而不是项目的 Scrum 入门。 |
| H2 · 双宿主，正文只维护一份 / Two hosts, one source | 说明 `plugins/ideo-scrum/` 是角色和内核源，DSH 适配器直接使用它；不做生成包同步。 |
| H2 · 仓库规则从哪里读 / Where repository rules load from | 说明 `AGENTS.md` 是唯一共用正文，Claude 由 `CLAUDE.md` 单向导入，DSH `0.2.2-rc.5` 的默认加载器直接读取；区分官方源码与实机结果、项目规则与子代理 preset。 |
| H2 · 已装用户怎样迁移 / Migrating an existing installation | 给每个宿主一条经 Test 验证的 `6.0.3 → 0.6.3` 路径；教读者确认实际加载版本及项目日志不变。Claude 旧市场与 DSH 旧本地 bundle 分开说，不把后者写成旧公开版。 |
| H2 · 候选如何核验 / Checking a candidate | 讲版本同步、变更记录与发布边界；区分严格校验、回归、打包检查、实机入口与承诺证据，链接现有维护资料。 |

**本轮不进公开文档的内容。** DSH 命名 preset 已有官方依据，项目级自动发现／注册仍未证实；Claude 和 DSH 的降号迁移均未实跑。Sprint 23 的约定措辞与 Sprint 24 的角色／承诺行为不在本稿重写；整合时按最终生效版本核对。
