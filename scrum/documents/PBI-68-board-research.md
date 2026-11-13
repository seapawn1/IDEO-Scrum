# 看板调研：现有结果汇总

> 生成 2026-11-14。来源：三份后台调研 workflow 的已完成部分；调研到此为止，不再补。正文是文字与链接；两处配过浏览器实拍截图，涉及别人的版权，只留在当时那台机器上，没入库。

## 一、总调研：好看的 Scrum / 看板（PO 要的）

### 1.1 成熟 SaaS 工具（8 个）

### Linear
- 链接：https://linear.app/docs/projects
- 类型：项目管理 / 产品研发工作台
- 风格：暗色优先的极简界面：灰阶层级加极细边框，Inter 字体，低饱和紫只作强调；信息密度高但留白克制。
- 强项：项目概览页把摘要、属性、资源、描述、里程碑和进度图收进一条纵向阅读流，层级清楚；看板列头带数量，状态和进度一眼能扫。
- 不适合我们的：它的精致感很大程度来自暗色应用外壳、侧栏和可交互细节；我们是只读单页、没有操作，整套搬过来会显得空，手机上也偏重。
- 契合度：high
- 可以抄：把每张卡做成“小标题—一句摘要—细进度条—关键属性”的纵向阅读流，强调色只给当前阶段和进度。
### Notion Projects
- 链接：https://www.notion.com/product/projects
- 类型：文档 + 数据库工作区
- 风格：文档式排版：大留白、黑白为主、细分隔线；卡片小圆角、轻阴影，靠封面图和 emoji 点一点颜色。
- 强项：页面读起来像一篇文章而不是仪表盘，三张卡可以顺着读；数据库卡片把状态、负责人、进度压成一行小属性；天然适合手机单列。
- 不适合我们的：Notion 的视觉个性依赖封面、emoji 和可编辑块；去掉交互后容易变成普通白页。数据库视图还需要大量字段和配置，和“只读概览”不是一回事。
- 契合度：high
- 可以抄：用文档排版承载看板：大标题 + 短摘要 + 2–4px 细进度条，手机端直接单列堆叠，不做横向滚动。
### Asana
- 链接：https://asana.com/features/project-management
- 类型：项目协作 / 工作管理
- 风格：明亮、留白充足，浅灰底配少量品牌色；列表视图干净，圆角卡片和轻阴影，信息按行分组。
- 强项：Asana 的 Project Overview（项目概览）把描述、角色、目标、关键资源和状态更新集中成一页项目简报；on track / at risk / off track 这类状态独立于任务列表，适合概括。
- 不适合我们的：概览页偏表单和控件，视觉记忆点弱；官网主要展示列表而非看板，真正的 Overview 还要配置。静态化后容易像一张表格。
- 契合度：medium
- 可以抄：给每张卡一个“简报区”：目标原文 + 当前状态 + 关键角色/资源，任务只留计数和完成标记，不展开明细。
### Shortcut
- 链接：https://www.shortcut.com/blog/designing-a-calmer-clearer-faster-shortcut/
- 类型：软件开发项目管理（原 Clubhouse）
- 风格：2025 年改版主打 calm：减少图标和装饰、增加呼吸感，颜色只帮助聚焦；排版层级统一，深色模式重新调过对比。
- 强项：公开拆解了看板、故事卡、导航怎么减噪：故事卡简化到标题、任务计数等必要信息，导航按 Work / Planning 分组；改版后 77% 用户留在新版。
- 不适合我们的：仍是交互式应用，文章是营销叙述加前后对比图，没有可直接套用的概览版式；紫色主色和工具化密度不适合安静的只读页。
- 契合度：medium
- 可以抄：定一条“颜色只表示状态”的规则：五阶段用一条低饱和进度轨加当前节点，其余全部灰阶。
### GitHub Projects
- 链接：https://github.com/features/project-management
- 类型：开发者项目管理（issue / PR 驱动）
- 风格：开发者工具式克制：白底、细灰边框、紧凑表格，绿/黄/红状态胶囊，编号和分支用等宽字体。
- 强项：同一份数据可在 Table / Board / Roadmap 间切换；状态、迭代、标签、负责人都是小字段；完成项降饱和，扫读成本低，和本仓库的日志文化很接近。
- 不适合我们的：为密集条目和拖拽设计，字号小、个性弱；表格截图不是“漂亮”的编辑式版式，直接照搬会像后台而不是看板。
- 契合度：medium
- 可以抄：工作项用“状态点 + 标题 + 编号/计数”的紧凑行，已完成项整体降饱和并加勾，未完成项保持正常对比。
### Trello
- 链接：https://trello.com/
- 类型：看板式任务管理
- 风格：彩色板背景配白卡，标签色条、封面图、贴纸；整体轻松、视觉化、偏消费级。
- 强项：列和卡的阅读顺序最直觉；卡片上的标签色和封面让分类不靠文字；手机端体验成熟。
- 不适合我们的：颜色和装饰太多，和“只读、安静、有设计感”冲突；多列拖动的心智模型不适合三张概览卡；缺少项目叙事层。
- 契合度：medium
- 可以抄：每张卡顶部加一条 3–4px 的语义色条（产品/冲刺/设计各一色），卡身保持白底黑字，颜色只做索引。
### Jira
- 链接：https://www.atlassian.com/software/jira/features
- 类型：企业级敏捷项目管理
- 风格：Atlassian 企业蓝、控件密集；泳道、列头计数、状态徽章、筛选条，典型工具界面。
- 强项：Scrum 板的行业标准：冲刺目标、列、WIP 限制、泳道、状态一目了然；列头数字和状态色帮助快速判断进度。
- 不适合我们的：界面外壳重、按钮多、密度高，视觉偏旧；我们的页面没有操作，照搬会显得笨重；手机端必须整页重排。
- 契合度：low
- 可以抄：冲刺卡顶部照 Scrum 板习惯写清“目标 + Now + 各列计数”，五阶段像列头一样等宽排开、当前列加粗。
### monday.com
- 链接：https://monday.com/
- 类型：工作管理 / 可视化看板
- 风格：高饱和状态色、卡片化 dashboard、图标和插画多；活泼、营销感强，信息块密集。
- 强项：状态色系统非常清晰（首页示例为 Ready to start / In progress / Waiting / Done），不同视图复用同一套颜色；dashboard 组件让概览有节奏。
- 不适合我们的：太吵、太彩色，组件像积木；我们只有三张卡，抄它的仪表盘会过度设计；大量图标和按钮与“不放按钮”相冲突。
- 契合度：low
- 可以抄：定一套三到四色的语义状态色并全页复用（进行中/等待/完成），但把饱和度压下来，只用于圆点和细条。
### 1.2 开源看板（6 个）

