"""Read-only curriculum snapshots and reviewed, versioned offline HTML exports.

Python 3.9+, standard library only. Run with --help. No course-record writes.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
from html import escape
from html.parser import HTMLParser
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import shutil
import socket
import sys
import uuid
from urllib.parse import unquote, urlsplit

SKILL = Path(__file__).resolve().parents[1]
TUPLE = ('course_id', 'plan_version', 'source_version', 'ingestion_revision')
OPERATIONAL = {'Teaching order and rationale', 'Advance, revisit, pause, and escalate',
               'Answer-free recall handoff', 'Record metadata', 'Metadata rules', 'Contents'}
ID = re.compile(r'[A-Za-z][A-Za-z0-9_-]*\Z')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def safe(root, name):
    root = Path(root).resolve()
    rel = Path(name)
    require(isinstance(name, str) and name == rel.as_posix() and not rel.is_absolute()
            and '..' not in rel.parts and rel.parts, 'unsafe relative path: ' + str(name))
    path = root / rel
    require(not any(root.joinpath(*rel.parts[:i]).is_symlink() for i in range(1, len(rel.parts) + 1)),
            'symlink not permitted: ' + name)
    require(path.resolve().is_relative_to(root), 'path escapes selected root')
    return path


def metadata(path):
    text = Path(path).read_text(encoding='utf-8')
    match = re.search(r'^```json\s*\n(.*?)\n```', text, re.M | re.S)
    require(match is not None, 'missing JSON metadata: ' + str(path))
    data = json.loads(match.group(1))
    require(isinstance(data, dict), 'metadata must be an object')
    return data, text


def headings(text):
    # Ignore fenced code; a heading inside a code example is not a source section.
    lines, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = re.match(r' {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if fence:
            lines.append(re.sub(r'[^\r\n]', ' ', line))
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= fence[1] and not marker.group(2).strip():
                fence = None
        elif marker:
            fence = (marker.group(1)[0], len(marker.group(1)))
            lines.append(re.sub(r'[^\r\n]', ' ', line))
        else:
            lines.append(line)
    masked = ''.join(lines)
    pattern = r'^ {0,3}(#{1,6})[ \t]+(.+?)(?:[ \t]+#+[ \t]*)?[ \t]*$'
    return list(re.finditer(pattern, masked, re.M)), text


def section(text, heading):
    found, clean = headings(text)
    selected = [i for i, match in enumerate(found) if match.group(2) == heading]
    require(len(selected) == 1, 'missing or ambiguous source heading: ' + heading)
    i = selected[0]
    start, level = found[i].start(), len(found[i].group(1))
    end = next((m.start() for m in found[i+1:] if len(m.group(1)) <= level), len(clean))
    return clean[start:end].strip()


def records_for(vault):
    path = safe(vault, '03_Agents/scripts/records.py')
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('html_course_records', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def snapshot(vault, course_id, objective_ids, assets=()):
    vault = Path(vault).resolve()
    require(re.fullmatch(r'\d{4}_\d{4}/(?:Winter|Summer)_Semester/[^/]+', course_id), 'full course identity required')
    course = safe(vault, '03_Agents/' + course_id)
    records = records_for(vault)
    require(records.status(course)['ready'], 'course locked or transaction pending')
    plan, _ = metadata(course / 'learning_plan.md')
    manifest, _ = metadata(course / 'source_manifest.md')
    state = load(course / 'ingestion_state.json')
    require(plan.get('schema_version') == manifest.get('schema_version') == 3, 'schema-3 plan and manifest required')
    require(plan.get('plan_status') in {'ready', 'partial'}, 'plan is not ready or partially ready')
    require(plan.get('owner') == manifest.get('owner') == 'plan' and state.get('owner') == 'ingest', 'record owner mismatch')
    require(plan.get('course_id') == manifest.get('course_id') == state.get('course_id') == course_id, 'course identity mismatch')
    require(state.get('status') == 'complete', 'ingestion incomplete')
    require(type(state.get('ingestion_revision')) is int and state['ingestion_revision'] == plan.get('ingestion_revision'), 'ingestion revision mismatch')
    require(all(plan.get(k) == manifest.get(k) for k in TUPLE), 'plan/manifest tuple mismatch')
    require(plan.get('transaction_id') == manifest.get('transaction_id'), 'plan/manifest transaction mismatch')
    require(records.verify(course, 'ingest', state['transaction_id'], ['ingestion_state.json']), 'ingestion transaction does not verify')
    index = {o['objective_id']: o for o in plan['objectives']}
    require(len(index) == len(plan['objectives']), 'duplicate objective identity')
    require(objective_ids and len(objective_ids) == len(set(objective_ids)), 'unique requested objectives required')
    ordered, visiting = [], set()

    def visit(oid):
        require(oid in index and index[oid].get('status') == 'ready', 'objective unavailable or not ready: ' + oid)
        require(oid not in visiting, 'prerequisite cycle: ' + oid)
        if oid in ordered:
            return
        visiting.add(oid)
        for dependency in index[oid].get('prerequisite_ids', []):
            visit(dependency)
        visiting.remove(oid)
        ordered.append(oid)

    for oid in objective_ids:
        visit(oid)
    files, units, selected, locations = {}, {}, [], {}

    def remember(relative):
        path = safe(vault, relative)
        files[relative] = digest(path.read_bytes())
        return path

    for name in ['learning_plan.md', 'source_manifest.md', 'ingestion_state.json']:
        remember('03_Agents/' + course_id + '/' + name)
    for oid in ordered:
        entry = index[oid]
        relative = '03_Agents/' + course_id + '/' + entry['lesson_path']
        require(entry['lesson_path'].startswith('lessons/'), 'lesson outside owned lesson directory')
        path = remember(relative)
        lesson, text = metadata(path)
        require(all(lesson.get(k) == plan.get(k) for k in TUPLE), 'lesson tuple mismatch: ' + oid)
        require(lesson.get('schema_version') == 3 and lesson.get('owner') == 'plan' and lesson.get('status') == 'ready', 'lesson not ready: ' + oid)
        require(lesson.get('objective_id') == oid and all(lesson.get(k) == entry.get(k)
                for k in ['objective_revision', 'criterion_version', 'prerequisite_ids']), 'lesson/index definition mismatch: ' + oid)
        require(lesson.get('transaction_id') == plan['transaction_id'], 'lesson transaction mismatch: ' + oid)
        require(records.verify(course, 'plan', plan['transaction_id'], ['learning_plan.md', 'source_manifest.md', entry['lesson_path']]), 'plan transaction does not verify: ' + oid)
        for match in headings(text)[0]:
            if len(match.group(1)) == 2:
                title = match.group(2)
                content = section(text, title)
                key = relative + '#' + title
                units[key] = {'key': key, 'kind': 'lesson', 'path': relative, 'heading': title,
                              'text': content, 'sha256': digest(content.encode())}
        require(lesson.get('note_locations'), 'lesson lacks note provenance: ' + oid)
        weeks = set()
        for loc in lesson['note_locations']:
            require(loc['path'].startswith('01_Notes/' + course_id + '/'), 'note belongs to another course')
            locations[(loc['path'], loc['heading'])] = loc
            weeks.update(int(v) for v in re.findall(r'/Week_(\d+)(?:/|$)', loc['path']))
        selected.append({**entry, 'weeks': sorted(weeks)})
    checked = {n['path']: n for n in state.get('finished_notes', [])}
    entries = {e['path']: e for e in manifest.get('entries', [])}
    for relative, title in locations:
        path = remember(relative)
        require(relative in checked and relative in entries, 'note not in checked ingestion and manifest: ' + relative)
        require(files[relative] == checked[relative]['sha256'] == entries[relative]['sha256'], 'stale note bytes: ' + relative)
        require(title in checked[relative].get('headings', []) and title in entries[relative].get('note_sections', []), 'heading outside checked coverage: ' + title)
        content = section(path.read_text(encoding='utf-8'), title)
        key = relative + '#' + title
        units[key] = {'key': key, 'kind': 'note', 'path': relative, 'heading': title,
                      'text': content, 'sha256': digest(content.encode())}
    passes = list(dict.fromkeys([state.get('completion_log'), *manifest.get('ingestion_pass_refs', [])]))
    require(passes and all(passes), 'checked ingestion pass reference required')
    for name in passes:
        require(name.startswith('03_Agents/runtime/ingest/logs/'), 'unexpected ingestion pass path')
        remember(name)
    for name in assets:
        require(name.startswith('01_Notes/' + course_id + '/'), 'asset outside selected note course')
        remember(name)
        checked_assets = {a['path']: a for a in state.get('finished_assets', [])}
        require(name in checked_assets and name in entries
                and files[name] == checked_assets[name].get('sha256') == entries[name].get('sha256'),
                'stale or unchecked asset: ' + name)
    require(records.status(course)['ready'], 'source changed/locked while snapshotting')
    for name, sha in files.items():
        require(digest(safe(vault, name).read_bytes()) == sha, 'input changed while snapshotting: ' + name)
    result = {'schema_version': 1, 'course_id': course_id, 'tuple': {k: plan[k] for k in TUPLE},
              'plan_transaction': plan['transaction_id'], 'ingest_transaction': state['transaction_id'],
              'requested_objectives': objective_ids, 'objectives': selected,
              'plan_objectives': {k: v.get('status') for k, v in index.items()},
              'source_files': files, 'source_units': list(units.values()), 'assets': list(assets),
              'ingestion_pass_refs': passes}
    result['fingerprint'] = digest(encoded(result))
    return result


def fresh(vault, snap):
    actual = snapshot(vault, snap['course_id'], snap['requested_objectives'], snap.get('assets', []))
    require(actual == snap, 'snapshot stale or changed; take a fresh snapshot and reconcile draft')


ALLOWED = set('p h2 h3 h4 strong em b i ul ol li blockquote pre code table thead tbody tfoot tr th td caption br hr div span details summary a img figure figcaption sup sub dl dt dd'.split())


class Fragment(HTMLParser):
    def handle_starttag(self, tag, attrs):
        require(tag in ALLOWED, 'unsupported content HTML tag: ' + tag)
        for key, value in attrs:
            require(not key.startswith('on') and key not in {'style', 'srcset'}, 'unsafe content attribute: ' + key)
            require(key in {'id', 'class', 'href', 'src', 'alt', 'title', 'colspan', 'rowspan', 'scope', 'open', 'start'}
                    or key.startswith(('aria-', 'data-')), 'unsupported content attribute: ' + key)
            if key in {'href', 'src'}:
                parsed = urlsplit(value or '')
                require(not parsed.netloc or parsed.scheme == 'https', 'unsafe URL')
                require(parsed.scheme in {'', 'https'}, 'unsafe URL scheme')
                if key == 'src':
                    require(not parsed.scheme and not parsed.netloc, 'remote image dependency')
                require(not (value or '').startswith('/'), 'absolute resource path')


def fragment(value):
    require(isinstance(value, str) and value.strip(), 'nonempty HTML content required')
    require(not re.search(r'!?\[\[', value), 'convert Obsidian links/embeds before rendering')
    parser = Fragment(convert_charrefs=True)
    parser.feed(value)
    return value


def valid_id(value):
    require(isinstance(value, str) and ID.fullmatch(value), 'invalid stable ID: ' + str(value))
    return value


def finite(value):
    require(type(value) in (float, int) and math.isfinite(value), 'finite numeric value required')
    return value


def widget(item):
    key, kind = valid_id(item['id']), item['kind']
    prompt = fragment(item['prompt_html'])
    solution = fragment(item['solution_html'])
    solution = f'<details class="solution-block"><summary>Reveal explanation</summary>{solution}</details>'
    if kind == 'numeric':
        value = finite(item['answer'])
        tolerance = finite(item.get('tolerance', 1e-6))
        require(tolerance >= 0, 'negative numerical tolerance')
        return f'<div class="practice" data-widget="numeric" data-answer="{value}" data-tolerance="{tolerance}">{prompt}<div class="answer-row"><label for="{key}">Your answer</label><input id="{key}" class="answer-input" type="number" step="any" inputmode="decimal"><button class="button" type="button">Check answer</button></div><p class="feedback" role="status" aria-live="polite"></p>{solution}</div>'
    if kind == 'choice':
        choices, answer = item['choices'], item['correct_index']
        require(len(choices) >= 2 and type(answer) is int and 0 <= answer < len(choices), 'invalid choice answer')
        options = ''.join(f'<label class="radio-option"><input type="radio" name="{key}" value="{i}"><span>{fragment(v)}</span></label>' for i, v in enumerate(choices))
        return f'<div class="practice" data-widget="choice" data-answer="{answer}"><fieldset style="border:0;padding:0;margin:0"><legend>{prompt}</legend>{options}</fieldset><button class="button secondary" type="button">Check answer</button><p class="feedback" role="status" aria-live="polite"></p>{solution}</div>'
    if kind == 'reflection':
        return f'<div class="practice"><label class="question-label" for="{key}">{prompt}</label><textarea id="{key}" data-draft="{key}" placeholder="Write your reasoning…"></textarea><p class="notebook-note">A local draft for your own study.</p>{solution}</div>'
    if kind == 'residual-plot':
        points = item['points']
        require(len(points) >= 2 and all(len(p) == 2 for p in points), 'at least two xy points required')
        for point in points:
            for value in point:
                finite(value)
        for name in ['intercept', 'slope', 'minimum', 'maximum', 'step']:
            finite(item[name])
        require(item['minimum'] <= item['slope'] <= item['maximum'] and item['minimum'] < item['maximum'] and item['step'] > 0, 'invalid plot slider bounds')
        config = escape(json.dumps({k: item[k] for k in ['points', 'intercept', 'slope', 'minimum', 'maximum', 'step']}), quote=True)
        return f'<div data-widget="residual-plot" data-config="{config}">{prompt}<div class="explorer"><div class="chart-wrap"><canvas class="chart" role="img" aria-label="Observations, a candidate line and vertical residuals"></canvas><span class="axis-y">\\(y\\)</span><span class="axis-x">\\(x\\)</span></div><div class="controls"><div class="slider-label"><label for="{key}">Slope \\(\\beta_1\\)</label><output class="slider-number"></output></div><div class="range-row"><input id="{key}" aria-label="Slope" type="range" min="{item["minimum"]}" max="{item["maximum"]}" step="{item["step"]}" value="{item["slope"]}"></div><p class="live-value">Sum of squared residuals: <output class="sse"></output></p><button class="text-button" type="button">Reset the line</button></div></div><p class="plot-caption">The intercept stays at \\({item["intercept"]}\\). This exploration changes only the slope.</p>{solution}</div>'
    raise ValueError('unsupported built-in interaction; provide a reviewed custom asset: ' + kind)


def validate_draft(draft, snap):
    require(draft.get('language') == 'en', 'English export required')
    require(draft.get('source_fingerprint') == snap['fingerprint'], 'draft/snapshot fingerprint mismatch')
    require(draft.get('course_id') == snap['course_id'], 'draft course mismatch')
    require(isinstance(draft.get('title'), str) and draft['title'].strip(), 'course title required')
    objectives = {o['objective_id']: o for o in snap['objectives']}
    lessons, anchors, covered = draft['lessons'], set(), set()
    require(lessons, 'at least one lesson required')
    ids = [valid_id(l['id']) for l in lessons]
    require(len(set(ids)) == len(ids), 'duplicate lesson ID')
    for lesson in lessons:
        require(lesson.get('objective_ids') and set(lesson['objective_ids']) <= set(objectives), 'unknown lesson objective')
        covered.update(lesson['objective_ids'])
        require(type(lesson['week']) is int and lesson['week'] > 0, 'positive week number required')
        weeks = {lesson['week'], *lesson.get('additional_weeks', [])}
        supported = {w for oid in lesson['objective_ids'] for w in objectives[oid]['weeks']}
        require(weeks <= supported if supported else bool(lesson.get('week_basis')), 'week not established by selected source paths; record an explicit week basis')
        require(lesson.get('title') and lesson.get('sections'), 'lesson title and sections required')
        for dependency in lesson.get('prerequisite_lessons', []):
            require(dependency in ids and dependency != lesson['id'], 'unavailable prerequisite lesson')
        for block in lesson['sections']:
            target = lesson['id'] + '#' + valid_id(block['id'])
            require(target not in anchors, 'duplicate section anchor')
            anchors.add(target)
            fragment(block['html'])
            for item in block.get('interactions', []):
                widget(item)
    require(covered == set(objectives), 'not all requested/prerequisite objectives are exported')
    for objective in objectives.values():
        for prerequisite in objective.get('prerequisite_ids', []):
            require(prerequisite in covered, 'missing prerequisite objective')
    by_id = {l['id']: l for l in lessons}
    visiting, visited = set(), set()
    def visit(lid):
        require(lid not in visiting, 'lesson prerequisite cycle')
        if lid in visited:
            return
        visiting.add(lid)
        lesson = by_id[lid]
        routed = {oid for dep in lesson.get('prerequisite_lessons', []) for oid in by_id[dep]['objective_ids']}
        needed = {oid for current in lesson['objective_ids'] for oid in objectives[current].get('prerequisite_ids', [])} - set(lesson['objective_ids'])
        require(needed <= routed, 'lesson is missing a prepared prerequisite link')
        for dep in lesson.get('prerequisite_lessons', []):
            visit(dep)
        visiting.remove(lid)
        visited.add(lid)
    for lid in by_id:
        visit(lid)
    units = {u['key']: u for u in snap['source_units']}
    coverage = draft['coverage']
    require({c['source'] for c in coverage} == set(units) and len(coverage) == len(units), 'coverage map must account once for every source unit')
    for entry in coverage:
        unit = units[entry['source']]
        if entry['disposition'] == 'operational_only':
            require(unit['kind'] == 'lesson' and unit['heading'] in OPERATIONAL and entry.get('reason'), 'academic content cannot be omitted as operational')
        else:
            require(entry['disposition'] == 'included' and entry.get('targets') and set(entry['targets']) <= anchors, 'coverage target missing')
    return anchors


def navigation(draft, current, prefix):
    output = f'<aside class="sidebar"><p class="brand"><a href="{prefix}index.html">{escape(draft["title"])}</a></p><a class="contents-link" href="{prefix}index.html">Course contents</a><nav aria-label="Lessons by week">'
    weeks = sorted({w for l in draft['lessons'] for w in [l['week'], *l.get('additional_weeks', [])]})
    for week in weeks:
        label = escape(draft.get('week_titles', {}).get(str(week), ''))
        output += f'<div class="nav-week"><span class="week-label">Week {week:02d}</span><em>{label}</em></div>'
        for i, lesson in enumerate(draft['lessons'], 1):
            if week in [lesson['week'], *lesson.get('additional_weeks', [])]:
                active = 'aria-current="page"' if current == lesson['id'] and week == lesson['week'] else ''
                cross = 'Also: ' if week != lesson['week'] else ''
                output += f'<a class="lesson-link" {active} href="{prefix}lessons/{lesson["id"]}.html"><span>{i:02d}</span>{escape(cross+lesson["title"])}</a>'
    return output + '</nav></aside>'


def page(draft, title, body, prefix='', current=None, revision=''):
    context = json.dumps({'course_id': draft['course_id'], 'lesson_id': current, 'revision': revision}, ensure_ascii=False).replace('<', '\\u003c')
    scripts = ['assets/vendor/katex.min.js', 'assets/vendor/auto-render.min.js', 'assets/runtime.js', *draft.get('custom_scripts', [])]
    tags = ''.join(f'<script defer src="{prefix}{escape(name, quote=True)}"></script>' for name in scripts)
    styles = ''.join(f'<link rel="stylesheet" href="{prefix}{escape(name, quote=True)}">' for name in draft.get('custom_styles', []))
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{escape(title)} · {escape(draft["title"])}</title><link rel="stylesheet" href="{prefix}assets/fonts.css"><link rel="stylesheet" href="{prefix}assets/math.css"><link rel="stylesheet" href="{prefix}assets/theme.css">{styles}{tags}</head><body><a class="skip" href="#main">Skip to lesson content</a>{navigation(draft,current,prefix)}<main class="main" id="main"><div class="reading">{body}<footer class="page-foot"><span>{escape(draft["title"])}</span><a href="{prefix}index.html">All weeks & lessons</a></footer></div></main><script type="application/json" id="course-context">{context}</script></body></html>'


def render(draft, folder):
    weeks = sorted({w for lesson in draft['lessons'] for w in [lesson['week'], *lesson.get('additional_weeks', [])]})
    body = f'<header class="toc-header"><p class="eyebrow">Your course companion</p><h1>{escape(draft["title"])}</h1><p class="toc-intro">{escape(draft["scope"])}</p></header>'
    for week in weeks:
        body += f'<section class="toc-week" id="week-{week}"><div class="toc-week-head"><p class="eyebrow">Week {week:02d}</p><h2>{escape(draft.get("week_titles", {}).get(str(week), "Lessons"))}</h2></div><div>'
        for i, lesson in enumerate(draft['lessons'], 1):
            if week not in [lesson['week'], *lesson.get('additional_weeks', [])]:
                continue
            hint = 'Also connects to this week. ' if week != lesson['week'] else ''
            body += f'<a class="toc-lesson" href="lessons/{lesson["id"]}.html"><span class="num">{i:02d}</span><div><h3>{escape(lesson["title"])}</h3><p>{escape(hint+lesson.get("description", ""))}</p></div></a>'
        body += '</div></section>'
    if draft.get('limitations'):
        body += '<details class="solution-block"><summary>Sources and scope</summary><p>' + escape(draft['limitations']) + '</p></details>'
    (folder / 'index.html').write_text(page(draft, 'Course contents', body), encoding='utf-8')
    (folder / 'lessons').mkdir()
    for i, lesson in enumerate(draft['lessons']):
        body = f'<header class="lesson-head"><div class="breadcrumb"><a href="../index.html#week-{lesson["week"]}">Week {lesson["week"]:02d}</a><span class="slash">/</span><span>Lesson {i+1:02d}</span></div><h1>{escape(lesson["title"])}</h1><p class="subtitle">{escape(lesson.get("subtitle", ""))}</p></header>'
        if lesson.get('prerequisite_lessons'):
            body += '<p class="prerequisite">Useful first: ' + ', '.join(f'<a href="{lid}.html">{escape(next(l["title"] for l in draft["lessons"] if l["id"] == lid))}</a>' for lid in lesson['prerequisite_lessons']) + '</p>'
        for j, block in enumerate(lesson['sections'], 1):
            body += f'<section class="section" id="{block["id"]}"><div class="section-title"><span class="section-number">{j:02d}</span><h2>{escape(block["title"])}</h2></div><div class="section-body">{block["html"]}{"".join(widget(item) for item in block.get("interactions", []))}</div></section>'
        body += '<nav class="page-nav" aria-label="Previous and next lesson">'
        body += f'<a href="{draft["lessons"][i-1]["id"]}.html">Previous: {escape(draft["lessons"][i-1]["title"])}</a>' if i else '<a href="../index.html">Course contents</a>'
        body += f'<a href="{draft["lessons"][i+1]["id"]}.html">Next: {escape(draft["lessons"][i+1]["title"])}</a>' if i+1 < len(draft['lessons']) else '<a href="../index.html">Return to contents</a>'
        body += '</nav>'
        revision = digest(encoded(lesson))[:20]
        (folder / 'lessons' / (lesson['id'] + '.html')).write_text(page(draft, lesson['title'], body, '../', lesson['id'], revision), encoding='utf-8')


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs = [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append((tag, attrs[key]))


def check_html(folder):
    folder = Path(folder)
    documents = {}
    for path in folder.rglob('*.html'):
        parser = Document()
        parser.feed(path.read_text(encoding='utf-8'))
        require(len(parser.ids) == len(set(parser.ids)), 'duplicate HTML IDs: ' + str(path))
        documents[path.resolve()] = parser
    for path, doc in documents.items():
        for tag, value in doc.refs:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                require(tag == 'a' and url.scheme == 'https', 'external runtime dependency')
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            require(target.is_relative_to(folder.resolve()) and target.is_file(), 'broken/escaping local link: ' + value)
            if url.fragment:
                require(target in documents and unquote(url.fragment) in documents[target].ids, 'broken HTML anchor: ' + value)
    for path in folder.rglob('*.css'):
        css = path.read_text(encoding='utf-8')
        require('@import' not in css.lower(), 'bundle CSS imports instead of fetching them')
        for value in re.findall(r'url\(\s*["\']?([^\)"\']+)["\']?\s*\)', css):
            if value.startswith('data:font/'):
                continue
            url = urlsplit(value)
            target = (path.parent / unquote(url.path)).resolve()
            require(not url.scheme and not url.netloc and target.is_relative_to(folder.resolve()) and target.is_file(), 'unbundled CSS resource')
    return len(documents)


def build(vault, snap, draft, draft_path, candidate):
    fresh(vault, snap)
    validate_draft(draft, snap)
    candidate = Path(candidate)
    protect_destination(vault, candidate)
    require(not candidate.exists(), 'candidate already exists; preserve it and choose a new staging path')
    candidate.mkdir(parents=True)
    shutil.copytree(SKILL / 'assets', candidate / 'assets')
    for asset in draft.get('assets', []):
        target = asset['target']
        require(target.startswith(('assets/figures/', 'assets/custom/')), 'asset must use figures/custom namespace')
        if asset['origin'] == 'vault':
            require(asset['path'] in snap.get('assets', []), 'vault asset absent from snapshot')
            source = safe(vault, asset['path'])
        else:
            require(asset['origin'] == 'draft' and asset['path'].startswith('assets/'), 'custom asset must be inside draft assets')
            source = safe(Path(draft_path).parent, asset['path'])
        require(digest(source.read_bytes()) == asset['sha256'], 'asset fingerprint mismatch')
        destination = safe(candidate, target)
        require(not destination.exists(), 'asset collision')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source.read_bytes())
    for script in draft.get('custom_scripts', []):
        require(script.startswith('assets/custom/') and script.endswith('.js') and safe(candidate, script).is_file(), 'custom script not a declared local asset')
    for style in draft.get('custom_styles', []):
        require(style.startswith('assets/custom/') and style.endswith('.css') and safe(candidate, style).is_file(), 'custom style not a declared local asset')
    render(draft, candidate)
    (candidate / 'snapshot.json').write_bytes(encoded(snap))
    (candidate / 'draft.json').write_bytes(encoded(draft))
    check_html(candidate)
    files = {p.relative_to(candidate).as_posix(): digest(p.read_bytes()) for p in sorted(candidate.rglob('*')) if p.is_file()}
    manifest = {'schema_version': 1, 'course_id': snap['course_id'], 'tuple': snap['tuple'],
                'objective_ids': [o['objective_id'] for o in snap['objectives']], 'source_fingerprint': snap['fingerprint'], 'files': files}
    manifest['candidate_digest'] = digest(encoded(manifest))
    (candidate / 'manifest.json').write_bytes(encoded(manifest))
    fresh(vault, snap)
    return manifest


def checked_tree(folder):
    folder = Path(folder)
    manifest = load(safe(folder, 'manifest.json'))
    signature = {k: v for k, v in manifest.items() if k not in {'candidate_digest', 'publication_files', 'entrypoint_sha256'}}
    require(digest(encoded(signature)) == manifest['candidate_digest'], 'candidate manifest changed')
    files = {**manifest['files'], **manifest.get('publication_files', {})}
    actual = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}
    require(actual == set(files) | {'manifest.json'}, 'unexpected or missing candidate/export files')
    for name, sha in files.items():
        require(digest(safe(folder, name).read_bytes()) == sha, 'candidate/export bytes changed: ' + name)
    check_html(folder)
    return manifest


def atomic(path, data):
    temporary = path.with_name('.' + path.name + '-' + uuid.uuid4().hex)
    with temporary.open('xb') as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)
    fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def protect_destination(vault, path):
    vault, path = Path(vault).resolve(), Path(path).absolute()
    # macOS exposes its normal temporary namespaces through these fixed aliases.
    aliases = {'/tmp': '/private/tmp', '/var': '/private/var'}
    require(not any(p.is_symlink() and str(p.resolve()) != aliases.get(str(p))
                    for p in [path, *path.parents]), 'output path contains symlink')
    require(path.resolve() != vault, 'output cannot be the vault root')
    for name in ['00_Materials', '01_Notes', '03_Agents', '.git', '.codex', '.obsidian']:
        require(not path.resolve().is_relative_to(vault / name), 'output overlaps protected vault files')


def sync_tree(folder):
    for path in folder.rglob('*'):
        if path.is_file():
            with path.open('rb') as handle:
                os.fsync(handle.fileno())
    for path in [*sorted((p for p in folder.rglob('*') if p.is_dir()), reverse=True), folder]:
        fd = os.open(path, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)


@contextmanager
def export_lock(root):
    directory = root / '.html-course.lock'
    directory.mkdir()
    token = uuid.uuid4().hex
    record = directory / 'owner.json'
    try:
        record.write_bytes(encoded({'token': token, 'host': socket.gethostname(), 'pid': os.getpid(), 'created_at': datetime.now(timezone.utc).isoformat()}))
        yield
    finally:
        if record.is_file() and load(record).get('token') == token:
            record.unlink()
            directory.rmdir()


def active_export(root):
    root = Path(root)
    entries = {p.name for p in root.iterdir()}
    require(entries <= {'versions', 'index.html', '.html-course.lock'}, 'unexpected export-root files; preserve them')
    require(not (root / 'versions').is_symlink() and not (root / 'index.html').is_symlink(), 'export symlink')
    if not (root / 'index.html').exists():
        return None
    data = (root / 'index.html').read_bytes()
    match = re.search(rb'<meta name="html-course-build" content="(b-[a-f0-9]{64})">', data)
    require(match, 'root index is not an owned export')
    manifest = checked_tree(safe(root, 'versions/' + match.group(1).decode()))
    require(digest(data) == manifest['entrypoint_sha256'], 'root contents externally edited')
    return manifest


def validate_reports(manifest, review, qa):
    require(review.get('kind') == 'academic' and qa.get('kind') == 'browser', 'separate academic and browser reports required')
    for report in (review, qa):
        require(report.get('status') == 'passed' and report.get('reviewer') and report.get('evidence')
                and report.get('candidate_digest') == manifest['candidate_digest'] and report.get('findings') == [], 'review missing, failed or for different candidate bytes')
    require(set(review.get('objective_ids', [])) == set(manifest['objective_ids']), 'academic review scope mismatch')
    require(all(qa.get('checks', {}).get(k) is True for k in ['links', 'math', 'interactions', 'desktop', 'compact', 'offline_dependencies']), 'browser QA incomplete')


def publish(vault, candidate, review, qa, output=None, allow_scope_reduction=False):
    candidate = Path(candidate).resolve()
    manifest = checked_tree(candidate)
    snap = load(candidate / 'snapshot.json')
    fresh(vault, snap)
    validate_reports(manifest, review, qa)
    root = Path(output) if output else safe(vault, '02_Resources/HTML_Courses/' + snap['course_id'])
    root = root.absolute()
    vault = Path(vault).resolve()
    require(not candidate.is_relative_to(root.resolve()) and not root.resolve().is_relative_to(candidate),
            'candidate and live export must not overlap in either direction')
    protect_destination(vault, root)
    root.mkdir(parents=True, exist_ok=True)
    with export_lock(root):
        previous = active_export(root)
        if previous:
            require(previous['course_id'] == snap['course_id'], 'export belongs to another course')
            removed = set(previous['objective_ids']) - set(manifest['objective_ids'])
            retired = {oid for oid, status in snap['plan_objectives'].items() if status == 'retired'}
            require(not removed or removed <= retired or allow_scope_reduction, 'refresh would drop previously exported scope')
        versions = root / 'versions'
        versions.mkdir(exist_ok=True)
        require(not list(versions.glob('.stage-*')), 'unfinished export stage; preserve and inspect before recovery')
        bid = 'b-' + manifest['candidate_digest']
        destination = safe(root, 'versions/' + bid)
        entrypoint = (candidate / 'index.html').read_text(encoding='utf-8').replace('<head>', f'<head><meta name="html-course-build" content="{bid}"><base href="versions/{bid}/index.html">', 1).encode()
        reports = {'reviews/academic.json': encoded(review), 'reviews/browser.json': encoded(qa)}
        published = {**manifest, 'entrypoint_sha256': digest(entrypoint), 'publication_files': {name: digest(data) for name, data in reports.items()}}
        if destination.exists():
            existing = checked_tree(destination)
            require(existing['candidate_digest'] == manifest['candidate_digest']
                    and existing.get('entrypoint_sha256') == published['entrypoint_sha256']
                    and set(existing.get('publication_files', {})) == set(reports),
                    'existing version is not a complete reviewed publication')
            saved_review, saved_qa = load(destination/'reviews/academic.json'), load(destination/'reviews/browser.json')
            validate_reports(existing, saved_review, saved_qa)
        else:
            stage = versions / ('.stage-' + uuid.uuid4().hex)
            shutil.copytree(candidate, stage)
            for name, data in reports.items():
                path = safe(stage, name)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            (stage / 'manifest.json').write_bytes(encoded(published))
            checked_tree(stage)
            fresh(vault, snap)
            sync_tree(stage)
            stage.rename(destination)
            fd = os.open(versions, os.O_RDONLY)
            try:
                os.fsync(fd)
            finally:
                os.close(fd)
        fresh(vault, snap)
        atomic(root / 'index.html', entrypoint)
        changed = sorted(name for name, sha in manifest['files'].items() if not previous or previous['files'].get(name) != sha)
    return {'index': str(root / 'index.html'), 'version': str(destination), 'changed_files': changed, 'candidate_digest': manifest['candidate_digest']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    snap = sub.add_parser('snapshot', help='verify ready inputs and capture source sections without writing records')
    snap.add_argument('--vault', required=True); snap.add_argument('--course', required=True)
    snap.add_argument('--objectives', nargs='+', required=True); snap.add_argument('--asset', action='append', default=[])
    snap.add_argument('--out', required=True)
    make = sub.add_parser('build', help='render a new candidate from a coverage-mapped English draft')
    make.add_argument('--vault', required=True); make.add_argument('--snapshot', required=True)
    make.add_argument('--draft', required=True); make.add_argument('--candidate', required=True)
    check = sub.add_parser('check', help='check exact candidate bytes, local links and IDs')
    check.add_argument('--candidate', required=True)
    pub = sub.add_parser('publish', help='activate a fresh candidate after matching independent/browser reports')
    pub.add_argument('--vault', required=True); pub.add_argument('--candidate', required=True)
    pub.add_argument('--review', required=True); pub.add_argument('--qa', required=True)
    pub.add_argument('--output'); pub.add_argument('--allow-scope-reduction', action='store_true')
    args = parser.parse_args(argv)
    if args.command == 'snapshot':
        result = snapshot(args.vault, args.course, args.objectives, args.asset)
        protect_destination(args.vault, args.out)
        require(not Path(args.out).exists(), 'snapshot output already exists; preserve it')
        Path(args.out).write_bytes(encoded(result))
        print(json.dumps({'snapshot': args.out, 'fingerprint': result['fingerprint'], 'objectives': [o['objective_id'] for o in result['objectives']]}))
    elif args.command == 'build':
        result = build(args.vault, load(args.snapshot), load(args.draft), args.draft, args.candidate)
        print(json.dumps({'candidate': args.candidate, 'candidate_digest': result['candidate_digest']}))
    elif args.command == 'check':
        print(json.dumps(checked_tree(args.candidate), ensure_ascii=False, indent=2))
    else:
        print(json.dumps(publish(args.vault, args.candidate, load(args.review), load(args.qa), args.output, args.allow_scope_reduction), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as error:
        print('HTML course blocked: ' + str(error), file=sys.stderr)
        sys.exit(1)
