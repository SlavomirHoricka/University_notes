"""Read-only install diagnostic; never prints secrets or reads academic records."""

import json
import platform
import shutil
import subprocess
from importlib.metadata import version
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    node = shutil.which("node")
    if node is None:
        raise SystemExit("Node 24 LTS is required")
    node_version = subprocess.check_output([node, "--version"], text=True).strip()
    problems = []
    if platform.python_version_tuple()[:2] != ("3", "12"):
        problems.append("Python 3.12 required")
    if not node_version.startswith("v24."):
        problems.append("Node 24 LTS required")
    for path in ("uv.lock", "frontend/package-lock.json", "frontend/node_modules"):
        if not (root / path).exists():
            problems.append(f"Missing {path}; follow README install steps")
    print(
        json.dumps(
            {
                "python": platform.python_version(),
                "node": node_version,
                "os": platform.platform(),
                "packages": {
                    name: version(name)
                    for name in ("fastapi", "pydantic", "uvicorn", "ruff", "mypy", "pytest")
                },
                "problems": problems,
            },
            indent=2,
        )
    )
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
