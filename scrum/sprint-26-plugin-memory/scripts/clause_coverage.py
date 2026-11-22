"""Sprint 26, Codex review follow-up (Master 2026-11-23): every clause of every old rule must have a home.

    python -X utf8 -I scripts/clause_coverage.py              write review/clause-coverage.md and print the counts
    python -X utf8 -I scripts/clause_coverage.py --show N     print the uncovered clauses of the first N rules (a working view)
    python -X utf8 -I scripts/clause_coverage.py --reverse    the other direction: parts of a list line that no old rule says
    python -X utf8 -I scripts/clause_coverage.py --plugin [DIR]   the same check on the files that landed in the plugin
                                                              (default plugins/ideo-scrum/skills/memory/; the list is its SKILL.md);
                                                              writes review/clause-coverage-plugin.md
    python -X utf8 -I scripts/clause_coverage.py --selftest

Each of the 111 old rules (review/ledger.json) is split into clauses: sentences, and the parts of a sentence between
semicolons. A clause is covered when most of its content words stand together in one sentence of a place that rule went
to: its own list lines, its details file, the target it was merged into, the line that indexes it (`via`), or the
`where_else` text that says where else it lives. A clause that is not covered needs a decision in
review/clause-decisions.json: `added` (the text was put back, so it is covered now), `reworded` (the same thing in
other words, in the place named), `elsewhere` (it lives in another place, named: a details file, a list line, a plugin
template or skill) or `dropped` (deliberately, with the reason). The place of the first three is read back and must
carry the clause (`added` 0.62 of its words in one sentence, `elsewhere` 0.5, `reworded` 0.45); a decision whose place
does not, stays open unless it says `"force": true` with a reason. A script cannot judge meaning: a covered clause can
still be worded wrongly, and the review documents are where that is read. It catches what drops out unnoticed.
"""
from __future__ import annotations

import glob
import json
import pathlib
import re
import sys
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
LEDGER = SPRINT / "review" / "ledger.json"
DRAFT = SPRINT / "review" / "draft"
ROOT = SPRINT.parents[1]


def _memory_files() -> tuple[pathlib.Path, pathlib.Path, bool]:
    """The details folder and the list file: the draft, or (with --plugin [DIR]) the files that landed in the plugin."""
    if "--plugin" in sys.argv:
        i = sys.argv.index("--plugin")
        arg = sys.argv[i + 1] if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith("--") else None
        mem = pathlib.Path(arg) if arg else ROOT / "plugins" / "ideo-scrum" / "skills" / "memory"
        return mem / "details", (mem / "SKILL.md" if (mem / "SKILL.md").exists() else mem / "MEMORY.md"), True
    return SPRINT / "memory-draft" / "details", SPRINT / "memory-draft" / "MEMORY.md", False


DETAILS, LIST, PLUGIN = _memory_files()
DECISIONS = SPRINT / "review" / "clause-decisions.json"
SOURCED = SPRINT / "review" / "po-sourced.json"  # list lines (re)written on the PO's word or the Master's, not from an old rule
OUT = SPRINT / "review" / ("clause-coverage-plugin.md" if PLUGIN else "clause-coverage.md")
COVERED, PARTIAL = 0.62, 0.45  # share of a clause's content words found together in one target sentence

STOP = set("""a an the of to in on at by for with from and or nor but if then else than as is are was were be been being it its this that
these those there their them they he she we you your our not no do does did done can could may might must should shall will would so such
into onto over under up down out off per via also only own same each any all both either neither more most less least other another one
two three first second third etc when where which who whom whose what how why while whether until after before once because since though
although yet still just very whatever whoever about around between within without upon even too us who s t""".split())
CANON = [(r"\bproduct owners?\b|\bpo\b", "poowner"), (r"\bscrum masters?\b|\bsm\b", "smaster"), (r"\bdevelopers?\b", "devlpr"),
         (r"\bdesigners?\b", "dsgnr"), (r"\bstakeholders?\b", "stkhldr"), (r"\bsprint backlog\b|\bsprint log\b", "sprintlog"),
         (r"\bproduct backlog\b|\bproduct log\b", "productlog"), (r"\bdesign log\b", "designlog"), (r"\bideo log\b", "ideolog")]


def stem(w: str) -> str:
    for suf, keep in (("ies", "y"), ("ing", ""), ("ed", ""), ("es", ""), ("s", "")):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[: -len(suf)] + keep
            break
    if w.endswith("e") and len(w) >= 5:
        w = w[:-1]
    return w


