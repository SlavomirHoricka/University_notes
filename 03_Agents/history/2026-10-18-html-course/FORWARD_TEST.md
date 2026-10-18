# Independent HTML course forward test

Reviewer: `/root/html_course_forward_test` (independent helper). Date: 2026-10-18 Europe/Prague.

Inspected canonical skill: `/Users/slavomirhoricka/.codex/worktrees/2237/University_notes/03_Agents/html-course`. Initial hashes are in `inspected-hashes.json`. This test makes no repository, real-course, plugin-service or cache writes. All course records below are fictional and confined to this directory.

## Executed scope

- Read SKILL.md, scripts/README.md, draft template, agent metadata, course.py, runtime.js, theme CSS, existing ingest/plan structure and relevant canonical curriculum templates.
- Ran the supplied 12-test regression suite: all pass (`baseline-tests.txt`).
- `rehearse.py` creates fictional committed ingestion/plan records, snapshots requested O002 with prerequisite O001, builds a complete tiny English Week 1 candidate, then exercises publication using explicitly fictional acceptance reports from the supplied test fixture. These reports are test inputs, not actual academic/browser approvals.
- Changed the fictional note, confirmed stale publication blocks, reconciled fictional ingestion revision 2 / P002 / V002 through owner transactions with P001 history, regenerated the complete exported scope and published it.
- Verified exact bytes of the initial immutable version, preservation of an unrelated file, unchanged retry with empty changed-files list, and preservation/blocking of an unfinished stage without root activation. See `workflow-result.json`, `export/`, `vault/` and `candidate-v1`/`candidate-v2`.
- Local link/asset/anchor checks pass for the generated candidates. Source passage includes finite/nonempty condition, formula, fully solved example, R code, numerical exercise/key and self-assessment explanation. Coverage map accounts for every fixture source unit. Real academic correctness/readiness is not certified.
- Browser inventory was inspected; no page was opened or interacted with. Parent owns actual browser verification. This pass is fictional functional/static testing only; it does not certify rendered math, fonts, viewport behavior, keyboard or browser offline behavior.

## Findings at initial review

1. **P1: Candidate/export overlap can recursively copy a directory into itself.** `scripts/course.py:557` rejects candidates inside output, but permits output inside candidate. `probes.py` calls publish with output `candidate-v2/nested-export`; guarded copytree observes destination `candidate-v2/nested-export/versions/.stage-...` inside source candidate-v2. The test guard stops before recursion; production copytree would descend into its own stage until failure. Require nonoverlap in both directions before creating the output directory. See `probe-results.json`.
2. **P2: Valid Markdown fenced code truncates source content.** `scripts/course.py:67–71` masks exactly triple-backtick fences only. `heading-probe.py` demonstrates tilde fenced R code with `## R comment, not a heading`: extracting `Worked example` loses the code and its following denominator explanation. Longer/indented Markdown fences need matching handling too. See `heading-probe-results.json`.
3. **Operational consistency observation:** canonical `plan/templates/objective_lesson.md` has H2 `Record metadata`, `Contents`, `Metadata rules`. Snapshot treats all as coverage units, while only three tutor/scheduling headings may be operational omissions. A real template-based lesson therefore has to map machine metadata/TOC as included despite the reading-flow metadata restriction. The tiny supplied fixture lacks those headings. Resolve through explicit nonacademic treatment without permitting academic omission.

No final no-material-findings conclusion is warranted until the two reproductions are corrected and rechecked. Structure, ownership, explicit invocation, independent final-digest review, bounded readiness and recoverable immutable publication instructions otherwise fit the existing skills well. The additional-week TOC cross-reference is present; sidebar shows primary weeks only, which does not prevent contents navigation and is not treated as a material finding.

## Final recheck after owner fixes

Independent recheck completed on 2026-10-18. Both material findings are resolved for the inspected scope:

