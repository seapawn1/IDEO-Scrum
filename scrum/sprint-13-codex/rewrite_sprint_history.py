#!/usr/bin/env python3
"""Remove archived raw outputs from the unpublished Sprint 13 history."""

from __future__ import annotations

import argparse
from functools import cache
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

import run_codex_smoke as privacy


ROOT = Path(__file__).resolve().parents[2]
SPRINT = Path("scrum/sprint-13-codex")
RESULTS = SPRINT / "results"
REF = "refs/heads/sprint-13-codex"


def git(*args: str, data: bytes | None = None, env: dict | None = None) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, input=data, env=env)


@cache
def rules():
    _, _, identifier, provider, values = privacy.source_settings()
    return values, privacy.provider_privacy(identifier, provider)[1]


def findings(data: bytes) -> dict[str, int]:
    value = data.decode("utf-8", errors="replace")
    secrets, contexts = rules()
    hits = {
        "private_values": sum(len(re.findall(re.escape(secret), value, re.I)) for secret in set(secrets)),
        "credential_shapes": sum(len(pattern.findall(value)) for pattern in privacy.SECRET_SHAPES),
        "serialized_provider_settings": sum(len(pattern.findall(value)) for _, pattern in contexts),
    }
    return {key: count for key, count in hits.items() if count}


def raw_path(name: str) -> bool:
    path = Path(name)
    if not path.is_relative_to(RESULTS):
        return False
    return path.suffix in {".jsonl", ".txt"} or path.name in {"install.json", "marketplace.json"}


def compact(value):
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if key in {"final_answer", "S1_final_answer", "command"}:
                continue
            if key == "installed_path" and isinstance(item, str):
                normalized = item.replace("\\", "/")
                result["installed_skill"] = "skills/" + normalized.rsplit("/skills/", 1)[-1]
            else:
                result[key] = compact(item)
        return result
    if isinstance(value, list):
        return [compact(item) for item in value]
    return value


