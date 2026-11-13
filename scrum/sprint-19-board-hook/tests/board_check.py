"""Board fixture and checker (Sprint 19, block 8; PBI-35 acceptance 1-5).

The board (`scrum/Board.html`) is written from the logs by a cheap model. This script builds a sample project
whose open logs are spread over branches, reads the logs with its own reading of the log conventions (the
"truth"), and checks a generated page against that truth:

  * every `data-fact` marker on the page holds exactly what the log holds (a fact the logs do not give fails);
  * every fact the page should show is there: commitments, Now, Waiting for PO, stages, work items with their
    done marks, items, maps, one card per open Sprint and design, one line for the IDEO log;
  * everything that waits for the Product Owner is in the top banner, and nothing else is;
  * items are grouped the way the project groups them; archived and done items are not shown;
  * every link opens (in-page ids exist, relative files exist in the working copy);
  * two pages made from the same state hold the same facts (`compare`).

usage (with `python -X utf8 -I`):
  board_check.py selftest
  board_check.py fixture --dest DIR [--scenario A|B]        build the sample project; prints its path
  board_check.py check   --repo DIR --page FILE [--scenario A|B]
  board_check.py compare PAGE PAGE [PAGE ...]
  board_check.py facts   --page FILE                         print the facts a page holds

Scenario A: the working copy is on `main`; every open Sprint and design is only on a branch.
Scenario B: the working copy is on the Sprint 01 branch, with an uncommitted change to its Now line.
"""
import argparse
import html
import html.parser
import json
import pathlib
import re
import subprocess
import sys
import tempfile

STAGES = ("Why", "What", "How", "Increment", "Test")
WS = re.compile(r"\s+")


def norm_ws(s):
    return WS.sub(" ", s).strip()


# ============================================================================================ the sample project
PRODUCT_LOG = """# 一、Product

## 1.1 Product

| 承诺 | Acme 订单台：把订单从下单到发货放在一个页面里。 |
| --- | --- |

## 1.2 Product Goal

| 承诺 | 看得清：每笔订单现在在哪一步，一眼就知道。（PO 2026-11-13 定） |
| --- | --- |

## 1.3 Definition of Done

| 维度 | 标准 |
| --- | --- |
| 无死链 | 链接都能打开 |

# 二、架构

## 2.2 架构

```mermaid
flowchart TD
    U["店员"] --> A["① 下单<br/>付款"]
    A --> B["② 发货"]
    B --> E["结局：客户收到货"]
```

# 三、Product Backlog Items

## 3.1 当前的 PBI

| 编号 | 标题 | 用户故事 | 架构定位 | 当前状态 | 规模 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| PBI-1 | 订单列表 | 作为店员，我想要订单列表 | ① | 在 Sprint 01（主线） | M | 备注一 |
| PBI-2 | 发货单 | 作为店员，我想要发货单 | ② | 在 Sprint 02（主线） | S | 备注二 |
| PBI-3 | 退款流程 | 作为客户，我想要退款 | ② | 待选（副线） | M | 备注三 |
| PBI-4 | 客户标签 | 作为店员，我想要给客户打标签 | ① | 以后 | L | 备注四 |
| PBI-5 | 批量重试 | 作为店员，我想要失败的单子自动重试 | ② | 在设计 design-gamma 中（副线） | M | 备注五 |

## 3.2 已完成 / 已关闭的 PBI

| 编号 | 标题 | 结果 | 出处 |
| --- | --- | --- | --- |
| PBI-0 | 旧的导入功能 | 已做完 | documents/sprint-00-old.md |
"""

ARCHIVED = """# Sprint Backlog — Sprint 00 (old)

> Now: Test：已收官
> Waiting for PO: None

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 旧冲刺的目标：导入老数据。 |
| --- | --- |
"""

SPRINT_01 = """# Sprint Backlog — Sprint 01 (alpha)

> Started: 2026-11-13 | Closes when the Sprint Goal is met | Branch: sprint-01-alpha | Product Owner: SeaPawn
> Now: How：Developer 起草方案，等 Master 审
> Waiting for PO: PBI-1 要不要含已取消的订单；PBI-3 退款走原路还是余额
> How to write this log: `sprint-log.md`.

## 1. Why

### 1.1 Sprint Goal

| 承诺 | 订单一眼看清：列表上直接看到每笔订单的状态。 |
| --- | --- |

### 1.2 Definition of Done

- 链接都能打开

## 2. What

### 2.1 Product Backlog Items

| 编号 | 标题 | 用户故事 | 架构定位 | 规模 |
| --- | --- | --- | --- | --- |
| PBI-1 | 订单列表 | 作为店员，我想要订单列表 | ① | M |

### 2.2 Refinement

细化已定。

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| 1 | 列表页骨架 | 页面 | ✓ 2026-11-13　页面能打开 |
| 2 | 状态列 | 一列 | 每行都有状态 |
| 3 | 筛选 | 筛选条 | 能按状态筛 |

**Key choices**

先做骨架。

Go-ahead: 尚未放行。

## 4. Increment notes

无。

## 5. Test

无。
"""

SPRINT_02 = """# Sprint Backlog — Sprint 02 (beta)

> Started: 2026-11-13 | Closes when the Sprint Goal is met | Branch: sprint-02-beta | Product Owner: SeaPawn
> Now: Increment: block 1 done, block 2 under way
> Waiting for PO: None
> How to write this log: `sprint-log.md`.

## 1. Why

### 1.1 Sprint Goal

| Commitment | Ship slips that print: a packing slip from any order in two clicks. |
| --- | --- |

## 2. What

### 2.1 Product Backlog Items

| # | Title | User story | Place | Size |
| --- | --- | --- | --- | --- |
| PBI-2 | 发货单 | 作为店员，我想要发货单 | ② | S |

## 3. How

| # | Work item | Output | Done when |
| --- | --- | --- | --- |
| H1 | Packing slip template | template | ✓ 2026-11-13 renders |
| H2 | Print button | button | prints one page |

Go-ahead: Master 2026-11-13 放行。

## 4. Increment notes

none.
"""

