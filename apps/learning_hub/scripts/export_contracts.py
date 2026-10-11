"""Export deterministic OpenAPI and generate TypeScript with the locked owning generator."""

import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from learning_hub.application.core.bootstrap import create_app

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "frontend/src/api/generated/openapi.json"
TYPES = ROOT / "frontend/src/api/generated/schema.ts"


def export(*, check: bool) -> None:
    schema = json.dumps(create_app().openapi(), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    with tempfile.TemporaryDirectory(prefix="hub-contracts-") as temporary:
        directory = Path(temporary)
        source = directory / "openapi.json"
        target = directory / "schema.ts"
        source.write_text(schema, encoding="utf-8")
        subprocess.run(
            [
                "node",
                str(ROOT / "frontend/node_modules/openapi-typescript/bin/cli.js"),
                str(source),
                "--output",
                str(target),
            ],
            check=True,
            cwd=ROOT,
        )
        types = target.read_text(encoding="utf-8")
        if check:
            if SCHEMA.read_text(encoding="utf-8") != schema:
                raise SystemExit("OpenAPI drift: run make export-contracts")
            if TYPES.read_text(encoding="utf-8") != types:
                raise SystemExit("TypeScript drift: run make export-contracts")
        else:
            SCHEMA.parent.mkdir(parents=True, exist_ok=True)
            SCHEMA.write_text(schema, encoding="utf-8")
            TYPES.write_text(types, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    export(check=parser.parse_args().check)
