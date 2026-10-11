import subprocess
from pathlib import Path


def test_app_private_runtime_ignored_and_canonical_journal_visible() -> None:
    root = Path(__file__).resolve().parents[3]
    ignored = [
        ".tools/token",
        ".runtime/state.sqlite3",
        ".private/answers.json",
        ".env",
        "frontend/test-results/result.json",
    ]
    for relative in ignored:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", str(root / relative)],
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, relative
    repository = root.parents[1]
    for path in [
        repository / "03_Agents/runtime/transactions/fixture/journal.json",
        root / "tests/fixtures/journal.json",
    ]:
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", str(path)], capture_output=True, check=False
        )
        assert result.returncode == 1, str(path)
