"""Fictional export fixtures only; no actual notes, provider or learner state."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("export_app", Path(__file__).with_name("export_app.py"))
assert SPEC and SPEC.loader
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        # macOS /var is an OS symlink; fixtures use the canonical /private/var.
        self.parent = Path(self.temp.name).resolve()
        self.root = self.parent / "repository" / "app"
        self.root.mkdir(parents=True)
        self.destination = self.parent / "standalone"
        self.write("README.md", "fictional app\n")
        self.manifest(["README.md"])

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def manifest(self, names):
        entries = []
        for name in names:
            data = (self.root / name).read_bytes()
            entries.append({"path": name, "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)})
        (self.root / tool.MANIFEST).write_text(json.dumps({"schema_version": 1, "provenance_commit": "a" * 40, "files": entries}))

    def git(self, root, *args):
        return subprocess.check_output(["git", "-C", str(root), *args], text=True)

    def test_export_only_listed_verified_files(self):
        self.write("unlisted-secret.txt", "do not copy")
        self.write(".private/token", "do not copy")
        self.assertEqual(tool.export(self.root, self.destination), 1)
        self.assertEqual({p.relative_to(self.destination).as_posix() for p in self.destination.rglob("*")}, {"README.md", tool.MANIFEST})

    def test_export_reexport_preserves_manifest_without_git(self):
        original = (self.root / tool.MANIFEST).read_bytes()
        self.assertEqual(tool.export(self.root, self.destination), 1)
        self.assertEqual((self.destination / tool.MANIFEST).read_bytes(), original)
        second = self.parent / "second-export"
        self.assertEqual(tool.export(self.destination, second), 1)
        self.assertEqual((second / tool.MANIFEST).read_bytes(), original)
        self.assertEqual((second / "README.md").read_bytes(), (self.root / "README.md").read_bytes())

    def test_source_ancestor_symlink_rejected(self):
        alias = self.parent / "source-alias"
        alias.symlink_to(self.root.parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Source path"):
            tool.export(alias / "app", self.destination)

    def test_tamper_fails_before_destination_creation(self):
        self.write("README.md", "same size edit!")
        with self.assertRaisesRegex(ValueError, "mismatch"):
            tool.export(self.root, self.destination)
        self.assertFalse(self.destination.exists())

    def test_same_size_hash_tamper(self):
        data = (self.root / "README.md").read_text()
        self.write("README.md", "X" + data[1:])
        with self.assertRaisesRegex(ValueError, "Hash mismatch"):
            tool.export(self.root, self.destination)

    def test_unsafe_paths_and_duplicate_paths(self):
        for value in ("../README.md", "/README.md", "a/../README.md", "./README.md", "a//b", "a\\b", "C:/file"):
            with self.subTest(path=value), self.assertRaises(ValueError):
                tool.safe_relative(value)
        self.manifest(["README.md", "README.md"])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            tool.export(self.root, self.destination)

    def test_file_and_directory_symlinks_rejected(self):
        external = self.parent / "external"
        external.mkdir()
        (external / "token").write_text("secret")
        (self.root / "link").symlink_to(external, target_is_directory=True)
        self.manifest(["link/token"])
        with self.assertRaisesRegex(ValueError, "Symlink"):
            tool.export(self.root, self.destination)
        (self.root / "README.md").unlink()
        (self.root / "README.md").symlink_to(external / "token")
        self.manifest(["README.md"])
        with self.assertRaisesRegex(ValueError, "Symlink"):
            tool.export(self.root, self.destination)

    def test_manifest_symlink_rejected(self):
        manifest = self.root / tool.MANIFEST
        external = self.parent / "manifest"
        manifest.rename(external)
        manifest.symlink_to(external)
        with self.assertRaisesRegex(ValueError, "Manifest"):
            tool.export(self.root, self.destination)

    def test_nonempty_destination_preserved(self):
        self.destination.mkdir()
        sentinel = self.destination / "existing"
        sentinel.write_text("preserve")
        with self.assertRaisesRegex(ValueError, "new or empty"):
            tool.export(self.root, self.destination)
        self.assertEqual(sentinel.read_text(), "preserve")

    def test_empty_destination_supported(self):
        self.destination.mkdir()
        self.assertEqual(tool.export(self.root, self.destination), 1)

    def test_same_nested_parent_and_symlink_destinations_rejected(self):
        for destination in (self.root, self.root / "nested", self.root.parent, self.parent):
            with self.subTest(destination=destination), self.assertRaises(ValueError):
                tool.export(self.root, destination)
        self.destination.symlink_to(self.parent / "elsewhere", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlinks"):
            tool.export(self.root, self.destination)

    def test_excluded_entry_cannot_be_added_by_manifest(self):
        self.write(".private/token", "secret")
        self.manifest([".private/token"])
        with self.assertRaisesRegex(ValueError, "excluded"):
            tool.export(self.root, self.destination)

    def test_nested_git_refresh_closure_and_provenance(self):
        top = self.root.parent
        self.git(top, "init", "-q")
        self.write("03_Agents/runtime/ingest/index.md", "runtime")
        self.write("03_Agents/2026_2027/Winter_Semester/Real/learning_log.md", "real history")
        self.write("tests/fixtures/journal.json", "{}")
        self.write("backend/domain/ports/runtime.py", "# code")
        self.write("03_Agents/plugins/uni-teach-0.4.0.zip", "archive")
        self.write("node_modules/module.js", "dependency")
        self.write(".private/token", "secret")
        (top / "notes-secret.txt").write_text("outside app")
        self.git(top, "add", ".")
        self.git(top, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fictional fixture")
        tool.refresh(self.root)
        manifest = json.loads((self.root / tool.MANIFEST).read_text())
        self.assertEqual(manifest["provenance_commit"], self.git(top, "rev-parse", "HEAD").strip())
        self.assertEqual({e["path"] for e in manifest["files"]}, {"README.md", "tests/fixtures/journal.json", "backend/domain/ports/runtime.py"})
        self.assertEqual(tool.export(self.root, self.destination), 3)

    def test_standalone_git_refresh(self):
        self.git(self.root, "init", "-q")
        self.git(self.root, "add", ".")
        self.git(self.root, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture")
        tool.refresh(self.root)
        self.assertEqual([e["path"] for e in json.loads((self.root / tool.MANIFEST).read_text())["files"]], ["README.md"])


if __name__ == "__main__":
    unittest.main()
