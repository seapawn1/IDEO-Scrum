"""Sprint 26, work item 2: check the subagents' annotations against the ledger and against the facts they cite, then assemble.

    python -X utf8 -I scripts/check_annotations.py check              check every review/annotations/*.json
    python -X utf8 -I scripts/check_annotations.py check --complete   also require that all 111 rules are annotated exactly once
    python -X utf8 -I scripts/check_annotations.py assemble           write review/<file>.md for each file (after `check --complete` passes)
    python -X utf8 -I scripts/check_annotations.py stats              counts by source, recommendation, home, confidence
    python -X utf8 -I scripts/check_annotations.py --selftest         prove the checks can fail

What is checked: the schema (fields, allowed values), that each id is in the ledger and used once, and that each cited
fact is real: a commit hash exists, a path exists, a quotation in 「」 occurs in the file it is cited for (white space
ignored). An invented basis is an error, so the annotation is not accepted until it is fixed or its basis is dropped.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPRINT = HERE.parent
REPO = SPRINT.parents[1]
REVIEW = SPRINT / "review"
ANN = REVIEW / "annotations"
LEDGER = REVIEW / "ledger.json"

SOURCES = ["原文", "PO 原话", "作者", "补充", "无据"]
KINDS = ["规矩", "格式", "说明"]
HOMES = ["清单", "长文件", "不进 Memory"]
RECS = ["留", "改", "并", "删"]
CONFS = ["高", "中", "低"]
REQUIRED = ["id", "source", "basis", "kind", "home", "recommend", "merge_into", "reason", "dups", "confidence"]
BASIS_TYPES = ["commit", "archive", "po", "memory", "source"]
QUOTE = re.compile(r"「([^」]+)」")
_text_cache: dict[str, str] = {}


def squash(s: str) -> str:
    return re.sub(r"\s+", "", s)


def resolve(path: str) -> Path | None:
    p = path.strip().strip("`'\"").rstrip(":：,，;；。")
    for cand in (Path(p), REPO / p):
        try:
            if cand.exists():
                return cand
        except OSError:
            pass
    return None


def file_text(path: Path) -> str:
    key = str(path)
    if key not in _text_cache:
        _text_cache[key] = squash(path.read_bytes().decode("utf-8", "replace"))
    return _text_cache[key]


def git_ok(*args: str) -> bool:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True).returncode == 0


def check_basis(item: str) -> list[str]:
    """Problems with one basis string. [] when every cited fact is real."""
    if item.strip().startswith("无据"):
        return []
    m = re.match(r"(\S+)\s+(.*)", item.strip(), re.S)
    if not m:
        return [f"basis is not '<type> <what>': {item[:50]!r}"]
    kind, rest = m.group(1), m.group(2)
    if kind not in BASIS_TYPES:
        return [f"unknown basis type {kind!r}: {item[:50]!r}"]
    errors: list[str] = []
    if kind == "commit":
        h = re.match(r"([0-9a-f]{7,40})\b", rest)
        if not h:
            return [f"commit basis has no hash: {item[:60]!r}"]
        if not git_ok("cat-file", "-e", h.group(1) + "^{commit}"):
            errors.append(f"commit {h.group(1)} does not exist")
        return errors
    path_part = rest.split("：")[0].split()[0] if rest.split("：")[0].split() else ""
    p = resolve(path_part)
    if p is None:
        return [f"{kind} path not found: {path_part!r}"]
    for q in QUOTE.findall(rest):
        if squash(q) not in file_text(p):
            errors.append(f"quote not in {path_part}: 「{q[:40]}…」")
    if kind in ("po", "source") and not QUOTE.search(rest):
        errors.append(f"{kind} basis needs a quotation in 「」: {item[:50]!r}")
    return errors


def check_item(obj: dict, ids: set[str], flags_by_id: dict[str, list[str]]) -> list[str]:
    errors: list[str] = []
    for k in REQUIRED:
        if k not in obj:
            errors.append(f"missing field {k}")
    if errors:
        return errors
    if obj["id"] not in ids:
        errors.append(f"id {obj['id']!r} is not in the ledger")
    for field, allowed in (("source", SOURCES), ("kind", KINDS), ("home", HOMES), ("recommend", RECS), ("confidence", CONFS)):
        if obj[field] not in allowed:
            errors.append(f"{field} {obj[field]!r} is not one of {allowed}")
    if obj["recommend"] == "并":
        if obj["merge_into"] not in ids or obj["merge_into"] == obj["id"]:
            errors.append("recommend 并 needs a merge_into that is another id in the ledger")
    elif obj["merge_into"] is not None:
        errors.append("merge_into must be null unless recommend is 并")
    if not isinstance(obj["reason"], str) or not obj["reason"].strip():
        errors.append("reason is empty")
    elif len(obj["reason"]) > 500:
        errors.append(f"reason is {len(obj['reason'])} characters; keep it to a line or two")
    if not isinstance(obj["dups"], list) or any(d not in ids for d in obj["dups"]):
        errors.append("dups must be a list of ledger ids")
    basis = obj["basis"]
    if not isinstance(basis, list) or not basis or not all(isinstance(b, str) for b in basis):
        errors.append("basis must be a non-empty list of strings")
        return errors
    for b in basis:
        errors += check_basis(b)
    kinds = {("无据" if b.strip().startswith("无据") else b.split()[0].rstrip("：:")) for b in basis if b.strip()}
    src = obj["source"]
    if src == "无据" and "无据" not in kinds:
        errors.append("source 无据 needs basis ['无据：…']")
    if src == "原文" and "source" not in kinds:
        errors.append("source 原文 needs a 'source' basis with a quotation")
    if src == "PO 原话" and "po" not in kinds:
        errors.append("source PO 原话 needs a 'po' basis with a quotation")
    if src == "作者" and not kinds & {"commit", "archive", "memory"}:
        errors.append("source 作者 needs a commit, archive or memory basis")
    if src == "补充" and "Supplement" not in flags_by_id.get(obj["id"], []):
        errors.append("source 补充 but the rule has no *Supplement* label (say so in reason, or choose another source)")
    return errors


def load_ledger() -> tuple[dict, set[str], dict[str, list[str]]]:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    ids, flags = set(), {}
    for f in ledger["files"]:
        for r in f["rules"]:
            ids.add(r["id"])
            flags[r["id"]] = r["flags"]
    return ledger, ids, flags


def load_annotations() -> tuple[list[tuple[str, dict]], list[str]]:
    rows, problems = [], []
    for p in sorted(ANN.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except ValueError as e:
            problems.append(f"{p.name}: not valid JSON ({e})")
            continue
        if not isinstance(data, list):
            problems.append(f"{p.name}: top level must be a list")
            continue
        for obj in data:
            rows.append((p.name, obj))
    return rows, problems


def run_check(complete: bool) -> int:
    _, ids, flags = load_ledger()
    rows, problems = load_annotations()
    seen: Counter = Counter()
    bad_items = 0
    for name, obj in rows:
        errs = check_item(obj, ids, flags) if isinstance(obj, dict) else ["not an object"]
        seen[obj.get("id") if isinstance(obj, dict) else None] += 1
        if errs:
            bad_items += 1
            problems += [f"{name} {obj.get('id') if isinstance(obj, dict) else '?'}: {e}" for e in errs]
    for i, n in seen.items():
        if n > 1:
            problems.append(f"id {i} is annotated {n} times")
    if complete:
        problems += [f"{i} is not annotated" for i in sorted(ids - set(seen))]
    print(f"{len(rows)} annotations in {len(list(ANN.glob('*.json')))} files; {bad_items} with problems; {len(problems)} problems")
    for p in problems:
        print("  " + p)
    return 1 if problems else 0


def run_stats() -> int:
    rows, _ = load_annotations()
    for field in ("source", "recommend", "kind", "home", "confidence"):
        print(field, dict(Counter(o.get(field) for _, o in rows)))
    return 0


def md_escape_fence(text: str) -> str:
    return text.replace("```", "'''")


def run_assemble() -> int:
    ledger, _, _ = load_ledger()
    rows, _ = load_annotations()
    by_id = {o["id"]: o for _, o in rows}
    for f in ledger["files"]:
        out = [f"# 审读记录：{f['short']}（{len(f['rules'])} 条）", "",
               f"`{f['path']}` · 基线 `{ledger['baseline_commit'][:7]}`。旧规矩逐字取自台账；出处、依据、建议、理由由子代理标注，已核对提交、路径与引文真实存在，我抽检。",
               "“转后的一行／去向”与“PO 定稿”两栏在行 6–8、行 10 填。", ""]
        for r in f["rules"]:
            a = by_id[r["id"]]
            merge = f"（并入 {a['merge_into']}）" if a["merge_into"] else ""
            out += [f"## {r['id']} · {r['name']}", "", "旧规矩（逐字）：", "", "```text", md_escape_fence(r["text"]), "```", "",
                    f"- **出处**：{a['source']}　**类别**：{a['kind']}　**去处**：{a['home']}　**把握**：{a['confidence']}",
                    "- **依据**：" + "；".join(a["basis"]),
                    f"- **建议**：{a['recommend']}{merge}。{a['reason']}"]
            if a["dups"]:
                out.append("- **重复**：" + "、".join(a["dups"]))
            out += ["- **转后的一行／去向**：（待行 6–8）", "- **PO 定稿**：（待行 10）", ""]
        (REVIEW / f"{f['short']}.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
        print("wrote", f"review/{f['short']}.md")
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    ids = {"a#1", "a#2", "a#3"}
    good = {"id": "a#1", "source": "作者", "basis": ["commit " + subprocess.run(["git", "rev-parse", "--short=7", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip() + " 本期提交"],
            "kind": "规矩", "home": "清单", "recommend": "留", "merge_into": None, "reason": "有依据，Memory 需要它。", "dups": [], "confidence": "高"}
    check(check_item(good, ids, {}) == [], "a correct annotation passes")
    check(any("does not exist" in e for e in check_item({**good, "basis": ["commit deadbee 编的提交"]}, ids, {})), "planted defect: an invented commit hash is caught")
    check(any("path not found" in e for e in check_item({**good, "basis": ["archive scrum/documents/no-such-file.md 不存在"]}, ids, {})), "planted defect: an invented path is caught")
    anchor = "scrum/sprint-26-plugin-memory/review/annotation-brief.md"
    check(check_basis(f"po {anchor}：「没有依据我是不可接受的」") == [], "a real quotation passes")
    check(any("quote not in" in e for e in check_basis(f"po {anchor}：「这句话文件里没有」")), "planted defect: a quotation that is not in the file is caught")
    check(any("needs a quotation" in e for e in check_basis(f"po {anchor} 没有引文")), "planted defect: a po basis without a quotation is caught")
    check(any("needs a merge_into" in e for e in check_item({**good, "recommend": "并"}, ids, {})), "planted defect: 并 without merge_into is caught")
    check(any("not one of" in e for e in check_item({**good, "recommend": "也许"}, ids, {})), "planted defect: a value outside the list is caught")
    check(any("missing field" in e for e in check_item({k: v for k, v in good.items() if k != "reason"}, ids, {})), "planted defect: a missing field is caught")
    check(any("needs a 'source' basis" in e for e in check_item({**good, "source": "原文"}, ids, {})), "planted defect: 原文 without a source quotation is caught")
    check(check_item({**good, "source": "无据", "basis": ["无据：查了提交与归档，没找到"]}, ids, {}) == [], "无据 with an honest basis passes")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main() -> int:
    argv = sys.argv[1:]
    if "--selftest" in argv:
        return selftest()
    if argv[:1] == ["check"]:
        return run_check("--complete" in argv)
    if argv[:1] == ["assemble"]:
        return run_assemble()
    if argv[:1] == ["stats"]:
        return run_stats()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
