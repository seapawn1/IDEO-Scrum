"""核对 PBI-66 的冻结样本；只供本冲刺测试，不进入插件。"""

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path


def cells(line):
    if not line.strip().startswith("|"):
        return []
    return [part.strip().replace(r"\|", "|") for part in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def parse(text):
    result = {"commitments": {}, "now": [], "waiting": [], "work_items": [], "for": None}
    heading = ""
    fenced = False
    work_table = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if match:
            heading = match.group(1)
            work_table = False
        if line.startswith("> Now:"):
            result["now"].append(line.removeprefix("> Now:").strip())
        if line.startswith("> Waiting for PO:"):
            result["waiting"].append(line.removeprefix("> Waiting for PO:").strip())
        match = re.search(r"(?:^|\|)\s*For:\s*([^|]+)", line) if line.startswith(">") else None
        if match:
            result["for"] = match.group(1).strip()
        row = cells(line)
        if len(row) == 2 and row[0] in ("Commitment", "承诺"):
            if heading in result["commitments"]:
                raise AssertionError(f"重复承诺：{heading}")
            result["commitments"][heading] = row[1]
        if heading == "3. How" and row == ["#", "Work item", "Output", "Done when"]:
            work_table = True
        elif work_table and len(row) == 4 and not all(re.fullmatch(r":?-+:?", item) for item in row):
            result["work_items"].append({"id": row[0], "done_when": row[3], "complete": row[3].startswith("✓")})
    return result


def render(template, spec):
    output = []
    heading = ""
    work_header = False
    found = set()
    for line in template.splitlines():
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if match:
            heading = match.group(1)
            work_header = False
        row = cells(line)
        if len(row) == 2 and row[0] == "Commitment" and heading in spec["commitments"]:
            value = spec["commitments"][heading].replace("|", r"\|")
            line = f"| {spec['key']} | {value} |"
            found.add(heading)
        if line.startswith("> Now:") and spec["now"] is not None:
            line = f"> Now: {spec['now']}"
        if line.startswith("> Waiting for PO:") and spec["waiting"] is not None:
            line = f"> Waiting for PO: {spec['waiting']}"
        if spec.get("for") and line.startswith(">") and "For:" in line:
            line = re.sub(r"(For:\s*)<[^>]+>", lambda match: match.group(1) + spec["for"], line)
        output.append(line)
        if heading == "3. How" and row == ["#", "Work item", "Output", "Done when"]:
            work_header = True
        elif work_header and len(row) == 4 and all(re.fullmatch(r":?-+:?", item) for item in row):
            for work in spec["work_items"]:
                output.append(f"| {work['id']} | 模拟工作块 | 模拟产出 | {work['done_when']} |")
            work_header = False
    assert found == set(spec["commitments"]), "模板的承诺表位置不齐"
    return "\n".join(output) + "\n"


def self_test():
    text = """# Sample
### 1.1 Sprint Goal
| 承诺 | 目标原文 |
| --- | --- |
> Now: Increment
> Waiting for PO: None
## 3. How
| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| A | 第一块 | 产出 | ✓ 2026-11-13；有证据 |
| B | 第二块 | 产出 | 待完成 |
```markdown
### Fake
| Commitment | 不能读进来 |
> Now: Fake
```
"""
    actual = parse(text)
    assert actual["commitments"] == {"1.1 Sprint Goal": "目标原文"}
    assert actual["now"] == ["Increment"] and actual["waiting"] == ["None"]
    assert [row["complete"] for row in actual["work_items"]] == [True, False]
    assert parse("### 1.1 Product\n| Commitment | English |\n")["commitments"] == {"1.1 Product": "English"}
    print("判定脚本自测：通过（双语键、已完成/未完成、代码围栏隔离）")


def verify(root, cases):
    plugin = root / "plugins/ideo-scrum/skills"
    paths = {
        "product": "scrum/ProductBacklog.md",
        "sprint": "scrum/sprint-sample/SprintBacklog.md",
        "design": "scrum/design-sample/DesignBacklog.md",
        "ideo": "scrum/ideo-sample/IdeoBacklog.md",
    }
    with tempfile.TemporaryDirectory(prefix="ideo-s18-66-") as temp:
        folder = Path(temp)
        for spec in cases:
            destination = folder / paths[spec["id"]]
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(render((plugin / spec["template"]).read_text(encoding="utf-8"), spec), encoding="utf-8")
        for spec in cases:
            destination = folder / paths[spec["id"]]
            actual = parse(destination.read_text(encoding="utf-8"))
            assert actual["commitments"] == spec["commitments"], (spec["id"], "承诺不符")
            assert actual["now"] == ([] if spec["now"] is None else [spec["now"]]), (spec["id"], "Now 不符")
            assert actual["waiting"] == ([] if spec["waiting"] is None else [spec["waiting"]]), (spec["id"], "Waiting 不符")
            assert actual["work_items"] == spec["work_items"], (spec["id"], "工作块不符")
            if spec.get("for"):
                assert actual["for"] == spec["for"], "For 路径不符"
                assert (destination.parent / actual["for"]).resolve().is_file(), "For 未指向服务日志"
            print(f"{spec['id']}: PASS")
    print(f"静态接口核对：{len(cases)}/{len(cases)}，原文、字段有无、For、✓ 行均一致")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        cases = json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))
        verify(args.root, cases["static_cases"])


if __name__ == "__main__":
    main()
