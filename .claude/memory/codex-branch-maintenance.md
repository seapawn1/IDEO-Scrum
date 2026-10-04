---
name: codex-branch-maintenance
description: codex 分支=与 main 并列的分发维护分支；角色载体为原生 skill（$ 调用，模板路线已废弃）；同步与校验流程
metadata:
  node_type: memory
  type: project
  originSessionId: 0c2606bb-29eb-4a3c-b74e-868c157a2e8b
  modified: 2026-10-04T10:47:08.932Z
---

**事实**：仓库 `codex` 分支是与 main 并列的维护分支，承载 Codex CLI 分发包（`codex/plugins/ideo-scrum/`；仓库根 `.agents/plugins/marketplace.json` 指向它，安装 `--ref codex`）。角色载体＝**原生 skill**：`$scrum-master` / `$designer` / `$developer` / `$stakeholder`，各带 `agents/openai.yaml`（`policy.allow_implicit_invocation: false`，显式调用、不自动介入）。**AGENTS.md 模板路线已废弃**（templates/ 已删）——勿再提恢复。Codex 无 command 机制，角色只能走 skill。

**Why:** 2026-10-04 会话 PO 定案「直接转成 codex 可用的方案，然后消除之前的决策」；同日发现 `~/.codex` 有原生 skills 目录与 `codex plugin` 体系，据此完成转换。

**How to apply:** 同步流程＝`git switch codex` → `git merge main`（根 README 常冲突，取并集）→ skills 全量镜像 + 四份角色 skill 用生成脚本从 `plugins/ideo-scrum/commands/*.md` 重生成 → 跑 Codex 原生校验 `python ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py codex/plugins/ideo-scrum` → 提交（不 push，随发版）。升级用户侧＝推送后 `codex plugin marketplace add seapawn1/IDEO-Scrum --ref codex` 重装。相关：[[plugin-guidance-vs-operational-content]]