### Planka（PLANKA）
- 链接：https://planka.app/
- 类型：开源自托管看板（Trello 式；现为 fair-code，社区版源码可见，Pro 闭源）
- 风格：深色插画底图配半透明磨砂列面板，白色圆角卡片；卡片按「封面大图 → 彩色标签 pill → 浅灰字段 chip → 粗体标题 → 灰色摘要 → 底部小图标计数」排列；一套中性色配单一强调色，另有五套主题（Pro）；整体精致、图片驱动、触感强。
- 强项：开源看板里公认界面最漂亮的一档；卡片解剖完整，标签、字段、描述、计数各就各位；对手机有专门布局：列宽约 80vw、横向滑动、信息单列堆叠；官网首页直接展示 board-view 与五套主题截图，GitHub README 有演示 GIF，planka.app 还提供可登录的 Pro 演示（数据每小时重置）。
- 不适合我们的：现已不是 OSI 开源（fair-code），手机支持与五套主题属 Pro 功能；视觉高度依赖封面大图，纯文字的只读页面照搬会显得空；加卡、拖拽、筛选等交互控件很多，正是我们不需要的。
- 契合度：high
- 可以抄：① 列做成浅色/磨砂圆角面板，列头只留小号标题 + 计数；② 卡片元信息用浅灰底小 chip（PBI 编号、日期、负责人），标题粗体、摘要两行截断；③ 375px 下只显示一列宽（约 85vw）横向滑动，卡片内部单列堆叠；④ 中性灰底 + 一个强调色贯穿，阶段色只出现在标签和列头细条上。
### Kan.bn
- 链接：https://kan.bn/
- 类型：开源 Trello 替代（AGPLv3，Next.js + Tailwind CSS）
- 风格：近黑深色主题（也有浅色版），背景带极细点阵；左侧窄图标栏 + 大号白色标题 + 大量留白；列无底色，卡片是深灰圆角块 + 1px 低对比边框；标签为描边 pill + 彩色小圆点；层级全靠字号和灰阶，极简、安静、Linear 风。
- 强项：目前开源看板里视觉最克制、最有设计感；结构简单（列 → 卡 → 标题 + 标签 + 少量元信息），天然适合只读展示；Tailwind 写法容易搬进单文件 HTML；官网有明暗两版真实 hero 截图。
- 不适合我们的：功能很薄：只有列表、卡片、标签、评论，没有冲刺、阶段、泳道、WIP 等 Scrum 结构，撑不起「产品目标 + 五阶段 + 工作项完成标记」的层级；没有公开的交互 demo；截图以桌面为主，375px 需自行重排。
- 契合度：high
- 可以抄：① 深色配色：近黑底 #0b0b0c、卡片 #17171a、边框 #26262a、标题白 90%、次要文字 55% 灰；② 列头只放 15–16px 白字 + 灰色计数，不加底色和重边框；③ 标签 pill 用 1px 描边 + 8px 彩色圆点，避免实心大色块；④ 列宽 300–320px、卡间距 10–12px、页面留白至少 32px，让只读页面不挤。
### Plane
- 链接：https://github.com/makeplane/plane
- 类型：开源项目管理（AGPLv3；Jira/Linear 替代）
- 风格：浅灰画布 + 白色圆角卡、细边框、近乎无阴影；状态用「小图标 + 文字」chip，元信息用浅灰底 chip（编号、日期、头像叠放）；同一屏可上时间轴（Gantt）、下看板；字号小、留白大，冷静专业的现代 SaaS / Linear 风。
- 强项：观感最接近高端商业产品，克制但不单调；状态 chip、编号 chip、日期、头像的元信息行非常值得借；「上方时间轴/进度 + 下方卡片流」的结构，正好对应我们的冲刺卡（目标 + 五阶段 + 工作项）；GitHub README 有 work items、cycles、modules、analytics 等多张真实截图。
- 不适合我们的：营销首页现在不放界面截图，要跳到 GitHub README 看；产品复杂度高、交互多（筛选、分组、菜单），不能照搬；小字号高密度在 375px 上必须重排。
- 契合度：high
- 可以抄：① 元信息行：小图标 + 浅灰编号 chip + 描边状态 chip + 日期 chip + 头像叠放；② 冲刺卡上半放一条极简五阶段进度条/时间轴，下半才是工作项卡片；③ 阶段色用低饱和米、淡紫、淡蓝 + 小圆点，标题始终最高对比；④ 底色 #f7f7f8、卡片 #fff、边框 #e6e6e8，用 1px 边框和留白分层。
### Focalboard（Mattermost）
- 链接：https://github.com/mattermost-community/focalboard
- 类型：开源项目管理（Notion/Trello 替代；已停止维护，代码仍公开）
- 风格：浅色 Notion 风：左侧饱和蓝侧栏、白色主区、超大的粗体页面标题；列头是柔和 pastel 底色（米/黄/绿）+ 灰色计数；卡片白底细边框圆角块，属性为彩色小 chip（P2、姓名、日期），几乎无装饰。
- 强项：属性 chip 和列头柔和底色，特别适合表达 PBI 编号、负责人和阶段；卡片文字优先、装饰极少，正合只读无按钮的页面；README 的 hero 截图清晰，能直接看到真实布局。
- 不适合我们的：已停止维护（README 明说 not maintained）；界面里的侧栏、工具栏、New/Filter/Sort 按钮很多，是我们明确要避免的；Notion 式就地编辑无法、也不该在单文件只读页复现；截图是桌面宽屏，移动端无参考。
- 契合度：medium
- 可以抄：① 列/组头用 8–10% 透明度的 pastel 底色 + 深一号文字，右侧配灰色计数；② 卡内属性 chip（编号、负责人、阶段）圆角 4px、字号 11–12px；③ 卡片只保留图标 + 标题 + 属性行，去掉全部按钮；④ 页面大标题 32–40px 粗体 + 一行灰色副标题，给整页定调。
### Vikunja
- 链接：https://vikunja.io/
- 类型：开源自托管任务管理（AGPLv3；List / Kanban / Gantt / Table 四视图）
- 风格：浅灰画布 + 白卡 + 淡边框；左侧 200px 侧栏、居中项目名；视图切换是白底 pill 分段控件（选中蓝底白字）；卡内有灰色 #编号、右对齐日期 chip、饱和度较高的标签 pill（红/绿/蓝）和优先级小图标；亲和、实用，设计感中等。
- 强项：信息层级（编号、日期、标签、优先级）清楚，最接近我们「工作项 + 完成标记」的需求；官网有明暗两套真实截图，try.vikunja.io 可免注册体验；列头的 WIP 计数（如 5/10）可借来做静态进度。
- 不适合我们的：视觉偏工具化，不如 Planka、Kan.bn 惊艳；Kanban 只是四种视图之一，列无容器底色，整体排布不够讲究；没有 Scrum 概念（冲刺、阶段、泳道）；截图以桌面为主。
- 契合度：medium
- 可以抄：① 浅灰画布 #f5f5f5 + 白卡 + #e5e5e5 边框，最省力也最耐看；② 页面顶部用 segmented control 切换「产品 / 冲刺 / 设计」三块，选中项 accent 底色；③ 工作项行：左侧灰色 #编号、右侧日期 chip，下一行标题 + 标签 pill；④ 列头写名称 + 计数（5/10），不画重边框。
### Taiga
- 链接：https://taiga.io/
- 类型：开源敏捷项目管理（Scrum + Kanban；AGPLv3）
- 风格：2015 年代 AngularJS 风格：浅绿白画布、深灰图标侧栏、彩色阶段列头（黄/蓝/橙/绿）、横向泳道；卡片小、字号 12–13px、可带封面图，标签 pill、头像组、评论/附件小图标密集；信息密度高，今天看略显旧。
- 强项：Scrum 信息架构最完整：泳道 + 阶段列 + WIP limit + epic 色点 + backlog，几乎就是我们要表达的冲刺结构；官网有 Kanban/Scrum/Issues 多张真实截图，tree.taiga.io 有公开项目可点。
- 不适合我们的：视觉陈旧、色彩发灰、字号小，不符合现在的审美；手机端不是重点；一眼就是「管理工具」，控件和密度都过多，与只读展示页相冲。
- 契合度：medium
- 可以抄：① 用泳道表达三条内容线（产品 / 冲刺 / 设计），泳道内再分阶段列；② 阶段列头用 4–6px 彩色细条 + 名称 + 计数，颜色只做编码；③ 完成/WIP 计数放列头右侧灰色小字；④ epic 色点 + 标签的组合，用来标 PBI 类别。
### 1.3 手机端适配（6 个）

