# PBI-68 看板：同类看板参考（Designer 找的 10 个）

> 2026-11-14，PBI-68 看板的设计冲刺（PO 叫停）里找的同类看板。只有文字和链接：别人的网页截图和对照页涉及版权，只留在当时那台机器上，没入库。Stakeholder 另做的调研见 `PBI-68-board-research.md`。

PO 看完对照页，最喜欢第 2 个（GitHub Actions 流水线图），因为它能折叠；他说如果别人比他的想法好，可以直接照搬——照搬版式没问题，搬代码或素材先看许可并登记到 ATTRIBUTION.md，AGPL 的不行。

## 1. 爬山图（Basecamp Hill Chart）（用图说进度）

- 它怎么做：每个待办清单是山坡上的一个点：左坡是「想办法」，右坡是「落地」。点的位置由人拖动，每次更新存成快照。
- 对我们：用一幅画说「做到哪一步」，比百分比直观。我的想法：Sprint 的五个阶段落在山坡上（Why、What、How 在左坡，Increment、Test 在右坡），位置取自 Now 行。
- 留意：Basecamp 里位置是人判断的，不是算的；我们的日志里没有这个字段，只能用日志里写着的阶段。
- 链接：[hill chart 介绍](https://basecamp.com/hill-charts)；[Shape Up：Show Progress](https://basecamp.com/shapeup/3.4-chapter-13)

## 2. 流水线图（GitHub Actions）（用图说进度）

- 它怎么做：每个任务一个方块，图标是状态，线是依赖。一组任务折成「3/3 jobs are completed」，点「Show all jobs」展开；点任务看日志。
- 对我们：最像「架构图加状态」：节点是步骤，亮的是正在动的；折叠、展开，就是你说的「能点开、能缩小」。
- 留意：它横向画；竖屏要改成竖着排。
- 链接：[官方说明](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-the-visualization-graph)

## 3. 地铁线路图式路线图（用图说进度）

- 它怎么做：一条条线是工作流，站是里程碑，线交汇处是依赖。
- 对我们：架构图缩成一条线，条目钉在站上；竖着排，正好适合竖屏。
- 留意：这个例子是付费的 PPT 模板，只看样子；做成真的要自己画。
- 链接：[SlideUplift 模板页](https://slideuplift.com/powerpoint-templates/subway-timeline-powerpoint-template/)

## 4. 状态页（GitHub Status）（一眼的状态）

- 它怎么做：一切正常时安静，有事才出现黄色横幅；下面每个组件一行：对勾加 90 天的小竖条。
- 对我们：「平时安静，有事才响」。第 1 版正好反过来，最响的是「没有」。
- 留意：它说的是「系统好不好」；我们要说的是「做到哪、等谁」。
- 链接：[GitHub Status](https://www.githubstatus.com/)

## 5. 壁板（Geckoboard）（一眼的状态）

- 它怎么做：深色底、大数字、小图，只放几个关键指标；它的原则是几秒读懂、隔着房间也看得清、实时更新。
- 对我们：竖屏常开的参照：字大、东西少、不用点。Klipfolio 说竖屏适合指标多的长看板，常开用显示器比平板稳（平板会自动熄屏）。
- 留意：它的内容是数字（销售、客服）；我们的是条目和阶段。
- 链接：[Geckoboard 例子库](https://www.geckoboard.com/dashboard-examples/)；[Klipfolio：电视、浏览器还是手机](https://www.klipfolio.com/blog/dashboard-display)

## 6. 壁挂面板（Home Assistant）（一眼的状态）

- 它怎么做：智能家居的壁挂屏：大块、深色、一点就开。作者说：墙上的看板和手机上的是两回事，几米外要读得清，一点就能操作，没人看的时候也要好看。另有「平面图」一类：画一张房子，灯亮了房间就亮，图本身就是状态。
- 对我们：竖屏常开的参照；平面图是「图即看板」的极端。
- 留意：内容是智能家居；平面图的例子在 Reddit 上，我没截图。
- 链接：[14 个例子](https://lazyadmin.nl/smart-home/home-assistant-dashboard-examples/)；[ha-floorplan](https://experiencelovelace.github.io/ha-floorplan/)

## 7. 现在 / 接下来 / 以后（Now-Next-Later）（条目怎么排）

- 它怎么做：三列；越往后越不确定、细节越少（Product Talk 的示例里，确定度从「现在」往「以后」递减）。
- 对我们：这是你的「主线、副线、以后」的另一种说法；列的深浅可以表示远近。
- 留意：很常见，容易显得「像模板」。
- 链接：[Product Talk](https://www.producttalk.org/product-roadmaps/)；[Hustle Badger：16 个真实路线图](https://www.hustlebadger.com/what-do-product-teams-do/product-roadmap-examples/)

## 8. 表格 / 看板 / 路线图（GitHub Projects，Linear）（条目怎么排）

- 它怎么做：同一批条目有三种看法：表格、看板（按状态分列）、路线图（时间线）。Linear 的看板还能加泳道，泳道能折叠。
- 对我们：「同一份数据，多种看法」；你的三段论里的「条目」，可以借看板或路线图的画法。
- 留意：条目少的时候，看板的列会空。
- 链接：[GitHub Projects 的三种布局](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view)；[Linear 的看板布局](https://linear.app/docs/board-layout)

## 9. Linear（做工的质感）

- 它怎么做：深色、克制，字当主角：大标题加一块产品截图。
- 对我们：你嫌第 1 版「做得一般」，这类是「做得不一般」的参照。
- 留意：它是工具，不是看板；这种风格学的人很多。
- 链接：[linear.app](https://linear.app/)

## 10. Glance（自托管仪表盘）（做工的质感）

- 它怎么做：一页多栏的小组件（日历、RSS、天气、行情……），深色、字紧凑；手机上变成单列。
- 对我们：多栏收成单列的做法。
- 留意：AGPL-3.0：不能把它的代码拷进 MIT 的插件。
- 链接：[GitHub](https://github.com/glanceapp/glance)

## 模式小结（Designer 的读法）

- 用图说进度有三种画法：位置（爬山图）、带状态的节点图（流水线图，可折叠）、线路图（站点）。
- 常开屏的共同点：东西少、字大、不用点、几秒读懂；常开用显示器比平板稳（Klipfolio 的文章），竖屏适合指标多的长看板。
- 条目的排法两条主路：按状态分列（看板）、按远近分列（Now-Next-Later）；越往后越简略。
- 状态页是「平时安静、有事才响」；第 1 版看板正相反（最响的是「没有」）。
- 看的这 10 个里，没有哪一个同时做到「承诺、带状态的图、条目」三段；这三段要自己拼。
