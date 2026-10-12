import sqlite3
import unicodedata
from pathlib import Path


def connect_database(path: Path) -> sqlite3.Connection:
    """Open an explicitly selected local operational database; never select a vault implicitly."""
    if not path.is_absolute() or path.is_symlink():
        raise ValueError("Absolute nonsymlink operational DB path required")
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    connection = sqlite3.connect(path, isolation_level=None, timeout=5)
    path.chmod(0o600)
    connection.row_factory = sqlite3.Row
    connection.create_function(
        "nfc", 1, lambda text: unicodedata.normalize("NFC", text), deterministic=True
    )
    connection.execute("PRAGMA foreign_keys=ON")
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute("PRAGMA synchronous=FULL")
    connection.execute("PRAGMA busy_timeout=5000")
    return connection
