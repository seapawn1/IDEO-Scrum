#!/usr/bin/env python3
"""Sprint 17 引用核对：每处「convention N」指到存在的条，并印出所指的短名，供逐处读。"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
D = ROOT / "drafts"

FILES = {
    "sprint-log.md": D / "sprint-kernel/conventions/sprint-log.md",
    "sprint-backlog-template.md": D / "sprint-kernel/conventions/sprint-backlog-template.md",
    "product-log.md": D / "scrum-kernel/conventions/product-log.md",
    "overview.md": D / "scrum-kernel/overview.md",
    "design-log.md": D / "design-kernel/conventions/design-log.md",
    "design-backlog-template.md": D / "design-kernel/conventions/design-backlog-template.md",
    "design-sprint-or-five-modes.md": D / "ideo-kernel/conventions/design-sprint-or-five-modes.md",
    "scrum-kernel-SKILL.md": D / "scrum-kernel/SKILL.md",
    "ideo-kernel-SKILL.md": D / "ideo-kernel/SKILL.md",
}

# 同名文件 → 唯一的约定文件；模板默认找同文件夹的约定文件
CONV_FILE = {
    "sprint-log.md": "sprint-log.md",
    "sprint-backlog-template.md": "sprint-log.md",
    "product-log.md": "product-log.md",
    "overview.md": "overview.md",
    "design-log.md": "design-log.md",
    "design-backlog-template.md": "design-log.md",
    "design-sprint-or-five-modes.md": "design-sprint-or-five-modes.md",
    "SKILL.md": None,
}

def conventions(path):
    text = path.read_text(encoding="utf-8")
    return {int(m.group(1)): m.group(2)
            for m in re.finditer(r"^\s*(\d+)\.\s+\*\*(.+?)\*\*", text, re.M)}

CONV = {name: conventions(p) for name, p in FILES.items()}

def expand(spec):
    nums = []
    for part in re.split(r",\s*|\s+and\s+", spec):
        m = re.fullmatch(r"(\d+)\s*[–-]\s*(\d+)", part.strip())
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            nums.extend(range(min(a, b), max(a, b) + 1))
        elif part.strip().isdigit():
            nums.append(int(part.strip()))
    return nums

# 已知结果自测
assert expand("11") == [11]
assert expand("13–14") == [13, 14]
assert expand("9 and 11–15") == [9, 11, 12, 13, 14, 15]
assert expand("6–7") == [6, 7]

NUM = re.compile(r"\bconventions?\s+([0-9](?:[0-9,\s–-]*[0-9])?)")
PATH = re.compile(r"`([^`\n]+\.md)`")
problems = 0
rows = []
for name, path in FILES.items():
    text = path.read_text(encoding="utf-8")
    for m in NUM.finditer(text):
        nums = expand(m.group(1))
        before = text[max(0, m.start() - 80): m.start()]
        after = text[m.end(): m.end() + 60]
        bpaths = [p for p in PATH.findall(before)
                  if Path(p).name in CONV_FILE and Path(p).name != "SKILL.md"]
        apaths = [p for p in re.findall(r"in\s+`([^`\n]+\.md)`", after)
                  if Path(p).name in CONV_FILE]
        ref = apaths[0] if apaths else (bpaths[-1] if bpaths else None)
        if ref:
            ref = Path(ref).name
        tgt = CONV_FILE.get(ref, ref) if ref else None
        if tgt is None:
            tgt = CONV_FILE.get(name, name)
        if tgt not in CONV:
            rows.append((name, tgt or "?", nums, "!! 目标未知"))
            problems += 1
            continue
        for n in nums:
            short = CONV[tgt].get(n)
            if short is None:
                rows.append((name, tgt, [n], "!! 条不存在"))
                problems += 1
            else:
                rows.append((name, tgt, [n], short))

for name, tgt, nums, short in rows:
    print(f"{name:30s} -> {tgt:30s} {str(nums):12s} {short}")
print(f"\n共 {len(rows)} 处引用；问题 {problems} 处")
sys.exit(1 if problems else 0)
