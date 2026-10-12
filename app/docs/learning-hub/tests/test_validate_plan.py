"""Dispatch safety checks use isolated copies, never mutate repository evidence."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_plan", PACKAGE / "validate_plan.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DispatchSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.package = self.root / "docs/learning-hub"
        shutil.copytree(PACKAGE, self.package, ignore=shutil.ignore_patterns("__pycache__"))
        profiles = self.root / ".codex/agents"
        profiles.mkdir(parents=True)
        for source in PACKAGE.parents[1].glob(".codex/agents/hub_*.toml"):
            shutil.copy2(source, profiles / source.name)
        self.graph_path = self.package / "task_graph.json"
        self.graph = json.loads(self.graph_path.read_text())

    def save(self):
        self.graph_path.write_text(json.dumps(self.graph))

    def assert_failure(self, fragment):
        self.assertTrue(any(fragment in e for e in MODULE.validate(self.root)),
                        MODULE.validate(self.root))

    def test_approved_package_dispatches(self):
        self.assertEqual([], MODULE.validate(self.root))

    def test_cycle_rejected(self):
        self.graph["tasks"][0]["depends_on"] = ["H16"]
        self.save()
        self.assert_failure("Dependency cycle")

    def test_missing_dependency_rejected(self):
        self.graph["tasks"][0]["depends_on"] = ["H99"]
        self.save()
        self.assert_failure("unknown dependency H99")

    def test_untracked_role_transfer_rejected(self):
        self.graph["tasks"][0]["role"] = "hub_provider"
        self.save()
        self.assert_failure("reciprocal task ownership mismatch")

    def test_model_override_drift_rejected(self):
        path = self.root / ".codex/agents/hub_foundation.toml"
        path.write_text(path.read_text().replace('model = "gpt-6.1-sol"', 'model = "gpt-6-luna"'))
        self.assert_failure("profile model differs")

    def test_branch_registry_drift_rejected(self):
        self.graph["roles"][0]["branch"] = "codex/hub-other"
        self.save()
        self.assert_failure("Branch registry differs")

    def test_reference_substitution_rejected(self):
        (self.package / "reference/personal_learning_hub_v3.html").write_text("changed")
        self.assert_failure("Reference prototype")

    def test_path_escape_rejected(self):
        self.graph["roles"][0]["owned_paths"].append("../outside")
        self.save()
        self.assert_failure("unsafe relative path")

    def test_malformed_registry_rejected(self):
        self.graph_path.write_text('["wrong shape"]')
        self.assert_failure("JSON objects")


if __name__ == "__main__":
    unittest.main()
