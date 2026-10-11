import hashlib
import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


class MigrationError(RuntimeError):
    pass


@dataclass(frozen=True)
class Migration:
    version: int
    name: str
    sql: str
    checksum: str


def load_migrations(directory: Path | None = None) -> tuple[Migration, ...]:
    directory = directory or Path(__file__).parent / "migrations"
    migrations = []
    for path in sorted(directory.glob("[0-9][0-9][0-9][0-9]_*.sql")):
        data = path.read_bytes()
        migrations.append(
            Migration(
                int(path.name[:4]),
                path.name,
                data.decode("utf-8"),
                hashlib.sha256(data).hexdigest(),
            )
        )
    if [m.version for m in migrations] != list(range(1, len(migrations) + 1)) or not migrations:
        raise MigrationError("Noncontiguous migration set")
    return tuple(migrations)


def statements(sql: str) -> tuple[str, ...]:
    complete = []
    pending = ""
    for line in sql.splitlines(keepends=True):
        pending += line
        if sqlite3.complete_statement(pending):
            complete.append(pending)
            pending = ""
    if pending.strip():
        raise MigrationError("Incomplete SQL statement")
    return tuple(complete)


def applied_versions(connection: sqlite3.Connection, migrations: tuple[Migration, ...]) -> int:
    present = connection.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='schema_migrations'"
    ).fetchone()
    if not present:
        if connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        ).fetchone():
            raise MigrationError("Unversioned existing database")
        return 0
    rows = connection.execute(
        "SELECT version,name,checksum FROM schema_migrations ORDER BY version"
    ).fetchall()
    if [row[0] for row in rows] != list(range(1, len(rows) + 1)):
        raise MigrationError("Migration ledger gap")
    for row in rows:
        if row[0] > len(migrations):
            raise MigrationError("Unknown newer database schema")
        known = migrations[row[0] - 1]
        if (row[1], row[2]) != (known.name, known.checksum):
            raise MigrationError("Migration checksum/name mismatch")
    return len(rows)


def verify_integrity(connection: sqlite3.Connection) -> None:
    if connection.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
        raise MigrationError("Foreign keys must be enabled")
    if connection.execute("PRAGMA foreign_key_check").fetchall():
        raise MigrationError("Foreign key integrity failure")
    if [row[0] for row in connection.execute("PRAGMA integrity_check")] != ["ok"]:
        raise MigrationError("Database integrity failure")


def migrate(
    connection: sqlite3.Connection,
    *,
    target: int | None = None,
    backup_path: Path | None = None,
    migrations: tuple[Migration, ...] | None = None,
) -> int:
    """Checksummed, transactional per-version upgrade; H14 coordinates worker quiescence."""
    if connection.in_transaction:
        raise MigrationError("Migration requires a quiescent connection")
    known = migrations or load_migrations()
    target = len(known) if target is None else target
    current = applied_versions(connection, known)
    if not 0 <= current <= target <= len(known):
        raise MigrationError("Downgrade/unknown target forbidden")
    verify_integrity(connection)
    if 0 < current < target:
        if backup_path is None or not backup_path.is_absolute() or backup_path.exists():
            raise MigrationError("Upgrade requires a new absolute backup path")
        backup_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with sqlite3.connect(backup_path) as backup:
            connection.backup(backup)
        backup_path.chmod(0o600)
    for migration in known[current:target]:
        connection.execute("BEGIN IMMEDIATE")
        try:
            # Another cooperating upgrader cannot silently replace the inspected ledger.
            if applied_versions(connection, known) != migration.version - 1:
                raise MigrationError("Concurrent migration ledger changed")
            for statement in statements(migration.sql):
                connection.execute(statement)
            connection.execute(
                "INSERT INTO schema_migrations(version,name,checksum,applied_at) VALUES(?,?,?,?)",
                (
                    migration.version,
                    migration.name,
                    migration.checksum,
                    datetime.now(UTC).isoformat().replace("+00:00", "Z"),
                ),
            )
            verify_integrity(connection)
            connection.commit()
        except BaseException:
            connection.rollback()
            raise
    return target