### GitHub Projects 手机版（公开测试）
- 链接：https://github.blog/changelog/2022-10-11-on-the-go-with-github-projects-on-github-mobile-public-beta/
- 类型：产品版本说明
- 风格：工具型、列表优先、少装饰；系统字体、中性色，信息密度高但不拥挤
- 强项：把桌面表格在手机上改成纵向列表，而不是把表格压窄；分组用可折叠的分组（bucket），默认只展开要看的一组；自定义字段变成每行里一眼能读的元数据小胶囊（metadata pills），扫一眼就知道状态；顶部标题栏下拉切换视图；长按条目可预览或编辑。对只读概览最值得学的是「分组—条目—元数据」三层压得很清楚。
- 不适合我们的：2022 年的公开测试说明，视觉细节和截图级规范很少；交互依赖长按和编辑，只读网页用不上；没有卡片式主视觉和图表折叠；对非工程读者，信息密度仍偏高。
- 契合度：high
- 可以抄：375px 下把三张卡变成三个可折叠分组：默认只展开「当前冲刺」，产品卡和设计卡收成一行标题加最多两个小胶囊（如 Product Goal、当前阶段）；冲刺卡内每条工作项排成一行——左侧 ✓/○ 状态、中间标题单行省略、右侧一个阶段小胶囊；分组标题做成 sticky 小条，滚动时始终知道在哪一组；不要横向滚动。
### Linear 手机版（ScreensDesign 界面拆解）
- 链接：https://screensdesign.com/showcase/linear-mobile
- 类型：UI 图库 / 产品拆解
- 风格：极简、精密、低饱和；靠字重、留白和细线分层，暗色模式也克制
- 强项：手机上明确是「read-mostly」的伴侣：底部工具栏放核心导航，拇指可达；列表行只保留优先级和负责人两个关键元数据，点进去才看详情；每个字段用独立的聚焦弹层，避免一屏堆满控件；层级是 Home→Team→Issue，始终只有一条主线。对只读看板，「列表行只留两个线索、详情另开」最值得抄。
- 不适合我们的：原生 App 的底部工具栏、长按和弹层都需要 JS 或原生容器，单文件静态 HTML 只能模拟；它服务工程师的高频操作，不是给 PO 看的概览；视觉偏冷，放在设计或创意语境里可能太工程。
- 契合度：high
- 可以抄：手机端只保留一条纵向卡片流；每张卡头部一行「小标签 + 标题」，下面最多三条关键事实（Product Goal 一句、Sprint Goal 一句、Now 一句），再多就收进「查看日志」链接；阶段、工作项、完成数用一行三个等宽小格，数字大、标签小；导航做成底部三个文字锚点（产品 / 冲刺 / 设计）或顶部 sticky 三锚点，二选一，别做侧栏；卡片之间用 1px 细线和 24px 留白分隔，不用重阴影。
### Notion 手机端页面布局技巧（DevelopersIO）
- 链接：https://dev.classmethod.jp/articles/20240610-tips-for-creating-a-comfortable-layout-for-smartphone-viewing/
- 类型：设计文章 / 教程
- 风格：文档型、朴素、结构优先；黑白灰为主，靠标题层级和折叠组织内容
- 强项：讲清了多列在手机上的行为：桌面从左到右的列，在手机上按顺序从上到下堆叠；建议不要在列里再嵌数据库；长内容用 toggle 折叠；数据库和代码块打开「右端折返」，避免横向滑动；目录放左列，否则手机上会掉到页底；桌面浏览器压窄窗口不能代替真机测试。
- 不适合我们的：是 Notion 专用技巧，不是通用 CSS 布局方案；没有断点数值和视觉设计建议；对「好看」帮助有限，只能借结构。
- 契合度：medium
- 可以抄：桌面三栏在手机上按 DOM 顺序堆叠，所以先定好顺序：当前冲刺放第一，产品卡第二，设计卡第三（或按 PO 的卡片优先级），不要用 CSS order 让视觉顺序和阅读顺序不一致；每张卡内部用原生 details 折叠「背景 / 历史 / 细节」，默认只开当前冲刺；所有长文本允许换行，不做横向滚动；375px 单独在真机或 DevTools 看一遍，不要只看桌面窄窗口。
### 让 Dashboard 适配手机（The Bricks）
- 链接：https://www.thebricks.com/resources/how-to-make-your-dashboard-mobile-friendly
- 类型：设计文章 / 指南
- 风格：数据仪表盘、卡片化、实用主义；干净的图表和数字优先布局
- 强项：给的是可直接执行的数字：先按单列设计再扩列；手机首屏只放 2–3 个 KPI；不要因为桌面把大图放最上面，200px 高的折线图在手机上读不了，先给关键数字再给图；表格转卡片三种做法（每行一张卡、只留 2–3 列点开看更多、换成横向条形图），明确说绝不要横向滚动的表格；组与组之间加小标题帮助滚动定位；触控目标 Apple 44px / Google 48px；正文 16–18px、KPI 数字 24–32px；一主色加一强调色。
- 不适合我们的：面向数据仪表盘，不是项目看板；没有 375px 精确断点；示例偏通用，视觉风格不强；KPI 数字写到 32px 时，旁边再放长中文标题会显得过大。
- 契合度：high
- 可以抄：375px 首屏先放三个大数字（当前冲刺完成 3/7、进行中 2、待 PO 决定 1），下面才是卡片；阶段图或进度图压到 120–160px 高，或直接改成一行文字「阶段 3/5 · Prototype」；每张卡之间加 12px 的小标题（产品 / 冲刺 / 设计）；正文 16px、数字 28px、行高 1.5；状态用「文字 + 圆点」而不是只靠颜色；所有可点区域至少 44px 高。
### 响应式 SaaS 界面的三档布局（SaaS Development Agency）
- 链接：https://saasdevelopment.agency/blog/responsive-saas-ui-complex-figma-layouts
- 类型：设计文章 / 工程实践
- 风格：工程化、断点驱动、组件优先级；视觉中性，重结构和状态
- 强项：把断点说死：≥1280px 桌面全侧栏 240–280px；768–1279px 平板图标栏 64–72px；小于 768px 手机无侧栏，主 section 进底部 tab bar，最多 4–5 项，次级放抽屉。面板有优先级，变窄时低优先级折进 expand、accordion 或 tabs。表格三种策略：横向滚动加固定 1–2 列、转卡片加 show more、按优先级隐藏列。图表会按容器宽度减少标签（12 个月改成每 3 个或每 6 个）、图例从侧边移到下方、窄屏改高纵横比、数据点抽样。这些正是「图表和地图怎么折叠」的通用做法。
- 不适合我们的：面向复杂 SaaS 应用，需要 JS 状态和 ResizeObserver；对单文件静态看板过重；底部 tab 对只有三个 section 的页面可能多余；文章是工程视角，视觉范例少。
- 契合度：high
- 可以抄：只做两档就够：900px 以上三栏卡片；900px 以下单列，并按优先级折叠——当前冲刺全展开，产品卡只留 Product Goal 一行，设计卡只留当前阶段一行；手机上不要横向滚动；阶段图在窄屏改成竖向 5 步（或一行 5 个点加当前步高亮），标签只留当前阶段，其余用序号；图例和说明移到图下方；如果设计卡里有地图或关系图，手机上默认折成一张缩略图加一句「展开看设计日志」，不要全屏铺开。
### Skyscanner Design — Card List
- 链接：https://www.skyscanner.design/latest/components/card-list/overview-TcDlJyFZ
- 类型：设计系统文档
- 风格：旅行产品、卡片化、清晰；圆角卡片、图像与文字分区、轻阴影
- 强项：明确区分手机上的两种卡片排法：rail（横滑）和 stack（纵列）。rail 适合空间不够、需要扫一组卡片；stack 适合内容跟随页面自然纵向流；桌面网格可以对应任意一种，不是固定配对；卡内横排还是竖排取决于内容比例（宽大于高用横版，高大于宽用竖版）。这正好回答「卡片怎么单列」。
- 不适合我们的：设计系统组件文档，没有信息密度、折叠和断点细节；rail 对可发现性有风险，不适合内容多的概览；没有 375px 的具体尺寸。
- 契合度：medium
- 可以抄：我们的看板是「页面自然纵向流」，选 stack 不选 rail：375px 下三张卡全宽单列、间距 12px、圆角 12–16px，不做横滑；卡内用竖版（标题在上、元数据在下）；只有「数字 + 一句话」的 KPI 小卡可以用横版（左文右数），因为宽大于高；卡片不要嵌套横向滚动或轮播，卡内信息一屏读完。
### 1.4 单页概览（6 个）

