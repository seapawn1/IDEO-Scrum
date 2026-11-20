# Maintaining IDEO-Scrum

This guide is for maintainers of the IDEO-Scrum repository across Claude Code and DeepSeek Harness (DSH). If you are using the plugin to run a project Sprint or design, read [Quick start](quick-start.md), the [README](../README.md), and the [Glossary](glossary.md) instead. ([中文](maintaining.zh-CN.md))

> **Review draft status (Sprint 25, `0.6.3` candidate).** Statements about host internals cite pinned upstream source code (`dsh-v0.2.2-rc.5`); historical notes (`v6.0.3` and `b2679aa`) are baselines only. Live `0.6.3` installation, `6.0.3 → 0.6.3` migration, and runtime instruction/commitment checks await Test authorization and are not yet recorded as confirmed user guidance.

## Two hosts, one source

`plugins/ideo-scrum/` holds the single canonical methodology source for both hosts. There is no generated DSH copy and no sync script.

| Piece | Claude Code | DeepSeek Harness (DSH) |
| --- | --- | --- |
| Roles and kernels (`plugins/ideo-scrum/commands/`, `plugins/ideo-scrum/skills/`) | Loaded through [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) (`./plugins/ideo-scrum`) and [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) | Registered at runtime by [`dsh/index.js`](../dsh/index.js) directly from `plugins/ideo-scrum/` |
| Commitments context | [`hooks.json`](../plugins/ideo-scrum/hooks/hooks.json) runs [`commitments.sh`](../plugins/ideo-scrum/hooks/commitments.sh) via POSIX `sh` on `SessionStart` and `UserPromptSubmit` | [`dsh/index.js`](../dsh/index.js) registers `systemPrompt.context` (`ideo-scrum:commitments`, `order: 130`, `interpolate: false`) via [`dsh/commitments.js`](../dsh/commitments.js) |
| Packaging and metadata | [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json) and [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) | [`package.json`](../package.json) (`@seapawn/ideo-scrum`), [`cordis.patch.yml`](../cordis.patch.yml), [`dsh/locale/en.json`](../dsh/locale/en.json), [`dsh/locale/zh.json`](../dsh/locale/zh.json), and `plugins/ideo-scrum/icon.png` |