def words(text: str) -> set[str]:
    t = text.lower().replace("’", "'")
    t = re.sub(r"`[^`]*\.(?:md|html|py|js|json|sh)`", " ", t)  # a path is a pointer, not a claim
    for pat, rep in CANON:
        t = re.sub(pat, rep, t)
    out = set()
    for w in re.findall(r"[a-z][a-z0-9'-]*", t):
        w = re.sub(r"'s$", "", w.strip("'-"))  # a possessive is its noun
        if len(w) < 3 or w in STOP:
            continue
        out.add(stem(w))
    return out


def sentences(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)  # diagrams are blocks, not clauses
    out = []
    for chunk in re.split(r"\n+", text):
        chunk = chunk.strip().lstrip("-*| ").strip()
        if not chunk:
            continue
        for s in re.split(r"(?<=[.!?:])\s+(?=[A-Z“\"`(\[*])", chunk):
            for part in re.split(r";\s+", s):
                part = part.strip()
                if part:
                    out.append(part)
    return out


def clauses_of(rule_text: str) -> list[str]:
    body = re.sub(r"^\d+\.\s+\*\*.+?\*\*\s*—\s*", "", rule_text.strip(), count=1)
    body = re.sub(r"\((?:[^()]*\bconventions?\s+\d+[^()]*)\)", " ", body)  # "(overview.md, convention 1)" is a pointer
    out = []
    for s in sentences(body):
        if len(words(s)) >= 3 and not re.match(r"^(this departs from|see the departures)", s, re.I):
            out.append(s)
    return out


def lines_of(o: dict) -> list[str]:
    return [o["line"]] if o.get("line") else (o.get("lines") or [])


def load_rows() -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for fp in sorted(glob.glob(str(DRAFT / "*.json"))):
        for o in json.loads(pathlib.Path(fp).read_text(encoding="utf-8")):
            rows[o["id"]] = o
    if PLUGIN:  # check what landed, not what was drafted: each draft line is replaced by the landed line of the same handle
        live = {m.group(1): ln for ln in list_lines() for m in [re.match(r"^- \*\*([a-z0-9-]+)\*\*", ln)] if m}

        def land(ln: str) -> str:
            m = re.match(r"^- \*\*([a-z0-9-]+)\*\*", ln)
            return live.get(m.group(1), f"- **{m.group(1)}** (this line did not land in the plugin)") if m else ln

        for o in rows.values():
            if o.get("line"):
                o["line"] = land(o["line"])
            if o.get("lines"):
                o["lines"] = [land(x) for x in o["lines"]]
    return rows


def details_text(name: str | None) -> str:
    if not name:
        return ""
    p = DETAILS / f"{name}.md"
    if p.exists():
        return p.read_text(encoding="utf-8")
    if name == "board-log":  # stays in place; the board lines point at it
        q = SPRINT.parents[1] / "plugins" / "ideo-scrum" / "board" / "board-log.md"
        return q.read_text(encoding="utf-8") if q.exists() else ""
    return ""


def targets_for(i: str, rows: dict[str, dict]) -> list[tuple[str, str]]:
    """(where, sentence) pairs a clause of rule i may be found in."""
    o = rows.get(i)
    if o is None:
        return []
    seen, out = set(), []

    def take(rule_id: str):
        if rule_id in seen or rule_id not in rows:
            return
        seen.add(rule_id)
        r = rows[rule_id]
        for ln in lines_of(r):
            h = re.match(r"^- \*\*([a-z0-9-]+)\*\*", ln)
            out.append((f"line {h.group(1) if h else '?'}", ln))
        if r.get("long_file"):
            for s in sentences(details_text(r["long_file"])):
                out.append((f"details/{r['long_file']}", s))
        if r.get("where_else"):
            for s in sentences(r["where_else"]):
                out.append(("where_else", s))
        if r.get("merged_into"):
            take(r["merged_into"])
        for a in r.get("absorbed") or []:
            pass  # an absorbing rule's text is not where this rule's clauses go
        if r.get("via"):
            for rr in rows.values():
                if any(re.match(rf"^- \*\*{re.escape(r['via'])}\*\*", ln) for ln in lines_of(rr)):
                    for ln in lines_of(rr):
                        out.append((f"line {r['via']}", ln))

    take(i)
    return out


def best(clause: str, targets: list[tuple[str, str]]) -> tuple[float, str, str]:
    cw = words(clause)
    if not cw:
        return 1.0, "", ""
    top = (0.0, "", "")
    for where, s in targets:
        score = len(cw & words(s)) / len(cw)
        if score > top[0]:
            top = (score, where, s)
    return top


