# plugin-validator（Sprint 26 行 12、13 共用的一次）

2026-11-23，`plugin-dev:plugin-validator`（`model: haiku`），由 Master 在 Master 会话里派出，只读，审 `3a30fbe` 的插件树（开始和结束时 HEAD 都是 `3a30fbe`，中途没变）。结果由 Master 经跨会话消息转给 Developer；这页是 Developer 按那条消息记的，不是验证员的原始报告。

**判定：PASS，没有 error。**

## 核过的项

- 清单（`plugin.json`）与目录结构没问题；
- 七个技能的 `name` 与文件夹一致，`description` 都 ≤1024 字符：design-kernel 1006、ideo-kernel 1009、memory 353、scrum-kernel 967、sprint-kernel 942（design-kernel 的描述是 1006 字符、1030 字节，上限按字符算）；
- 五个角色入口点名的技能都在，没有一处还指向已删掉的旧约定；
- memory 里 15 个细则文件和 `../../board/board-log.md` 都解析得到；其他技能指向 memory 和模板的路径也都解析得到；
- hooks 没问题。

## 两条 warning 与 Master 的判断

1. `template/design-backlog-template.md` 第 13、32、44、56、65 行的 `steps/…`：不算问题。这是 Sprint 26 之前就有的写法，模板头部写明了「excerpt paths below are relative to that skill's folder」。
2. `template/product-backlog-template.md:4` 的「`details/flow-maps.md` in the same skill」：可以接受。模板会被拷进用户的项目，相对插件的路径在那里本来就解析不到，点明是哪个技能正是该用的写法。另提：`board/board-log.md:3` 的「`details/names.md` in the memory skill」，要不要改成 `../skills/memory/details/names.md`，Master 交 Developer 定，不挡收官。**Developer 定：改**——这份文件留在插件里，读它的人从 `board/` 出发，`AGENTS.md` 也要求引用别的技能的文件写 `../<技能>/文件`，不裸写文件名；已改，随下一个提交。

## 注

- 模型：Master 派的子代理写了 `model: haiku`；实际跑的是哪个模型由 Master 会话的宿主决定，Developer 没有核对。
- 第一次尝试（Developer 经 `scripts/run_prompt.py` 在会话外跑，magpie 的便宜模型）被系统因内存告急停掉，没有结论，记为技术失败，见 `SprintBacklog.md` 第 4 章「行 13 迁引用做完」。
