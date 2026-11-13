"""Stranger test driver (Sprint 20, PBI-63). The standard is section 2.2 of that Sprint's log ("63-a"): written and
committed before any run; after the smoke run only the run limits (LIMITS) may be calibrated.

Two claude-magpie sessions and this script between them. S plays a stranger who knows Scrum and has only the README,
the quick start and the glossary; P is Claude Code with the plugin installed, in an empty temporary project. S's
replies go to P as chat input, P's answers go back to S. S's `ASK_AUTHOR:` and `STUCK:` lines are recorded and
answered with "the author is not here". The plugin is installed from the committed state of this repository
(`git archive HEAD`), with the same commands as the README; only the GitHub address is swapped for the local copy.

    python -X utf8 -I scripts/stranger_test/driver.py selftest
    python -X utf8 -I scripts/stranger_test/driver.py run --kind smoke
    python -X utf8 -I scripts/stranger_test/driver.py run --kind formal --n 3 --parallel
    python -X utf8 -I scripts/stranger_test/driver.py run --scripted replies.json     (no S: plumbing only)
    python -X utf8 -I scripts/stranger_test/driver.py verify RUN_DIR                  (check a saved project again)

Raw output goes to --out, outside the repository (default: the archive folder of this Sprint). The channel is
magpie's own `claude run`, which is what `claude-magpie.cmd` runs; it is called directly because the .cmd wrapper
cannot carry a multi-line argument. The environment of both sessions is a whitelist with a throwaway home folder.
"""
import argparse
import concurrent.futures
import datetime
import html.parser
import json
import os
import pathlib
import queue
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
import time
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify  # noqa: E402

REPO = HERE.parents[1]
DEFAULT_OUT = pathlib.Path(r"S:\IDEO-Scrum-Archives\sprint-20-presentable\stranger-test")
README_SOURCES = ("seapawn1/IDEO-Scrum", "https://github.com/seapawn1/IDEO-Scrum", "https://github.com/seapawn1/IDEO-Scrum.git")
PLUGIN_REF = "ideo-scrum@ideo-scrum"
PAGES = ["README.md", "docs/quick-start.md", "docs/glossary.md"]
# The run limits (63-a, "运行的上限"): the one thing that may be calibrated after the smoke run.
LIMITS = {"rounds": 60, "p_message_s": 20 * 60, "run_s": 120 * 60, "s_message_s": 10 * 60}
P_TOOLS = "Read,Write,Edit,Bash,Glob,Grep,Skill,Agent"
MODEL = "haiku"  # magpie maps any model name to its own cheap model
WHITELIST = {"systemroot", "path", "comspec", "pathext", "windir"}
# Names that mark the author's own places (63-a: the memory folder and this repository), plus magpie's settings and
# the variable that points at them; the real ~/.claude, ~/.config and ~/.cache are added by verify.scan_author.
AUTHOR_NAMES = ("seapawn-memory", "ideo-scrum-archives", "s:/ideo-scrum", "sprint-20-presentable",
                "/.config/magpie", "xdg_config_home")


# ---- the sessions -------------------------------------------------------------------------------------------
def magpie_prefix() -> list:
    """The command that starts Claude Code through magpie: what claude-magpie.cmd runs."""
    wrapper = shutil.which("claude-magpie.cmd")
    if wrapper:
        exe = shutil.which("magpie", path=str(pathlib.Path(wrapper).parent))
        if exe:
            return [exe, "claude", "run"]
        return [wrapper]
    sys.exit("claude-magpie.cmd is not on PATH")


def clean_path(path: str, real_home: str, keep: set, isdir=os.path.isdir) -> str:
    """The host's PATH without the author's own folders. A folder is dropped when it does not exist, or when it lies
    under the real home and is not one of `keep` (the folders of the tools the run needs). The smoke runs showed why:
    the plugin session read PATH, saw the author's missing ~/bin and proposed creating it there (first run), and
    installed the little tool into the author's real ~/.local/bin (second run)."""
    home = norm_dir(real_home)
    kept = []
    for entry in path.split(os.pathsep):
        e = entry.strip().strip('"')
        if not e or not isdir(e):
            continue
        n = norm_dir(e)
        if (n == home or n.startswith(home + "/")) and n not in keep:
            continue
        kept.append(e)
    return os.pathsep.join(kept)


def norm_dir(p: str) -> str:
    return p.replace("\\", "/").lower().rstrip("/")


def tool_dirs() -> set:
    """The folders of the tools the plugin session may use (not claude itself: magpie finds that on its own)."""
    return {norm_dir(str(pathlib.Path(w).parent)) for w in
            (shutil.which(t) for t in ("git", "sh", "python", "node", "magpie")) if w}


