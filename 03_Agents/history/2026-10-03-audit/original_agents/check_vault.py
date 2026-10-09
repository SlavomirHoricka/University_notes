"""Read-only naming/link check. Run: python3 03_Agents/check_vault.py.

Checks file targets, source metadata, hub names, and course-directory mirroring.
Reports missing concepts; it does not create notes or validate academic content.
"""
from pathlib import Path
from collections import defaultdict
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]

def canonical(value):
    return unicodedata.normalize('NFC', str(value))

def audit(root):
    index = defaultdict(set)
    for folder in ['00_Materials', '01_Notes', '02_Resources', '03_Agents']:
        for path in (root / folder).rglob('*'):
            if not path.is_file() or path.name.startswith('.'):
                continue
            rel = str(path.relative_to(root))
            keys = [rel, path.name]
            if path.suffix == '.md':
                keys += [rel[:-3], path.stem]
            for key in keys:
                index[canonical(key)].add(rel)
    missing, ambiguous, malformed, sources, naming = [], [], [], [], []
    total = 0
    for path in sorted((root / '01_Notes').rglob('*.md')):
        rel = str(path.relative_to(root))
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if line.startswith('Source: [[') and not line.endswith(']]'):
                malformed.append({'file': rel, 'line': number})
            if line.startswith('source:'):
                target = line.split(':', 1)[1].strip().strip('"\'')
                if target.startswith('00_Materials/') and not (root / target).is_file():
                    sources.append({'file': rel, 'line': number, 'target': target})
            for match in re.finditer(r'\[\[([^\[\]\n]+)\]\]', line):
                target = re.split(r'\\?\||#', match.group(1), maxsplit=1)[0]
                if not target:
                    continue
                total += 1
                hits = index.get(canonical(target), set())
                item = {'file': rel, 'line': number, 'target': target}
                if not hits:
                    missing.append(item)
                elif len(hits) > 1:
                    ambiguous.append(item)
        if path.stem.endswith('_Master') or path.stem.startswith('Main_-_'):
            naming.append(rel)
        if path.stem.endswith('_main') and canonical(path.stem) != canonical(path.parent.name + '_main'):
            naming.append(rel)
    notes = {canonical(p.relative_to(root / '01_Notes')) for p in (root / '01_Notes').glob('*/*/*') if p.is_dir()}
    agents = {canonical(p.relative_to(root / '03_Agents')) for p in (root / '03_Agents').glob('*/*/*') if p.is_dir()}
    return {'checked_links': total, 'missing_links': missing, 'ambiguous_links': ambiguous,
            'malformed_source_links': malformed, 'missing_source_metadata': sources,
            'nonstandard_hubs': naming, 'course_mirror_difference': sorted(notes ^ agents)}

if __name__ == '__main__':
    result = audit(ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(int(any(result[k] for k in result if k != 'checked_links')))
