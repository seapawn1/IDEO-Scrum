"""Check the plugin's user-facing docs against each other (Sprint 20, PBI-62).

    python -X utf8 -I scripts/check_docs.py             check this repository
    python -X utf8 -I scripts/check_docs.py --selftest  prove each check can fail, on a copy with planted defects

For each English/Chinese pair (README.md and README.zh-CN.md, docs/quick-start.md and docs/quick-start.zh-CN.md):
the same headings in the same order; in every section the same number of list items, table rows and code blocks;
the same commands in the `sh` blocks (typed in a terminal) and in the `text` blocks whose lines all start with
`/` (typed in a Claude Code session); a trailing `# comment` is ignored; the same links.
For every document, glossary included: every relative link and image resolves, and every #fragment names a heading
in its target. Also: each README's version is the plugin's version, and the English README's "How it differs"
table repeats the Departures table of overview.md word for word (the Here and Why columns).

Prints one JSON object and exits 1 when there are errors. It checks shape, not meaning: whether a sentence says
what the convention says is read by a person.
"""
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ("README.md", "README.zh-CN.md"),
    ("docs/quick-start.md", "docs/quick-start.zh-CN.md"),
]
SINGLES = ["docs/glossary.md"]
OVERVIEW = "plugins/ideo-scrum/skills/scrum-kernel/overview.md"
DEPARTURES = "Departures from the official guides"
DIFFERS = "How it differs from textbook Scrum"
PLUGIN_JSON = "plugins/ideo-scrum/.claude-plugin/plugin.json"

