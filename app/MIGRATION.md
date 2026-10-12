# Standalone app export

This package separates engineering code and a bounded legacy Uni workflow fork
from the university vault. It contains no course materials, finished notes,
learner evidence, real course records, credentials or installed dependencies.
The original vault and its existing personal skill registrations remain intact.

The separation checkpoint and actual acceptance status belong in the package's
status record and engineering receipts. The app is still an unfinished
implementation; a successful export does not establish release readiness.

## What to copy

Use the manifest exporter from this package. Its allowlist consists of tracked
files under `app/` in the enclosing repository, or tracked files under the root
of the standalone app repository. The manifest records exact working-tree byte
hashes and sizes plus a verified provenance commit. That commit identifies the
checkpoint; file hashes identify the exported snapshot, which can include the
reviewed separation changes made after the checkpoint.

The default manifest is `MIGRATION_MANIFEST.json`. It excludes itself to avoid
self-referential hashes. Export copies its listed files plus the exact manifest
bytes as audit metadata. The exported snapshot can therefore be exported again
without Git or regeneration, retaining the original provenance. It does not
copy Git history. The reported file count covers listed files; the manifest is
reported separately.

Refresh the manifest only after reviewing and staging all intended package
paths. `git ls-files` includes staged new files and current bytes of tracked
files; untracked additions are excluded.

From the parent repository:

```sh
python3 -B app/tools/export_app.py refresh --root app --provenance-commit 4272b77d3b9aa4080116b4ba022b82bd7864ba2f
python3 -B -m unittest discover -s app/tools -p 'test_export_app.py'
python3 -B app/tools/export_app.py export /absolute/new/learning-hub --root app
```

Replace `4272b77d3b9aa4080116b4ba022b82bd7864ba2f` with the verified integration checkpoint recorded by
the separation task. The destination must be new or empty, outside `app/`, and
cannot be its ancestor. Existing files are never overwritten. Paths containing
symlinks are rejected; on macOS use canonical `/private/tmp/...` when doing a
temporary rehearsal instead of `/tmp/...`.

The exporter checks all manifest entries and hashes before creating output. A
copy or disk failure can leave partial output: preserve or inspect it and use a
different empty destination for retry. It never cleans an existing directory.

Before a new GitHub repository is published, verify the export in its own local
Git repository. Application checks include Git ignore boundaries and therefore
need Git initialized:

```sh
cd /absolute/new/learning-hub
git init
git add .
python3 -B docs/learning-hub/validate_plan.py --root .
python3 -B -m unittest discover -s tools -p 'test_export_app.py'
python3 -B -m unittest discover -s 03_Agents/scripts -p 'test_*.py'
python3 -B 03_Agents/recall/scripts/schedule.py --self-test
python3 -B 03_Agents/scripts/sync_plugin.py --check
```

Follow `apps/learning_hub/README.md` for the locked toolchain install and
`make check-all build`. Do not copy `.tools`, `.venv` or `node_modules` from the
old checkout. After review, create the initial commit. A future manifest refresh
inside this repository uses the same command with `--root .` and its own HEAD.
Refresh only when intentionally creating a new reviewed snapshot; it replaces
the old provenance with the selected commit:

```sh
python3 -B tools/export_app.py refresh --root .
```

## Workflow sources and runtime authority

`03_Agents/{ingest,plan,teach,recall}`, references, utilities and maintained
Uni role definitions are the legacy workflow source fork. Generated plugin and
project Uni profiles are included to keep packaging/model-routing checks
complete. Maintain the sources, then regenerate copies with the local packaging
utility; never edit installed plugin caches or global registrations.

Some legacy instructions describe a selected Git checkout as an Obsidian vault
and cite the original primary path. They are preserved design inputs during
separation, not permission to dispatch against the parent vault. While this
package is nested in the old repository, `git rev-parse --show-toplevel` still
returns the parent repository; do not use that as the app's runtime data root.

Production Uni dispatch remains gated until the standalone architecture defines
explicit application storage roots and owner adapters. App data, uploads,
credentials and learner records must live outside source control. Separation
does not redesign persistence, activate academic workflows, import existing
course data or grant remote access.

The existing personal `ingest` and `teach` registrations continue to target the
original vault. They are not app registrations. No symlink or installed-cache
change is required to export this package.

## Next repository and product boundary

Copy/export the entire app envelope, not only apps/learning_hub. Create the new GitHub repository from that exported folder; the export contains a clean source snapshot rather than the notes repository's Git history. No new repository or course-data import is performed by this separation. Keep the unfinished provider worktree until its 14 untracked source/test files have been reviewed and explicitly transferred; they are not in this accepted package.

Before resuming H07-H10, revise their runtime storage/owner contracts for the standalone app: app-owned database and upload storage are authoritative; Markdown is optional export; no Obsidian installation, mirrored vault folders or historical Markdown format compatibility is a product requirement. Preserve evidence integrity and source/curriculum reviews. Current plan text and legacy workflows remain historical design inputs until that reviewed revision; this task does not implement a new persistence model. Current scope remains PC localhost with no paid API fallback, remote access or external task synchronization.

Academic sources/notes/records stay in the original vault. Existing ingest/teach registrations still work there. App workflow sources are an independent fork; future changes require explicit coordination, not blind copying back. Engineering session history is under docs/learning-hub/history/.
