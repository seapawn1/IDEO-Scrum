"""Check a written scrum/ScrumBoard.html against the project's logs (acceptance 68-4, updated for PBI-105 & PBI-106).

    python -X utf8 -I scripts/board_check/check.py check --project DIR [--page FILE] [--template FILE] [--render]
    python -X utf8 -I scripts/board_check/check.py selftest
    python -X utf8 -I scripts/board_check/check.py ref --project DIR --summaries FILE --out FILE

`check` compares the data block with the logs (ProductBacklog.md and open SprintBacklog.md files only) and the rest of
the page with the template. It checks copied fields, map labels, sources, and chapter 3 work items (matched by header so
solution comparison tables in How do not interfere). It does not judge whether a summary makes sense or follows the
map's main line. `--render` counts the rendered elements, not their visual readability.

`selftest` checks reference pages for fixture projects and verifies that deliberate data errors are reported.
`ref` writes a data file from the logs and supplied summaries.
"""
import argparse
import copy
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
TEMPLATE = REPO / "plugins/ideo-scrum/board/scrum-board-template.html"
PLACEHOLDER = '{"todo": "Replace this line with the board data (board-log.md lists the fields)."}'
# the data block runs to the next script, so a stray </script> inside the data cannot hide itself
BLOCK_RE = re.compile(r'(<script type="application/json" id="board-data">)(.*?)(</script>\s*<script>)', re.S)
LOG_FILES = {"sprint": "SprintBacklog.md"}
PRODUCT_LOG = "scrum/ProductBacklog.md"
PATHS = {k: re.compile(r"^scrum/(%s-[^/]+)/%s$" % (k, v)) for k, v in LOG_FILES.items()}
GROUPS = ("sprint", "next", "later")
WORK_ITEM_COL_RE = re.compile(r"(?:work\s*item|工作项)", re.I)
DONE_WHEN_COL_RE = re.compile(r"(?:done\s*when|完成条件)", re.I)
BROWSERS = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"]


# ---------------------------------------------------------------- reading the logs

def git(root, *args):
    r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def norm_nl(text):
    return text.replace("\r\n", "\n")


def discover(root):
    """Open Sprint logs: in the working copy, else on a branch (the newest commit wins). Ignores documents/ and IDEO."""
    root = pathlib.Path(root)
    found = {}
    scrum = root / "scrum"
    if scrum.is_dir():
        for dirpath, dirs, files in os.walk(scrum):
            dirs[:] = [d for d in dirs if d != "documents"]
            for f in files:
                rel = (pathlib.Path(dirpath) / f).relative_to(root).as_posix()
                for kind, pat in PATHS.items():
                    m = pat.match(rel)
                    if m:
                        found[(kind, m.group(1))] = {"path": rel, "source": "working copy", "commit": ""}
    if (root / ".git").exists():
        best = {}
        for branch in (git(root, "for-each-ref", "--format=%(refname:short)", "refs/heads") or "").split():
            sha = (git(root, "rev-parse", branch) or "").strip()
            stamp = int((git(root, "log", "-1", "--format=%ct", branch) or "0").strip() or 0)
            for rel in (git(root, "ls-tree", "-r", "--name-only", branch, "--", "scrum") or "").split("\n"):
                for kind, pat in PATHS.items():
                    m = pat.match(rel.strip())
                    if m and (kind, m.group(1)) not in found:
                        key = (kind, m.group(1))
                        if key not in best or stamp > best[key][0]:
                            best[key] = (stamp, branch, sha, rel.strip())
        for key, (stamp, branch, sha, rel) in best.items():
            found[key] = {"path": rel, "source": "branch %s @ %s" % (branch, sha[:7]), "commit": sha}
    return found


def read_log(root, path, source):
    root = pathlib.Path(root)
    if source == "working copy":
        p = root / path
        return norm_nl(p.read_text(encoding="utf-8")) if p.is_file() else None
    m = re.match(r"^branch (\S+) @ ([0-9a-f]{7,40})$", source)
    if m:
        out = git(root, "show", "%s:%s" % (m.group(2), path))
        return None if out is None else norm_nl(out)
    return None


