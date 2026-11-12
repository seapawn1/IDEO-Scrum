#!/usr/bin/env python3
"""Loading smoke: each of the four role commands, twice, with a neutral prompt."""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

ROLES = ("scrum-master", "designer", "developer", "stakeholder")
PROMPT = "跟我说说你能帮我做什么。"
ENV_DROP = ("CLAUDE_CODE_HOST_AUTH_ENV_VAR", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST", "ANTHROPIC_BASE_URL")


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    plugin = args.plugin.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if k not in ENV_DROP}
    results = []
    for role in ROLES:
        for n in (1, 2):
            project = out / "projects" / f"{role}-{n}"
            project.mkdir(parents=True, exist_ok=True)
            target = out / f"{role}-{n}.jsonl"
            command = [
                "claude", "-p", f"/ideo-scrum:{role} {PROMPT}", "--model", "haiku",
                "--plugin-dir", str(plugin),
                "--allowedTools", "Read", "Grep", "Glob", "Skill",
                "--disallowedTools", "Bash", "PowerShell", "Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch", "Task",
                "--strict-mcp-config", "--no-session-persistence",
                "--output-format", "stream-json", "--verbose",
            ]
            print(f"loading smoke {role} #{n}", flush=True)
            with target.open("wb") as handle:
                subprocess.run(command, cwd=project, env=dict(env, TEMP=str(project), TMP=str(project)), stdout=handle, stderr=subprocess.STDOUT, check=False)
            skills = []
            for line in target.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                if o.get("type") == "assistant":
                    for block in (o.get("message") or {}).get("content") or []:
                        if block.get("type") == "tool_use" and block.get("name") == "Skill":
                            skills.append((block.get("input") or {}).get("skill", "?"))
            ok = "ideo-kernel" in skills and "scrum-kernel" in skills and "design-kernel" not in skills and "sprint-kernel" not in skills
            results.append({"role": role, "n": n, "skills": skills, "ok": ok})
    print(json.dumps(results, ensure_ascii=False, indent=2))
    ok_count = sum(1 for r in results if r["ok"])
    print(f"loading smoke: {ok_count}/8")


if __name__ == "__main__":
    main()
