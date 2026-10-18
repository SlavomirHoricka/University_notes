"""Generate/check local package copies and immutable versioned snapshots.

Run: python3 03_Agents/scripts/sync_plugin.py [--check] [--source-only]
Source-only mode explicitly excludes the ZIP; it never creates/replaces snapshots.
"""
import argparse
from pathlib import Path
import hashlib
import json
import os
import tempfile
import zipfile

AGENTS = Path(__file__).resolve().parents[1]
PACKAGE = AGENTS/'plugins/uni-teach'


def expected_files():
    files = {}
    for name in ('ingest','plan','teach','recall'):
        for p in (AGENTS/name).rglob('*'):
            if p.is_file() and not any(x.startswith('.') or x=='__pycache__' for x in p.relative_to(AGENTS/name).parts):
                files['skills/'+name+'/'+p.relative_to(AGENTS/name).as_posix()] = p
    for p in (AGENTS/'references').rglob('*'):
        if p.is_file() and p.name!='PLUGIN_README.md':files['references/'+p.relative_to(AGENTS/'references').as_posix()]=p
    for p in (AGENTS/'scripts').glob('*.py'):
        if p.name not in {'sync_plugin.py','test_vault.py','test_model_routing.py'}: files['scripts/'+p.name]=p
    for p in (AGENTS/'agents').glob('uni_*.toml'):
        files['agents/'+p.name]=p
    files['LEARNING_ARCHITECTURE.md']=AGENTS/'LEARNING_ARCHITECTURE.md'
    files['README.md']=AGENTS/'references/PLUGIN_README.md'
    return files


def compatibility(manifest):
    return {'name':manifest['name'],'version':manifest['version'],
            'description':manifest['description'],'author':manifest['author'],
            'skills':'./skills','keywords':[],
            'interface':manifest['extensions']['com.openai']['interface']}


def archive_matches(archive, payload):
    try:
        with zipfile.ZipFile(archive) as z:
            names=z.namelist()
            return len(names)==len(set(names)) and set(names)==set(payload) and all(z.read(name)==data for name,data in payload.items())
    except (OSError, zipfile.BadZipFile, RuntimeError, EOFError):
        return False


def run(check=False, source_only=False):
    sources=expected_files(); errors=[]
    project_agents=AGENTS.parent/'.codex/agents'
    old_inventory_path=PACKAGE/'package_inventory.json'
    old_inventory=json.loads(old_inventory_path.read_text()) if old_inventory_path.exists() else {}
    # Refuse collisions/user edits before mutating project or package copies.
    for name,p in sources.items():
        if not name.startswith('agents/'):continue
        target=project_agents/p.name
        if check:
            if not target.is_file() or target.read_bytes()!=p.read_bytes():errors.append('project agent mismatch: '+p.name)
        elif target.exists() and target.read_bytes()!=p.read_bytes():
            prior_hash=old_inventory.get('files',{}).get(name,{}).get('sha256')
            if hashlib.sha256(target.read_bytes()).hexdigest()!=prior_hash:
                raise ValueError('project agent collision or external edit: '+str(target))
    # Validate all managed names before writes, including unexpected stale files.
    for folder in ('skills','scripts','references','agents'):
        for p in (PACKAGE/folder).rglob('*'):
            if p.is_file() and not any(x in {'__pycache__','.DS_Store'} for x in p.relative_to(PACKAGE).parts) and p.relative_to(PACKAGE).as_posix() not in sources:
                errors.append('unexpected generated file: '+p.relative_to(PACKAGE).as_posix())
    manifest=json.loads((PACKAGE/'plugin.json').read_text())
    if manifest['name']!='uni-teach':raise ValueError('identity changed')
    compat=json.dumps(compatibility(manifest),ensure_ascii=False,indent=2)+'\n'
    inventory={'schema_version':1,'package_version':manifest['version'],'source_root':'03_Agents',
      'files':{name:{'source':str(p.relative_to(AGENTS)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for name,p in sorted(sources.items())}}
    generated={name:p.read_bytes() for name,p in sources.items()}
    generated['.codex-plugin/plugin.json']=compat.encode()
    generated['package_inventory.json']=(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n').encode()
    payload={p.relative_to(PACKAGE).as_posix():p.read_bytes() for p in PACKAGE.rglob('*')
             if p.is_file() and not any(x in {'__pycache__','.DS_Store'} for x in p.relative_to(PACKAGE).parts)}
    payload.update(generated)
    archive=AGENTS/'plugins'/f"uni-teach-{manifest['version']}.zip"
    if check:
        for name,data in generated.items():
            if not (PACKAGE/name).is_file() or (PACKAGE/name).read_bytes()!=data:errors.append('generated mismatch: '+name)
        if not source_only and not archive_matches(archive,payload):errors.append('missing, corrupt, or mismatched snapshot: '+str(archive))
    elif not source_only and archive.exists() and not archive_matches(archive,payload):
        errors.append('existing snapshot differs; choose a new package version or use --source-only: '+str(archive))
    if errors:raise ValueError('\n'.join(errors))
    if not check:
        # Create a complete temporary ZIP, then install exclusively; no overwrite.
        if not source_only and not archive.exists():
            fd,temporary=tempfile.mkstemp(prefix='.uni-teach-',suffix='.zip',dir=archive.parent)
            os.close(fd)
            try:
                with zipfile.ZipFile(temporary,'w',zipfile.ZIP_DEFLATED) as z:
                    for name,data in sorted(payload.items()):z.writestr(name,data)
                os.link(temporary,archive)
            finally:
                Path(temporary).unlink(missing_ok=True)
            print('Packaged',archive)
        for name,data in generated.items():
            dest=PACKAGE/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        for name,p in sources.items():
            if name.startswith('agents/'):
                project_agents.mkdir(parents=True,exist_ok=True)
                (project_agents/p.name).write_bytes(generated[name])
    print('Verified',len(sources),'generated files; version',manifest['version'],
          '(source-only; snapshot not checked)' if source_only else '(including snapshot)')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--source-only',action='store_true')
    args=parser.parse_args()
    run(check=args.check,source_only=args.source_only)