### Zed Roadmap（含内嵌 GitHub 看板）
- 链接：https://zed.dev/roadmap
- 类型：公开路线图 + 内嵌看板
- 风格：深色极简、工程感；大标题下横向卡片配小号状态胶囊，下半页嵌三列 issue 看板；黑白为主、留白克制、几乎无装饰
- 强项：一页三段递进：Currently Working On 用大卡（标题、一句说明、In Progress/Done 胶囊）→ Coming Up Next 降为纯文字卡 → Build Zed with Us 嵌 Triage / Planned / In progress 三列看板，卡面只留标题、issue 号和票数；已完成项直接链到文档或博客，细节不堆在页面上。
- 不适合我们的：六张卡横排在 375px 会变成长堆叠；票数与 issue 号对只读项目看板是噪音；视觉锚定 GitHub，深色品牌感强，不一定适合项目日志的气质。
- 契合度：high
- 可以抄：用三档信息密度代替折叠：正在做给「标题 + 一句说明 + 状态胶囊」的大卡；接下来降级为纯文字列表；看板区只留三列和极短卡面，任何细节都外链到日志或 issue。手机端自然变成一条纵向、密度递减的阅读线。
### Obsidian Roadmap
- 链接：https://obsidian.md/roadmap
- 类型：公开路线图
- 风格：单列文档式、大量留白；粗标题加细分隔线，少量品牌色强调；没有卡片阴影，层级几乎全靠字号与间距
- 强项：Active / Planned / Launched 三段一目了然：进行中给一句说明，计划中只给标题，Launched 按月倒序、每条链到 changelog、博客或帮助文档；顶部一句话把 Changelog 和论坛设为出口，读者知道去哪里看细节。
- 不适合我们的：视觉偏朴素，缺少进度感和负责人/时间；Launched 会越积越长，页面越来越重；首屏没有一句「现在最该看什么」的总览。
- 契合度：high
- 可以抄：用三个固定状态词排顺序：当前项一句话，未来项只留标题，历史按月分组并链到日志原文。这样一页里只有「当下」是重的，过去自然沉底；单列结构在 375px 上不需要任何重排。
### GitHub Public Roadmap
- 链接：https://github.com/github/roadmap
- 类型：公开路线图（README 说明页 + Projects 看板）
- 风格：GitHub 原生 Markdown 文档风：标题、粗体标签、表格、少量装饰符号；功能优先，几乎不做视觉设计
- 强项：分层非常彻底：README 只解释「怎么读」——Release phases（Preview / GA / in design / exploring）、标签体系、GHES 版本表、免责声明；条目本体在另一个 Projects 看板；交付后关 issue 并评论 Changelog 链接，历史有明确去处。
- 不适合我们的：视觉参考价值低；真正内容要跳到另一个页面且依赖 JS 渲染；标签与流程对单人项目过重。
- 契合度：high
- 可以抄：把「图例」和「数据」分开：看板顶部只留三四个状态的定义、更新时间和一句免责声明，具体卡片仍在同一页；已完成项不留在主列表，收进「已交付」小列表并链到日志对应章节，避免主视图被历史占满。
### Ghost Changelog
- 链接：https://ghost.org/changelog/
- 类型：更新日志（卡片索引）
- 风格：编辑式卡片网格：每张卡一张宽幅题图、标题、一句摘要、日期和 New / Improved / Beta 小标签；干净、留白多、品牌感中等
- 强项：索引页只给一句话和标签，完整内容在 /changelog/<slug> 独立页；十条一页加 Load more，页面不会一次压满；标签把「新功能 / 改进 / Beta」三种性质直接写在卡面上，扫一眼就能分级。
- 不适合我们的：卡片依赖题图，纯文字项目会失去一半视觉节奏；没有「当前进度」总览，仍是按时间而不是按状态组织；Load more 是交互，静态只读页用不上。
- 契合度：medium
- 可以抄：卡片只留四样：标题、一句摘要、日期、状态标签；正文和截图都放到详情页。索引页固定只显示 6–8 张而不是全量列表，历史通过「更多」链接交给日志，让首屏始终轻。
### GitHub Status
- 链接：https://www.githubstatus.com/
- 类型：状态页
- 风格：Atlassian Statuspage 标准模板：绿/黄/红状态色、组件方格、按日期分组的事件时间线；克制、运营感、信息密度高
- 强项：顶部一条总体状态横幅（Operational / Degraded Performance / Partial Outage 等），下面组件方格一眼扫完；再往下是 90 天 uptime 和 Past Incidents，事件按日期倒序、带状态标签与 UTC 时间戳，单条详情另开页。
- 不适合我们的：面向服务可用性而非项目进度；视觉普通、模板感强；事件正文可能很长；实时数据对静态只读页是额外负担。
- 契合度：medium
- 可以抄：首屏只放一句总体状态加更新时间（如「Sprint 20 进行中 · 11-14 更新」），下面用三到六个小方格分别表示产品、冲刺、设计的状态；历史只留标题、日期、状态标签三样，详情链到日志的对应章节。
### Linear「Now」项目主页
- 链接：https://linear.app/now
- 类型：项目主页 / 内容索引
- 风格：极简编辑式：大标题、大量留白、细分隔线；层级靠字号、字重和间距而非卡片容器，链接以 → 或 ↗ 收尾，品牌色克制
- 强项：一页分了四档密度：Featured stories（大标题 + 摘要 + 作者日期）→ Changelog（四条短文，View all →）→ Press（四条外链，↗）→ Archive（TitleAuthor·Date 的密排）。所有细节都在独立页，主页只负责「选读」，越往下越轻。
- 不适合我们的：它是内容索引而非状态总览，看不到 Now/Next 的进度；条目多时页面会很长；依赖大量文章页才有意义。
- 契合度：medium
- 可以抄：用密度分层代替折叠：最重要的三到五条用大字号加一句摘要；次一级用两行列表；历史压成单行元数据。每档末尾放一个「View all / 全部 →」把细节送走，手机端顺着密度递减读下去即可。
> 设计作品社区（Dribbble/Behance）那个方向当时还没跑出来，未包含。

