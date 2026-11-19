# Sprint Backlog — Sprint 22 (project-agents)

> Started: 2026-11-19 | Closes when the Sprint Goal is met or the Product Owner stops the Sprint | Branch: `claude/sprint-22-project-agents-b09bf1` | Product Owner: SeaPawn | Scrum Master: 项目 Scrum Master | Developer: Sprint 22 Developer
> Now: Why 草案；PO 同意并行准备 Sprint 22（「可以的，没问题，下面准备22吧」），尚未确认本期目标。
> Waiting for PO: 1. 确认 Sprint Goal 与 DoD 核验重点？; 2. Why 定稿后是否放行进入 What？
> How to write this log: [Sprint log conventions](../../plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md).

## 1. Why

### 1.1 Sprint Goal

| 草案（待 PO 确认） | 独立的第二视角：拍板前能请参谋复核方案，也能按本项目的角色卡听取 Stakeholder 的反馈；身份不用每次重讲，意见每次独立，决定仍由 PO 来做。 |
| --- | --- |

这一步服务于[产品化](../ProductBacklog.md#12-product-goal)：让用户不用借作者的项目配置，也能在自己的项目里拿到独立反馈、继续走流程。

### 1.2 Definition of Done

[产品日志 §1.3 的完整 DoD](../ProductBacklog.md#13-definition-of-done) 全部生效。Outcome Done 仍衡量产品给用户带来的价值；下表只列本期建议重点核验的 Output Done，未列项不豁免。

| 核验重点（草案） | 本期看什么 |
| --- | --- |
| 内容忠实 | 角色职责和方法依据不走样；新增或改动的方法论说明有出处和依据。 |
| 可导航、无死链 | 产品日志、角色和文档入口的相关引用能打开；从 `SKILL.md` 到任意 reference 仍不超过两跳。 |
| Claude 插件校验 | `claude plugin validate --strict plugins/ideo-scrum` 通过。 |
| DSH 既有回归 | `node --test scripts/check_dsh.mjs` 通过；这不代表 DSH 支持项目 Agent，等价能力待查。若改分发，另验实际安装和角色入口。 |

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |

### 2.2 Refinement

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |

**Key choices**

**Risks and open points**

## 4. Increment notes

## 5. Test
