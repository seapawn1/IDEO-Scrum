# IDEO-Scrum: Product Goal & Product Backlog

## Context

IDEO-Scrum 是一个 Claude Code marketplace 插件，当前 v0.1.1。项目已完成方法论内核的导入和插件骨架搭建（5 个 commit），现在进入打磨阶段。

核心问题：两个内核质量不对称。ideo-kernel 有完整的使用协议、触发条件、方法模板；scrum-kernel 仅有 Scrum Guide 原文，无任何操作指引。此外两个内核之间没有衔接，各自独立运作。

本次 Sprint Planning 的目标是：定义 Product Goal，并产出一个有序的 Product Backlog。

---

## Product Goal

> **IDEO-Scrum 成为一个"可落地的方法论引导系统"——Claude 在实际对话中能主动、准确地引导 Design Thinking 和 Scrum 流程。**

---

## Product Backlog

| # | 事项 | 状态 | 说明 |
|---|---|---|---|
| 1 | 插件骨架搭建 | Done | 仓库初始化；ideo-kernel 导入（5 mode + ~40 方法 + 使用协议 + 触发条件）；scrum-kernel 导入（Scrum Guide 原文）；ai-partner 输出风格；Marketplace 清单；README；版本号至 0.1.1 |
| 2 | scrum-kernel 结构化改造 | Next | 补齐 Use Protocol、Event 引导模板（Sprint Planning / Daily Scrum / Review / Retro）、触发条件、Scrum 角色引导方式。目标：达到与 ideo-kernel 同等的可操作性。 |
