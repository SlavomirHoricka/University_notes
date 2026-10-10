"""Routing configuration and packaging integration regressions (no model calls)."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest

try:
    import tomllib
except ImportError:
    tomllib = None

AGENTS = Path(__file__).resolve().parents[1]

class RoutingContractTests(unittest.TestCase):
    @unittest.skipIf(tomllib is None, 'TOML validation requires Python 3.11+; use the bundled Python runtime')
    def test_role_contracts_and_escalation_are_discoverable(self):
        policy=(AGENTS/'references/MODEL_ROUTING.md').read_text()
        expected={
          'uni_ingest_owner':('gpt-6.1-sol','high',False),
          'uni_ingest_draft':('gpt-6-luna','medium',True),
          'uni_ingest_draft_high':('gpt-6-luna','high',True),
          'uni_ingest_reasoning_astra':('gpt-6-astra','high',True),
          'uni_source_checker':('gpt-6-astra','high',True),
          'uni_source_checker_xhigh':('gpt-6-astra','xhigh',True),
          'uni_plan_owner':('gpt-6.1-sol','high',False),
          'uni_plan_owner_astra':('gpt-6-astra','high',False),
          'uni_curriculum_checker':('gpt-6-astra','high',True),
          'uni_curriculum_checker_xhigh':('gpt-6-astra','xhigh',True),
          'uni_teach_owner':('gpt-6-luna','medium',False),
          'uni_teach_assessor':('gpt-6.1-sol','high',True),
          'uni_recall_owner':('gpt-6-luna','low',False),
          'uni_recall_owner_medium':('gpt-6-luna','medium',False),
        }
        self.assertEqual(set(expected),{p.stem for p in (AGENTS/'agents').glob('*.toml')})
        for name,(model,effort,readonly) in expected.items():
            with self.subTest(role=name):
                source=AGENTS/'agents'/f'{name}.toml'
                d=tomllib.loads(source.read_text())
                self.assertEqual((d['name'],d['model'],d['model_reasoning_effort']),(name,model,effort))
                self.assertTrue(d['description']); self.assertTrue(d['developer_instructions'])
                self.assertEqual(d.get('sandbox_mode'), 'read-only' if readonly else None)
                self.assertIn(name,policy)
                self.assertEqual(source.read_bytes(),(AGENTS.parent/'.codex/agents'/source.name).read_bytes())
                self.assertEqual(source.read_bytes(),(AGENTS/'plugins/uni-teach/agents'/source.name).read_bytes())
        for skill in ('ingest','plan','teach','recall'):
            text=(AGENTS/skill/'SKILL.md').read_text()
            self.assertIn('MODEL_ROUTING.md',text)
            self.assertIn(f'uni_{skill}_owner',text)
            self.assertNotIn('this skill does not switch it',text)

    def fixture(self, root):
        agents=root/'03_Agents'; package=agents/'plugins/uni-teach'
        package.mkdir(parents=True)
        (package/'plugin.json').write_text(json.dumps({'name':'uni-teach','version':'0.4.0','description':'test','author':{},'extensions':{'com.openai':{'interface':{}}}}))
        for name in ('ingest','plan','teach','recall'):
            (agents/name).mkdir(); (agents/name/'SKILL.md').write_text('fixture '+name)
        (agents/'references').mkdir(); (agents/'references/PLUGIN_README.md').write_text('fixture')
        (agents/'LEARNING_ARCHITECTURE.md').write_text('fixture')
        (agents/'scripts').mkdir(); (agents/'agents').mkdir()
        (agents/'agents/uni_fixture.toml').write_text('name = "uni_fixture"')
        shutil.copy(AGENTS/'scripts/sync_plugin.py',agents/'scripts/sync_plugin.py')
        spec=importlib.util.spec_from_file_location('fixture_sync',agents/'scripts/sync_plugin.py')
        mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        return mod

    def test_packaging_is_checkout_independent_and_preserves_other_agents(self):
        with tempfile.TemporaryDirectory() as tmp:
            first=Path(tmp)/'first'; second=Path(tmp)/'second'
            mod=self.fixture(first)
            custom=first/'.codex/agents/personal.toml';custom.parent.mkdir(parents=True)
            custom.write_text('unrelated user agent')
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            self.assertEqual(custom.read_text(),'unrelated user agent')
            shutil.copytree(first,second)
            spec=importlib.util.spec_from_file_location('second_sync',second/'03_Agents/scripts/sync_plugin.py')
            other=importlib.util.module_from_spec(spec);spec.loader.exec_module(other)
            with contextlib.redirect_stdout(io.StringIO()):other.run(check=True)
            inventory=json.loads((second/'03_Agents/plugins/uni-teach/package_inventory.json').read_text())
            self.assertEqual(inventory['source_root'],'03_Agents')

    def test_external_project_agent_edit_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);mod=self.fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            target=root/'.codex/agents/uni_fixture.toml';target.write_text('user changed this')
            source=root/'03_Agents/agents/uni_fixture.toml';source.write_text('new maintained version')
            package=root/'03_Agents/plugins/uni-teach/agents/uni_fixture.toml'
            old=package.read_bytes()
            with self.assertRaisesRegex(ValueError,'collision or external edit'):mod.run()
            self.assertEqual(target.read_text(),'user changed this');self.assertEqual(package.read_bytes(),old)

    def test_owned_profile_update_rebuilds_and_check_detects_missing_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);mod=self.fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            source=root/'03_Agents/agents/uni_fixture.toml';source.write_text('updated maintained version')
            with contextlib.redirect_stdout(io.StringIO()):mod.run();mod.run(check=True)
            target=root/'.codex/agents/uni_fixture.toml';self.assertEqual(target.read_bytes(),source.read_bytes())
            target.unlink()
            with self.assertRaisesRegex(ValueError,'project agent mismatch'):mod.run(check=True)

if __name__ == '__main__':
    unittest.main()
