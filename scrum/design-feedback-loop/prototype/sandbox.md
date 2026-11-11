# 测试用的全局记忆

在这次的临时根目录里建 `GlobalMemory/`，内容如下。每次测试都从这份干净的样子开始。

`GlobalMemory/MEMORY.md`：

```markdown
# Memory Index

- [时间按 UTC+8](time-utc8-get-date.md) — 用户叫台北时间；每个日期和时间都用 PowerShell `Get-Date` 查
- [图表用 Mermaid TD 和表格](mermaid-td-and-tables.md) — 结构化内容用 Mermaid 图和表格；一律 `flowchart TD`

## Feedback

- [IDEO-Scrum：构思要先发散](feedback/IDEO-Scrum/2026-11-08-ideate-same.md) — 隔离草图之前每份先发散，不然几份方案都差不多
- [IDEO-Scrum：设计地图要粗](feedback/IDEO-Scrum/2026-11-10-map-rough.md) — 地图只画现在发生什么：五六个框、一个环；分支和解法不进地图
- [IDEO-Scrum：设计目标写愿景](feedback/IDEO-Scrum/2026-11-11-goal-vision.md) — 设计目标写为什么做、想到哪里，不写怎么做
- [待认领：报位置太长](feedback/待认领/2026-11-11-path-long.md) — 每次都要报一长串位置，太别扭；说不清是哪个产品
- [ClaudeDream：整理时误合并](feedback/ClaudeDream/2026-11-09-merge-wrong.md) — 整理记忆时把两条合并错了
```

两个普通条目的文件各写一行同样的内容即可。五个反馈文件，每个都有 frontmatter（name、description、metadata.type: feedback、metadata.product），正文五项：

| 文件 | 日期 | 项目 | 原话 | 当时在做什么 | 理解 |
| --- | --- | --- | --- | --- | --- |
| `feedback/IDEO-Scrum/2026-11-08-ideate-same.md` | 2026-11-08 | SeaPawn | 四份方案都差不多，没发散开 | 做 design-apikey 的构思 | 隔离草图之前没有先发散，四份同质 |
| `feedback/IDEO-Scrum/2026-11-10-map-rough.md` | 2026-11-10 | SeaPawn | 地图不该画这么细，应该粗一点 | 做 fact-first 设计的定义 | 地图只画现在发生什么，五六个框 |
| `feedback/IDEO-Scrum/2026-11-11-goal-vision.md` | 2026-11-11 | IDEO-Scrum | 目标说的是一种愿景，你这个带有很强的执行性 | 定设计目标 | 设计目标写愿景，不写怎么做 |
| `feedback/待认领/2026-11-11-path-long.md` | 2026-11-11 | MTGP | 每次都要报一长串位置，太别扭 | 用语音交代 AI 记东西 | 说不清是哪个产品 |
| `feedback/ClaudeDream/2026-11-09-merge-wrong.md` | 2026-11-09 | IDEO-Scrum | 整理记忆的时候把两条合并错了 | 看整理后的记忆 | 整理记忆时误合并 |
