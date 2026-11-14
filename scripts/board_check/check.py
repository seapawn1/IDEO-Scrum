"""Check a written scrum/ScrumBoard.html against the project's logs (acceptance 68-4).

    python -X utf8 -I scripts/board_check/check.py check --project DIR [--page FILE] [--template FILE] [--render]
    python -X utf8 -I scripts/board_check/check.py selftest
    python -X utf8 -I scripts/board_check/check.py ref --project DIR --summaries FILE --out FILE

`check` reads the board's data block (conventions in `board-log.md`) and compares it with what the logs say:
the copied fields character for character, the summarized fields (maps) against the logs' maps, the ids and the order,
the sources; it also compares the page with the template outside the data block, so a page that lost a character in
copying is caught. `--render` opens the page in headless Edge and counts what it drew. Exit code 0 when no error.

`selftest` writes reference pages for small fixture projects (a working copy, a log only on another branch, a blank
page), checks that they pass, then makes about twenty kinds of damage and checks that each one is caught.
`ref` writes a data file from the logs plus a summaries file; it stands in for a perfect writer.
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
                "map_labels": map_labels(body, r"^#{2,3}\s*2\.1\b")}
        else:
            target = header_field(body, "For")
            m = re.search(r"(sprint-[^/\s]+|design-[^/\s]+)", target)
            now = now_line(body)
            # only an IDEO log that serves an open Sprint or design and is itself still open is on the page: one
            # whose For is the product log, or whose Now says concluded / closed, is not open work (board-log 11)
            P["ideo"][ident] = {"source": info["source"], "now": now, "for": m.group(1) if m else "",
                                "open": bool(m) and not re.search(r"\b(concluded|closed)\b", now, re.I)}
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
        for i, node in enumerate(d.get("map") or []):
            if not in_map(str(node), w["map_labels"]):
                errors.append("design %s map[%d] %r is not found in the design log's map" % (ident, i, node))
            for wn in stop_warnings(str(node)):
                warnings.append("design %s map[%d] %s" % (ident, i, wn))
        story = d.get("story") or []
        if len(story) > 5 or any(not isinstance(x, dict) or not x.get("title") or not x.get("text") for x in story):
            errors.append("design %s story: at most five frames, each with a title and a text" % ident)

    # IDEO logs: each sits under the Sprint or design its For field points to
    placed = {}
    for owner in list(sdata.values()) + list(ddata.values()):
        for x in owner.get("ideo") or []:
            placed[x.get("id")] = (owner.get("id"), x.get("now"))
    for ident, w in P["ideo"].items():
        if not w["open"]:
            continue  # serves the product log, or says concluded / closed: not on the page (board-log 11)
        if ident not in placed:
            errors.append("ideo %s: the log is open but the page does not show it" % ident)
        else:
            if placed[ident][0] != w["for"]:
                errors.append("ideo %s: shown under %s, its For field points to %s" % (ident, placed[ident][0], w["for"]))
            eq(errors, "ideo %s now" % ident, placed[ident][1], w["now"])
    for ident in placed:
        if ident not in P["ideo"] or not P["ideo"][ident]["open"]:
            errors.append("ideo %s is shown but has no open log" % ident)


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
            "cards": len(re.findall(r'class="card"', dom))}


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
    designs = [{"id": k, "for": v["for"], "goal": v["goal"], "now": v["now"], "source": v["source"],
                "map": summ.get("designs", {}).get(k, {}).get("map", []),
                "story": summ.get("designs", {}).get(k, {}).get("story", [])} for k, v in P["designs"].items()]
    by_id = {x["id"]: x for x in sprints + designs}
    for k, v in P["ideo"].items():
        if v["open"] and v["for"] in by_id:
            by_id[v["for"]].setdefault("ideo", []).append({"id": k, "now": v["now"]})
    lang = "zh" if re.search(r"[\u4e00-\u9fff]", pp["statement"]) else "en"
    return {"lang": lang, "generated": "2026-11-14 12:00",
            "product": {"name": name, "statement": pp["statement"], "goal": pp["goal"], "source": "working copy",
                        "map": summ.get("map", []), "closed": pp["closed"]},
            "items": items, "sprints": sprints, "designs": designs}


def make_page(data, template_text):
    block = json.dumps(data, ensure_ascii=False, indent=1).replace("<", chr(92) + "u003c")
    assert PLACEHOLDER in template_text
    return template_text.replace(PLACEHOLDER, block)


ACME_SUMM = {"map": [{"text": "下单", "here": ["sprint-01-alpha"]}, {"text": "发货", "here": ["sprint-02-beta", "design-gamma"]}],
             "designs": {"design-gamma": {"map": ["单子失败", "重试", "成功或放弃"],
                                          "story": [{"title": "分批重试流程", "text": "失败的批次单独重试，成功的批次不动。"}]}}}


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
        def check(label, data=None, page=None, project=None, want_ok=True, expect=""):
            nonlocal cases
            cases += 1
            text = page if page is not None else make_page(data, tpl)
            errs, _ = check_page(text, project, tpl)
            if want_ok and errs:
                failures.append("%s: expected pass, got %s" % (label, errs[:3]))
            if not want_ok and not errs:
                failures.append("%s: damage not caught" % label)
            if not want_ok and errs and expect and not any(expect in e for e in errs):
                failures.append("%s: caught, but not by the %r check: %s" % (label, expect, errs[:2]))

        acme = build_fixture("acme", tmp)
        ref = reference_data(acme, ACME_SUMM)
        check("acme reference passes", ref, project=acme)
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
        # an IDEO log that is not open work is not on the page: its For is the product log, or its Now says concluded
        # (formal run 2 drew a voice run for the product log, closed, and left it off the page — correctly)
        id_dir = pathlib.Path(tmp) / "ideocase"
        id_dir.mkdir()
        ideo = build_fixture("acme", id_dir)
        lo = ideo / "scrum/ideo-delta/IdeoBacklog.md"
        body = lo.read_text(encoding="utf-8")
        for old, new in (("> Opened 2026-11-13 | For: ../design-gamma/DesignBacklog.md", "> Opened 2026-11-13 | For: ../ProductBacklog.md"),
                         ("> Now: Test：把重试间隔拿给两位店员看", "> Now: concluded 2026-11-14 — the frame is found")):
            if old not in body:
                failures.append("ideo not open work: %r not found in the fixture" % old)
            body = body.replace(old, new)
        lo.write_text(body, encoding="utf-8")
        cases += 1
        idref = reference_data(ideo, ACME_SUMM)
        if any(x.get("ideo") for x in idref["sprints"] + idref["designs"]):
            failures.append("ideo not open work: the page data still shows it")
        check("a log that serves the product log, and is concluded, is not shown", idref, project=ideo)
        shown = copy.deepcopy(idref)
        shown["designs"][0].setdefault("ideo", []).append({"id": "ideo-delta", "now": "concluded 2026-11-14 — the frame is found"})
        errs, _ = check_page(make_page(shown, tpl), ideo, tpl)
        if not any("has no open log" in e for e in errs):
            failures.append("ideo not open work: showing it is not caught (%s)" % errs[:2])
        cases += 1
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
        mutate("a design map node that is not in the map", lambda d: d["designs"][0]["map"].append("编出来的"), "map[")
        mutate("a design for the wrong item", lambda d: d["designs"][0].update({"for": ["PBI-1"]}), "for")
        mutate("a design story with a frame without text", lambda d: d["designs"][0]["story"].append({"title": "x", "text": ""}), "story")
        mutate("an IDEO log under the wrong owner", lambda d: (d["designs"][0].pop("ideo"), d["sprints"][0].setdefault("ideo", []).append({"id": "ideo-delta", "now": "x"})), "ideo")
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
        data = reference_data(a.project, summ)
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
                for key, want in drawn.items():
                    if counts[key] != want:
                        out["errors"].append("the page drew %d %s, the data has %d" % (counts[key], key, want))
                        out["ok"] = False
            except (ValueError, KeyError, TypeError):
                pass  # the data errors are already reported above
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
