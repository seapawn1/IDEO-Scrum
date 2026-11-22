"""Sprint 26, work item 4: the carrier test. The standard is review/carrier-criteria.md (committed before any run).

How Memory gets into a role's context: A1 (a `memory` skill the role entry calls), A2 (appended to scrum-kernel),
B (a hook), C (A1 plus a hook that tops it up after compaction), N (no Memory, the control).

    python -X utf8 -I scripts/carrier_test.py selftest
    python -X utf8 -I scripts/carrier_test.py build  --out DIR            build the five plugin copies and show their sizes
    python -X utf8 -I scripts/carrier_test.py smoke  --out DIR            one session per carrier, only to calibrate how the evidence is read
    python -X utf8 -I scripts/carrier_test.py run    --out DIR --scenario role --n 3 --parallel 4
    python -X utf8 -I scripts/carrier_test.py timing --out DIR            the hook script, 20 runs each
    python -X utf8 -I scripts/carrier_test.py report --out DIR            the tables for the criteria

Raw output goes to --out, outside the repository. Sessions are claude-magpie stream-json sessions with a throwaway home
and a whitelist environment (the helpers of scripts/stranger_test/driver.py); evidence is read from the event stream,
never from what the model says about itself.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import os
import pathlib
import re
import secrets
import shutil
import statistics
import subprocess
import sys
import tempfile
import threading
import time

HERE = pathlib.Path(__file__).resolve().parent
SPRINT = HERE.parent
REPO = SPRINT.parents[1]
sys.path.insert(0, str(REPO / "scripts" / "stranger_test"))
import driver  # noqa: E402  (make_env, magpie_prefix, Session, neutral_parent, rmtree, probe_memory_files)

PLUGIN_SRC = REPO / "plugins" / "ideo-scrum"
LEDGER = SPRINT / "review" / "ledger.json"
CARRIERS = ["N", "A1", "A2", "B", "C"]
BUILD_ALSO = ["B2"]  # B plus a PreToolUse hook on Skill, built for the model-calls-a-role test only
ROLES = {"developer": "DEV", "scrum-master": "SM", "designer": "DES", "stakeholder": "STK"}
ROLE_TITLES = {"DEV": "Developer", "SM": "Scrum Master", "DES": "Designer", "STK": "Stakeholder"}
TOOLS = "Read,Grep,Glob,Skill,Agent"
TOOLS_NO_AGENT = "Read,Grep,Glob,Skill"
MODEL = "haiku"  # magpie maps any model name to its own cheap model
PROBE_SUFFIX = "-zq7"
TARGET_CHARS = 8000
LIMITS = {"message_s": 600, "session_s": 1500}  # the run limits: the one thing the smoke run may calibrate


# ---- the stand-in Memory ----------------------------------------------------------------------------------------
def new_canaries() -> dict:
    return {k: f"{k}-{secrets.token_hex(4)}" for k in ["MEMORY-START", "MEMORY-END", "ROLE-DEV", "ROLE-SM", "ROLE-DES", "ROLE-STK"]}


def snippets() -> list[str]:
    """One-line stand-ins taken word for word from the ledger: the rule's name and the start of its text."""
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    out = []
    for f in ledger["files"]:
        for r in f["rules"]:
            body = r["text"].split("—", 1)[-1].strip().replace("\n", " ")
            out.append(f"- {r['name']}: {body[:150].rstrip()}")
    return out


def memory_text(c: dict, roles: list[str] | None = None) -> str:
    """The stand-in: start canary, shared rules (3-5 real ones, the probe rule, filler of the same sort), one short
    section per role with its own canary, end canary. `roles` limits the role sections (a hook gives one)."""
    snip = snippets()
    shared = [
        "# Plugin Memory (stand-in for the carrier test)",
        c["MEMORY-START"],
        "",
        "## Shared rules",
        f"- Probe rule: when you name a new Sprint folder, always end the suffix with `{PROBE_SUFFIX}`.",
        snip[ [i for i, s in enumerate(snip) if s.startswith("- How is a plan")][0] ],
        snip[ [i for i, s in enumerate(snip) if s.startswith("- Go-ahead")][0] ],
        snip[ [i for i, s in enumerate(snip) if s.startswith("- Ask the Product Owner")][0] ],
        snip[ [i for i, s in enumerate(snip) if s.startswith("- No TBD")][0] ],
    ]
    i = 0
    role_block = ["", "## Roles"]
    for r in (roles or list(ROLE_TITLES)):
        role_block += [f"### {ROLE_TITLES[r]}", f"{c['ROLE-' + r]}: rules for the {ROLE_TITLES[r]} only; a {ROLE_TITLES[r]} session follows these in addition to the shared rules."]
    tail = ["", c["MEMORY-END"]]
    pool = [s for s in snip if not any(s in x for x in shared)]
    while len("\n".join(shared + role_block + tail)) < TARGET_CHARS and i < len(pool):
        shared.append(pool[i])
        i += 1
    return "\n".join(shared + role_block + tail) + "\n"


