# HTML-course implementation review

Reviewer: `/root/html_course_code_review` (independent read-only implementation reviewer).
Checkout: `/Users/slavomirhoricka/.codex/worktrees/2237/University_notes`, `codex/html-course-skill`, base `13eb266`.
Status: **changes requested** on the inspected initial implementation. This is not academic source review, browser QA or GitHub approval.

## Actionable findings

1. **P2 — Compare selected figures with checked ingestion hashes.** `03_Agents/html-course/scripts/course.py:193–195` hashes arbitrary requested files inside the note course, but never compares them with `ingestion_state.finished_assets`. Editing an already checked figure after its ingestion transaction therefore produces a new accepted snapshot instead of a stale-input failure. Notes and ingestion journals can remain valid while the figure becomes unchecked. Require selected source figures to belong to the checked asset inventory and match its recorded bytes (and any supported manifest asset inventory); keep custom newly created illustrations in the separately reviewed draft-assets route. Reproducer: `PYTHONDONTWRITEBYTECODE=1 python3 /private/tmp/html-course-code-review/reproduce.py`, first output `ASSET_STALE_ACCEPTED True`.

2. **P2 — Verify complete publication metadata before reusing a version.** `03_Agents/html-course/scripts/course.py:591–592` accepts an existing directory using the generic candidate checker plus digest only. Place an otherwise valid candidate tree at the expected `versions/b-<digest>` path; publication activates it despite absent stored reviews, `publication_files` and `entrypoint_sha256`. The next `active_export` immediately raises `KeyError 'entrypoint_sha256'`, blocking further refresh. Reuse must verify the required final publication fields/reports, existing reports' scope/status/digest, and expected entrypoint hash before activation. The same Python reproducer prints `INCOMPLETE_VERSION_ACTIVATED True` and `ACTIVATED_VERSION_READ_FAILS KeyError 'entrypoint_sha256'`.

3. **P2 — Make escaped currency compatible with math rendering.** `03_Agents/html-course/assets/runtime.js:10–16` enables the `$` opening delimiter, while `SKILL.md` §5.3 instructs escaping currency. The actual bundled auto-render searches opening delimiters without respecting a preceding backslash. In a single text node `Cost is \$10; then \(x=2\).`, no equation is rendered, although the normal control renders `x=2`; runtime still marks math passed. Escaped currency retains its slash as plain text. Prefer a supported currency strategy (for example standardizing output on bracket/parenthesis LaTeX delimiters and dropping single-dollar recognition, or safely protecting/restoring literal currency). Reproducer: `node /private/tmp/html-course-code-review/currency.js`.

## Checks and inspected scope

- Read the new skill, template, utility guide, entire `course.py`, `test_course.py`, `runtime.js`, vendor math renderer, asset provenance/license records, packaging code and changed shared documentation/manifest integration.
- The HTML skill has the same eight outer sections and dual GitHub/Obsidian jump convention as the four core skills. All 40 jump links resolve against its actual headings; the bounded template/commands/report format is operationally consistent.
- The four core skill bodies and role profiles have no working-tree changes. Shared edits describe an additive derived-only consumer; no new owner is inserted into the existing record transaction schema.
- HTML regression suite: 15 tests passed with `TMPDIR=/private/tmp/html-course-code-review` and bytecode disabled.
- Packaging/routing suite: 7 passed; 1 skipped because system Python lacks TOML support (Python 3.11+ required). The new fictional packaging test preserves four existing skill bytes while adding the fifth.
- All declared third-party file hashes match. CSS embeds fonts locally. Static checks cover links, anchors and CSS resource paths; custom-script behavior and academic fidelity correctly remain explicit independent/browser review duties.
- Existing prerequisite closure, supported week checks, coverage-ledger accounting, byte checks, candidate preservation, root activation and refresh scope protections are useful and exercised. Findings above concern gaps in their edge states, not a whole-course readiness claim.
- No real course/record, repository file, installed cache or service was mutated. Browser work remains with the parent. Fictional reproductions and reports are confined to this temporary directory.

Exact inspected hashes are in `inspected-hashes.json`. Main initial hashes:

- `course.py`: `3c36dcb2399a82f74760d35f22dee9da95462325709f815eaf2437a611f0b8d0`
- `test_course.py`: `9cdc52637f0765da719a3a09b67f3e41bbb5ee8db9da913644a65aedf875adea`
- `SKILL.md`: `826ff779cd461e3a93113658b929d6dba690c51baa25bcb4386e75a3b7c92e73`
- `runtime.js`: `25ebc4302138735f4932fdc37aaf5512ec4fbbec25ad94272d4ba7292aff29cd`
- `sync_plugin.py`: `0d87a595d3c86ba14b9bec4131cbcdc410b9e510d5199c2710fb891756f5f491`
