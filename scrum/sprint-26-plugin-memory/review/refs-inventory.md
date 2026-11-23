# 旧约定引用清单（Sprint 26 行 11–13 的准备）

由 `scripts/refs_inventory.py` 生成：活文件里所有指向六份旧约定的引用（档案 `scrum/documents/` 与 `references/` 不动）。落盘迁移时，每一处要么改指 Memory 的 handle，要么随旧文件一起删。

合计 20 处：路径 8、编号 5（其中解析不出目标 4）、标题 7。六份约定文件自己里面 0 处，别处 0 处。

## 按文件

| 文件 | 处数 |
| --- | --- |
| `CHANGELOG.md` | 8 |
| `scripts/check_docs.py` | 6 |
| `scripts/board_check/check.py` | 4 |
| `plugins/ideo-scrum/skills/memory/details/departures.md` | 1 |
| `scripts/check_dsh.mjs` | 1 |

## 解析不出目标的编号引用（要人看）

- `scripts/board_check/check.py:345` warnings.append("the data block holds a raw <; convention 15 asks for backslash-u003c")
- `scripts/board_check/check.py:886` # the product log in the working copy: its source is `working copy`, and a branch form is wrong (convention 4)
- `scripts/board_check/check.py:890` # the product log only on branches (conventions 4 and 11): `branch <name> @ <commit>`, the newest commit wins
- `scripts/board_check/check.py:890` # the product log only on branches (conventions 4 and 11): `branch <name> @ <commit>`, the newest commit wins

## 迁完后留下的（有意保留，逐文件附理由）

| 文件 | 处数 | 理由 |
| --- | --- | --- |
| `CHANGELOG.md` | 8 | the release history: its entries say what the files said then |
| `scripts/board_check/check.py` | 4 | numbers of board-log.md's own conventions; board-log.md stays at plugins/ideo-scrum/board/ |
| `plugins/ideo-scrum/skills/memory/details/departures.md` | 1 | its own heading |
| `scripts/check_docs.py` | 6 | the Departures table the README is checked against now lives in the Memory's details/departures.md |
| `scripts/check_dsh.mjs` | 1 | the guard that no plugin file names a conventions/ folder or overview.md |

## 六份约定文件之外的引用（要迁的，逐处）

| 位置 | 种类 | 目标 | 原文 |
| --- | --- | --- | --- |