DESIGN = """# Design Backlog — gamma

> Opened 2026-11-13 | From: Sprint 02 里「批量重试」这个难点 | Branch: sprint-02-beta | Product Owner: SeaPawn | Designer: AI
> Now: Ideate：评审三个草图
> Waiting for PO: PBI-5 选哪个草图
> How to write this log: `design-log.md`.

## 1. Empathize

### 1.1 Challenge

失败的单子怎么自动重试。

### 1.2 设计目标

| 承诺 | 弄清失败的单子重试几次、隔多久才让店员放心。 |
| --- | --- |

## 2. Define

### 2.1 Map

```mermaid
flowchart TD
    S["店员"] --> F["单子失败"]
    F --> R["重试<br/>隔一会儿"]
    R --> E["成功或放弃"]
```

## 3. Ideate

### 3.1 Solution

分批重试流程

失败的批次单独重试，成功的批次不动。
"""

IDEO = """# IDEO Log — delta

> Opened 2026-11-13 | For: ../design-gamma/DesignBacklog.md | Product Owner: SeaPawn
> Now: Test：把重试间隔拿给两位店员看
> Waiting for PO: None

## 1. Empathize

无。
"""

FILES_MAIN = {
    ".gitignore": "scrum/Board.html\n",
    "scrum/ProductBacklog.md": PRODUCT_LOG,
    "scrum/documents/sprint-00-old.md": ARCHIVED,
    "src/app.py": "print('acme')\n",
}


def git(repo, *args, check=True):
    p = subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "user.name=fixture", "-c", "user.email=f@example.com",
                        *args], cwd=str(repo), capture_output=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.decode('utf-8', 'replace')}")
    return p.stdout.decode("utf-8", "replace")


def write(repo, rel, text):
    p = pathlib.Path(repo) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")


def build_fixture(dest, scenario="A"):
    dest = pathlib.Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    git(dest, "init", "-q", "-b", "main")
    for rel, text in FILES_MAIN.items():
        write(dest, rel, text)
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "main")
    git(dest, "checkout", "-q", "-b", "sprint-01-alpha")
    write(dest, "scrum/sprint-01-alpha/SprintBacklog.md", SPRINT_01)
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "sprint 01")
    git(dest, "checkout", "-q", "main")
    git(dest, "checkout", "-q", "-b", "sprint-02-beta")
    write(dest, "scrum/sprint-02-beta/SprintBacklog.md", SPRINT_02)
    write(dest, "scrum/design-gamma/DesignBacklog.md", DESIGN)
    write(dest, "scrum/ideo-delta/IdeoBacklog.md", IDEO)
    # a log inside a test fixture, deeper in the tree: not an open log
    write(dest, "scrum/sprint-02-beta/tests/fixtures/project/scrum/sprint-09-nested/SprintBacklog.md",
          SPRINT_01.replace("订单一眼看清", "嵌套的假冲刺"))
    git(dest, "add", "-A")
    git(dest, "commit", "-q", "-m", "sprint 02, design, ideo")
    if scenario == "B":
        git(dest, "checkout", "-q", "sprint-01-alpha")
        f = dest / "scrum/sprint-01-alpha/SprintBacklog.md"
        f.write_text(f.read_text(encoding="utf-8").replace("How：Developer 起草方案，等 Master 审",
                                                          "Increment：块 1 做完，块 2 在做"), encoding="utf-8", newline="\n")
    else:
        git(dest, "checkout", "-q", "main")
    return dest


# =============================================================================================== reading the logs
def cells(line):
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return None
    return [c.strip() for c in s[1:-1].split("|")]


def parse_log(text, kind):
    """The reading rules, applied independently of the hook and of any generator."""
    lines = text.replace("\r\n", "\n").split("\n")
    out = {"kind": kind, "commitments": {}, "now": None, "waiting": None, "items": [], "blocks": [], "map": None,
           "solution": None, "done_items": [], "for": None, "from": None}
    heading, in_fence, fence_lines, fence_head = "", False, [], ""
    chapter3 = False
    for i, line in enumerate(lines):
        if in_fence:
            if line.startswith("```"):
                in_fence = False
                if out["map"] is None and (("2.2" in fence_head and kind == "product") or ("2.1" in fence_head and kind == "design")):
                    out["map"] = "\n".join(fence_lines)
            else:
                fence_lines.append(line)
            continue
        if line.startswith("```mermaid"):
            in_fence, fence_lines, fence_head = True, [], heading
            continue
        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            heading = m.group(1).strip()
            chapter3 = bool(re.match(r"^3\.\s", heading)) and kind == "sprint"
            continue
        if line.startswith("> Now:"):
            out["now"] = line[len("> Now:"):].strip()
        elif line.startswith("> Waiting for PO:"):
            out["waiting"] = line[len("> Waiting for PO:"):].strip()
        elif line.startswith("> Opened") or line.startswith("> From") or line.startswith("> Started"):
            mf = re.search(r"For:\s*([^|]+?)\s*(\||$)", line)
            if mf:
                out["for"] = mf.group(1).strip()
            mf = re.search(r"From:\s*([^|]+?)\s*(\||$)", line)
            if mf:
                out["from"] = mf.group(1).strip()
        c = cells(line)
        if c and len(c) == 2 and c[0] in ("承诺", "Commitment"):
            name = None
            if "Sprint Goal" in heading:
                name = "Sprint Goal"
            elif "Product Goal" in heading:
                name = "Product Goal"
            elif re.search(r"Design [Gg]oal|设计目标", heading):
                name = "Design goal"
            elif "Product" in heading or "产品" in heading:
                name = "Product"
            if name and name not in out["commitments"]:
                out["commitments"][name] = c[1]
        if kind == "product" and c and len(c) == 7 and re.match(r"^PBI-\d+$", c[0]) and heading.startswith("3.1"):
            out["items"].append({"number": c[0], "title": c[1], "status": c[4], "size": c[5]})
        if kind == "product" and c and len(c) == 4 and re.match(r"^PBI-\d+$", c[0]) and heading.startswith("3.2"):
            out["done_items"].append({"number": c[0], "title": c[1]})
        if kind == "sprint" and c and len(c) == 5 and re.match(r"^PBI-\d+$", c[0]) and heading.startswith("2.1"):
            out["items"].append({"number": c[0], "title": c[1]})
        if kind == "sprint" and chapter3 and c and len(c) == 4 and c[0] != "#" and c[1] != "Work item" \
                and not set(c[0]) <= set("-: "):
            # a work item's number is free (1, H1 ...); the header and the separator row are not work items
            out["blocks"].append({"text": c[1], "done": c[3].startswith("✓")})
        if kind == "design" and heading.startswith("3.1") and out["solution"] is None and line.strip() \
                and not line.startswith("<!--"):
            out["solution"] = line.strip()
    now = out["now"] or ""
    word = re.split(r"[:：\s]", now, maxsplit=1)[0] if now else ""
    out["stage"] = word if word in STAGES else None
    return out