# ---- the plugin copies ------------------------------------------------------------------------------------------
HOOK_SH = r'''#!/bin/sh
# Sprint 26 carrier test: the Memory hook. Stand-in for the real one; the same shape as hooks/commitments.sh (pure sh).
#   expand   UserPromptExpansion: a role command was run; remember the role for this session, print that role's Memory
#   compact  SessionStart (compact): print the Memory again if this session had it
#   mark     PostToolUse (Skill): remember that this session loaded the memory skill
#   skill    PreToolUse (Skill): the model itself called a role as a skill; print that role's Memory (variant B2)
[ "$IDEO_SCRUM_MEMORY" = "off" ] && exit 0
mode=$1
part=$2   # a Memory over the host's 10,000-character limit is sent as several hooks, one part each: "expand 1", "expand 2"

# Copy $1 into __path with every backslash turned into a slash (the plugin root can be a Windows path).
to_slashes() {
  __path=$1
  while :; do
    case $__path in
      *\\*) __path=${__path%%\\*}/${__path#*\\} ;;
      *) break ;;
    esac
  done
}
to_slashes "$0"
here=${__path%/*}

strip_blanks() {
  while :; do
    case $v in
      [[:space:]]*) v=${v#?} ;;
      *) break ;;
    esac
  done
}

json_field() {
  case $1 in
    *\"$2\"*) ;;
    *) __value=; return 1 ;;
  esac
  v=${1#*\"$2\"}
  strip_blanks
  case $v in
    :*) v=${v#:} ;;
    *) __value=; return 1 ;;
  esac
  strip_blanks
  case $v in
    \"*) v=${v#\"} ;;
    *) __value=; return 1 ;;
  esac
  __value=${v%%\"*}
  return 0
}

input=
while IFS= read -r line || [ -n "$line" ]; do
  input=$input$line
done <&0

session=nosession
json_field "$input" session_id && case $__value in
  *[!A-Za-z0-9_-]*) ;;
  *) session=$__value ;;
esac
state_dir=${CLAUDE_PLUGIN_DATA:-${TMPDIR:-/tmp}}/ideo-scrum-memory
[ -d "$state_dir" ] || mkdir -p "$state_dir" 2>/dev/null

case $mode in
  expand)
    json_field "$input" command_name || exit 0
    case $__value in
      *developer) role=dev ;;
      *scrum-master) role=sm ;;
      *designer) role=des ;;
      *stakeholder) role=stk ;;
      *) exit 0 ;;
    esac
    printf '%s' "$role" > "$state_dir/$session.role" 2>/dev/null
    if [ -n "$part" ]; then cat "$here/memory-data/$role.p$part.json"; else cat "$here/memory-data/$role.json"; fi
    ;;
  compact)
    if [ -r "$state_dir/$session.role" ]; then
      read -r role < "$state_dir/$session.role"
      if [ -n "$part" ]; then cat "$here/memory-data/$role.p$part.txt"; else cat "$here/memory-data/$role.txt"; fi
    elif [ -r "$state_dir/$session.mark" ]; then
      if [ -n "$part" ]; then cat "$here/memory-data/all.p$part.txt"; else cat "$here/memory-data/all.txt"; fi
    fi
    ;;
  skill)
    json_field "$input" skill || exit 0
    case $__value in
      *developer) role=dev ;;
      *scrum-master) role=sm ;;
      *designer) role=des ;;
      *stakeholder) role=stk ;;
      *) exit 0 ;;
    esac
    printf '%s' "$role" > "$state_dir/$session.role" 2>/dev/null
    if [ -n "$part" ]; then cat "$here/memory-data/$role.pre.p$part.json"; else cat "$here/memory-data/$role.pre.json"; fi
    ;;
  mark)
    case $input in
      *ideo-scrum:memory*) printf 'x' > "$state_dir/$session.mark" 2>/dev/null ;;
    esac
    ;;
esac
exit 0
'''

SKILL_MD = '''---
name: memory
description: "Use only when summoned: an ideo-scrum role command tells you to load it, or the user asks for the plugin's Memory (the shared rules every role follows). When summoned, invoke this skill before answering, even for a short request. General questions about Scrum or design that do not name this plugin are not a summons: answer normally without loading it."
---

'''


def sh_cmd(mode: str) -> dict:
    return {"type": "command", "command": f'sh "${{CLAUDE_PLUGIN_ROOT}}/hooks/memory.sh" {mode}; exit 0', "timeout": 10}


SPLIT_AT = 9800  # a hook's additionalContext over 10,000 characters is moved to a file by the host; each part stays under it


def parts_of(text: str, limit: int = SPLIT_AT) -> list[str]:
    """Cut a text into parts of at most `limit` characters at line ends; the start of the text stays in the first part
    and the end in the last. One part when it fits."""
    if len(text) <= limit:
        return [text]
    parts, cur = [], ""
    for ln in text.splitlines(keepends=True):
        if cur and len(cur) + len(ln) > limit:
            parts.append(cur)
            cur = ""
        cur += ln
    parts.append(cur)
    return parts


def hook_modes(mode: str, n: int) -> list[dict]:
    return [sh_cmd(mode)] if n == 1 else [sh_cmd(f"{mode} {i}") for i in range(1, n + 1)]


