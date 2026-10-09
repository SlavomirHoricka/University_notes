"""Bounded curriculum contract/arithmetic check; never writes learner records/tasks."""
from pathlib import Path
import hashlib
import json
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

BASE = Path(__file__).resolve().parent
VAULT = BASE.parents[2]
sys.path.insert(0, str(VAULT / '03_Agents/scripts'))
import records


def metadata(path):
    return json.loads(re.search(r'```json\s*\n(.*?)\n```', path.read_text(), re.S)[1])


def check():
    plan = metadata(BASE / 'learning_plan.md')
    manifest = metadata(BASE / 'source_manifest.md')
    fields = ['course_id', 'transaction_id', 'plan_version', 'source_version', 'ingestion_revision']
    assert all(plan[f] == manifest[f] for f in fields)
    assert plan['validation_artifact'] and not plan['production_ready']
    note = VAULT / manifest['entries'][0]['path']
    assert hashlib.sha256(note.read_bytes()).hexdigest() == manifest['entries'][0]['sha256']
    headings = re.findall(r'^#{1,6} (.+)$', note.read_text(), re.M)
    assert all(h in headings for h in manifest['entries'][0]['note_sections'])
    lessons = {}
    required = ['Outcome and conditions', 'Prerequisites and checks', 'Teaching order and rationale',
                'Motivation, intuition, and definitions', 'Explanation steps', 'Worked example',
                'Practice with fading assistance', 'Rubric and independence',
                'Misconceptions and correction', 'Immediate and delayed checks',
                'Advance, revisit, pause, and escalate', 'Answer-free recall handoff']
    for objective in plan['objectives']:
        path = BASE / objective['lesson_path']
        lesson = metadata(path)
        assert all(plan[f] == lesson[f] for f in fields)
        assert lesson['criterion_version'] == objective['criterion_version']
        assert lesson['objective_revision'] == objective['objective_revision']
        assert lesson['delayed_rule']['minimum_elapsed_hours'] == 24
        assert lesson['acquisition_rule']['distinct_independent_passes'] == 2
        assert set(required).issubset(set(re.findall(r'^## (.+)$', path.read_text(), re.M)))
        assert all(s.split('#', 1)[1] in headings for s in lesson['note_locations'])
        assert all((VAULT / s.split('#', 1)[0]).exists() for s in lesson['note_locations'])
        assert 'Key' in path.read_text() and 'Pass' in path.read_text()
        lessons[lesson['objective_id']] = lesson
    seen = set()
    def visit(oid, pending):
        assert oid not in pending, 'dependency cycle'
        if oid in seen:
            return
        for pre in lessons[oid]['prerequisite_ids']:
            assert pre in lessons
            visit(pre, pending | {oid})
        seen.add(oid)
    for oid in lessons:
        visit(oid, set())
    # Independent arithmetic recomputation of every prepared quantitative case.
    cases = [
        (10000, 1000, 20, 30, 25, 30, 0, 5000, -5000, -10000),  # W1
        (6000, 600, 10, 20, 15, 20, 0, 3000, -3000, -6000),    # F1
        (8000, 400, 15, 35, 25, 35, 0, 4000, -4000, -8000),    # I1
        (5000, 200, 10, None, 8, 35, None, -400, -5400, -5000), # I2
        (9000, 300, 12, 42, 22, 42, 0, 3000, -6000, -9000),    # C1
        (12000, 800, 5, 20, 14, 20, 0, 7200, -4800, -12000),   # D1
        (4000, 100, 6, None, 6, 46, None, 0, -4000, -4000),     # D2
    ]
    for initial, q, c, promise, cut, breakeven, total, surplus, produce, refuse in cases:
        assert c + initial / q == breakeven
        assert (cut - c) * q == surplus
        assert surplus - initial == produce and -initial == refuse
        assert produce - refuse == surplus
        if promise is not None:
            assert (promise - c) * q - initial == total
    local = ZoneInfo('Europe/Prague')
    exposure = datetime.fromisoformat('2026-10-03T21:00:00+02:00')
    early = datetime.fromisoformat('2026-10-04T08:00:00+02:00')
    delayed = datetime.fromisoformat('2026-10-04T21:30:00+02:00')
    overdue = datetime.fromisoformat('2026-10-07T21:30:00+02:00')
    assert (early - exposure).total_seconds() / 3600 == 11
    assert (delayed - exposure).total_seconds() / 3600 == 24.5
    assert (overdue - exposure).total_seconds() / 3600 == 96.5
    # Calendar midnight and DST do not by themselves satisfy 24 elapsed hours.
    autumn_a = datetime.fromisoformat('2026-10-24T23:30:00+02:00')
    autumn_b = datetime.fromisoformat('2026-10-25T23:00:00+01:00')
    assert (autumn_b - autumn_a).total_seconds() / 3600 == 24.5
    assert autumn_b.astimezone(local).date().isoformat() == '2026-10-25'
    status = records.status(BASE)
    assert status['ready'], status
    names = ['learning_plan.md', 'source_manifest.md'] + [o['lesson_path'] for o in plan['objectives']]
    assert records.verify(BASE, 'plan', plan['transaction_id'], names), 'bundle journal does not verify'
    # Exact P001/P002 definitions remain journaled, without retroactive criteria edits.
    for prior_version, archive_tx in [('P001', 'VALIDATION-PLAN-002'), ('P002', 'VALIDATION-PLAN-003'), ('P003', 'VALIDATION-PLAN-004'), ('P004', 'VALIDATION-PLAN-005')]:
        journal=json.loads((BASE/'.transactions'/archive_tx/'journal.json').read_text())
        frozen=[name for name in journal['files'] if name.startswith(f'curriculum_history/{prior_version}/')]
        assert len(frozen)==4
        for name in frozen:
            assert hashlib.sha256((BASE/name).read_bytes()).hexdigest()==journal['files'][name]['new_sha256']
        for oid in ('O001','O002'):
            prior=metadata(BASE/'curriculum_history'/prior_version/'lessons'/f'{oid}.md')
            assert prior['objective_revision']==lessons[oid]['objective_revision']
            assert prior['criterion_version']==('O001-C2' if prior_version in {'P003','P004'} and oid=='O001' else f'{oid}-C1')
    assert lessons['O001']['criterion_version']=='O001-C2'
    assert lessons['O002']['criterion_version']=='O002-C1'
    assert plan['objectives'][0]['reassessment_requirement']['requirement_id']=='G-O001-C2'
    # Regression for the reviewed alternate-route gap: all mechanism substitutes
    # explicitly prompt and key the remedy + limitation, alongside the timing chain.
    text=(BASE/'lessons/O001.md').read_text()
    c1=text.split('**O001-C1 v2, fresh mechanism follow-up:**',1)[1].split('\n\n',1)[0]
    d1=text.split('**O001-D1 v2, delayed mechanism:**',1)[1].split('\n\n',1)[0]
    d2=text.split('**O001-D2 v2, delayed discrimination:**',1)[1].split('\n\n',1)[0]
    assert 'Give one remedy and its limitation' in c1 and 'Pass requires that remedy and its limitation' in c1
    assert 'what limits that remedy' in d1 and 'remedy + its limitation' in d1
    assert 'defects the buyer cannot observe' in d2 and 'hidden-before-exchange information contrast' in d2
    assert 'no automatic-collapse claim' in d2
    assert 'O001-D2 v2' in plan['objectives'][0]['reassessment_requirement']['prepared_item_ids']
    assert 'reassessment_met' in (BASE/'REHEARSAL.md').read_text()
    print('PASS: provenance/hash/anchors, committed tuples, 2 objective contracts, exact P001–P004 history, O001-C2 assessment route repairs, dependency graph, 7 arithmetic keys, early/delayed/overdue/DST boundaries. Contract check only; no learner or connector writes.')


if __name__ == '__main__':
    check()
