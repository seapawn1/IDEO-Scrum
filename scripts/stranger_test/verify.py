"""Checks on a finished stranger-test run (Sprint 20, PBI-63; the standard is section 2.2 of that Sprint's log,
"63-a"): the five outputs in the temporary project, the isolation of the plugin session, and the signals the
stuck criteria are read from. Everything here reads results, not the conversation; whether a stuck point is the
documents' or the model's is read by a person.
"""
import json
import os
import pathlib
import re
import subprocess
import sys

COMMIT_ROW = re.compile(r"^\|\s*(Commitment|承诺)\s*\|\s*(.+?)\s*\|\s*$", re.M)
GO_AHEAD = re.compile(r"go-ahead|放行", re.I)
SPRINT_LOG_PATH = re.compile(r"^scrum/(sprint-\d+-[^/]+/SprintBacklog\.md|documents/.+\.md)$")
SPRINT_FOLDER = re.compile(r"^scrum/(sprint-\d+-[^/]+)/")
BUILTIN_PLUGIN_PREFIX = "cc-plugin-"  # Claude Code's own built-in plugins show up in init next to ours
TOOL_SUFFIXES = {".py": ["python"], ".js": ["node"], ".sh": ["bash"], ".bat": ["cmd", "/c"], ".cmd": ["cmd", "/c"]}


def read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")


