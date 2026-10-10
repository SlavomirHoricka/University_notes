# Validation and finished-app gates

Package validation now is distinct from application validation in H00–H16. Profiles parsing or branches existing cannot establish app behavior, model entitlement or academic readiness.

## Package checks

Python 3.11+ is required; this host has `/opt/homebrew/bin/python3.11`.

```sh
python3.11 docs/learning-hub/validate_plan.py
python3.11 -m unittest discover -s docs/learning-hub/tests -v
python3 03_Agents/check_vault.py
git diff --check
```

The validator checks package/schema, unique tasks/roles/branches, finite DAG, reciprocal ownership, role/profile routing, task-card presence, branch registry, safe paths, required files, V01–V16 and the original prototype hash. It is read-only. Tests inject cycles, missing dependencies, routing/branch mismatches and changed reference bytes into isolated copies.

Compare before/after vault issues by category and targets, never counts alone. Unrelated existing conceptual links/anchors and absent empty course mirrors are documented, not silently repaired. Introduced failures and material affected-output issues block integration. H09 changes to maintained record/skill inputs require their maintenance tests, applicable records verification and `sync_plugin.py --check`.

## App commands H00 must implement

These are proposed Makefile targets in `apps/learning_hub`, not commands currently installed. Failures propagate nonzero status.

| Target | Required checks |
| --- | --- |
| check-unit | Ruff, chosen Python type checker, pytest pure/unit, focused frontend tests |
| check-contracts | Strict public/private schemas, owner-extension fixtures, SQL migrations, generated OpenAPI/TS drift |
| check-integration | Temporary SQLite/filesystem/owner journals, fake provider, crash/root isolation |
| check-ui | ESLint, strict TS, component accessibility, visual reference cases |
| check-e2e | Playwright through actual local HTTP/worker with fictional isolated vault |
| check-all | All preceding checks, no silent critical skip |
| build | Locked backend/frontend release; no private bank in assets/source maps |
| export-contracts | Deterministic API fixtures and generated TS, CI detects drift |
| launch / stop | H14 manual detached startup and graceful shutdown |

Record installed versions/OS/lock hashes. Rerun affected checks after fixes. Ordinary CI mocks provider networking; real account and academic gates require separate observed receipts.

## Release matrix

H15 maps each row to named tests and actual results on the integrated SHA; owners implement repairs. H16 verifies final receipts and observed gates.

### V01 — subscription and routing

H01: OAuth state/nonce/PKCE/redirect/ID-token identity, refresh race and revocation tests. Real sign-in plus terminal completed inference on the user's account; record requested/actual model/effort and transport version. A catalog, text delta or mock cannot pass this gate. Missing grant/unsupported route blocks precisely; no credits/API-key fallback.

### V02 — sources and prior weeks

H07/H10: explicit course/week, durable immutable originals/hashes; PDF/PPTX/DOCX/Markdown/text/image extraction with page/slide locators and unresolved content. Detect duplicate, changed previous week, rename, ambiguous replacement and disappearance. Reject traversal/symlink/type mismatch/oversize. No history deletion; unreadable pages cannot certify coverage.

### V03 — checked academic preparation

H09/H10/H16: owner ingest→independent original-source review→verified records→plan→independent curriculum review→normal Git integration→export. Required notes map to taught/assessed objectives, explanations, keys/rubrics and supported visuals. Inject missing review, finding, stale source, pending transaction and integration failure: no Ready publication. Optional scope only when sources explicitly mark it.

### V04 — course/lesson flow

H04/H05: published weeks accessible without score locks; roughly 25-minute teaching with separate quiz estimate. Sections, headings/prose/bullets, free revisit, Previous/Next, bookmark resume, keyboard controls. Partial coverage and unknown evidence explicit. No manual completion control/endpoint; scrolling cannot establish understanding.

### V05 — maths, outline and visuals

H05/H06: long inline/display KaTeX, invalid TeX safe error, bounded macros/no trusted HTML; outline follows headings with offset links/reduced motion. Allowlisted visual domain/formula/units/reference cases and accessible alternatives. No generated executable JS/eval. Market reference cases only when actual finished notes support them.

### V06 — checkpoints and feedback

H03/H05/H11: deterministic choice/matching/final-number/scenario checks; authored explanations for each option and misconception-based distractors. Persist first response/assistance before feedback; correction stays distinct from independent success. No inference per checkpoint. Incorrect work uses prepared repair route; shuffle cannot produce a fresh variant.

### V07 — durable evidence

