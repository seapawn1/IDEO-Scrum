# 设计侧全文：找到的问题与每处的建议

> 照 sprint-log 第 12 条：全文附问题与建议，交 Master 审。文件都在 `drafts/` 里，按新布局放。

## 改了什么（对照 outline.md）

| 文件 | 改动 |
| --- | --- |
| `drafts/design-kernel/conventions/design-log.md` | 第 1、3、4、6、8、9、11（整条重写）条；新增第 12 条（58 ③）；原 12–26 顺延为 13–27；图下加「The three loops」导读（58 ④）；全部摘录路径改 `steps/`；`sprint-log.md` 的路径改 `../sprint-kernel/conventions/` |
| `drafts/design-kernel/conventions/design-backlog-template.md` | 1.2 加「A vision, not how (convention 6)」；2.1 改成「只画现在发生的事：五六个框、一个环（convention 8）」；摘录路径改 `steps/`；条号跟着顺延 |
| `drafts/ideo-kernel/conventions/design-sprint-or-five-modes.md` | 新文件：图 + 第 1 条 |
| `drafts/ideo-kernel/SKILL.md` | 工具箱一节末尾加指向；Use Protocol 第 6 条加指向；`prototype/fake-it.md` 改 `steps/4-1-fake-it.md`（Sprint 16 的路径） |
| `drafts/scrum-kernel/SKILL.md` | 「Working with the Design and IDEO Kernels」一段：两处「open a design first」改成指向 ideo 约定第 1 条；其余不动（结构归 Sprint 16） |

## 问题与建议

1. **模板 2.1 原来写「five to fifteen steps between」**，与 58 ① 的「五六个框、一个环」冲突。建议：改成「只画现在发生的事：五六个框、一个环（convention 8）」；十五步的上限留在 `steps/2-1-make-a-map.md` 里当上限，不当目标（反馈文件原话）。已改。
2. **三个环与原型到测试之间的门**：导读说原型和测试可以自己跑，design-log 第 26 条和图上却有一道 PO 的决定。建议：门不删；导读写「PO 可以把这一处的阶段决定交给 Scrum Master（overview 第 12 条）」，这样两段能自己往下跑。已按此写；**停点 ② 请 PO 看这一处**。
3. **新第 12 条使 12–26 顺延为 13–27**：草稿已是最终条号。按 How 的「改号与内容分开提交」，搬运时先提交内容（新条暂排 27、旧号不动），再单独提交改号（脚本对短名、逐处读）。草稿是审阅用的最终文本，两个提交都从它导出。
4. **`scrum-kernel/SKILL.md` 的草稿基于现行文件**：Sprint 16 会删掉冲刺日志两行与事件章、把 `scrum-guide-2020.md` 挪进 `assets/`。建议：搬运时取 Sprint 16 的版本，只套用我改的这一段；草稿里其余部分是现行原文，方便看上下文。已按此写。
5. **「全新子代理」在多处出现**（design-log 第 11、17 条、命令）：定义由本冲刺写进 overview 第 7 条（第 4 项），这里只使用这个词，不重复定义。建议：保持。
6. **58 ⑦ 的局限用通用说法**：第 11 条只写「有的工具会把项目说明自动带给每个子代理；遇到就在设计日志里记一笔」，不写 Claude Code 的受管策略、子目录 CLAUDE.md、git 状态；依据在第 4 章笔记，收官写进 PBI-46。已按此写。
7. **设计模板 1.2、2.1 的注释**只加几个字和条号，没有把整条规矩再抄一遍（Master 的建议 e）。已按此写。
8. **路径写法**：design-log 与模板里的摘录路径相对 design-kernel 技能文件夹（文件开头已说明），写 `steps/…`；跨技能写 `../ideo-kernel/conventions/…`、`../sprint-kernel/conventions/sprint-log.md`、`../scrum-kernel/overview.md`。已按此写。
9. **ideo 约定只有一条**：图里 PO 先定；PO 不说时按默认分。没有编号到第二条。建议：保持一条，短。
10. **「聊着聊着碰到要研究的事，当场开设计」**是 PO 原话，保留在 ideo 约定第 1 条末尾。
