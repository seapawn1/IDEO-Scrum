"""Sprint 27 trigger test (PBI-86): which role entry does the model load for a plain request?

Two arms, same day, same environment: the baseline (a git revision, normally 1145382) and the candidate (the
sprint branch). A trial is one headless magpie session with read-only tools; the judge reads only the Skill calls in
its stream. The prompts and the pass lines are frozen: prompts.json beside this file, THRESHOLDS below, and chapter 2.2
of the sprint log. Raw output goes outside the repository.

  python -X utf8 -I run_trigger.py --selftest
  python -X utf8 -I run_trigger.py --probe  --candidate REV
  python -X utf8 -I run_trigger.py --smoke  --baseline REV --candidate REV
  python -X utf8 -I run_trigger.py --run    --baseline REV --candidate REV [--groups A,B,C] [--reps 3]
                                            [--rep-start 1] [--out DIR] [--workers 3] [--max-minutes 150]
  python -X utf8 -I run_trigger.py --judge  DIR
"""
import argparse
import concurrent.futures as cf
import io
import json
import math
import os
import pathlib
import shutil
import subprocess
import sys
import tarfile
import threading
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
PROMPTS = HERE / "prompts.json"
FIXTURE = REPO / "scripts" / "board_check" / "fixtures" / "acme"
PUBLIC = pathlib.Path(r"C:\Users\Public\s27-trigger")
ARCHIVE = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-27-wrap-up\trigger")
PREFIX = "ideo-scrum:"
ROLES = ("scrum-master", "developer", "designer", "stakeholder", "supporter")
DISALLOWED = "Bash,PowerShell,Write,Edit,NotebookEdit,Workflow,SendMessage,WebFetch,WebSearch,mcp__*"
INSTRUCTION_FILES = ("CLAUDE.md", "CLAUDE.local.md", "AGENTS.md", ".claude/CLAUDE.md")
# The pass lines of chapter 2.2 (Master 2026-11-22): A: the candidate loads `supporter` in at least two thirds of the
# trials; B, C: the candidate's hits are not below the baseline's; mixing: at most one per nine trials.
THRESHOLDS = {"A_min_fraction": 2 / 3, "mix_per_nine": 1}


# ---------------------------------------------------------------- the judge (no model, no files)

def judge_stream(lines):
    """Read one trial's stream-json lines; return what the judge needs."""
    rec = {"init": False, "tools": None, "permission_mode": None, "model": None, "skills": [], "roles": [],
           "result_subtype": None, "is_error": None, "denials": None, "cost_usd": None, "has_assistant": False}
    for line in lines:
        try:
            d = json.loads(line)
        except ValueError:
            continue
        kind, sub = d.get("type"), d.get("subtype")
        if kind == "system" and sub == "init":
            rec.update(init=True, tools=d.get("tools"), permission_mode=d.get("permissionMode"), model=d.get("model"))
        elif kind == "assistant":
            rec["has_assistant"] = True
            content = (d.get("message") or {}).get("content")
            for block in content if isinstance(content, list) else []:
                if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") == "Skill":
                    inp = block.get("input") or {}
                    name = str(inp.get("skill") or inp.get("name") or inp.get("command") or "").strip()
                    if name:
                        rec["skills"].append(name)
        elif kind == "result":
            rec.update(result_subtype=sub, is_error=d.get("is_error"), denials=len(d.get("permission_denials") or []),
                       cost_usd=d.get("total_cost_usd"))
    for name in rec["skills"]:
        bare = name[len(PREFIX):] if name.startswith(PREFIX) else name
        if bare in ROLES and bare not in rec["roles"]:
            rec["roles"].append(bare)
    rec["first_role"] = rec["roles"][0] if rec["roles"] else None
    rec["valid"], rec["why_invalid"] = True, ""
    if not rec["init"]:
        rec["valid"], rec["why_invalid"] = False, "no init event"
    elif rec["result_subtype"] is None:
        rec["valid"], rec["why_invalid"] = False, "no result event"
    elif str(rec["result_subtype"]).startswith("error") and rec["result_subtype"] != "error_max_turns":
        rec["valid"], rec["why_invalid"] = False, "result " + str(rec["result_subtype"])
    return rec