- **Role and kernel registration (`dsh/index.js`)**: strips YAML frontmatter (requiring one double-quoted JSON-compatible `description` line, plus matching `name` on `SKILL.md`), registers the four kernels and four user-invocable roles (`/scrum-master`, `/developer`, `/designer`, `/stakeholder`, without the `ideo-scrum:` prefix), prepends the DSH tool-mapping and routing prelude, and preloads `ideo-kernel` then `scrum-kernel` verbatim before each role body while keeping `sprint-kernel` and `design-kernel` on demand.
- **Bundle whitelist (`package.json`)**: `files` includes only `cordis.patch.yml`, `dsh/`, `ATTRIBUTION.md`, `plugins/ideo-scrum/commands/`, `plugins/ideo-scrum/skills/`, and `plugins/ideo-scrum/icon.png` (excluding `hooks/` and `.claude-plugin/`), has no `dependencies` or `scripts`, and sets `engines.dsh` to `>=0.2.2-rc.5 <0.3.0`.
- **Commitments adapter (`dsh/commitments.js`)**: reads the `Commitment` (`承诺`) row under the matching heading ([`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md), convention 17) inside the nearest `.git` root, ignores symlinked `scrum/` directories, reports counts when multiple Sprints or designs are open, and honors `IDEO_SCRUM_COMMITMENTS=off`; host compaction replay relies on DSH's named `runtime-context` handling, while live post-compact `0.6.3` checks remain pending Test.

## Where repository rules load from

[`AGENTS.md`](../AGENTS.md) is the single shared repository rule file. [`CLAUDE.md`](../CLAUDE.md) contains only `@AGENTS.md` — a one-way import with no circular `@CLAUDE.md` reference inside `AGENTS.md`. Maintainers update `AGENTS.md` only; `CLAUDE.md` is changed only by a session directly authorized by the Product Owner.

- **Claude Code**: loads `CLAUDE.md` and imports `@AGENTS.md` (isolated `/context all` verification for `0.6.3` test sessions is part of the Test checklist).
- **DSH `0.2.2-rc.5` (pinned upstream source vs. live verification)**: commit `9c2670d3bce5275e0d1610272958121af87787bb` shows that `dsh-base` enables the instruction loader by default, reads `AGENTS.md` and `CLAUDE.md` from `.git` root to working directory while deduplicating identical text per directory ([`agent-instructions/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L30-L42), [`config.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/src/config.ts#L11-L46)), and does **not** expand `@path` imports ([`README.md#L223-L224`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/context/agent-instructions/README.md#L223-L224)) — so DSH reads `AGENTS.md` directly rather than via `CLAUDE.md`. Live Web and Standard verification showing `AGENTS.md` loaded on the first turn without duplication or parent-directory leakage is still pending Sprint 25 Test.
- **Project-level Agents vs. named presets (unverified)**: upstream `dsh-v0.2.2-rc.5` supports Cordis named preset registration ([`agent-preset/src/index.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/preset/agent-preset/src/index.ts#L11-L29)) and constrained in-process subagent preset selection ([`tool-subagent/README.md`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/subagent/tool-subagent/README.md#L50-L71)), which does **not** establish automatic discovery of project-level Agent files and is unrelated to `.agents/skills` or `/stakeholder`. Project-level Agent support in DSH remains unverified and is outside this bundle.

## Migrating an existing installation

Moving from `6.0.3` to `0.6.3` lowers the SemVer version number (`6.0.3` > `0.6.3`), and **neither host's downgrade migration path has been run in Sprint 25 live Test yet**. Verified user-facing migration instructions will be published in the [README](../README.md#upgrade) and [Quick start](quick-start.md) only after live isolated Test passes; in user docs, keep the DSH host version (`0.2.2-rc.5`) in the [install instructions](../README.md#install) explicitly distinct from the plugin version (`0.6.3`).

| Host | Previous baseline | Upgrade nuance and what live Test must confirm |
| --- | --- | --- |
| Claude Code | `v6.0.3` (`d681c69`), marketplace install from `./plugins/ideo-scrum` via the [version cache](https://code.claude.com/docs/en/plugins/loading#versions-and-updates) | Confirm whether `claude plugin update ideo-scrum@ideo-scrum` accepts a SemVer downgrade or needs a clean fallback (such as uninstall and reinstall); check the active version-cache path, `claude plugin list`, role invocation, commitment hooks, and untouched `scrum/` logs. |
| DSH (`0.2.2-rc.5`) | Local directory link to commit `b2679aa` (`@seapawn/ideo-scrum`, `private: true`, not a public registry release) | Upstream [`versions.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/boot/plugin-manager/src/versions.ts#L32-L48) only lists higher registry SemVer versions and does not settle what a linked local checkout loads after restart; test updating in place plus restart versus **Uninstall** plus **Add plugin**, then verify `0.6.3` in a **new Standard session** via native events and untouched `scrum/` logs. |

- **Do not conflate the two baselines**: Claude Code had a public `v6.0.3` git tag and marketplace release, whereas DSH `b2679aa` was only a linked local repository checkout (not an earlier public npm or registry package).
- **Verify the actual loaded source and version**: inspect the active Claude version-cache directory or DSH's linked checkout path plus native session events, rather than checking `package.json` or `plugin.json` on disk or asking the model what version it thinks is loaded. In DSH, always open a new **Standard** session after restarting DSH because Minimal sessions do not mount the skill loader and an existing session can retain prior context.
- **Confirm project logs survive unchanged**: verify `scrum/ProductBacklog.md` and any open `scrum/sprint-*/SprintBacklog.md` or `scrum/design-*/DesignBacklog.md` files before and after migration.

## Checking a candidate

Keep `plugins/ideo-scrum/.claude-plugin/plugin.json` and [`package.json`](../package.json) on the same candidate version (`0.6.3`), keep both README top lines in sync with [`plugin.json`](../plugins/ideo-scrum/.claude-plugin/plugin.json), keep [`CHANGELOG.md`](../CHANGELOG.md) `## [Unreleased]` separate from published tag history (never rewrite shipped release notes or treat a version bump as a release), commit content changes and version bumps separately, and wait for Product Owner authorization before tagging, merging, or pushing.

```sh
claude plugin validate --strict plugins/ideo-scrum
node --test scripts/check_dsh.mjs
npm pack --dry-run --json --ignore-scripts
python -X utf8 -I scripts/check_docs.py
python -X utf8 -I scripts/check_docs.py --selftest
python -X utf8 -I scripts/board_check/check.py selftest
```

- **Static and packaging checks do not prove runtime host behavior**: `claude plugin validate --strict`, [`check_dsh.mjs`](../scripts/check_dsh.mjs), `npm pack --dry-run`, [`check_docs.py`](../scripts/check_docs.py), and [`board_check/check.py`](../scripts/board_check/check.py) verify manifests, adapter registration, tarball whitelist, bilingual doc parity, and board checks without replacing live host tests. Note: add `docs/maintaining.md` and `docs/maintaining.zh-CN.md` to `PAIRS` in [`check_docs.py`](../scripts/check_docs.py) when finalizing user-doc integration.
- **Live isolation rules ([`headless-testing.md`](../scrum/documents/headless-testing.md))**: run in a neutral directory with zero ancestor instruction files (verified with `/context all` in Claude Code), separate non-reused `CLAUDE_CONFIG_DIR`, `DSH_HOME`, and `DSH_AGENTS_HOME` ([`home-paths`](https://github.com/deepseek-ai/deepseek-harness/blob/9c2670d3bce5275e0d1610272958121af87787bb/packages/util/home-paths/src/index.ts#L127-L152)), a Git marketplace version-cache fixture for Claude Code (never `--plugin-dir` or a directory marketplace for migration), and persistent-checkout Web installation plus a Standard session for DSH (do not substitute `dsh --profile headless` for Web/Standard); keep raw session logs outside the repository and redact credentials or provider settings.
- **Live evidence gate**: record host version, actual loaded cache or link path, role invocation, native hook / `skill-invocation` / `runtime-context` (`ideo-scrum:commitments`) events, distinct `AGENTS.md` marker load proof, and unchanged project logs; reject model self-report, disk presence, or command list presence as proof.
- **Related maintainer files**: [`AGENTS.md`](../AGENTS.md) (shared repository rules), [`overview.md`](../plugins/ideo-scrum/skills/scrum-kernel/overview.md) (process overview and departures), [`board-log.md`](../plugins/ideo-scrum/skills/scrum-kernel/conventions/board-log.md) (board conventions), and [`ATTRIBUTION.md`](../ATTRIBUTION.md) (third-party source terms).