def filtered_blob(name: str, data: bytes) -> bytes:
    if name.startswith(RESULTS.as_posix() + "/") and name.endswith(".json"):
        parsed = compact(json.loads(data.decode("utf-8-sig")))
        data = (json.dumps(parsed, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    secrets, _ = rules()
    value = data.decode("utf-8", errors="strict")
    # There should be no private data in methodology sources; fail rather than alter them.
    sanitized, _ = privacy.scrub(value, secrets)
    changed = sanitized.encode("utf-8")
    if changed != data and (name.startswith("plugins/") or name.startswith("codex/")):
        raise ValueError("Unexpected private-value collision in a product source: " + name)
    if findings(changed):
        raise ValueError("Unresolved provider setting in retained file: " + name)
    return changed


def audit() -> dict:
    if git("symbolic-ref", "HEAD").decode().strip() != REF:
        raise ValueError("The Sprint 13 branch must remain checked out")
    revisions = git("rev-list", "--reverse", "main..HEAD").decode().splitlines()
    checked: set[str] = set()
    for revision in revisions:
        commit = git("cat-file", "commit", revision)
        if findings(commit):
            raise ValueError("Private value in retained commit metadata")
        for item in git("ls-tree", "-r", "-z", revision).split(b"\0"):
            if not item:
                continue
            metadata, name = item.split(b"\t", 1)
            mode, kind, oid = metadata.decode().split()
            if raw_path(name.decode("utf-8")):
                raise ValueError("A raw output is still reachable in Sprint history")
            if kind != "blob" or oid in checked:
                continue
            if findings(git("cat-file", "blob", oid)):
                raise ValueError("Private value in a retained history blob")
            checked.add(oid)
    patch = git("log", "-p", "--no-ext-diff", "--no-color", "main..HEAD")
    if findings(patch):
        raise ValueError("Private value remains in git log -p main..HEAD")
    return {
        "branch_commits_checked": len(revisions),
        "unique_blobs_checked": len(checked),
        "raw_outputs_reachable": 0,
        "private_value_matches": 0,
        "credential_shape_matches": 0,
        "serialized_provider_setting_matches": 0,
        "log_patch_matches": 0,
        "scope": "All retained snapshots, commit metadata, and git log -p main..HEAD",
        "public_setting_scope": "Protocol enums, booleans and generic provider labels are checked in configuration key/value context",
    }


def rewrite() -> dict:
    if git("symbolic-ref", "HEAD").decode().strip() != REF:
        raise ValueError("Wrong checked-out branch")
    if git("status", "--porcelain").strip():
        raise ValueError("Commit the current work before rewriting")
    state = json.loads((ROOT / SPRINT / "archive-location.json").read_text(encoding="utf-8"))
    archive = Path(state["archive"]).resolve()
    if archive.parent != Path("S:/IDEO-Scrum-Archives").resolve() or archive.is_relative_to(ROOT):
        raise ValueError("Invalid external archive")
    for entry in json.loads((archive / "manifest.json").read_text(encoding="utf-8")):
        original = archive / "workspace" / entry["path"]
        if hashlib.sha256(original.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError("External backup failed verification")
    git("bundle", "verify", str(archive / "before-rewrite.bundle"))
    head = git("rev-parse", "HEAD").decode().strip()
    main = git("rev-parse", "main").decode().strip()
    git("bundle", "create", str(archive / "with-english-draft.bundle"), "main..HEAD")
    git("bundle", "verify", str(archive / "with-english-draft.bundle"))
    references_before = git("for-each-ref", "--format=%(refname) %(objectname)").decode().splitlines()
    revisions = git("rev-list", "--reverse", "--topo-order", "main..HEAD").decode().splitlines()
    mappings: dict[str, str] = {}
    cached: dict[tuple[str, str], str] = {}
    removed: set[str] = set()
    with tempfile.TemporaryDirectory(prefix="ideo-codex-history-") as directory:
        temporary = Path(directory).resolve()
        if temporary.parent != Path(tempfile.gettempdir()).resolve():
            raise ValueError("Unexpected temporary index location")
        environment = os.environ.copy()
        environment["GIT_INDEX_FILE"] = str(temporary / "index")
        for revision in revisions:
            entries = []
            for item in git("ls-tree", "-r", "-z", revision).split(b"\0"):
                if not item:
                    continue
                metadata, encoded_name = item.split(b"\t", 1)
                mode, kind, oid = metadata.decode().split()
                name = encoded_name.decode("utf-8")
                if raw_path(name):
                    target = (ROOT / name).resolve()
                    if not target.is_relative_to((ROOT / RESULTS).resolve()):
                        raise ValueError("Removal escaped the Sprint results folder")
                    removed.add(name)
                    continue
                key = (name, oid)
                if key not in cached:
                    original = git("cat-file", "blob", oid)
                    filtered = filtered_blob(name, original)
                    cached[key] = oid if original == filtered else git(
                        "hash-object", "-w", "--stdin", data=filtered
                    ).decode().strip()
                entries.append(f"{mode} {cached[key]}\t".encode() + encoded_name + b"\0")
            git("read-tree", "--empty", env=environment)
            git("update-index", "-z", "--index-info", data=b"".join(entries), env=environment)
            tree = git("write-tree", env=environment).decode().strip()
            commit = git("cat-file", "commit", revision)
            headers, message = commit.split(b"\n\n", 1)
            if b"\ngpgsig " in b"\n" + headers:
                raise ValueError("Signed commits need explicit signature handling")
            rewritten = []
            for line in headers.splitlines():
                if line.startswith(b"tree "):
                    line = b"tree " + tree.encode()
                elif line.startswith(b"parent "):
                    parent = line[7:].decode()
                    line = b"parent " + mappings.get(parent, parent).encode()
                rewritten.append(line)
            cleaned_message = privacy.scrub(message.decode("utf-8"), rules()[0])[0].encode("utf-8")
            data = b"\n".join(rewritten) + b"\n\n" + cleaned_message
            mappings[revision] = git("hash-object", "-t", "commit", "-w", "--stdin", data=data).decode().strip()
    # Only the explicitly authorized unpublished branch ref changes.
    git("update-ref", REF, mappings[head], head)
    git("reset", "--hard", "--quiet", mappings[head])
    assert git("rev-parse", "main").decode().strip() == main
    references_after = git("for-each-ref", "--format=%(refname) %(objectname)").decode().splitlines()
    assert [x for x in references_before if not x.startswith(REF + " ")] == [
        x for x in references_after if not x.startswith(REF + " ")
    ]
    mapping = {
        "base_main_unchanged": main,
        "archive": str(archive),
        "commits": [{"old": old, "new": new} for old, new in mappings.items()],
    }
    (ROOT / SPRINT / "rewrite-map.json").write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")
    (archive / "rewrite-map.json").write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")
    report = audit()
    report.update({"removed_raw_files": len(removed), "rewritten_commits": len(mappings), "other_refs_unchanged": True})
    (ROOT / RESULTS / "privacy-history-scan.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()
    print(json.dumps(audit() if args.audit_only else rewrite(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
