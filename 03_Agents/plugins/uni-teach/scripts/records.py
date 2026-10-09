"""Owner-scoped optimistic writes with an inspectable, recoverable journal.

CLI: records.py status COURSE | commit COURSE OWNER DRAFT_JSON |
     recover COURSE OWNER TRANSACTION_ID
Draft: {"changes": {relative_path: text}, "expected": {path: sha256_or_null}}.
No connector calls and no learning/scheduling decisions.
"""
from contextlib import contextmanager
from pathlib import Path
import hashlib
import json
import os
import re
import socket
import sys
import uuid
from datetime import datetime, timezone


def digest(path):
    path = Path(path)
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def atomic(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name('.' + path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        with temp.open('xb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
        fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    finally:
        temp.unlink(missing_ok=True)


@contextmanager
def lock(course, owner):
    course = Path(course)
    course.mkdir(parents=True, exist_ok=True)
    directory = course / '.learning-write.lock'
    directory.mkdir()  # held lock raises; never expire it automatically
    token = uuid.uuid4().hex
    metadata = {'owner': owner, 'token': token, 'pid': os.getpid(),
                'host': socket.gethostname(), 'created_at': datetime.now(timezone.utc).isoformat()}
    try:
        atomic(directory / 'owner.json', json.dumps(metadata).encode())
        yield token
    finally:
        record = directory / 'owner.json'
        if record.exists() and json.loads(record.read_text()).get('token') == token:
            record.unlink()
            directory.rmdir()


def target(course, owner, name):
    rel = Path(name)
    if rel.is_absolute() or '..' in rel.parts or not rel.parts or name != rel.as_posix():
        raise ValueError('unsafe relative path')
    allowed = {'ingest': {'ingestion_state.json'}, 'teach': {'learning_log.md'},
               'recall': {'recall_state.json'}, 'plan': {'learning_plan.md', 'source_manifest.md'}}
    if Path(course).name == 'recall' and Path(course).parent.name == 'runtime':
        allowed['recall'] = {'project_map.json'}
    if owner not in allowed:
        raise ValueError('unknown owner')
    if name not in allowed[owner] and not (owner == 'plan' and
            len(rel.parts) > 1 and rel.parts[0] in {'lessons', 'curriculum_history'}):
        raise ValueError(f'{owner} does not own {name}')
    course = Path(course).resolve()
    p = course / rel
    if any((course.joinpath(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts) + 1)) or not p.resolve().is_relative_to(course):
        raise ValueError('symlink/path escape')
    return p


def events(text):
    return [o for s in re.findall(r'```json\s*\n(.*?)\n```', text, re.S)
            if isinstance(o := json.loads(s), dict) and o.get('event_id')]


def check_history(path, new):
    if new.startswith('<!-- uni-teach-log:3 -->\n'):
        h = re.search(r'```json\s*\n(.*?)\n```', new, re.S)
        m = json.loads(h.group(1)) if h else {}
        if m.get('schema_version') != 3 or m.get('owner') != 'teach' or m.get('event_id'):
            raise ValueError('invalid schema3 metadata')
    following = events(new)
    ids = [o['event_id'] for o in following]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate event id')
    prior = events(path.read_bytes().decode('utf-8')) if path.exists() else []
    prior_ids = {o['event_id'] for o in prior}
    allowed_events = {'session_started', 'session_route', 'session_paused', 'session_closed',
                      'attempt_started', 'attempt_result', 'attempt_abandoned', 'instruction_or_feedback',
                      'exposure_reported', 'acquisition_met', 'reassessment_met', 'plan_issue',
                      'note_issue', 'correction'}
    for event in following:
        if event['event_id'] not in prior_ids:
            if event.get('writer') != 'teach' or event.get('event_type') not in allowed_events:
                raise ValueError('new events must be teach-owned learner/session events')
    if not path.exists():
        return
    old = path.read_bytes().decode('utf-8')
    header = re.search(r'```json\s*\n(.*?)\n```', old, re.S)
    metadata = json.loads(header.group(1)) if header else {}
    is_new_format = (old.startswith('<!-- uni-teach-log:3 -->\n') and
                     metadata.get('schema_version') == 3 and metadata.get('owner') == 'teach' and
                     not metadata.get('event_id'))
    if is_new_format and not new.startswith('<!-- uni-teach-log:3 -->\n'):
        raise ValueError('schema3 format marker must remain')
    # Legacy remains byte-for-byte even after appended new metadata/events.
    if not is_new_format and not new.startswith(old):
        raise ValueError('legacy log must remain an exact prefix')
    prior = events(old)
    if ids[:len(prior)] != [o['event_id'] for o in prior]:
        raise ValueError('existing event order is immutable')
    lookup = {o['event_id']: o for o in following}
    if any(json.dumps(lookup.get(o['event_id']), sort_keys=True) != json.dumps(o, sort_keys=True) for o in prior):
        raise ValueError('learner history cannot be deleted or reinterpreted')


def status(course):
    course = Path(course)
    if (course / '.transactions').is_symlink():
        raise ValueError('transaction directory symlink')
    pending = []
    for p in sorted((course / '.transactions').glob('*/journal.json')):
        if p.is_symlink() or p.parent.is_symlink():
            raise ValueError('transaction journal symlink')
        j = json.loads(p.read_text())
        if j['status'] != 'committed':
            pending.append({'transaction_id': p.parent.name, 'owner': j['owner'], 'status': j['status']})
    return {'locked': (course / '.learning-write.lock').exists(), 'pending': pending,
            'ready': not pending and not (course / '.learning-write.lock').exists()}


def verify(course, owner, transaction_id, names):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', transaction_id):
        raise ValueError('invalid transaction id')
    if not status(course)['ready']:
        return False
    folder = Path(course) / '.transactions' / transaction_id
    if folder.is_symlink() or (folder / 'journal.json').is_symlink():
        raise ValueError('transaction journal symlink')
    j = json.loads((folder / 'journal.json').read_text())
    return j['owner'] == owner and j['status'] == 'committed' and all(
        name in j['files'] and digest(target(course, owner, name)) == j['files'][name]['new_sha256']
        for name in names)


def verify_record(course, owner, name):
    """Find a committed journal that exactly matches this current owned record."""
    if not status(course)['ready']:
        return None
    for p in sorted((Path(course) / '.transactions').glob('*/journal.json')):
        j = json.loads(p.read_text())
        if j['owner'] == owner and j['status'] == 'committed' and name in j['files']:
            if digest(target(course, owner, name)) == j['files'][name]['new_sha256']:
                return p.parent.name
    return None


def apply(course, folder, j):
    for name, entry in j['files'].items():
        p = target(course, j['owner'], name)
        staged = folder / entry['stage']
        if not re.fullmatch(r'\d+\.stage', entry['stage']) or staged.is_symlink():
            raise ValueError('invalid staged path')
        if digest(staged) != entry['new_sha256']:
            raise ValueError('staged bytes corrupt')
        current = digest(p)
        if current not in (entry['expected'], entry['new_sha256']):
            raise ValueError(f'conflict recovering {name}; preserve journal')
        if current != entry['new_sha256']:
            atomic(p, staged.read_bytes())
    j['status'] = 'committed'
    atomic(folder / 'journal.json', json.dumps(j, indent=2).encode())


def commit(course, owner, changes, expected, transaction_id=None):
    course = Path(course)
    if not changes or set(changes) != set(expected):
        raise ValueError('every change requires an expected hash (null for absent)')
    tx = transaction_id or 'T-' + uuid.uuid4().hex
    if not re.fullmatch(r'[A-Za-z0-9_-]+', tx):
        raise ValueError('invalid transaction id')
    with lock(course, owner):
        if status(course)['pending']:
            raise ValueError('recover unfinished transaction first')
        for name, content in changes.items():
            p = target(course, owner, name)
            if digest(p) != expected[name]:
                raise ValueError(f'changed since read: {name}')
            if owner == 'plan' and Path(name).parts[0] == 'curriculum_history' and p.exists():
                if p.read_bytes() != content.encode('utf-8'):
                    raise ValueError('curriculum history is immutable')
            if owner == 'teach':
                check_history(p, content)
        folder = course / '.transactions' / tx
        folder.mkdir(parents=True)
        j = {'owner': owner, 'status': 'prepared', 'files': {}}
        for i, (name, content) in enumerate(changes.items()):
            stage = f'{i}.stage'
            data = content.encode('utf-8')
            atomic(folder / stage, data)
            j['files'][name] = {'stage': stage, 'expected': expected[name],
                                'new_sha256': hashlib.sha256(data).hexdigest()}
        atomic(folder / 'journal.json', json.dumps(j, indent=2).encode())
        apply(course, folder, j)
    return tx


def recover(course, owner, tx):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', tx):
        raise ValueError('invalid transaction id')
    with lock(course, owner):
        if (Path(course) / '.transactions').is_symlink():
            raise ValueError('transaction directory symlink')
        folder = Path(course) / '.transactions' / tx
        if folder.is_symlink() or (folder / 'journal.json').is_symlink():
            raise ValueError('transaction journal symlink')
        j = json.loads((folder / 'journal.json').read_text())
        if j['owner'] != owner:
            raise ValueError('only transaction owner can recover')
        apply(course, folder, j)
    return tx


if __name__ == '__main__':
    command, course, *args = sys.argv[1:]
    if command == 'status':
        print(json.dumps(status(course), indent=2))
    elif command == 'commit':
        owner, draft_path = args
        draft = json.loads(Path(draft_path).read_text())
        print(commit(course, owner, **draft))
    elif command == 'recover':
        print(recover(course, *args))
    elif command == 'verify':
        owner, tx, *names = args
        if not names:
            raise SystemExit('verify requires owned record names')
        valid = verify(course, owner, tx, names)
        print(json.dumps({'verified': valid}))
        raise SystemExit(0 if valid else 1)
    elif command == 'verify-record':
        tx = verify_record(course, *args)
        print(json.dumps({'verified': tx is not None, 'transaction_id': tx}))
        raise SystemExit(0 if tx else 1)
    else:
        raise SystemExit('unknown command')
