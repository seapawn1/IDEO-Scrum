# 落盘后与审定的草稿不同的地方（Sprint 26 行 12）

由 `scripts/land_memory.py --apply` 生成。清单（`SKILL.md` 的正文）与草稿 `memory-draft/MEMORY.md` 逐字相同，没有差异；下面是细则文件与别处落盘时做的事。

## 细则文件（`skills/memory/details/`）与草稿的差别

| 文件 | 做了什么 |
| --- | --- |
| `closing.md` | the Open points for the Product Owner section removed；the drafting note "the text is the old rules word for word" removed |
| `departures.md` | the Open points for the Product Owner section removed |
| `design-ending.md` | the Open points for the Product Owner section removed；the drafting note "the text is the old rules word for word" removed |
| `design.md` | the Open points for the Product Owner section removed；the drafting note "the text is the old rules word for word" removed |
| `flow-maps.md` | the Open points for the Product Owner section removed；said plainly: The process maps of the six old convention files, with the lines (hand… |
| `folders.md` | the Open points for the Product Owner section removed |
| `gates.md` | the Open points for the Product Owner section removed；the drafting note "the text is the old rules word for word" removed；said plainly: Sprint 27 changed convention 12 in two ways, both here: it says *stage… |
| `goal-fixed.md` | the Open points for the Product Owner section removed |
| `handoff.md` | the Open points for the Product Owner section removed |
| `ideo-ending.md` | the Open points for the Product Owner section removed |
| `names.md` | the Open points for the Product Owner section removed |
| `product-log.md` | the Open points for the Product Owner section removed |
| `refinement.md` | the Open points for the Product Owner section removed |
| `roles.md` | the Open points for the Product Owner section removed |
| `sprint.md` | the Open points for the Product Owner section removed；the drafting note "the text is the old rules word for word" removed |

## 别处

- `skills/memory/SKILL.md`：新建，frontmatter（`name: memory`、一行带引号的描述，不超过 1024 字符）加上面说的清单正文。
- `commands/{developer,designer,scrum-master,stakeholder,supporter}.md`：加载序列最后加 `ideo-scrum:memory`；「Subagents you dispatch load…」那句加上 memory；`supporter.md` 的转达限制按 PO 2026-11-23 的决定改（经授权的 Supporter 转达也算，写明何时何地授权；宿主自己的确认照宿主来）。
- `dsh/index.js`、`scripts/check_dsh.mjs`：DSH 适配器注册并预载 memory；压缩后重新调用 memory 的提示放在每轮回放的命名上下文 `ideo-scrum:memory` 里（Master 2026-11-23：写法 B），`check_dsh` 加了一项断言。
- `ATTRIBUTION.md`：引用位置由 `scrum-kernel/conventions/` 改为 `skills/memory/details/`。
- 删除（`git rm`）：`skills/scrum-kernel/overview.md`、`skills/scrum-kernel/conventions/product-log.md`、`skills/sprint-kernel/conventions/sprint-log.md`、`skills/design-kernel/conventions/design-log.md`、`skills/ideo-kernel/conventions/ideo-log.md`。`board/board-log.md` 留在原处。
