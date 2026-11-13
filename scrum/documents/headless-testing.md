# 无头回归测试手册

> 从 CLAUDE.md 的「回归测试」一节搬出（2026-11-14，PO 拍板精简 CLAUDE.md）。这是本仓库跑无头测试的操作手册：判定口径、magpie 用法、子进程限制、超时与判定。插件不要求用户照做。

- 判定标准先写、单独提交，再跑；出结果后不改标准。
- 用便宜的模型跑（PO 2026-11-08）。要另起 Claude CLI 时用 `claude-magpie`（用户级规矩，2026-11-13）：它把 `--model` 固定映射到 magpie 自己的便宜模型，写什么都一样，不是 Haiku；汇总标「magpie 的便宜模型，非 Haiku」，不写模型名和提供方。
- 脚本按关键词判断大纲顺序会误判；判错的逐条人工看，改判写明理由，验收时摆给 PO（2026-11-08）。
- 触发测两条路径：从角色命令进入，和直接说。
- 比较描述效果，同日同环境对照，带改前基线。
- 无头测法（Sprint 18、19 定）：`claude-magpie.cmd -p --plugin-dir <插件 Windows 路径>`（Git Bash 里要带 `.cmd`）。子进程环境用白名单，不从宿主逐个删：宿主除了认证和网关，还注入模型重映射与模型目录（Sprint 18：`haiku` 被解析成宿主的模型名，上游 502）、AUTO_COMPACT_WINDOW、跨会话消息的套接字与令牌、会话编号。只带 SystemRoot、PATH、USERPROFILE、APPDATA、LOCALAPPDATA、HOMEDRIVE、HOMEPATH、ComSpec、PATHEXT，再设 TEMP、TMP（每次全新的空目录）、CLAUDE_CODE_GIT_BASH_PATH、MSYS_NO_PATHCONV；额外的开关只用 `--env` 明着给。magpie 默认 bypassPermissions，`--allowedTools` 只是免询问、限不住工具：用 `--tools Read,Grep,Glob,Skill` 限工具，`--disallowedTools` 另禁 Bash、PowerShell、Write、Edit、Agent，`--strict-mcp-config` 去掉 MCP；加 `--permission-mode dontAsk` 也不够，用户 settings 里宽泛的 allow 规则照样放行，要再加 `--setting-sources project,local` 把用户 settings 挡在外面，白名单才真生效（Sprint 19）；冒烟时核 init 里的实际工具和模型（只比布尔，不记值）。比对技能名时去掉 `ideo-scrum:` 前缀；同一轮只用一条通道；路径用 `cygpath -w`；`--resume` 会让 SessionStart 每轮都触发，要测会话里的行为，就在同一进程里用 `--input-format stream-json` 一条一条发，等上一条的 result 再发下一条（一次发多条会并成一轮；`/compact` 也能这样发）；核对 hook 用 `--include-hook-events` 的流，不靠模型复述。查变量只列名字，不打印值。
- Windows 上超时要杀整棵进程树（`taskkill /T /F`）：只杀 cmd，CLI 会接着跑，写出迟到的答案。API 自动重试能拖过超时，超时不等于模型没调用：看重试事件和 API 耗时。技术失败照冻结的标准补齐有效试次，不挑样本，迟到的答案不算（Sprint 18：B 组 6 次超时，修好后补跑 6/6）。
- 验证用的子进程先核对它真的被限制了：看 init 事件的 `permissionMode`，也看 `permission_denials` 出没出现过——一次都没有，多半是限制没生效，不是模型守规矩（Sprint 19）。
- 量 token 要成对比：文档 MCP 开场连没连上，同一个提示的输入就差约 1300 token；两个臂拿连接状态相同的一对来减（Sprint 19）。
- 选定规则要把限定词写全：「选最省的过线臂」要写成「在带 SessionStart 的过线臂里」，字面读会选出一个自己没过线的配置；判「过期」看明细，模型可能是发现了不一致、照日志做了对的决定（Sprint 19）。
- 检查脚本独立读日志时，路径锚在顶层（后缀匹配会把测试夹具里的假日志当成开着的），别假定编号写法（Sprint 18 的工作块是 `H1`）；夹具放真仓库才有的形状，并先拿真仓库的状态过一遍（Sprint 19）。
- 便宜的模型逐字抄长文会丢字（地图里丢一个 `-`、删掉 `<br/>`）：逐字的规矩要配核对；权限放宽时模型自己写脚本拷贝就不丢，收紧时只能手抄（Sprint 19）。
- 工具审查员（skill-reviewer 等）的必改项，落盘前先对一遍 PO 的定案和约定原文；冲突就报 Master，不照改。（Sprint 18：审查员要把 stakeholder 的「never the builder」改回旧说法，与 sprint-log 第 17 条原文冲突，没采纳。）
- 测试记录先写结论（过没过、缺口在哪），细节和编号放后面（Sprint 18 熟手 Review：结论埋在近万字里）。
- 测试题不带引导词（如「按插件的约定」）：引导词等于叫模型去加载插件，测不到用户自然的说法；题里也别有会限制它行动的话（「先别看东西」被当成「别读文件」）（2026-11-08，Sprint 10）。
- 判对不只看加载了哪个技能，还要看读没读该读的约定（Sprint 10：加载了 scrum-kernel 却只读 references，答出两周冲刺）；用 Grep 读到文件内容也算读了。
- 判定脚本先拿一两份已知结果自测再用（Sprint 10：正则里混进一个退格符，三份对的回答全被判错）。
- 「不少于改前」这类过线，改前可能满分时要留余量或加次数，并且在跑之前定（Sprint 14 样板：改前 15/15，改后 14，少 1 次就没过线，也测不出结构的好处）。
- 汇总里把行为（有没有触发、读没读约定）和内容（答得对不对）分两栏列，别混成一个分数；缺口出在哪一栏，改法才对得上（Sprint 14：题 3 的内容渐渐答对，缺的一直是触发和先读约定，登记 PBI-52）。
- Windows 上无头测试要连 PowerShell 一起禁（只禁 Bash 拦不住）；要写文件的测试不放在 `~/.claude` 下，那里会被权限系统拦写，改用系统临时目录。
- 测试的原始输出放仓库外，仓库里只留判定汇总；提交前按提供方地址、凭据值、令牌形态、设置值扫一遍（Sprint 13：原始输出带了模型服务地址，只好改写未推送的冲刺历史）。
- 正式测之前先冒烟：一次最简单的调用，确认模型在提供方的实际目录里（不看本地模型缓存）、读文件的权限正常（Sprint 13：第一轮模型无通道，第二轮只读权限拒读，各白跑一轮）。
- 在 Codex 里测角色：`codex exec` 里裸打 `$角色` 挂不上角色，要用 app-server 的原生 Skill 输入；隔离安装用独立的用户目录，不动本机 `~/.codex`。当时的脚本在 `git show sprint-13-codex~1:scrum/sprint-13-codex/run_codex_smoke.py`（Sprint 13）。
- 原型说明里举例，别用正在测的那个点：它等于把那个点又写了一遍，会混进对照（Sprint 15 设计第二轮）。
- 对照组跑之前先确认真的去掉了那样东西：检查最终喂给模型的文件，不只看源文件（Sprint 15：脚本先内联后删行，第一次对照没隔开）。
- 判定标准照被测的那句话写，别比它更严：被测那一行允许「一个环」，标准写成「没有判断分支」，第三轮就有一次卡在这里（Sprint 15）。
- 描述有 1024 字符上限（Agent Skills 规范，plugin-validator 会报，Codex 也照它）；Claude Code 技能清单每条显示到 1536，但以 1024 为准。现在最长的是 ideo-kernel，1023 字符（Sprint 18），已经顶线；改描述时先量长度（Sprint 16；Sprint 17 第 2 轮一度超到 1191，收官前压回）。