def cell_counts(trials):
    """(arm, group) -> {n, hits, mix, first, none}: the first valid attempt of each slot counts."""
    prompts = json.loads(PROMPTS.read_text(encoding="utf-8"))["groups"]
    taken, cells = set(), {}
    for t in trials:
        slot = (t["arm"], t["group"], t["prompt_index"], t["rep"])
        if not t.get("valid") or slot in taken:
            continue
        taken.add(slot)
        cell = cells.setdefault((t["arm"], t["group"]), {"n": 0, "hits": 0, "mix": 0, "none": 0, "first": {}})
        spec = prompts[t["group"]]
        cell["n"] += 1
        cell["hits"] += spec["expect"] in t["roles"]
        cell["mix"] += bool(spec["wrong"]) and spec["wrong"] in t["roles"]
        cell["none"] += not t["roles"]
        cell["first"][t["first_role"] or "-"] = cell["first"].get(t["first_role"] or "-", 0) + 1
    return cells


def evaluate(cells, expected_n):
    """expected_n: group -> trials per arm that must be valid. Returns (checks, near_miss_groups)."""
    checks, near = [], []
    for g, want in expected_n.items():
        base, cand = cells.get(("baseline", g), {}), cells.get(("candidate", g), {})
        if base.get("n", 0) != want or cand.get("n", 0) != want:
            checks.append((g, "complete", False, "valid trials baseline %s, candidate %s, need %s" % (
                base.get("n", 0), cand.get("n", 0), want)))
            continue
        if g == "A":
            need = math.ceil(want * THRESHOLDS["A_min_fraction"])
            ok = cand["hits"] >= need
            checks.append((g, "candidate loads supporter >= %d/%d" % (need, want), ok, "got %d" % cand["hits"]))
            if not ok and cand["hits"] == need - 1:
                near.append(g)
        else:
            ok = cand["hits"] >= base["hits"]
            checks.append((g, "candidate hits >= baseline hits", ok, "candidate %d, baseline %d" % (cand["hits"], base["hits"])))
            if not ok and cand["hits"] == base["hits"] - 1:
                near.append(g)
        if g in ("A", "B"):
            limit = want // 9 * THRESHOLDS["mix_per_nine"]
            ok = cand["mix"] <= limit
            who = "stakeholder in A" if g == "A" else "supporter in B"
            checks.append((g, "mixing: %s <= %d" % (who, limit), ok, "got %d" % cand["mix"]))
    return checks, near


# ---------------------------------------------------------------- the host side

def tool_dirs():
    out = set()
    for name in ("git", "sh", "python", "node", "magpie"):
        found = shutil.which(name)
        if found:
            out.add(str(pathlib.Path(found).parent).replace("\\", "/").lower())
    return out


def make_env(base):
    """An allow-list environment, as the handbook asks: no host variables, a fresh home, fresh TEMP."""
    whitelist = {"systemroot", "path", "comspec", "pathext", "windir"}
    env = {k: v for k, v in os.environ.items() if k.lower() in whitelist}
    real_home = os.environ["USERPROFILE"]
    home = base / "home"
    (home / "AppData" / "Roaming").mkdir(parents=True, exist_ok=True)
    (home / "AppData" / "Local").mkdir(parents=True, exist_ok=True)
    userbin = home / ".local" / "bin"
    userbin.mkdir(parents=True, exist_ok=True)
    for k in list(env):
        if k.lower() == "path":
            kept = []
            for entry in env[k].split(os.pathsep):
                e = entry.strip().strip('"')
                if not e or not os.path.isdir(e):
                    continue
                n = e.replace("\\", "/").lower().rstrip("/")
                rh = real_home.replace("\\", "/").lower()
                if (n == rh or n.startswith(rh + "/")) and n not in tool_dirs():
                    continue
                kept.append(e)
            env[k] = os.pathsep.join([str(userbin), *kept])
    tmp = base / "tmp"
    tmp.mkdir(exist_ok=True)
    drive, tail = os.path.splitdrive(str(home))
    env.update({
        "USERPROFILE": str(home), "HOME": str(home), "HOMEDRIVE": drive, "HOMEPATH": tail,
        "APPDATA": str(home / "AppData" / "Roaming"), "LOCALAPPDATA": str(home / "AppData" / "Local"),
        "TEMP": str(tmp), "TMP": str(tmp), "CLAUDE_CONFIG_DIR": str(home / ".claude"),
        "XDG_CONFIG_HOME": str(pathlib.Path(real_home) / ".config"),
        "XDG_CACHE_HOME": str(pathlib.Path(real_home) / ".cache"),
        "MSYS_NO_PATHCONV": "1",
    })
    sh = shutil.which("sh")
    if sh:
        env["CLAUDE_CODE_GIT_BASH_PATH"] = str(pathlib.Path(sh).with_name("bash.exe"))
    return env