FENCE = re.compile(r"^\s*```(\w*)\s*$")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG_MD = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
IMG_HTML = re.compile(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", re.I)
TRAILING_COMMENT = re.compile(r"\s+#\s.*$")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def slug(title: str) -> str:
    """GitHub's heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    s = title.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def new_section(level: int, title: str) -> dict:
    return {"level": level, "title": title, "items": 0, "rows": 0, "blocks": 0, "sh": [], "slash": [],
            "links": [], "images": [], "table": []}


def parse(text: str) -> dict:
    """Split a document into sections; count what is outside code fences."""
    sections = [new_section(0, "")]
    in_code = False
    lang = ""
    block: list[str] = []
    for line in text.split("\n"):
        m = FENCE.match(line)
        if m:
            if not in_code:
                in_code, lang, block = True, m.group(1), []
            else:
                in_code = False
                sections[-1]["blocks"] += 1
                lines = [TRAILING_COMMENT.sub("", l).rstrip() for l in block if l.strip()]
                if lang == "sh":
                    sections[-1]["sh"].append(lines)
                elif lang == "text" and lines and all(l.startswith("/") for l in lines):
                    sections[-1]["slash"].append(lines)
            continue
        if in_code:
            block.append(line)
            continue
        h = HEADING.match(line)
        if h:
            sections.append(new_section(len(h.group(1)), h.group(2)))
            continue
        sec = sections[-1]
        if LIST_ITEM.match(line):
            sec["items"] += 1
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                sec["rows"] += 1
                sec["table"].append(cells)
        sec["links"] += LINK.findall(line)
        sec["images"] += IMG_MD.findall(line) + IMG_HTML.findall(line)
    return {"sections": sections}


def headings(doc: dict) -> set:
    return {slug(s["title"]) for s in doc["sections"] if s["level"]}


def norm_target(target: str) -> str:
    """Compare links across languages: drop the fragment, fold the zh file names onto the English ones."""
    if target.startswith("#"):
        return "#"
    return target.split("#", 1)[0].replace(".zh-CN.md", ".md")


def check(root: Path) -> dict:
    errors: list[str] = []
    docs: dict[str, dict] = {}
    link_count = 0

    for name in [n for pair in PAIRS for n in pair] + SINGLES:
        path = root / name
        if not path.is_file():
            errors.append(f"missing: {name}")
            continue
        docs[name] = parse(read(path))

    # pairs: the same shape
    for en, zh in PAIRS:
        if en not in docs or zh not in docs:
            continue
        a, b = docs[en]["sections"], docs[zh]["sections"]
        if [s["level"] for s in a] != [s["level"] for s in b]:
            errors.append(f"{zh}: heading levels differ from {en}: "
                          f"{[s['level'] for s in b]} vs {[s['level'] for s in a]}")
            continue
        for sa, sb in zip(a, b):
            where = f"{zh} section {sb['title'] or '(top)'!r} (English: {sa['title'] or '(top)'!r})"
            for key, label in (("items", "list items"), ("rows", "table rows"), ("blocks", "code blocks")):
                if sa[key] != sb[key]:
                    errors.append(f"{where}: {label} {sb[key]} vs {sa[key]}")
            if sa["sh"] != sb["sh"]:
                errors.append(f"{where}: the sh blocks differ: {sb['sh']} vs {sa['sh']}")
            if sa["slash"] != sb["slash"]:
                errors.append(f"{where}: the slash-command blocks differ: {sb['slash']} vs {sa['slash']}")
            la = sorted(norm_target(t) for t in sa["links"] + sa["images"])
            lb = sorted(norm_target(t) for t in sb["links"] + sb["images"])
            if la != lb:
                errors.append(f"{where}: links differ: {lb} vs {la}")

    # links and images resolve
    for name, doc in docs.items():
        base = (root / name).parent
        own = headings(doc)
        for sec in doc["sections"]:
            for target in sec["links"] + sec["images"]:
                link_count += 1
                if re.match(r"[a-z][a-z0-9+.-]*:", target, re.I):
                    continue  # http, https, mailto: not checked here
                path_part, _, fragment = target.partition("#")
                if not path_part:
                    if fragment and fragment not in own:
                        errors.append(f"{name}: no heading for #{fragment}")
                    continue
                dest = (base / path_part).resolve()
                if not dest.exists():
                    errors.append(f"{name}: dead link {target}")
                    continue
                if fragment and dest.suffix == ".md" and fragment not in headings(parse(read(dest))):
                    errors.append(f"{name}: {path_part} has no heading for #{fragment}")

    # each README carries the plugin's version
    version = json.loads(read(root / PLUGIN_JSON))["version"]
    for name in ("README.md", "README.zh-CN.md"):
        if name in docs:
            head = "\n".join(read(root / name).split("\n")[:12])
            found = re.findall(r"\*\*v(\d+\.\d+\.\d+)\*\*", head)
            if found != [version]:
                errors.append(f"{name}: version {found} is not the plugin's {version}")

    # the "How it differs" table repeats the Departures table of overview.md
    departures = []
    for sec in parse(read(root / OVERVIEW))["sections"]:
        if sec["title"] == DEPARTURES:
            departures = [(r[0], r[2]) for r in sec["table"][1:]]
    if not departures:
        errors.append(f"{OVERVIEW}: no Departures table found")
    if "README.md" in docs:
        rows = [s for s in docs["README.md"]["sections"] if s["title"] == DIFFERS]
        if len(rows) != 1:
            errors.append(f"README.md: expected one section {DIFFERS!r}")
        else:
            got = [(r[0], r[1]) for r in rows[0]["table"][1:]]
            for g in got:
                if g not in departures:
                    errors.append(f"README.md: row not in the Departures table word for word: {g[0]!r}")
            if len(got) != len(departures):
                errors.append(f"README.md: {len(got)} rows, the Departures table has {len(departures)}")

    return {"documents": sorted(docs), "links_checked": link_count, "errors": errors}


# ---- the self-test: plant a defect, expect the check to name it ---------------------------------------------
STUB_EN = "# Stub\n\n## Part\n\n- one\n- two\n\n| a | b |\n| --- | --- |\n| 1 | 2 |\n"
STUB_ZH = "# 桩\n\n## 部分\n\n- 一\n- 二\n\n| 甲 | 乙 |\n| --- | --- |\n| 1 | 2 |\n"


def build_copy(dest: Path) -> None:
    """A copy of what the check reads: the real READMEs, overview.md and plugin.json, stub docs, and empty
    files at the other link targets."""
    for name in ("README.md", "README.zh-CN.md", OVERVIEW, PLUGIN_JSON):
        (dest / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(ROOT / name, dest / name)
    for name, text in (("docs/quick-start.md", STUB_EN), ("docs/quick-start.zh-CN.md", STUB_ZH),
                       ("docs/glossary.md", STUB_EN)):
        (dest / name).parent.mkdir(parents=True, exist_ok=True)
        (dest / name).write_text(text, encoding="utf-8")
    for name in ("README.md", "README.zh-CN.md"):
        for sec in parse(read(ROOT / name))["sections"]:
            for target in sec["links"] + sec["images"]:
                path_part = target.partition("#")[0]
                if path_part and not re.match(r"[a-z][a-z0-9+.-]*:", path_part, re.I):
                    p = dest / path_part
                    if not p.exists():
                        p.parent.mkdir(parents=True, exist_ok=True)
                        p.write_text("", encoding="utf-8")


def selftest() -> int:
    cases = [
        ("a zh heading removed", "README.zh-CN.md", "## 反馈\n", "", "heading levels differ"),
        ("a zh slash command changed", "README.zh-CN.md", "/reload-plugins\n```", "/reload\n```",
         "slash-command blocks differ"),
        ("a zh terminal command changed", "README.zh-CN.md", "claude plugin update ideo-scrum@ideo-scrum\n```",
         "claude plugin update ideo-scrum\n```", "sh blocks differ"),
        ("a zh list item removed", "README.zh-CN.md", "- 你要接 JIRA 或 Linear，或者要一个给整个团队用的平台。\n", "",
         "list items"),
        ("a zh table row removed", "README.zh-CN.md", "| `scripts/` | 生成、核对 Codex 版和文档的脚本 |\n", "",
         "table rows"),
        ("an en Departures cell changed", "README.md", "AI works by session, not by day", "AI works by session",
         "not in the Departures table"),
        ("a stale version", "README.md", "**v", "**v1", "version"),
        ("a dead link", "README.md", "[Glossary](docs/glossary.md)", "[Glossary](docs/nope.md)", "dead link"),
        ("a missing heading", "README.md", "overview.md#departures-from-the-official-guides",
         "overview.md#no-such-heading", "no heading for #no-such-heading"),
        ("a zh link retargeted", "README.zh-CN.md", "[词汇表](docs/glossary.md)", "[词汇表](CHANGELOG.md)",
         "links differ"),
    ]
    failures = []
    base = Path(tempfile.mkdtemp(prefix="check-docs-"))
    try:
        build_copy(base)
        clean = check(base)["errors"]
        if clean:
            failures.append(f"the copy without defects reports errors: {clean}")
        for label, name, old, new, expect in cases:
            work = Path(tempfile.mkdtemp(prefix="check-docs-case-"))
            try:
                build_copy(work)
                text = read(work / name)
                if old not in text:
                    failures.append(f"{label}: the planted text was not found in {name}")
                    continue
                (work / name).write_text(text.replace(old, new, 1), encoding="utf-8")
                errors = check(work)["errors"]
                if expect and not any(expect in e for e in errors):
                    failures.append(f"{label}: expected an error with {expect!r}, got {errors}")
                if not expect and errors:
                    failures.append(f"{label}: expected no errors, got {errors}")
            finally:
                shutil.rmtree(work, ignore_errors=True)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print(json.dumps({"selftest": "failed" if failures else "ok", "cases": len(cases) + 1, "failures": failures},
                     ensure_ascii=False, indent=2))
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    result = check(ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
