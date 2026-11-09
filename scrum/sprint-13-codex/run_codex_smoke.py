#!/usr/bin/env python3
"""Run the five reviewed prompts in an isolated Codex install."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import tomllib


ROOT = Path(__file__).resolve().parents[2]
RESULTS = Path(__file__).resolve().parent / "results"
ROLES = {"R1": "scrum-master", "R2": "designer", "R3": "developer", "R4": "stakeholder", "S1": "developer"}
SENSITIVE = re.compile(r"key|token|secret|password|credential", re.I)
SECRET_SHAPES = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?i)\bBearer[ \t]+[A-Za-z0-9._~+/-]{16,}={0,2}"),
)


def secret_values(value: object, sensitive: bool = False) -> list[str]:
    if isinstance(value, dict):
        return [s for k, v in value.items() for s in secret_values(v, sensitive or bool(SENSITIVE.search(k)))]
    if isinstance(value, list):
        return [s for v in value for s in secret_values(v, sensitive)]
    return [value] if sensitive and isinstance(value, str) and len(value) >= 8 else []


def scrub(value: str, secrets: list[str]) -> tuple[str, int]:
    redactions = 0
    for secret in sorted(set(secrets), key=len, reverse=True):
        for form in {secret, json.dumps(secret)[1:-1]}:
            redactions += value.count(form)
            value = value.replace(form, "[REDACTED]")
    for pattern in SECRET_SHAPES:
        value, count = pattern.subn("[REDACTED]", value)
        redactions += count
    return value, redactions


def save(path: Path, value: str, secrets: list[str]) -> int:
    cleaned, redactions = scrub(value, secrets)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(cleaned, encoding="utf-8")
    return redactions


def toml_scalar(value: object) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(map(toml_scalar, value)) + "]"
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{json.dumps(k)} = {toml_scalar(v)}" for k, v in value.items()) + " }"
    raise ValueError("Unsupported provider setting type")


def source_settings() -> tuple[Path, dict, str, dict, list[str]]:
    user_directory = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).resolve()
    config = tomllib.loads((user_directory / "config.toml").read_text(encoding="utf-8-sig"))
    provider_id = config["model_provider"]
    provider = config["model_providers"][provider_id]
    secrets = secret_values(provider)
    auth = user_directory / "auth.json"
    if auth.is_file():
        secrets.extend(secret_values(json.loads(auth.read_text(encoding="utf-8-sig")), True))
    return user_directory, config, provider_id, provider, secrets


def snapshot(user_directory: Path) -> dict[str, str]:
    files = [user_directory / "config.toml", user_directory / "auth.json"]
    plugins = user_directory / "plugins"
    if plugins.is_dir():
        files.extend(p for p in plugins.iterdir() if p.is_file())
    installed = plugins / "cache/ideo-scrum/ideo-scrum/3.2.0"
    if installed.is_dir():
        files.extend(p for p in installed.rglob("*") if p.is_file())
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file()}


def setup_home(source: Path, target: Path, provider_id: str, provider: dict) -> None:
    target.mkdir()
    top = {
        "model_provider": provider_id,
        "model": "gpt-6-luna",
        "model_reasoning_effort": "low",
        "approval_policy": "never",
        "sandbox_mode": "read-only",
        "cli_auth_credentials_store": "file",
    }
    config = "\n".join(f"{key} = {toml_scalar(value)}" for key, value in top.items())
    config += "\n\n[model_providers." + json.dumps(provider_id) + "]\n"
    config += "\n".join(f"{json.dumps(key)} = {toml_scalar(value)}" for key, value in provider.items()) + "\n"
    (target / "config.toml").write_text(config, encoding="utf-8")
    if (source / "auth.json").is_file():
        shutil.copy2(source / "auth.json", target / "auth.json")
    if (source / "models_cache.json").is_file():
        shutil.copy2(source / "models_cache.json", target / "models_cache.json")


def fixture(path: Path) -> None:
    (path / "scrum/documents").mkdir(parents=True)
    (path / "scrum/ProductBacklog.md").write_text(
        "# Product Backlog\n\n## 1. Product\n\n"
        "IDEO-Scrum provides design thinking and Scrum guidance as a plugin.\n\n"
        "### Product Goal\n\nHelp new users complete their first Sprint without asking the author for help.\n\n"
        "### Definition of Done\n\nSource fidelity; references within two hops of SKILL.md; no broken local links.\n\n"
        "## 2. Stakeholders and architecture\n\n"
        "| Role | Who | Wants | Satisfaction | Can see | When |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        "| 陌生人 | First-time solo developer who knows Codex and has not used this plugin | Know the first thing to say | Complete a first Sprint without asking the author | Plugin and README | Onboarding feedback |\n\n"
        "Install plugin -> describe project -> plan Sprint -> build -> review.\n\n"
        "## 3. Items\n\n"
        "| # | Title | User story | Place | Status | Size | Notes |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        "| PBI-001 | 新用户上手说明 | 作为陌生人，我想知道安装后第一句话说什么，以便开始第一个冲刺 | Onboarding | Waiting | S | Add a short getting-started guide |\n",
        encoding="utf-8",
    )
    (path / "scrum/documents/sprint-12-previous.md").write_text(
        "# Sprint 12\n\nGoal met; review and retrospective complete. No Sprint is in progress.\n",
        encoding="utf-8",
    )
    shutil.copy2(ROOT / "README.md", path / "README.md")
    shutil.copytree(ROOT / "codex/plugins/ideo-scrum", path / "plugin")
    subprocess.run(["git", "init", "--quiet", "-b", "sprint-13-codex"], cwd=path, check=True, capture_output=True)


def prompts() -> dict[str, str]:
    log = (Path(__file__).parent / "SprintBacklog.md").read_text(encoding="utf-8-sig")
    cases = dict(re.findall(r"(?m)^\| (R[1-4]|S1) \| `([^`]+)` \|", log))
    if set(cases) != set(ROLES):
        raise ValueError("The five reviewed prompts were not found in the log")
    return cases


def cli(executable: str, args: list[str], env: dict, cwd: Path, prompt: str | None = None, timeout: int = 180) -> subprocess.CompletedProcess:
    return subprocess.run(
        [executable, "--no-daemon", *args],
        cwd=cwd, env=env, input=prompt,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8",
        errors="replace", timeout=timeout,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
    )


def audit_outputs(secrets: list[str]) -> dict:
    checked = 0
    for path in RESULTS.rglob("*"):
        if not path.is_file():
            continue
        cleaned, hits = scrub(path.read_text(encoding="utf-8-sig"), secrets)
        if hits:
            raise ValueError(f"Credential pattern found in saved output: {path.name}")
        checked += 1
    return {"files_checked": checked, "credential_matches": 0}


def cleanup_test_directory(directory: Path) -> None:
    system_temp = Path(tempfile.gettempdir()).resolve()
    directory = directory.resolve()
    if directory.parent != system_temp or not directory.name.startswith("ideo-codex-"):
        raise ValueError("Refusing to remove a directory outside this task's temporary area")
    for name in ("config.toml", "auth.json"):
        credential = directory / "codex-user" / name
        if credential.exists():
            if not credential.resolve().is_relative_to(directory):
                raise ValueError("Credential path escaped the temporary directory")
            credential.unlink()
    if directory.exists():
        # Codex's bundled plugins can exceed Windows' traditional MAX_PATH.
        extended = "\\\\?\\" + str(directory) if os.name == "nt" else str(directory)
        def writable(function, path, exception):
            os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            function(path)
        shutil.rmtree(extended, onexc=writable)


@contextmanager
def test_directory():
    directory = Path(tempfile.mkdtemp(prefix="ideo-codex-smoke-")).resolve()
    try:
        yield directory
    finally:
        cleanup_test_directory(directory)


def run() -> dict:
    executable = shutil.which("codex")
    if not executable:
        raise RuntimeError("Codex CLI not found")
    user_directory, _, provider_id, provider, secrets = source_settings()
    before = snapshot(user_directory)
    report = {"model": "gpt-6-luna", "reasoning_effort": "low", "cases": {}}
    RESULTS.mkdir(exist_ok=True)
    if any((RESULTS / f"{case}.jsonl").exists() for case in ROLES):
        raise RuntimeError("Results already exist; reviewed tests must not silently rerun")
    temporary_root: Path | None = None
    try:
        with test_directory() as directory:
            temporary_root = Path(directory).resolve()
            if not temporary_root.is_relative_to(Path(tempfile.gettempdir()).resolve()):
                raise ValueError("Test directory escaped the system temporary directory")
            home = temporary_root / "codex-user"
            setup_home(user_directory, home, provider_id, provider)
            environment = os.environ.copy()
            environment["CODEX_HOME"] = str(home)
            marketplace = temporary_root / "marketplace"
            (marketplace / ".agents/plugins").mkdir(parents=True)
            (marketplace / "codex/plugins").mkdir(parents=True)
            shutil.copy2(ROOT / ".agents/plugins/marketplace.json", marketplace / ".agents/plugins/marketplace.json")
            shutil.copytree(ROOT / "codex/plugins/ideo-scrum", marketplace / "codex/plugins/ideo-scrum")
            for label, command in (
                ("marketplace", ["plugin", "marketplace", "add", str(marketplace), "--json"]),
                ("install", ["plugin", "add", "ideo-scrum@ideo-scrum", "--json"]),
            ):
                result = cli(executable, command, environment, temporary_root)
                save(RESULTS / f"{label}.json", result.stdout, secrets)
                save(RESULTS / f"{label}.stderr.txt", result.stderr, secrets)
                if result.returncode:
                    raise RuntimeError(f"Isolated {label} failed; see sanitized output")
            for case, prompt in prompts().items():
                project = temporary_root / case
                fixture(project)
                existing = set((home / "sessions").rglob("*.jsonl"))
                print(f"Running {case} with gpt-6-luna (one attempt)", flush=True)
                result = cli(
                    executable,
                    ["exec", "--json", "--skip-git-repo-check", "-m", "gpt-6-luna", "-C", str(project), "-"],
                    environment, project, prompt + "\n",
                )
                redactions = save(RESULTS / f"{case}.jsonl", result.stdout, secrets)
                redactions += save(RESULTS / f"{case}.stderr.txt", result.stderr, secrets)
                save(RESULTS / f"{case}.input.txt", prompt + "\n", secrets)
                rollouts = sorted(set((home / "sessions").rglob("*.jsonl")) - existing)
                for index, rollout in enumerate(rollouts):
                    redactions += save(RESULTS / f"{case}.rollout-{index}.jsonl", rollout.read_text(encoding="utf-8"), secrets)
                report["cases"][case] = {
                    "role": ROLES[case], "exit_code": result.returncode,
                    "redactions": redactions, "rollouts": len(rollouts),
                    "assessment": "Pending review of loading and file-read evidence",
                }
                print(f"Finished {case}: exit {result.returncode}", flush=True)
                provider_error = result.stdout + result.stderr
                if result.returncode and any(
                    marker in provider_error for marker in (
                        "401 Unauthorized", "403 Forbidden", "503 Service Unavailable", "No available channel"
                    )
                ):
                    raise RuntimeError("Provider unavailable; remaining prompts not attempted")
    finally:
        report["temporary_directory_removed"] = temporary_root is None or not temporary_root.exists()
        report["current_install_unchanged"] = snapshot(user_directory) == before
        report["secret_scan"] = audit_outputs(secrets)
        save(RESULTS / "smoke-summary.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n", secrets)
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    if args.audit_only:
        print(json.dumps(audit_outputs(source_settings()[-1]), ensure_ascii=False))
    else:
        print(json.dumps(run(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
