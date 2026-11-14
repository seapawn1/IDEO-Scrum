"""A guard for the author's own files: a PreToolUse hook for the plugin session of a stranger test (Sprint 20, PBI-63).

The plugin session runs as the author's own Windows account, so the author's real home folder lies on the same disk
and the session can find it: the Python folder on PATH names it, `ls -la` shows the owner. In the second formal run
the simulated stranger asked for the tool to be installed "in the Windows profile home", and the session installed it
there, with a .bashrc and a .bash_profile that did not exist before, in the author's real home. A stranger's machine
has no second home, so the test bench closes this one: the hook refuses every tool call that names a path under the
author's real home (except the folders of the tools the run uses), and every call that names the author's memory
folder or repository.

    python guard.py CONFIG.json          stdin: the hook's JSON; exit 2 blocks the call, stderr goes to the model

CONFIG.json: {"real_home": "C:\\Users\\name", "allow": ["c:/users/name/appdata/local/programs/python/python313"],
"names": ["seapawn-memory", "s:/ideo-scrum"]}; `allow` and `names` are lower case with forward slashes. Only the
fields that hold a path or a command are read, not the text a tool writes or the prompt it gives a subagent. When the
hook cannot read its input or its config it lets the call through: a broken guard must not stop the run.
"""
import json
import re
import sys

PATH_FIELDS = ("command", "file_path", "path", "notebook_path", "cwd", "pattern")
# what the model reads when a call is refused, and what verify.py counts: it must not say that this is a test, nor
# name anything of the author's (the hook error shows the hook's command line too, so that is kept plain as well)
MARKER = "a place outside this session's folders"


def norm(s: str) -> str:
    """Lower case, forward slashes, and the MSYS form /c/users folded to c:/users."""
    s = s.replace("\\", "/").lower()
    return re.sub(r"(?<![a-z0-9_])/([a-z])/(?=\w)", r"\1:/", s)


def reason(tool_input, cfg) -> str:
    """Why the call must be blocked, or '' when it may go on."""
    user = norm(cfg["real_home"]).rstrip("/").split("/")[-1]
    token = re.compile(r"[a-z]:/users/" + re.escape(user) + r"(?![\w.-])[^\s\"'`;|&<>)]*")
    allow = [a.rstrip("/") for a in cfg.get("allow", [])]
    for field in PATH_FIELDS:
        value = tool_input.get(field) if isinstance(tool_input, dict) else None
        if not isinstance(value, str):
            continue
        n = norm(value)
        for t in token.findall(n):
            if not any(t == a or t.startswith(a + "/") for a in allow):
                return "it names " + t[:80]
        for name in cfg.get("names", []):
            if name in n:
                return "it names " + name
    return ""


def main(argv) -> int:
    try:
        cfg = json.load(open(argv[1], encoding="utf-8"))
        data = json.load(sys.stdin)
        why = reason(data.get("tool_input"), cfg)
    except (OSError, ValueError, KeyError, IndexError):
        return 0
    if why:
        print("Blocked: " + why + ", " + MARKER + ". Use your own home ($HOME) and the project folder instead.",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
