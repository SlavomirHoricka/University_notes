"""Generate/check package copies; never edit installation caches or publish.
Run: python3 03_Agents/scripts/sync_plugin.py [--check]
"""
from pathlib import Path
import hashlib
import json
import sys
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
        # Vault-link tests depend on the vault-local checker, not a plugin runtime.
        if p.name not in {'sync_plugin.py','test_vault.py'}: files['scripts/'+p.name]=p
    files['LEARNING_ARCHITECTURE.md']=AGENTS/'LEARNING_ARCHITECTURE.md'
    files['README.md']=AGENTS/'references/PLUGIN_README.md'
    return files


def compatibility(manifest):
    return {'name':manifest['name'],'version':manifest['version'],
            'description':manifest['description'],'author':manifest['author'],
            'skills':'./skills','keywords':[],
            'interface':manifest['extensions']['com.openai']['interface']}


def run(check=False):
    sources=expected_files(); errors=[]
    manifest=json.loads((PACKAGE/'plugin.json').read_text())
    if manifest['name']!='uni-teach':raise ValueError('identity changed')
    compat=json.dumps(compatibility(manifest),ensure_ascii=False,indent=2)+'\n'
    if check:
        if (PACKAGE/'.codex-plugin/plugin.json').read_text()!=compat:errors.append('compatibility manifest mismatch')
    else:
        (PACKAGE/'.codex-plugin').mkdir(exist_ok=True)
        (PACKAGE/'.codex-plugin/plugin.json').write_text(compat)
    for name,p in sources.items():
        dest=PACKAGE/name
        if check:
            if not dest.is_file() or dest.read_bytes()!=p.read_bytes():errors.append(name)
        else:
            dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(p.read_bytes())
    # No unexpected instruction copies are allowed; obsolete remote paths must be stubs in source.
    for folder in ('skills','scripts','references'):
        for p in (PACKAGE/folder).rglob('*'):
            if p.is_file() and not any(x=='__pycache__' or x=='.DS_Store' for x in p.relative_to(PACKAGE).parts) and p.relative_to(PACKAGE).as_posix() not in sources:
                errors.append('unexpected generated file: '+p.relative_to(PACKAGE).as_posix())
    inventory={'schema_version':1,'package_version':manifest['version'],'source_root':str(AGENTS),
      'files':{name:{'source':str(p.relative_to(AGENTS)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for name,p in sorted(sources.items())}}
    inventory_text=json.dumps(inventory,ensure_ascii=False,indent=2)+'\n'
    if check:
        if not (PACKAGE/'package_inventory.json').exists() or (PACKAGE/'package_inventory.json').read_text()!=inventory_text:errors.append('package inventory mismatch')
    else:(PACKAGE/'package_inventory.json').write_text(inventory_text)
    if errors:raise ValueError('\n'.join(errors))
    if not check:
        archive=AGENTS/'plugins'/f"uni-teach-{manifest['version']}.zip"
        with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
            for p in sorted(PACKAGE.rglob('*')):
                if p.is_file() and not any(x=='__pycache__' or x=='.DS_Store' for x in p.relative_to(PACKAGE).parts):z.write(p,p.relative_to(PACKAGE))
        print('Packaged',archive)
    print('Verified',len(sources),'generated files; version',manifest['version'])


if __name__=='__main__':run('--check' in sys.argv)