## 二、早期的三个缺口（Designer 点名，后来重点改成节点图）

### 2.1 A 竖屏常开（wallboard / kiosk）（3 个）

### DAKboard
- 链接：https://dakboard.com/
- 最能说明问题的一页：https://dakboard.com/c/use-cases/agile-dashboard-display/
- 类型：商业壁挂看板（SaaS）
- 许可：—
- 怎么画 / 窄屏怎么办：墙面屏只放放大的概览：阻塞数、Sprint 倒计时、velocity、站会笔记这类数字和短句，明确不放卡片正文和小字；自定义屏按目标分辨率单独排版（竖屏 1080×1920 另做一版），Loops 每 5 秒到 1 小时整屏轮播（Plus），数据块 15–30 分钟刷新。
### Grafana Playlist / Kiosk
- 链接：https://grafana.com/
- 最能说明问题的一页：https://grafana.com/docs/grafana/latest/visualizations/dashboards/create-manage-playlists/
- 类型：开源监控看板（kiosk/playlist）
- 许可：AGPL-3.0-only
- 怎么画 / 窄屏怎么办：用 playlist 把多个仪表盘按 Interval（30s、5m 等）自动逐张轮播，Kiosk 隐去菜单、导航和控件，Kiosk + auto fit panels 自动调整面板以利用整屏；24 栏网格在窄屏（约 768px 以下）折成单列纵向堆叠，电视上是整屏、手机上是长列表。
### MagicMirror²
- 链接：https://magicmirror.builders/
- 最能说明问题的一页：https://docs.magicmirror.builders/modules/configuration.html
- 类型：开源竖屏智能镜（模块化）
- 许可：MIT
- 怎么画 / 窄屏怎么办：竖屏镜面用 13 个固定区域（top_left、middle_center、bottom_bar 等）摆模块，同区模块按配置顺序从上往下堆、区域随内容伸缩，整体可用 zoom 缩放；布局不随宽度重排，换方向要在 custom.css 写媒体查询或用系统旋转，窄屏不是它的设计目标。
### 2.2 B 用图说进度（0 个）

