#!/usr/bin/env python3
"""Refresh a tracked-file manifest and export a verified standalone app snapshot.

No Git history, secrets, dependencies or runtime state is copied. This preserves
the audited code snapshot; it does not certify a finished learning application.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

MANIFEST = "MIGRATION_MANIFEST.json"
EXCLUDED_DIRS = {
    ".git", ".tools", ".venv", ".runtime", ".private", ".cache",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", "__pycache__",
    "node_modules", "dist", "build", "test-results", "playwright-report",
}


def safe_relative(value: object) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise ValueError(f"Invalid relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in {".", ".."} for p in value.split("/")):
        raise ValueError(f"Unsafe relative path: {value!r}")
    if path.as_posix() != value or re.match(r"^[A-Za-z]:", value):
        raise ValueError(f"Noncanonical relative path: {value!r}")
    return value


def excluded(value: str, manifest_name: str = MANIFEST) -> bool:
    parts = PurePosixPath(value).parts
    name = parts[-1]
    return (
        value == manifest_name
        or any(p in EXCLUDED_DIRS or p.endswith(".egg-info") for p in parts)
        or name.endswith((".pyc", ".pyo", ".db", ".db-wal", ".db-shm", ".sqlite3"))
        or (name.startswith(".env") and name != ".env.example")
        or value.startswith(("00_Materials/", "01_Notes/", "02_Resources/", "Excalidraw/", ".obsidian/", ".claudian/"))
        or value.startswith(("03_Agents/runtime/", "03_Agents/history/", "03_Agents/.backups/", "03_Agents/validation/"))
        or bool(re.match(r"03_Agents/\d{4}_\d{4}(?:/|$)", value))
        or bool(re.match(r"03_Agents/plugins/uni-teach[^/]*\.zip$", value))
        or value == "03_Agents/plugins/uni-teach-release.json"
    )


def checked_file(root: Path, relative: str) -> Path:
    relative = safe_relative(relative)
    current = root
    for component in PurePosixPath(relative).parts:
        current = current / component
        if current.is_symlink():
            raise ValueError(f"Symlink is not exportable: {relative}")
    if not current.is_file() or not current.resolve().is_relative_to(root):
        raise ValueError(f"Missing or escaped source file: {relative}")
    return current


def source_root(root: Path) -> Path:
    absolute = root.absolute()
    if any(component.is_symlink() for component in (absolute, *absolute.parents)):
        raise ValueError("Source path cannot contain symlinks")
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("Source root must exist")
    return root


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True)


def refresh(root: Path, provenance_commit: str | None = None) -> Path:
    root = source_root(root)
    top = Path(git(root, "rev-parse", "--show-toplevel").strip()).resolve()
    prefix = root.relative_to(top).as_posix()
    prefix = "" if prefix == "." else prefix + "/"
    provenance = git(top, "rev-parse", "--verify", (provenance_commit or "HEAD") + "^{commit}").strip()
    names = git(top, "ls-files", "-z", "--", prefix or ".").split("\x00")
    files = []
    for name in sorted(n for n in names if n):
        if not name.startswith(prefix):
            raise ValueError(f"Tracked path outside source root: {name}")
        relative = safe_relative(name[len(prefix):])
        if excluded(relative):
            continue
        data = checked_file(root, relative).read_bytes()
        files.append({"path": relative, "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)})
    if not files:
        raise ValueError("No tracked exportable files; stage the app paths before refreshing")
    manifest = root / MANIFEST
    if manifest.is_symlink():
        raise ValueError("Manifest cannot be a symlink")
    content = {"schema_version": 1, "provenance_commit": provenance, "files": files}
    manifest.write_text(json.dumps(content, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def validated_entries(root: Path, manifest: Path) -> tuple[bytes, list[tuple[str, bytes, int]]]:
    if manifest.is_symlink() or not manifest.is_file():
        raise ValueError("Manifest must be a regular file")
    manifest_bytes = manifest.read_bytes()
    content = json.loads(manifest_bytes.decode("utf-8"))
    if not isinstance(content, dict) or content.get("schema_version") != 1:
        raise ValueError("Unsupported manifest schema")
    if not isinstance(content.get("provenance_commit"), str) or not re.fullmatch(r"[0-9a-f]{40,64}", content["provenance_commit"]):
        raise ValueError("Invalid provenance commit")
    entries = content.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Manifest requires a nonempty files list")
    seen: set[str] = set()
    result = []
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("Invalid file entry")
        relative = safe_relative(entry.get("path"))
        if relative in seen or excluded(relative):
            raise ValueError(f"Duplicate or excluded manifest path: {relative}")
        seen.add(relative)
        path = checked_file(root, relative)
        data = path.read_bytes()
        if not isinstance(entry.get("size"), int) or isinstance(entry["size"], bool) or len(data) != entry["size"]:
            raise ValueError(f"Size mismatch: {relative}")
        if hashlib.sha256(data).hexdigest() != entry.get("sha256"):
            raise ValueError(f"Hash mismatch: {relative}; refresh only after reviewing changes")
        result.append((relative, data, path.stat().st_mode & 0o777))
    return manifest_bytes, result


def export(root: Path, destination: Path) -> int:
    root = source_root(root)
    # Reject symlink components before resolving an existing or new destination.
    raw_destination = destination.absolute()
    for component in (raw_destination, *raw_destination.parents):
        if component.is_symlink():
            raise ValueError("Destination path cannot contain symlinks")
    destination = raw_destination.resolve()
    if destination == root or destination.is_relative_to(root) or root.is_relative_to(destination):
        raise ValueError("Destination must be outside source and cannot be its parent")
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError("Destination must be new or empty; existing files are never overwritten")
    manifest_bytes, entries = validated_entries(root, root / MANIFEST)
    destination.mkdir(parents=True, exist_ok=True)
    for relative, data, mode in entries:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        # Copy the verified byte snapshot, not a later reread of mutable sources.
        with target.open("xb") as stream:
            stream.write(data)
        target.chmod(mode)
    # Audit metadata is intentionally outside its own hashed file list.
    with (destination / MANIFEST).open("xb") as stream:
        stream.write(manifest_bytes)
    return len(entries)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    default_root = Path(__file__).resolve().parents[1]
    update = subparsers.add_parser("refresh", help="Hash tracked files after a scoped review")
    update.add_argument("--root", type=Path, default=default_root)
    update.add_argument("--provenance-commit", help="Verified pre-separation checkpoint (default HEAD)")
    copy = subparsers.add_parser("export", help="Verify manifest and copy only its files")
    copy.add_argument("destination", type=Path)
    copy.add_argument("--root", type=Path, default=default_root)
    args = parser.parse_args()
    try:
        if args.command == "refresh":
            print(f"Manifest refreshed: {refresh(args.root, args.provenance_commit)}")
        else:
            print(f"Exported {export(args.root, args.destination)} verified files plus unchanged manifest to {args.destination}")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
