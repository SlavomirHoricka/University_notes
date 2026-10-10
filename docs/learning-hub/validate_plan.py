#!/usr/bin/env python3
"""Read-only validation of the hub's dispatch package, not application readiness."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import tomllib

REQUIRED_DOCS = (
    "README.md", "START_HERE.md", "PRODUCT_SPEC.md", "ARCHITECTURE.md",
    "CONTRACTS.md", "WORKFLOWS.md", "UI_IMPLEMENTATION.md", "TASKS.md",
    "VALIDATION.md",
)
PROTOTYPE_SHA256 = "be558e726fe68093fb2672b2d1e54a9c829c6ac1f060393c5bd6bf58716aedaf"


def validate(root: Path) -> list[str]:
    """Return actionable structural failures without modifying any input."""
    errors: list[str] = []
    package = root / "docs/learning-hub"
    for name in REQUIRED_DOCS:
        if not (package / name).is_file():
            errors.append(f"Missing document: {name}")
    try:
        graph = json.loads((package / "task_graph.json").read_text())
        branches = json.loads((package / "branch_provisioning.json").read_text())
    except (OSError, ValueError) as exc:
        return errors + [f"Cannot load registries: {exc}"]
    if not isinstance(graph, dict) or not isinstance(branches, dict):
        return errors + ["Registries must be JSON objects"]
    if graph.get("schema_version") != 1 or branches.get("schema_version") != 1:
        errors.append("Unsupported registry schema version")
    if graph.get("package_id") != "personal-learning-hub-v1":
        errors.append("Unexpected package identity")
    if graph.get("max_total_agents") != 4 or graph.get("root_counts_as_slot") is not True:
        errors.append("Dispatch must account for four total slots including root")
    roles, tasks = graph.get("roles"), graph.get("tasks")
    if not isinstance(roles, list) or not isinstance(tasks, list):
        return errors + ["roles/tasks must be lists"]
    if not all(isinstance(x, dict) and isinstance(x.get("id"), str) for x in roles + tasks):
        return errors + ["Malformed role/task record"]
    role_map, task_map = {r["id"]: r for r in roles}, {t["id"]: t for t in tasks}
    if len(role_map) != len(roles) or len(task_map) != len(tasks):
        errors.append("Duplicate role/task IDs")
    if set(task_map) != {f"H{i:02d}" for i in range(17)}:
        errors.append("Expected H00-H16 task set")
    role_branches = [r.get("branch") for r in roles]
    if len(set(role_branches)) != len(role_branches):
        errors.append("Duplicate role branches")
    registry = branches.get("branches")
    if not isinstance(registry, list) or not all(isinstance(x, dict) for x in registry):
        errors.append("Malformed branch registry")
    else:
        pairs = [(x.get("role"), x.get("branch")) for x in registry]
        if len(pairs) != len(set(pairs)) or set(pairs) != {(r["id"], r.get("branch")) for r in roles}:
            errors.append("Branch registry differs from role routing")
    for role in roles:
        rid = role["id"]
        if not re.fullmatch(r"hub_[a-z_]+", rid):
            errors.append(f"{rid}: invalid role ID")
        if not isinstance(role.get("branch"), str) or not role["branch"].startswith("codex/hub-"):
            errors.append(f"{rid}: invalid branch")
        paths = [role.get("profile", "")] + role.get("owned_paths", [])
        for path in paths:
            if not isinstance(path, str) or not path or PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
                errors.append(f"{rid}: unsafe relative path {path!r}")
        profile_path = role.get("profile")
        if not isinstance(profile_path, str):
            errors.append(f"{rid}: missing profile")
            continue
        try:
            profile = tomllib.loads((root / profile_path).read_text())
        except (OSError, ValueError) as exc:
            errors.append(f"{rid}: invalid TOML/profile: {exc}")
            continue
        for key, expected in (("name", rid), ("model", role.get("model")),
                              ("model_reasoning_effort", role.get("effort"))):
            if profile.get(key) != expected:
                errors.append(f"{rid}: profile {key} differs from registry")
        if not profile.get("description") or not profile.get("developer_instructions"):
            errors.append(f"{rid}: profile lacks instructions/description")
        if role.get("read_only") and (role.get("owned_paths") or profile.get("sandbox_mode") != "read-only"):
            errors.append(f"{rid}: reviewer must remain read-only")
        assigned = role.get("tasks")
        if not isinstance(assigned, list) or set(assigned) != {t["id"] for t in tasks if t.get("role") == rid}:
            errors.append(f"{rid}: reciprocal task ownership mismatch")
    cards = (package / "TASKS.md").read_text() if (package / "TASKS.md").is_file() else ""
    for task in tasks:
        tid, owner = task["id"], role_map.get(task.get("role"))
        if owner is None:
            errors.append(f"{tid}: unknown role")
        elif (task.get("model"), task.get("effort")) != (owner.get("model"), owner.get("effort")):
            errors.append(f"{tid}: routing differs from role")
        deps = task.get("depends_on")
        if not isinstance(deps, list) or not all(isinstance(d, str) for d in deps):
            errors.append(f"{tid}: invalid dependencies")
        else:
            for dep in deps:
                if dep not in task_map:
                    errors.append(f"{tid}: unknown dependency {dep}")
        for field in ("steps", "outputs", "acceptance"):
            if not isinstance(task.get(field), list) or not task[field] or not all(isinstance(x, str) and x for x in task[field]):
                errors.append(f"{tid}: missing {field}")
        if not re.search(r"^## " + re.escape(tid) + r"\b", cards, re.MULTILINE):
            errors.append(f"{tid}: missing task card")
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(tid: str) -> None:
        if tid in visiting:
            errors.append(f"Dependency cycle at {tid}")
            return
        if tid in visited:
            return
        visiting.add(tid)
        for dep in task_map[tid].get("depends_on", []):
            if isinstance(dep, str) and dep in task_map:
                visit(dep)
        visiting.remove(tid)
        visited.add(tid)

    if all(isinstance(t.get("depends_on"), list) for t in tasks):
        for tid in task_map:
            visit(tid)
    matrix = (package / "VALIDATION.md").read_text() if (package / "VALIDATION.md").is_file() else ""
    for i in range(1, 17):
        if not re.search(r"^### V" + f"{i:02d}" + r"\b", matrix, re.MULTILINE):
            errors.append(f"Missing release case V{i:02d}")
    prototype = package / "reference/personal_learning_hub_v3.html"
    if not prototype.is_file() or hashlib.sha256(prototype.read_bytes()).hexdigest() != PROTOTYPE_SHA256:
        errors.append("Reference prototype absent or changed")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Plan valid: 10 fixed roles, 17 tasks, DAG, profiles, branches and V01-V16.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

