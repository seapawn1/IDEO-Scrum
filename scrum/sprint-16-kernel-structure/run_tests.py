#!/usr/bin/env python3
"""Run the Sprint 16 trigger tests headlessly: 7 questions x 2 paths x N runs."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

QUESTIONS = {
    1: ("我在做一个帮人整理读书笔记的命令行小工具，产品日志已经写好了。现在要开一个新的 Sprint，把它往前推一步。这个 Sprint 从头到尾会怎么走？每一段做完以后，由谁来决定能不能往下走？", "scrum-master"),
    2: ("Sprint 里精化做到一半，碰到一个问题：这个读书笔记工具的用户到底是谁，对他们来说怎样才算好用，我们自己说不清，手上的资料里也没有现成的答案。这时候该怎么办？这个 Sprint 接下来怎么走？", "scrum-master"),
    3: ("我有个想法：给一家社区图书馆做一个帮读者找书的工具。现在手上只有这一句话，没有产品日志，也不知道读者具体要什么。我想把这件事正式做起来，第一步该做什么？", "scrum-master"),
    4: ("设计走到构思这一步了：挑战、设计目标、设计问题和地图都写进日志了，PO 也选出了要解决的那个问题。接下来怎么得到方案？谁来做，各自怎么做，最后怎么选？", "designer"),
    5: ("这个 Sprint 的 Sprint Goal 已经达成，PO 说可以收官了。收官要做哪些事？冲刺日志怎么处理？这个 Sprint 学到的教训记在哪里？", "developer"),
    6: ("我们项目的产品日志要重写一遍：产品是什么、Product Goal 怎么写、待办事项怎么列，还有这些该由谁来决定。这份日志应该写成什么样？", "scrum-master"),
    7: ("项目要开下一个 Sprint 了，我们准备把冲刺日志建起来。这个日志放在哪里、叫什么名字？里面要有哪几章？开头要写些什么？", "developer"),
}

ENV_DROP = ("CLAUDE_CODE_HOST_AUTH_ENV_VAR", "CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST", "ANTHROPIC_BASE_URL")
TOOLS_ALLOWED = ["--allowedTools", "Read", "Grep", "Glob", "Skill"]
TOOLS_DENIED = ["--disallowedTools", "Bash", "PowerShell", "Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch", "Task"]


def run(plugin: Path, out: Path, runs: int, questions: list[int]) -> None:
    env = {k: v for k, v in os.environ.items() if k not in ENV_DROP}
    for q in questions:
        text, role = QUESTIONS[q]
        for path_no, prompt in ((1, text), (2, f"/ideo-scrum:{role} {text}")):
            for n in range(1, runs + 1):
                target = out / f"q{q}-p{path_no}-{n}.jsonl"
                if target.exists() and target.stat().st_size > 0:
                    print(f"skip {target.name}", flush=True)
                    continue
                project = out / "projects" / f"q{q}p{path_no}r{n}"
                project.mkdir(parents=True, exist_ok=True)
                call_env = dict(env, TEMP=str(project), TMP=str(project))
                command = [
                    "claude", "-p", prompt, "--model", "haiku",
                    "--plugin-dir", str(plugin),
                    *TOOLS_ALLOWED, *TOOLS_DENIED,
                    "--strict-mcp-config", "--no-session-persistence",
                    "--output-format", "stream-json", "--verbose",
                ]
                print(f"run q{q} p{path_no} n{n}", flush=True)
                with target.open("wb") as handle:
                    subprocess.run(command, cwd=project, env=call_env, stdout=handle, stderr=subprocess.STDOUT, check=False)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--questions", default="1-7")
    args = parser.parse_args()
    if "-" in args.questions:
        low, high = args.questions.split("-")
        questions = list(range(int(low), int(high) + 1))
    else:
        questions = [int(x) for x in args.questions.split(",")]
    args.out.mkdir(parents=True, exist_ok=True)
    run(args.plugin.resolve(), args.out.resolve(), args.runs, questions)
    print(json.dumps({"done": True, "out": str(args.out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