> 当时还没跑出来，未包含。

### 2.3 C 先概括后下钻（3 个）

### Notion 折叠块（Toggle list）
- 链接：https://www.notion.com/help/writing-and-editing-basics
- 最能说明问题的一页：Basic blocks → Toggle list（Notion 无单独的 toggle 帮助页，这一页是官方说明；正文里也讲了移动端编辑的差异）
- 类型：折叠分组（accordion）
- 许可：专有（页脚仅 © Notion Labs, Inc.，无开源许可），仅作参考
- 怎么画 / 窄屏怎么办：分层：一行标题加一个三角箭头，收起时只看到概括，展开才看到里面的内容，还能一层层嵌套；窄屏：同一种原地展开，不弹层也不下钻，手机上仍是一列，长页面不会变成多层跳转。
### Jira Cloud Backlog + 工作项侧栏
- 链接：https://support.atlassian.com/jira-software-cloud/docs/customize-your-view-of-the-board-and-backlog/
- 最能说明问题的一页：Backlog settings 里的 Expand all / Collapse all 与 Epic panel；Board settings 里的 Open work items in sidebar（选中后从右侧栏打开，关掉则居中弹窗）
- 类型：侧边抽屉（drawer / peek）
- 许可：专有（页脚仅 © 2026 Atlassian，无明示开源许可），仅作参考
- 怎么画 / 窄屏怎么办：分层：Backlog 一行一条工作项、按 Epic 整组展开或收起，摘要留在列表里，点开才在右侧抽屉读详情；窄屏：抽屉变成整页（手机 App 同样），返回就回到列表。
### Sentry Issue Details（问题详情页）
- 链接：https://docs.sentry.io/product/issues/issue-details/
- 最能说明问题的一页：Issue Details 页的四个区：顶部 header、事件图、正文 event（Stack Trace / Breadcrumbs / Tags 等分区）、右侧 issue 侧栏；入口是 Issues 列表
- 类型：下钻页（drill-down）
- 许可：文档仓库 FSL-1.1-Apache-2.0（发布两年后转 Apache 2.0）；产品界面专有，仅作参考
- 怎么画 / 窄屏怎么办：分层：问题列表每行只给标题、事件数、用户数和最后出现时间，点进来才是详情页——头部摘要、正文事件、右侧元数据栏，长堆栈默认把库帧折起来，要看再展开；窄屏：四区收成一列，右栏落到正文之后，分区逐段展开。
## 三、节点图（最新重点：可折叠的项目结构图）

### 3.1 流水线与 DAG（3 个）

### GitLab CI/CD 流水线图
- 链接：https://gitlab.com/
- 最能说明问题的一页：https://docs.gitlab.com/ci/pipelines/
- 类型：CI/CD 流水线图
- 许可：MIT（社区版）
- 怎么画 / 窄屏怎么办：作业节点上直接标状态（完成打绿勾、失败标红），整条流水线另有 mini graph：按阶段分组、每段可展开，悬停显示阶段名与状态，一眼看出全绿还是有失败。点某个作业进入作业页看完整日志，可取消、重试或重跑。窄屏没有专门布局，mini graph 是最紧凑的形态，但展开后的完整作业图仍需横向滚动。
### Apache Airflow Graph 视图
- 链接：https://airflow.apache.org/
- 最能说明问题的一页：https://airflow.apache.org/docs/apache-airflow/stable/ui.html
- 类型：DAG 运行状态图
- 许可：Apache-2.0
- 怎么画 / 窄屏怎么办：Graph 视图把某次运行的任务状态直接叠在依赖结构上，节点按状态着色并带时长指示，失败一眼可辨。点任务看元数据与最近运行历史，在 Dag Run 视图里还能下钻到 Task Instance 详情。文档没有窄屏或竖屏方案，画布只能缩放平移，手机竖屏读起来吃力。
### Dagster 资产图（Asset Graph）
- 链接：https://dagster.io/
- 最能说明问题的一页：https://dagster.io/docs/guides/build/assets/metadata-and-tags/groups
- 类型：数据资产血缘图
- 许可：Apache-2.0
- 怎么画 / 窄屏怎么办：资产按组画成带标签的方框，组可嵌套；点组头就折叠成单个节点，节点上给出组内各状态的汇总计数。左侧栏把同一套层级画成可展开的树，和画布一一对应。没有移动端说明，图面横向铺开，窄屏时侧栏那棵层级树最接近可用入口。
### 3.2 可折叠树与思维导图（3 个）

### Markmap
（截图只留在本机，没入库：Markmap 首屏：Markdown 大纲变成可折叠的思维导图（浏览器实拍））
- 链接：https://markmap.js.org/
- 最能说明问题的一页：https://markmap.js.org/editor
- 类型：开源库 + 在线编辑器（Markdown 直接转思维导图）
- 许可：MIT
- 怎么画 / 窄屏怎么办：点子节点旁的圆点即可折叠、展开整条分支，可用 foldLevel 或 <!-- markmap: fold --> 让某层默认收起，也能全展开、全收起；节点本身没有状态字段，状态得写进节点文字（可带 HTML）或靠配色区分；图是 SVG，可缩放、拖动，autoFit 能让整图自动套进容器，窄屏就靠自适应缩放加平移。
### jsMind
- 链接：https://github.com/hizzgdev/jsmind
- 最能说明问题的一页：https://hizzgdev.github.io/jsmind/example/2_features.html
- 类型：开源 JavaScript 思维导图库
- 许可：BSD-3-Clause
- 怎么画 / 窄屏怎么办：节点旁有 +/− 角标，点一下折叠或展开，可设成显示子节点数，API 有 toggle_node、expand_node、collapse_node、expand_to_depth；本身不带状态，用 custom_node_render 自己往节点里画状态徽章；窄屏可缩到 0.5 倍、拖动画布平移，node_overflow 可让长文字换行。
### React Flow（Expand and Collapse 示例）
- 链接：https://reactflow.dev/
- 最能说明问题的一页：https://reactflow.dev/examples/layout/expand-collapse
- 类型：商业 React 流程图组件库的官方示例
- 许可：xyflow Pro License（付费，示例标为 Pro）
- 怎么画 / 窄屏怎么办：点带子节点的节点就收起或展开它的全部后代，只渲染可见节点并用 dagre 自动重排，展开状态记在 node.data 里；示例没有状态徽章，但节点是自定义组件，可以自己加；画布自带缩放、平移和 fitView，窄屏要自己设计纵向布局。
### 3.3 依赖图（3 个）

