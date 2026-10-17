# Source-checked note-reference repairs

Follow-up to the [repository audit](REPORT.md), 2026-10-17. The human explicitly authorized correcting the six note-reference findings despite the earlier protected-note restriction. The original audit remains a dated snapshot of the maintenance merge, not the current unresolved-issue list.

## Resolutions

| Finding | Checked destination or repair |
| --- | --- |
| Missing descriptive-statistics overview | Existing JEB142 course-hub section, `I. Data and Descriptive Statistics`. |
| Missing Bernoulli page | Existing Bernoulli PMF example in `Probability_Mass_Function.md#Examples`. |
| Missing standard-error page | Minimal source-grounded explanation in `Sample_Mean_and_Sample_Variance.md#Standard Error of the Sample Mean`; repaired Variance link. |
| Missing Kolmogorov–Smirnov page | Minimal one-sample KS subsection in the CDF note, with iid/continuous/fully specified-null assumptions and calibration caveats. |
| Incomplete IQR anchor | Exact `2. Interquartile Range (IQR)` heading. |
| Incomplete inclusion-exclusion anchor | Exact `Inclusion-Exclusion Principle (Theorem 4)` heading. |

The source check also resolved a directly adjacent percentile-convention ambiguity: the prior interpolation formula is preserved as an alternate convention, while the lecture rule is explicit, bounded to interior percentiles, and illustrated by its checked salary quartiles and IQR. Seven existing notes changed; no new placeholder note was created.

## Provenance and limits

Authoritative ingestion records are the [six-reference pass](../../runtime/ingest/logs/20261017T224005+0200_statistics_reference_repairs.md) and its [interior-percentile follow-up](../../runtime/ingest/logs/20261017T224419+0200_statistics_percentile_boundary.md). They record exact local source passages, hashes, coverage limits, reviewer results and transactions. Original PDFs and unrelated notes/resources remain untouched.

Ingest owner `/root/statistics_ingest` obtained independent checks from `/root/statistics_ingest/source_check` and fresh `/root/statistics_ingest/boundary_check`, configured source-checker Astra/high profiles. Final results: no material findings in accuracy/coverage, priorities, foundations or simplification for the selected repair context. The parent also reviewed the final scoped diff and requested the checked percentile-domain qualification.

JEB142 correction revision 2 (`T-statistics-percentile-boundary-complete-JEB142`) and JEB105 correction revision 1 (`T-statistics-references-complete-JEB105`) verify as complete only for the listed passages. Their notes' remaining sections and whole-course coverage were not adopted. No learner evidence, scheduling state or external tasks were created. Curriculum-impact inspection and final integration checks are recorded in the [engineering session](../../runtime/sessions/2026-10-17-statistics-reference-repairs.md).

All six reference/anchor issues are resolved. Fresh worktrees still report nine unrelated empty course mirrors absent because Git does not track empty directories; the two affected courses now have genuine bounded correction records. Structural validation does not certify unrelated academic content or full-course readiness.

## Final validation

The plan owner and fresh independent curriculum-impact reviewer found no affected consumer across all six existing curriculum bundles (67 current plan/manifest/lesson files, 55 ready indexed lessons). No plan version, hash, assessment route or reassessment gate requires a change. Both Statistics courses retain absent curricula; the bounded corrections do not create course readiness.

After integrating latest main, 24 maintenance tests, generated-source parity and whitespace checks pass. Both active correction states, seven note hashes, all 44 journals and 233 staged payload hashes verify. [Final reference output](post_repair_vault_check.json) has no broken link/anchor/metadata category; fresh-checkout empty mirrors remain separately disclosed. Original materials, shared resources, Obsidian settings, skill bodies and existing curricula/learner records remain unchanged.
