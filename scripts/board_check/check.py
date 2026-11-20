"""Check a written scrum/ScrumBoard.html against the project's logs (acceptance 68-4).

    python -X utf8 -I scripts/board_check/check.py check --project DIR [--page FILE] [--template FILE] [--render]
    python -X utf8 -I scripts/board_check/check.py selftest
    python -X utf8 -I scripts/board_check/check.py ref --project DIR --summaries FILE --out FILE

`check` compares the data block with the logs and the rest of the page with the template. It checks copied fields,
map labels, sources, design solution structure, and IDEO log placement. It does not judge whether a summary makes
sense or follows the map's main line. `--render` counts the rendered elements, not their visual readability.

`selftest` checks reference pages for fixture projects and verifies that deliberate data errors are reported.
`ref` writes a data file from the logs and supplied summaries; give each design a solution object or an explicit null.
"""
import argparse
import copy
import json
import os
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
TEMPLATE = REPO / "plugins/ideo-scrum/skills/scrum-kernel/conventions/scrum-board-template.html"
PLACEHOLDER = '{"todo": "Replace this line with the board data (board-log.md lists the fields)."}'
# the data block runs to the next script, so a stray </script> inside the data cannot hide itself
BLOCK_RE = re.compile(r'(<script type="application/json" id="board-data">)(.*?)(</script>\s*<script>)', re.S)
LOG_FILES = {"sprint": "SprintBacklog.md", "design": "DesignBacklog.md", "ideo": "IdeoBacklog.md"}
PATHS = {k: re.compile(r"^scrum/(%s-[^/]+)/%s$" % (k, v)) for k, v in LOG_FILES.items()}
GROUPS = ("sprint", "design", "next", "later")
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
    """The open Sprint, design, and IDEO logs: in the working copy, else on a branch (the newest commit wins)."""
    root = pathlib.Path(root)
    found = {}
    scrum = root / "scrum"
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