def make_env(base: pathlib.Path) -> tuple:
    """A whitelist environment with a throwaway home, config dir and temp dir under base. magpie keeps its
    providers under the real ~/.config, so only that is pointed back at the real home. PATH starts with a
    throwaway ~/.local/bin (empty, where a person would put a little tool) and has none of the author's folders."""
    env = {k: v for k, v in os.environ.items() if k.lower() in WHITELIST}
    real_home = os.environ["USERPROFILE"]
    home = base / "home"
    (home / "AppData" / "Roaming").mkdir(parents=True)
    (home / "AppData" / "Local").mkdir(parents=True)
    userbin = home / ".local" / "bin"
    userbin.mkdir(parents=True)
    for k in list(env):
        if k.lower() == "path":
            env[k] = os.pathsep.join([str(userbin), clean_path(env[k], real_home, tool_dirs())])
    tmp = base / "tmp"
    tmp.mkdir()
    gitconfig = base / "gitconfig"
    gitconfig.write_text("", encoding="utf-8")
    drive, tail = os.path.splitdrive(str(home))
    real_home = pathlib.Path(real_home)
    env.update({
        "USERPROFILE": str(home), "HOME": str(home), "HOMEDRIVE": drive, "HOMEPATH": tail,
        "APPDATA": str(home / "AppData" / "Roaming"), "LOCALAPPDATA": str(home / "AppData" / "Local"),
        "TEMP": str(tmp), "TMP": str(tmp), "CLAUDE_CONFIG_DIR": str(home / ".claude"),
        "XDG_CONFIG_HOME": str(real_home / ".config"), "XDG_CACHE_HOME": str(real_home / ".cache"),
        "MSYS_NO_PATHCONV": "1", "GIT_CONFIG_GLOBAL": str(gitconfig), "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "Stranger", "GIT_AUTHOR_EMAIL": "stranger@example.invalid",
        "GIT_COMMITTER_NAME": "Stranger", "GIT_COMMITTER_EMAIL": "stranger@example.invalid",
    })
    sh = shutil.which("sh")
    if sh:
        env["CLAUDE_CODE_GIT_BASH_PATH"] = str(pathlib.Path(sh).with_name("bash.exe"))
    return env, home


def rmtree(path) -> None:
    """Delete a folder tree on Windows, where git leaves read-only files that plain rmtree skips."""
    def force(func, p, *_):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass
    try:
        shutil.rmtree(path, onexc=force)
    except TypeError:  # Python before 3.12
        shutil.rmtree(path, onerror=force)


def kill_tree(proc) -> None:
    if proc.poll() is None:
        subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True)


