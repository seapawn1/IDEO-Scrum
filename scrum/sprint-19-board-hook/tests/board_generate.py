"""Block 9: have a cheap model write the board from the logs, then check the page (board_check.py).

Each run starts in a fresh copy of the sample project (or of this repository's current state), with no
`scrum/Board.html`, so every page is made from nothing: the page owns nothing, and a second run must hold the
same facts. The model gets the brief a Scrum Master would give a subagent, and the plugin from this branch.

usage (with `python -X utf8 -I`):
  board_generate.py fixture --out DIR [--scenario A|B] [--runs 3] [--parallel 3]
  board_generate.py real    --out DIR [--runs 2] [--parallel 2]

Raw streams and pages go to --out (outside the repository). The channel is the same as the frequency test's:
`claude-magpie.cmd -p`, a whitelist environment, a fresh empty TEMP and TMP for each run.
"""
import argparse
import concurrent.futures
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
PLUGIN = REPO / "plugins/ideo-scrum"
CHECK = HERE / "board_check.py"
EXE = "claude-magpie.cmd"
WHITELIST = {"systemroot", "path", "userprofile", "appdata", "localappdata", "homedrive", "homepath", "comspec",
             "pathext", "temp", "tmp", "claude_code_git_bash_path", "msys_no_pathconv"}

# The brief a Scrum Master would give a subagent: where the conventions are, and where to write; nothing else.
BRIEF = ("Make the project board for this repository. Load the ideo-scrum:scrum-kernel skill with the Skill tool, "
         "read conventions/board.md and conventions/board-template.html in that skill's folder, and follow them. "
         "Write the page to scrum/Board.html. Reply with one line when it is written.")

# Read-only git, plus the date; Write only reaches the temporary copy the run works in.
TOOLS = "Bash,Read,Grep,Glob,Write,Skill"
ALLOWED = ",".join(["Read", "Grep", "Glob", "Write", "Skill"] +
                   [f"Bash({c} *)" for c in ("git show", "git branch", "git for-each-ref", "git ls-tree", "git rev-parse",
                                            "git log", "git status", "git worktree list", "date", "ls", "cat")] +
                   [f"Bash({c}:*)" for c in ("git show", "git branch", "git for-each-ref", "git ls-tree", "git rev-parse",
                                            "git log", "git status", "git worktree list", "date", "ls", "cat")])


def clean_env():
    env = {k: v for k, v in os.environ.items() if k.lower() in WHITELIST}
    sh = shutil.which("sh")
    if sh:
        env["CLAUDE_CODE_GIT_BASH_PATH"] = str(pathlib.Path(sh).with_name("bash.exe"))
    env["MSYS_NO_PATHCONV"] = "1"
    for k in ("TEMP", "TMP"):
        env[k] = tempfile.mkdtemp(prefix="board-tmp-")
    return env


def git(cwd, *args):
    p = subprocess.run(["git", "-c", "core.autocrlf=false", "-c", "user.name=fixture", "-c", "user.email=f@example.com", *args],
                       cwd=str(cwd), capture_output=True)
    if p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.decode('utf-8', 'replace')}")
    return p.stdout.decode("utf-8", "replace")


def generate(work, stream_path, timeout=1200):
    # dontAsk: whatever the allowlist does not name is refused, instead of the channel's default bypassPermissions
    # (the first batch of runs showed the default does not enforce the allowlist).
    # --setting-sources project,local: the user's settings carry broad allow rules that made dontAsk and the
    # allowlist moot in the second batch of runs; without them the allowlist is what the model really has.
    cmd = [EXE, "-p", BRIEF, "--output-format", "stream-json", "--verbose", "--model", "haiku",
           "--tools", TOOLS, "--allowedTools", ALLOWED, "--permission-mode", "dontAsk",
           "--setting-sources", "project,local", "--plugin-dir", str(PLUGIN)]
    t0 = time.time()
    with open(stream_path, "wb") as out:
        try:
            p = subprocess.run(cmd, cwd=str(work), env=clean_env(), stdout=out, stderr=subprocess.PIPE, timeout=timeout)
            status = "ok" if p.returncode == 0 else f"exit {p.returncode}"
        except subprocess.TimeoutExpired:
            status = f"timeout after {timeout}s"
    return {"status": status, "seconds": round(time.time() - t0)}


