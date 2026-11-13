"""Direct-run tests for plugins/ideo-scrum/hooks/commitments.sh (Sprint 19, block 4; PBI-61 acceptance 1-4).

Builds small sample projects in a temp directory, feeds the hook the JSON a real hook gets on stdin, and
compares what it prints with the exact expected text. No Claude Code session is started.

usage:  python -X utf8 -I hook_cases.py [--runner local|wsl] [--distro Ubuntu-24.04] [--hook PATH]

`local` runs `sh <hook>` with the sh found on PATH (Git Bash's sh on Windows). `wsl` runs it under the
distro's own /bin/sh (dash on Ubuntu) to stand in for Linux. Exit code 0 only if every case passes and the
comparer's self-test catches deliberately wrong output.
"""
import argparse
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[3]
HOOK_DEFAULT = REPO / "plugins/ideo-scrum/hooks/commitments.sh"

# ---- sample logs (the same sentences as the frequency test's fixture) --------------------------------
ZH = dict(
    product="ExportKit：把订单导出成 CSV 文件的小工具。",
    goal="导出又快又稳：一万行订单一分钟内导完，出错能从断点接着导。",
    sprint="导出先稳：失败的行单独记下来，不拖垮整批；PO 看一眼错误清单就知道哪几行要补。",
    sprint_v2="导出先快：先做按列选择，只导 PO 勾选的列；本冲刺不碰错误清单。",
    design="先弄清 PO 怎么检查失败的行。",
)
EN = dict(
    product="ExportKit: a small tool that exports orders to CSV files.",
    goal="Fast and steady: ten thousand orders in a minute, and a failed export resumes where it stopped.",
    sprint="Steady first: failed rows are recorded apart and never sink the batch.",
    design="Find out how the PO checks the failed rows.",
)


def product_log(t, key, h11="1.1 Product", h12="1.2 Product Goal"):
    return (f"# Product\n\n## {h11}\n\n| {key} | {t['product']} |\n| --- | --- |\n\n"
            f"## {h12}\n\n| {key} | {t['goal']} |\n| --- | --- |\n\n## 1.3 Definition of Done\n\n"
            "| 维度 | 标准 |\n| --- | --- |\n| 无死链 | 链接都能打开 |\n")


def sprint_log(text, key, name="01 (batch-export)"):
    return (f"# Sprint Backlog — Sprint {name}\n\n> Started: 2026-11-13 | Branch: x\n> Now: Increment\n"
            f"> Waiting for PO: None\n\n## 1. Why\n\n### 1.1 Sprint Goal\n\n| {key} | {text} |\n| --- | --- |\n\n"
            "### 1.2 Definition of Done\n\n- done\n")


def design_log(text, key, heading):
    return (f"# Design Backlog — export\n\n> Now: Empathize\n> Waiting for PO: None\n\n## 1. Empathize\n\n"
            f"### 1.1 Challenge\n\nx\n\n### {heading}\n\n| {key} | {text} |\n| --- | --- |\n")


def write(path, text, crlf=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))


def project(root, t, key, sprints=(), designs=(), crlf=False, product=True):
    """sprints: [(folder, text)]; designs: [(folder, text, heading)]."""
    if product:
        write(root / "scrum/ProductBacklog.md", product_log(t, key), crlf)
    for folder, text in sprints:
        write(root / "scrum" / folder / "SprintBacklog.md", sprint_log(text, key), crlf)
    for folder, text, heading in designs:
        write(root / "scrum" / folder / "DesignBacklog.md", design_log(text, key, heading), crlf)
    write(root / "src/export.py", "def write_csv(rows):\n    pass\n")
    return root


# ---- expected output ---------------------------------------------------------------------------------
def expect_zh(*lines):
    return "\n".join(("本项目日志里的承诺（原文）：",) + lines) + "\n"


def expect_en(*lines):
    return "\n".join(("Commitments from this project's logs (verbatim):",) + lines) + "\n"


ZH_THREE = expect_zh(f"Product：{ZH['product']}", f"Product Goal：{ZH['goal']}",
                     f"Sprint Goal（sprint-01-batch-export）：{ZH['sprint']}")


