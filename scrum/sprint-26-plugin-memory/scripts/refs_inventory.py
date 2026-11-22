"""Sprint 26 rows 11-13 (prep): inventory every reference to the old conventions, so the migration is a table and not a hunt.

    python -X utf8 -I scripts/refs_inventory.py            write review/refs-inventory.md and print the counts
    python -X utf8 -I scripts/refs_inventory.py --selftest

Scans the live files (plugin, docs, README, scripts, dsh, AGENTS.md ...) and not the archives (scrum/documents/,
references/), which stay as they are. A reference is one of:
  path      a mention of one of the six convention files, or of overview.md, by path or bare name
  number    "convention N", "conventions N-M", "(conventions 10, 12)" ...; resolved to a rule id (file#N) when the
            same sentence names the file ("`../sprint-kernel/conventions/sprint-log.md`, convention 17"), else to the
            file that holds the reference when that file is one of the six, else left unresolved (listed for a human)
  heading   a mention of a heading of the old files by name (the Departures section)
"""
from __future__ import annotations

import pathlib
import re
import sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
REPO = SPRINT.parents[1]
OUT = SPRINT / "review" / "refs-inventory.md"

SCAN_GLOBS = ["plugins/**/*", "docs/**/*", "scripts/**/*", "dsh/**/*", "README.md", "README.zh-CN.md", "AGENTS.md", "CLAUDE.md",
              "package.json", "cordis.patch.yml", "ATTRIBUTION.md", "CHANGELOG.md", ".worktreeinclude", "scrum/ProductBacklog.md"]
SKIP_PARTS = {"node_modules", ".git", "__pycache__", "fixtures"}
TEXT_SUFFIX = {".md", ".py", ".js", ".mjs", ".json", ".yml", ".yaml", ".html", ".sh", ".txt", ""}
SIX = {"overview": "overview.md", "product-log": "conventions/product-log.md", "board-log": "conventions/board-log.md",
       "sprint-log": "conventions/sprint-log.md", "design-log": "conventions/design-log.md", "ideo-log": "conventions/ideo-log.md"}
PATH_RE = re.compile(r"(?:[\w./-]*?)(overview\.md|(?:product|sprint|design|ideo)-log\.md)")  # board-log.md stays (Master 2026-11-23): its path and numbers are not migrated
NUM_RE = re.compile(r"\bconventions?\s+((?:\d+(?:\s*[–-]\s*\d+)?)(?:\s*(?:,|and|and also)\s*\d+(?:\s*[–-]\s*\d+)?)*)", re.I)
HEAD_RE = re.compile(r"Departures section|Departures from the official guides|#departures-from-the-official-guides|\bDepartures table\b", re.I)
# what stays after the migration, and why: there the old number or name means something else, or the file is history
ALLOWED = {
    "CHANGELOG.md": "the release history: its entries say what the files said then",
    "scripts/board_check/check.py": "numbers of board-log.md's own conventions; board-log.md stays at plugins/ideo-scrum/board/",
    "plugins/ideo-scrum/skills/memory/details/departures.md": "its own heading",
    "scripts/check_docs.py": "the Departures table the README is checked against now lives in the Memory's details/departures.md",
    "scripts/check_dsh.mjs": "the guard that no plugin file names a conventions/ folder or overview.md",
}
SHORT = {"overview.md": "overview", "product-log.md": "product-log", "board-log.md": "board-log", "sprint-log.md": "sprint-log",
         "design-log.md": "design-log", "ideo-log.md": "ideo-log"}


def host_short(rel: str) -> str | None:
    name = pathlib.PurePosixPath(rel).name
    return SHORT.get(name) if "skills/" in rel and (name == "overview.md" or "conventions/" in rel) else None