ROOT = SPRINT.parents[1]
KINDS = {"added": 0.62, "elsewhere": 0.5, "reworded": 0.45}  # share of the clause's words the named place must carry


def list_lines() -> list[str]:
    return [ln for ln in LIST.read_text(encoding="utf-8").splitlines() if ln.startswith("- **")]


def place_sentences(where: str) -> list[tuple[str, str]]:
    """Places are separated by ';': `details/x.md`, `line <handle>`, `header`, or a path from the repository root."""
    out: list[tuple[str, str]] = []
    for w in [x.strip() for x in where.split(";") if x.strip()]:
        if w.startswith("details/"):
            f = DETAILS / w.split("/", 1)[1]
        elif w.startswith("line "):
            h = w[5:].strip()
            out += [(w, ln) for ln in list_lines() if re.match(rf"^- \*\*{re.escape(h)}\*\*", ln)]
            continue
        elif w == "header":
            out += [(w, s) for s in sentences(LIST.read_text(encoding="utf-8").split("\n- **", 1)[0])]
            continue
        else:
            f = ROOT / w
        if f.exists():
            out += [(w, s) for s in sentences(f.read_text(encoding="utf-8"))]
    return out


def verify(d: dict, clause: str) -> tuple[bool, float]:
    """Does the place a decision names carry the clause? `dropped` needs a reason of its own."""
    if d["decision"] == "dropped":
        return len((d.get("reason") or "").strip()) >= 12, 0.0
    sc, _, _ = best(clause, place_sentences(d.get("where") or ""))
    ok = sc >= KINDS[d["decision"]] or (bool(d.get("force")) and len((d.get("reason") or "").strip()) >= 12)
    return ok, sc


def load_decisions() -> list[dict]:
    return json.loads(DECISIONS.read_text(encoding="utf-8")) if DECISIONS.exists() else []


def decision_for(i: str, clause: str, decisions: list[dict]) -> dict | None:
    for d in decisions:
        if d["id"] == i and clause.startswith(d["clause"]):
            return d
    return None


EXTERNAL_VERBATIM = {"board-log": SPRINT.parents[1] / "plugins" / "ideo-scrum" / "board" / "board-log.md"}  # the file stays in place, so its rules stay word for word


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip().lower()


def anywhere_targets() -> list[tuple[str, str]]:
    out = [("MEMORY.md", ln) for ln in LIST.read_text(encoding="utf-8").splitlines() if ln.startswith("- **")]
    plug = ROOT / "plugins" / "ideo-scrum"
    for fp in sorted(list((plug / "template").glob("*.md")) + list(plug.glob("skills/*/SKILL.md"))):
        out += [(str(fp.relative_to(ROOT)).replace("\\", "/"), s) for s in sentences(fp.read_text(encoding="utf-8"))]
    for fp in sorted(glob.glob(str(DETAILS / "*.md"))):
        name = pathlib.Path(fp).name
        out += [(f"details/{name}", s) for s in sentences(pathlib.Path(fp).read_text(encoding="utf-8"))]
    return out


def analyse() -> list[dict]:
    led = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = load_rows()
    decisions = load_decisions()
    out = []
    for f in led["files"]:
        for r in f["rules"]:
            tg = targets_for(r["id"], rows)
            ext = EXTERNAL_VERBATIM.get(r["id"].split("#")[0])
            ext_text = norm(ext.read_text(encoding="utf-8")) if ext and ext.exists() else ""
            for k, c in enumerate(clauses_of(r["text"]), start=1):
                score, where, snippet = best(c, tg)
                if ext_text and norm(c) in ext_text:
                    score, where, snippet = 1.0, f"{ext.name} (kept in place)", c
                status = "covered" if score >= COVERED else ("partial" if score >= PARTIAL else "missing")
                d = decision_for(r["id"], c, decisions)
                vscore = None
                if d is not None and d.get("decision") in ("added", "elsewhere", "reworded", "dropped"):
                    ok, vscore = verify(d, c)
                    if not ok:
                        d = {**d, "unverified": True}
                o = rows.get(r["id"]) or {}
                if d is None and status != "covered" and not lines_of(o) and not o.get("long_file") and not o.get("merged_into") and not o.get("via") and o.get("where_else"):
                    # a rule the draft drops on purpose: where_else is the reason and the place (it was checked against the files, row 2)
                    d = {"decision": "dropped", "reason": "（草稿里整条不进清单）" + o["where_else"][:150]}
                if d is not None and d.get("unverified"):
                    status_decision = None  # a decision whose place does not carry the clause is no decision
                else:
                    status_decision = d
                out.append({"id": r["id"], "k": k, "clause": c, "score": round(score, 2), "status": status, "where": where,
                            "snippet": snippet[:140], "decision": status_decision, "tried": d if status_decision is None else None,
                            "vscore": None if vscore is None else round(vscore, 2)})
    return out