def magpie_prefix():
    wrapper = shutil.which("claude-magpie.cmd")
    if not wrapper:
        sys.exit("claude-magpie.cmd is not on PATH")
    exe = shutil.which("magpie", path=str(pathlib.Path(wrapper).parent))
    return [exe, "claude", "run"] if exe else [wrapper]


def instruction_files_above(path):
    found = []
    for folder in [pathlib.Path(path).resolve(), *pathlib.Path(path).resolve().parents]:
        for rel in INSTRUCTION_FILES:
            if (folder / rel).is_file():
                found.append(str(folder / rel))
        rules = folder / ".claude" / "rules"
        if rules.is_dir():
            found.extend(str(p) for p in sorted(rules.rglob("*.md")))
    return found


def extract_arm(rev, dest):
    """The plugin as committed at REV, extracted with git archive (not the working copy)."""
    data = subprocess.run(["git", "-C", str(REPO), "archive", rev, "plugins/ideo-scrum"],
                          capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(data)) as tf:
        tf.extractall(dest, filter="data")
    return dest / "plugins" / "ideo-scrum"


def rev_id(rev):
    return subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", rev], capture_output=True, text=True,
                          check=True).stdout.strip()


def run_trial(root, arm, plugin, group, pidx, prompt, rep, attempt, timeout=240):
    base = root / "trials" / ("%s-%s%d-r%d-a%d" % (arm, group, pidx + 1, rep, attempt))
    proj = base / "proj"
    shutil.copytree(FIXTURE, proj)
    env = make_env(base)
    cmd = magpie_prefix() + [
        "-p", "--plugin-dir", str(plugin), "--input-format", "stream-json", "--output-format", "stream-json",
        "--verbose", "--model", "haiku", "--tools", "Read,Grep,Glob,Skill", "--disallowedTools", DISALLOWED,
        "--strict-mcp-config", "--permission-mode", "dontAsk", "--setting-sources", "project,local",
        "--max-turns", "4"]
    t0 = time.time()
    proc = subprocess.Popen(cmd, cwd=str(proj), env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    lines, errs = [], []
    readers = [threading.Thread(target=lambda: [lines.append(r.decode("utf-8", "replace").rstrip("\r\n")) for r in proc.stdout], daemon=True),
               threading.Thread(target=lambda: [errs.append(r.decode("utf-8", "replace")) for r in proc.stderr], daemon=True)]
    for t in readers:
        t.start()
    try:
        message = {"type": "user", "message": {"role": "user", "content": prompt}}
        proc.stdin.write((json.dumps(message, ensure_ascii=False) + "\n").encode("utf-8"))
        proc.stdin.close()
    except OSError:
        pass
    while proc.poll() is None and time.time() - t0 < timeout:
        time.sleep(0.5)
    timed_out = proc.poll() is None
    if timed_out:  # kill the whole tree: killing only the wrapper leaves the CLI running (handbook)
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True)
    for t in readers:
        t.join(5)
    (base / "session.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (base / "stderr.log").write_text("".join(errs), encoding="utf-8")
    rec = judge_stream(lines)
    if timed_out:
        rec["valid"], rec["why_invalid"] = False, "timeout"
    rec.update(arm=arm, group=group, prompt_index=pidx, rep=rep, attempt=attempt, elapsed_s=round(time.time() - t0, 1),
               trial=base.name)
    return rec


def probe(plugin, root):
    base = root / "probe"
    proj = base / "proj"
    shutil.copytree(FIXTURE, proj)
    env = make_env(base)
    cmd = magpie_prefix() + ["-p", "--output-format", "text", "--model", "haiku", "--tools", "",
                             "--setting-sources", "project,local", "/context all"]
    try:
        r = subprocess.run(cmd, cwd=str(proj), env=env, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=180, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError) as exc:
        return {"ok": False, "error": type(exc).__name__}
    leak = [x for x in instruction_files_above(proj) if "Public" not in x]
    return {"ok": r.returncode == 0 and "Context Usage" in r.stdout and not leak, "exit": r.returncode,
            "has_context_usage": "Context Usage" in r.stdout, "leak": leak}


# ---------------------------------------------------------------- commands

def load_prompts():
    return json.loads(PROMPTS.read_text(encoding="utf-8"))


def stamp():
    return time.strftime("%Y%m%d-%H%M%S")


def cmd_probe(args):
    root = PUBLIC / ("probe-" + stamp())
    result = probe(None, root)
    print(json.dumps(result, ensure_ascii=False))
    shutil.rmtree(root, ignore_errors=True)
    return 0 if result["ok"] else 1


def cmd_smoke(args):
    prompts = load_prompts()
    root = PUBLIC / ("smoke-" + stamp())
    out = {}
    for arm, rev in (("baseline", args.baseline), ("candidate", args.candidate)):
        plugin = extract_arm(rev, root / "arms" / arm)
        rec = run_trial(root, arm, plugin, "C", 0, prompts["smoke"], 1, 1)
        init_ok = (rec["permission_mode"] == "dontAsk" and rec["tools"] is not None
                   and not {"Bash", "PowerShell", "Write", "Edit"} & set(rec["tools"] or []))
        out[arm] = {"rev": rev_id(rev), "valid": rec["valid"], "why": rec["why_invalid"], "permission_mode": rec["permission_mode"],
                    "tools": rec["tools"], "model_set": bool(rec["model"]), "skills": rec["skills"], "init_restricted": init_ok,
                    "result": rec["result_subtype"], "elapsed_s": rec["elapsed_s"]}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    shutil.rmtree(root, ignore_errors=True)
    return 0 if all(v["valid"] and v["init_restricted"] for v in out.values()) else 1


def cmd_run(args):
    prompts = load_prompts()["groups"]
    groups = [g for g in args.groups.split(",") if g]
    out = pathlib.Path(args.out) if args.out else ARCHIVE / (stamp() + "-round" + str(args.round))
    out.mkdir(parents=True, exist_ok=True)
    root = PUBLIC / ("run-" + stamp())
    arms = {"baseline": (args.baseline, extract_arm(args.baseline, root / "arms" / "baseline")),
            "candidate": (args.candidate, extract_arm(args.candidate, root / "arms" / "candidate"))}
    meta = {"stamp": stamp(), "baseline": rev_id(args.baseline), "candidate": rev_id(args.candidate), "groups": groups,
            "reps": args.reps, "rep_start": args.rep_start, "round": args.round,
            "model_note": "magpie's cheap model (not Haiku): --model haiku is remapped by the wrapper"}
    meta_path = out / "meta.jsonl"
    with meta_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    jobs = []
    for rep in range(args.rep_start, args.rep_start + args.reps):
        for g in groups:
            for pi, text in enumerate(prompts[g]["prompts"]):
                for arm in ("baseline", "candidate"):
                    jobs.append((arm, g, pi, text, rep))
    lock = threading.Lock()
    deadline = time.time() + args.max_minutes * 60
    results = out / "results.jsonl"

    def work(job):
        arm, g, pi, text, rep = job
        rec = None
        for attempt in range(1, 4):
            if time.time() > deadline:
                break
            rec = run_trial(root, arm, arms[arm][1], g, pi, text, rep, attempt)
            with lock, results.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print("%s %s%d r%d a%d valid=%s roles=%s %ss" % (arm, g, pi + 1, rep, attempt, rec["valid"], rec["roles"],
                                                          rec["elapsed_s"]), flush=True)
            if rec["valid"]:
                break
        return rec

    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(work, jobs))
    raw = out / "raw"
    raw.mkdir(exist_ok=True)
    for d in (root / "trials").glob("*"):
        for name in ("session.jsonl", "stderr.log"):
            if (d / name).is_file():
                shutil.copy2(d / name, raw / ("%s.%s" % (d.name, name)))
    shutil.rmtree(root, ignore_errors=True)
    print("written", out)
    return cmd_judge(argparse.Namespace(dir=str(out)))