def build_plugin(carrier: str, dest: pathlib.Path, c: dict) -> None:
    shutil.copytree(PLUGIN_SRC, dest)
    if carrier == "N":
        return
    full = memory_text(c)
    if carrier in ("A1", "C"):
        (dest / "skills" / "memory").mkdir()
        (dest / "skills" / "memory" / "SKILL.md").write_text(SKILL_MD + full, encoding="utf-8", newline="\n")
        for cmd in ROLES:
            p = dest / "commands" / f"{cmd}.md"
            text = p.read_text(encoding="utf-8")
            new, n = re.subn(r"(call the Skill tool in this order: (?:`[^`]+`(?: → )?)+)\.", r"\1 → `ideo-scrum:memory`.", text, count=1)
            assert n == 1, f"{cmd}: the loading sentence was not found"
            p.write_text(new, encoding="utf-8", newline="\n")
    if carrier == "A2":
        p = dest / "skills" / "scrum-kernel" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + full, encoding="utf-8", newline="\n")
    if carrier in ("B", "B2", "C"):
        hooks = dest / "hooks"
        (hooks / "memory-data").mkdir()
        (hooks / "memory.sh").write_text(HOOK_SH, encoding="utf-8", newline="\n")
        n_parts = 1
        for r in ROLE_TITLES:
            text = memory_text(c, [r])
            key = r.lower()
            ps = parts_of(text)
            n_parts = max(n_parts, len(ps))
            for i, part in enumerate(ps, start=1):
                tag = "" if len(ps) == 1 else f".p{i}"
                (hooks / "memory-data" / f"{key}{tag}.txt").write_text(part, encoding="utf-8", newline="\n")
                (hooks / "memory-data" / f"{key}{tag}.json").write_text(
                    json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptExpansion", "additionalContext": part}}, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="\n")
                (hooks / "memory-data" / f"{key}.pre{tag}.json").write_text(
                    json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": part}}, ensure_ascii=False) + "\n",
                    encoding="utf-8", newline="\n")
        fp = parts_of(full)
        n_parts = max(n_parts, len(fp))
        for i, part in enumerate(fp, start=1):
            (hooks / "memory-data" / ("all.txt" if len(fp) == 1 else f"all.p{i}.txt")).write_text(part, encoding="utf-8", newline="\n")
        cfg = json.loads((hooks / "hooks.json").read_text(encoding="utf-8"))
        h = cfg["hooks"]
        if carrier in ("B", "B2"):
            h["UserPromptExpansion"] = [{"matcher": "ideo-scrum:(developer|scrum-master|designer|stakeholder)", "hooks": hook_modes("expand", n_parts)}]
            if carrier == "B2":
                h["PreToolUse"] = h.get("PreToolUse", []) + [{"matcher": "Skill", "hooks": hook_modes("skill", n_parts)}]
        else:
            h["PostToolUse"] = [{"matcher": "Skill", "hooks": [sh_cmd("mark")]}]
        h["SessionStart"] = h["SessionStart"] + [{"matcher": "compact", "hooks": hook_modes("compact", n_parts)}]
        (hooks / "hooks.json").write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8", newline="\n")


def build_all(out: pathlib.Path) -> tuple[dict, dict]:
    c = new_canaries()
    base = out / "plugins"
    if base.exists():
        driver.rmtree(base)
    for carrier in CARRIERS + BUILD_ALSO:
        build_plugin(carrier, base / carrier / "ideo-scrum", c)
    (out / "canaries.json").write_text(json.dumps(c, indent=1), encoding="utf-8")
    sizes = {carrier: sum(p.stat().st_size for p in (base / carrier).rglob("*") if p.is_file()) for carrier in CARRIERS + BUILD_ALSO}
    return c, sizes


# ---- reading the event stream ----------------------------------------------------------------------------------
def read_stream(path: pathlib.Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            pass
    return rows


def text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(text_of(x.get("text") if isinstance(x, dict) and "text" in x else x.get("content", "") if isinstance(x, dict) else x) for x in content)
    return ""


def context_chars(stdout) -> int:
    """How many characters a hook put into the context: the additionalContext of its JSON output, or the plain text of
    a SessionStart hook. The host moves anything over 10,000 characters to a file and gives a 2,000-character preview."""
    s = text_of(stdout).strip()
    if s.startswith("{"):
        try:
            d = json.loads(s)
            return len(((d.get("hookSpecificOutput") or {}).get("additionalContext")) or "")
        except ValueError:
            pass
    return len(s)


def scan(rows: list[dict], c: dict) -> dict:
    """What the stream shows: Skill calls with their results, hook events, where each canary first appeared, whether a
    compaction happened and what came after it. Evidence only, no judgement."""
    uses: dict[str, dict] = {}
    skills, hooks, hits, subagent_text = [], [], {}, []
    boundary_at = None
    first_usage = None
    for i, r in enumerate(rows):
        raw = json.dumps(r, ensure_ascii=False)
        t, st = r.get("type"), r.get("subtype")
        if t == "system" and st == "compact_boundary":
            boundary_at = i
        if t == "system" and isinstance(st, str) and st.startswith("hook"):
            hooks.append({"i": i, "subtype": st, "event": r.get("hook_event"), "name": r.get("hook_name"), "exit": r.get("exit_code"),
                          "outcome": r.get("outcome"), "len": len(text_of(r.get("stdout") or r.get("output") or "")),
                          "ctx_len": context_chars(r.get("stdout") or r.get("output") or "")})
        if t == "assistant":
            msg = r.get("message") or {}
            if first_usage is None and msg.get("usage"):
                first_usage = msg["usage"]
            for b in msg.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    uses[b.get("id")] = {"name": b.get("name"), "input": b.get("input"), "i": i, "parent": r.get("parent_tool_use_id")}
        if t == "user":
            for b in (r.get("message") or {}).get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_result":
                    use = uses.get(b.get("tool_use_id"), {})
                    body = text_of(b.get("content"))
                    if use.get("name") == "Skill":
                        skills.append({"skill": (use.get("input") or {}).get("skill"), "ok": not b.get("is_error"), "i": i, "chars": len(body),
                                       "canaries": [k for k, v in c.items() if v in body]})
                    if use.get("name") == "Agent":
                        subagent_text.append(body)
        for k, v in c.items():
            if v in raw and k not in hits:
                hits[k] = {"i": i, "type": t, "subtype": st}
    results = [str(r.get("result") or "") for r in rows if r.get("type") == "result"]
    return {"skills": skills, "hooks": hooks, "hits": hits, "boundary_at": boundary_at, "n_events": len(rows), "first_usage": first_usage,
            "subagent_text": subagent_text, "results": results,
            "init": next(({"permissionMode": r.get("permissionMode"), "tools": r.get("tools"), "model_set": bool(r.get("model"))} for r in rows
                          if r.get("type") == "system" and r.get("subtype") == "init"), None),
            "denials": sum(len(r.get("permission_denials") or []) for r in rows if r.get("type") == "result"),
            "tool_names": sorted({u["name"] for u in uses.values() if u.get("name")})}


# ---- one session ------------------------------------------------------------------------------------------------
SCENARIOS = {
    "role": lambda role: [f"/ideo-scrum:{role}"],
    # after compaction the stream does not show what was re-attached, so the probe asks for two things only the full text
    # can give: the probe rule, and the random end marker (a summary does not keep a random token; a truncated copy loses it)
    "compact": lambda role: [f"/ideo-scrum:{role}", "/compact",
                             "A new Sprint is about to be opened for a login-page redesign. Without using any tool, answer two things. "
                             "1) What exact suffix should its folder name end with, according to the plugin Memory you were given earlier? "
                             "2) Quote, character for character, the very last line of that plugin Memory (it is one marker token). "
                             "If you do not have them, say so; do not guess."],
    "subagent": lambda role: [f"/ideo-scrum:{role}",
                              "Use the Agent tool to start one general-purpose subagent. Give it exactly this task and nothing else, no rules and no background: "
                              "\"Suggest a folder name for a new Sprint about a login-page redesign. Reply with just the folder name.\" Then tell me what the subagent answered."],
    "plain": lambda role: ["Write a Python function that returns the first n Fibonacci numbers."],
    # criterion 4, sub-case for B and C: an ordinary session (no role was ever called), one /compact
    "plain-compact": lambda role: ["Write a Python function that returns the first n Fibonacci numbers.", "/compact"],
    "model": lambda role: [f"Please call the Skill tool now with the skill `ideo-scrum:{role}`, then reply with the single word ready."],
}


def run_trial(out: pathlib.Path, carrier: str, scenario: str, role: str, n: int, c: dict) -> dict:
    tag = f"{scenario}-{carrier}-{role}-{n}"
    d = out / "trials" / tag
    d.mkdir(parents=True, exist_ok=True)
    root = pathlib.Path(tempfile.mkdtemp(prefix="s26-", dir=driver.neutral_parent()))
    t0 = time.time()
    status = "ok"
    try:
        env, home = driver.make_env(root / "env")
        proj = root / "project"
        proj.mkdir()
        tools = TOOLS if scenario == "subagent" else TOOLS_NO_AGENT
        # tools limited with --tools (--allowedTools only skips the prompt), nothing else allowed (dontAsk), user settings
        # kept out (headless-testing.md, Sprint 19); the init event is checked in the smoke run for the real tool list
        cmd = driver.magpie_prefix() + ["-p", "--input-format", "stream-json", "--output-format", "stream-json", "--verbose",
                                        "--include-hook-events", "--model", MODEL, "--tools", tools, "--allowedTools", tools,
                                        "--disallowedTools", "Bash,PowerShell,Write,Edit,NotebookEdit",
                                        "--permission-mode", "dontAsk", "--strict-mcp-config",
                                        "--setting-sources", "project,local", "--plugin-dir", str(out / "plugins" / carrier / "ideo-scrum")]
        s = driver.Session(tag, cmd, proj, env, d / "stream.jsonl")
        s.start()
        for m in SCENARIOS[scenario](role):
            r = s.send(m, LIMITS["message_s"])
            if r["status"] != "ok":
                status = r["status"]
                break
        s.close()
    except Exception as e:  # a harness failure is a technical failure of the trial, recorded
        status = f"harness-error: {e}"
    finally:
        driver.rmtree(root)
    ev = scan(read_stream(d / "stream.jsonl"), c) if (d / "stream.jsonl").exists() else {}
    res = {"tag": tag, "carrier": carrier, "scenario": scenario, "role": role, "n": n, "status": status, "seconds": round(time.time() - t0, 1), "evidence": ev}
    (d / "evidence.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


def cmd_smoke(a) -> int:
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    c, sizes = build_all(out)
    print("built", sizes)
    # the ground rule of the smoke run: only how the evidence is read may change after it, never the pass lines
    base = pathlib.Path(tempfile.mkdtemp(prefix="s26-probe-", dir=driver.neutral_parent()))
    try:
        env, _ = driver.make_env(base / "env")
        proj = base / "project"
        proj.mkdir()
        files = driver.probe_memory_files(env, proj, [])
        print("instruction files loaded into a session in the run folder:", files)
    finally:
        driver.rmtree(base)
    jobs = [(carrier, "role", "developer", 0) for carrier in CARRIERS] + [
        ("A1", "compact", "developer", 0), ("B", "compact", "developer", 0), ("C", "compact", "developer", 0),
        ("N", "plain", "developer", 0), ("B", "plain-compact", "developer", 0), ("C", "plain-compact", "developer", 0),
        ("A1", "subagent", "developer", 0), ("A1", "model", "developer", 0), ("B", "model", "developer", 0),
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        for res in ex.map(lambda j: run_trial(out, *j, c), jobs):
            ev = res["evidence"]
            print(res["tag"], res["status"], res["seconds"], "s; skills", [(s["skill"], s["ok"], s["canaries"]) for s in ev.get("skills", [])],
                  "hooks", [(h["event"], h["subtype"], h["exit"], h["len"]) for h in ev.get("hooks", [])], "hits", list(ev.get("hits", {})),
                  "boundary", ev.get("boundary_at"), "tools", ev.get("tool_names"))
    return 0


def free_mb() -> int:
    """Free physical memory in MB, as Windows reports it (the same number the watchdog reads)."""
    out = subprocess.run(["powershell", "-NoProfile", "-Command", "(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory"],
                         capture_output=True, text=True, timeout=60).stdout.strip()
    return int(out) // 1024


class Gate:
    """Concurrency drops to 1 while free memory is under the soft floor (Master 2026-11-23: under 3 GB, one session at a time).
    A trial starts when nothing else is running, or when free memory is at the floor or above; a running trial is never stopped.
    The hard floor (2 GB) is the watchdog's: it stops the whole run."""

    def __init__(self, soft_mb: int, free=free_mb, poll_s: float = 15.0):
        self.soft_mb, self.free, self.poll_s = soft_mb, free, poll_s
        self.active = 0
        self.lock = threading.Lock()
        self.low = False  # under the floor right now
        self.dropped = False  # was under the floor at some trial start
        self.lowest = None

    def enter(self) -> None:
        while True:
            with self.lock:
                if self.active == 0:
                    self.active = 1
                    return
                f = self.free()
                self.lowest = f if self.lowest is None else min(self.lowest, f)
                if f >= self.soft_mb:
                    self.active += 1
                    if self.low:
                        self.low = False
                        print(f"[gate] free {f} MB: back to the full concurrency", flush=True)
                    return
                if not self.low:
                    self.low = self.dropped = True
                    print(f"[gate] free {f} MB under {self.soft_mb} MB: one session at a time until it recovers", flush=True)
            time.sleep(self.poll_s)

    def leave(self) -> None:
        with self.lock:
            self.active -= 1


def cmd_run(a) -> int:
    out = pathlib.Path(a.out)
    c = json.loads((out / "canaries.json").read_text(encoding="utf-8"))
    roles = list(ROLES) if a.role == "all" else [a.role]
    carriers = CARRIERS if a.carrier == "all" else a.carrier.split(",")
    jobs = [(carrier, a.scenario, role, n) for carrier in carriers for role in roles for n in range(1, a.n + 1)]
    if a.skip_done:  # a resumed run: a trial that already has valid evidence is not run again
        keep = []
        for j in jobs:
            ev = out / "trials" / f"{a.scenario}-{j[0]}-{j[2]}-{j[3]}" / "evidence.json"
            ok = False
            if ev.exists():
                try:
                    ok = json.loads(ev.read_text(encoding="utf-8")).get("status") == "ok"
                except ValueError:
                    ok = False
            if not ok:
                keep.append(j)
        print(f"skip-done: {len(jobs) - len(keep)} of {len(jobs)} trials already have valid evidence")
        jobs = keep
    gate = Gate(a.soft_free_mb) if a.soft_free_mb else None

    def one(j):
        if gate:
            gate.enter()
        try:
            return run_trial(out, *j, c)
        finally:
            if gate:
                gate.leave()

    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as ex:
        for res in ex.map(one, jobs):
            print(res["tag"], res["status"], res["seconds"])
    if gate:
        print(f"[gate] lowest free memory seen at a trial start: {gate.lowest} MB; dropped to one session at a time: {'yes' if gate.dropped else 'no'}")
    return 0


def pct(xs: list[float], p: float) -> float:
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(p * (len(xs) - 1))))]


def cmd_timing(a) -> int:
    out = pathlib.Path(a.out)
    c = json.loads((out / "canaries.json").read_text(encoding="utf-8"))
    sh = shutil.which("sh")
    stdin = {"expand": json.dumps({"session_id": "timing-test", "hook_event_name": "UserPromptExpansion", "command_name": "ideo-scrum:developer"}),
             "compact": json.dumps({"session_id": "timing-test", "hook_event_name": "SessionStart", "source": "compact"}),
             "mark": json.dumps({"session_id": "timing-test", "hook_event_name": "PostToolUse", "tool_input": {"skill": "ideo-scrum:memory"}})}
    res = {}
    for carrier in ("B", "C"):
        script = out / "plugins" / carrier / "ideo-scrum" / "hooks" / "memory.sh"
        for mode in ("expand", "compact", "mark"):
            ts = []
            for _ in range(a.runs):
                t = time.perf_counter()
                subprocess.run([sh, str(script), mode], input=stdin[mode], capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(out / "state")})
                ts.append((time.perf_counter() - t) * 1000)
            res[f"{carrier}/{mode}"] = {"runs": len(ts), "p50_ms": round(statistics.median(ts), 1), "p95_ms": round(pct(ts, 0.95), 1), "max_ms": round(max(ts), 1)}
            print(f"{carrier}/{mode}: {res[f'{carrier}/{mode}']}")
    (out / "timing.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    return 0


def skill_ok(ev: dict, name: str, hit: dict | None) -> bool:
    """The skill was called, succeeded, and the text that carries the canary came after that call."""
    return any(s["skill"] == name and s["ok"] and (hit is None or hit["i"] >= s["i"]) for s in ev.get("skills", []))


def judge(res: dict, c: dict) -> dict:
    """The criteria applied to one trial's evidence: what pass means for it, plus the numbers they ask to report.
    Nothing here reads what the model says about itself, except the probe answer after a compaction (the criteria's
    fallback: the log does not show what was re-attached, and a random end marker cannot survive a summary or a cut)."""
    ev = res.get("evidence") or {}
    sc, ca = res["scenario"], res["carrier"]
    hits = ev.get("hits") or {}
    start, end = hits.get("MEMORY-START"), hits.get("MEMORY-END")
    out = {"tag": res["tag"], "carrier": ca, "scenario": sc, "role": res["role"], "status": res["status"]}
    if res["status"] != "ok":
        out["technical_failure"] = True
        return out
    hook_resp = [h for h in ev.get("hooks", []) if h["subtype"] == "hook_response"]
    if sc == "role":
        if ca == "N":
            ok = not hits
        elif ca in ("A1", "C"):
            ok = bool(start and end and start["type"] == "user" and skill_ok(ev, "ideo-scrum:memory", start))
        elif ca == "A2":
            ok = bool(start and end and start["type"] == "user" and skill_ok(ev, "ideo-scrum:scrum-kernel", start))
        else:  # B, B2: the hook's own output
            exp = [h for h in hook_resp if h["event"] == "UserPromptExpansion"]
            sizes = [h.get("ctx_len", 0) for h in exp]
            out["ctx_chars"] = sizes
            ok = bool(exp and all(h["exit"] == 0 for h in exp) and start and end and start["subtype"] == "hook_response" and max(sizes) <= 10000)
        out["pass"] = ok
        out["roles_seen"] = sorted(k for k in hits if k.startswith("ROLE-"))
    elif sc == "compact":
        ans = (ev.get("results") or [""])[-1]
        out["compacted"] = ev.get("boundary_at") is not None
        out["probe_suffix"] = PROBE_SUFFIX in ans
        out["end_marker"] = c["MEMORY-END"] in ans
        out["pass"] = bool(out["compacted"] and out["probe_suffix"] and out["end_marker"])
    elif sc == "subagent":
        out["pass"] = any(PROBE_SUFFIX in tx for tx in ev.get("subagent_text") or [])
    elif sc in ("plain", "plain-compact"):
        out["pass"] = not hits and not any("memory" in (s.get("skill") or "") for s in ev.get("skills", []))
        if sc == "plain-compact":
            out["compacted"] = ev.get("boundary_at") is not None
        fu = ev.get("first_usage") or {}
        out["first_request_tokens"] = sum(fu.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    elif sc == "model":
        out["pass"] = bool(start and end)
    return out


SCEN_TITLES = [("role", "① 叫出角色必带上（用户打 /ideo-scrum:<角色>）"), ("compact", "② 压缩后还在（探针答复含 -zq7 与确切结尾暗号）"),
               ("subagent", "③ 子代理（产出里有 -zq7；只报）"), ("plain", "④ 普通会话不出现暗号"), ("plain-compact", "④ 子情形：普通会话里 /compact 不误注"),
               ("model", "另测：模型自己调 Skill 叫角色（只报）")]


def cmd_report(a) -> int:
    out = pathlib.Path(a.out)
    c = json.loads((out / "canaries.json").read_text(encoding="utf-8"))
    rows = []
    for f in sorted((out / "trials").glob("*/evidence.json")):
        res = json.loads(f.read_text(encoding="utf-8"))
        if (f.parent / "stream.jsonl").exists():  # read the raw stream again, so a better way of reading applies to trials already run
            res["evidence"] = scan(read_stream(f.parent / "stream.jsonl"), c)
        rows.append(judge(res, c))
    carriers = [x for x in CARRIERS + BUILD_ALSO if any(r["carrier"] == x for r in rows)]
    md = [f"# 载体测试结果：{getattr(a, 'label', None) or out.name}", "",
          "单元格＝通过的试次／有效试次；括号里是技术失败的试次（超时、被杀、接口错，另补跑）。N 是对照：① ④ 应全过、② ③ 应为 0。", "",
          "| 判据 | " + " | ".join(carriers) + " |", "| --- | " + " | ".join("---" for _ in carriers) + " |"]
    for sc, title in SCEN_TITLES:
        cells = []
        for ca in carriers:
            rs = [r for r in rows if r["scenario"] == sc and r["carrier"] == ca]
            if not rs:
                cells.append("—")
                continue
            tech = sum(1 for r in rs if r.get("technical_failure"))
            good = sum(1 for r in rs if r.get("pass"))
            cells.append(f"{good}/{len(rs) - tech}" + (f"（{tech} 次技术失败）" if tech else ""))
        if any(x != "—" for x in cells):
            md.append(f"| {title} | " + " | ".join(cells) + " |")
    roles = sorted({r["role"] for r in rows if r["scenario"] == "role"})
    if roles:
        md += ["", "## ⑦ 每个角色带上了哪些暗号（① 的会话）", "", "| 角色 | " + " | ".join(carriers) + " |", "| --- | " + " | ".join("---" for _ in carriers) + " |"]
        for role in roles:
            cells = []
            for ca in carriers:
                seen = sorted({k.replace("ROLE-", "") for r in rows if r["scenario"] == "role" and r["carrier"] == ca and r["role"] == role for k in r.get("roles_seen", [])})
                cells.append(",".join(seen) or "—")
            md.append(f"| {role} | " + " | ".join(cells) + " |")
    sizes = sorted({n for r in rows if r["scenario"] == "role" and r["carrier"] in ("B", "B2") for n in r.get("ctx_chars", [])})
    if sizes:
        md += ["", f"B 的每次 additionalContext 字符数：{sizes}（线：≤ 10,000）"]
    plain = {ca: [r["first_request_tokens"] for r in rows if r["scenario"] == "plain" and r["carrier"] == ca and "first_request_tokens" in r] for ca in carriers}
    if plain.get("N"):
        base = statistics.mean(plain["N"])
        md += ["", "④ 普通会话第一次请求的输入 token（含缓存）对 N 的差（只报）：" + "；".join(f"{ca} {statistics.mean(v) - base:+.0f}" for ca, v in plain.items() if v and ca != "N")]
    bad = [r for r in rows if not r.get("technical_failure") and r.get("pass") is False]
    if bad:
        md += ["", "## 没过的试次（含对照 N 本来就应不过的）", ""] + [f"- {r['tag']}" + (f"：ctx_chars {r['ctx_chars']}" if r.get("ctx_chars") else "") + (f"：探针 {r.get('probe_suffix')}、结尾暗号 {r.get('end_marker')}、压缩 {r.get('compacted')}" if r["scenario"] == "compact" else "") for r in bad]
    tech = [r["tag"] + " " + r["status"] for r in rows if r.get("technical_failure")]
    if tech:
        md += ["", "## 技术失败（要补跑）", ""] + [f"- {x}" for x in tech]
    (out / "report.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "report.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(md))
    return 0


def cmd_selftest(a) -> int:
    ok = True

    def check(cond: bool, what: str):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + what)
        ok = ok and cond

    c = new_canaries()
    full = memory_text(c)
    one = memory_text(c, ["DEV"])
    check(7500 <= len(full) <= 9500, f"the stand-in is about 8,000 characters ({len(full)})")
    check(full.index(c["MEMORY-START"]) < full.index(c["ROLE-DEV"]) < full.index(c["MEMORY-END"]), "start canary, role canary, end canary in that order")
    check(all(c[k] in full for k in c), "the full text carries every canary")
    check(c["ROLE-DEV"] in one and c["ROLE-SM"] not in one and c["MEMORY-START"] in one and c["MEMORY-END"] in one, "a hook's text carries the shared part and only its own role")
    check(PROBE_SUFFIX in full, "the probe rule is in the shared part")
    check(len(set(c.values())) == len(c), "canaries are distinct")
    rows = [
        {"type": "system", "subtype": "hook_response", "hook_event": "UserPromptExpansion", "hook_name": "x", "exit_code": 0, "stdout": "a " + c["MEMORY-START"]},
        {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "t1", "name": "Skill", "input": {"skill": "ideo-scrum:memory"}}], "usage": {"input_tokens": 5}}},
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t1", "content": "body " + c["MEMORY-END"]}]}},
        {"type": "system", "subtype": "compact_boundary"},
    ]
    ev = scan(rows, c)
    check(ev["skills"] == [{"skill": "ideo-scrum:memory", "ok": True, "i": 2, "chars": len("body " + c["MEMORY-END"]), "canaries": ["MEMORY-END"]}], "scan: a Skill call and the canary in its result")
    check(ev["hooks"][0]["len"] > 0 and ev["hits"]["MEMORY-START"]["subtype"] == "hook_response", "scan: a hook's output and where the canary first appeared")
    check(ev["boundary_at"] == 3, "scan: the compaction boundary")
    g = Gate(3000, free=lambda: 1000, poll_s=0.05)
    g.enter()
    started = []

    def second():
        g.enter()
        started.append(1)
        g.leave()

    th = threading.Thread(target=second)
    th.start()
    time.sleep(0.4)
    check(not started and g.dropped, "gate: free memory under the floor, a second trial waits for the first")
    g.leave()
    th.join(timeout=5)
    check(started == [1] and g.active == 0, "gate: it starts once the first has left")
    g2 = Gate(3000, free=lambda: 5000, poll_s=0.05)
    g2.enter()
    g2.enter()
    check(g2.active == 2 and not g2.dropped, "gate: with enough free memory two run together")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="s26-selftest-"))
    try:
        build_plugin("A1", tmp / "A1", c)
        text = (tmp / "A1" / "commands" / "developer.md").read_text(encoding="utf-8")
        check("`ideo-scrum:sprint-kernel` → `ideo-scrum:memory`." in text, "A1: the developer entry calls memory last")
        check("`ideo-scrum:design-kernel` → `ideo-scrum:memory`." in (tmp / "A1" / "commands" / "scrum-master.md").read_text(encoding="utf-8"), "A1: the scrum-master entry calls memory after design-kernel")
        build_plugin("B", tmp / "B", c)
        cfg = json.loads((tmp / "B" / "hooks" / "hooks.json").read_text(encoding="utf-8"))
        check("UserPromptExpansion" in cfg["hooks"] and cfg["hooks"]["SessionStart"][-1]["matcher"] == "compact" and len(cfg["hooks"]["SessionStart"]) == 2, "B: hooks.json keeps the commitments hook and adds the two new ones")
        data = json.loads((tmp / "B" / "hooks" / "memory-data" / "dev.json").read_text(encoding="utf-8"))
        check(c["MEMORY-END"] in data["hookSpecificOutput"]["additionalContext"], "B: the developer hook output is valid JSON and carries the text")
        build_plugin("A2", tmp / "A2", c)
        check((tmp / "A2" / "skills" / "scrum-kernel" / "SKILL.md").read_text(encoding="utf-8").rstrip().endswith(c["MEMORY-END"]), "A2: the Memory is at the end of scrum-kernel")
        sh = shutil.which("sh")
        r = subprocess.run([sh, str(tmp / "B" / "hooks" / "memory.sh"), "expand"], input=json.dumps({"session_id": "t", "command_name": "ideo-scrum:developer"}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
        check(r.returncode == 0 and c["ROLE-DEV"] in r.stdout, "B: the hook script prints the developer text for a developer command")
        r = subprocess.run([sh, str(tmp / "B" / "hooks" / "memory.sh"), "expand"], input=json.dumps({"session_id": "t2", "command_name": "ideo-scrum:other"}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
        check(r.returncode == 0 and r.stdout == "", "B: the hook script prints nothing for any other command")
        r = subprocess.run([sh, str(tmp / "B" / "hooks" / "memory.sh"), "compact"], input=json.dumps({"session_id": "t"}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
        check(c["ROLE-DEV"] in r.stdout, "B: after compaction the same role's text comes back")
        r = subprocess.run([sh, str(tmp / "B" / "hooks" / "memory.sh"), "compact"], input=json.dumps({"session_id": "never-called"}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
        check(r.stdout == "", "B: a session that never called a role gets nothing after compaction")
        check(parts_of("a\nb\n", 100) == ["a\nb\n"], "a short text is one part")
        src = "".join(f"line {i}\n" for i in range(300))
        ps = parts_of(src, 500)
        check(len(ps) > 1 and all(len(p) <= 500 for p in ps) and "".join(ps) == src, "a long text is cut at line ends and nothing is lost")
        two = hook_modes("expand", 2)
        check(hook_modes("expand", 1) == [sh_cmd("expand")] and "expand 1;" in two[0]["command"] and "expand 2;" in two[1]["command"], "one hook for one part, 'expand 1' and 'expand 2' for two")
        build_plugin("B2", tmp / "B2", c)
        cfg3 = json.loads((tmp / "B2" / "hooks" / "hooks.json").read_text(encoding="utf-8"))["hooks"]
        check(cfg3["PreToolUse"][-1]["matcher"] == "Skill" and "skill" in cfg3["PreToolUse"][-1]["hooks"][0]["command"] and "UserPromptExpansion" in cfg3, "B2: B plus a PreToolUse hook on Skill")
        r = subprocess.run([sh, str(tmp / "B2" / "hooks" / "memory.sh"), "skill"], input=json.dumps({"session_id": "t4", "hook_event_name": "PreToolUse", "tool_name": "Skill", "tool_input": {"skill": "ideo-scrum:developer"}}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
        pre = json.loads(r.stdout)["hookSpecificOutput"] if r.stdout else {}
        check(pre.get("hookEventName") == "PreToolUse" and c["ROLE-DEV"] in pre.get("additionalContext", ""), "B2: a model's call of the developer skill gets the developer text as PreToolUse context")
        r = subprocess.run([sh, str(tmp / "B2" / "hooks" / "memory.sh"), "skill"], input=json.dumps({"session_id": "t5", "tool_name": "Skill", "tool_input": {"skill": "ideo-scrum:ideo-kernel"}}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
        check(r.stdout == "", "B2: a kernel skill gets nothing")
        check(context_chars(json.dumps({"hookSpecificOutput": {"hookEventName": "X", "additionalContext": "abc"}})) == 3 and context_chars("plain text\n") == 10, "context_chars: the additionalContext of the JSON, or the plain text")
        good = {"tag": "role-A1-developer-0", "scenario": "role", "carrier": "A1", "role": "developer", "status": "ok",
                "evidence": {"hits": {"MEMORY-START": {"i": 22, "type": "user", "subtype": None}, "MEMORY-END": {"i": 22, "type": "user", "subtype": None}, "ROLE-DEV": {"i": 22, "type": "user", "subtype": None}},
                             "skills": [{"skill": "ideo-scrum:memory", "ok": True, "i": 21}]}}
        check(judge(good, c)["pass"] is True, "judge: A1 passes when the memory skill succeeded and its text came after")
        bad = json.loads(json.dumps(good))
        bad["evidence"]["skills"] = []
        check(judge(bad, c)["pass"] is False, "judge: A1 fails without a successful memory skill call")
        bsz = {"tag": "role-B-developer-0", "scenario": "role", "carrier": "B", "role": "developer", "status": "ok",
               "evidence": {"hits": {"MEMORY-START": {"i": 5, "type": "system", "subtype": "hook_response"}, "MEMORY-END": {"i": 5, "type": "system", "subtype": "hook_response"}},
                            "hooks": [{"subtype": "hook_response", "event": "UserPromptExpansion", "exit": 0, "len": 12000, "ctx_len": 11000}]}}
        check(judge(bsz, c)["pass"] is False, "judge: B fails when one hook put more than 10,000 characters into the context")
        bsz["evidence"]["hooks"][0]["ctx_len"] = 9500
        check(judge(bsz, c)["pass"] is True, "judge: B passes at 9,500")
        cmp_ = {"tag": "compact-A2-developer-0", "scenario": "compact", "carrier": "A2", "role": "developer", "status": "ok",
                "evidence": {"boundary_at": 100, "results": ["a", "b", f"The suffix ends with {PROBE_SUFFIX}. The last line is not known."]}}
        check(judge(cmp_, c)["pass"] is False, "judge: a compaction answer without the exact end marker fails")
        cmp_["evidence"]["results"][-1] += " " + c["MEMORY-END"]
        check(judge(cmp_, c)["pass"] is True, "judge: with the probe suffix and the end marker it passes")
        old = TARGET_CHARS
        globals()["TARGET_CHARS"] = 20000  # the larger stand-in: the hook must send it in parts, each under the host's limit
        try:
            big = new_canaries()
            build_plugin("B", tmp / "B20", big)
            hl = json.loads((tmp / "B20" / "hooks" / "hooks.json").read_text(encoding="utf-8"))["hooks"]["UserPromptExpansion"][0]["hooks"]
            check(len(hl) == 2, f"B at 20,000 characters: two hooks, one per part ({len(hl)})")
            q1 = json.loads((tmp / "B20" / "hooks" / "memory-data" / "dev.p1.json").read_text(encoding="utf-8"))["hookSpecificOutput"]["additionalContext"]
            q2 = json.loads((tmp / "B20" / "hooks" / "memory-data" / "dev.p2.json").read_text(encoding="utf-8"))["hookSpecificOutput"]["additionalContext"]
            check(len(q1) <= 10000 and len(q2) <= 10000 and big["MEMORY-START"] in q1 and big["MEMORY-END"] in q2, f"each part is under 10,000 characters ({len(q1)}, {len(q2)}), the start in the first, the end in the last")
            outs = []
            for i in (1, 2):
                r = subprocess.run([sh, str(tmp / "B20" / "hooks" / "memory.sh"), "expand", str(i)], input=json.dumps({"session_id": "t3", "command_name": "ideo-scrum:developer"}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
                outs.append(r.stdout)
            check(big["MEMORY-START"] in outs[0] and big["MEMORY-END"] in outs[1] and big["MEMORY-END"] not in outs[0], "B at 20,000: the hook script prints part 1 and part 2")
            r = subprocess.run([sh, str(tmp / "B20" / "hooks" / "memory.sh"), "compact", "2"], input=json.dumps({"session_id": "t3"}), capture_output=True, text=True, env={**os.environ, "CLAUDE_PLUGIN_DATA": str(tmp / "st")})
            check(big["MEMORY-END"] in r.stdout, "B at 20,000: after compaction part 2 comes back too")
        finally:
            globals()["TARGET_CHARS"] = old
    finally:
        driver.rmtree(tmp)
    print("selftest:", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    global TARGET_CHARS
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest")
    for name in ("build", "smoke", "timing", "report"):
        p = sub.add_parser(name)
        p.add_argument("--out", required=True)
        p.add_argument("--parallel", type=int, default=5)
        p.add_argument("--runs", type=int, default=20)
        p.add_argument("--chars", type=int, default=TARGET_CHARS, help="size of the stand-in Memory in characters (the default is the committed criteria's)")
    p = sub.add_parser("run")
    p.add_argument("--out", required=True)
    p.add_argument("--scenario", choices=sorted(SCENARIOS), required=True)
    p.add_argument("--carrier", default="all")
    p.add_argument("--role", default="developer")
    p.add_argument("--n", type=int, default=3)
    p.add_argument("--parallel", type=int, default=4)
    p.add_argument("--skip-done", action="store_true", help="do not run a trial that already has valid evidence (resume after a stop)")
    p.add_argument("--soft-free-mb", type=int, default=0, help="while free memory is under this, start a trial only when nothing else is running (0: off)")
    p.add_argument("--chars", type=int, default=TARGET_CHARS, help="size of the stand-in Memory in characters (the default is the committed criteria's)")
    a = ap.parse_args(argv)
    if getattr(a, "chars", None):
        TARGET_CHARS = a.chars
    if a.cmd == "selftest":
        return cmd_selftest(a)
    if a.cmd == "build":
        c, sizes = build_all(pathlib.Path(a.out))
        print(sizes)
        return 0
    return {"smoke": cmd_smoke, "run": cmd_run, "timing": cmd_timing, "report": cmd_report}.get(a.cmd, lambda a: 2)(a)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