### npmgraph
（截图只留在本机，没入库：npmgraph：express 的依赖图，右侧是可折叠的报告栏（浏览器实拍））
- 链接：https://npmgraph.js.org/
- 最能说明问题的一页：https://npmgraph.js.org/?q=send#color=moduleType
- 类型：开源 Web 应用
- 许可：MIT
- 怎么画 / 窄屏怎么办：npm 依赖图画布加一个 inspector 面板：选中某个模块时，面板自动切到 module 标签显示该模块详情；节点可按 moduleType、bus factor、outdated 上色，也可用 select 高亮一组模块；官方未写窄屏规则，图与 inspector 目前是左右分栏。
### Snyk 依赖树（Dependencies 标签页）
- 链接：https://snyk.io/
- 最能说明问题的一页：https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-projects/view-project-issues-fixes-and-dependencies
- 类型：商业 SaaS
- 许可：专有（商业 SaaS）
- 怎么画 / 窄屏怎么办：依赖以可展开的列表树呈现，每条依赖标题前用 Critical/High/Medium/Low 严重度图标上色并显示最高分；滚动到依赖即列出其下逐条 issue，Show more detail 打开漏洞库详情；左侧筛选栏加主区列表，窄屏行为未文档化。
### Obsidian Graph view
- 链接：https://obsidian.md/
- 最能说明问题的一页：https://help.obsidian.md/plugins/graph
- 类型：商业桌面/移动应用
- 许可：专有（闭源，个人与商用免费）
- 怎么画 / 窄屏怎么办：节点按 Groups 里的搜索查询分组上色（先匹配先得），可当状态图例用；点节点直接打开对应笔记、右键出菜单；帮助页标了 mobile: true，手机端可用，但官方未写窄屏布局细节。
### 3.4 核实记录（7 条）

