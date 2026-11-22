"""Sprint 26: run one prompt in a fresh headless session outside the main session (PO 2026-11-22: no subagents inside the session).

    python -X utf8 -I scripts/run_prompt.py PROMPT.txt --out DIR [--name NAME] [--plugin-dir PATH ...] [--timeout 900] [--model haiku]

The prompt file is fed on stdin to `claude-magpie -p` in a neutral project folder (no instruction file above it), with a
throwaway home and a whitelist environment (the helpers of scripts/stranger_test/driver.py, as run_workflow.py does).
Each --plugin-dir is passed through (the plugin under test, or a helper plugin such as plugin-dev for its agents).
magpie maps every model name to its own cheap model, so what runs is "magpie's cheap model, not Haiku".

Writes DIR/<name>.stream.jsonl, DIR/<name>.summary.json (the init event's mode and tools, the Agent/Task calls the
session made with their subagent_type and model, the result event with the permission denials counted) and
DIR/<name>.result.md (the final text). The run is killed, process tree and all, when --timeout seconds pass.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import tempfile
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]
sys.path.insert(0, str(REPO / "scripts" / "stranger_test"))
import driver  # noqa: E402  (make_env, magpie_prefix, neutral_parent, kill_tree, rmtree)


def summarize(stream: pathlib.Path) -> dict:
    """What the stream says: the init event, the subagent launches, the result. Reads evidence, judges nothing."""
    info: dict = {"events": 0, "init": None, "launches": [], "tool_counts": {}, "result": None}
    for line in stream.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        info["events"] += 1
        if d.get("type") == "system" and d.get("subtype") == "init":
            info["init"] = {"permissionMode": d.get("permissionMode"), "model": d.get("model"), "tools": d.get("tools"),
                            "plugins": d.get("plugins"), "agents": d.get("agents")}
        if d.get("type") == "assistant":
            for block in (d.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "tool_use":
                    name = block.get("name")
                    info["tool_counts"][name] = info["tool_counts"].get(name, 0) + 1
                    if name in ("Agent", "Task"):
                        inp = block.get("input") or {}
                        info["launches"].append({"subagent_type": inp.get("subagent_type"), "model": inp.get("model"),
                                                 "description": inp.get("description")})
        if d.get("type") == "result":
            info["result"] = {"is_error": d.get("is_error"), "subtype": d.get("subtype"), "num_turns": d.get("num_turns"),
                              "duration_ms": d.get("duration_ms"), "permission_denials": len(d.get("permission_denials") or []),
                              "text": d.get("result")}
    return info


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", default="run")
    ap.add_argument("--plugin-dir", action="append", default=[])
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--permission-mode", default="bypassPermissions")
    ap.add_argument("--disallow", default="Write,Edit,NotebookEdit")
    a = ap.parse_args(argv)

    prompt = pathlib.Path(a.prompt).resolve().read_bytes()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    stream, err = out / f"{a.name}.stream.jsonl", out / f"{a.name}.stderr"
    root = pathlib.Path(tempfile.mkdtemp(prefix="s26-run-", dir=driver.neutral_parent()))
    status = "?"
    t0 = time.time()
    try:
        env, _home = driver.make_env(root / "env")
        env["CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"] = "0"
        proj = root / "project"
        proj.mkdir()
        cmd = driver.magpie_prefix() + ["-p", "--output-format", "stream-json", "--verbose", "--model", a.model,
                                        "--permission-mode", a.permission_mode, "--disallowedTools", a.disallow,
                                        "--setting-sources", "user,project,local"]
        for d in a.plugin_dir:
            cmd += ["--plugin-dir", d]
        with open(stream, "wb") as so, open(err, "wb") as se:
            p = subprocess.Popen(cmd, cwd=str(proj), env=env, stdin=subprocess.PIPE, stdout=so, stderr=se)
            p.stdin.write(prompt)
            p.stdin.close()
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
    info.update({"name": a.name, "status": status, "seconds": round(time.time() - t0)})
    (out / f"{a.name}.summary.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    res = info["result"] or {}
    (out / f"{a.name}.result.md").write_text(res.get("text") or "", encoding="utf-8", newline="\n")
    print(f"{a.name}: {status} in {info['seconds']} s; {info['events']} events; launches={info['launches']}; "
          f"error={res.get('is_error')} turns={res.get('num_turns')} denials={res.get('permission_denials')}; "
          f"mode={(info['init'] or {}).get('permissionMode')}")
    print((res.get("text") or "")[:3000])
    return 0 if status == "exit 0" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
