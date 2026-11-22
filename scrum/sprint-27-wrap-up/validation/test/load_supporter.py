"""Sprint 27 Test, item 2 (the "加载" line of chapter 2.2): headless Claude Code, `/ideo-scrum:supporter`, three sessions.

The pass line, as frozen in 2.2: in each session the kernels the model loads through the Skill tool are ideo-kernel and
then scrum-kernel, and sprint-kernel and design-kernel are never loaded; 3 of 3 sessions pass. A session is one headless
magpie run with read-only tools, built like a trial of the trigger test: run_trigger.py is imported, not copied, so the
tool restrictions, the allow-list environment, the fresh home and the stream reading are the same. The three chores are
the first three prompts of group A of the frozen trigger prompts; each is typed after the command. Raw output goes outside
the repository.

  python -X utf8 -I load_supporter.py --selftest
  python -X utf8 -I load_supporter.py --smoke [--rev REV]       the isolation probe and one session; not counted
  python -X utf8 -I load_supporter.py --run   [--rev REV] [--min-free-gb 2.3]
  python -X utf8 -I load_supporter.py --judge DIR

The sessions run one after another. Before each one the free physical memory is read; below --min-free-gb nothing more
starts and the exit code is 3. A technical failure (no init, no result, timeout, execution error; error_max_turns is
valid) is retried, at most twice per slot; the first valid attempt counts.
"""
import argparse
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("run_trigger", HERE.parent / "trigger" / "run_trigger.py")
rt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rt)

PUBLIC = pathlib.Path(r"C:\Users\Public\s27-load")
ARCHIVE = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-27-wrap-up\load")
COMMAND = "/ideo-scrum:supporter"
WANTED = ["ideo-kernel", "scrum-kernel"]
FORBIDDEN = ("sprint-kernel", "design-kernel")
SLOTS = 3


# ---------------------------------------------------------------- the judge (no model, no files)

def judge_load(skills):
    """skills: the names of the Skill calls of one session, in order. Pass: the kernels loaded are ideo-kernel then
    scrum-kernel, and neither sprint-kernel nor design-kernel appears. A call to the supporter skill itself is only
    noted: typed as a command, it should be expanded by the host and not be a Skill call."""
    names = [s[len(rt.PREFIX):] if s.startswith(rt.PREFIX) else s for s in skills]
    kernels = [n for n in names if n.endswith("-kernel")]
    forbidden = [k for k in kernels if k in FORBIDDEN]
    return {"pass": kernels[:2] == WANTED and not forbidden, "kernels": kernels, "forbidden": forbidden,
            "supporter_called": "supporter" in names}


def enough_memory(free_gb, minimum_gb):
    return free_gb >= minimum_gb


def free_gb():
    """Free physical memory in GiB (Windows reports kilobytes)."""
    out = subprocess.run(["powershell", "-NoProfile", "-Command", "(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory"],
                         capture_output=True, text=True, timeout=60).stdout.strip()
    return int(out) / 1024 / 1024


# ---------------------------------------------------------------- the host side

def chores():
    return rt.load_prompts()["groups"]["A"]["prompts"][:SLOTS]


def init_restricted(rec):
    return (rec["permission_mode"] == "dontAsk" and rec["tools"] is not None
            and not {"Bash", "PowerShell", "Write", "Edit"} & set(rec["tools"] or []))


def one_session(root, plugin, slot, attempt):
    rec = rt.run_trial(root, "candidate", plugin, "L", slot, COMMAND + " " + chores()[slot], 1, attempt)
    rec.update(judge_load(rec["skills"]), init_restricted=init_restricted(rec))
    return rec


def line(rec):
    return "slot %d a%d valid=%s pass=%s kernels=%s supporter_called=%s result=%s denials=%s restricted=%s %ss" % (
        rec["prompt_index"] + 1, rec["attempt"], rec["valid"], rec["pass"], rec["kernels"], rec["supporter_called"],
        rec["result_subtype"], rec["denials"], rec["init_restricted"], rec["elapsed_s"])


def cmd_smoke(args):
    root = PUBLIC / ("smoke-" + rt.stamp())
    plugin = rt.extract_arm(args.rev, root / "arms" / "candidate")
    print("rev", rt.rev_id(args.rev), "free GiB %.2f" % free_gb())
    print("isolation probe:", json.dumps(rt.probe(plugin, root), ensure_ascii=False))
    if not enough_memory(free_gb(), args.min_free_gb):
        print("stop: free memory below %.1f GiB" % args.min_free_gb)
        return 3
    rec = one_session(root, plugin, 0, 1)
    print(line(rec), "| skills:", rec["skills"], "| model set:", bool(rec["model"]))
    shutil.rmtree(root, ignore_errors=True)
    return 0 if rec["valid"] and rec["init_restricted"] else 1