def counts(items: list[dict]) -> Counter:
    c: Counter = Counter()
    for x in items:
        c["clauses"] += 1
        c[x["status"]] += 1
        if x["status"] != "covered":
            c["accounted" if x["decision"] else "open"] += 1
    return c


def write_report(items: list[dict]) -> None:
    c = counts(items)
    rules = {x["id"] for x in items}
    lines = ["# 分句覆盖核查（Sprint 26，Codex 对抗审查之后）", "",
             "由 `scripts/clause_coverage.py` 生成：111 条旧规矩各按分句（句子，句内分号隔开的部分）拆开，看每个分句的实词是否集中出现在它的去处里"
             "（自己的清单行、细则文件、并入的目标、索引它的那一行、`where_else` 写明的别处）；够不上的需要在 `review/clause-decisions.json` 里记一个决定："
             "`added`（补回去了，补完应能被脚本认出）、`dropped`（有意删，写理由）、`elsewhere`（脚本看不见的别处，写出在哪）。"
             "脚本判不了意思：认为「覆盖」的分句仍可能写歪，那要靠读审阅文件；它抓的是悄悄掉了的半句。", "",
             f"{len(rules)} 条规矩、{c['clauses']} 个分句：覆盖 {c['covered']}，部分 {c['partial']}，缺 {c['missing']}；"
             f"不够的 {c['partial'] + c['missing']} 个里，有决定的 {c['accounted']}，还没有的 {c['open']}。", ""]
    for status, title in (("missing", "缺"), ("partial", "部分")):
        group = [x for x in items if x["status"] == status]
        if not group:
            continue
        lines += [f"## {title}（{len(group)}）", "", "| 规矩 | 分句 | 最像的去处 | 重合 | 决定 |", "| --- | --- | --- | --- | --- |"]
        for x in group:
            d = x["decision"]
            tr = x.get("tried")
            if d:
                dec = f"{d['decision']}（{x['vscore']}）：{d.get('where') or ''} {d.get('reason') or ''}".strip()
            elif tr:
                dec = f"**还没有**（记过一条决定，但它写的去处只有 {x['vscore']} 的重合：{tr.get('where') or ''}）"
            else:
                dec = "**还没有**"
            lines.append(f"| {x['id']}#{x['k']} | {x['clause'][:150].replace('|', '/')} | {x['where']}：{x['snippet'][:90].replace('|', '/')} | {x['score']} | {dec.replace('|', '/')} |")
        lines.append("")
    po = [x for x in items if x["decision"] and x["decision"].get("po")]
    if po:
        lines += [f"## PO 改过的分句（{len(po)}）", "", "PO 的话（`review/po-review-2026-11-23.md`，Master 转来）改了这些分句：脚本按词看它们可能「覆盖」，但意思已经不是旧文的意思；这里单列，决定里写着怎么改、为什么。", "",
                  "| 规矩 | 旧分句 | 决定 |", "| --- | --- | --- |"]
        for x in po:
            d = x["decision"]
            lines.append(f"| {x['id']}#{x['k']} | {x['clause'][:150].replace('|', '/')} | {d['decision']}（{x['vscore']}）：{d.get('where') or ''} {d.get('reason') or ''} |".replace("|  |", "| |"))
        lines.append("")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def sourced() -> dict[str, str]:
    return {x["handle"]: x["source"] for x in json.loads(SOURCED.read_text(encoding="utf-8"))} if SOURCED.exists() else {}


