"""Sprint 26: run a saved workflow script outside the main session (PO 2026-11-22: no subagents inside the session).

    python -X utf8 -I scripts/run_workflow.py SCRIPT.js --out DIR [--timeout 2700] [--model haiku]

SCRIPT.js starts with `export const meta = {name: '<name>', ...}`. It is copied to <project>/.claude/workflows/<name>.js
in a neutral project folder (no instruction file above it), and `claude-magpie -p "/<name>"` runs it in a fresh session
with a throwaway home and a whitelist environment (the helpers of scripts/stranger_test/driver.py). magpie maps every
model name to its own cheap model, so what runs is "magpie's cheap model, not Haiku".

A workflow script has no file access: its agents write their results as files (paths given in the script), and this
launcher only runs it and reports. Raw stream: DIR/<name>.stream.jsonl; the run is killed, process tree and all, when
--timeout seconds pass.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "scripts" / "stranger_test"))
import driver  # noqa: E402  (make_env, magpie_prefix, neutral_parent, kill_tree, rmtree)


def workflow_name(text: str) -> str:
    m = re.search(r"name:\s*['\"]([A-Za-z0-9_-]+)['\"]", text)
    if not m:
        sys.exit("no `name: '...'` in the script's meta")
    return m.group(1)


def summarize(stream: pathlib.Path) -> dict:
    """What the stream says at the end: the result event, the init event's mode and tools, counts of the workflow's
    own events. Reads evidence, judges nothing."""
    info: dict = {"events": 0, "result": None, "init": None, "kinds": {}}
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        info["events"] += 1
        key = f"{d.get('type')}/{d.get('subtype')}"
        info["kinds"][key] = info["kinds"].get(key, 0) + 1
        if d.get("type") == "system" and d.get("subtype") == "init":
            info["init"] = {"permissionMode": d.get("permissionMode"), "model": d.get("model"), "tools": d.get("tools"),
                            "slash_commands": [c for c in (d.get("slash_commands") or []) if "s26" in c or "sprint26" in c]}
        if d.get("type") == "result":
            info["result"] = {"is_error": d.get("is_error"), "subtype": d.get("subtype"), "num_turns": d.get("num_turns"),
                              "duration_ms": d.get("duration_ms"), "cost": d.get("total_cost_usd"),
                              "permission_denials": len(d.get("permission_denials") or []), "text": d.get("result")}
    return info


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script")
    ap.add_argument("--out", required=True)
    ap.add_argument("--timeout", type=int, default=2700)
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--permission-mode", default="bypassPermissions")
    a = ap.parse_args(argv)

    script = pathlib.Path(a.script).resolve()
    name = workflow_name(script.read_text(encoding="utf-8"))
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    stream, err = out / f"{name}.stream.jsonl", out / f"{name}.stderr"
    root = pathlib.Path(tempfile.mkdtemp(prefix="s26-wf-", dir=driver.neutral_parent()))
    status = "?"
    t0 = time.time()
    try:
        env, _home = driver.make_env(root / "env")
        proj = root / "project"
        (proj / ".claude" / "workflows").mkdir(parents=True)
        shutil.copy2(script, proj / ".claude" / "workflows" / f"{name}.js")
        # the first smoke run showed `permissionMode: default` with a throwaway config (magpie's bypass default did not
        # carry over), and the Workflow tool then stopped at "Review dynamic workflow before running": say it out loud
        cmd = driver.magpie_prefix() + ["-p", "--output-format", "stream-json", "--verbose", "--model", a.model,
                                        "--permission-mode", a.permission_mode,
                                        "--setting-sources", "user,project,local", f"/{name}"]
        with open(stream, "wb") as so, open(err, "wb") as se:
            p = subprocess.Popen(cmd, cwd=str(proj), env=env, stdin=subprocess.DEVNULL, stdout=so, stderr=se)
            while p.poll() is None and time.time() - t0 < a.timeout:
                time.sleep(2)
            if p.poll() is None:
                driver.kill_tree(p)
                status = "timeout"
            else:
                status = f"exit {p.returncode}"
    finally:
        driver.rmtree(root)
    info = summarize(stream)
    info.update({"workflow": name, "status": status, "seconds": round(time.time() - t0)})
    (out / f"{name}.summary.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    res = info["result"] or {}
    print(f"{name}: {status} in {info['seconds']} s; {info['events']} events; result error={res.get('is_error')} turns={res.get('num_turns')} "
          f"denials={res.get('permission_denials')}; mode={(info['init'] or {}).get('permissionMode')}")
    print((res.get("text") or "")[:1500])
    return 0 if status == "exit 0" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
