# 流程测试判定汇总（验收 6，第 8 项）

2026-11-10。题目与过线标准在 `SprintBacklog.md` 2.2「流程测试」，先提交（`1b07623`、`a87bd1c`）后跑；跑后标准没改。原始输出（15 份事件流和回答）放仓库外的系统临时目录，这里只留判定。收官时删除本文件。

**怎么跑的**：被测是提交 `87bd0db` 上的 `plugins/ideo-scrum/`（跑之前核对与工作区一致，跑的过程中没动）；`claude -p --model haiku`（实际模型 `claude-haiku-5-5`）`--plugin-dir`，只开 Read、Grep、Glob、Skill；空项目做工作目录，每次全新会话；5 题 × 3 次，15 次都在第一次调用就成功，没有重试。判定：读了哪些文件、五个阶段名的先后用脚本（先拿冒烟那份输出和改动副本自测，20 项全对）；语义项由我逐条读回答判。

## 结果

| 题 | 过 / 3 | 过线（≥2） | 说明 |
| --- | --- | --- | --- |
| 1 开冲刺 | 3 | 过 | 三次都读了 sprint-log 和 overview，五个阶段按序说全，每段结束由 PO 拍板，五处具体决定都说到 |
| 2 精化碰到没有现成答案的问题 | 1 | **不过** | 三次的内容都对，但有两次没读任何约定文件（只加载了技能），按「必须读到约定文件」判不过 |
| 3 白纸项目 | 0 | **不过** | 三次都没读约定文件；内容也不对：没有一次说出「产品和 Product Goal 写不出，所以交给设计、结论流回产品日志」 |
| 4 设计的构思 | 3 | 过 | 三次都读了 design-log 和 IDEO 的构思模式文件，先发散后收敛、隔离的子代理、PO 选定都说到 |
| 5 收官 | 3 | 过 | 三次都读了 sprint-log，Review、Retro 都当动作，都说不设章 |

## 每次

| 次 | 加载的技能 | 读到的约定文件 | 必答 | 不能 | 判 |
| --- | --- | --- | --- | --- | --- |
| 1-1 | scrum-kernel | sprint-log、overview | ①②③ 中 | 无 | 过 |
| 1-2 | scrum-kernel | sprint-log、overview | ①②③ 中 | 无 | 过 |
| 1-3 | scrum-kernel | sprint-log、overview | ①②③ 中 | 无 | 过 |
| 2-1 | design-kernel、ideo-kernel | design-log | ①②③ 中 | 无 | 过 |
| 2-2 | design-kernel、scrum-kernel | 无（回答里自己说「还没读 design-log 和 sprint-log」） | ①②③ 中 | 无 | 不过（没读） |
| 2-3 | design-kernel、ideo-kernel | 无 | ①②③ 中 | 无 | 不过（没读） |
| 3-1 | design-kernel、ideo-kernel | 无（只读了 ideo-kernel 的共情模式文件） | ① 勉强（说先做 Empathize、问要不要开设计日志）；② ③ 未中 | 无 | 不过 |
| 3-2 | 无（没调用任何工具） | 无 | ① ② ③ 未中（设计只作为「想按正式流程走」的选项） | 无 | 不过 |
| 3-3 | design-kernel、ideo-kernel | 无 | ① 中（开设计，只做 Empathize）；② ③ 未中 | 无 | 不过 |
| 4-1 | design-kernel | design-log、ideo-kernel 构思模式 | ①②③④ 中 | 无 | 过 |
| 4-2 | design-kernel | design-log、ideo-kernel 构思模式 | ①③④ 中；② 边缘（见下） | 无 | 过 |
| 4-3 | design-kernel | design-log、ideo-kernel 构思模式 | ①②③④ 中 | 无 | 过 |
| 5-1 | scrum-kernel | sprint-log、overview | ①②③ 中 | 无 | 过 |
| 5-2 | scrum-kernel | sprint-log、overview | ①②③ 中 | 无 | 过 |
| 5-3 | scrum-kernel | sprint-log | ①②③ 中 | 无 | 过 |

## 判定时的几处说明

- **4-2 的必答 ②（IDEO）算过，边缘**：它在流程里写「先发散（至少两种方法）」，没点出是 IDEO 的方法；但读了 ideo-kernel 的构思模式文件，并写明「还没读 ideo-kernel 的 Ideate 方法文件，正式开跑前要先读」，等于把 IDEO 方法当作流程里的一步。按 Master 定的判法（把 IDEO 方法当作流程里的一步来用，就算过；说成「需要时再用」才算不过）判过。若改判，题 4 仍是 2/3，过线不变。
- **题 1 里提到收官的 Review、Retro、「检查点代替每日站会」不算违规**：按 Master 的补充（收官时把 Review、Retro 当作动作提到，不算违规；违规是拿 Scrum Guide 的事件代替五个阶段来组织回答），三次都是按五个阶段组织的。
- **题 4 的脚本标记「可选」三处**：都指角色卡 Stakeholder 的 straw poll（设计日志约定写的就是「PO 要的话才让角色卡投一轮」），不是 IDEO 方法，不算违规。
- **题 5 的 5-3 多答了一段**：「教训记在哪里」除了项目的记忆或说明文件，还提到跨项目通用的放全局记忆；这是这台机器的全局约定，不是插件里的，没有违反「不能」项。
- 题 4、5 里模型都说没在项目里找到日志，因为测试的项目是空的，与判定无关。

## 没过线的两题怎么看

- **题 2**：三次的回答内容都对（开设计、只取难点、Sprint 其余照常、从共情起），没过线是因为判定里要求读到约定文件；两次只靠技能里的 SKILL.md 就答了，并说明「还没读约定」。这说明：这个问题的关键内容在两份 SKILL.md 里就能答对，但技能没有把「先读约定再答」推到这个问题上。
- **题 3**：三次都没加载 scrum-kernel（两次只加载 design-kernel 和 ideo-kernel，一次什么都没加载），所以「白纸项目先从设计开始」这条（在 scrum-kernel 的 SKILL.md、product-log 2、overview 2、design-log 1 里）一次也没碰到；design-kernel 的 SKILL.md 里没有这条。入口是「没有产品日志的新想法」这类说法时，现在的技能触发和 SKILL.md 带不到它。
- 这两处都是插件文字或技能描述要改的事，不属于已冻结的被测文字；怎么处理由 Master 和 PO 定，我没有动插件，也没有加跑。