def git(proj: pathlib.Path, env: dict, *args: str, timeout: int = 90) -> str:
    r = subprocess.run(["git", "-C", str(proj), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=timeout, env=env, stdin=subprocess.DEVNULL)
    return r.stdout if r.returncode == 0 else ""


# ---- the five outputs ---------------------------------------------------------------------------------------
def commitment_rows(text: str) -> list:
    return [m.group(2) for m in COMMIT_ROW.finditer(text)]


def real_commitment(row: str) -> bool:
    """A filled commitment, not the template's placeholder."""
    return len(row) >= 5 and "<" not in row and ">" not in row


def sprint_log_texts(proj: pathlib.Path, env: dict) -> dict:
    """The text of every sprint log, or archived sprint log, ever in the project: path -> text (the working tree
    and every line any commit added)."""
    texts: dict = {}
    for p in list(proj.glob("scrum/sprint-*/SprintBacklog.md")) + list(proj.glob("scrum/documents/**/*.md")):
        rel = p.relative_to(proj).as_posix()
        if SPRINT_LOG_PATH.match(rel):
            texts[rel] = texts.get(rel, "") + read(p) + "\n"
    log = git(proj, env, "log", "--all", "-p", "--no-color", "--format=", "--", "scrum", timeout=180)
    current = None
    for line in log.split("\n"):
        if line.startswith("diff --git "):
            m = re.match(r"diff --git a/(.+?) b/(.+)$", line)
            current = m.group(2) if m and SPRINT_LOG_PATH.match(m.group(2)) else None
        elif current and line.startswith("+") and not line.startswith("+++"):
            texts[current] = texts.get(current, "") + line[1:] + "\n"
    return texts


def check_outputs(proj: pathlib.Path, env: dict, board_check=None) -> dict:
    """The five outputs of 63-a. Each value is {"ok": bool, "detail": str}."""
    out = {}

    pl = proj / "scrum" / "ProductBacklog.md"
    if not pl.is_file():
        out["1_product_log"] = {"ok": False, "detail": "no scrum/ProductBacklog.md"}
    else:
        rows = [r for r in commitment_rows(read(pl)) if real_commitment(r)]
        out["1_product_log"] = {"ok": len(rows) >= 2, "detail": f"{len(rows)} filled commitment rows"}

    texts = sprint_log_texts(proj, env)
    goal = [p for p, t in texts.items() if any(real_commitment(r) for r in commitment_rows(t))]
    ahead = [p for p, t in texts.items() if GO_AHEAD.search(t)]
    out["2_sprint_log"] = {"ok": bool(goal) and bool(ahead),
                           "detail": f"Sprint Goal commitment in {sorted(goal)[:3]}; go-ahead in {sorted(ahead)[:3]}"}

    out["3_tool_runs"] = check_tool(proj)

    names = set()
    for line in git(proj, env, "log", "--all", "--name-only", "--format=").split("\n"):
        m = SPRINT_FOLDER.match(line.strip())
        if m:
            names.add(m.group(1))
    tags = set(git(proj, env, "tag", "-l").split())
    archived = {p.stem for p in proj.glob("scrum/documents/**/*.md")}
    closed = sorted(n for n in names if n in tags and n in archived)
    out["4_close"] = {"ok": bool(closed),
                      "detail": f"sprint folders {sorted(names)}, tags {sorted(tags)}, archived {sorted(archived)[:5]}"}

    board = proj / "scrum" / "Board.html"
    if not board.is_file():
        out["5_board"] = {"ok": False, "detail": "no scrum/Board.html"}
    elif board_check is None:
        out["5_board"] = {"ok": True, "detail": "the file is there; the 68-4 check is not wired in yet"}
    else:
        ok, detail = board_check(board, proj)
        out["5_board"] = {"ok": ok, "detail": detail}
    return out


def check_tool(proj: pathlib.Path) -> dict:
    """The little tool: run each script found in the project (not under scrum/ or .git/); it passes when one exits
    0 and prints a line."""
    tried = []
    for p in sorted(proj.rglob("*")):
        rel = p.relative_to(proj).as_posix()
        if not p.is_file() or rel.startswith((".git/", "scrum/")) or len(rel.split("/")) > 4:
            continue
        runner = TOOL_SUFFIXES.get(p.suffix.lower())
        if not runner:
            continue
        env = {k: v for k, v in os.environ.items() if k.lower() in ("systemroot", "path", "comspec", "pathext")}
        try:
            r = subprocess.run(runner + [str(p)], cwd=str(proj), capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=20, env=env, stdin=subprocess.DEVNULL)
        except (subprocess.TimeoutExpired, OSError) as e:
            tried.append(f"{rel}: {type(e).__name__}")
            continue
        line = next((l for l in r.stdout.split("\n") if l.strip()), "")
        tried.append(f"{rel}: exit {r.returncode}, {'a line' if line else 'no output'}")
        if r.returncode == 0 and line:
            return {"ok": True, "detail": f"{rel} printed a line ({len(line)} characters)"}
    return {"ok": False, "detail": "no script ran and printed a line; tried: " + ("; ".join(tried) or "none")}


# ---- isolation ----------------------------------------------------------------------------------------------
def norm_path(s: str) -> str:
    """Lower case, forward slashes, and the MSYS form /c/users folded to c:/users."""
    s = s.replace("\\", "/").lower()
    return re.sub(r"^/([a-z])/", r"\1:/", s)


def tool_inputs(rows: list) -> list:
    """[(tool name, string)] for every string in every tool call of the stream."""
    found = []

    def walk(name, v):
        if isinstance(v, str):
            found.append((name, v))
        elif isinstance(v, dict):
            for x in v.values():
                walk(name, x)
        elif isinstance(v, list):
            for x in v:
                walk(name, x)

    for d in rows:
        if d.get("type") == "assistant":
            for c in (d.get("message") or {}).get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    walk(c.get("name"), c.get("input"))
    return found


def scan_paths(rows: list, allowed_roots: list, real_home: str, forbidden: tuple) -> list:
    """What the plugin session reached for that is the author's: a path under the real home that is not inside
    one of the run's own folders, or any of the forbidden names. Returns [(tool, offending text)]."""
    allowed = [norm_path(str(a)).rstrip("/") + "/" for a in allowed_roots]
    user = norm_path(real_home).rstrip("/").split("/")[-1]
    token = re.compile(r"[a-z]:/users/" + re.escape(user) + r"[^\s\"'`;|&<>)]*|/c/users/" + re.escape(user) +
                       r"[^\s\"'`;|&<>)]*|~/[^\s\"'`;|&<>)]*")
    hits = []
    for tool, text in tool_inputs(rows):
        n = norm_path(text)
        for t in token.findall(n):
            if t.startswith("~/"):
                continue  # ~ is the run's own throwaway home
            t = norm_path(t)
            if not any((t + "/").startswith(a) for a in allowed):
                hits.append((tool, t[:160]))
        for name in forbidden:
            if name.lower() in n:
                hits.append((tool, name))
    return hits


def init_facts(rows: list, home: str) -> dict:
    init = next((d for d in rows if d.get("type") == "system" and d.get("subtype") == "init"), {})
    plugins = [p if isinstance(p, str) else (p or {}).get("name") for p in init.get("plugins", [])]
    mem = (init.get("memory_paths") or {}).get("auto") or ""
    denials = [d for d in rows if d.get("type") == "system" and d.get("subtype") == "permission_denied"]
    return {
        "plugins": plugins,
        "other_plugins": [p for p in plugins if p != "ideo-scrum" and not str(p).startswith(BUILTIN_PLUGIN_PREFIX)],
        "ideo_scrum_loaded": "ideo-scrum" in plugins,
        "slash_commands_of_ours": sorted(c for c in init.get("slash_commands", []) if str(c).startswith("ideo-scrum:")),
        "memory_inside_home": bool(mem) and norm_path(mem).startswith(norm_path(home).rstrip("/") + "/"),
        "tools": init.get("tools"),
        "permissionMode": init.get("permissionMode"),
        "model_present": bool(init.get("model")),
        "permission_denials": len(denials),
    }


# ---- stuck signals ------------------------------------------------------------------------------------------
def tool_failure_streak(rows: list) -> int:
    """The longest run of the same tool call failing in a row."""
    calls, best, streak, last = {}, 0, 0, None
    for d in rows:
        content = (d.get("message") or {}).get("content") or []
        if d.get("type") == "assistant":
            for c in content:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    calls[c.get("id")] = (c.get("name"), json.dumps(c.get("input"), sort_keys=True))
        elif d.get("type") == "user":
            for c in content if isinstance(content, list) else []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    sig = calls.get(c.get("tool_use_id"))
                    if c.get("is_error"):
                        streak = streak + 1 if sig == last else 1
                        last = sig
                        best = max(best, streak)
                    else:
                        streak, last = 0, None
    return best


def stuck_signals(convo: list, p_rows: list) -> dict:
    """What the four stuck criteria are read from (63-a); a person reads the rest.
    convo is the driver's list of events: {"round", "who", "kind", "text"}."""
    s_actions = [c for c in convo if c.get("who") == "S"]
    repeats = sum(1 for a, b in zip(s_actions, s_actions[1:]) if a["kind"] == b["kind"] in ("message", "command")
                  and a["text"].strip() == b["text"].strip())
    return {
        "ask_author": sum(1 for c in s_actions if c["kind"] == "ask"),
        "stuck_lines": sum(1 for c in s_actions if c["kind"] == "stuck"),
        "s_repeated_itself": repeats,
        "p_errors": sum(1 for c in convo if c.get("who") == "P" and c.get("kind") == "error"),
        "same_tool_failed_in_a_row": tool_failure_streak(p_rows),
    }


def load_rows(path: pathlib.Path) -> list:
    rows = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8", errors="replace").split("\n"):
            try:
                rows.append(json.loads(line))
            except ValueError:
                pass
    return rows


if __name__ == "__main__":
    sys.exit("verify.py is a module of driver.py")
