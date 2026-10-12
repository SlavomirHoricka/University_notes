"""Temporary miniature vault checks, never modifies actual notes."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import unittest

spec=importlib.util.spec_from_file_location('check_vault',Path(__file__).resolve().parents[1]/'check_vault.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class VaultTests(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.root=Path(self.temp.name)
        for n in ('00_Materials','01_Notes','02_Resources','03_Agents'):(self.root/n).mkdir()
    def tearDown(self):self.temp.cleanup()
    def put(self,name,text):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text);return p
    def test_unicode_headings_blocks_and_images(self):
        self.put('01_Notes/Cafe\u0301.md','# Café\n## Why this follows\nReason. ^proof\n')
        self.put('01_Notes/index.md','[[Café#Why this follows]]\n[[Café#^proof]]\n![figure](../02_Resources/figure.png)\n')
        self.put('02_Resources/figure.png','fixture')
        a=m.audit(self.root);self.assertEqual(a['missing_links'],[]);self.assertEqual(a['missing_anchors'],[]);self.assertEqual(a['markdown_link_issues'],[])
    def test_history_does_not_ambiguate_live_and_explicit_target_works(self):
        self.put('01_Notes/Topic.md','# Topic\n')
        self.put('03_Agents/history/old/Topic.md','# Old\n')
        self.put('03_Agents/README.md','[[Topic]]\n[[03_Agents/history/old/Topic.md]]\n')
        a=m.audit(self.root);self.assertEqual(a['ambiguous_links'],[]);self.assertEqual(a['agent_missing_links'],[])
    def test_mirror_only_counts_year_semester_course_and_missing_anchor(self):
        self.put('01_Notes/2026_2027/Winter_Semester/Course/Note.md','# Note\n[[#Missing]]\n')
        (self.root/'03_Agents/2026_2027/Winter_Semester/Course').mkdir(parents=True)
        (self.root/'03_Agents/plugins/pkg/skills').mkdir(parents=True)
        a=m.audit(self.root);self.assertEqual(a['course_mirror_difference'],[]);self.assertEqual(len(a['missing_anchors']),1)

if __name__=='__main__':unittest.main()