class Session:
    """One Claude Code process in stream-json mode: send a message, wait for its result."""

    def __init__(self, name: str, cmd: list, cwd: pathlib.Path, env: dict, log: pathlib.Path):
        self.name, self.cmd, self.cwd, self.env, self.log = name, cmd, cwd, env, log
        self.results: queue.Queue = queue.Queue()
        self.proc = None
        self.cost = 0.0

    def start(self) -> None:
        self.cwd.mkdir(parents=True, exist_ok=True)
        self.proc = subprocess.Popen(self.cmd, cwd=str(self.cwd), env=self.env, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = open(self.log, "a", encoding="utf-8", newline="\n")
        err = open(str(self.log) + ".stderr", "a", encoding="utf-8", newline="\n")

        def reader():
            for raw in self.proc.stdout:
                line = raw.decode("utf-8", "replace").rstrip("\r\n")
                out.write(line + "\n")
                out.flush()
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if d.get("type") == "result":  # the stream stays on disk; only the results are kept in memory
                    self.cost += float(d.get("total_cost_usd") or 0)
                    self.results.put(d)
            self.results.put(None)
            out.close()

        def errs():
            for raw in self.proc.stderr:
                err.write(raw.decode("utf-8", "replace"))
                err.flush()
            err.close()

        threading.Thread(target=reader, daemon=True).start()
        threading.Thread(target=errs, daemon=True).start()

    def send(self, text: str, timeout: float) -> dict:
        """{'status': ok | error | timeout | ended, 'text': the answer}."""
        msg = {"type": "user", "message": {"role": "user", "content": text}}
        try:
            self.proc.stdin.write((json.dumps(msg, ensure_ascii=False) + "\n").encode("utf-8"))
            self.proc.stdin.flush()
        except OSError:
            return {"status": "ended", "text": ""}
        try:
            d = self.results.get(timeout=max(1.0, timeout))
        except queue.Empty:
            kill_tree(self.proc)
            return {"status": "timeout", "text": ""}
        if d is None:
            return {"status": "ended", "text": ""}
        return {"status": "error" if d.get("is_error") else "ok", "text": d.get("result") or "",
                "subtype": d.get("subtype")}

    def close(self) -> None:
        try:
            self.proc.stdin.close()
        except (OSError, AttributeError):
            pass
        if self.proc:
            t0 = time.time()
            while self.proc.poll() is None and time.time() - t0 < 60:
                time.sleep(0.5)
            kill_tree(self.proc)


# ---- what the stranger reads and writes ---------------------------------------------------------------------
def parse_reply(text: str) -> dict:
    """One of: empty, ask, stuck, done, commands (leading lines that start with /), message."""
    t = text.strip()
    m = re.fullmatch(r"```[a-zA-Z]*\n(.*?)\n?```", t, re.S)
    if m:
        t = m.group(1).strip()
    if not t:
        return {"kind": "empty", "text": ""}
    first = t.split("\n", 1)[0].strip()
    for prefix, kind in (("ASK_AUTHOR:", "ask"), ("STUCK:", "stuck"), ("DONE:", "done")):
        if first.upper().startswith(prefix):
            return {"kind": kind, "text": t[len(prefix):].strip()}
    lines = [l.strip() for l in t.split("\n") if l.strip()]
    if lines[0].startswith("/"):
        cmds = []
        for l in lines:
            if not l.startswith("/"):
                break
            cmds.append(l)
        return {"kind": "commands", "lines": cmds, "text": "\n".join(cmds), "ignored": "\n".join(lines[len(cmds):])}
    return {"kind": "message", "text": t}


class _Visible(html.parser.HTMLParser):
    SKIP = {"script", "style", "head", "title", "noscript"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.parts: list = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.depth += 1
        elif tag in ("br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "section", "article", "header", "footer"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if not self.depth and data.strip():
            self.parts.append(data.strip() + " ")


def visible_text(page: str) -> str:
    """The text a person would see on the page: no tags, scripts or styles."""
    p = _Visible()
    p.feed(page)
    text = "".join(p.parts)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def is_install_line(line: str) -> bool:
    return bool(re.match(r"/(plugin\b|reload-plugins\b)", line))


# ---- one run ------------------------------------------------------------------------------------------------
class Run:
    def __init__(self, run_id: str, kind: str, out: pathlib.Path, repo: pathlib.Path, limits: dict,
                 scripted=None, keep_temp=False):
        self.id, self.kind, self.repo, self.limits = run_id, kind, repo, dict(limits)
        self.dir = out / run_id
        self.scripted = list(scripted) if scripted is not None else None
        self.keep_temp = keep_temp
        self.convo: list = []
        self.t0 = time.time()
        self.p = None
        self.p_restart = False
        self.p_log = self.dir / "p.jsonl"
        self.board_seen = None
        self.installs: list = []

    # -- setup
    def setup(self) -> None:
        self.dir.mkdir(parents=True, exist_ok=False)
        self.root = pathlib.Path(tempfile.mkdtemp(prefix="st-"))
        self.p_base, self.s_base = self.root / "p", self.root / "s"
        for b in (self.p_base, self.s_base):
            b.mkdir()
        self.p_env, self.p_home = make_env(self.p_base)
        self.s_env, self.s_home = make_env(self.s_base)
        self.proj = self.root / "project"
        self.proj.mkdir()
        self.market = self.root / "market"
        self.market.mkdir()
        z = self.root / "market.zip"
        subprocess.run(["git", "-C", str(self.repo), "archive", "--format=zip", "-o", str(z), "HEAD",
                        ".claude-plugin", "plugins"], check=True)
        with zipfile.ZipFile(z) as f:
            f.extractall(self.market)
        self.pages = {}
        for name in PAGES:
            r = subprocess.run(["git", "-C", str(self.repo), "show", f"HEAD:{name}"], capture_output=True,
                               text=True, encoding="utf-8")
            self.pages[name] = r.stdout
        self.commit = subprocess.run(["git", "-C", str(self.repo), "rev-parse", "HEAD"], capture_output=True,
                                     text=True).stdout.strip()
        self.dirty = bool(subprocess.run(["git", "-C", str(self.repo), "status", "--porcelain", "--", "README.md",
                                          "docs", "plugins", ".claude-plugin"], capture_output=True,
                                         text=True).stdout.strip())
        manifest = json.loads((self.market / "plugins/ideo-scrum/.claude-plugin/plugin.json").read_text("utf-8"))
        self.plugin_version = manifest.get("version")
        (self.dir / "run.json").write_text(json.dumps({
            "commit": self.commit, "dirty_docs_or_plugin": self.dirty, "plugin_version": self.plugin_version,
            "limits": self.limits, "scripted": self.scripted is not None, "temp_root": str(self.root),
            "started": datetime.datetime.now().isoformat(timespec="seconds"), "installs": self.installs,
        }, indent=2), encoding="utf-8")

    def log(self, who: str, kind: str, text: str, **extra) -> None:
        ev = {"t": round(time.time() - self.t0, 1), "round": getattr(self, "round", 0), "who": who, "kind": kind,
              "text": text, **extra}
        self.convo.append(ev)
        with open(self.dir / "conversation.jsonl", "a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")

    # -- the plugin session
    def start_p(self) -> None:
        cmd = magpie_prefix() + ["-p", "--input-format", "stream-json", "--output-format", "stream-json",
                                 "--verbose", "--include-hook-events", "--model", MODEL, "--tools", P_TOOLS,
                                 "--permission-mode", "acceptEdits", "--allowedTools", "Bash",
                                 "--add-dir", str(self.market), "--setting-sources", "user,project,local"]
        self.p = Session("P", cmd, self.proj, self.p_env, self.p_log)
        self.p.start()
        self.p_restart = False

    def install(self, line: str) -> str:
        """The README's install commands, run as their `claude plugin` equivalents in the stranger's own config."""
        m = re.fullmatch(r"/plugin\s+marketplace\s+add\s+(\S+)", line)
        if m:
            if m.group(1) not in README_SOURCES:
                return f"Could not find a marketplace at {m.group(1)}."
            return self.cli(["plugin", "marketplace", "add", str(self.market)])
        m = re.fullmatch(r"/plugin\s+install\s+(\S+)", line)
        if m:
            if m.group(1) != PLUGIN_REF:
                return f"Plugin {m.group(1)} was not found in any marketplace."
            out = self.cli(["plugin", "install", PLUGIN_REF])
            self.p_restart = self.p is not None
            return out
        if re.fullmatch(r"/reload-plugins", line):
            self.p_restart = self.p is not None
            return "Plugins reloaded."
        return "This command is not available here."

    def cli(self, args: list) -> str:
        exe = shutil.which("claude")
        r = subprocess.run([exe] + args, env=self.p_env, cwd=str(self.proj), capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=300, stdin=subprocess.DEVNULL)
        out = (r.stdout + r.stderr).strip()
        self.installs.append({"args": args[:3], "exit": r.returncode})
        self.log("H", "install", out, exit=r.returncode, args=" ".join(args[:3]))
        return out

    def to_p(self, text: str) -> tuple:
        """Send a message or command to P. Returns (what S sees, fatal status or None)."""
        if self.p is None or self.p_restart:
            if self.p is not None:
                self.p.close()
            self.start_p()
            self.log("H", "p_start", "plugin session started")
        left = self.limits["run_s"] - (time.time() - self.t0)
        r = self.p.send(text, min(self.limits["p_message_s"], left))
        if r["status"] == "timeout":
            self.log("P", "timeout", "", seconds=self.limits["p_message_s"])
            return "Claude Code did not answer in time.", "p_timeout"
        if r["status"] == "ended":
            self.log("P", "error", "the session ended")
            return "Claude Code closed.", "p_ended"
        kind = "reply" if r["status"] == "ok" else "error"
        self.log("P", kind, r["text"], subtype=r.get("subtype"))
        seen = r["text"] if r["status"] == "ok" else f"(Claude Code reported an error: {r.get('subtype')})\n{r['text']}"
        board = self.proj / "scrum" / "ScrumBoard.html"
        if board.is_file():
            stat = (board.stat().st_mtime_ns, board.stat().st_size)
            if stat != self.board_seen:
                self.board_seen = stat
                shown = visible_text(board.read_text(encoding="utf-8", errors="replace"))
                self.log("H", "board", shown)
                seen += "\n\n[scrum/ScrumBoard.html now shows this text:]\n" + shown
        return seen, None

    # -- the run
    def ask_s(self, s, text: str):
        if self.scripted is not None:
            return {"status": "ok", "text": self.scripted.pop(0) if self.scripted else "DONE: script ended"}
        left = self.limits["run_s"] - (time.time() - self.t0)
        return s.send(text, min(self.limits["s_message_s"], left))

    def execute(self) -> dict:
        self.setup()
        status = "rounds"
        s = None
        try:
            s_input = "Here are the pages you found about the plugin.\n\n"
            for name, text in self.pages.items():
                s_input += f"=== {name} ===\n{text.strip()}\n\n"
            s_input += "Your task:\n" + (HERE / "task.md").read_text(encoding="utf-8").strip()
            if self.scripted is None:
                system = (HERE / "channel.md").read_text(encoding="utf-8").format(
                    identity=(HERE / "stranger_card.md").read_text(encoding="utf-8").strip())
                cmd = magpie_prefix() + ["-p", "--input-format", "stream-json", "--output-format", "stream-json",
                                         "--verbose", "--model", MODEL, "--tools", "", "--system-prompt", system,
                                         "--setting-sources", "user,project,local"]
                s = Session("S", cmd, self.root / "s-cwd", self.s_env, self.dir / "s.jsonl")
                s.start()
            empties = 0
            for n in range(1, self.limits["rounds"] + 1):
                self.round = n
                if time.time() - self.t0 >= self.limits["run_s"]:
                    status = "run_timeout"
                    break
                reply = self.ask_s(s, s_input)
                if reply["status"] != "ok":
                    status = "s_" + reply["status"]
                    self.log("S", "error", reply.get("text", ""), status=reply["status"])
                    break
                act = parse_reply(reply["text"])
                if act["kind"] == "commands":
                    self.log("S", "command", act["text"], ignored=act.get("ignored", ""))
                else:
                    self.log("S", act["kind"], act["text"])
                if act["kind"] == "done":
                    status = "done"
                    break
                if act["kind"] == "empty":
                    empties += 1
                    if empties >= 3:
                        status = "s_empty"
                        break
                    s_input = "(Your reply was empty.)"
                    continue
                empties = 0
                if act["kind"] in ("ask", "stuck"):
                    s_input = ("The plugin's author is not here. You have only the pages you were given, and what "
                               "Claude Code tells you.")
                    self.log("H", "no_author", s_input)
                    continue
                seen, fatal = [], None
                if act["kind"] == "commands":
                    for i, line in enumerate(act["lines"]):
                        if is_install_line(line):
                            seen.append("The command printed:\n" + self.install(line))
                        else:
                            text, fatal = self.to_p(line)
                            seen.append("Claude Code says:\n" + text)
                            if i + 1 < len(act["lines"]):
                                seen.append("(Only the first of your commands was sent; send one at a time.)")
                            break
                else:
                    text, fatal = self.to_p(act["text"])
                    seen.append("Claude Code says:\n" + text)
                if fatal:
                    status = fatal
                    break
                s_input = "\n\n".join(seen)
        finally:
            if s is not None:
                s.close()
            if self.p is not None:
                self.p.close()
        return self.finish(status, s)

    def finish(self, status: str, s) -> dict:
        """Save the project, evaluate, write result.json and the transcript. An error in the evaluation must not
        cost the raw output: it is recorded, and `driver.py report RUN_DIR` can evaluate again from the saved files."""
        result = {"run": self.id, "kind": self.kind, "status": status, "rounds": getattr(self, "round", 0),
                  "seconds": round(time.time() - self.t0)}
        try:
            shutil.copytree(self.proj, self.dir / "project", dirs_exist_ok=True)
            meta = json.loads((self.dir / "run.json").read_text("utf-8"))
            result.update(meta)
            result.update(evaluate(self.dir / "project", self.p_env, self.root, self.p_home, self.s_home, self.convo,
                                   verify.load_rows(self.p_log), verify.load_rows(self.dir / "s.jsonl"),
                                   self.scripted is not None))
        except Exception as e:  # noqa: BLE001
            result["evaluation_error"] = repr(e)
        (self.dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        write_transcript(self.dir, self.convo)
        if not self.keep_temp:
            rmtree(self.root)
        return result


def evaluate(proj, env, root, p_home, s_home, convo, p_rows, s_rows, scripted) -> dict:
    """The five outputs, the isolation and the stuck signals of a finished run, from what the run saved."""
    real_home = os.environ["USERPROFILE"]
    outputs = verify.check_outputs(pathlib.Path(proj), env)
    author = verify.scan_author(p_rows, real_home, AUTHOR_NAMES)
    leaks = verify.scan_paths(p_rows, [root], real_home, (), ignore=tuple(tool_dirs()))
    p_init, s_init = verify.init_facts(p_rows, str(p_home)), verify.init_facts(s_rows, str(s_home))
    s_ok = scripted or (not s_init["other_plugins"] and s_init["memory_inside_home"] and not s_init["tools"])
    return {
        "concessions": [
            "XDG_CONFIG_HOME and XDG_CACHE_HOME point at the real .config and .cache, only so that magpie can "
            "sign in; any read there counts as touching the author's paths",
            "the plugin is installed with the `claude plugin` equivalents of the README's commands, from a "
            "local copy of the committed state instead of GitHub",
        ],
        "outputs": outputs, "all_outputs": all(v["ok"] for v in outputs.values()),
        # pass line 4 of 63-a: no author path touched, and the stranger's sessions carry nothing of the author's
        "isolation": {"ok": bool(not p_init["other_plugins"] and p_init["memory_inside_home"] and not author and s_ok),
                      "author_paths_touched": author, "p": p_init, "s": s_init},
        # hygiene, beyond the pass line: anything else the plugin session did under the author's real home
        "leaks": leaks,
        "stuck": verify.stuck_signals(convo, p_rows),
        "cost_usd_estimate": {"P": round(verify.session_cost(p_rows), 2), "S": round(verify.session_cost(s_rows), 2)},
    }


def write_transcript(directory: pathlib.Path, convo: list) -> None:
    lines = []
    for e in convo:
        head = f"[{e['t']:>7}s round {e['round']}] {e['who']} {e['kind']}"
        lines.append(head + "\n" + (e["text"] or "").rstrip() + "\n")
    (directory / "transcript.md").write_text("\n".join(lines), encoding="utf-8")


def summary_line(r: dict) -> str:
    head = f"{r['run']}: {r['status']} in {r['rounds']} rounds, {r['seconds']} s"
    if "outputs" not in r:
        return f"{head}; NOT evaluated: {r.get('evaluation_error')}"
    marks = "".join(k[0] if v["ok"] else "." for k, v in sorted(r["outputs"].items()))
    return (f"{head}; outputs {marks} ({'all' if r['all_outputs'] else 'not all'}); "
            f"isolation {'ok' if r['isolation']['ok'] else 'NOT ok'}, leaks {len(r['leaks'])}; "
            f"ask_author {r['stuck']['ask_author']}, stuck {r['stuck']['stuck_lines']}")


# ---- commands -----------------------------------------------------------------------------------------------
def cmd_run(args) -> int:
    out = pathlib.Path(args.out)
    scripted = json.loads(pathlib.Path(args.scripted).read_text("utf-8")) if args.scripted else None
    limits = dict(LIMITS)
    for k in ("rounds", "p_message_s", "run_s", "s_message_s"):
        v = getattr(args, k)
        if v:
            limits[k] = v
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    ids = [f"{args.kind}-{stamp}-{i + 1}" for i in range(args.n)]

    def one(i):
        return Run(i, args.kind, out, pathlib.Path(args.repo), limits, scripted, args.keep_temp).execute()

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.n if args.parallel else 1) as ex:
        for r in ex.map(one, ids):
            results.append(r)
            print(summary_line(r))
    return 0 if all(r["status"] == "done" for r in results) else 1


def cmd_report(args) -> int:
    """Evaluate a saved run again from its files (stream, conversation, project copy): for a run whose evaluation
    failed, or to apply a corrected check. Writes result.json and transcript.md in the run folder."""
    run = pathlib.Path(args.run_dir)
    convo = [json.loads(l) for l in (run / "conversation.jsonl").read_text("utf-8").split("\n") if l.strip()]
    p_rows, s_rows = verify.load_rows(run / "p.jsonl"), verify.load_rows(run / "s.jsonl")
    init = next((d for d in p_rows if d.get("type") == "system" and d.get("subtype") == "init"), None)
    if not init:
        sys.exit("no init event in p.jsonl: the plugin session never started")
    root = pathlib.Path(init["cwd"]).parent  # <temp root>/project
    meta_file = run / "run.json"
    meta = json.loads(meta_file.read_text("utf-8")) if meta_file.is_file() else {}
    for k in ("commit", "plugin_version"):
        if getattr(args, k):
            meta[k] = getattr(args, k)
    env = {k: v for k, v in os.environ.items() if k.lower() in WHITELIST}
    env.update({"GIT_CONFIG_NOSYSTEM": "1"})
    last = convo[-1] if convo else {}
    status = "done" if last.get("who") == "S" and last.get("kind") == "done" else "unknown"
    result = {"run": run.name, "kind": run.name.split("-")[0], "status": status,
              "rounds": max([e.get("round", 0) for e in convo] or [0]), "seconds": round(last.get("t", 0)),
              **meta, "reported_from_saved_files": True}
    result.update(evaluate(run / "project", env, root, root / "p" / "home", root / "s" / "home", convo, p_rows,
                           s_rows, bool(meta.get("scripted"))))
    (run / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_transcript(run, convo)
    print(summary_line(result))
    return 0


def cmd_verify(args) -> int:
    run = pathlib.Path(args.run_dir)
    proj = run / "project"
    env = {k: v for k, v in os.environ.items() if k.lower() in WHITELIST}
    print(json.dumps(verify.check_outputs(proj, env), ensure_ascii=False, indent=2))
    return 0


# ---- the self-test: no model, no network ----------------------------------------------------------------------
def selftest() -> int:
    failures = []

    def expect(label, got, want):
        if got != want:
            failures.append(f"{label}: got {got!r}, wanted {want!r}")

    # parse_reply
    expect("empty", parse_reply("  \n")["kind"], "empty")
    expect("ask", parse_reply("ASK_AUTHOR: which command?")["kind"], "ask")
    expect("stuck", parse_reply("stuck: no idea")["kind"], "stuck")
    expect("done", parse_reply("DONE: all good")["text"], "all good")
    expect("fenced commands", parse_reply("```\n/plugin install a@b\n/reload-plugins\n```")["lines"],
           ["/plugin install a@b", "/reload-plugins"])
    expect("command then prose", parse_reply("/foo\nand some text")["ignored"], "and some text")
    expect("message", parse_reply("I want a tool.")["kind"], "message")
    expect("install line", is_install_line("/plugin marketplace add x/y"), True)
    expect("not install", is_install_line("/ideo-scrum:scrum-master"), False)
    # visible_text
    page = "<html><head><title>t</title><style>p{}</style></head><body><h1>Board</h1><script>x=1</script><p>One <b>thing</b></p></body></html>"
    expect("visible text", visible_text(page), "Board\nOne thing")
    # paths
    real = r"C:\Users\someone"
    root = pathlib.Path(r"C:\Users\someone\AppData\Local\Temp\st-abc")
    rows = [{"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "1", "name": "Bash", "input": {"command": f"ls {root.as_posix()}/market && cat ~/.claude/x"}},
        {"type": "tool_use", "id": "2", "name": "Read", "input": {"file_path": r"C:\Users\someone\.claude\plugins\cache\x"}},
        {"type": "tool_use", "id": "3", "name": "Bash", "input": {"command": "cat /c/users/someone/.config/magpie/a"}},
        {"type": "tool_use", "id": "4", "name": "Bash", "input": {"command": "ls S:/SeaPawn-Memory/memory"}},
    ]}}]
    hits = verify.scan_paths(rows, [root], real)
    expect("hygiene: inside the run is fine", [h for h in hits if "st-abc" in h[1]], [])
    expect("hygiene: the real .claude and .config are caught", len(hits) >= 2, True)
    author = verify.scan_author(rows, real, AUTHOR_NAMES)
    expect("pass line: real .claude, magpie config and memory are caught", len(author) >= 3, True)
    expect("pass line: the run's own folders and ~ are fine",
           [a for a in author if "st-abc" in a[1] or a[1] == "~"], [])
    # XDG_CONFIG_HOME points at the real .config only so that magpie can sign in: anything read there, magpie or
    # not, counts as touching the author's paths
    other = [{"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "5", "name": "Read", "input": {"file_path": r"C:\Users\someone\.config\gh\hosts.yml"}}]}}]
    expect("pass line: another folder of the real .config is caught",
           len(verify.scan_author(other, real, AUTHOR_NAMES)), 1)
    var = [{"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "6", "name": "Bash", "input": {"command": "ls $XDG_CONFIG_HOME/gh"}}]}}]
    expect("pass line: reaching for the XDG variable is caught",
           len(verify.scan_author(var, real, AUTHOR_NAMES)) >= 1, True)
    # the second smoke run: the tool installed into the real ~/.local/bin is a hygiene leak, not a pass-line miss
    installed = [{"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "7", "name": "Bash", "input": {"command": "cp today /c/Users/someone/.local/bin/today"}}]}}]
    expect("hygiene: a file put into the real ~/.local/bin is caught", len(verify.scan_paths(installed, [root], real)), 1)
    expect("pass line: ... but it is not an author path of the standard",
           len(verify.scan_author(installed, real, AUTHOR_NAMES)), 0)
    pyexe = [{"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "8", "name": "Bash", "input": {"command": r"C:\Users\someone\AppData\Local\Programs\Python\Python313\python.exe -V"}}]}}]
    expect("hygiene: the folder of a tool in use is ignored",
           verify.scan_paths(pyexe, [root], real, ignore=(r"C:\Users\someone\AppData\Local\Programs\Python\Python313",)), [])
    # a system event whose `message` is a string must not break the checks (the second smoke run crashed on one)
    mixed = [{"type": "system", "subtype": "x", "message": "plain text"}] + rows
    expect("a string message", verify.tool_failure_streak(mixed), 0)
    expect("a string message in the scan", len(verify.scan_paths(mixed, [root], real)) >= 2, True)
    expect("session cost is the running total's last value",
           verify.session_cost([{"type": "result", "total_cost_usd": 0.2}, {"type": "result", "total_cost_usd": 0.9}]), 0.9)
    # make_env: PATH starts with a throwaway ~/.local/bin and carries no folder of the author's claude
    base = pathlib.Path(tempfile.mkdtemp(prefix="st-selftest-env-"))
    try:
        env, home = make_env(base)
        entries = env["PATH"].split(os.pathsep)
        expect("PATH starts with the throwaway user bin", entries[0], str(home / ".local" / "bin"))
        claude_dir = shutil.which("claude")
        expect("PATH has no folder of the author's claude",
               bool(claude_dir) and norm_dir(str(pathlib.Path(claude_dir).parent)) in [norm_dir(e) for e in entries], False)
    finally:
        rmtree(base)
    # clean_path: the author's missing ~/bin and private tool folders go; system folders and needed tools stay
    base = pathlib.Path(tempfile.mkdtemp(prefix="st-selftest-path-"))
    try:
        home = base / "home"
        for d in ("tools", "other", "bin_exists"):
            (home / d).mkdir(parents=True)
        (base / "system").mkdir()
        joined = os.pathsep.join([str(home / "bin"), str(home / "tools"), str(home / "other"), str(base / "system"),
                                  str(base / "nowhere")])
        cleaned = clean_path(joined, str(home), {norm_dir(str(home / "tools"))})
        expect("clean_path", cleaned.split(os.pathsep), [str(home / "tools"), str(base / "system")])
    finally:
        rmtree(base)
    # a project that passes, then planted defects
    work = pathlib.Path(tempfile.mkdtemp(prefix="st-selftest-"))
    env = {k: v for k, v in os.environ.items() if k.lower() in WHITELIST}
    env.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t",
                "GIT_COMMITTER_EMAIL": "t@example.invalid", "GIT_CONFIG_GLOBAL": str(work / "gc"),
                "GIT_CONFIG_NOSYSTEM": "1"})
    (work / "gc").write_text("", encoding="utf-8")
    try:
        proj = work / "p"
        (proj / "scrum" / "sprint-01-daily").mkdir(parents=True)

        def g(*a):
            subprocess.run(["git", "-C", str(proj), *a], check=True, capture_output=True, env=env)

        g("init", "-q")
        (proj / "scrum/ProductBacklog.md").write_text(
            "| Commitment | Daily Quote: prints one sentence a day. |\n| --- | --- |\n\n"
            "| Commitment | A morning ritual people enjoy. |\n| --- | --- |\n", encoding="utf-8")
        (proj / "quote.py").write_text("print('Carpe diem')\n", encoding="utf-8")
        (proj / "scrum/sprint-01-daily/SprintBacklog.md").write_text(
            "| Commitment | Print one quote, from a list. |\n| --- | --- |\n\nGo-ahead: 2026-11-14, PO.\n",
            encoding="utf-8")
        g("add", "-A")
        g("commit", "-q", "-m", "open the sprint")
        (proj / "scrum/documents/sprint").mkdir(parents=True)
        (proj / "scrum/documents/sprint/sprint-01-daily.md").write_text("Summary. Goal kept.\n", encoding="utf-8")
        (proj / "scrum/sprint-01-daily/SprintBacklog.md").unlink()
        (proj / "scrum/ScrumBoard.html").write_text("<html><body><h1>Board</h1></body></html>", encoding="utf-8")
        g("add", "-A")
        g("commit", "-q", "-m", "close the sprint")
        g("tag", "sprint-01-daily")
        ok = verify.check_outputs(proj, env)
        expect("good project: all five", {k: v["ok"] for k, v in ok.items()},
               {"1_product_log": True, "2_sprint_log": True, "3_tool_runs": True, "4_close": True, "5_board": True})
        (proj / "today").write_text("#!/usr/bin/env python\nprint('Carpe diem')\n", encoding="utf-8")
        (proj / "quote.py").write_text("raise SystemExit(1)\n", encoding="utf-8")
        expect("a script without a suffix, run by its shebang", verify.check_outputs(proj, env)["3_tool_runs"]["ok"],
               True)
        # a sh/Python polyglot that fails under sh when it is not an installed command, but runs under python
        (proj / "today").write_text(
            "#!/bin/sh\n''''exec python \"$(cygpath -w \"$(command -v -- \"$0\")\")\" \"$@\" # '''\nprint('Carpe diem')\n",
            encoding="utf-8")
        expect("a polyglot script is tried with the other interpreters",
               verify.check_outputs(proj, env)["3_tool_runs"]["ok"], True)
        (proj / "today").unlink()
        expect("a failing tool", verify.check_outputs(proj, env)["3_tool_runs"]["ok"], False)
        g("tag", "-d", "sprint-01-daily")
        expect("no tag", verify.check_outputs(proj, env)["4_close"]["ok"], False)
        (proj / "scrum/ProductBacklog.md").write_text("| Commitment | <product> |\n| --- | --- |\n", encoding="utf-8")
        expect("placeholder commitments", verify.check_outputs(proj, env)["1_product_log"]["ok"], False)
        (proj / "scrum/ScrumBoard.html").unlink()
        expect("no board", verify.check_outputs(proj, env)["5_board"]["ok"], False)
    finally:
        rmtree(work)
    # stuck signals
    rows = [
        {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "a", "name": "Bash", "input": {"c": 1}}]}},
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "a", "is_error": True}]}},
        {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "b", "name": "Bash", "input": {"c": 1}}]}},
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "b", "is_error": True}]}},
        {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "c", "name": "Bash", "input": {"c": 1}}]}},
        {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "c", "is_error": True}]}},
    ]
    expect("three failures in a row", verify.tool_failure_streak(rows), 3)
    convo = [{"who": "S", "kind": "message", "text": "go"}, {"who": "S", "kind": "message", "text": "go"},
             {"who": "S", "kind": "ask", "text": "?"}, {"who": "P", "kind": "error", "text": ""}]
    sig = verify.stuck_signals(convo, rows)
    expect("stuck signals", (sig["ask_author"], sig["s_repeated_itself"], sig["p_errors"]), (1, 1, 1))
    # init facts
    init = {"type": "system", "subtype": "init", "plugins": ["ideo-scrum", "cc-plugin-x", "seapawn"],
            "memory_paths": {"auto": r"C:\x\home\.claude\projects\p\memory"}, "tools": ["Bash"]}
    facts = verify.init_facts([init], r"C:\x\home")
    expect("init facts", (facts["other_plugins"], facts["memory_inside_home"]), (["seapawn"], True))
    print(json.dumps({"selftest": "failed" if failures else "ok", "failures": failures}, indent=2))
    return 1 if failures else 0


def main(argv) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--kind", choices=["smoke", "formal"], default="smoke")
    r.add_argument("--n", type=int, default=1)
    r.add_argument("--parallel", action="store_true")
    r.add_argument("--out", default=str(DEFAULT_OUT))
    r.add_argument("--repo", default=str(REPO))
    r.add_argument("--scripted", help="a JSON list of the stranger's replies, instead of the model")
    r.add_argument("--keep-temp", action="store_true")
    for k in ("rounds", "p_message_s", "run_s", "s_message_s"):
        r.add_argument("--" + k.replace("_", "-"), dest=k, type=int, default=0)
    v = sub.add_parser("verify")
    v.add_argument("run_dir")
    rp = sub.add_parser("report")
    rp.add_argument("run_dir")
    rp.add_argument("--commit", default="")
    rp.add_argument("--plugin-version", dest="plugin_version", default="")
    sub.add_parser("selftest")
    args = ap.parse_args(argv)
    if args.cmd == "selftest":
        return selftest()
    if args.cmd == "verify":
        return cmd_verify(args)
    if args.cmd == "report":
        return cmd_report(args)
    return cmd_run(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