- Original nested-export reproducer now fails before any copytree call; output: `candidate and live export must not overlap in either direction`, `copy_calls: []`. Initial evidence preserved as `probe-results-before-fix.json`; final evidence is `probe-results.json`.
- Original tilde-fence reproducer now preserves code and the full following interpretation; false code heading excluded. Initial evidence preserved as `heading-probe-results-before-fix.json`; final evidence is `heading-probe-results.json`. Additional independent longer-backtick and three-space-indented tilde fence checks pass.
- Canonical lesson-style `Record metadata` and `Contents` source units now permit explicit operational omissions with reasons while academic omission rejection remains in the regression suite. SKILL and utility README describe the narrower metadata/navigation exception consistently.
- Cross-week static render now includes the secondary-week contents and sidebar cross-reference, with a valid primary prerequisite route.
- Re-ran all 15 final utility tests: pass (`final-tests.txt`). Independently repeated the complete fictional committed-record build/change/reconcile/refresh/preservation/retry/stage sequence with final code in `final-run/`; all checks pass.

**Final result: no remaining material findings in the independently inspected skill wording, fictional snapshot/build/publication/refresh/recovery behavior and static-render scope.** This is not browser QA, real-source ingestion review, real academic conversion approval or whole-vault readiness. The publication reports in the test exports remain explicitly fictional acceptance data. Parent owns browser QA. No repository files were written by this helper.

Final inspected file hashes (all files listed in `final-inspected-hashes.json`):

- `SKILL.md`: `826ff779cd461e3a93113658b929d6dba690c51baa25bcb4386e75a3b7c92e73`
- `scripts/course.py`: `3c36dcb2399a82f74760d35f22dee9da95462325709f815eaf2437a611f0b8d0`
- `scripts/test_course.py`: `9cdc52637f0765da719a3a09b67f3e41bbb5ee8db9da913644a65aedf875adea`
- `scripts/README.md`: `af17fae5e013adc639a947c61dd966c9af3579193af940832e491d720a1f13f9`

## Additional targeted review of asset/reuse/delimiter changes

All 17 supplied tests pass (`final-targeted-tests.txt`); previous overlap/fence reproductions remain fixed. Explicit-only math delimiters and conversion instructions agree in runtime, SKILL and utility README. Selected asset bytes are now checked against both ingest finished_assets and plan manifest entries.

One new P2 finding prevents a no-material-findings result for this intermediate source: `scripts/course.py:601–604` checks saved publication review status/digest only. A structurally complete inactive version with reports containing only `{status: passed, candidate_digest: ...}` is activated and retains incomplete saved review evidence. Reproducer `saved-report-probe.py` and output `saved-report-probe/result.json` are fictional utility data. Full kind/identity/evidence/findings/objective/browser check validation should also apply to saved reports. Intermediate hashes: `targeted-inspected-hashes.json`.

## Final targeted confirmation

Shared `validate_reports` now applies identical incoming/persisted kind, identity/evidence/findings/digest, academic objective scope and browser check gates. The original incomplete-saved-report reproducer now rejects activation (`saved-report-probe-fixed/result.json`). All 18 final tests pass (`final-targeted-tests.txt`). Full fictional snapshot/build/source-change/reconciliation/refresh/preservation/retry/stage workflow reran successfully against latest source in `release-final-run/`; test approvals remain explicitly fictional. Previous overlap/fence/metadata issues remain fixed.

**Final targeted result: no remaining material findings in the inspected skill workflow and static/fictional execution scope.** Browser QA and real academic conversion approval remain outside this helper's scope. Exact final source hashes: `release-final-inspected-hashes.json`.

- `SKILL.md`: `3c7e6dd647f4b71f5d800865c5c8ad24f7fbc4487a747ce87cd26bdb0e76f373`
- `scripts/course.py`: `ecc0e2bc70b2128314e8d5ab4dbfaa87ee1e903178bdaace5d24d4ff566363b8`
- `scripts/test_course.py`: `d5c68a923e6f3c79bf6db9a656a68925ae7254d76524f7834b601fca2ed65887`
- `scripts/README.md`: `c8ff9f8d4d6a96e70afc70b2a947daf2f567ddde1503fa5e3503e81a1749dcaf`
- `assets/runtime.js`: `b672bfac26fbf6ec91717aab209d4ee134b7319bd4e4ef7fedc7d870a926effd`