def summary_of(stream_path):
    usage, tools, result, mode, denied = {}, {}, "", None, []
    for line in open(stream_path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") == "system" and d.get("subtype") == "init" and mode is None:
            mode = d.get("permissionMode")
        if d.get("type") == "result":
            u = d.get("usage") or {}
            usage = {k: u.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")}
            result = (d.get("result") or "")[:200]
            denied = [(x.get("tool_name"), str((x.get("tool_input") or {}).get("command") or "")[:60]) for x in d.get("permission_denials") or []]
        if d.get("type") == "assistant":
            for c in (d.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    tools[c.get("name")] = tools.get(c.get("name"), 0) + 1
    return {"usage": usage, "tools": tools, "result": result, "permission_mode": mode, "denied": denied}


def run_checks(work, page, scenario):
    r = subprocess.run([sys.executable, "-X", "utf8", "-I", str(CHECK), "check", "--repo", str(work), "--page", str(page),
                        "--scenario", scenario], capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def one(source, out, tag, scenario):
    work = pathlib.Path(tempfile.mkdtemp(prefix=f"board-{tag}-"))
    shutil.rmtree(work)
    shutil.copytree(source, work, symlinks=True)
    page = work / "scrum/Board.html"
    if page.exists():
        page.unlink()
    r = generate(work, out / f"{tag}.jsonl")
    r.update(summary_of(out / f"{tag}.jsonl"))
    r["page"] = page.is_file()
    if page.is_file():
        shutil.copy(page, out / f"{tag}.html")
        rc, text = run_checks(work, page, scenario)
        r["check_rc"], r["check"] = rc, text
        (out / f"{tag}.check.txt").write_text(text, encoding="utf-8")
    return tag, r


def real_copy(dest):
    """This repository's current state: main checked out, the two open Sprints as local branches."""
    git(dest.parent, "clone", "--quiet", "--no-hardlinks", str(REPO.parents[2]), str(dest))
    # every branch that still has an open Sprint folder (Sprint 18 was merged and closed after the first batches)
    for line in git(dest, "for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").splitlines():
        b = line.strip()[len("origin/"):]
        if b in ("HEAD", "main") or not b:
            continue
        tree = git(dest, "ls-tree", "--name-only", f"origin/{b}", "scrum/")
        if any(re.match(r"^scrum/(sprint|design|ideo)-", t) for t in tree.splitlines()):
            git(dest, "branch", b, f"origin/{b}")
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["fixture", "real"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--scenario", default="A")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--parallel", type=int, default=3)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    base = pathlib.Path(tempfile.mkdtemp(prefix="board-base-"))
    if a.cmd == "fixture":
        sys.path.insert(0, str(HERE))
        import importlib.util
        spec = importlib.util.spec_from_file_location("board_check", CHECK)
        bc = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bc)
        source = bc.build_fixture(base / "src", a.scenario)
        scenario = a.scenario
        prefix = f"fixture{a.scenario}"
    else:
        source = real_copy(base / "src")
        scenario = "real"
        prefix = "real"
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        futs = [ex.submit(one, source, out, f"{prefix}-{i}", scenario) for i in range(1, a.runs + 1)]
        for f in concurrent.futures.as_completed(futs):
            tag, r = f.result()
            results[tag] = r
            print(tag, json.dumps({k: v for k, v in r.items() if k != "check"}, ensure_ascii=False), flush=True)
            print("   ", r.get("check", "no page written").strip().splitlines()[-1] if r.get("check") else "no page written", flush=True)
    pages = sorted(out.glob(f"{prefix}-*.html"))
    if len(pages) >= 2:
        r = subprocess.run([sys.executable, "-X", "utf8", "-I", str(CHECK), "compare", *map(str, pages)], capture_output=True)
        print("compare:", r.stdout.decode("utf-8", "replace").strip()[:600])
    (out / f"{prefix}-summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    main()