def branches_and_tips(repo):
    tips = {}
    for line in git(repo, "for-each-ref", "--format=%(refname:short) %(objectname)", "refs/heads").splitlines():
        name, h = line.split()
        tips[name] = h
    return tips


def read_truth(repo, scenario="A"):
    """Every open log of the sample project, as the page should show it."""
    repo = pathlib.Path(repo)
    tips = branches_and_tips(repo)
    logs = {}
    patterns = [("scrum/sprint-*/SprintBacklog.md", "sprint"), ("scrum/design-*/DesignBacklog.md", "design"),
                ("scrum/ideo-*/IdeoBacklog.md", "ideo")]
    # the working copy first
    paths = {"scrum/ProductBacklog.md": "product"}
    for pat, kind in patterns:
        for p in sorted(repo.glob(pat)):
            paths[p.relative_to(repo).as_posix()] = kind
    for rel, kind in paths.items():
        t = parse_log((repo / rel).read_text(encoding="utf-8"), kind)
        t.update(path=rel, read="working copy", branch=None, commit=None, in_working_copy=True)
        logs[rel] = t
    # then every branch that holds an open log the working copy does not have
    for branch, tip in tips.items():
        for rel in git(repo, "ls-tree", "-r", "--name-only", tip).splitlines():
            # only the top-level scrum/ folder: a log inside a test fixture deeper down is not an open log
            kind = next((k for pat, k in patterns if re.fullmatch(pat.replace("*", "[^/]+").replace(".", r"\."), rel)), None)
            if kind and rel not in logs and not rel.startswith("scrum/documents/"):
                t = parse_log(git(repo, "show", f"{tip}:{rel}"), kind)
                t.update(path=rel, read=f"branch {branch} @ {tip[:7]}", branch=branch, commit=tip, in_working_copy=False)
                logs[rel] = t
    return {"logs": logs, "tips": tips, "scenario": scenario}


def folder(path):
    return pathlib.PurePosixPath(path).parent.name


# ================================================================================================ reading a page
class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.children, self.parts = tag, dict(attrs), parent, [], []

    def text(self):
        out = list(self.parts) if not self.children else []
        if self.children:
            out = []
            for item in self._flow():
                out.append(item)
        return norm_ws("".join(out))

    def _flow(self):
        for kind, x in self.seq:
            if kind == "t":
                yield x
            else:
                yield x.text()
                yield " "

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def ancestors(self):
        n = self.parent
        while n is not None:
            yield n
            n = n.parent

    def cls(self):
        return (self.attrs.get("class") or "").split()


class Page(html.parser.HTMLParser):
    VOID = {"meta", "br", "img", "input", "link", "hr", "area", "base", "col", "source", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {}, None)
        self.root.seq = []
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        n.seq = []
        self.cur.children.append(n)
        self.cur.seq.append(("n", n))
        if tag not in self.VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        n.seq = []
        self.cur.children.append(n)
        self.cur.seq.append(("n", n))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.seq.append(("t", data))
        self.cur.parts.append(data)


def raw_text(node):
    """Text of a node exactly as in the page, without collapsing whitespace (for a map's source)."""
    out = []

    def go(n):
        for kind, x in n.seq:
            if kind == "t":
                out.append(x)
            else:
                go(x)
    go(node)
    return "".join(out)


def load_page(path):
    p = Page()
    p.feed(pathlib.Path(path).read_text(encoding="utf-8"))
    p.close()
    return p.root


def log_of(node):
    for n in [node, *node.ancestors()]:
        if "data-log" in n.attrs:
            return n.attrs["data-log"]
    return None


def page_facts(root):
    """[(fact, log, extra, text)] for every marker on the page; map text is kept exactly."""
    facts = []
    for n in root.walk():
        f = n.attrs.get("data-fact")
        if not f:
            continue
        text = raw_text(n).strip("\n") if f == "map" else n.text()
        extra = {k: v for k, v in n.attrs.items() if k in ("data-name", "data-done")}
        facts.append({"fact": f, "log": log_of(n), "extra": extra, "text": text, "node": n})
    return facts


# =========================================================================================== expected groupings
def bracket_word(status):
    m = re.search(r"[（(]([^）)]+)[）)]\s*$", status)
    return m.group(1) if m else None


