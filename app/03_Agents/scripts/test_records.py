import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
import json

spec = importlib.util.spec_from_file_location('records', Path(__file__).with_name('records.py'))
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)

class RecordsTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory(); self.root = Path(self.temp.name)
    def tearDown(self): self.temp.cleanup()
    def test_ownership_paths_and_symlinks(self):
        for name in ['learning_log.md', '../learning_plan.md', './curriculum_history/v1/plan.md']:
            with self.assertRaises(ValueError): r.target(self.root,'plan',name)
        (self.root/'lessons').mkdir(); (self.root/'lessons/alias').symlink_to(self.root)
        with self.assertRaises(ValueError): r.target(self.root,'plan','lessons/alias/learning_log.md')
    def test_conflict_lock_and_success(self):
        tx=r.commit(self.root,'recall',{'recall_state.json':'{}'}, {'recall_state.json':None})
        self.assertTrue(r.status(self.root)['ready'])
        with self.assertRaises(ValueError):r.commit(self.root,'recall',{'recall_state.json':'new'}, {'recall_state.json':None})
        with r.lock(self.root,'teach'):
            with self.assertRaises(FileExistsError):r.commit(self.root,'recall',{'recall_state.json':'new'}, {'recall_state.json':r.digest(self.root/'recall_state.json')})
    def test_interrupted_two_file_recovery(self):
        original=r.atomic
        def fail(path, data):
            if Path(path).name=='source_manifest.md':raise OSError('simulated interruption')
            return original(path,data)
        with patch.object(r,'atomic',side_effect=fail):
            with self.assertRaises(OSError):r.commit(self.root,'plan',{'learning_plan.md':'plan','source_manifest.md':'manifest'}, {'learning_plan.md':None,'source_manifest.md':None},'T-recovery')
        self.assertFalse(r.status(self.root)['ready'])
        r.recover(self.root,'plan','T-recovery'); r.recover(self.root,'plan','T-recovery')
        self.assertEqual((self.root/'source_manifest.md').read_text(),'manifest');self.assertTrue(r.status(self.root)['ready'])
    def test_recovery_conflict_preserves_journal(self):
        with patch.object(r,'apply',side_effect=OSError('crash')):
            with self.assertRaises(OSError):r.commit(self.root,'recall',{'recall_state.json':'planned'},{'recall_state.json':None},'T-conflict')
        (self.root/'recall_state.json').write_text('human edit')
        with self.assertRaises(ValueError):r.recover(self.root,'recall','T-conflict')
        self.assertEqual((self.root/'recall_state.json').read_text(),'human edit');self.assertFalse(r.status(self.root)['ready'])
    def test_history_immutable(self):
        r.commit(self.root,'plan',{'curriculum_history/P1/plan.md':'old'},{'curriculum_history/P1/plan.md':None})
        with self.assertRaises(ValueError):r.commit(self.root,'plan',{'curriculum_history/P1/plan.md':'changed'},{'curriculum_history/P1/plan.md':r.digest(self.root/'curriculum_history/P1/plan.md')})
    def test_legacy_prefix_survives_schema3_append(self):
        p=self.root/'learning_log.md';old='Manual history\n```json\n{"schema_version":1}\n```\n';p.write_text(old)
        appended=old+'```json\n{"schema_version":3,"event_id":"E1","writer":"teach","event_type":"session_started"}\n```\n';r.check_history(p,appended);p.write_text(appended)
        with self.assertRaises(ValueError):r.check_history(p,appended.replace('Manual history','changed'))
    def test_event_order_payload_and_duplicate(self):
        p=self.root/'learning_log.md';head='<!-- uni-teach-log:3 -->\n```json\n{"schema_version":3,"owner":"teach"}\n```\n'
        a='```json\n{"event_id":"E1","outcome":"pass","writer":"teach","event_type":"attempt_result"}\n```\n';b='```json\n{"event_id":"E2","outcome":"fail","writer":"teach","event_type":"attempt_result"}\n```\n';p.write_text(head+a+b)
        for s in [head+b+a,head+a+b.replace('fail','pass'),head+a+b+a]:
            with self.assertRaises(ValueError):r.check_history(p,s)
        with self.assertRaises(ValueError):r.check_history(self.root/'absent',head+a+a)
        r.check_history(p,head+a+b)
    def test_yaml_only_and_crlf_legacy(self):
        p=self.root/'learning_log.md';old='Legacy\r\n~~~yaml\r\nschema_version: 2\r\n~~~\r\n'
        p.write_bytes(old.encode());added=old+'```json\n{"schema_version":3,"event_id":"E","writer":"teach","event_type":"session_started"}\n```\n'
        r.check_history(p,added);p.write_bytes(added.encode())
        with self.assertRaises(ValueError):r.check_history(p,added.replace('Legacy','edited'))
        with self.assertRaises(ValueError):r.check_history(p,added.replace('\r\n','\n'))

    def test_control_symlink_and_stage_corruption(self):
        outside=self.root/'external';outside.mkdir();(self.root/'.transactions').symlink_to(outside)
        with self.assertRaises(ValueError):r.commit(self.root,'recall',{'recall_state.json':'{}'},{'recall_state.json':None})
        (self.root/'.transactions').unlink()
        with patch.object(r,'apply',side_effect=OSError('crash')):
            with self.assertRaises(OSError):r.commit(self.root,'recall',{'recall_state.json':'planned'},{'recall_state.json':None},'T-corrupt')
        with self.assertRaises(ValueError):r.recover(self.root,'teach','T-corrupt')
        (self.root/'.transactions/T-corrupt/0.stage').write_text('corrupt')
        with self.assertRaises(ValueError):r.recover(self.root,'recall','T-corrupt')
        self.assertFalse((self.root/'recall_state.json').exists());self.assertFalse(r.status(self.root)['ready'])

    def test_event_owner_and_committed_record_verification(self):
        p=self.root/'learning_log.md'
        with self.assertRaises(ValueError):r.check_history(p,'```json\n{"event_id":"E","writer":"recall","event_type":"schedule_update"}\n```\n')
        tx=r.commit(self.root,'plan',{'learning_plan.md':'p','source_manifest.md':'m'}, {'learning_plan.md':None,'source_manifest.md':None})
        self.assertTrue(r.verify(self.root,'plan',tx,['learning_plan.md','source_manifest.md']))
        self.assertEqual(r.verify_record(self.root,'plan','learning_plan.md'),tx)
        self.assertFalse(r.verify(self.root,'teach',tx,['learning_log.md']))
        (self.root/'learning_plan.md').write_text('manual edit')
        self.assertFalse(r.verify(self.root,'plan',tx,['learning_plan.md']))
        self.assertIsNone(r.verify_record(self.root,'plan','learning_plan.md'))

    def test_numeric_type_changes_are_not_immutable_retries(self):
        p=self.root/'learning_log.md';head='<!-- uni-teach-log:3 -->\n```json\n{"schema_version":3,"owner":"teach"}\n```\n'
        event='```json\n{"event_id":"E","writer":"teach","event_type":"attempt_result","objective_revision":1}\n```\n'
        p.write_text(head+event)
        for changed in (event.replace('":1','":true'),event.replace('":1','":1.0')):
            with self.assertRaises(ValueError):r.check_history(p,head+changed)

if __name__=='__main__':unittest.main()
