"""Read-only live vault path/heading/block audit; historical/generated copies excluded.

Run from any cwd: python3 /absolute/vault/03_Agents/check_vault.py.
Does not certify academic content or PDF page bounds. Template placeholders skipped.
"""
from pathlib import Path
from collections import defaultdict
import json
import re
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def canonical(value):
    return unicodedata.normalize('NFC', str(value))


def excluded(path, root):
    rel = path.relative_to(root).parts
    return (any(p.startswith('.') or p == '__pycache__' for p in rel)
            or (rel[0] == '03_Agents' and len(rel) > 1 and rel[1] in {'history', 'plugins'}))


def headings(text):
    clean = re.sub(r'```.*?```', '', text, flags=re.S)
    found = []
    for line in clean.splitlines():
        m = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if m:
            h = re.sub(r'[*_`]', '', m[1]).strip()
            found.extend([canonical(h), canonical(re.sub(r'[^\w\s-]', '', h.lower()).replace(' ', '-'))])
    return set(found)


def placeholder(s):
    return '...' in s or bool(re.search(r'<[^>]+>|\{[^}]+\}', s))


def audit(root):
    root = Path(root).resolve()
    index = defaultdict(set)
    live = []
    for folder in ['00_Materials', '01_Notes', '02_Resources', '03_Agents']:
        for path in (root / folder).rglob('*'):
            if not path.is_file() or excluded(path, root):
                continue
            rel = str(path.relative_to(root))
            keys = [rel, path.name]
            if path.suffix == '.md':
                keys += [rel[:-3], path.stem]
                live.append(path)
            for key in keys:
                index[canonical(key)].add(rel)
    missing, ambiguous, malformed, sources, naming = [], [], [], [], []
    agent_missing, markdown_issues, anchors = [], [], []
    total = 0

    def resolve(path, raw, markdown=False):
        raw = unquote(raw.strip().strip('<>'))
        if raw.startswith(('http:', 'https:', 'mailto:', 'obsidian:', 'plugin:', 'app:', 'codex:')):
            return None, None
        raw = re.split(r'\\?\|', raw, maxsplit=1)[0]
        target, _, anchor = raw.partition('#')
        if placeholder(target):
            return None, None
        if not target:
            return {str(path.relative_to(root))}, anchor
        if target.startswith(('00_Materials/', '01_Notes/', '02_Resources/', '03_Agents/')):
            candidates = [root / target]
            if not Path(target).suffix:
                candidates.append(root / (target + '.md'))
            for candidate in candidates:
                if candidate.is_file():
                    return {str(candidate.resolve())}, anchor
        if markdown:
            candidate = path.parent / target
            if target.startswith('/'):
                candidate = Path(target)
            if candidate.is_file():
                return {str(candidate.resolve())}, anchor
            # Obsidian often uses vault-relative Markdown image links.
            if (root / target).is_file():
                return {str((root / target).resolve())}, anchor
            return set(), anchor
        direct = path.parent / target
        for p in [direct, direct.with_suffix('.md') if not direct.suffix else direct]:
            if p.is_file():
                return {str(p.resolve())}, anchor
        return index.get(canonical(target), set()), anchor

    for path in sorted(live):
        rel = str(path.relative_to(root))
        text = path.read_text()
        in_fence = False
        for number, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith('```'):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            line = re.sub(r'`[^`]*`', '', line)
            if line.startswith('Source: [[') and not line.endswith(']]'):
                malformed.append({'file': rel, 'line': number})
            if line.startswith('source:'):
                t = line.split(':', 1)[1].strip().strip('"\'')
                if t.startswith('00_Materials/') and not (root / t).is_file():
                    sources.append({'file': rel, 'line': number, 'target': t})
            refs = [(m.group(1), False) for m in re.finditer(r'\[\[([^\[\]\n]+)\]\]', line)]
            refs += [(m.group(1), True) for m in re.finditer(r'(?<!!)\[[^\[\]]*\]\((<[^>]+>|[^)\s]+)\)', line)]
            refs += [(m.group(1), True) for m in re.finditer(r'!\[[^\[\]]*\]\((<[^>]+>|[^)\s]+)\)', line)]
            for raw, md in refs:
                hits, anchor = resolve(path, raw, md)
                if hits is None:
                    continue
                total += 1
                item = {'file': rel, 'line': number, 'target': raw}
                if not hits:
                    (markdown_issues if md else missing if rel.startswith('01_Notes/') else agent_missing).append(item)
                elif len(hits) > 1:
                    ambiguous.append(item)
                elif anchor:
                    target = Path(next(iter(hits)))
                    if not target.is_absolute():
                        target = root / target
                    if target.suffix == '.md':
                        content = target.read_text()
                        if anchor.startswith('^'):
                            valid = bool(re.search(r'\^' + re.escape(anchor[1:]) + r'\s*$', content, re.M))
                        else:
                            valid = canonical(anchor) in headings(content)
                        if not valid:
                            anchors.append(item)
            if path.stem.endswith('_Master') or path.stem.startswith('Main_-_'):
                if rel.startswith('01_Notes/') and rel not in naming:
                    naming.append(rel)
        if rel.startswith('01_Notes/') and path.stem.endswith('_main') and canonical(path.stem) != canonical(path.parent.name + '_main'):
            naming.append(rel)
    def courses(folder):
        return {canonical(p.relative_to(root / folder)) for y in (root / folder).iterdir()
                if y.is_dir() and re.fullmatch(r'\d{4}_\d{4}', y.name)
                for s in y.iterdir() if s.is_dir() and s.name in {'Winter_Semester', 'Summer_Semester'}
                for p in s.iterdir() if p.is_dir()}
    return {'checked_links': total, 'missing_links': missing, 'agent_missing_links': agent_missing,
            'markdown_link_issues': markdown_issues, 'missing_anchors': anchors, 'ambiguous_links': ambiguous,
            'malformed_source_links': malformed, 'missing_source_metadata': sources,
            'nonstandard_hubs': naming, 'course_mirror_difference': sorted(courses('01_Notes') ^ courses('03_Agents'))}


if __name__ == '__main__':
    result = audit(ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(int(any(result[k] for k in result if k != 'checked_links')))