def expected_groups(items):
    """Partition of item numbers, and the word each bracket group is named by (None for the others)."""
    if any(bracket_word(i["status"]) for i in items):
        groups = {}
        for i in items:
            groups.setdefault(bracket_word(i["status"]) or "Other", []).append(i["number"])
        return groups, True
    groups = {}
    for i in items:
        s = i["status"]
        k = "In a Sprint" if re.search(r"Sprint", s) else "In a design" if re.search(r"design|设计", s) else \
            "Waiting" if re.search(r"waiting|Waiting|待选", s) else "Other"
        groups.setdefault(k, []).append(i["number"])
    return groups, False


# ====================================================================================================== the check
def check_page(page_path, truth, board_dir):
    """Returns a list of failures; empty when the page is right."""
    root = load_page(page_path)
    facts = page_facts(root)
    logs = truth["logs"]
    product = logs["scrum/ProductBacklog.md"]
    prod_items = {i["number"]: i for i in product["items"]}
    fails = []

    def bad(msg):
        fails.append(msg)

    def expect_in(f, values, what):
        if f["text"] not in values:
            bad(f"{what} not in the log: {f['text'][:80]!r}")

    # --- every marker is a fact of a log
    for f in facts:
        kind, log, text = f["fact"], f["log"], f["text"]
        t = logs.get(log) if log else None
        if kind == "commitment":
            name = f["extra"].get("data-name")
            want = (t or {}).get("commitments", {}).get(name)
            if want is None or text != want:
                bad(f"commitment {name!r} of {log}: page has {text[:60]!r}, log has {str(want)[:60]!r}")
        elif kind == "now":
            if t is None or text != t["now"]:
                bad(f"Now of {log}: page has {text[:60]!r}, log has {str((t or {}).get('now'))[:60]!r}")
        elif kind == "waiting":
            if t is None or text != t["waiting"] or text == "None":
                bad(f"Waiting for PO of {log}: page has {text[:60]!r}, log has {str((t or {}).get('waiting'))[:60]!r}")
        elif kind == "stage":
            if text not in STAGES or t is None or t["stage"] != text:
                bad(f"stage of {log}: page has {text!r}, the Now line names {(t or {}).get('stage')!r}")
        elif kind == "block":
            hit = [b for b in (t or {}).get("blocks", []) if b["text"] == text]
            if not hit:
                bad(f"work item of {log} not in the log: {text[:60]!r}")
            elif str(hit[0]["done"]).lower() != f["extra"].get("data-done"):
                bad(f"work item {text[:40]!r}: data-done={f['extra'].get('data-done')!r}, the log says done={hit[0]['done']}")
        elif kind == "map":
            want = (t or {}).get("map")
            if want is None or text != want:
                bad(f"map of {log} differs from the log")
        elif kind == "solution":
            want = (t or {}).get("solution")
            if want is None or norm_ws(want) not in text:
                bad(f"solution of {log}: page has {text[:60]!r}, the log's title is {str(want)[:60]!r}")
        elif kind == "source":
            if t is None:
                bad(f"source line for an unknown log {log}")
            elif t["in_working_copy"]:
                if text != "working copy":
                    bad(f"source of {log}: page says {text!r}, the log was read from the working copy")
            else:
                m = re.match(r"^branch (\S+) @ ([0-9a-f]{7,40})$", text)
                if not m or m.group(1) != t["branch"] or not t["commit"].startswith(m.group(2)):
                    bad(f"source of {log}: page says {text!r}, expected branch {t['branch']} @ {t['commit'][:7]}")
        elif kind == "generated":
            if not re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$", text):
                bad(f"generated time is not YYYY-MM-DD HH:MM: {text!r}")
        elif kind in ("item-number", "item-title", "item-status", "item-size"):
            pass  # checked per item below
        else:
            bad(f"unknown marker {kind!r}")

    # --- items: group the item markers by their container (the nearest ancestor holding an item-number)
    def item_rows(scope):
        rows = []
        for n in scope.walk():
            if n.attrs.get("data-fact") == "item-number":
                box = n.parent
                while box is not None and not any(
                        c.attrs.get("data-fact") in ("item-title",) or any(x.attrs.get("data-fact") == "item-title" for x in c.walk())
                        for c in [box]):
                    box = box.parent
                row = {"number": n.text(), "box": box}
                for x in (box.walk() if box else []):
                    k = x.attrs.get("data-fact")
                    if k in ("item-title", "item-status", "item-size") and k[5:] not in row:
                        row[k[5:]] = x.text()
                rows.append(row)
        return rows

    def check_row(r, where, with_size):
        want = prod_items.get(r["number"])
        if want is None:
            bad(f"{where}: {r['number']!r} is not an item of the product log (done or archived items are not shown)")
            return
        for k in ("title", "status") + (("size",) if with_size else ()):
            if r.get(k) != want[k]:
                bad(f"{where} {r['number']}: {k} is {r.get(k)!r}, the product log has {want[k]!r}")

    prod_node = next((n for n in root.walk() if n.attrs.get("id") == "product"), None)
    if prod_node is None:
        bad("no product card (id=\"product\")")
    else:
        rows = item_rows(prod_node)
        shown = [r["number"] for r in rows]
        if sorted(shown) != sorted(prod_items):
            bad(f"product card shows {sorted(shown)}, the product log's current items are {sorted(prod_items)}")
        for r in rows:
            check_row(r, "product card", True)
        # grouping: the partition and the names
        cols = next((n for n in prod_node.walk() if "cols" in n.cls()), None)
        groups, bracketed = expected_groups(product["items"])
        if cols is None:
            bad("no grouped items (class=\"cols\") in the product card")
        else:
            got = {}
            for card in [c for c in cols.children if c.tag == "div"]:
                label = next((x.text() for x in card.walk() if "label" in x.cls()), "")
                nums = [n.text() for n in card.walk() if n.attrs.get("data-fact") == "item-number"]
                if nums:
                    got[label] = nums
            part_got = sorted(sorted(v) for v in got.values())
            part_want = sorted(sorted(v) for v in groups.values())
            if part_got != part_want:
                bad(f"item groups are {part_got}, expected {part_want}")
            elif bracketed:
                for word, nums in groups.items():
                    if word != "Other" and not any(word in label and sorted(v) == sorted(nums) for label, v in got.items()):
                        bad(f"the group of {nums} is not named by its bracketed word {word!r}")

    # --- cards: one for each open Sprint and design, none for anything else; facts present
    ids = {n.attrs["id"]: n for n in root.walk() if "id" in n.attrs}
    open_logs = {p: t for p, t in logs.items() if t["kind"] in ("sprint", "design")}
    cards = {}
    for p, t in open_logs.items():
        node = ids.get(folder(p))
        if node is None or node.attrs.get("data-log") != p:
            bad(f"no card for {p} (id {folder(p)!r} with data-log={p!r})")
            continue
        cards[p] = node
    for n in root.walk():
        if n.attrs.get("data-log") and n.attrs["data-log"] not in logs:
            bad(f"a card for a log that is not open: {n.attrs['data-log']}")
    covered = lambda node, fact, **kw: [f for f in facts if f["fact"] == fact and node in [f["node"], *f["node"].ancestors()]
                                        and all(f["extra"].get(k) == v for k, v in kw.items())]
    for p, node in cards.items():
        t = open_logs[p]
        for name, text in t["commitments"].items():
            if not [f for f in covered(node, "commitment", **{"data-name": name}) if f["text"] == text]:
                bad(f"card {folder(p)}: commitment {name!r} is missing")
        if not [f for f in covered(node, "now") if f["text"] == t["now"] and f["log"] == p]:
            bad(f"card {folder(p)}: the Now line is missing")
        if t["waiting"] not in (None, "None") and not [f for f in covered(node, "waiting") if f["text"] == t["waiting"]]:
            bad(f"card {folder(p)}: Waiting for PO is missing")
        if t["waiting"] in (None, "None") and covered(node, "waiting"):
            bad(f"card {folder(p)}: shows Waiting for PO but the log says None")
        if not [f for f in covered(node, "source") if f["log"] == p]:
            bad(f"card {folder(p)}: no source line")
        if t["kind"] == "sprint":
            st = covered(node, "stage")
            if (t["stage"] and [f["text"] for f in st] != [t["stage"]]) or (not t["stage"] and st):
                bad(f"card {folder(p)}: stage marker is {[f['text'] for f in st]}, expected {t['stage']}")
            blocks = [(f["text"], f["extra"].get("data-done")) for f in covered(node, "block")]
            want = [(b["text"], str(b["done"]).lower()) for b in t["blocks"]]
            if blocks != want:
                bad(f"card {folder(p)}: work items are {blocks}, expected {want}")
            rows = item_rows(node)
            if sorted(r["number"] for r in rows) != sorted(i["number"] for i in t["items"]):
                bad(f"card {folder(p)}: items are {[r['number'] for r in rows]}, expected {[i['number'] for i in t['items']]}")
            for r in rows:
                check_row(r, f"card {folder(p)}", False)
        if t["kind"] == "design":
            if t["map"] and not [f for f in covered(node, "map") if f["text"] == t["map"]]:
                bad(f"card {folder(p)}: the map is missing")
            if t["solution"] and not covered(node, "solution"):
                bad(f"card {folder(p)}: the solution is missing")
    # IDEO logs: one line on the card they serve, no card of their own
    for p, t in logs.items():
        if t["kind"] != "ideo":
            continue
        served = str((pathlib.PurePosixPath(p).parent / t["for"]).as_posix()) if t["for"] else None
        served = str(pathlib.PurePosixPath(*[x for x in pathlib.PurePosixPath(served).parts])) if served else None
        served = re.sub(r"[^/]+/\.\./", "", served) if served else None
        card = cards.get(served)
        if card is None or not [f for f in covered(card, "now") if f["log"] == p and f["text"] == t["now"]]:
            bad(f"IDEO log {p}: its Now line is not on the card of the log it serves ({served})")
        if ids.get(folder(p)) is not None:
            bad(f"IDEO log {p} has a card of its own")

    # --- the banner: exactly what waits
    banner = ids.get("waiting")
    wanted = sorted(t["waiting"] for t in logs.values() if t["waiting"] not in (None, "None"))
    if wanted:
        if banner is None:
            bad("no banner (id=\"waiting\")")
        else:
            got = sorted(f["text"] for f in facts if f["fact"] == "waiting" and banner in f["node"].ancestors())
            if got != wanted:
                bad(f"the banner lists {got}, what waits is {wanted}")
    else:
        # nothing waits: one line says so (the template's `banner none`), and no banner lists anything
        if not [n for n in root.walk() if "banner" in n.cls() and "none" in n.cls()]:
            bad("nothing waits for the Product Owner, but no `banner none` line says so")
        if [f for f in facts if f["fact"] == "waiting" and any("banner" in a.cls() for a in f["node"].ancestors())]:
            bad("nothing waits for the Product Owner, but a banner lists something")

    # --- archived and done items stay out
    page_text = norm_ws(raw_text(root))
    for marker in ("旧的导入功能", "旧冲刺的目标", "PBI-0 "):
        if marker in page_text:
            bad(f"archived or done material is on the page: {marker!r}")

    # --- links
    board_dir = pathlib.Path(board_dir)
    for n in root.walk():
        href = n.attrs.get("href")
        if n.tag != "a" or not href or re.match(r"^[a-z]+://", href):
            continue
        if href.startswith("#"):
            if href[1:] not in ids:
                bad(f"dead link {href}")
        elif not (board_dir / href.split("#")[0]).is_file():
            bad(f"dead link {href}")
    for p, node in list(cards.items()):
        t = open_logs[p]
        links = [n.attrs["href"] for n in node.walk() if n.tag == "a" and n.attrs.get("href") and not n.attrs["href"].startswith(("#", "http"))]
        if t["in_working_copy"] and not links:
            bad(f"card {folder(p)}: the log is in the working copy but the card has no link to it")
    if prod_node is not None and not [n for n in prod_node.walk() if n.tag == "a" and n.attrs.get("href", "").endswith("ProductBacklog.md")]:
        bad("the product card has no link to the product log")
    return fails


