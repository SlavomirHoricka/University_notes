# Repository navigation and local-reference audit

Date: 2026-10-17. Scope: repository support structure and local links/paths. The human excluded external URLs and academic-content review and required `00_Materials/`, `01_Notes/`, `02_Resources/` to remain untouched.

## Findings and changes

| Finding | Result |
| --- | --- |
| Main guidance and four session redirects pointed to a component removed from this repository. | Removed retired implementation guidance and the four empty dead redirects; repaired incoming session references. Current architecture and generated documentation describe only the vault workflow. |
| The checker skipped root documentation and Excalidraw, and rejected valid directory links. | Expanded traversal/resolution; added two regression cases for root/drawing/directory links and maintained archive indexes. |
| Three report redirects cluttered the agent-folder root without live incoming references. | Removed redirects; substantive original reports remain in their existing historical folders. |
| Superseded ZIPs mixed with the current distribution. | Moved six archives into `history/plugin-releases/`, verified their hashes, and added release navigation plus an annotation on the historical 0.3.1 publication record. |
| Finder metadata and Python bytecode were tracked outside protected content. | Removed three disposable Finder files and two bytecode files; added ignore rules. Protected folders and original historical snapshots remain exact. |
| The course map described an older filesystem and missing notes that now exist. | Rebuilt navigation from 21 actual course identities; current paths/declarations are explicitly distinguished from readiness. Corrected one dated fixture README's claim about current note availability. |
| An older maintained workflow diagram gave recall a write arrow to the learner log. | Routed scheduling to recall state and reminders through Todoist; linked the current editable swimlane drawing and labeled the older source as historical. |
| Runtime, history, package and utility folders lacked entry points. | Added focused indexes; rewrote root/workspace READMEs around purpose, structure, navigation and the four-stage workflow. Updated AGENTS after inspecting supporting references; preserved academic ownership and integration gates. |

The four canonical skill bodies, templates, actual course bundles, model-role profiles, learner evidence, transaction journals and Obsidian settings retain their existing bytes. Stable registration paths remain in place. Historical snapshots, earlier release ZIPs and dated session claims retain their provenance; they do not become current instructions.

## Reference and integrity checks

- [Reference-bearing file inventory](reference_files.json): 5,621 local links across 433 live Markdown files, including entry points, referenced support documents, drawings and maintained archive indexes. The inventory records per-file counts. Targets, headings and block IDs are checked mechanically; academic claims are not re-audited.
- [Literal support-path review](support_path_audit.json): contextual review of 294 path-like spans, distinguishing existing files from course-relative contracts, patterns, transient locks, branch/timezone/API identifiers and dated relocated paths. Three formerly abbreviated architecture template paths are qualified in the final document. Historical source-relative paths resolve under their recorded course identity.
- [Current record verification](record_verification.json): five ingestion states and all 55 ready indexed lesson bundles pass the applicable `records.py verify` checks, with no locks or pending transactions. This verifies committed bytes, not academic completeness or learning.
- [Preservation evidence](preservation.json): 1,158 protected tracked files remain unchanged; 374 additional skill/profile/snapshot/transaction files were compared with the base. All 38 committed journals and 227 staged payloads checked here retain valid staged hashes. The [move/removal ledger](file_changes.json) records six hash-preserving archive moves and twelve disposable-file/redirect removals.
- The 37-source generated package check passes. All 41 entries in prepared `uni-teach-0.5.3.zip` match the generated directory. The exact published 0.5.2 archive and its release receipt remain unchanged. No account publication, installation-cache update or host activation was performed.

## Validation and remaining findings

Bundled Python: 24 maintenance tests and 35 recall tests passed, with no skips. `sync_plugin.py --check` and `git diff --check` passed. Scoped review confirmed that the AGENTS changes remove retired guidance and improve navigation/check scope while preserving the existing academic, review, safe-write and Git integration requirements.

[Baseline](baseline_vault_check.json) and [final checker output](final_vault_check.json) were compared by issue identity and target. The four dead support redirects are gone; the expanded checker also found and helped remove three broken README targets previously outside its scope. There are no remaining missing agent links, Markdown links, ambiguous targets, malformed source links, missing source metadata or nonstandard hubs.

The full vault checker still exits 1 for these unchanged protected or checkout-specific findings:

- Four missing conceptual links in Statistics notes: `Descriptive_Statistics_Overview`, `Bernoulli_Distribution`, `Kolmogorov_Smirnov_Test`, `Standard_Error`.
- Two missing note headings: `Measures_of_Dispersion#Interquartile Range` and `Kolmogorov_Axioms#Inclusion-Exclusion Principle`.
- Eleven absent course-record mirrors. Each corresponding primary-checkout directory was inspected and is empty; Git does not preserve empty directories. No course records were fabricated.

Exact files, lines and targets are retained in the final checker output. No new issue identities were introduced. Original source files, protected academic content and learner history were not changed to make the checker pass.

## Limits and handoff

This is a structural maintenance audit. External URL availability, academic citations/content, PDF page bounds, live learner execution and native Obsidian UI interactions were outside scope. Existing Obsidian configuration and course navigation are preserved by byte comparison; no UI behavior is claimed from a test that did not run.

The [engineering session](../../runtime/sessions/2026-10-17-repository-navigation-audit.md) records branch/base, validation and integration handoff. Current workflow authority remains the [architecture](../../LEARNING_ARCHITECTURE.md) and maintained skills. Root [README](../../../README.md) explains the resulting repository structure and workflow.