def commitments(text):
    """{kind: exact text} from the one-row tables whose first cell is Commitment / 承诺; the heading says which.
    A heading may be left in English or put into Chinese (产品, 产品目标, 冲刺目标, 设计目标): a stranger's AI writing
    the log in Chinese translated "1.1 Product" to "1.1 产品" (formal run 1, 2026-11-14), which the commitments hook
    (commitments.sh) reads, and this check has to read too."""
    out, head = {}, ""
    for line in text.split("\n"):
        if line.startswith("#"):
            head = line.lstrip("# ").strip()
        m = re.match(r"^\|\s*(?:Commitment|承诺)\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            h = head.lower()
            kind = ("sprint_goal" if ("sprint goal" in h or "冲刺目标" in h)
                    else "product_goal" if ("product goal" in h or "产品目标" in h)
                    else "design_goal" if ("design goal" in h or "设计目标" in h)
                    else "product" if ("product" in h or "产品" in h) else "")
            if kind and kind not in out:
                out[kind] = m.group(1)
    return out


def now_line(text):
    m = re.search(r"^> Now:\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def header_field(text, name):
    m = re.search(r"^>.*?\b%s:\s*([^|\n]*)" % name, text, re.M)
    return m.group(1).strip() if m else ""


def ideo_host(text, log_path):
    value = header_field(text, "For")
    link = re.fullmatch(r"\[[^\]]*\]\(([^)]+)\)", value)
    value = (link[1] if link else value.strip("`")).strip().replace("\\", "/")
    path = posixpath.normpath(value)
    if not path.startswith("scrum/"):
        path = posixpath.normpath(posixpath.join(posixpath.dirname(log_path), path))
    for kind in ("sprint", "design"):
        match = PATHS[kind].fullmatch(path)
        if match:
            return kind + "s", match[1]
    return None


def ideo_concluded(now):
    # 只识别状态开头的明确收尾，不把正文里的 finished work 或待收尾当成结论。
    return bool(re.match(
        r"^(?:(?:Empathize|Define|Ideate|Prototype|Test|共情|定义|构思|原型|测试)\s*[:：]\s*)?"
        r"(?:(?:this run (?:is|has been)\s+)?(?:concluded|closed)|(?:本轮|本次)?已(?:收尾|结束|关闭))"
        r"(?=$|\s*(?:[.。:：·,，—–;；（(]|-\s|\d{4}-\d{2}-\d{2}\b))",
        now, re.I,
    ))


def table_after(text, heading_re):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(heading_re, line):
            rows = []
            for nxt in lines[i + 1:]:
                if nxt.startswith("|"):
                    rows.append([c.strip() for c in nxt.strip().strip("|").split("|")])
                elif rows:
                    break
                elif nxt.startswith("#"):
                    break
            return rows[2:]
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


def has_section_content(text, number):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    start = re.search(r"^(#{2,6})[ \t]+" + re.escape(number) + r"(?=[ \t.:：]|$)[^\n]*$", text, re.M)
    if not start:
        return False
    following = text[start.end():]
    end = re.search(r"^#{1,%d}[ \t]+" % len(start.group(1)), following, re.M)
    return bool((following[:end.start()] if end else following).strip())


def squash(s):
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"[①②③④⑤⑥⑦⑧⑨⑩]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def has_id(text, item_id):
    return re.search(r"(?<![A-Za-z0-9])%s(?![0-9])" % re.escape(item_id), text) is not None


def read_project(root):
    root = pathlib.Path(root)
    P = {"product": None, "sprints": {}, "designs": {}, "ideo": {}}
    pl = root / "scrum/ProductBacklog.md"
    if not pl.is_file():
        return P
    text = norm_nl(pl.read_text(encoding="utf-8"))
    c = commitments(text)
    items = [(r[0], r[1], r[4] if len(r) > 4 else "", r[5] if len(r) > 5 else "")
             for r in table_after(text, r"^#{2,3}\s*3\.1\b") if r and r[0]]
    P["product"] = {"statement": c.get("product", ""), "goal": c.get("product_goal", ""), "items": items,
                    "closed": len([r for r in table_after(text, r"^#{2,3}\s*3\.2\b") if r and r[0]]),
                    "map_labels": map_labels(text, r"^#{2,3}\s*2\.2\b")}
    for (kind, ident), info in discover(root).items():
        body = read_log(root, info["path"], info["source"])
        if body is None:
            continue
        if kind == "sprint":
            P["sprints"][ident] = {
                "source": info["source"], "goal": commitments(body).get("sprint_goal", ""), "now": now_line(body),
                "items": [r[0] for r in table_after(body, r"^#{2,3}\s*2\.1\b") if r and r[0]],
                "blocks": [(r[0], r[1], len(r) > 3 and r[3].startswith("✓"))
                           for r in table_after(body, r"^#{2,3}\s*3\.") if r and r[0]]}
        elif kind == "design":
            frm = header_field(body, "From")
            P["designs"][ident] = {
                "source": info["source"], "goal": commitments(body).get("design_goal", ""), "now": now_line(body),
                "for": [i[0] for i in items if has_id(frm, i[0])],
                "map_labels": map_labels(body, r"^#{2,3}\s*2\.1\b"),
                "has_solution_section": has_section_content(body, "3.1"),
                "has_storyboard_section": has_section_content(body, "3.2")}
        else:
            P["ideo"][ident] = {"now": now_line(body), "host": ideo_host(body, info["path"])}
    return P


def expected_ideo(project):
    """按看板约定 11、16 得到每条应展示的 IDEO 日志唯一的宿主和 Now。"""
    expected = {}
    for ident, log in project["ideo"].items():
        host = log["host"]
        if host and host[1] in project[host[0]] and not ideo_concluded(log["now"]):
            expected[ident] = host[1], log["now"]
    return expected


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
    check_data(D, P, errors, warnings, separate_solution=uses_solution_data(template_text))
    return errors, warnings


def uses_solution_data(template_text):
    # 历史体验测试显式传入当时的模板，不能用新版字段要求倒判旧页面。
    return template_text is None or "data-solution" in template_text


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


def check_data(D, P, errors, warnings, *, separate_solution=True):
    if not isinstance(D, dict):
        errors.append("the data is not an object")
        return
    if D.get("lang") not in ("zh", "en"):
        errors.append("lang must be zh or en, not %r" % D.get("lang"))
    if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", str(D.get("generated", ""))):
        errors.append("generated must be YYYY-MM-DD HH:MM, not %r" % D.get("generated"))
    for key in ("items", "sprints", "designs"):
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
    eq(errors, "product.source", prod.get("source"), "working copy")
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
    in_design = {i for d in D["designs"] if isinstance(d, dict) for i in (d.get("for") or [])}
    for it in D["items"]:
        g, ident = it.get("group"), it.get("id")
        if g not in GROUPS:
            errors.append("item %s: group %r is not one of %s" % (ident, g, "/".join(GROUPS)))
        elif (g == "sprint") != (ident in in_sprint):
            errors.append("item %s: group %r does not match the Sprints (in a Sprint's items: %s)" % (ident, g, ident in in_sprint))
        elif g == "design" and ident not in in_design:
            errors.append("item %s: group design, but no design is for it" % ident)
        elif g in ("next", "later") and ident in in_design:
            errors.append("item %s: a design is for it, so its group is design" % ident)

    # the map of the product
    stops = prod.get("map") if isinstance(prod.get("map"), list) else []
    if not isinstance(prod.get("map"), list):
        errors.append("product.map must be a list")
    if stops and not 2 <= len(stops) <= 10:
        warnings.append("product.map has %d stops; five to eight is meant" % len(stops))
    ids = {s.get("id") for s in D["sprints"] if isinstance(s, dict)} | {d.get("id") for d in D["designs"] if isinstance(d, dict)}
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
                errors.append("product.map[%d] here %r is not an open Sprint or design" % (i, h))

    listed = {h for stop in stops if isinstance(stop, dict) for h in (stop.get("here") or [])}
    for d in D["designs"]:
        if isinstance(d, dict) and stops and d.get("id") not in listed:
            warnings.append("design %s is open but no stop of product.map lists it in here" % d.get("id"))

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

    # designs
    ddata = {d.get("id"): d for d in D["designs"] if isinstance(d, dict)}
    if set(ddata) != set(P["designs"]):
        errors.append("designs: the page has %s, the open design logs are %s" % (sorted(ddata), sorted(P["designs"])))
    for ident, d in ddata.items():
        w = P["designs"].get(ident)
        if not w:
            continue
        eq(errors, "design %s goal" % ident, d.get("goal"), w["goal"])
        eq(errors, "design %s now" % ident, d.get("now"), w["now"])
        eq(errors, "design %s for" % ident, d.get("for"), w["for"])
        eq(errors, "design %s source" % ident, d.get("source"), w["source"])
        route = d.get("map", [])
        if not isinstance(route, list):
            errors.append("design %s map must be a list of stop texts" % ident)
        elif not route and w["map_labels"]:
            errors.append("design %s map is empty but section 2.1 contains a map" % ident)
        else:
            for i, node in enumerate(route):
                if not isinstance(node, str) or not node.strip() or not in_map(node, w["map_labels"]):
                    errors.append("design %s map[%d] %r is not found in the design log's map" % (ident, i, node))
                    continue
                for wn in stop_warnings(node):
                    warnings.append("design %s map[%d] %s" % (ident, i, wn))
        # 只自动核结构与有无出处，摘要意思和地图主线的顺序交给读卡和源文对账。
        solution = d.get("solution")
        if separate_solution:
            if "solution" not in d:
                errors.append("design %s needs a solution object or an explicit null" % ident)
            elif solution is None and w["has_solution_section"]:
                warnings.append("design %s: section 3.1 has content; verify that it records no chosen solution" % ident)
            elif solution is not None:
                if (not isinstance(solution, dict) or not solution or solution.keys() - {"title", "text"}
                        or any(not isinstance(v, str) or not v.strip() for v in solution.values())):
                    errors.append("design %s solution needs a nonempty title or text" % ident)
                elif not w["has_solution_section"]:
                    errors.append("design %s solution has no source in section 3.1" % ident)
        story = d.get("story", [])
        if (not isinstance(story, list) or any(not isinstance(x, dict) or
                any(not isinstance(x.get(k), str) or not x[k].strip() for k in ("title", "text")) for x in story)):
            errors.append("design %s story must be a list of frames with a title and a text" % ident)
        elif separate_solution and story and (solution is None or not w["has_storyboard_section"]):
            errors.append("design %s story needs a chosen solution and a source in section 3.2" % ident)

    # 保留全部挂载，避免后出现的正确宿主覆盖先出现的错误宿主。
    placed = {}
    owners = [("product", prod)] + [(v.get("id"), v) for v in D["sprints"] + D["designs"] if isinstance(v, dict)]
    for owner_id, owner in owners:
        entries = owner.get("ideo", [])
        if not isinstance(entries, list):
            errors.append("ideo under %s must be a list" % owner_id)
            continue
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get("id"), str) or not entry["id"]:
                errors.append("ideo under %s needs a log id" % owner_id)
                continue
            placed.setdefault(entry["id"], []).append((owner_id, entry.get("now")))
    expected = expected_ideo(P)
    for ident, (host, now) in expected.items():
        locations = placed.get(ident, [])
        if not locations:
            errors.append("ideo %s: the open host %s is missing this log" % (ident, host))
        elif len(locations) != 1:
            errors.append("ideo %s: appears more than once; it belongs only under %s" % (ident, host))
        else:
            actual_host, actual_now = locations[0]
            eq(errors, "ideo %s host" % ident, actual_host, host)
            eq(errors, "ideo %s now" % ident, actual_now, now)
    for ident in placed.keys() - expected.keys():
        errors.append("ideo %s: shown but not eligible for the board" % ident)


def render_counts(page_path):
    exe = next((b for b in BROWSERS if os.path.isfile(b)), None)
    if not exe:
        return None
    r = subprocess.run([exe, "--headless", "--disable-gpu", "--allow-file-access-from-files", "--virtual-time-budget=5000",
                        "--dump-dom", pathlib.Path(page_path).resolve().as_uri()], capture_output=True, timeout=120)
    dom = r.stdout.decode("utf-8", "replace")
    # the noscript note also says class="fail"; what counts is a message in place of the board inside #app
    return {"pbi": len(re.findall(r'class="pbi[ "]', dom)), "nodes": len(re.findall(r'class="node (?:sprint|design)[ "]', dom)),
            "fail": re.search(r'id="app"[^>]*>\s*<div class="fail"', dom) is not None,
            "cards": len(re.findall(r'class="card"', dom)),
            "solutions": dict(Counter(re.findall(r'<div\b[^>]*\bdata-solution="([a-z]+)"', dom))),
            "storyboards": len(re.findall(r'<details class="design-story">', dom))}


# ---------------------------------------------------------------- a perfect writer, and the self-test

def reference_data(root, summ):
    P = read_project(root)
    pp = P["product"]
    items = []
    for i in pp["items"]:
        in_s = any(i[0] in s["items"] for s in P["sprints"].values())
        in_d = any(i[0] in d["for"] for d in P["designs"].values())
        grp = "sprint" if in_s else "design" if in_d else "later" if re.search(r"以后|later", i[2], re.I) else "next"
        items.append({"id": i[0], "title": i[1], "status": i[2], "size": i[3], "group": grp})
    name = pp["statement"].split("：")[0].split(": ")[0]
    sprints = [{"id": k, "goal": v["goal"], "now": v["now"], "items": v["items"], "source": v["source"],
                "blocks": [{"n": b[0], "title": b[1], "done": b[2]} for b in v["blocks"]]} for k, v in P["sprints"].items()]
    designs = []
    design_summaries = summ.get("designs", {})
    for k, v in P["designs"].items():
        summary = design_summaries.get(k, {})
        if "solution" not in summary:
            raise ValueError("design %s: summaries need a solution object or an explicit null; reread section 3.1" % k)
        if v["map_labels"] and not summary.get("map"):
            raise ValueError("design %s: summaries need the route from section 2.1" % k)
        design = {"id": k, "for": v["for"], "goal": v["goal"], "now": v["now"], "source": v["source"],
                  "solution": summary["solution"]}
        for key in ("map", "story"):
            if key in summary:
                design[key] = summary[key]
        designs.append(design)
    by_id = {x["id"]: x for x in sprints + designs}
    for ident, (host, now) in expected_ideo(P).items():
        by_id[host].setdefault("ideo", []).append({"id": ident, "now": now})
    lang = "zh" if re.search(r"[\u4e00-\u9fff]", pp["statement"]) else "en"
    return {"lang": lang, "generated": "2026-11-14 12:00",
            "product": {"name": name, "statement": pp["statement"], "goal": pp["goal"], "source": "working copy",
                        "map": summ.get("map", []), "closed": pp["closed"]},
            "items": items, "sprints": sprints, "designs": designs}


def make_page(data, template_text):
    block = json.dumps(data, ensure_ascii=False, indent=1).replace("<", chr(92) + "u003c")
    assert PLACEHOLDER in template_text
    return template_text.replace(PLACEHOLDER, block)


ACME_SUMM = {
    "map": [{"text": "下单", "here": ["sprint-01-alpha"]},
            {"text": "发货", "here": ["sprint-02-beta"]},
            {"text": "设计冲刺", "branch": True,
             "here": ["design-gamma", "design-feedback-sample", "design-choosing"]}],
    "designs": {
        "design-gamma": {
            "map": ["单子失败", "筛出失败批次", "重试", "查看重试结果", "确认成功或放弃"],
            "solution": {"title": "分批重试流程", "text": "失败的批次单独重试，成功的批次不动。"},
            "story": [{"title": "发现失败", "text": "店员在订单台看到失败的批次。"},
                      {"title": "单独重试", "text": "店员只重试失败批次，成功批次无需重试。"}]},
        "design-feedback-sample": {
            "map": ["用产品时发现问题", "交给手边的 AI", "记下反馈", "在会话里用上反馈", "更新产品时取回"],
            "solution": {"title": "记一下就够：全局说明管路线，反馈进全局记忆",
                         "text": "PO 只说「记一下」，不用报位置；手边的 AI 按产品记入全局记忆。"
                                 "反馈在会话里马上生效，更新产品时集中取回，由 PO 决定要改什么。"}},
        "design-choosing": {
            "map": ["打开订单", "提交退款申请", "查看退款进度", "收到退款通知", "核对退款去向"],
            "solution": None}
    }
}


def build_fixture(name, workdir, branch=False):
    dest = pathlib.Path(workdir) / name
    shutil.copytree(HERE / "fixtures" / name, dest)
    if branch:
        env = ["-c", "user.name=t", "-c", "user.email=t@example.com", "-c", "commit.gpgsign=false"]

        def g(*a):
            subprocess.run(["git", "-C", str(dest), *env, *a], capture_output=True, check=True)
        g("init", "-q", "-b", "main")
        moved = dest / "scrum/sprint-02-beta"
        hold = pathlib.Path(workdir) / "hold"
        shutil.move(str(moved), str(hold))
        g("add", "-A")
        g("commit", "-q", "-m", "main")
        g("checkout", "-q", "-b", "sprint-02-beta")
        shutil.move(str(hold), str(moved))
        g("add", "-A")
        g("commit", "-q", "-m", "sprint 02")
        g("checkout", "-q", "main")
        shutil.rmtree(moved, ignore_errors=True)  # git already took it away; the working copy of main does not have it
    return dest


def selftest():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    failures, cases = [], 0
    tmp = tempfile.mkdtemp(prefix="bc-")
    try:
        def check(label, data=None, page=None, project=None, want_ok=True, expect="", expect_warning=""):
            nonlocal cases
            cases += 1
            text = page if page is not None else make_page(data, tpl)
            errs, warnings = check_page(text, project, tpl)
            if want_ok and errs:
                failures.append("%s: expected pass, got %s" % (label, errs[:3]))
            if not want_ok and not errs:
                failures.append("%s: damage not caught" % label)
            if not want_ok and errs and expect and not any(expect in e for e in errs):
                failures.append("%s: caught, but not by the %r check: %s" % (label, expect, errs[:2]))
            if expect_warning and not any(expect_warning in w for w in warnings):
                failures.append("%s: expected warning %r, got %s" % (label, expect_warning, warnings[:2]))

        acme = build_fixture("acme", tmp)
        ref = reference_data(acme, ACME_SUMM)
        check("acme reference passes", ref, project=acme)
        # 夹具对照只约束这份已知输入，不把固定站名或文案当成通用判据。
        expectations = json.loads((HERE / "fixtures/review-expectations.json").read_text(encoding="utf-8"))
        design_cards = {d["id"]: d for d in ref["designs"]}
        for case in expectations["cases"]:
            cases += 1
            card = design_cards.get(case["id"], {})
            actual = (card.get("goal"), card.get("map"), bool(card.get("solution")), bool(card.get("story")))
            want = (case["goal"], case["route"], case["solution_title"] is not None, case["has_storyboard"])
            if actual != want:
                failures.append("design fixture %s: expected %r, reference generated %r" % (case["case"], want, actual))
        cases += 3
        if len(stop_warnings("① 写产品日志：Product · 架构 · PBI（product-log）")) < 3:
            failures.append("a stop copied whole is not flagged")
        if stop_warnings("写产品日志"):
            failures.append("a clean stop is flagged")
        _, warns = check_page(make_page(ref, tpl), acme, tpl)
        if warns:
            failures.append("the reference page has warnings: %s" % warns[:2])
        blank = build_fixture("blank", tmp)
        check("blank reference passes", reference_data(blank, {}), project=blank)
        # a log whose headings were put into Chinese (formal run 1: "1.1 产品") reads the same as the English one
        zh_dir = pathlib.Path(tmp) / "zhcase"
        zh_dir.mkdir()
        zh = build_fixture("acme", zh_dir)
        for rel, pairs in (("scrum/ProductBacklog.md", (("## 1.1 Product", "## 1.1 产品"),
                                                         ("## 1.2 Product Goal", "## 1.2 产品目标"))),
                           ("scrum/sprint-01-alpha/SprintBacklog.md", (("### 1.1 Sprint Goal", "### 1.1 冲刺目标"),)),
                           ("scrum/sprint-02-beta/SprintBacklog.md", (("### 1.1 Sprint Goal", "### 1.1 冲刺目标"),))):
            path = zh / rel
            body = path.read_text(encoding="utf-8")
            for old, new in pairs:
                if old not in body:
                    failures.append("zh headings: %r not found in the %s fixture" % (old, rel))
                body = body.replace(old, new)
            path.write_text(body, encoding="utf-8")
        cases += 1
        en_p, zh_p = read_project(acme), read_project(zh)
        if not en_p["product"]["statement"] or not en_p["product"]["goal"]:
            failures.append("zh headings: the English fixture has no Product or Product Goal to compare with")
        if (zh_p["product"]["statement"], zh_p["product"]["goal"]) != (en_p["product"]["statement"], en_p["product"]["goal"]):
            failures.append("zh headings: 产品 / 产品目标 are not read as Product / Product Goal")
        if {k: v["goal"] for k, v in zh_p["sprints"].items()} != {k: v["goal"] for k, v in en_p["sprints"].items()} \
                or not all(v["goal"] for v in zh_p["sprints"].values()):
            failures.append("zh headings: 冲刺目标 is not read as the Sprint Goal")
        def card_data(data, ident):
            return next(c for c in data["sprints"] + data["designs"] if c["id"] == ident)

        # 每个归属样本只改变一项条件；期望不从参考生成器或判卷推导。
        id_dir = pathlib.Path(tmp) / "ideocase"
        id_dir.mkdir()
        ideo = build_fixture("acme", id_dir)
        lo = ideo / "scrum/ideo-delta/IdeoBacklog.md"
        body = lo.read_text(encoding="utf-8")
        active = "Test：把重试间隔拿给两位店员看"
        design_path = "../design-gamma/DesignBacklog.md"
        scenarios = [
            ("open for a design", design_path, active, "design-gamma"),
            ("open for a Sprint", "[Sprint 01](../sprint-01-alpha/SprintBacklog.md)", active, "sprint-01-alpha"),
            ("open for the product log", "`scrum/ProductBacklog.md`", active, None),
            ("concluded in English", design_path, "concluded 2026-11-14 — the frame is found", None),
            ("concluded with an English full stop", design_path, "Test: concluded.", None),
            ("concluded in Chinese", design_path, "测试：本轮已收尾（待归档）", None),
            ("still waiting to close", design_path, "测试：待收尾", "design-gamma"),
            ("closed mentioned in ongoing work", design_path, "Test: review closed cases", "design-gamma"),
            ("no open host", "../sprint-09-closed/SprintBacklog.md", active, None),
            ("a note is not a host log", "../design-gamma/Notes.md", active, None),
        ]
        for label, target, now, host in scenarios:
            text = body.replace("For: " + design_path, "For: " + target, 1).replace(
                "> Now: " + active, "> Now: " + now, 1)
            lo.write_text(text, encoding="utf-8")
            data = reference_data(ideo, ACME_SUMM)
            entry = {"id": "ideo-delta", "now": now}
            actual = [(c["id"], x) for c in data["sprints"] + data["designs"] for x in c.get("ideo", [])]
            want = [(host, entry)] if host else []
            if actual != want:
                failures.append("%s: expected %r, reference generated %r" % (label, want, actual))
            check(label, data, project=ideo)
            if not host:
                shown = copy.deepcopy(data)
                card_data(shown, "design-gamma").setdefault("ideo", []).append(entry)
                check(label + " incorrectly shown", shown, project=ideo, want_ok=False, expect="not eligible")

        # 两张同类卡可交换遍历顺序；保留正确挂载再向错误卡复制，不能只测移走原条目。
        lo.write_text(body.replace("For: " + design_path, "For: ../sprint-01-alpha/SprintBacklog.md", 1), encoding="utf-8")
        double = reference_data(ideo, ACME_SUMM)
        double["sprints"].sort(key=lambda card: card["id"])
        card_data(double, "sprint-02-beta")["ideo"] = [{"id": "ideo-delta", "now": active}]
        check("duplicate IDEO, correct host first", double, project=ideo, want_ok=False, expect="appears more than once")
        double["sprints"].reverse()
        check("duplicate IDEO, correct host last", double, project=ideo, want_ok=False, expect="appears more than once")
        br_dir = pathlib.Path(tmp) / "branchcase"
        br_dir.mkdir()
        branch = build_fixture("acme", br_dir, branch=True)
        bref = reference_data(branch, ACME_SUMM)
        check("branch case reference passes", bref, project=branch)
        sp2 = next(s for s in bref["sprints"] if s["id"] == "sprint-02-beta")
        check("branch case: the source is a branch", bref, project=branch) if sp2["source"].startswith("branch ") else \
            failures.append("branch case: sprint-02 was not found on its branch (%s)" % sp2["source"])

        def mutate(label, fn, expect, base=ref, project=acme):
            d = copy.deepcopy(base)
            fn(d)
            check(label, d, project=project, want_ok=False, expect=expect)

        mutate("a character of the Product changed", lambda d: d["product"].update(statement=d["product"]["statement"] + "。"), "product.statement")
        mutate("the Product Goal changed", lambda d: d["product"].update(goal=d["product"]["goal"][1:]), "product.goal")
        mutate("closed count wrong", lambda d: d["product"].update(closed=9), "product.closed")
        mutate("an item left out", lambda d: d["items"].pop(0), "items")
        mutate("an item invented", lambda d: d["items"].append({"id": "PBI-99", "title": "x", "status": "待选", "size": "S", "group": "next"}), "items")
        mutate("items swapped", lambda d: d["items"].reverse(), "items")
        mutate("an item title changed", lambda d: d["items"][0].update(title="别的标题"), "items")
        mutate("a Sprint item in group next", lambda d: d["items"][0].update(group="next"), "group")
        mutate("a bad group word", lambda d: d["items"][0].update(group="soon"), "group")
        mutate("the Sprint Goal changed", lambda d: d["sprints"][0].update(goal=d["sprints"][0]["goal"] + "x"), "goal")
        mutate("the Now line cut short", lambda d: d["sprints"][0].update(now=d["sprints"][0]["now"][:-2]), " now")
        mutate("a Sprint's items out of order", lambda d: d["sprints"][0].update(items=["PBI-9"]), "items")
        mutate("a block marked done that is not", lambda d: d["sprints"][0]["blocks"][1].update(done=True), "blocks")
        mutate("a block title changed", lambda d: d["sprints"][0]["blocks"][0].update(title="骨架"), "blocks")
        mutate("a Sprint left out", lambda d: d["sprints"].pop(), "sprints")
        mutate("a Sprint invented", lambda d: d["sprints"].append(dict(d["sprints"][0], id="sprint-09-ghost")), "sprints")
        mutate("a wrong source", lambda d: d["sprints"][0].update(source="branch x @ 1234567"), "source")
        mutate("a map stop that is not in the map", lambda d: d["product"]["map"].append({"text": "不存在的一步"}), "map")
        mutate("a note number that is not in the map", lambda d: d["product"]["map"][0].update(note="77"), "note")
        mutate("a here id that does not exist", lambda d: d["product"]["map"][0].update(here=["sprint-77-x"]), "here")
        mutate("a design map node that is not in the map", lambda d: card_data(d, "design-gamma")["map"].append("编出来的"), "map[")
        mutate("a design with a source map loses its route",
               lambda d: card_data(d, "design-gamma").pop("map"), "map is empty but section 2.1 contains a map")
        no_route = copy.deepcopy(ACME_SUMM)
        no_route["designs"]["design-gamma"].pop("map")
        cases += 1
        try:
            reference_data(acme, no_route)
        except ValueError as exc:
            if "design-gamma: summaries need the route from section 2.1" not in str(exc):
                failures.append("a missing route was rejected for the wrong reason: %s" % exc)
        else:
            failures.append("reference data omitted a route even though section 2.1 contains a map")
        mutate("a design for the wrong item", lambda d: card_data(d, "design-gamma").update({"for": ["PBI-1"]}), "for")
        mutate("a selected design loses its solution field without a storyboard",
               lambda d: card_data(d, "design-feedback-sample").pop("solution"), "explicit null")
        false_null = copy.deepcopy(ref)
        card_data(false_null, "design-feedback-sample")["solution"] = None
        check("a selected design without a storyboard is mistaken for undecided", false_null, project=acme,
              expect_warning="design design-feedback-sample: section 3.1 has content")
        mutate("a solution invented for an undecided design",
               lambda d: card_data(d, "design-choosing").update(solution={"title": "退回余额"}), "section 3.1")
        mutate("a storyboard invented for a design without one",
               lambda d: card_data(d, "design-feedback-sample").update(story=[{"title": "x", "text": "y"}]), "section 3.2")
        mutate("a design story with a frame without text",
               lambda d: card_data(d, "design-gamma")["story"].append({"title": "x", "text": ""}), "story")
        mutate("an IDEO log omitted", lambda d: card_data(d, "design-gamma").pop("ideo"), "missing this log")
        mutate("an IDEO log under the wrong owner",
               lambda d: card_data(d, "sprint-01-alpha").update(ideo=card_data(d, "design-gamma").pop("ideo")), "ideo ideo-delta host")
        mutate("an IDEO Now rewritten",
               lambda d: card_data(d, "design-gamma")["ideo"][0].update(now="Test：验证间隔"), "ideo ideo-delta now")
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
                drawn = {"pbi": len(D["items"]), "nodes": len(D["sprints"]) + len(D["designs"]),
                         "cards": 1 + len(D["sprints"]) + len(D["designs"])}
                if uses_solution_data(tpl) and not errors:
                    drawn["solutions"] = dict(Counter(
                        "undecided" if d["solution"] is None else "chosen" for d in D["designs"]))
                    drawn["storyboards"] = sum(bool(d.get("story")) for d in D["designs"])
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