def fact_set(page_path):
    """What a page holds, without the time it was made: for comparing two pages made from the same state."""
    out = []
    for f in page_facts(load_page(page_path)):
        if f["fact"] != "generated":
            out.append((f["fact"], f["log"], tuple(sorted(f["extra"].items())), f["text"]))
    return sorted(out)


# ================================================================================ a reference page, for the self-test
def esc(s):
    return html.escape(s, quote=False)


def render_reference(truth, board_dir):
    """A correct page for the sample project, written the way the template says. Used only by the self-test."""
    logs, board_dir = truth["logs"], pathlib.Path(board_dir)
    product = logs["scrum/ProductBacklog.md"]
    items = {i["number"]: i for i in product["items"]}
    open_logs = {p: t for p, t in logs.items() if t["kind"] in ("sprint", "design")}

    def card_id_for_status(status):
        for p in open_logs:
            if re.search(r"Sprint\s*0*" + re.escape(folder(p).split("-")[1].lstrip("0") or "0") + r"\b", status) and open_logs[p]["kind"] == "sprint":
                return folder(p)
            if open_logs[p]["kind"] == "design" and folder(p).split("-", 1)[1] in status:
                return folder(p)
        return None

    def src(t):
        link = ""
        if t["in_working_copy"]:
            rel = pathlib.PurePosixPath(t["path"]).relative_to("scrum")
            link = f' · <a href="{rel}">{rel.name}</a>'
        else:
            link = " · not in this working copy"
        return f'<div class="src"><span data-fact="source">{esc(t["read"])}</span>{link}</div>'

    h = ['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Project board</title></head><body><div class="wrap">',
         '<h1>Project board</h1>',
         '<div class="meta">Made <span data-fact="generated">2026-11-13 23:00</span> · read: the logs</div>']
    waits = [(p, t) for p, t in logs.items() if t["waiting"] not in (None, "None")]
    if waits:
        h.append(f'<div class="banner" id="waiting"><strong>Waiting for the Product Owner · {len(waits)}</strong><ul>')
        for p, t in waits:
            anchor = folder(p) if t["kind"] in ("sprint", "design") else None
            h.append(f'<li><strong>{esc(folder(p))}</strong>: <span data-fact="waiting" data-log="{p}">{esc(t["waiting"])}</span>'
                     + (f' <a href="#{anchor}">card</a>' if anchor else "") + "</li>")
        h.append("</ul></div>")
    else:
        h.append('<div class="banner none"><strong>Nothing is waiting for the Product Owner.</strong></div>')
    h.append('<section id="product" data-log="scrum/ProductBacklog.md"><div class="grid2">')
    for name in ("Product", "Product Goal"):
        h.append(f'<div class="card"><div class="label">{name}</div><p class="commit" data-fact="commitment" data-name="{name}">{esc(product["commitments"][name])}</p></div>')
    h.append('</div>' + src(product))
    h.append('<details class="card map" id="product-map"><summary>Architecture map</summary><div class="drawn"></div>'
             f'<details class="src"><summary>Map source</summary><pre class="source" data-fact="map">{esc(product["map"])}</pre></details></details>')
    groups, _ = expected_groups(product["items"])
    h.append(f'<h2>Items not done · {len(items)}</h2><div class="cols">')
    for word, nums in groups.items():
        h.append(f'<div class="card"><div class="label">{esc(word)} · {len(nums)}</div>')
        for n in nums:
            i = items[n]
            cid = card_id_for_status(i["status"])
            chip = (f'<a class="chip" href="#{cid}" data-fact="item-status">{esc(i["status"])}</a>' if cid
                    else f'<span class="chip" data-fact="item-status">{esc(i["status"])}</span>')
            h.append(f'<div class="pbi"><span class="badge" data-fact="item-number">{n}</span><span class="size" data-fact="item-size">{i["size"]}</span>'
                     f'<div class="ptitle" data-fact="item-title">{esc(i["title"])}</div>{chip}</div>')
        h.append("</div>")
    h.append("</div></section>")
    sprints = [(p, t) for p, t in open_logs.items() if t["kind"] == "sprint"]
    h.append(f'<h2>Sprints · {len(sprints)}</h2><div class="grid2">')
    for p, t in sprints:
        h.append(f'<div class="card" id="{folder(p)}" data-log="{p}"><div class="label">{esc(folder(p))}</div>'
                 f'<div class="kv"><span>Sprint Goal</span><p data-fact="commitment" data-name="Sprint Goal">{esc(t["commitments"]["Sprint Goal"])}</p></div>'
                 f'<div class="kv"><span>Now</span><p data-fact="now">{esc(t["now"])}</p></div>')
        stages = "".join((f'<li class="cur" data-fact="stage">{s}</li>' if s == t["stage"] else f"<li>{s}</li>") for s in STAGES)
        h.append(f'<div class="kv"><span>Stage</span><ol class="stages">{stages}</ol></div><div class="kv"><span>Items</span><ul>')
        for i in t["items"]:
            w = items[i["number"]]
            h.append(f'<li><span data-fact="item-number">{i["number"]}</span> <span data-fact="item-title">{esc(w["title"])}</span> '
                     f'<span class="chip" data-fact="item-status">{esc(w["status"])}</span></li>')
        h.append('</ul></div><div class="kv"><span>How</span><ul class="blocks">')
        for b in t["blocks"]:
            h.append(f'<li{" class=\"done\"" if b["done"] else ""} data-fact="block" data-done="{str(b["done"]).lower()}">{esc(b["text"])}</li>')
        h.append("</ul></div>")
        if t["waiting"] not in (None, "None"):
            h.append(f'<div class="kv"><span>Waiting for the Product Owner</span><p class="warn" data-fact="waiting">{esc(t["waiting"])}</p></div>')
        h.append(src(t) + "</div>")
    h.append("</div>")
    designs = [(p, t) for p, t in open_logs.items() if t["kind"] == "design"]
    h.append(f'<h2>Designs · {len(designs)}</h2><div class="grid2">')
    for p, t in designs:
        h.append(f'<div class="card" id="{folder(p)}" data-log="{p}"><div class="label">{esc(folder(p))}</div>'
                 f'<div class="kv"><span>Design goal</span><p data-fact="commitment" data-name="Design goal">{esc(t["commitments"]["Design goal"])}</p></div>'
                 f'<div class="kv"><span>Now</span><p data-fact="now">{esc(t["now"])}</p></div>'
                 f'<div class="kv"><span>Solution being worked on</span><p data-fact="solution">{esc(t["solution"])}</p></div>'
                 f'<details class="card map" id="{folder(p)}-map"><summary>Map</summary><div class="drawn"></div><details class="src"><summary>Map source</summary>'
                 f'<pre class="source" data-fact="map">{esc(t["map"])}</pre></details></details>')
        for q, u in logs.items():
            if u["kind"] == "ideo" and u["for"] and folder(q) and pathlib.PurePosixPath(u["for"]).parts[-2] == folder(p):
                h.append(f'<div class="kv"><span>IDEO log</span><p><span data-fact="now" data-log="{q}">{esc(u["now"])}</span></p></div>')
        if t["waiting"] not in (None, "None"):
            h.append(f'<div class="kv"><span>Waiting for the Product Owner</span><p class="warn" data-fact="waiting">{esc(t["waiting"])}</p></div>')
        h.append(src(t) + "</div>")
    h.append("</div></div></body></html>")
    return "\n".join(h)