def find_product_log(root):
    """(text, source) of the product log: from the working copy when present, else from the newest branch holding it."""
    root = pathlib.Path(root)
    in_copy = root / PRODUCT_LOG
    if in_copy.is_file():
        return norm_nl(in_copy.read_text(encoding="utf-8")), "working copy"
    if (root / ".git").exists():
        best = None
        for branch in (git(root, "for-each-ref", "--format=%(refname:short)", "refs/heads") or "").split():
            if not (git(root, "ls-tree", "--name-only", branch, "--", PRODUCT_LOG) or "").strip():
                continue
            sha = (git(root, "rev-parse", branch) or "").strip()
            stamp = int((git(root, "log", "-1", "--format=%ct", branch) or "0").strip() or 0)
            if best is None or stamp > best[0]:
                best = (stamp, branch, sha)
        if best:
            source = "branch %s @ %s" % (best[1], best[2][:7])
            return read_log(root, PRODUCT_LOG, source), source
    return None, None


def commitments(text):
    """{kind: exact text} from one-row Commitment/承诺 tables; nearest heading selects product/product_goal/sprint_goal."""
    out, head = {}, ""
    for line in text.split("\n"):
        if line.startswith("#"):
            head = line.lstrip("# ").strip()
        m = re.match(r"^\|\s*(?:Commitment|承诺)\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            h = head.lower()
            kind = ("sprint_goal" if ("sprint goal" in h or "冲刺目标" in h)
                    else "product_goal" if ("product goal" in h or "产品目标" in h)
                    else "product" if ("product" in h or "产品" in h) else "")
            if kind and kind not in out:
                out[kind] = m.group(1)
    return out


def now_line(text):
    m = re.search(r"^> Now:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def split_table_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if re.search(r"(?<!\\)\|$", s):
        s = s[:-1]
    return [c.replace(r"\|", "|").strip() for c in re.split(r"(?<!\\)\|", s)]


def parse_table_rows(block_lines):
    return [split_table_row(ln) for ln in block_lines]


def table_after(text, heading_re):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(heading_re, line):
            rows = []
            for nxt in lines[i + 1:]:
                if nxt.startswith("|"):
                    rows.append(split_table_row(nxt))
                elif rows:
                    break
                elif nxt.startswith("#"):
                    break
            return rows[2:]
    return []


def work_item_table(text):
    """Find the chapter 3 work-item table by header (Work item/工作项 + Done when/完成条件), skipping solution tables.

    Scans all Markdown tables inside `## 3.` up to the next `## ` heading (ignoring fenced code blocks). Returns
    `[(n, title, done_bool), ...]` for the matching 4+ column table, or `[]` if chapter 3 has no work-item table.
    """
    lines = text.split("\n")
    start_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^##\s*3\.", line):
            start_idx = i + 1
            break
    if start_idx is None:
        return []

    section_lines = []
    in_fence = False
    for line in lines[start_idx:]:
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            section_lines.append("")
            continue
        if not in_fence and re.match(r"^#{1,2}\s+", line):
            break
        section_lines.append("" if in_fence else line)

    tables = []
    cur = []
    for line in section_lines:
        if line.startswith("|"):
            cur.append(line)
        elif cur:
            tables.append(cur)
            cur = []
    if cur:
        tables.append(cur)

    for tbl in tables:
        rows = parse_table_rows(tbl)
        if len(rows) < 2:
            continue
        header = rows[0]
        if len(header) < 4:
            continue
        if any(WORK_ITEM_COL_RE.search(c) for c in header) and any(DONE_WHEN_COL_RE.search(c) for c in header):
            id_idx = next((idx for idx, c in enumerate(header) if c.strip() == "#"), 0)
            wi_idx = next((idx for idx, c in enumerate(header) if WORK_ITEM_COL_RE.search(c)), 1)
            dw_idx = next((idx for idx, c in enumerate(header) if DONE_WHEN_COL_RE.search(c)), 3)
            out = []
            for r in rows[2:]:
                if len(r) > id_idx and r[id_idx]:
                    title = r[wi_idx] if len(r) > wi_idx else ""
                    done = len(r) > dw_idx and r[dw_idx].startswith("✓")
                    out.append((r[id_idx], title, done))
            return out
    return []


def map_labels(text, heading_re):
    """The node labels of the first Mermaid block under the heading: text right after [ ( or { and a quotation mark."""
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(heading_re, line):
            block, inside = [], False
            for nxt in lines[i + 1:]:
                if nxt.startswith("```mermaid"):
                    inside = True
                elif inside and nxt.startswith("```"):
                    break
                elif inside:
                    block.append(nxt)
                elif nxt.startswith("#") and not inside:
                    break
            return [m for m in re.findall(r'(?<=[\[\(\{])"([^"]*)"', "\n".join(block))]
    return []


def squash(s):
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"[①②③④⑤⑥⑦⑧⑨⑩]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def read_project(root):
    root = pathlib.Path(root)
    P = {"product": None, "sprints": {}}
    text, product_source = find_product_log(root)
    if text is None:
        return P
    c = commitments(text)
    items = [(r[0], r[1], r[4] if len(r) > 4 else "", r[5] if len(r) > 5 else "")
             for r in table_after(text, r"^#{2,3}\s*3\.1\b") if r and r[0]]
    P["product"] = {"statement": c.get("product", ""), "goal": c.get("product_goal", ""), "items": items,
                    "closed": len([r for r in table_after(text, r"^#{2,3}\s*3\.2\b") if r and r[0]]),
                    "map_labels": map_labels(text, r"^#{2,3}\s*2\.2\b"), "source": product_source}
    for (kind, ident), info in discover(root).items():
        body = read_log(root, info["path"], info["source"])
        if body is None:
            continue
        if kind == "sprint":
            P["sprints"][ident] = {
                "source": info["source"], "goal": commitments(body).get("sprint_goal", ""), "now": now_line(body),
                "items": [r[0] for r in table_after(body, r"^#{2,3}\s*2\.1\b") if r and r[0]],
                "blocks": work_item_table(body)}
    return P


# ---------------------------------------------------------------- the page

def split_page(page):
    m = BLOCK_RE.search(page)
    return (None, None) if not m else (m.group(2), BLOCK_RE.sub(lambda x: x.group(1) + "@@DATA@@" + x.group(3), page, count=1))


def check_page(page, project, template_text=None):
    errors, warnings = [], []
    raw, shell = split_page(norm_nl(page))
    if raw is None:
        return ["no data block: <script type=\"application/json\" id=\"board-data\"> is missing"], warnings
    if PLACEHOLDER in raw:
        return ["the data block still holds the template placeholder"], warnings
    if re.search(r"</script|<!--", raw, re.I):
        errors.append("the data block holds a raw </script or <!--; every < must be written as backslash-u003c")
    elif "<" in raw:
        warnings.append("the data block holds a raw <; convention 15 asks for backslash-u003c")
    try:
        D = json.loads(raw)
    except ValueError as e:
        return errors + ["the data block is not valid JSON: %s" % e], warnings
    if template_text is not None:
        _, tshell = split_page(norm_nl(template_text))
        if tshell is not None and tshell != shell:
            errors.append("the page differs from the template outside the data block (a character was lost or changed)")
    P = read_project(project)
    if P["product"] is None:
        return errors + ["no scrum/ProductBacklog.md in the project"], warnings
    check_data(D, P, errors, warnings)
    return errors, warnings


def eq(errors, label, got, want):
    if got != want:
        errors.append("%s: the page has %r, the log has %r" % (label, got, want))


def in_map(text, labels):
    flat = [squash(x) for x in labels]
    whole = squash(text)
    if any(whole in f for f in flat):
        return True
    parts = [p.strip() for p in whole.split("→") if p.strip()]
    return bool(parts) and all(any(p in f for f in flat) for p in parts)


def stop_warnings(text):
    """A map stop is a few words (board-log.md, convention 12): flag a label copied whole."""
    out = []
    if len(text) > 30:
        out.append("is %d characters long; cut it to a few words" % len(text))
    if re.search(r"[①②③④⑤⑥⑦⑧⑨⑩]", text):
        out.append("still has the step number")
    if re.search(r"[（(]", text):
        out.append("still has a bracket")
    return out


def check_data(D, P, errors, warnings):
    if not isinstance(D, dict):
        errors.append("the data is not an object")
        return
    if D.get("lang") not in ("zh", "en"):
        errors.append("lang must be zh or en, not %r" % D.get("lang"))
    if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", str(D.get("generated", ""))):
        errors.append("generated must be YYYY-MM-DD HH:MM, not %r" % D.get("generated"))
    for key in ("items", "sprints"):
        if not isinstance(D.get(key), list):
            errors.append("%s must be a list" % key)
            return
    prod, pp = D.get("product"), P["product"]
    if not isinstance(prod, dict):
        errors.append("product must be an object")
        return
    eq(errors, "product.statement", prod.get("statement"), pp["statement"])
    eq(errors, "product.goal", prod.get("goal"), pp["goal"])
    if not prod.get("name") or str(prod["name"]) not in pp["statement"]:
        errors.append("product.name %r is not found in the Product commitment" % prod.get("name"))
    eq(errors, "product.source", prod.get("source"), pp["source"])
    eq(errors, "product.closed", prod.get("closed"), pp["closed"])

    # items: the same rows, in the same order
    want = [{"id": i[0], "title": i[1], "status": i[2], "size": i[3]} for i in pp["items"]]
    got = [{k: it.get(k) for k in ("id", "title", "status", "size")} for it in D["items"] if isinstance(it, dict)]
    if got != want:
        gid, wid = [g["id"] for g in got], [w["id"] for w in want]
        if gid != wid:
            errors.append("items: the page lists %s, the log lists %s" % (gid, wid))
        for g, w in zip(got, want):
            if g["id"] == w["id"] and g != w:
                errors.append("items %s: the page has %r, the log has %r" % (w["id"], g, w))
    in_sprint = {i for s in D["sprints"] if isinstance(s, dict) for i in (s.get("items") or [])}
    for it in D["items"]:
        g, ident = it.get("group"), it.get("id")
        if g not in GROUPS:
            errors.append("item %s: group %r is not one of %s" % (ident, g, "/".join(GROUPS)))
        elif (g == "sprint") != (ident in in_sprint):
            errors.append("item %s: group %r does not match the Sprints (in a Sprint's items: %s)" % (ident, g, ident in in_sprint))

    # the map of the product
    stops = prod.get("map") if isinstance(prod.get("map"), list) else []
    if not isinstance(prod.get("map"), list):
        errors.append("product.map must be a list")
    if stops and not 2 <= len(stops) <= 10:
        warnings.append("product.map has %d stops; five to eight is meant" % len(stops))
    ids = {s.get("id") for s in D["sprints"] if isinstance(s, dict)}
    for i, stop in enumerate(stops):
        if not isinstance(stop, dict) or not str(stop.get("text", "")).strip():
            errors.append("product.map[%d] needs a text" % i)
            continue
        if not in_map(stop["text"], pp["map_labels"]):
            errors.append("product.map[%d] %r is not found in the product log's map" % (i, stop["text"]))
        for w in stop_warnings(str(stop["text"])):
            warnings.append("product.map[%d] %s" % (i, w))
        for num in re.findall(r"\d+", str(stop.get("note", ""))):
            if not any(num in l for l in pp["map_labels"]):
                errors.append("product.map[%d] note %r: %s is not in the map" % (i, stop.get("note"), num))
        for h in stop.get("here") or []:
            if h not in ids:
                errors.append("product.map[%d] here %r is not an open Sprint" % (i, h))

    # Sprints
    sdata = {s.get("id"): s for s in D["sprints"] if isinstance(s, dict)}
    if set(sdata) != set(P["sprints"]):
        errors.append("sprints: the page has %s, the open Sprint logs are %s" % (sorted(sdata), sorted(P["sprints"])))
    for ident, s in sdata.items():
        w = P["sprints"].get(ident)
        if not w:
            continue
        eq(errors, "sprint %s goal" % ident, s.get("goal"), w["goal"])
        eq(errors, "sprint %s now" % ident, s.get("now"), w["now"])
        eq(errors, "sprint %s items" % ident, s.get("items"), w["items"])
        eq(errors, "sprint %s source" % ident, s.get("source"), w["source"])
        blocks = [(b.get("n"), b.get("title"), b.get("done")) for b in s.get("blocks") or [] if isinstance(b, dict)]
        eq(errors, "sprint %s blocks" % ident, blocks, w["blocks"])
        known = {i[0] for i in pp["items"]}
        for i in s.get("items") or []:
            if i not in known:
                warnings.append("sprint %s: item %s is not an item that is not done" % (ident, i))


def render_counts(page_path):
    exe = next((b for b in BROWSERS if os.path.isfile(b)), None)
    if not exe:
        return None
    r = subprocess.run([exe, "--headless", "--disable-gpu", "--allow-file-access-from-files", "--virtual-time-budget=5000",
                        "--dump-dom", pathlib.Path(page_path).resolve().as_uri()], capture_output=True, timeout=120)
    dom = r.stdout.decode("utf-8", "replace")
    return {"pbi": len(re.findall(r'class="pbi[ "]', dom)), "nodes": len(re.findall(r'class="node sprint[ "]', dom)),
            "fail": re.search(r'id="app"[^>]*>\s*<div class="fail"', dom) is not None,
            "cards": len(re.findall(r'class="card"', dom))}


# ---------------------------------------------------------------- a perfect writer, and the self-test

def reference_data(root, summ):
    P = read_project(root)
    pp = P["product"]
    items = []
    for i in pp["items"]:
        in_s = any(i[0] in s["items"] for s in P["sprints"].values())
        grp = "sprint" if in_s else "later" if re.search(r"以后|later", i[2], re.I) else "next"
        items.append({"id": i[0], "title": i[1], "status": i[2], "size": i[3], "group": grp})
    name = pp["statement"].split("：")[0].split(": ")[0]
    sprints = [{"id": k, "goal": v["goal"], "now": v["now"], "items": v["items"], "source": v["source"],
                "blocks": [{"n": b[0], "title": b[1], "done": b[2]} for b in v["blocks"]]} for k, v in P["sprints"].items()]
    lang = "zh" if re.search(r"[\u4e00-\u9fff]", pp["statement"]) else "en"
    return {"lang": lang, "generated": "2026-11-24 12:00",
            "product": {"name": name, "statement": pp["statement"], "goal": pp["goal"], "source": pp["source"],
                        "map": summ.get("map", []), "closed": pp["closed"]},
            "items": items, "sprints": sprints}


def make_page(data, template_text):
    block = json.dumps(data, ensure_ascii=False, indent=1).replace("<", chr(92) + "u003c")
    assert PLACEHOLDER in template_text
    return template_text.replace(PLACEHOLDER, block)


ACME_SUMM = {
    "map": [{"text": "下单", "here": ["sprint-01-alpha"]},
            {"text": "发货", "here": ["sprint-02-beta"]}],
}


def build_fixture(name, dst, branch=False, product_branches=()):
    """Copy a fixture into dst. If branch=True, move sprint-02-beta onto its own git branch.
    If product_branches is given, put the product log only on those branches (last is newest)."""
    src = HERE / "fixtures" / name
    shutil.copytree(src, dst, dirs_exist_ok=True)
    if not (branch or product_branches):
        return dst

    def run(*a, env=None):
        subprocess.run(["git", "-C", str(dst), *a], check=True, capture_output=True, env=env)

    run("init", "-q", "-b", "main")
    run("config", "user.email", "t@t")
    run("config", "user.name", "t")
    if product_branches:
        pl = dst / PRODUCT_LOG
        pl_text = pl.read_text(encoding="utf-8")
        pl.unlink()
        (dst / ".keep").write_text("base\n", encoding="utf-8")
        run("add", ".")
        run("commit", "-qm", "base without product log")
        for idx, bname in enumerate(product_branches):
            run("checkout", "-qb", bname, "main")
            pl.write_text(pl_text, encoding="utf-8")
            run("add", PRODUCT_LOG)
            stamp = "2026-11-14T12:0%d:00Z" % idx
            env = {**os.environ, "GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp}
            run("commit", "-qm", "product log on " + bname, env=env)
        run("checkout", "-q", "main")
        return dst
    s2 = dst / "scrum/sprint-02-beta"
    tmp = dst.parent / "_s2"
    shutil.move(str(s2), str(tmp))
    run("add", ".")
    run("commit", "-qm", "base")
    run("checkout", "-qb", "sprint-02-beta")
    shutil.move(str(tmp), str(s2))
    run("add", ".")
    run("commit", "-qm", "sprint 2")
    run("checkout", "-q", "main")
    return dst


def selftest():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    tmp = tempfile.mkdtemp(prefix="board-selftest-")
    failures, cases = [], 0

    def check(label, data=None, page=None, project=None, want_ok=True, expect="", expect_warning=""):
        nonlocal cases
        cases += 1
        p = page if page is not None else make_page(data, tpl)
        errs, warns = check_page(p, project, tpl)
        ok = not errs
        if ok != want_ok:
            failures.append("%s: expected ok=%s, got ok=%s (errors=%s)" % (label, want_ok, ok, errs))
        elif expect and not any(expect in e for e in errs):
            failures.append("%s: expected error containing %r, got %s" % (label, expect, errs))
        elif expect_warning and not any(expect_warning in w for w in warns):
            failures.append("%s: expected warning containing %r, got %s" % (label, expect_warning, warns))

    def card_data(data, ident):
        return next(c for c in data["sprints"] if c["id"] == ident)

    try:
        acme = build_fixture("acme", pathlib.Path(tmp) / "acme")
        ref = reference_data(acme, ACME_SUMM)
        check("acme reference passes", ref, project=acme)

        blank = build_fixture("blank", pathlib.Path(tmp) / "blank")
        check("blank project passes", reference_data(blank, {}), project=blank)

        # Legacy design-* and ideo-* folders must be ignored by discovery and board data.
        legacy = build_fixture("acme", pathlib.Path(tmp) / "legacy")
        (legacy / "scrum/design-old").mkdir(parents=True)
        (legacy / "scrum/design-old/DesignBacklog.md").write_text(
            "# Design Backlog — old\n\n### 1.2 Design goal\n\n| 承诺 | 旧设计目标 |\n| --- | --- |\n", encoding="utf-8")
        (legacy / "scrum/ideo-notes").mkdir(parents=True)
        (legacy / "scrum/ideo-notes/IdeoBacklog.md").write_text(
            "# IDEO Backlog — notes\n\n> For: ../sprint-01-alpha/SprintBacklog.md\n> Now: Empathize\n", encoding="utf-8")
        lref = reference_data(legacy, ACME_SUMM)
        cases += 1
        if set(k for k, _ in discover(legacy)) != {"sprint"}:
            failures.append("legacy discovery found non-sprint logs: %r" % list(discover(legacy)))
        check("legacy design-* and ideo-* ignored", lref, project=legacy)

        # PBI-106: Chapter 3 with a solution comparison table BEFORE the work-item table, and Chapter 3 without a work-item table.
        how_proj = build_fixture("acme", pathlib.Path(tmp) / "howcase")
        s1_path = how_proj / "scrum/sprint-01-alpha/SprintBacklog.md"
        s1_text = s1_path.read_text(encoding="utf-8")
        comparison_tbl = (
            "## 3. How\n\n"
            "**方案对比**\n\n"
            "| 方案 | 优点 | 缺点 |\n"
            "| --- | --- | --- |\n"
            "| A 方案 | 简单 | 扩展弱 |\n"
            "| B 方案 | 灵活 | 略重 |\n\n"
        )
        s1_path.write_text(s1_text.replace("## 3. How\n", comparison_tbl, 1), encoding="utf-8")
        s2_path = how_proj / "scrum/sprint-02-beta/SprintBacklog.md"
        s2_path.write_text(re.sub(
            r"## 3\. How[\s\S]*?(?=## 4\.)",
            "## 3. How\n\n方案对比仅用正文写清，不设工作项表。\n\n| Option | Pros | Cons |\n| --- | --- | --- |\n| X | fast | rough |\n\nGo-ahead: 2026-11-24\n\n",
            s2_path.read_text(encoding="utf-8"),
        ), encoding="utf-8")
        href = reference_data(how_proj, ACME_SUMM)
        cases += 1
        s1_blocks = card_data(href, "sprint-01-alpha")["blocks"]
        s2_blocks = card_data(href, "sprint-02-beta")["blocks"]
        if len(s1_blocks) != 3 or s1_blocks[0]["n"] != "1" or not s1_blocks[0]["done"]:
            failures.append("PBI-106 table after comparison table failed: %r" % s1_blocks)
        if s2_blocks != []:
            failures.append("PBI-106 chapter 3 without work-item table expected [], got %r" % s2_blocks)
        check("PBI-106 solution tables in How pass", href, project=how_proj)

        # Codex review regressions: escaped pipe \| in cells, non-default column order, and ### 3. subheading interference.
        edge_proj = build_fixture("acme", pathlib.Path(tmp) / "edgecase")
        ep_path = edge_proj / "scrum/ProductBacklog.md"
        ep_text = ep_path.read_text(encoding="utf-8")
        # Plant an escaped pipe in a ProductBacklog item title (exercises table_after)
        ep_path.write_text(ep_text.replace("| PBI-1 | ", "| PBI-1 | A \\| B ", 1), encoding="utf-8")
        es1_path = edge_proj / "scrum/sprint-01-alpha/SprintBacklog.md"
        es1_text = es1_path.read_text(encoding="utf-8")
        # Plant a `### 3.` subheading inside chapter 2 before `## 3. How`, and reorder columns + include \| in `## 3. How`
        distractor_sub = (
            "### 3. 备忘干扰项\n\n"
            "| # | Work item | Output | Done when |\n"
            "| --- | --- | --- | --- |\n"
            "| 99 | 误命中子标题 | bad | ✓ 2026-11-24 |\n\n"
            "## 3. How\n\n"
            "| Work item | # | Done when | Output |\n"
            "| --- | --- | --- | --- |\n"
            "| 改 `a \\| b` 逻辑 | 1 | ✓ 2026-11-24 | `x \\| y` |\n"
            "| 补测用例 | 2 | 测试通过 | 脚本 |\n\n"
            "Go-ahead: 2026-11-24\n\n"
        )
        es1_path.write_text(
            re.sub(r"## 3\. How[\s\S]*?(?=## 4\.)", distractor_sub, es1_text),
            encoding="utf-8",
        )
        eref = reference_data(edge_proj, ACME_SUMM)
        cases += 3
        epbi1 = next((it for it in eref["items"] if it["id"] == "PBI-1"), None)
        if not epbi1 or "A | B " not in epbi1["title"] or epbi1["group"] != "sprint":
            failures.append("escaped pipe in ProductBacklog table_after failed: %r" % epbi1)
        eblocks = card_data(eref, "sprint-01-alpha")["blocks"]
        want_eblocks = [
            {"n": "1", "title": "改 `a | b` 逻辑", "done": True},
            {"n": "2", "title": "补测用例", "done": False},
        ]
        if eblocks != want_eblocks:
            failures.append("escaped pipe / column order / ### 3. guard failed: got %r, want %r" % (eblocks, want_eblocks))
        if any(b["n"] == "99" for b in eblocks):
            failures.append("### 3. subheading interference leaked into work_item_table: %r" % eblocks)
        check("escaped pipe, non-default column order, and ### 3. guard pass", eref, project=edge_proj)

        # Archived sprint logs under scrum/documents/ must not be discovered.
        archived = legacy / "scrum/documents/sprint-99-old"
        archived.mkdir(parents=True)
        shutil.copy(legacy / "scrum/sprint-01-alpha/SprintBacklog.md", archived / "SprintBacklog.md")
        cases += 1
        if any("99" in ident for _, ident in discover(legacy)):
            failures.append("archived sprint under scrum/documents/ was discovered")

        # Branch discovery
        br_dir = pathlib.Path(tmp) / "branchcase"
        br_dir.mkdir()
        branch = build_fixture("acme", br_dir, branch=True)
        bref = reference_data(branch, ACME_SUMM)
        check("branch case reference passes", bref, project=branch)
        sp2 = card_data(bref, "sprint-02-beta")
        cases += 1
        if not sp2["source"].startswith("branch "):
            failures.append("branch case: sprint-02 was not found on its branch (%s)" % sp2["source"])

        def mutate(label, fn, expect, base=ref, project=acme):
            d = copy.deepcopy(base)
            fn(d)
            check(label, d, project=project, want_ok=False, expect=expect)

        mutate("a branch source for a product log in working copy",
               lambda d: d["product"].update(source="branch main @ 1234567"), "product.source")

        # Product log only on branches
        pb_dir = pathlib.Path(tmp) / "productbranch"
        pb_dir.mkdir()
        pb = build_fixture("acme", pb_dir, product_branches=("product-old", "product-new"))

        def tip(branch_name):
            return subprocess.run(["git", "-C", str(pb), "rev-parse", branch_name], capture_output=True, text=True,
                                  check=True).stdout.strip()

        pbref = reference_data(pb, ACME_SUMM)
        want_source = "branch product-new @ " + tip("product-new")[:7]
        cases += 1
        if pbref["product"]["source"] != want_source:
            failures.append("product branch case: expected %r, got %r" % (want_source, pbref["product"]["source"]))
        check("product log only on a branch passes", pbref, project=pb)
        mutate("product log only on a branch says working copy",
               lambda d: d["product"].update(source="working copy"), "product.source", base=pbref, project=pb)
        mutate("product log on older branch",
               lambda d: d["product"].update(source="branch product-old @ " + tip("product-old")[:7]), "product.source",
               base=pbref, project=pb)
        mutate("product log wrong commit",
               lambda d: d["product"].update(source="branch product-new @ 1234567"), "product.source",
               base=pbref, project=pb)

        mutate("a character of the Product changed", lambda d: d["product"].update(statement=d["product"]["statement"] + "。"), "product.statement")
        mutate("a character of the Product Goal changed", lambda d: d["product"].update(goal=d["product"]["goal"].rstrip("）")), "product.goal")
        mutate("a wrong product name", lambda d: d["product"].update(name="Other"), "product.name")
        mutate("a wrong closed count", lambda d: d["product"].update(closed=99), "product.closed")
        mutate("an item omitted", lambda d: d["items"].pop(), "items:")
        mutate("an item reworded", lambda d: d["items"][0].update(title="列表"), "items PBI-1")
        mutate("an item in the wrong group", lambda d: d["items"][0].update(group="next"), "group")
        mutate("an obsolete design group rejected", lambda d: d["items"][2].update(group="design"), "not one of sprint/next/later")
        mutate("an invented map stop", lambda d: d["product"]["map"].append({"text": "不存在的站"}), "not found in the product log")
        mutate("an invented map note", lambda d: d["product"]["map"][0].update(note="999"), "not in the map")
        mutate("an invented here id", lambda d: d["product"]["map"][0].update(here=["sprint-99-nope"]), "not an open Sprint")
        mutate("a Sprint omitted", lambda d: d["sprints"].pop(), "sprints:")
        mutate("a Sprint Goal changed", lambda d: card_data(d, "sprint-01-alpha").update(goal="改写"), "sprint sprint-01-alpha goal")
        mutate("a Sprint Now changed", lambda d: card_data(d, "sprint-01-alpha").update(now="改写"), "sprint sprint-01-alpha now")
        mutate("a Sprint item changed", lambda d: card_data(d, "sprint-01-alpha").update(items=["PBI-2"]), "sprint sprint-01-alpha items")
        mutate("a Sprint source changed", lambda d: card_data(d, "sprint-01-alpha").update(source="branch x @ 1234567"), "sprint sprint-01-alpha source")
        mutate("a Sprint block done flipped", lambda d: card_data(d, "sprint-01-alpha")["blocks"][0].update(done=False), "sprint sprint-01-alpha blocks")
        mutate("a bad time", lambda d: d.update(generated="today"), "generated")
        mutate("a bad lang", lambda d: d.update(lang="fr"), "lang")

        good = make_page(ref, tpl)
        check("a character lost from the template", page=good.replace("flex-wrap:wrap", "flex-wrp:wrap", 1), project=acme, want_ok=False, expect="template")
        check("a raw </script in a text", page=good.replace('"下单"', '"下</script>单"', 1), project=acme, want_ok=False, expect="</script")
        check("the placeholder left in", page=tpl, project=acme, want_ok=False, expect="placeholder")
        check("no data block", page="<html></html>", project=acme, want_ok=False, expect="no data block")
        check("invalid JSON", page=good.replace('"lang": "zh"', '"lang": zh', 1), project=acme, want_ok=False, expect="JSON")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps({"selftest": "ok" if not failures else "FAILED", "cases": cases, "failures": failures}, ensure_ascii=False, indent=1))
    return 0 if not failures else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--project", required=True)
    c.add_argument("--page")
    c.add_argument("--template", default=str(TEMPLATE))
    c.add_argument("--render", action="store_true")
    r = sub.add_parser("ref")
    r.add_argument("--project", required=True)
    r.add_argument("--summaries", required=True)
    r.add_argument("--out", required=True)
    sub.add_parser("selftest")
    a = ap.parse_args()
    if a.cmd == "selftest":
        return selftest()
    if a.cmd == "ref":
        summ = json.loads(pathlib.Path(a.summaries).read_text(encoding="utf-8"))
        try:
            data = reference_data(a.project, summ)
        except ValueError as e:
            ap.error(str(e))
        pathlib.Path(a.out).write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("wrote", a.out)
        return 0
    page = pathlib.Path(a.page) if a.page else pathlib.Path(a.project) / "scrum/ScrumBoard.html"
    if not page.is_file():
        print(json.dumps({"ok": False, "errors": ["no page at %s" % page]}))
        return 1
    tpl = pathlib.Path(a.template).read_text(encoding="utf-8") if a.template and pathlib.Path(a.template).is_file() else None
    errors, warnings = check_page(page.read_text(encoding="utf-8"), a.project, tpl)
    out = {"ok": not errors, "errors": errors, "warnings": warnings}
    if a.render:
        counts = render_counts(page)
        out["render"] = counts
        if counts is None:
            out["warnings"].append("no browser found, the page was not opened")
        elif counts["fail"] or not counts["cards"]:
            out["errors"].append("the page opened but shows a message instead of the board: %s" % counts)
            out["ok"] = False
        else:
            try:
                raw, _ = split_page(norm_nl(page.read_text(encoding="utf-8")))
                D = json.loads(raw)
                drawn = {"pbi": len(D["items"]), "nodes": len(D["sprints"]),
                         "cards": 1 + len(D["sprints"])}
                for key, want in drawn.items():
                    if counts[key] != want:
                        out["errors"].append("the page drew %r %s, the data has %r" % (counts[key], key, want))
                        out["ok"] = False
            except (ValueError, KeyError, TypeError):
                pass  # the data errors are already reported above
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
