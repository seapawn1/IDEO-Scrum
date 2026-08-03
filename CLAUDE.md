# IDEO-Scrum

为 Claude Code 提供 Design Thinking 与 Scrum Sprint 方法论的插件。

## 这个仓库是什么

两层结构，改动前先分清在哪一层：

| 层 | 位置 | 性质 |
|---|---|---|
| **插件本体** | `plugins/ideo-scrum/` | 交付物。别人安装的就是这里 |
| **工作记录** | `Scrum/` | 用本插件的方法论开发本插件的过程记录 |

`Scrum/` 下的 sprint 目录是**历史记录**，记录当时的事实。除非发现事实错误，否则不要回头修改已完成 sprint 的内容。

## 维护规约

**README 是文件索引与当前状态，Git 历史负责追溯过去。**

- README 优先陈述：这里是什么、文件地图、当前状态
- 提交前确认 README 是否需要同步更新——尤其是新增/删除/重命名文件、改动插件版本号时
- 若发现 README 已过期、可能误导新会话的 LLM，必须显式提醒用户更新，不要默默放过
- 追溯旧决策、文件演变、阶段状态时，放手查阅 Git 历史

**版本号与 tag**

- 主干分支是 `main`，永远指向最新状态
- 版本号用 tag 标记，不写进分支名
- 插件版本号在 `plugins/ideo-scrum/.claude-plugin/plugin.json`，改动时 README 的两处版本号需同步

## 源材料与授权

插件内所有第三方摘录必须带署名。新增摘录时：

1. 文件顶部标注 `> Source:` 与 `> License:` 两行，License 须与 [ATTRIBUTION.md](ATTRIBUTION.md) 中记录的条款一致
2. 若引入新来源，先在 ATTRIBUTION.md 中登记，再写摘录

**已知的授权约束：**

- Scrum Guide 2020 / SGEP —— CC BY-SA 4.0，可摘录、可商用
- Stanford d.school Bootleg —— CC BY-**NC**-SA 4.0，含非商业限制
- 《Sprint》(Knapp) —— 全版权。**仅记录方法流程，不逐字摘录大段原文，不含书内插图**

`references/` 是源材料原件，**不入库**（`.gitignore` 已拦截），仅存于作者本地。

## 插件内容的自足性

插件会运行在别人的 Claude Code 里，那里没有本仓库的上下文，也没有作者的全局配置。

**写插件内容时，不要依赖任何未在插件内言明的约定。** 例如「用 mermaid 画图」必须同时说明方向（`flowchart TD`），否则在他人环境中行为不一致。