# ========================================================================================================= commands
def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        ok = ok and bool(cond)
        print(("PASS  " if cond else "FAIL  ") + name + (f"  {detail}" if detail and not cond else ""))

    for scenario in ("A", "B"):
        with tempfile.TemporaryDirectory(prefix="boardfix-") as d:
            repo = build_fixture(pathlib.Path(d) / "repo", scenario)
            truth = read_truth(repo, scenario)
            logs = truth["logs"]
            check(f"[{scenario}] truth: product, two Sprints, a design, an IDEO log; the archived Sprint is not open",
                  sorted(t["kind"] for t in logs.values()) == ["design", "ideo", "product", "sprint", "sprint"]
                  and not any("sprint-00" in p for p in logs) and not any("sprint-09-nested" in p for p in logs))
            s1 = logs["scrum/sprint-01-alpha/SprintBacklog.md"]
            check(f"[{scenario}] truth: Sprint 01 is read from {'the working copy' if scenario == 'B' else 'its branch'}",
                  s1["in_working_copy"] == (scenario == "B") and (s1["stage"] == ("Increment" if scenario == "B" else "How")))
            check(f"[{scenario}] truth: facts of the logs",
                  s1["blocks"] == [{"text": "列表页骨架", "done": True}, {"text": "状态列", "done": False}, {"text": "筛选", "done": False}]
                  and logs["scrum/sprint-02-beta/SprintBacklog.md"]["waiting"] == "None"
                  and logs["scrum/sprint-02-beta/SprintBacklog.md"]["blocks"] == [
                      {"text": "Packing slip template", "done": True}, {"text": "Print button", "done": False}]
                  and logs["scrum/design-gamma/DesignBacklog.md"]["solution"] == "分批重试流程"
                  and "<br/>" in logs["scrum/ProductBacklog.md"]["map"] and len(logs["scrum/ProductBacklog.md"]["items"]) == 5)
            board_dir = repo / "scrum"
            page = pathlib.Path(d) / "Board.html"
            ref = render_reference(truth, board_dir)
            page.write_text(ref, encoding="utf-8")
            (board_dir).mkdir(exist_ok=True)
            fails = check_page(page, truth, board_dir)
            check(f"[{scenario}] a correct page passes", not fails, "; ".join(fails[:3]))

            def mutate(name, fn):
                m = fn(ref)
                if m == ref:
                    check(f"[{scenario}] caught: {name}", False, "the mutation changed nothing")
                    return
                page.write_text(m, encoding="utf-8")
                got = check_page(page, truth, board_dir)
                check(f"[{scenario}] caught: {name}", bool(got), "the checker passed a broken page")

            mutate("a commitment changed by one character", lambda s: s.replace("看得清：每笔订单", "看得清：每笔订单。", 1).replace("订单台：把订单从", "订单台：把订单由", 1))
            mutate("a Sprint Goal reworded", lambda s: s.replace("订单一眼看清：列表上直接看到每笔订单的状态。", "订单一眼看清：列表上看到每笔订单的状态。"))
            mutate("a Waiting for PO entry dropped from the banner", lambda s: re.sub(r'<li><strong>sprint-01-alpha</strong>.*?</li>', "", s, count=1, flags=re.S))
            mutate("a Now line paraphrased", lambda s: s.replace("Developer 起草方案，等 Master 审", "Developer 写方案，等 Master 审").replace("块 1 做完，块 2 在做", "块 1 完成，块 2 在做"))
            mutate("a work item's done flag flipped", lambda s: s.replace('data-done="true"', 'data-done="false"', 1))
            mutate("a dead link", lambda s: s.replace('href="ProductBacklog.md"', 'href="Nope.md"', 1))
            mutate("a dead in-page link", lambda s: s.replace('href="#sprint-02-beta"', 'href="#sprint-99"', 1))
            mutate("an item status changed", lambda s: s.replace("待选（副线）", "待选", 1))
            mutate("an archived item shown", lambda s: s.replace('<div class="cols">', '<div class="cols"><div class="card"><div class="label">Other · 1</div><div class="pbi"><span data-fact="item-number">PBI-0</span><div data-fact="item-title">旧的导入功能</div><span data-fact="item-status">已做完</span></div></div>', 1))
            mutate("the map changed", lambda s: s.replace("② 发货", "② 发货单", 1))
            mutate("the map's <br/> left unescaped", lambda s: s.replace("下单&lt;br/&gt;付款", "下单<br/>付款", 1))
            mutate("the source line wrong", lambda s: re.sub(r"branch sprint-02-beta @ [0-9a-f]{7}", "branch sprint-02-beta @ 0000000", s, count=1))
            mutate("a Sprint card dropped", lambda s: re.sub(r'<div class="card" id="sprint-02-beta".*?</ul></div>(?=<div class="kv"><span>Waiting|<div class="src">)', "", s, count=1, flags=re.S) if False else s.replace('id="sprint-02-beta"', 'id="sprint-02-x"'))
            mutate("two groups merged", lambda s: s.replace(' · 2</div>', ' · 2</div>', 1).replace('<div class="label">副线 · 2</div>', '<div class="label">主线 · 2</div>', 1))
            mutate("the IDEO line dropped", lambda s: re.sub(r'<div class="kv"><span>IDEO log</span>.*?</p></div>', "", s, count=1, flags=re.S))
            mutate("an invented fact", lambda s: s.replace('<h1>Project board</h1>', '<h1>Project board</h1><p data-fact="now" data-log="scrum/sprint-01-alpha/SprintBacklog.md">Increment：全做完了</p>', 1))
            mutate("the stage marker on the wrong stage", lambda s: re.sub(r'<li class="cur" data-fact="stage">(\w+)</li>', lambda mo: f"<li>{mo.group(1)}</li>", s, count=1).replace("<li>Test</li>", '<li class="cur" data-fact="stage">Test</li>', 1))
            mutate("a waiting entry invented for a log that says None", lambda s: s.replace('</ul></div><div class="kv"><span>Waiting', '</ul></div><div class="kv"><span>Waiting', 1).replace('<div class="src"><span data-fact="source">branch sprint-02-beta', '<div class="kv"><span>Waiting for the Product Owner</span><p data-fact="waiting">None</p></div><div class="src"><span data-fact="source">branch sprint-02-beta', 1))
            # the empty state: nothing waits, one line says so, no banner lists anything
            import copy
            t2 = copy.deepcopy(truth)
            for t in t2["logs"].values():
                if t["waiting"] is not None:
                    t["waiting"] = "None"
            ref2 = render_reference(t2, board_dir)
            page.write_text(ref2, encoding="utf-8")
            check(f"[{scenario}] nothing waits: the page with the one-line empty state passes", not check_page(page, t2, board_dir),
                  "; ".join(check_page(page, t2, board_dir)[:3]))
            page.write_text(ref2.replace('<div class="banner none"><strong>Nothing is waiting for the Product Owner.</strong></div>', ""), encoding="utf-8")
            check(f"[{scenario}] caught: the empty-state line missing", bool(check_page(page, t2, board_dir)))
            page.write_text(ref2.replace('<h1>Project board</h1>', '<h1>Project board</h1><div class="banner"><ul><li><span data-fact="waiting" data-log="scrum/sprint-01-alpha/SprintBacklog.md">PBI-1 做不做</span></li></ul></div>'), encoding="utf-8")
            check(f"[{scenario}] caught: a banner that lists something when nothing waits", bool(check_page(page, t2, board_dir)))
            # two pages from the same state hold the same facts; a different one does not
            page.write_text(ref.replace("2026-11-13 23:00", "2026-11-14 08:15"), encoding="utf-8")
            other = pathlib.Path(d) / "Board2.html"
            other.write_text(ref, encoding="utf-8")
            check(f"[{scenario}] compare: the same facts, a different time, are equal", fact_set(page) == fact_set(other))
            other.write_text(ref.replace("发货单", "发货单。", 1), encoding="utf-8")
            check(f"[{scenario}] compare: a changed fact is different", fact_set(page) != fact_set(other))
    print("selftest", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["selftest", "fixture", "check", "compare", "facts"])
    ap.add_argument("files", nargs="*")
    ap.add_argument("--dest")
    ap.add_argument("--repo")
    ap.add_argument("--page")
    ap.add_argument("--scenario", default="A")
    a = ap.parse_args()
    if a.cmd == "selftest":
        return selftest()
    if a.cmd == "fixture":
        print(build_fixture(a.dest, a.scenario))
        return 0
    if a.cmd == "facts":
        for f in page_facts(load_page(a.page)):
            print(f["fact"], f["log"], f["extra"], f["text"][:100])
        return 0
    if a.cmd == "compare":
        sets = [fact_set(p) for p in a.files]
        same = all(s == sets[0] for s in sets)
        print("same facts" if same else "DIFFERENT facts")
        if not same:
            base = set(map(repr, sets[0]))
            for p, s in zip(a.files[1:], sets[1:]):
                cur = set(map(repr, s))
                print(p, "only here:", sorted(cur - base)[:5], "| missing:", sorted(base - cur)[:5])
        return 0 if same else 1
    truth = read_truth(a.repo, a.scenario)
    fails = check_page(a.page, truth, pathlib.Path(a.repo) / "scrum")
    for f in fails:
        print("FAIL", f)
    print("page OK" if not fails else f"{len(fails)} failure(s)")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
