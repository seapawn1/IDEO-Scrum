#!/usr/bin/env python3
"""Sprint 17 流程测试：从 stream-json 输出提取行为栏（加载了哪些技能、读了哪些约定文件）与回答文本。"""
import json, re, sys
from pathlib import Path

ARCH = Path(r"S:/IDEO-Scrum-Archives/sprint-17-conventions-rewrite")
OUT = Path(r"S:/IDEO-Scrum/.claude/worktrees/awesome-pare-fb64d7/scrum/sprint-17-conventions-rewrite/test-results")

def parse(p):
    skills, reads, greps, result = [], [], [], ""
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("type") == "assistant":
            for c in e.get("message", {}).get("content", []):
                if c.get("type") != "tool_use":
                    continue
                name, inp = c.get("name"), c.get("input", {}) or {}
                if name == "Skill":
                    skills.append(str(inp.get("skill", "")))
                elif name == "Read":
                    reads.append(str(inp.get("file_path", "")))
                elif name == "Grep":
                    greps.append(str(inp.get("path", "")) + " :: " + str(inp.get("pattern", ""))[:60])
        elif e.get("type") == "result":
            result = e.get("result", "") or ""
    return skills, reads, greps, result

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for p in sorted(ARCH.glob("q*.jsonl")):
        skills, reads, greps, result = parse(p)
        conv_reads = [r for r in reads if re.search(r"(conventions/|overview\.md$|SKILL\.md$)", r.replace("\\", "/"))]
        rows.append((p.name, skills, conv_reads, greps, len(result)))
        (OUT / (p.stem + ".txt")).write_text(result, encoding="utf-8")
    for name, skills, conv_reads, greps, n in rows:
        print(f"{name:28s} skills={skills} conv_reads={[Path(x).name for x in conv_reads]} greps={len(greps)} len={n}")
    print(f"\n共 {len(rows)} 份")

if __name__ == "__main__":
    main()