### 核实：Nx Graph（保留；链接可开）
- 链接：https://nx.dev
- 实际看到：target 页 https://nx.dev/features/explore-graph 可打开：页面确认同一文件夹的项目聚成「composite node」，可原地展开或聚焦，侧栏有 group by folder、搜索与手动隐藏，右下浮动按钮导出 .png，点节点弹出带项目详情链接的 tooltip；确实没有状态配色和窄屏/移动适配的字样。
- 修正/判断：参考属实，但它是桌面端的项目依赖图，不是「产品为根」的层级树，也没有节点状态；可借鉴的正是 composite node 的原地展开/聚焦，加上按文件夹分组、搜索与隐藏这几个交互。状态配色、点开出总结和竖屏 9:16 常开都得由我们自己设计，别把它当成这三点的先例。
### 核实：GitLab CI/CD 流水线图（保留；链接可开）
- 链接：https://docs.gitlab.com/ci/pipelines/
- 实际看到：文档「Pipeline mini graphs」一节原文可逐字对上：mini graph「always groups jobs by stage」「Stages in pipeline mini graphs are expandable」「Hover your mouse over each stage to see the name and status, and select a stage to expand its jobs list」「take less space and can tell you at a quick glance if all jobs passed or something failed」；流水线详情页「displays a graph of all the jobs in the pipeline」，并可「cancel a running pipeline, retry failed jobs」。但「点作业进入作业页看完整日志」「窄屏无专门布局、展开后需横向滚动」在该页均无文字；「完成打绿勾」只出现在示例图的替代文本（"First three stages show completed jobs with green checkmarks"），没有正式说明。
- 修正/判断：核心机制与「可折叠项目结构图：产品为根、节点带状态、点开出总结」吻合，可直接引用：节点带状态、按阶段分组、每段可展开、悬停显示阶段名与状态、mini graph 刻意省空间用于「一眼看全绿还是有失败」，且取消/重试就在流水线页完成——这支持「紧凑状态树可常驻、按需展开」的思路。需修正三处：①「点作业进作业页看完整日志」依赖产品行为，该页未写，引用时只能算合理推断；②窄屏布局与横向滚动同样无据，页面只说 mini graph「take less space」，不要写成文档结论；③形态别混淆——文档描述的是流水线详情页的横向作业图加散布在各处的 mini graph，不是竖屏 9:16 常开的竖向结构图；mini graph 常驻于提交/流水线列表这一点可借，「9:16 竖屏」在 GitLab 没有对应依据，是我们的设计取舍。
### 核实：Dagster 资产图（Asset Graph）（保留；链接可开）
- 链接：https://dagster.io/docs/guides/build/assets/metadata-and-tags/groups
- 实际看到：target_page 真实存在（标题 "Groups | Dagster Docs"，含 Assigning a group / Nested groups / Groups in the UI 三节），原文逐句确认：资产组画成带标签的方框（"Each group is drawn as a labeled box around its assets"），嵌套组是父组框里再套一个框（"a box inside its parent's box"）；点组头折叠成单个节点并显示组内状态汇总计数（"Clicking a group's header collapses it into a single node showing rolled-up status counts for everything inside, including any nested groups"）；侧栏把同一层级画成可展开的树（"The sidebar renders the same hierarchy as an expandable tree."）。全页无 "mobile"/"responsive" 字样，也未说侧栏与画布一一对应；另经 WebSearch 交叉核实该页确为 Dagster 官方文档。
- 修正/判断：参考价值成立，可保留：它是「可折叠项目结构图」的成熟先例——分组节点折叠后给出组内状态汇总计数，侧栏用同层级树做入口，与「产品为根、节点带状态、点开出总结」在交互上同构。但需修正两点：① 原文只说侧栏是「同一层级」（same hierarchy），没有说与画布一一对应，原说法属推断，应弱化；② 原文完全没提窄屏/移动端，Dagster 是桌面 Web 的横向资产图画布，与「竖屏 9:16 常开」形态不同——「窄屏时侧栏树最接近可用入口」只是合理推断，不能当作出处，引用时勿用它支撑移动端做法。
### 核实：Kiali（保留；链接可开）
- 链接：https://github.com/kiali/kiali
- 实际看到：target_page 真实可打开。原文：节点边按请求健康度着色（"A node colored red or orange might need attention"；"The color of an edge ... represents the health of the requests"），单击选中节点后由 "The collapsible side-panel summarizes the current graph selection"，其中含 Charts（流量与响应时间）、Health、Links to fully-detailed pages；"The health of nodes and edges is refreshed automatically"、"The graph can also be paused"、"Graph replay allows you to replay traffic from a selected past time-period"。但 kiosk 不在 target_page 上，见仓库 README（raw README.adoc）："To enable Kiosk mode, simply add a `kiosk=<platform_id>` URL parameter"，"the main header and navigation bar are not displayed"，示例 `/graph/namespaces?namespaces=bookinfo&kiosk=console`。该页通篇未提屏幕尺寸、响应式或窄屏布局；原文只写红/橙，未逐字列绿。
- 修正/判断：对照「可折叠项目结构图：产品为根、节点带状态、点开出总结、竖屏 9:16 常开」：四点里三点有据——节点（和边）带健康状态色、单击节点由可折叠侧栏汇总图表/健康/明细链接、靠 kiosk 参数隐藏头部与导航栏后嵌入大屏/iframe，另有自动刷新与暂停、回放可借。不支持的两点要写明：一是形态是服务网格拓扑图，不是「产品为根」的单根层级树，根节点与树形收折它证明不了；二是它是桌面控制台，全站未见窄屏或竖屏适配，对 9:16 常开只能作反例参考（要另设布局，不能照抄）。价值：作为「状态着色节点 + 点开→可折叠侧栏总结 + kiosk 嵌入常开」的实证参考成立，可保留；引用时把 kiosk 出处标到仓库 README 的 Embedding 节，不标 target_page。
### 核实：Apache Airflow Graph 视图（保留；链接可开）
- 链接：https://airflow.apache.org/docs/apache-airflow/stable/ui.html
- 实际看到：target_page 可打开（HTTP 200，约 150 KB）。页面两处 Graph View 原文：Dag Run 的「Shows the Dag's task dependency structure overlaid with the status of each task in this specific run」「Each node includes a visual indicator of task duration」；Dag 页的「Each node represents a task. Edges show the dependencies between them. You can click any task to view its metadata and recent run history」；Task Instance View 的「When you click on a specific task from the Dag Run view, you're brought to the Task Instance View」。全文检索 mobile / responsive / narrow / portrait / zoom / pan / screen size 均零命中，只有一条浏览器版本兼容提示。
- 修正/判断：参考真实，主体准确，但三点要收窄：① 文档只说 Graph 视图把「状态叠加在依赖结构上」并列举 success / failed / upstream failed，「节点按状态着色」是 UI 的实际实现，文档没明写颜色；② 「画布只能缩放平移」文档里查不到（无 zoom / pan 字样），只能当实际使用观察，不能引作文档依据；③ 对照「可折叠项目结构图：产品为根、节点带状态、点开出总结、竖屏 9:16 常开」——Airflow Graph 是依赖 DAG，不是可折叠层级树、没有产品根节点、点节点是跳转到 Task Instance 页而非就地展开总结，也没有任何窄屏/竖屏方案，所以它是「节点带状态 + 点开看详情」的旁证，同时恰好是竖屏 9:16 常开要避开的反例（桌面画布、靠缩放平移），价值在于佐证问题与反差，不能直接照搬为原型。
### 核实：XMind（保留；链接可开）
- 链接：https://xmind.com/user-guide/fold-unfold-subtopic-new
- 实际看到：目标页可正常打开，原文明确写 "Hover over a topic to see a button, click on it to fold the subtopics."、"the number of the sub-topics will be displayed right beside the main topic"、"you can unfold them by directly clicking on the number."，并说明选中中心主题后可右键或用 Edit 菜单做 Fold/Unfold all Sub-Branches（带快捷键）。另查 xmind.com/user-guide/marker-new：内置 marker 含 priority、task progress 组，用来在主题上显示优先级/进度/任务状态；官网首页写 "Works on web, desktop, and mobile."
- 修正/判断：折叠相关的四条全部属实：悬停出按钮、右键/快捷键、折叠旁标隐藏子主题数、点数字展开、一键全折叠/全展开。节点状态也属实：Task Progress、优先级等标记直接显示在主题节点上，正是「节点带状态」的好样式参考。需修正两处：① 手机端「捏合缩放、拖动画布」在 XMind 官方文档中查不到，官网只写三端都有 App；这半句应删去或降为「有手机 App 可浏览整图（手势未获官方文档确认）」。② 「点开出总结」与 XMind 不符——点数字展开的是被折叠的子主题，不是生成总结，XMind 的 Summary（概要）是另一个功能，引用时别混。另需注意 XMind 是通用思维导图（居中根主题、放射/树形布局），与「产品为根、竖屏 9:16 常开的项目结构图」不完全同构：它适合作为折叠计数徽标和节点状态 marker 的交互/样式参考，不宜当作竖屏布局参考。
### 核实：Logseq（保留；链接可开）
- 链接：https://logseq.com/
- 实际看到：Tasks.md 确实写了两套状态流（默认 LATER→NOW→DONE，或 TODO→DOING→DONE）、/A /B /C 优先级与 /Deadline /Scheduled 日期，示例显示为行内样式标签；官方 Start here 页写明「Logseq is an outliner. Each bullet is a block」，且 iOS/Android 都有官方 App。但目标页本身没讲点圆点折叠和移动端布局，这两点属于产品事实而非该页内容。
- 修正/判断：作为「可折叠项目结构图」的大纲先例有价值：单列竖排、点圆点/箭头折叠整棵子树、节点带状态/优先级/日期行内标签、移动端竖屏原生。但它是笔记大纲编辑器而非以产品为根的节点图，「点开」最接近的是 zoom 进块看内容、不是弹出总结卡；手机端另有自己的移动 UI，不能据此说「窄屏无需额外适配」。保留折叠树+节点状态两点，其余弱化。