def cmd_judge(args):
    out = pathlib.Path(args.dir)
    trials = [json.loads(x) for x in (out / "results.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    groups = sorted({t["group"] for t in trials})
    reps = {g: len({t["rep"] for t in trials if t["group"] == g}) for g in groups}
    expected = {g: len(load_prompts()["groups"][g]["prompts"]) * reps[g] for g in groups}
    cells = cell_counts(trials)
    for (arm, g), c in sorted(cells.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        print("%-9s %s  n=%-2d hits=%-2d mix=%-2d no-role=%-2d first=%s" % (arm, g, c["n"], c["hits"], c["mix"], c["none"], c["first"]))
    checks, near = evaluate(cells, expected)
    for g, what, ok, detail in checks:
        print("%s  %-4s %s (%s)" % ("PASS" if ok else "FAIL", g, what, detail))
    if near:
        print("near miss by one (supplement rule: both arms, each prompt 3 more times, judge once on the combined count):", near)
    technical = [t for t in trials if not t["valid"]]
    print("technical failures:", len(technical), [(t["trial"], t["why_invalid"]) for t in technical][:12])
    return 0 if checks and all(c[2] for c in checks) else 1


def cmd_selftest(args):
    def stream(skills, subtype="success", init=True, assistant=True):
        rows = []
        if init:
            rows.append({"type": "system", "subtype": "init", "tools": ["Read", "Skill"], "permissionMode": "dontAsk", "model": "m"})
        if assistant:
            rows.append({"type": "assistant", "message": {"content": [
                {"type": "text", "text": "x"}] + [{"type": "tool_use", "name": "Skill", "input": {"skill": s}} for s in skills]}})
        if subtype:
            rows.append({"type": "result", "subtype": subtype, "is_error": subtype != "success", "permission_denials": [], "total_cost_usd": 0.01})
        return [json.dumps(r) for r in rows]

    failures = []

    def expect(label, got, want):
        if got != want:
            failures.append("%s: got %r, want %r" % (label, got, want))

    r = judge_stream(stream(["ideo-scrum:supporter", "ideo-scrum:ideo-kernel"]))
    expect("supporter loaded", (r["roles"], r["first_role"], r["valid"]), (["supporter"], "supporter", True))
    r = judge_stream(stream(["ideo-scrum:ideo-kernel", "ideo-scrum:stakeholder", "ideo-scrum:supporter"]))
    expect("first role is the first one called, both are loaded", (r["roles"], r["first_role"]), (["stakeholder", "supporter"], "stakeholder"))
    r = judge_stream(stream(["scrum-master"]))
    expect("a name without the prefix counts (DSH style)", r["roles"], ["scrum-master"])
    r = judge_stream(stream(["ideo-scrum:project-stakeholder", "ideo-scrum:second-opinion"]))
    expect("a skill that only contains a role name is not a role", r["roles"], [])
    r = judge_stream(stream([], subtype="error_max_turns"))
    expect("max turns is a valid trial", r["valid"], True)
    r = judge_stream(stream(["ideo-scrum:supporter"], subtype="error_during_execution"))
    expect("an execution error is a technical failure", (r["valid"], r["why_invalid"]), (False, "result error_during_execution"))
    r = judge_stream(stream(["ideo-scrum:supporter"], init=False))
    expect("no init is a technical failure", r["valid"], False)
    r = judge_stream(stream(["ideo-scrum:supporter"], subtype=None))
    expect("no result is a technical failure", r["valid"], False)
    r = judge_stream(["not json", ""] + stream(["ideo-scrum:developer"]))
    expect("noise lines are skipped", r["roles"], ["developer"])

    def trials(arm, group, hits_by_slot):
        spec = load_prompts()["groups"][group]
        out = []
        for i, roles in enumerate(hits_by_slot):
            out.append({"arm": arm, "group": group, "prompt_index": i % 3, "rep": i // 3 + 1, "valid": True,
                        "roles": roles, "first_role": roles[0] if roles else None, "attempt": 1})
        return out

    sup, stk, mst = ["supporter"], ["stakeholder"], ["scrum-master"]
    # A: six of nine pass, five of nine is a near miss; a second attempt of a slot never counts twice
    cand_a = trials("candidate", "A", [sup] * 6 + [stk, mst, []])
    base_a = trials("baseline", "A", [stk] * 9)
    cells = cell_counts(cand_a + base_a)
    checks, near = evaluate(cells, {"A": 9})
    expect("A six of nine passes, and one stakeholder in A is within the mixing line", [c[2] for c in checks if c[0] == "A"], [True, True])
    cand_a5 = trials("candidate", "A", [sup] * 5 + [mst] * 4)
    checks, near = evaluate(cell_counts(cand_a5 + base_a), {"A": 9})
    expect("A five of nine fails and is a near miss", ([c[2] for c in checks if "supporter >=" in c[1]], near), ([False], ["A"]))
    # B: not below the baseline
    base_b = trials("baseline", "B", [stk] * 7 + [mst, []])
    cand_b = trials("candidate", "B", [stk] * 7 + [sup, []])
    checks, near = evaluate(cell_counts(base_b + cand_b), {"B": 9})
    expect("B equal passes; one supporter in B is within the mixing line", [c[2] for c in checks], [True, True])
    cand_b6 = trials("candidate", "B", [stk] * 6 + [sup, sup, []])
    checks, near = evaluate(cell_counts(base_b + cand_b6), {"B": 9})
    expect("B one below baseline fails, is a near miss, and two supporters break the mixing line",
           ([c[2] for c in checks], near), ([False, False], ["B"]))
    # incomplete cells are not judged as passes
    checks, near = evaluate(cell_counts(base_b + cand_b[:8]), {"B": 9})
    expect("a missing valid trial is incomplete", [(c[1], c[2]) for c in checks], [("complete", False)])
    # a technical failure slot is replaced by its valid second attempt, and counted once
    failed = dict(cand_b[0], valid=False, attempt=1)
    retried = dict(cand_b[0], attempt=2)
    cells = cell_counts(base_b + [failed, retried] + cand_b[1:])
    expect("retry of a technical failure counts once", cells[("candidate", "B")]["n"], 9)
    print(json.dumps({"selftest": "ok" if not failures else "FAILED", "failures": failures}, ensure_ascii=False, indent=1))
    return 0 if not failures else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    for flag in ("selftest", "probe", "smoke", "run"):
        mode.add_argument("--" + flag, action="store_true")
    mode.add_argument("--judge", metavar="DIR")
    ap.add_argument("--baseline", default="1145382")
    ap.add_argument("--candidate", default="HEAD")
    ap.add_argument("--groups", default="A,B,C")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--rep-start", type=int, default=1)
    ap.add_argument("--round", type=int, default=1)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--max-minutes", type=float, default=150)
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.selftest:
        return cmd_selftest(a)
    if a.judge:
        a.dir = a.judge
        return cmd_judge(a)
    if a.probe:
        return cmd_probe(a)
    if a.smoke:
        return cmd_smoke(a)
    return cmd_run(a)


if __name__ == "__main__":
    sys.exit(main())