# ---- runner ------------------------------------------------------------------------------------------
class Runner:
    def __init__(self, kind, distro, hook, awk=None):
        self.kind, self.distro, self.hook = kind, distro, pathlib.Path(hook)
        self.sh = shutil.which("sh") or "sh"
        self.path_prefix = ""
        if kind == "wsl" and awk:
            # Make `awk` resolve to another implementation (mawk, nawk ...) for the whole run.
            d = f"/tmp/hookcases-awk-{awk}"
            subprocess.run(["wsl.exe", "-d", distro, "--", "sh", "-c", f"mkdir -p {d} && ln -sf $(command -v {awk}) {d}/awk"],
                           capture_output=True)
            self.path_prefix = d + ":"

    def native(self, p):
        """A path as the shell under test sees it."""
        p = pathlib.Path(p)
        if self.kind == "wsl":
            s = str(p.resolve())
            return "/mnt/" + s[0].lower() + s[2:].replace("\\", "/")
        return str(p)

    def run(self, event, cwd, env_extra=None, project_dir=None, raw_stdin=None, path_override=None):
        env = {k: v for k, v in os.environ.items() if not k.startswith(("IDEO_SCRUM_", "CLAUDE_")) and k != "PWD"}
        env.update(env_extra or {})
        if project_dir is not None:
            env["CLAUDE_PROJECT_DIR"] = project_dir
        data = raw_stdin if raw_stdin is not None else json.dumps(event, ensure_ascii=False)
        if self.kind == "wsl":
            env_args = [f"{k}={v}" for k, v in env.items() if k.startswith(("IDEO_SCRUM_", "CLAUDE_"))]
            cmd = ["wsl.exe", "-d", self.distro, "--cd", self.native(cwd), "--", "env", "-i",
                   f"PATH={self.path_prefix}/usr/local/bin:/usr/bin:/bin"] + env_args + ["sh", self.native(self.hook)]
            run_env = None
        else:
            if path_override is not None:
                env["PATH"] = path_override
            cmd = [self.sh, str(self.hook)]
            run_env = env
        p = subprocess.run(cmd, input=data.encode("utf-8"), cwd=str(cwd), env=run_env, capture_output=True)
        return p.stdout.decode("utf-8", "replace").replace("\r\n", "\n"), p.returncode


def ev(name, session="s1", source=None, prompt=None, cwd="/x"):
    d = {"session_id": session, "transcript_path": "/t.jsonl", "cwd": cwd, "hook_event_name": name}
    if source:
        d["source"] = source
    if prompt is not None:
        d["permission_mode"] = "default"
        d["prompt"] = prompt
    return d


# ---- the comparer, with a self-test --------------------------------------------------------------------
def same(expected, actual):
    return expected == actual


def comparer_self_test():
    good = same(ZH_THREE, ZH_THREE)
    caught = [not same(ZH_THREE, ZH_THREE.replace("导出先稳", "导出先快")),
              not same(ZH_THREE, ZH_THREE.rstrip("\n")),
              not same(ZH_THREE, ""),
              not same("", ZH_THREE)]
    return good and all(caught)


