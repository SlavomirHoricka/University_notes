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
            # Self-contained skills embed routing; they must preserve owner/helper dispatch guards.
            self.assertIn('delegated_owner: <profile>',text)
            self.assertIn('helper_role',text)
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

    def test_optional_html_skill_is_packaged_without_changing_existing_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);mod=self.fixture(root)
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            old={name:(mod.PACKAGE/'skills'/name/'SKILL.md').read_bytes()
                 for name in ('ingest','plan','teach','recall')}
            skill=mod.AGENTS/'html-course';(skill/'assets').mkdir(parents=True)
            (skill/'SKILL.md').write_text('new optional skill')
            (skill/'assets/runtime.js').write_text('offline renderer')
            manifest=mod.PACKAGE/'plugin.json';value=json.loads(manifest.read_text());value['version']='0.5.0'
            manifest.write_text(json.dumps(value))
            with contextlib.redirect_stdout(io.StringIO()):mod.run();mod.run(check=True)
            self.assertEqual((mod.PACKAGE/'skills/html-course/SKILL.md').read_text(),'new optional skill')
            self.assertEqual((mod.PACKAGE/'skills/html-course/assets/runtime.js').read_text(),'offline renderer')
            for name,data in old.items():self.assertEqual((mod.PACKAGE/'skills'/name/'SKILL.md').read_bytes(),data)

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
            with contextlib.redirect_stdout(io.StringIO()):mod.run(source_only=True);mod.run(check=True,source_only=True)
            target=root/'.codex/agents/uni_fixture.toml';self.assertEqual(target.read_bytes(),source.read_bytes())
            target.unlink()
            with self.assertRaisesRegex(ValueError,'project agent mismatch'):mod.run(check=True)

    def test_snapshot_is_required_readable_and_exact(self):
        for damage in ('missing','corrupt','mismatch'):
            with self.subTest(damage=damage),tempfile.TemporaryDirectory() as tmp:
                mod=self.fixture(Path(tmp))
                with contextlib.redirect_stdout(io.StringIO()):mod.run()
                archive=mod.AGENTS/'plugins/uni-teach-0.4.0.zip'
                if damage=='missing':archive.unlink()
                elif damage=='corrupt':archive.write_text('not a zip')
                else:
                    import zipfile
                    with zipfile.ZipFile(archive,'a') as z:z.writestr('unexpected','extra')
                with self.assertRaisesRegex(ValueError,'snapshot'):mod.run(check=True)
                with contextlib.redirect_stdout(io.StringIO()):mod.run(check=True,source_only=True)

    def test_existing_snapshot_is_preserved_and_new_version_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            mod=self.fixture(Path(tmp))
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            archive=mod.AGENTS/'plugins/uni-teach-0.4.0.zip';old=archive.read_bytes()
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            self.assertEqual(archive.read_bytes(),old)
            source=mod.AGENTS/'ingest/SKILL.md';source.write_text('changed source')
            dest=mod.PACKAGE/'skills/ingest/SKILL.md';before=dest.read_bytes()
            with self.assertRaisesRegex(ValueError,'new package version'):mod.run()
            self.assertEqual(archive.read_bytes(),old);self.assertEqual(dest.read_bytes(),before)
            with contextlib.redirect_stdout(io.StringIO()):mod.run(source_only=True)
            self.assertEqual(dest.read_bytes(),source.read_bytes());self.assertEqual(archive.read_bytes(),old)
            manifest=mod.PACKAGE/'plugin.json';value=json.loads(manifest.read_text());value['version']='0.4.1';manifest.write_text(json.dumps(value))
            with contextlib.redirect_stdout(io.StringIO()):mod.run();mod.run(check=True)
            self.assertTrue((archive.parent/'uni-teach-0.4.1.zip').is_file());self.assertEqual(archive.read_bytes(),old)

    def test_unexpected_generated_file_is_rejected_before_mutation(self):
        with tempfile.TemporaryDirectory() as tmp:
            mod=self.fixture(Path(tmp))
            with contextlib.redirect_stdout(io.StringIO()):mod.run()
            dest=mod.PACKAGE/'skills/ingest/SKILL.md';before=dest.read_bytes()
            (mod.AGENTS/'ingest/SKILL.md').write_text('changed')
            (mod.PACKAGE/'skills/ingest/stale.md').write_text('stale')
            with self.assertRaisesRegex(ValueError,'unexpected generated file'):mod.run(source_only=True)
            self.assertEqual(dest.read_bytes(),before)

if __name__ == '__main__':
    unittest.main()
