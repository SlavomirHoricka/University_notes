# Agent workspace organization audit — 2026-10-18

The requested organization is implemented: all five canonical skills live under `03_Agents/skills/`, shared documentation under `03_Agents/docs/`, and only `README.md` and `VAULT_MAP.md` remain as top-level files. The vault checker now lives under `03_Agents/scripts/`.

## Findings and changes

| Finding | Resolution |
| --- | --- |
| Five skill folders mixed with infrastructure at workspace root | Grouped under skills, retaining their owned templates, references, scripts and assets; added an index. |
| Loose architecture/naming documents and separate shared-reference folder | Consolidated into docs with an index. |
| Loose checker script | Moved to scripts, corrected root discovery/import and updated commands. |
| Skill paths embedded in roles, templates and package discovery | Updated maintained sources, generated project/package copies and source inventory; package-internal layout remains compatible. |
| Navigation did not present the fifth skill consistently | Updated root/workspace READMEs, architecture, map navigation, repository instructions and package guide. HTML export is explicit, optional and consumes checked notes/ready lessons. |
| Package guide still claimed 0.5.4 as the installed release | Corrected to the existing verified 0.6.0 receipt. Local 0.6.1 is prepared only. |

Actual incoming links were traced before moves. Three legacy Econometrics I headers, two engineering-session links and the workflow drawing's explanatory link were retargeted. Every byte from each legacy record's first JSON fence onward is unchanged; no observed outcome, criterion, version, curriculum history or scene data was altered. Historical snapshots, recorded plain-text paths and publication receipts retain their dated provenance.

## Validation

- 29 maintenance tests, 18 HTML export tests and 42 recall tests pass.
- Seven ingestion states and 55 ready indexed lesson bundles verify against their committed transactions.
- All five skill bodies match their base versions after operational-path substitutions only.
- The 1,282-file protected baseline matches except for the maintained history index and the three navigation-only legacy headers described above. Original materials, notes/assets, course evidence payloads, transaction data, historical snapshots, settings, previous ZIPs and publication receipt remain intact.
- Full 52-source/56-entry package and local 0.6.1 snapshot parity passes. No private publication or installation is performed.
- The vault checker has no link, heading, metadata or hub failures. Its same nine absent empty course mirrors remain: JEB104, JEB010, JEB050, JEB160, JEB009, JEB027, JEB044, JEB108 and JEM231; these are pre-existing navigation limitations in fresh Git worktrees.
- Root-file and grouped-skill assertions, scoped diff review and whitespace validation pass. This is an infrastructure audit, not a new academic source/curriculum certification.

## Deferred local migration

The primary checkout has unrelated material changes and is not fast-forwarded. Its standalone ingest/teach registrations still point to its existing folders. Update both symlink targets together with primary synchronization; see the live migration procedure in `03_Agents/docs/README.md`. Installed plugin caches remain the published 0.6.0 snapshot.

The authoritative engineering handoff, integration and additional authorized hub-branch cleanup scope are in `03_Agents/runtime/sessions/2026-10-18-agents-folder-audit.md`.

The human additionally authorized removing leftover learning-hub branches after integration. [Hub branch recovery inventory](HUB_BRANCHES.json) records 15 local and 14 remote refs, all already merged, plus the existing worktrees to preserve. Deletion outcomes must be verified separately from this preflight.