def numbers(spec: str) -> list[int]:
    out: list[int] = []
    for part in re.split(r"\s*(?:,|and also|and)\s*", spec):
        m = re.fullmatch(r"(\d+)\s*[–-]\s*(\d+)", part.strip())
        if m:
            out += list(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.strip().isdigit():
            out.append(int(part))
    return out


def scan_line(rel: str, no: int, line: str) -> list[dict]:
    found = []
    # a file of the Memory's details/ that carries an old name (details/product-log.md, details/departures.md) is the new place
    paths = [(m.start(), SHORT[m.group(1)]) for m in PATH_RE.finditer(line) if not m.group(0)[: m.start(1) - m.start(0)].endswith("details/")]
    for _, short in paths:
        found.append({"file": rel, "line": no, "kind": "path", "target": short, "text": line.strip()[:160]})
    for m in NUM_RE.finditer(line):
        if rel.endswith("board/board-log.md") or "board-log" in line[: m.start()]:
            continue  # a number of board-log's own: that file stays, so the number stays valid
        before = [s for pos, s in paths if pos < m.start()]
        target = before[-1] if before else host_short(rel)
        for n in numbers(m.group(1)):
            found.append({"file": rel, "line": no, "kind": "number", "target": f"{target}#{n}" if target else None, "text": line.strip()[:160]})
    if HEAD_RE.search(line) and "details/departures.md" not in line:
        found.append({"file": rel, "line": no, "kind": "heading", "target": "overview:Departures", "text": line.strip()[:160]})
    return found


def files() -> list[pathlib.Path]:
    seen, out = set(), []
    for g in SCAN_GLOBS:
        for p in REPO.glob(g):
            if p.is_file() and p not in seen and not (set(p.parts) & SKIP_PARTS) and p.suffix.lower() in TEXT_SUFFIX:
                seen.add(p)
                out.append(p)
    return sorted(out)


def main() -> int:
    refs: list[dict] = []
    for p in files():
        rel = p.relative_to(REPO).as_posix()
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for no, line in enumerate(text.split("\n"), 1):
            refs += scan_line(rel, no, line)
    by_kind = Counter(r["kind"] for r in refs)
    unresolved = [r for r in refs if r["kind"] == "number" and not r["target"]]
    inside = [r for r in refs if host_short(r["file"])]
    allowed = [r for r in refs if r["file"] in ALLOWED]
    outside = [r for r in refs if not host_short(r["file"]) and r["file"] not in ALLOWED]
    by_file = Counter(r["file"] for r in refs)
    lines = ["# 旧约定引用清单（Sprint 26 行 11–13 的准备）", "",
             "由 `scripts/refs_inventory.py` 生成：活文件里所有指向六份旧约定的引用（档案 `scrum/documents/` 与 `references/` 不动）。落盘迁移时，每一处要么改指 Memory 的 handle，要么随旧文件一起删。", "",
             f"合计 {len(refs)} 处：路径 {by_kind['path']}、编号 {by_kind['number']}（其中解析不出目标 {len(unresolved)}）、标题 {by_kind['heading']}。六份约定文件自己里面 {len(inside)} 处，别处 {len(outside)} 处。", "",
             "## 按文件", "", "| 文件 | 处数 |", "| --- | --- |"]
    for f, n in by_file.most_common():
        lines.append(f"| `{f}` | {n} |")
    lines += ["", "## 解析不出目标的编号引用（要人看）", ""]
    lines += [f"- `{r['file']}:{r['line']}` {r['text']}" for r in unresolved] or ["（无）"]
    lines += ["", "## 迁完后留下的（有意保留，逐文件附理由）", "", "| 文件 | 处数 | 理由 |", "| --- | --- | --- |"]
    for f, why in ALLOWED.items():
        lines.append(f"| `{f}` | {sum(1 for r in allowed if r['file'] == f)} | {why} |")
    lines += ["", "## 六份约定文件之外的引用（要迁的，逐处）", "", "| 位置 | 种类 | 目标 | 原文 |", "| --- | --- | --- | --- |"]
    for r in sorted(outside, key=lambda r: (r["file"], r["line"])):
        lines.append(f"| `{r['file']}:{r['line']}` | {r['kind']} | {r['target'] or '?'} | {r['text'].replace('|', chr(92) + '|')} |")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(refs)} references: {dict(by_kind)}; unresolved numbers: {len(unresolved)}; inside the six: {len(inside)}; allowed to stay: {len(allowed)}; outside the allowed: {len(outside)}")
    print("top files:", by_file.most_common(8))
    return 0


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    r = scan_line("plugins/ideo-scrum/skills/scrum-kernel/conventions/product-log.md", 1, "see `../sprint-kernel/conventions/sprint-log.md`, convention 17 and `overview.md`, convention 5.")
    check([x["target"] for x in r if x["kind"] == "number"] == ["sprint-log#17", "overview#5"], "a number takes the nearest file named before it")
    r = scan_line("plugins/ideo-scrum/skills/sprint-kernel/conventions/sprint-log.md", 1, "(conventions 10–12, 14)")
    check([x["target"] for x in r if x["kind"] == "number"] == ["sprint-log#10", "sprint-log#11", "sprint-log#12", "sprint-log#14"], "a range and a list inside the host file resolve to the host")
    r = scan_line("plugins/ideo-scrum/commands/developer.md", 1, "(`overview.md`, convention 12)")
    check([x["target"] for x in r if x["kind"] == "number"] == ["overview#12"], "a command file's reference resolves through the path")
    r = scan_line("docs/glossary.md", 1, "see convention 3")
    check([x["target"] for x in r if x["kind"] == "number"] == [None], "a bare number outside the six stays unresolved")
    r = scan_line("README.md", 1, "[Departures](plugins/ideo-scrum/skills/scrum-kernel/overview.md#departures-from-the-official-guides)")
    check({x["kind"] for x in r} == {"path", "heading"}, "a link to the Departures anchor counts as a path and a heading")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