# ---- cases ---------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runner", default="local", choices=["local", "wsl"])
    ap.add_argument("--distro", default="Ubuntu-24.04")
    ap.add_argument("--hook", default=str(HOOK_DEFAULT))
    ap.add_argument("--wsl-awk", default=None, help="with --runner wsl: run with this awk (mawk, nawk ...) as `awk`")
    a = ap.parse_args()
    R = Runner(a.runner, a.distro, a.hook, a.wsl_awk)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="hookcases-"))
    results = []

    def check(name, ok, detail=""):
        results.append((name, bool(ok), detail))

    def case(name, expected, actual_rc, want_rc=0):
        actual, rc = actual_rc
        check(name, rc == want_rc and same(expected, actual),
              "" if rc == want_rc and same(expected, actual) else f"rc={rc} got={actual!r} want={expected!r}")

    def sd(n):
        d = tmp / f"state-{n}"
        d.mkdir(exist_ok=True)
        return str(R.native(d)) if a.runner == "wsl" else str(d)

    start = ev("SessionStart", source="startup")

    # 61-1: one open Sprint -> the three commitments, word for word
    p = project(tmp / "p1", ZH, "承诺", sprints=[("sprint-01-batch-export", ZH["sprint"])])
    case("61-1 one sprint, Chinese log", ZH_THREE, R.run(start, p))
    p = project(tmp / "p1en", EN, "Commitment", sprints=[("sprint-01-batch-export", EN["sprint"])])
    case("61-1 one sprint, English log", expect_en(f"Product: {EN['product']}", f"Product Goal: {EN['goal']}",
                                                  f"Sprint Goal (sprint-01-batch-export): {EN['sprint']}"),
         R.run(start, p))
    case("61-1 the same on UserPromptSubmit in `every` mode", ZH_THREE,
         R.run(ev("UserPromptSubmit", prompt="hi"), tmp / "p1", {"IDEO_SCRUM_COMMITMENTS_MODE": "every",
                                                                "CLAUDE_PLUGIN_DATA": sd("a")}))
    # reading rules
    p = project(tmp / "p1crlf", ZH, "承诺", sprints=[("sprint-01-batch-export", ZH["sprint"])], crlf=True)
    case("CRLF logs give the same text", ZH_THREE, R.run(start, p))
    case("run from a subdirectory", ZH_THREE, R.run(start, tmp / "p1/src"))
    other = tmp / "elsewhere"
    other.mkdir()
    pd = str(tmp / "p1") if a.runner == "local" else R.native(tmp / "p1")
    case("fall back to CLAUDE_PROJECT_DIR", ZH_THREE, R.run(start, other, project_dir=pd))
    if a.runner == "local" and os.name == "nt":
        case("CLAUDE_PROJECT_DIR with backslashes (PowerShell fallback)", ZH_THREE,
             R.run(start, other, project_dir=str(tmp / "p1").replace("/", "\\")))

    # 61-2: two open Sprints -> only the product statements and a count
    p = project(tmp / "p2", ZH, "承诺", sprints=[("sprint-01-batch-export", ZH["sprint"]),
                                                 ("sprint-02-other", ZH["sprint_v2"])])
    case("61-2 two sprints: count, no Sprint Goal",
         expect_zh(f"Product：{ZH['product']}", f"Product Goal：{ZH['goal']}", "有 2 个冲刺开着，见看板"),
         R.run(start, p))
    p = project(tmp / "p2en", EN, "Commitment", sprints=[("sprint-01-a", EN["sprint"]), ("sprint-02-b", EN["sprint"])])
    case("61-2 two sprints, English",
         expect_en(f"Product: {EN['product']}", f"Product Goal: {EN['goal']}", "2 Sprints are open; see the board"),
         R.run(start, p))

    # designs
    p = project(tmp / "p3", ZH, "承诺", sprints=[("sprint-01-batch-export", ZH["sprint"])],
                designs=[("design-export", ZH["design"], "1.2 设计目标")])
    case("a Sprint and a design: four lines",
         ZH_THREE + f"设计目标（design-export）：{ZH['design']}\n", R.run(start, p))
    p = project(tmp / "p3en", EN, "Commitment", designs=[("design-export", EN["design"], "1.2 Design goal")])
    case("English design goal", expect_en(f"Product: {EN['product']}", f"Product Goal: {EN['goal']}",
                                         f"Design goal (design-export): {EN['design']}"), R.run(start, p))
    p = project(tmp / "p3two", ZH, "承诺", designs=[("design-a", ZH["design"], "1.2 设计目标"),
                                                    ("design-b", ZH["design"], "1.2 设计目标")])
    case("two designs: count", expect_zh(f"Product：{ZH['product']}", f"Product Goal：{ZH['goal']}",
                                         "有 2 个设计开着，见看板"), R.run(start, p))

    # no Sprint open -> only the product statements
    p = project(tmp / "p4", ZH, "承诺")
    case("no Sprint open", expect_zh(f"Product：{ZH['product']}", f"Product Goal：{ZH['goal']}"), R.run(start, p))

    # placeholders of an unfilled template are not injected
    p = tmp / "p5"
    write(p / "scrum/ProductBacklog.md", product_log(dict(ZH, product="<product statement>"), "Commitment"))
    write(p / "scrum/sprint-01-x/SprintBacklog.md", sprint_log("<Sprint Goal>", "Commitment"))
    case("template placeholders are skipped", expect_en(f"Product Goal: {ZH['goal']}"), R.run(start, p))

    # 61-3: nothing is injected, and the exit code is 0
    case("61-3 no product log", "", R.run(start, project(tmp / "p6", ZH, "承诺", product=False)))
    case("61-3 switch off", "", R.run(start, tmp / "p1", {"IDEO_SCRUM_COMMITMENTS": "off"}))
    case("61-3 garbage on stdin", "", R.run(None, tmp / "p1", raw_stdin="not json \x00 \x01"))
    case("61-3 empty stdin", "", R.run(None, tmp / "p1", raw_stdin=""))
    case("61-3 an event it does not handle", "", R.run(ev("Stop"), tmp / "p1"))
    write(tmp / "p7/scrum/ProductBacklog.md", "\x00\x01\x02 binary \xff| 承诺 |\n")
    case("61-3 a product log that is not a log", "", R.run(start, tmp / "p7"))
    if a.runner == "local":
        sh_dir = tmp / "emptybin"
        sh_dir.mkdir(exist_ok=True)
        case("61-3 tools missing (empty PATH)", "", R.run(start, tmp / "p1", path_override=str(sh_dir)))

    # frequency modes (test-only): SessionStart, six prompts, the goal changes after prompt 3, then a compact
    def sequence(mode):
        pr = project(tmp / f"m-{mode}", ZH, "承诺", sprints=[("sprint-01-batch-export", ZH["sprint"])])
        env = {"IDEO_SCRUM_COMMITMENTS_MODE": mode, "CLAUDE_PLUGIN_DATA": sd(mode)}
        got = []
        out, _ = R.run(ev("SessionStart", session="seq", source="startup"), pr, env)
        got.append(bool(out))
        for i in range(1, 7):
            if i == 4:
                f = pr / "scrum/sprint-01-batch-export/SprintBacklog.md"
                f.write_text(f.read_text(encoding="utf-8").replace(ZH["sprint"], ZH["sprint_v2"]), encoding="utf-8")
            out, _ = R.run(ev("UserPromptSubmit", session="seq", prompt=f"p{i}"), pr, env)
            got.append(bool(out))
        out, _ = R.run(ev("SessionStart", session="seq", source="compact"), pr, env)
        got.append(bool(out))
        out, _ = R.run(ev("UserPromptSubmit", session="seq", prompt="p7"), pr, env)
        got.append(bool(out))
        return got

    T, F = True, False
    want = {
        "start":   [T, F, F, F, F, F, F, T, F],
        "every":   [T, T, T, T, T, T, T, T, T],
        "every-n": [T, F, F, F, F, T, F, T, F],
        "changed": [T, F, F, F, T, F, F, T, F],
    }
    for mode, w in want.items():
        got = sequence(mode)
        check(f"mode {mode}: injections per event", got == w, "" if got == w else f"got={got} want={w}")

    # a state directory that cannot be created: `changed` fails open, nothing crashes
    blocker = tmp / "blocker"
    blocker.write_text("a file, not a directory")
    out, rc = R.run(ev("UserPromptSubmit", session="x", prompt="p"), tmp / "p1",
                    {"IDEO_SCRUM_COMMITMENTS_MODE": "changed", "CLAUDE_PLUGIN_DATA": R.native(blocker / "sub")})
    check("unwritable state directory: no crash, exit 0", rc == 0, f"rc={rc}")

    # the real log of this repository: each injected sentence is a cell of a log
    out, rc = R.run(start, REPO)
    real = {}
    for line in out.splitlines()[1:]:
        label, _, text = line.partition("：")
        real[label] = text
    sources = []
    for f in [REPO / "scrum/ProductBacklog.md"] + sorted((REPO / "scrum").glob("sprint-*/SprintBacklog.md")):
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.startswith("| 承诺 |"):
                sources.append(l[len("| 承诺 |"):].rstrip(" |").strip())
    ok = rc == 0 and out.startswith("本项目日志里的承诺（原文）：") and len(real) >= 3 \
        and all(any(t == s for s in sources) for k, t in real.items() if k in ("Product", "Product Goal")) \
        and any(k.startswith("Sprint Goal（") for k in real)
    check("this repository's real logs", ok, f"rc={rc} out={out[:300]!r}")

    shutil.rmtree(tmp, ignore_errors=True)
    check("comparer self-test (wrong output is caught)", comparer_self_test())

    width = max(len(n) for n, _, _ in results)
    for n, ok, d in results:
        print(f"{'PASS' if ok else 'FAIL'}  {n.ljust(width)}  {d}")
    bad = [n for n, ok, _ in results if not ok]
    print(f"\n{len(results) - len(bad)}/{len(results)} passed, runner={a.runner}" + (f", awk={a.wsl_awk}" if a.wsl_awk else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
