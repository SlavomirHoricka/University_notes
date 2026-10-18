"""Fictional courses only: freshness, coverage and export-preservation behavior."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from urllib.parse import urljoin, urlsplit, unquote

import course as html

COURSE = '2026_2027/Winter_Semester/Fictional_HTML_Test'


def meta(data, body):
    return '# Fictional course\n\n```json\n' + json.dumps(data, indent=2) + '\n```\n\n' + body


def fixture(root):
    root = Path(root)
    record_source = next(p / 'scripts/records.py' for p in html.SKILL.parents if (p / 'scripts/records.py').is_file())
    scripts = root / '03_Agents/scripts'
    scripts.mkdir(parents=True)
    shutil.copyfile(record_source, scripts / 'records.py')
    records = html.records_for(root)
    directory = root / '03_Agents' / COURSE
    directory.mkdir(parents=True)
    note = '01_Notes/' + COURSE + '/Week_1/Mean.md'
    path = root / note
    path.parent.mkdir(parents=True)
    path.write_text('# Sample mean — fictional test\n\n## Definition\nFor n positive, the sample mean is the sum divided by n.\n\\[\\bar x=\\frac{1}{n}\\sum_{i=1}^n x_i.\\]\n\n## Worked example\nFor 1,2,3 the mean is 2.\n```r\n# Not a Markdown heading\nmean(c(1,2,3))\n```\n', encoding='utf-8')
    sha = html.digest(path.read_bytes())
    asset = '01_Notes/' + COURSE + '/assets/mean-data.csv'
    (root/asset).parent.mkdir(parents=True)
    (root/asset).write_text('x\n1\n2\n3\n')
    asset_sha = html.digest((root/asset).read_bytes())
    passed = '03_Agents/runtime/ingest/logs/fictional.md'
    (root / passed).parent.mkdir(parents=True)
    (root / passed).write_text('# Fictional complete pass\n\nDefinition and worked example checked; test fixture only.\n')
    state = {'schema_version': 1, 'owner': 'ingest', 'course_id': COURSE, 'ingestion_revision': 1,
             'transaction_id': 'INGEST-TEST', 'status': 'complete', 'completion_log': passed,
             'finished_notes': [{'path': note, 'sha256': sha, 'headings': ['Definition', 'Worked example']}],
             'finished_assets': [{'path': asset, 'sha256': asset_sha}]}
    records.commit(directory, 'ingest', {'ingestion_state.json': json.dumps(state)}, {'ingestion_state.json': None}, 'INGEST-TEST')
    base = {'schema_version': 3, 'owner': 'plan', 'course_id': COURSE, 'plan_version': 'P001',
            'source_version': 'V001', 'ingestion_revision': 1, 'transaction_id': 'PLAN-TEST'}
    objectives = [{'objective_id': oid, 'objective_revision': 1, 'criterion_version': oid+'-C1',
                   'lesson_path': 'lessons/'+oid+'.md', 'status': 'ready', 'title': 'Calculate a sample mean',
                   'prerequisite_ids': ['O001'] if oid == 'O002' else []} for oid in ['O001', 'O002']]
    plan = {**base, 'plan_status': 'ready', 'objectives': objectives}
    manifest = {**base, 'ingestion_pass_refs': [passed], 'entries': [{'path': note, 'sha256': sha,
                'note_sections': ['Definition', 'Worked example'], 'objective_ids': ['O001', 'O002']},
                {'path': asset, 'sha256': asset_sha, 'objective_ids': ['O001','O002']}]}
    changes = {'learning_plan.md': meta(plan, 'Prepared fictional mean example.'),
               'source_manifest.md': meta(manifest, 'Fictional complete note mapping.')}
    body = '## Outcome and conditions\nCalculate a mean for a nonempty finite sample.\n\n## Explanation\nAdd every value and divide by the number of values.\\[\\bar x=\\frac{1}{n}\\sum_i x_i.\\]\n\n## Practice\nFor 1,2,3 calculate the mean. Key: (1+2+3)/3=2.\n'
    for objective in objectives:
        lesson = {**base, **objective, 'note_locations': [{'path': note, 'heading': h} for h in ['Definition', 'Worked example']]}
        changes[objective['lesson_path']] = meta(lesson, body)
    records.commit(directory, 'plan', changes, {name: None for name in changes}, 'PLAN-TEST')
    return directory, note


def draft_for(snap):
    lessons = []
    for i, objective in enumerate(snap['objectives']):
        oid = objective['objective_id']
        lessons.append({'id': oid.lower(), 'title': 'Understand the sample mean', 'subtitle': 'Fictional validation lesson',
                        'description': 'Complete tiny example for utility tests.', 'week': 1,
                        'objective_ids': [oid], 'prerequisite_lessons': ['o001'] if oid == 'O002' else [],
                        'sections': [{'id': 'idea', 'title': 'The idea',
                         'html': '<p>For a nonempty finite sample, add all observations and divide by their number.</p><div class="equation">\\[\\bar x=\\frac{1}{n}\\sum_{i=1}^{n}x_i.\\]</div><p>For \\(1,2,3\\), the mean is \\(2\\).</p>',
                         'interactions': [{'id': oid.lower()+'-answer', 'kind': 'numeric', 'answer': 2, 'tolerance': 1e-6,
                          'prompt_html': '<p>Calculate the mean of \\(1,2,3\\).</p>', 'solution_html': '<p>\\((1+2+3)/3=2\\).</p>'}]}]})
    return {'course_id': snap['course_id'], 'title': 'Fictional HTML validation', 'language': 'en',
            'source_fingerprint': snap['fingerprint'], 'scope': 'Fictional mean example, Week 1. Not real course evidence.',
            'lessons': lessons, 'coverage': [{'source': unit['key'], 'disposition': 'included',
             'targets': [(next((l['id'] for l in lessons if '/'+l['id'].upper()+'.md#' in unit['key']), lessons[0]['id']))+'#idea']}
             for unit in snap['source_units']], 'assets': [], 'custom_scripts': []}


def reports(manifest):
    common = {'status': 'passed', 'reviewer': 'fictional-test-reviewer', 'candidate_digest': manifest['candidate_digest'],
              'evidence': 'Fictional unit-test acceptance data; not an actual academic/browser review.', 'findings': []}
    return ({**common, 'kind': 'academic', 'objective_ids': manifest['objective_ids']},
            {**common, 'kind': 'browser', 'checks': {k: True for k in ['links','math','interactions','desktop','compact','offline_dependencies']}})


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.vault = self.base / 'vault'
        self.directory, self.note = fixture(self.vault)

    def candidate(self, ids=None, name='candidate'):
        snap = html.snapshot(self.vault, COURSE, ids or ['O002'])
        draft = draft_for(snap)
        destination = self.base / name
        manifest = html.build(self.vault, snap, draft, self.base/'draft.json', destination)
        return snap, draft, destination, manifest

    def test_snapshot_closes_prerequisites_preserves_code_and_does_not_write_records(self):
        before = {p: p.read_bytes() for p in self.directory.rglob('*') if p.is_file()}
        snap = html.snapshot(self.vault, COURSE, ['O002'])
        self.assertEqual([o['objective_id'] for o in snap['objectives']], ['O001','O002'])
        unit = next(u for u in snap['source_units'] if u['heading']=='Worked example')
        self.assertIn('mean(c(1,2,3))', unit['text'])
        self.assertNotIn('Not a Markdown heading', [u['heading'] for u in snap['source_units']])
        self.assertEqual(before, {p: p.read_bytes() for p in self.directory.rglob('*') if p.is_file()})

    def test_fenced_code_is_preserved_without_becoming_section_boundaries(self):
        for opener,closer in [('~~~r','~~~'),('````r','````'),('   ~~~~r','   ~~~~')]:
            text='## Worked example\nBefore.\n'+opener+'\n## R comment, not a heading\nmean(c(1,2,3))\n'+closer+'\nInterpret the denominator.\n## Next\nOther content.'
            with self.subTest(opener=opener):
                extracted=html.section(text,'Worked example')
                self.assertIn('mean(c(1,2,3))',extracted)
                self.assertIn('Interpret the denominator.',extracted)
                self.assertNotIn('Other content.',extracted)
                self.assertEqual([m.group(2) for m in html.headings(text)[0]],['Worked example','Next'])

    def test_stale_note_and_unchecked_heading_block(self):
        path = self.vault / self.note
        original = path.read_bytes()
        path.write_bytes(original+b'\nChanged academic content.')
        with self.assertRaisesRegex(ValueError, 'stale note'):
            html.snapshot(self.vault, COURSE, ['O001'])
        path.write_bytes(original)
        with self.assertRaisesRegex(ValueError, 'missing or ambiguous'):
            html.section(original.decode(), 'Unverified topic')

    def test_pending_or_locked_inputs_block(self):
        lock = self.directory/'.learning-write.lock'
        lock.mkdir()
        with self.assertRaisesRegex(ValueError, 'locked'):
            html.snapshot(self.vault, COURSE, ['O001'])
        lock.rmdir()
        pending = self.directory/'.transactions/PENDING'
        pending.mkdir()
        (pending/'journal.json').write_text(json.dumps({'owner':'plan','status':'prepared'}))
        with self.assertRaisesRegex(ValueError, 'pending'):
            html.snapshot(self.vault, COURSE, ['O001'])

    def test_changed_or_unchecked_assets_cannot_be_adopted_by_snapshot(self):
        asset='01_Notes/'+COURSE+'/assets/mean-data.csv'
        snap=html.snapshot(self.vault,COURSE,['O001'],[asset])
        self.assertIn(asset,snap['source_files'])
        (self.vault/asset).write_text('x\n100\n200\n')
        with self.assertRaisesRegex(ValueError,'stale or unchecked asset'):
            html.snapshot(self.vault,COURSE,['O001'],[asset])

    def test_coverage_and_week_and_prerequisite_routes_are_required(self):
        snap=html.snapshot(self.vault,COURSE,['O002'])
        draft=draft_for(snap)
        bad=copy.deepcopy(draft);bad['coverage'].pop()
        with self.assertRaisesRegex(ValueError,'coverage map'):html.validate_draft(bad,snap)
        bad=copy.deepcopy(draft);bad['coverage'][0].update(disposition='operational_only',reason='shorter')
        with self.assertRaisesRegex(ValueError,'academic content'):html.validate_draft(bad,snap)
        bad=copy.deepcopy(draft);bad['lessons'][0]['week']=3
        with self.assertRaisesRegex(ValueError,'week not established'):html.validate_draft(bad,snap)
        bad=copy.deepcopy(draft);bad['lessons'][1]['prerequisite_lessons']=[]
        with self.assertRaisesRegex(ValueError,'prerequisite link'):html.validate_draft(bad,snap)

    def test_custom_active_html_and_network_resources_block(self):
        for content in ['<script>alert(1)</script>','<p onclick="x()">x</p>','<img src="https://example.org/a.png">','<a href="javascript:x()">x</a>']:
            with self.subTest(content=content), self.assertRaises(ValueError):html.fragment(content)
        _,_,candidate,_=self.candidate()
        (candidate/'assets/custom.css').write_text('@import "https://example.org/a.css";')
        with self.assertRaisesRegex(ValueError,'CSS imports'):html.check_html(candidate)

    def test_review_digest_scope_and_browser_gates(self):
        _,_,candidate,manifest=self.candidate()
        review,qa=reports(manifest)
        for bad in [{**review,'candidate_digest':'wrong'},{**review,'objective_ids':['O001']},{**review,'findings':['unresolved']}]:
            with self.assertRaises(ValueError):html.publish(self.vault,candidate,bad,qa)
        qa['checks']['math']=False
        with self.assertRaisesRegex(ValueError,'browser QA'):html.publish(self.vault,candidate,review,qa)
        self.assertFalse((self.vault/'02_Resources').exists())

    def test_publication_retry_is_idempotent_and_prior_version_is_preserved(self):
        snap,draft,candidate,manifest=self.candidate()
        review,qa=reports(manifest)
        result=html.publish(self.vault,candidate,review,qa)
        first=Path(result['version']); files={p:p.read_bytes() for p in first.rglob('*') if p.is_file()}
        index=Path(result['index']);base=__import__('re').search(r'<base href="([^"]+)">',index.read_text()).group(1)
        skip=urljoin(urljoin(index.as_uri(),base),'#main')
        self.assertTrue(Path(unquote(urlsplit(skip).path)).is_file())
        repeat=html.publish(self.vault,candidate,review,qa)
        self.assertEqual(repeat['changed_files'],[])
        self.assertEqual(first,Path(repeat['version']))
        draft['lessons'][1]['sections'][0]['html']+='<p>An additional wording clarification of the same example.</p>'
        next_candidate=self.base/'next'
        second=html.build(self.vault,snap,draft,self.base/'draft.json',next_candidate)
        changed=html.publish(self.vault,next_candidate,*reports(second))
        self.assertNotEqual(result['version'],changed['version'])
        self.assertEqual(files,{p:p.read_bytes() for p in first.rglob('*') if p.is_file()})
        self.assertIn('lessons/o002.html',changed['changed_files'])
        self.assertNotIn('lessons/o001.html',changed['changed_files'])

    def test_changed_source_after_candidate_blocks_activation(self):
        _,_,candidate,manifest=self.candidate()
        note=self.vault/self.note;note.write_text(note.read_text()+'\nChanged.\n')
        with self.assertRaisesRegex(ValueError,'stale note'):
            html.publish(self.vault,candidate,*reports(manifest))

    def test_external_candidate_or_live_edits_are_preserved(self):
        _,_,candidate,manifest=self.candidate()
        result=html.publish(self.vault,candidate,*reports(manifest))
        live=Path(result['index']);live.write_bytes(live.read_bytes()+b'\nHuman edit.')
        with self.assertRaisesRegex(ValueError,'externally edited'):
            html.publish(self.vault,candidate,*reports(manifest))
        self.assertTrue(live.read_bytes().endswith(b'Human edit.'))
        (candidate/'lessons/o001.html').write_text('Human draft edit')
        with self.assertRaisesRegex(ValueError,'bytes changed'):html.checked_tree(candidate)

    def test_unexpected_files_locks_stages_and_protected_destinations_are_preserved(self):
        snap,draft,candidate,manifest=self.candidate()
        for name in ['01_Notes/course-output','03_Agents/course-output']:
            with self.assertRaisesRegex(ValueError,'protected'):
                html.publish(self.vault,candidate,*reports(manifest),output=self.vault/name)
        result=html.publish(self.vault,candidate,*reports(manifest));root=Path(result['index']).parent
        extra=root/'my-notes.txt';extra.write_text('Human notes')
        with self.assertRaisesRegex(ValueError,'unexpected export-root'):html.publish(self.vault,candidate,*reports(manifest))
        extra.unlink();lock=root/'.html-course.lock';lock.mkdir()
        with self.assertRaises(FileExistsError):html.publish(self.vault,candidate,*reports(manifest))
        self.assertTrue(lock.exists());lock.rmdir()
        stage=root/'versions/.stage-unfinished';stage.mkdir()
        with self.assertRaisesRegex(ValueError,'unfinished export stage'):html.publish(self.vault,candidate,*reports(manifest))
        self.assertTrue(stage.exists())

    def test_refresh_does_not_silently_drop_an_exported_week_or_objective(self):
        _,_,candidate,manifest=self.candidate()
        first=html.publish(self.vault,candidate,*reports(manifest))
        _,_,narrow,narrow_manifest=self.candidate(['O001'],'narrow')
        with self.assertRaisesRegex(ValueError,'drop previously exported scope'):
            html.publish(self.vault,narrow,*reports(narrow_manifest))
        accepted=html.publish(self.vault,narrow,*reports(narrow_manifest),allow_scope_reduction=True)
        self.assertTrue(Path(first['version']).exists())
        self.assertNotEqual(first['version'],accepted['version'])

    def test_nested_output_cannot_recursively_copy_its_candidate(self):
        _,_,candidate,manifest=self.candidate()
        nested=candidate/'nested-export'
        with self.assertRaisesRegex(ValueError,'must not overlap'):
            html.publish(self.vault,candidate,*reports(manifest),output=nested)
        self.assertFalse(nested.exists())

    def test_candidate_only_directory_is_not_reused_as_a_published_version(self):
        _,_,candidate,manifest=self.candidate()
        output=self.base/'export'
        versions=output/'versions';versions.mkdir(parents=True)
        incomplete=versions/('b-'+manifest['candidate_digest'])
        shutil.copytree(candidate,incomplete)
        with self.assertRaisesRegex(ValueError,'not a complete reviewed publication'):
            html.publish(self.vault,candidate,*reports(manifest),output=output)
        self.assertFalse((output/'index.html').exists())

    def test_incomplete_saved_reports_block_reactivation(self):
        _,_,candidate,manifest=self.candidate()
        result=html.publish(self.vault,candidate,*reports(manifest))
        output=Path(result['index']).parent
        (output/'index.html').unlink()
        version=Path(result['version'])
        minimal={'status':'passed','candidate_digest':manifest['candidate_digest']}
        published=html.load(version/'manifest.json')
        for name in ['reviews/academic.json','reviews/browser.json']:
            (version/name).write_bytes(html.encoded(minimal))
            published['publication_files'][name]=html.digest(html.encoded(minimal))
        (version/'manifest.json').write_bytes(html.encoded(published))
        with self.assertRaisesRegex(ValueError,'separate academic and browser reports'):
            html.publish(self.vault,candidate,*reports(manifest))
        self.assertFalse((output/'index.html').exists())

    def test_metadata_omission_and_cross_week_navigation(self):
        snap=html.snapshot(self.vault,COURSE,['O001']);draft=draft_for(snap)
        unit={'key':'metadata','kind':'lesson','heading':'Record metadata'}
        snap['source_units'].append(unit)
        draft['coverage'].append({'source':'metadata','disposition':'operational_only','reason':'Machine record header; not academic content.'})
        html.validate_draft(draft,snap)
        draft['lessons'][0]['additional_weeks']=[2]
        nav=html.navigation(draft,'o001','../')
        self.assertIn('Week 02',nav)
        self.assertIn('Also: Understand the sample mean',nav)

    def test_broken_links_and_duplicate_ids_block_candidates(self):
        snap=html.snapshot(self.vault,COURSE,['O001']);draft=draft_for(snap)
        draft['lessons'][0]['sections'][0]['html']+='<a href="missing.html">Missing lesson</a>'
        with self.assertRaisesRegex(ValueError,'broken/escaping'):
            html.build(self.vault,snap,draft,self.base/'draft.json',self.base/'broken')
        draft=draft_for(snap);draft['lessons'][0]['sections'][0]['html']+='<p id="idea">Duplicate anchor</p>'
        with self.assertRaisesRegex(ValueError,'duplicate HTML'):
            html.build(self.vault,snap,draft,self.base/'draft.json',self.base/'duplicate')


if __name__=='__main__':unittest.main()
