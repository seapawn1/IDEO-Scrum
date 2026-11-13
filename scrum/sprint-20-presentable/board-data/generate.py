"""Block 11: a cheap model writes the board for a clone of this repository, then the board is checked (68-4).

    python -X utf8 -I generate.py [--timeout SECONDS]

The clone holds what is committed, so commit first. The model gets one plain request and the conventions to follow;
it runs in the stranger test's throwaway home, with magpie's cheap model. The raw output goes to
S:\\IDEO-Scrum-Archives\\sprint-20-presentable\\board-gen\\<run>\\ (outside the repository); this script prints the summary.
"""
import argparse
import datetime
import json
import pathlib
import subprocess
import sys
import tempfile
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts" / "stranger_test"))
import driver  # noqa: E402

ARCHIVE = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-20-presentable\board-gen")
PROMPT = (
    "You are helping the Product Owner of this project. Write the project's Scrum board: read "
    "plugins/ideo-scrum/skills/scrum-kernel/conventions/board-log.md and follow it, using the template beside it, "
    "and write the page to scrum/ScrumBoard.html. Do not change any other file. When you are done, say in one or "
    "two sentences what you did."
)
TOOLS = "Bash,Read,Write,Edit,Glob,Grep"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=2400)
    args = ap.parse_args()
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = ARCHIVE / f"gen-{stamp}"
    out.mkdir(parents=True)
    base = pathlib.Path(tempfile.mkdtemp(prefix="st-"))
    try:
        env, _home = driver.make_env(base)
        proj = base / "proj"
        subprocess.run(["git", "clone", "-q", "--no-hardlinks", str(ROOT), str(proj)], env=env, check=True)
        head = subprocess.run(["git", "-C", str(proj), "rev-parse", "--short", "HEAD"], env=env, capture_output=True,
                              text=True).stdout.strip()
        cmd = driver.magpie_prefix() + ["-p", "--output-format", "stream-json", "--verbose", "--model", driver.MODEL,
                                         "--tools", TOOLS, "--permission-mode", "acceptEdits", "--allowedTools", "Bash",
                                         "--setting-sources", "project,local"]
        started = time.time()
        proc = subprocess.Popen(cmd, cwd=proj, env=env, stdin=subprocess.PIPE, stdout=open(out / "p.jsonl", "wb"),
                                stderr=open(out / "p.stderr", "wb"))
        try:
            proc.communicate(PROMPT.encode("utf-8"), timeout=args.timeout)
            timed_out = False
        except subprocess.TimeoutExpired:
            driver.kill_tree(proc)
            timed_out = True
        elapsed = round(time.time() - started)

        tools, result, turns = {}, {}, 0
        for line in (out / "p.jsonl").read_text(encoding="utf-8", errors="replace").split("\n"):
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if row.get("type") == "result":
                result = {k: row.get(k) for k in ("is_error", "duration_ms", "num_turns", "total_cost_usd", "result")}
            msg = row.get("message")
            if row.get("type") == "assistant" and isinstance(msg, dict):
                turns += 1
                for c in msg.get("content") or []:
                    if isinstance(c, dict) and c.get("type") == "tool_use":
                        tools[c["name"]] = tools.get(c["name"], 0) + 1
        status = subprocess.run(["git", "-C", str(proj), "status", "--porcelain"], env=env, capture_output=True,
                                text=True).stdout.strip().split("\n")
        page = proj / "scrum" / "ScrumBoard.html"
        check = {"ok": False, "errors": ["no page written"], "warnings": []}
        if page.is_file():
            (out / "ScrumBoard.html").write_bytes(page.read_bytes())
            r = subprocess.run([sys.executable, "-X", "utf8", "-I", str(ROOT / "scripts/board_check/check.py"), "check",
                                "--project", str(proj), "--page", str(page), "--render"], capture_output=True, text=True,
                               encoding="utf-8")
            try:
                check = json.loads(r.stdout)
            except ValueError:
                check = {"ok": False, "errors": ["the checker printed no JSON: " + (r.stderr or r.stdout)[-300:]], "warnings": []}
        summary = {"run": out.name, "commit": head, "seconds": elapsed, "timed_out": timed_out, "tools": tools,
                   "assistant_turns": turns, "result": result, "changed_files": [s for s in status if s],
                   "check": check}
        (out / "run.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
        print(json.dumps({k: v for k, v in summary.items() if k != "result"}, ensure_ascii=False, indent=1))
        print("result text:", str(result.get("result"))[:400])
        return 0 if check.get("ok") else 1
    finally:
        driver.rmtree(base)


if __name__ == "__main__":
    sys.exit(main())