H02/H03/H09: prompt reserve/display/answer, immutable response, canonical verified outbox and projection cursor. Crash before receipt, after outbox, during canonical write, after commit/before ack; duplicate retry/double tab/different payload. Replay once, honest conflicts/pending journal. Schema-3/4 readers preserve complete legacy byte prefix; no missing outcomes invented.

### V08 — assessment and weekly mix

H11: completion/pass/attention/objective evidence separate. 85% plus essentials passes with attention; 95% with unmet essential fails. Decimal 80/90 boundaries, units/percent/tolerance/intentional blanks. Prepared short-answer rubric validates component support and ambiguity; unavailable grading stays pending. Weekly ~50/50 new/prior points in same course, Week1 exception; no cooldown/future-week lock.

### V09 — exposure and retention

H11/H12: persist lineage/possible display before release; fresh retrieval precedes recap/hints and obeys existing actual-time/independence conditions. Reused/shuffled prompt, exposed sibling, worked example, unknown assistance and too-early result cannot become fresh delayed retention. Exhausted bank queues checked preparation and offers corrective/new work; historical mastery policy preserved.

### V10 — course-specific adaptation

H10/H12: committed evidence produces owner-derived recommendations/schedules; visible weakest topics and justified duration. One course per review, no arbitrary cap, nonblocking new lessons. Refresh and pre-recap retention distinct. Pending grades/browser attention cannot create recall evidence; changed criteria preserve earlier outcomes.

### V11 — background and quota

H08/H14: worker survives browser closure; explicit stop/relaunch/manual launch after reboot recovers steps. Known reset uses actual scope/time; unknown reset coalesced bounded probes, no assumed five-hour reset. Partial/failed/EOF turn cannot pass. Pause/cancel safely preserves artifacts; stale fences cannot publish or duplicate writes. Sleep/off computer is not promised execution.

### V12 — publication and sessions

H03/H10: immutable staged bundle plus atomic CAS pointer; crash gives complete old/new version. Active/reloaded session pins source/ingestion/plan/key/rubric. New criteria cannot regrade history. Source changes mark freshness honestly; routine update notices wait until lesson finish.

### V13 — Agents tab

H13: factual job/step/review progress, requested/actual settings, measured counts and known/unknown limits. SSE deduplication and gap resnapshot, authorized polling fallback. Future-role settings capability-checked; required gates/current rubric immutable. Durable pause/retry/cancel. No chain-of-thought, secret/key/unseen item in events/errors.

### V14 — local security

All owners/H15: exact loopback Host/Origin, server-derived principal and CSRF/session protection. Reject rebinding/cross-origin/path escapes; browser cannot submit trusted score/arbitrary tool path. Source/answer instructions cannot widen owner permissions. Original active HTML download-only. Private keys/banks/secrets absent from public payloads/builds/logs/errors. No wildcard bind/external synchronization enabled.

### V15 — operation and restore

H14/H15: double-click/manual launcher, fresh locked install, clear diagnostics, occupied non-app port preserved. Browser close keeps jobs alive. Consistent SQLite backup plus linked assets/canonical journals; isolated restore recovers pending intents and reconciles later canonical writes. Corrupt/newer schema fails safely. No login autostart/wake/hosted service. Normal learner operation needs no terminal/Obsidian.

### V16 — final release

H15/H16: all task acceptance and V01–V15 results on exact integrated SHA; independent engineering review and final recheck. Bounded real course pilot with distinct academic reviewers proves upload→checked notes/plan→published study under real subscription. Fictional answers stay isolated; only actual answers enter real evidence. Confirm normal PR merge, remote-main, primary sync/precise deferral, retained branches and task-only cleanup. Deliver actual launcher/version/runbooks/limitations.

## Results and reviewer receipts

H15 creates `apps/learning_hub/docs/validation/matrix.json`: schema version, integrated SHA, environment/lock hashes, rows V01–V16 with `not_run | passed | failed | blocked`, test IDs/commands/exit codes, artifact refs, observed/fixture scope, time and findings. External gates cannot pass on mocks. H16 assembles release.md.

Review receipt: role/model/effort requested and host-confirmed (unknown if unavailable), inspected SHA/scope, exact findings, fix SHAs, rechecked scope/final result. Reviewers read/report; owners fix. Academic reviewers are distinct. Substantive changes invalidate affected review; session metadata cannot manufacture a review.

Failed gates return tasks to correction; genuine external blockers preserve artifacts and next action while independent work continues. Never mark partial delivery finished, lower criteria, invent readiness or buy a paid fallback to close the ledger.

