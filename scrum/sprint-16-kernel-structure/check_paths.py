#!/usr/bin/env python3
"""Sprint 16 self-check: every backticked .md path, markdown link, and `convention N` reference in the plugin resolves."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path


PLUGIN = Path("plugins/ideo-scrum")
PATH_RE = re.compile(r"`([^`\n]+?\.md)`")
LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s]+?)(?:\s+[\"'][^\n]*?[\"'])?\s*\)")
NAMED_CONV_RE = re.compile(
    r"`([^`\n]+?\.md)`,\s*conventions?\s+(\d+)(?:\s*(?:[-–]\s*(\d+)|and\s+(\d+)))?"
)
BARE_CONV_RE = re.compile(r"\bconventions? (\d+)(?:\s*(?:[-–]\s*(\d+)|\s+and\s+(\d+)))?")


def skill_root(path: Path) -> Path | None:
    parts = path.parts
    if "skills" in parts:
        index = parts.index("skills")
        return Path(*parts[: index + 2])
    return None


def targets(path: Path) -> list[Path]:
    roots = [path.parent]
    root = skill_root(path)
    if root:
        roots.append(root)
    if path.parent.name == "commands":
        skills = path.parent.parent / "skills"
        roots.extend(sorted(p for p in skills.iterdir() if p.is_dir()))
    return roots


def resolve(path: Path, raw: str) -> bool:
    raw = raw.split("#")[0]
    if not raw or raw.startswith(("http://", "https://", "mailto:")):
        return True
    for base in targets(path):
        if (base / raw).resolve().exists():
            return True
    return False


def convention_max(path: Path) -> int:
    numbers = [int(n) for n in re.findall(r"(?m)^\s*(\d+)\.\s+\*\*", path.read_text(encoding="utf-8"))]
    return max(numbers) if numbers else 0


def scan(root: Path) -> tuple[list[str], dict]:
    plugin = root / PLUGIN
    errors: list[str] = []
    paths = links = conventions = name_mentions = 0
    for path in sorted(plugin.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw in PATH_RE.findall(text):
            paths += 1
            if "<" in raw or ">" in raw:
                continue
            if not resolve(path, raw):
                if "/" not in raw:
                    name_mentions += 1
                    continue
                errors.append(f"{path.relative_to(root)}: path {raw}")
        for raw in LINK_RE.findall(text):
            links += 1
            if not resolve(path, raw):
                errors.append(f"{path.relative_to(root)}: link {raw}")
        if "convention" not in text:
            continue
        own_max = convention_max(path)

        def limit_for(target: Path) -> int:
            if target == path and own_max == 0:
                if path.name.endswith("-template.md"):
                    sibling = path.with_name(path.name.replace("-template.md", ".md"))
                    if not sibling.exists():
                        logs = sorted(path.parent.glob("*-log.md"))
                        sibling = logs[0] if len(logs) == 1 else sibling
                else:
                    root_dir = skill_root(path)
                    logs = sorted((root_dir / "conventions").glob("*-log.md")) if root_dir else []
                    sibling = logs[0] if len(logs) == 1 else path
                if sibling.exists():
                    return convention_max(sibling)
            return convention_max(target) if target.suffix == ".md" else own_max

        for match in NAMED_CONV_RE.finditer(text):
            raw, *numbers = match.groups()
            numbers = [int(n) for n in numbers if n]
            conventions += 1
            target = path
            for base in targets(path):
                candidate = (base / raw.split("#")[0]).resolve()
                if candidate.exists():
                    target = candidate
                    break
            limit = limit_for(target)
            for number in numbers:
                if number > limit:
                    errors.append(
                        f"{path.relative_to(root)}: convention {number} beyond {target.relative_to(root)} ({limit})"
                    )

        stripped = NAMED_CONV_RE.sub("", text)
        for line in stripped.splitlines():
            for match in BARE_CONV_RE.finditer(line):
                numbers = [int(n) for n in match.groups() if n]
                conventions += 1
                limit = limit_for(path)
                for number in numbers:
                    if number > limit:
                        errors.append(
                            f"{path.relative_to(root)}: convention {number} beyond {path.relative_to(root)} ({limit})"
                        )
    return errors, {"paths": paths, "links": links, "convention_refs": conventions, "name_mentions": name_mentions}


def self_test(root: Path) -> dict:
    with tempfile.TemporaryDirectory(prefix="ideo-s16-check-") as directory:
        fixture = Path(directory).resolve()
        shutil.copytree(root / PLUGIN, fixture / PLUGIN)
        good, _ = scan(fixture)
        assert not good, f"known-good copy failed: {good[:3]}"
        sample = fixture / PLUGIN / "skills/scrum-kernel/conventions/product-log.md"
        original = sample.read_text(encoding="utf-8")
        sample.write_text(
            original.replace(
                "(`../sprint-kernel/conventions/sprint-log.md`, convention 6)",
                "(`../sprint-kernel/conventions/sprint-log.md`, convention 66)",
            ),
            encoding="utf-8",
        )
        assert any("convention 66" in e for e in scan(fixture)[0]), "bad convention not detected"
        sample.write_text(
            original.replace(
                "(`../sprint-kernel/conventions/sprint-log.md`, convention 6)",
                "(`../sprint-kernel/missing.md`, convention 6)",
            ),
            encoding="utf-8",
        )
        assert any("missing.md" in e for e in scan(fixture)[0]), "bad path not detected"
    return {"known_good": True, "bad_convention_detected": True, "bad_path_detected": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    report = {}
    if args.self_test:
        report["self_test"] = self_test(root)
    errors, counts = scan(root)
    report.update(counts, errors=errors)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
