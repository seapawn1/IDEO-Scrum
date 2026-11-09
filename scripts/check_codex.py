#!/usr/bin/env python3
"""Check Codex content parity, local links, navigation, and repeatable generation."""

from __future__ import annotations

import argparse
from collections import Counter, deque
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote, urlsplit

import yaml


KERNELS = ("ideo-kernel", "scrum-kernel", "design-kernel")
ROLES = {
    "developer": ("ideo-kernel", "scrum-kernel"),
    "designer": ("ideo-kernel", "design-kernel"),
    "scrum-master": KERNELS,
    "stakeholder": ("ideo-kernel",),
}
PACKAGE = Path("codex/plugins/ideo-scrum")


def text(path: Path) -> str:
    return path.read_bytes().decode("utf-8-sig").replace("\r\n", "\n")


def frontmatter(value: str) -> tuple[dict, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", value, re.S)
    if not match:
        raise ValueError("Missing frontmatter")
    return yaml.safe_load(match[1]), value[match.end():]


def approved_body(source: str, target: str, kernels: tuple[str, ...]) -> bool:
    original = source.splitlines(keepends=True)
    generated = target.splitlines(keepends=True)
    prefix = "**Load the kernel"
    a = [i for i, line in enumerate(original) if line.startswith(prefix)]
    b = [i for i, line in enumerate(generated) if line.startswith(prefix)]
    if len(a) != 1 or a != b:
        return False
    line = generated[b[0]]
    paths = [f"`../{kernel}/SKILL.md`" for kernel in kernels]
    if len(paths) == 1:
        expected = (
            "**Load the kernel first**: before anything else, read "
            f"{paths[0]}, relative to this skill's folder, unless it is already "
            "loaded in this conversation.\n"
        )
    else:
        target = f"{paths[0]} and then {paths[1]}" if len(paths) == 2 else ", then ".join(paths)
        expected = (
            "**Load the kernels first**: before anything else, read "
            f"{target}, resolving these paths relative to this skill's folder, "
            "skipping any that is already loaded in this conversation.\n"
        )
    if line != expected:
        return False
    original[a[0]] = generated[b[0]] = "<approved loader>\n"
    return original == generated


def content_errors(root: Path) -> tuple[list[str], dict]:
    package = root / PACKAGE
    source = root / "plugins/ideo-scrum"
    errors: list[str] = []
    interface_path = root / "scripts/codex_interface.json"
    approved_interface = json.loads(text(interface_path)) if interface_path.is_file() else {}
    kernel_paths = {
        path.relative_to(source)
        for kernel in KERNELS
        for path in (source / "skills" / kernel).rglob("*")
        if path.is_file()
    }
    expected = kernel_paths | {
        Path(f"skills/{role}/{name}")
        for role in ROLES for name in ("SKILL.md", "agents/openai.yaml")
    } | {Path(".codex-plugin/plugin.json"), Path("LICENSE"), Path("ATTRIBUTION.md")}
    if (root / "scripts/codex_readme.md").is_file():
        expected.add(Path("README.md"))
    actual = {p.relative_to(package) for p in package.rglob("*") if p.is_file()}
    errors += [f"missing: {p.as_posix()}" for p in sorted(expected - actual)]
    errors += [f"extra: {p.as_posix()}" for p in sorted(actual - expected)]
    for relative in sorted(kernel_paths & actual):
        before, after = source / relative, package / relative
        if relative == Path("skills/design-kernel/SKILL.md"):
            a, b = text(before), text(after)
            old = (
                "1. If the ideo-kernel skill is not loaded yet, invoke "
                "`ideo-scrum:ideo-kernel` first — every stage stands on it."
            )
            new = (
                "1. If the ideo-kernel skill is not loaded yet, read "
                "`../ideo-kernel/SKILL.md` first, relative to this skill's folder "
                "— every stage stands on it."
            )
            if a.count(old) != 1 or b.count(new) != 1 or a.replace(old, "") != b.replace(new, ""):
                errors.append(f"unapproved difference: {relative}")
        elif before.read_bytes() != after.read_bytes():
            errors.append(f"unapproved difference: {relative}")
    for role, kernels in ROLES.items():
        target = package / f"skills/{role}/SKILL.md"
        if not target.is_file():
            continue
        before_meta, before_body = frontmatter(text(source / f"commands/{role}.md"))
        after_meta, after_body = frontmatter(text(target))
        if after_meta != {"name": role, **before_meta}:
            errors.append(f"role frontmatter: {role}")
        if not approved_body(before_body, after_body, kernels):
            errors.append(f"role body: {role}")
        policy_path = package / f"skills/{role}/agents/openai.yaml"
        if policy_path.is_file():
            policy = yaml.safe_load(text(policy_path))
            expected_metadata = {"policy": {"allow_implicit_invocation": False}}
            if role in approved_interface.get("roles", {}):
                expected_metadata["interface"] = approved_interface["roles"][role]
            if policy != expected_metadata:
                errors.append(f"role invocation policy: {role}")

    if (package / ".codex-plugin/plugin.json").is_file():
        manifest = json.loads(text(package / ".codex-plugin/plugin.json"))
        original = json.loads(text(source / ".claude-plugin/plugin.json"))
        if {k: v for k, v in manifest.items() if k != "interface"} != {**original, "skills": "./skills/"}:
            errors.append("manifest differs from source metadata")
        if manifest.get("interface") != approved_interface.get("plugin"):
            errors.append("manifest display copy differs from approved copy")
    for name in ("LICENSE", "ATTRIBUTION.md"):
        if (package / name).is_file() and (root / name).read_bytes() != (package / name).read_bytes():
            errors.append(f"attribution copy differs: {name}")
    marketplace_path = root / ".agents/plugins/marketplace.json"
    if not marketplace_path.is_file():
        errors.append("missing Codex marketplace")
    else:
        market = json.loads(text(marketplace_path))
        entries = market.get("plugins", [])
        if len(entries) != 1 or entries[0].get("source") != {
            "source": "local", "path": "./codex/plugins/ideo-scrum"
        }:
            errors.append("Codex marketplace points to the wrong package")
    return errors, {"kernel_files": len(kernel_paths), "roles": len(ROLES), "package_files": len(actual)}


def without_fences(value: str) -> str:
    return re.sub(r"(?m)^([ `]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$", "", value, flags=re.S)


def anchors(value: str) -> set[str]:
    found: set[str] = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', value))
    counts: Counter = Counter()
    for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)(?:\s+#+)?$", without_fences(value)):
        title = re.sub(r"<[^>]+>", "", match[1]).replace("`", "").strip().lower()
        slug = "".join(
            char for char in title
            if char in "_- " or unicodedata.category(char)[0] not in "PS"
        ).replace(" ", "-")
        found.add(slug if not counts[slug] else f"{slug}-{counts[slug]}")
        counts[slug] += 1
    return found


def local_links(value: str) -> list[str]:
    value = without_fences(value)
    destinations = []
    for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s]+?)(?:\s+[\"'][^\n]*?[\"'])?\s*\)", value):
        destinations.append(match[1].strip("<>"))
    definitions = {
        key.casefold(): target.strip("<>")
        for key, target in re.findall(r"(?m)^ {0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", value)
    }
    for label, reference in re.findall(r"!?\[([^\]]+)\]\[([^\]]*)\]", value):
        key = (reference or label).casefold()
        destinations.append(definitions.get(key, f"__undefined_reference__/{key}"))
    # A reference definition is itself a destination worth checking.
    destinations.extend(definitions.values())
    return destinations


def link_errors(package: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0
    for path in sorted(package.rglob("*.md")):
        for raw in local_links(text(path)):
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            checked += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            label = f"{path.relative_to(package).as_posix()} -> {raw}"
            if not target.is_relative_to(package.resolve()) or not target.exists():
                errors.append(label)
            elif url.fragment and target.suffix.lower() == ".md" and unquote(url.fragment) not in anchors(text(target)):
                errors.append(label + " (missing anchor)")
    return errors, checked


def navigation_errors(package: Path) -> tuple[list[str], int]:
    errors = []
    resources = 0
    for kernel in KERNELS:
        skill = package / "skills" / kernel
        entry = skill / "SKILL.md"
        queue = deque([(entry, 0)])
        reachable = {entry}
        while queue:
            document, distance = queue.popleft()
            if distance == 2:
                continue
            candidates = re.findall(r"`([^`\n]+\.md)`", text(document))
            candidates.extend(local_links(text(document)))
            for candidate in candidates:
                if urlsplit(candidate).scheme:
                    continue
                filename = unquote(candidate.split("#")[0])
                for base in (document.parent, skill):
                    target = (base / filename).resolve()
                    if target.is_relative_to(package.resolve()) and target.is_file() and target not in reachable:
                        reachable.add(target)
                        queue.append((target, distance + 1))
                        break
        required = {p.resolve() for p in skill.rglob("*.md")} - {entry.resolve()}
        resources += len(required)
        errors += [str(p.relative_to(package.resolve())) for p in sorted(required - {p.resolve() for p in reachable})]
    return errors, resources


def self_test(root: Path) -> dict:
    with tempfile.TemporaryDirectory(prefix="ideo-codex-check-") as directory:
        fixture = Path(directory).resolve()
        if not fixture.is_relative_to(Path(tempfile.gettempdir()).resolve()):
            raise ValueError("Self-test directory escaped the system temporary directory")
        for folder in ("plugins", "codex", ".agents"):
            shutil.copytree(root / folder, fixture / folder)
        for name in ("LICENSE", "ATTRIBUTION.md"):
            shutil.copy2(root / name, fixture / name)
        if (root / "scripts").is_dir():
            (fixture / "scripts").mkdir()
            for name in ("codex_interface.json", "codex_readme.md"):
                if (root / "scripts" / name).is_file():
                    shutil.copy2(root / "scripts" / name, fixture / "scripts" / name)
        baseline, _ = content_errors(fixture)
        if baseline:
            raise AssertionError("The known-good content sample failed")
        sample = fixture / PACKAGE / "skills/scrum-kernel/overview.md"
        saved = sample.read_bytes()
        sample.unlink()
        assert any("missing:" in e for e in content_errors(fixture)[0])
        sample.write_bytes(saved + b"\nUnexpected prose.\n")
        assert any("unapproved difference:" in e for e in content_errors(fixture)[0])
        sample.write_bytes(saved)
        links = fixture / PACKAGE / "checker-sample.md"
        links.write_text("# Good\n\n[ok](#good)\n[license][ref]\n\n[ref]: LICENSE\n", encoding="utf-8")
        assert not link_errors(fixture / PACKAGE)[0]
        links.write_text("[bad](missing.md)\n[bad anchor](checker-sample.md#absent)\n", encoding="utf-8")
        assert len(link_errors(fixture / PACKAGE)[0]) == 2
    return {"known_good": True, "missing_file_detected": True, "changed_body_detected": True, "broken_links_detected": True}


def idempotency(root: Path) -> dict:
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=root, text=True).strip()
    if branch != "sprint-13-codex":
        raise ValueError("Repeatability check expects the Sprint 13 branch")
    with tempfile.TemporaryDirectory(prefix="ideo-codex-repeat-") as directory:
        temporary = Path(directory).resolve()
        if not temporary.is_relative_to(Path(tempfile.gettempdir()).resolve()):
            raise ValueError("Repeatability directory escaped the system temporary directory")
        clone = temporary / "repo"
        subprocess.run(
            ["git", "-c", "core.autocrlf=false", "clone", "--quiet", "--no-hardlinks",
             "--single-branch", "--branch", branch, str(root), str(clone)],
            check=True, capture_output=True,
        )
        runs = []
        for _ in range(2):
            result = subprocess.check_output([sys.executable, str(clone / "scripts/sync_codex.py")], cwd=clone, text=True)
            status = subprocess.check_output(["git", "status", "--porcelain"], cwd=clone, text=True)
            runs.append({"generator": json.loads(result), "clean": not status})
            if status:
                raise AssertionError("Regeneration changed the clean committed copy: " + status)
    return {"runs": runs, "temporary_copy_removed": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--idempotency", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    report = {}
    if args.self_test:
        report["self_test"] = self_test(root)
    content, counts = content_errors(root)
    links, link_count = link_errors(root / PACKAGE)
    navigation, resource_count = navigation_errors(root / PACKAGE)
    report.update(
        counts,
        local_links_checked=link_count, resources_checked=resource_count,
        content_errors=content, link_errors=links, navigation_errors=navigation,
    )
    if args.idempotency:
        report["idempotency"] = idempotency(root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if content or links or navigation:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
