# Agent workflow consistency audit — 2026-10-18

Scope: canonical ingest/plan/teach/recall skills, maintained role profiles, templates, shared references, transaction and scheduling utilities, package generation and the root/workspace documentation. This is infrastructure maintenance; original materials, notes, resources, actual course records, learner history and vault navigation/settings remain unchanged.

## Findings and fixes

| Finding | Final behavior |
| --- | --- |
| Corrected past evidence could replace an outstanding delayed/corrective date, and recovery could roll back on retry. | Invalidated support retains the outstanding date under an evidence gate. New post-correction acquisition starts a fresh replay chain whose correction boundary persists. Positive corrections and genuinely new observed lapses retain their ordinary behavior. |
| Record transactions accepted erasure/replacement of recall history despite the append-only contract. | `records.py` rejects edits, truncation or reordering of committed `schedule_history`, `task_history`, `scheduling_decisions` and `sync_journal` prefixes before staging. Derived fields remain editable; recovery remains idempotent. |
| Full package checks ignored the ZIP, and ordinary regeneration overwrote an existing same-version snapshot. | Full checks require exact ZIP entries/content. Differing existing snapshots block generation before copy writes. Identical snapshots retain their bytes. Explicit `--source-only` mode updates/checks loose copies while preserving and excluding ZIPs. |
| Folder-only invocation wording conflicted with explicit existing-note repairs; complete bounded repairs could be mistaken for whole-note verification. | Named-note/passages may establish bounded source context from cited originals. Scope limits remain explicit; the plan skill and manifest template require actual selected-section coverage, independently of whole-file hashes. |
| Recall task links defaulted to the retired `Uni` vault name. | The primary default is `University_notes`; callers may explicitly pass another registered vault name. |

The architecture, main READMEs, repository instructions and generated package now describe these same contracts. No new academic/readiness schema, interval policy, assessment criterion or live learner result was introduced. The utility enforces structural write/history guards; the owning workflows still verify academic correctness, coverage, readiness and external effects.

## Independent checks

- `/root/records_audit`: independently reproduced package/record failures using isolated fictional fixtures; final code review and 22 targeted tests found no material findings. Valid append/update, interrupted repeated recovery, corrupt/missing/differing ZIP rejection, source-only operation and snapshot preservation all checked.
- `/root/workflow_forward_test`: fictional repair-to-plan, generated-prompt resume, frozen key/history protection, acquisition-to-recall, corrected outcomes/eligibility, gate/recovery retries, later delayed reviews and compatible migration. It found two adjacent replay cases during repair; both were fixed and rechecked. Final result: no material findings in the tested scope; 42 scheduler regressions pass.
- Helpers remained read-only in the repository. Their temporary artifacts were not promoted to learner evidence, course records or production state.

## Validation and preservation

- 28 maintenance regressions pass with Python 3.11+ and no skips; 42 recall regressions pass. All four skills pass `quick_validate.py` (PyYAML supplied only in a disposable temporary directory).
- All seven active ingestion-state transactions, all 55 ready indexed lesson bundles, 44 committed journals and 233 staged payload hashes verify. All 834 baseline academic/evidence/settings files retain their hashes; originals and protected trees have no Git diff.
- Version 0.5.4 is a new prepared local snapshot. Full canonical/generated/project-role/ZIP parity passes. Existing 0.5.2 and 0.5.3 ZIPs and the private publication receipt retain their exact bytes. The preserved 0.5.3 ZIP intentionally predates later loose-copy role formatting. No account publication or host-cache installation was performed.
- [Final reference output](post_audit_vault_check.json) contains no broken link/anchor/source-metadata issue. The same nine absent empty course mirrors remain in this fresh Git worktree; this is a known checkout limitation, not an introduced content failure. The primary checkout is checked separately after integration.
- Scoped diff, staged diff and whitespace checks pass before integration. The [engineering session](../../runtime/sessions/2026-10-18-workflow-consistency-audit.md) records the branch, exact review scope and integration handoff. GitHub’s actual merged state remains the integration authority.

The review establishes consistency within the inspected workflows and exercised scenarios. It does not certify every course’s academic content, whole-semester coverage, live connector behavior or runtime model selection.