def reverse() -> list[tuple[str, str, float, str]]:
    """Every part of a list line (between semicolons) should come from the old rules that line was made from: a part with
    few of its words in any one sentence of them is new content, and new content needs a source."""
    led = json.loads(LEDGER.read_text(encoding="utf-8"))
    old = {r["id"]: r["text"] for f in led["files"] for r in f["rules"]}
    rows = load_rows()
    out = []
    for i, o in rows.items():
        ls = lines_of(o)
        if not ls:
            continue
        srcs = [i] + [j for j, r in rows.items() if r.get("merged_into") == i] + [a for a in (o.get("absorbed") or []) if isinstance(a, str)]
        sents = []
        for s in srcs:
            body = re.sub(r"^\d+\.\s+\*\*.+?\*\*\s*—\s*", "", old.get(s, "").strip(), count=1)
            sents += sentences(re.sub(r"\((?:[^()]*\bconventions?\s+\d+[^()]*)\)", " ", body))
            if rows.get(s, {}).get("where_else"):
                sents += sentences(rows[s]["where_else"])
        for ln in ls:
            m = re.match(r"^- \*\*([a-z0-9-]+)\*\*\s*(?:\[[a-z,]+\]\s*)?(.*?)(?:\s*Read (?:details|\.\./\.\.)/\S+ first\.)?$", ln)
            if not m:
                continue
            for part in re.split(r";\s+|:\s+", m.group(2)):
                w = words(part)
                if len(w) < 3:
                    continue
                sc = max((len(w & words(s)) / len(w) for s in sents), default=0.0)
                if sc < 0.5:
                    best_s = max(sents, key=lambda s: len(w & words(s)), default="")
                    out.append((m.group(1), part, round(sc, 2), best_s[:120]))
    return out


def selftest() -> int:
    ok = True

    def check(cond: bool, what: str) -> None:
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    cl = clauses_of("5. **Name** — Prepare the documents carefully today. Then review the complete second draft thoroughly; and approve the final version afterwards (convention 4). It carries another useful clause here.")
    check(len(cl) == 4 and cl[2].startswith("and approve"), f"sentences and semicolon parts become clauses ({len(cl)})")
    check("poowner" in words("The Product Owner decides") and "poowner" in words("the PO decided") and "smaster" in words("Scrum Master leads"), "role names are canonical")
    check(stem("decides") == stem("decided") == stem("deciding") == stem("decide"), "word forms meet at one stem")
    t = [("line x", "- **x** The PO decides the items with the Scrum Master; the Scrum Master and Developer say when it is too much.")]
    s_all, _, _ = best("Let the Product Owner decide the items together with the Scrum Master", t)
    s_miss, _, _ = best("At Planning the Product Owner leads the selection, and the Scrum Master says when it is too little", t)
    check(s_all >= COVERED, f"a clause that the line carries is covered ({s_all:.2f})")
    check(s_miss < COVERED, f"a clause the line dropped is not covered ({s_miss:.2f})")
    check(decision_for("a#1", "Do the first thing now.", [{"id": "a#1", "clause": "Do the first"}]) is not None, "a decision is found by the start of the clause")
    ok_d, sc_d = verify({"decision": "elsewhere", "where": "plugins/ideo-scrum/template/sprint-backlog-template.md"}, "Keep every heading, even the ones filled later; add none.")
    check(ok_d and sc_d >= 0.5, f"a decision is read back from the place it names ({sc_d:.2f})")
    ok_n, _ = verify({"decision": "dropped", "reason": ""}, "anything")
    check(not ok_n, "a drop with no reason is not a decision")
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return selftest()
    if "--reverse" in argv:
        rv, src = reverse(), sourced()
        flagged = [x for x in rv if x[0] not in src]
        for h, part, sc, bs in flagged:
            print(f"{h} [{sc}] {part}\n      nearest old: {bs}")
        for h, why in src.items():
            print(f"sourced: {h} - {why}")
        print(f"{len(flagged)} parts of list lines with little support in their old rules; {len(rv) - len(flagged)} more parts are on a named source ({len(src)} lines in review/po-sourced.json)")
        return 0
    items = analyse()
    write_report(items)
    c = counts(items)
    print(f"{c['clauses']} clauses of {len({x['id'] for x in items})} rules: covered {c['covered']}, partial {c['partial']}, missing {c['missing']}; "
          f"of the {c['partial'] + c['missing']} not covered: with a decision {c['accounted']}, open {c['open']}")
    if "--show" in argv:
        n = int(argv[argv.index("--show") + 1])
        shown = 0
        last = None
        for x in items:
            if x["status"] != "covered" and not x["decision"]:
                if x["id"] != last:
                    shown += 1
                    last = x["id"]
                if shown > n:
                    break
                print(f"{x['id']}#{x['k']} [{x['status']} {x['score']}] {x['clause'][:230]}")
                if "--anywhere" in argv:
                    sc, wh, sn = best(x["clause"], anywhere_targets())
                    print(f"      anywhere {sc:.2f} {wh}: {sn[:150]}")
    return 0 if c["open"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
