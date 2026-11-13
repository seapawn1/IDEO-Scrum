#!/usr/bin/env python3
"""Generate the Codex distribution from the unchanged Claude Code sources."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


KERNELS = ("ideo-kernel", "scrum-kernel", "sprint-kernel", "design-kernel")
ROLES = ("developer", "designer", "scrum-master", "stakeholder")
LOAD_SENTENCE = (
    "**Load the kernels first**: before anything else, invoke the `ideo-scrum:ideo-kernel` skill and then the "
    "`ideo-scrum:scrum-kernel` skill with the Skill tool, skipping any that is already loaded in this conversation. "
    "Load the `ideo-scrum:sprint-kernel` skill when the work involves a Sprint — opening, running, resuming, or "
    "closing one — and the `ideo-scrum:design-kernel` skill when it involves a design sprint. Subagents you dispatch "
    "load the ideo-kernel and scrum-kernel skills too."
)
CODEX_LOAD = (
    "**Load the kernels first**: before anything else, read `../ideo-kernel/SKILL.md` and then "
    "`../scrum-kernel/SKILL.md`, relative to this skill's folder, skipping any that are already loaded. "
    "Read `../sprint-kernel/SKILL.md` when the work involves a Sprint — opening, running, resuming, or closing "
    "one — and `../design-kernel/SKILL.md` when it involves a design sprint. Subagents you dispatch read the "
    "ideo-kernel and scrum-kernel skills too."
)
DESIGN_LOAD = (
    "1. If the ideo-kernel skill is not loaded yet, invoke "
    "`ideo-scrum:ideo-kernel` first — every stage stands on it.",
    "1. If the ideo-kernel skill is not loaded yet, read "
    "`../ideo-kernel/SKILL.md` first, relative to this skill's folder "
    "— every stage stands on it.",
)
PACKAGE = Path("codex/plugins/ideo-scrum")
MARKETPLACE = Path(".agents/plugins/marketplace.json")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def replace_once(data: bytes, old: str, new: str, label: str) -> bytes:
    before = old.encode("utf-8")
    if data.count(before) != 1:
        raise ValueError(f"{label}: expected the approved tool sentence exactly once")
    return data.replace(before, new.encode("utf-8"), 1)


def role_skill(command: bytes, role: str) -> bytes:
    newline = b"\r\n" if command.startswith(b"---\r\n") else b"\n"
    if not command.startswith(b"---" + newline):
        raise ValueError(f"{role}: command has no YAML frontmatter")
    converted = replace_once(command, LOAD_SENTENCE, CODEX_LOAD, role)
    return converted.replace(
        b"---" + newline,
        b"---" + newline + f"name: {role}".encode("utf-8") + newline,
        1,
    )


def expected_files(root: Path) -> tuple[dict[Path, bytes], bytes]:
    source = root / "plugins/ideo-scrum"
    files: dict[Path, bytes] = {}
    for kernel in KERNELS:
        directory = source / "skills" / kernel
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Symlink is not a distributable source: {path}")
            if not path.is_file():
                continue
            relative = path.relative_to(source)
            data = path.read_bytes()
            if relative == Path("skills/design-kernel/SKILL.md"):
                data = replace_once(data, *DESIGN_LOAD, "design-kernel")
            files[relative] = data

    # The plugin's hooks (hooks/hooks.json and the scripts it runs) go over unchanged: Codex looks for
    # hooks/hooks.json in the plugin root, and sets CLAUDE_PLUGIN_ROOT as Claude Code does.
    hooks = source / "hooks"
    if hooks.is_dir():
        for path in sorted(hooks.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Symlink is not a distributable source: {path}")
            if path.is_file():
                files[path.relative_to(source)] = path.read_bytes()

    interface_path = root / "scripts/codex_interface.json"
    # Display copy is added only after the Master approves its full text.
    interface = (
        json.loads(interface_path.read_text(encoding="utf-8"))
        if interface_path.is_file() else {}
    )
    for role in ROLES:
        files[Path(f"skills/{role}/SKILL.md")] = role_skill(
            (source / f"commands/{role}.md").read_bytes(), role
        )
        metadata = ""
        if role in interface.get("roles", {}):
            metadata = "interface:\n"
            for key, value in interface["roles"][role].items():
                metadata += f"  {key}: {json.dumps(value, ensure_ascii=False)}\n"
        metadata += "policy:\n  allow_implicit_invocation: false\n"
        files[Path(f"skills/{role}/agents/openai.yaml")] = metadata.encode("utf-8")

    manifest = json.loads(
        (source / ".claude-plugin/plugin.json").read_text(encoding="utf-8-sig")
    )
    manifest["skills"] = "./skills/"
    # The Claude plugin's `icon` names a file in the Claude plugin; the Codex package does not carry it
    # (Sprint 20, Master 2026-11-14), so the field would point at nothing.
    manifest.pop("icon", None)
    if "plugin" in interface:
        manifest["interface"] = interface["plugin"]
    files[Path(".codex-plugin/plugin.json")] = json_bytes(manifest)
    for name in ("LICENSE", "ATTRIBUTION.md"):
        files[Path(name)] = (root / name).read_bytes()
    readme = root / "scripts/codex_readme.md"
    if readme.is_file():
        files[Path("README.md")] = readme.read_bytes().replace(
            b"{{version}}", manifest["version"].encode("utf-8")
        )

    marketplace = {
        "name": manifest["name"],
        "plugins": [{
            "name": manifest["name"],
            "source": {"source": "local", "path": "./" + PACKAGE.as_posix()},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Productivity",
        }],
    }
    return files, json_bytes(marketplace)


def write_if_changed(path: Path, data: bytes) -> bool:
    if path.is_symlink():
        raise ValueError(f"Refusing to overwrite a symlink: {path}")
    if path.is_file() and path.read_bytes().replace(b"\r\n", b"\n") == data.replace(b"\r\n", b"\n"):
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def generate(root: Path) -> tuple[int, int]:
    root = root.resolve(strict=True)
    package = root / PACKAGE
    if package.is_symlink() or not package.resolve().is_relative_to(root):
        raise ValueError("The generated package must stay inside the repository")
    expected, marketplace = expected_files(root)
    changed = removed = 0
    # Inspect every resolved target before removing any generated file.
    existing = sorted(package.rglob("*")) if package.exists() else []
    for path in existing:
        if path.is_symlink() or not path.resolve().is_relative_to(package.resolve()):
            raise ValueError(f"Unsafe generated target: {path}")
    for path in existing:
        if path.is_file() and path.relative_to(package) not in expected:
            path.unlink()
            removed += 1
    for path in sorted(existing, key=lambda p: len(p.parts), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    for relative, data in expected.items():
        changed += write_if_changed(package / relative, data)
    changed += write_if_changed(root / MARKETPLACE, marketplace)
    return changed, removed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    changed, removed = generate(args.root)
    print(json.dumps({"written": changed, "removed": removed}, ensure_ascii=False))


if __name__ == "__main__":
    main()