def cmd_run(args):
    root = PUBLIC / ("run-" + rt.stamp())
    out = ARCHIVE / rt.stamp()
    out.mkdir(parents=True, exist_ok=True)
    plugin = rt.extract_arm(args.rev, root / "arms" / "candidate")
    meta = {"rev": rt.rev_id(args.rev), "plugin_tree": subprocess.run(["git", "-C", str(rt.REPO), "rev-parse", args.rev + ":plugins/ideo-scrum"],
                                                                      capture_output=True, text=True).stdout.strip(),
            "command": COMMAND, "slots": SLOTS, "min_free_gb": args.min_free_gb,
            "model_note": "magpie's cheap model (not Haiku): --model haiku is remapped by the wrapper"}
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    results = out / "results.jsonl"
    stopped = False
    for slot in range(SLOTS):
        for attempt in range(1, 4):
            free = free_gb()
            if not enough_memory(free, args.min_free_gb):
                print("stop before slot %d attempt %d: free memory %.2f GiB is below %.1f GiB" % (slot + 1, attempt, free, args.min_free_gb), flush=True)
                stopped = True
                break
            print("free %.2f GiB; starting slot %d attempt %d" % (free, slot + 1, attempt), flush=True)
            rec = one_session(root, plugin, slot, attempt)
            rec["free_gb_before"] = round(free, 2)
            with results.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(line(rec), flush=True)
            if rec["valid"]:
                break
        if stopped:
            break
    raw = out / "raw"
    raw.mkdir(exist_ok=True)
    for d in (root / "trials").glob("*"):
        for name in ("session.jsonl", "stderr.log"):
            if (d / name).is_file():
                shutil.copy2(d / name, raw / ("%s.%s" % (d.name, name)))
    shutil.rmtree(root, ignore_errors=True)
    print("written", out)
    if stopped:
        return 3
    return cmd_judge(argparse.Namespace(dir=str(out)))


def cmd_judge(args):
    out = pathlib.Path(args.dir)
    trials = [json.loads(x) for x in (out / "results.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    taken, counted = set(), []
    for t in trials:
        if t["valid"] and t["prompt_index"] not in taken:
            taken.add(t["prompt_index"])
            counted.append(t)
    for t in counted:
        print("slot %d: %s  kernels=%s  supporter_called=%s  result=%s  denials=%s  restricted=%s" % (
            t["prompt_index"] + 1, "PASS" if t["pass"] else "FAIL", t["kernels"], t["supporter_called"], t["result_subtype"],
            t["denials"], t["init_restricted"]))
    technical = [t for t in trials if not t["valid"]]
    print("technical failures:", len(technical), [(t["trial"], t["why_invalid"]) for t in technical])
    ok = len(counted) == SLOTS and all(t["pass"] for t in counted)
    print("%s  %d of %d sessions loaded ideo-kernel then scrum-kernel, and neither sprint-kernel nor design-kernel" % (
        "PASS" if ok else "FAIL", sum(t["pass"] for t in counted), SLOTS))
    return 0 if ok else 1


def cmd_selftest(args):
    failures = []

    def expect(label, got, want):
        if got != want:
            failures.append("%s: got %r, want %r" % (label, got, want))

    p = "ideo-scrum:"
    expect("ideo then scrum passes", judge_load([p + "ideo-kernel", p + "scrum-kernel"])["pass"], True)
    expect("scrum before ideo fails", judge_load([p + "scrum-kernel", p + "ideo-kernel"])["pass"], False)
    expect("only ideo fails", judge_load([p + "ideo-kernel"])["pass"], False)
    expect("nothing loaded fails", judge_load([])["pass"], False)
    expect("a third kernel that is the sprint kernel fails", judge_load([p + "ideo-kernel", p + "scrum-kernel", p + "sprint-kernel"])["pass"], False)
    expect("a design kernel anywhere fails", judge_load([p + "ideo-kernel", p + "design-kernel", p + "scrum-kernel"])["pass"], False)
    expect("a second call of the same kernel is harmless", judge_load([p + "ideo-kernel", p + "scrum-kernel", p + "ideo-kernel"])["pass"], True)
    expect("names without the prefix count (DSH style)", judge_load(["ideo-kernel", "scrum-kernel"])["pass"], True)
    r = judge_load([p + "supporter", p + "ideo-kernel", p + "scrum-kernel"])
    expect("a call to the supporter skill is noted, not failed", (r["pass"], r["supporter_called"]), (True, True))
    expect("a skill that only contains a kernel name is not a kernel", judge_load([p + "ideo-kernel-notes", p + "scrum-kernel"])["pass"], False)
    expect("enough memory", (enough_memory(3.1, 2.3), enough_memory(2.3, 2.3), enough_memory(2.29, 2.3)), (True, True, False))
    # the imported stream reader keeps what the judge needs, in call order
    rows = [{"type": "system", "subtype": "init", "tools": ["Read", "Skill"], "permissionMode": "dontAsk", "model": "m"},
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Skill", "input": {"skill": p + "ideo-kernel"}}]}},
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Skill", "input": {"skill": p + "scrum-kernel"}}]}},
            {"type": "result", "subtype": "error_max_turns", "is_error": True, "permission_denials": [], "total_cost_usd": 0.01}]
    rec = rt.judge_stream([json.dumps(x) for x in rows])
    expect("the stream reader keeps the call order", rec["skills"], [p + "ideo-kernel", p + "scrum-kernel"])
    expect("max turns is a valid session", rec["valid"], True)
    expect("the restriction check reads the init", init_restricted(dict(rec)), True)
    expect("a session with Bash is not restricted", init_restricted({"permission_mode": "dontAsk", "tools": ["Read", "Bash"]}), False)
    expect("three chores exist", len(chores()), SLOTS)
    print(json.dumps({"selftest": "ok" if not failures else "FAILED", "failures": failures}, ensure_ascii=False, indent=1))
    return 0 if not failures else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    for flag in ("selftest", "smoke", "run"):
        mode.add_argument("--" + flag, action="store_true")
    mode.add_argument("--judge", metavar="DIR")
    ap.add_argument("--rev", default="HEAD")
    ap.add_argument("--min-free-gb", type=float, default=2.3)
    a = ap.parse_args()
    if a.selftest:
        return cmd_selftest(a)
    if a.judge:
        a.dir = a.judge
        return cmd_judge(a)
    return cmd_smoke(a) if a.smoke else cmd_run(a)


if __name__ == "__main__":
    sys.exit(main())
