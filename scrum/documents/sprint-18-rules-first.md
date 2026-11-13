# Sprint Backlog — Sprint 18 (rules-first)

> Started: 2026-11-13 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/youthful-payne-b1e139`（原生 worktree `youthful-payne-b1e139`）| Product Owner: SeaPawn | Scrum Master: IDEO # [master]-[main]-[support sprint] | Developer: IDEO # [developer]-[sprint-18]-[do sprint 18]
> Now: 收官 · Master 2026-11-13 定收官（PO 授权）
> Waiting for PO: None
> 归档：2026-11-13 开工，同日收官；版本不动，仍 6.0.0（和 Sprint 19 一起发版）。日志已压缩成关键决定，逐条原文见 `git show 3e8860b:scrum/sprint-18-rules-first/SprintBacklog.md`；测试题、样本、判定脚本和报告见 `git show 3e8860b:scrum/sprint-18-rules-first/tests/`；原始输出在仓库外，不入库。

**并行与分工**：副线。主线 Sprint 19（看板、hook）同日开、并行做；两个 Developer 各在一个原生 worktree 里，Master 一个，在 main 上。

**PO 授权**（2026-11-13，原话）：「其实精化我一般让你做的，你的上下文最多，其实你可以详细的告诉他们得，怎么写精化啥得对不对，我把整个权限全放开了，也就是告诉你，后面你的权限拉满，除非必要，我来做决定，否则你都可以直接决定」。所以精化定案、精化结束、How 的审阅与放行、收官，都由 Master 做；改 Product Goal、推送发布、取消冲刺、推翻 PO 说过的话，仍回 PO。

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 规矩先顺：日志头部统一，scrum、sprint、design 召唤才来，角色说明写清；看板和 hook 照着就能读，文档照着就能写。（PO 2026-11-13 定） |
| --- | --- |

### 1.2 Definition of Done

Output Done 六项：内容忠实、可导航、无死链、插件校验、描述长度、Codex 包。

## 2. What

### 2.1 Product Backlog Items

PBI-66 日志头部、PBI-65 加载边界、PBI-60 角色说明（用户故事见产品日志 3.2 的出处）。

### 2.2 Refinement

精化由 Master 定案（Developer 的 66 头部提案在 `2561224`，定案只改了一处：承诺不挪到文件头）。

- **66 日志头部**：承诺留在原来的节里——产品日志 1.1、1.2，冲刺日志 1.1，设计日志 1.2——每处一张一行小表，键是 `Commitment`（中文日志写 `承诺`），只存一份，靠节标题认种类；冲刺、设计、IDEO 三种日志头部有 `> Now:` 和紧跟的 `> Waiting for PO:`，产品日志没有；IDEO 日志不设承诺，沿 For 找它服务的日志；阶段决定前引用目标原文，引不出就先补读，决定不算数；工作块做完在 Done when 格前写「✓ 日期」（66-8，看板要读）。理由：这几节本来就在最上面，挪到文件头要改四份模板结构，PO 不要大改内核。
- **65 加载边界**：只改描述——`disable-model-invocation` 会把技能从模型上下文里整个拿掉，角色命令就加载不了内核（claude-code-docs）。召唤是三种：角色命令、点名插件或内核、要建或改插件的日志；泛问照常回答。ideo 放开到发散、定义问题、做原型、做测试、用户研究。CLAUDE.md 描述规约那两句一起改；README「方法论会自动介入」一句一起改（65-7，Developer 查出）。
- **60 角色说明**：插件里五处「secretary」全换成「服务 PO；在书面授权范围内代行，问责仍在 PO，决定要记录」；stakeholder 命令加 PO 助手身份——整理日志、汇总、只转达已定的事、维护看板，不排序、不拍板、不审阅、不改插件；改范围、要放行都经 Master。看板放哪由 Sprint 19 写进 overview 第 4 条。
- **测试**：11 题（A 泛问 3、B 召唤 3、C ideo 放开 3、D 角色 2），每题 3 次，基线与新版同日同通道；过线 A ≤1/9、B ≥8/9、C ≥7/9 且不低于基线、D 每题不低于基线；标准先单独提交（`fde1f50`），之后没改过。

## 3. How

H1 冻结测试标准 → H2 先交 66 接口（Sprint 19 要读）→ H3 同日基线 → H4 改 65、60 → H5 新版对照 → H6 交审。Master 2026-11-13 放行：本分支提交，合并、tag、发版在 Review 定，不推送；审阅直接看分支上的 diff，不另写审阅稿（Master 定）。

## 4. Increment notes

- **66**（`1e347b4`）：9 份模板和约定照定案改，承诺格式只在 overview 第 17 条写定一处，其余指过去；Master 审过，当天转给 Sprint 19。
- **测试通道**：用 `claude-magpie`（用户级规矩）。冒烟两次失败才查清：子进程继承了宿主的模型重映射，`haiku` 解析成宿主的模型名，上游 502；改成 11 个变量的白名单环境（Sprint 19 验证、两边统一）。magpie 是固定映射，`--model` 写什么都跑同一个便宜模型，汇总标「非 Haiku」。
- **65、60**（`9b347af`、`76a2cc3`）：skill-reviewer 建议把 stakeholder 的「never the builder」改回旧说法，Master 不采纳——sprint-log 第 17 条原文就是「never the builder」，本意就是不许自己审自己。白纸项目的直接路径不再自动进设计冲刺，是 65 有意的结果，从角色命令进来照旧（PBI-52 的直接路径行为就此改变）。
- **第 1 轮**：A 0/9 过，B 6/9、C 0/9 不过——C 比基线 3/9 还差。原因：改描述时把 ideo 的「先加载再答」强句也删了（定案 65-4 没写清只删三个受控内核的）；B3 去读了日志却没加载技能。Master 限一轮修正：每条描述只加一句「命中就先加载」（`be78fa9`）。
- **第 2 轮**：A 0/9、D 3/3、3/3 过；C 3/9 只追平基线；B1、B2 六次在 300 秒处超时——magpie 的 API 一路重试，Windows 上超时又没杀掉子进程，答案迟到。照冻结原文「修环境后补齐有效试次」：修好整树终止，超时放到 1200 秒，只补这 6 次，同日完成，6/6 触发，B 最终 8/9 过；迟到的答案不算。
- **PO 2026-11-13 决定**（原话「1.可以 2C可以 3 可以」）：B 技术补跑；C 记成已知缺口，登记 PBI-67；然后交审、收官。

## 5. Test

| 组 | 基线 | 第 1 轮 | 第 2 轮 | 结论 |
| --- | --- | --- | --- | --- |
| A 泛问时三个受控内核不加载 | 9/9 误加载 | 0/9 | 0/9 | 过 |
| B 召唤时加载对的内核 | 9/9 | 6/9 | 8/9 | 过 |
| C 发散、定义、原型时加载 ideo | 3/9 | 0/9 | 3/9 | 不过：已知缺口，转 PBI-67（PO 定） |
| D 找对角色（助手 / Master） | 0/3、3/3 | 3/3、3/3 | 3/3、3/3 | 过 |

测试模型是 magpie 的便宜模型，非 Haiku。内容 31 达、2 部分、0 不达。DoD 六项都过：strict 校验通过（另有既有的 ICON_MISSING 提示，归 PBI-64）；Codex 核对 0 错；79 个资源两跳内可达；四条描述 ≤1024（ideo 1023，已顶线）；secretary 0 处；归档没动。66 的五项验收全过。

**Review**：Master 终审通过（自查 strict、Codex、secretary、描述长度、归档）。熟手卡（Haiku 子代理）看增量：愿意用，平时不用口述规矩，读头部就能接上；落差——README 说「不必先说 IDEO」言过其实（收官时已改成照实写）、召唤要用户自己记得、「书面授权」最简是什么没写、stakeholder 描述人读要读两遍、第 5 章结论埋在细节里、交审时 Waiting for PO 写 None 看不出在等 Master。前四条进产品日志（PBI-62、67），后两条进 Retro。

Master 2026-11-13 定收官（PO「3 可以」：H6 之后收官）。
