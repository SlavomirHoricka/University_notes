# Learning hub workflows and runtime implementation instructions

Status: implementation specification, 2026-10-10. No application, authentication, inference, worker, or academic publication described here has been implemented or verified on this host. The agreed product decisions are in the approved personal learning hub implementation plan. The repository's [master architecture](../../03_Agents/LEARNING_ARCHITECTURE.md), [model routing](../../03_Agents/references/MODEL_ROUTING.md), [ingest](../../03_Agents/ingest/SKILL.md), [plan](../../03_Agents/plan/SKILL.md), [teach](../../03_Agents/teach/SKILL.md), [recall](../../03_Agents/recall/SKILL.md), and [AGENTS.md](../../AGENTS.md) remain authoritative within their scope. This document specifies engineering work and compatible extension proposals; it does not grant missing source-replacement approval or bypass a skill gate.

## 1. Implementation ownership and entry conditions

Implementation coding agents and runtime University Assistant agents have different responsibilities. Engineering defaults are GPT-6.1 Sol/high for all coding roles and GPT-6 Astra/high for the read-only engineering reviewer; actual selection is recorded separately from configuration. The `hub_*` roles build and test application code in an implementation worktree. They never impersonate an ingest, plan, teach, recall, or academic reviewer. Runtime `uni_*` owners operate course records through the maintained skills; read-only runtime reviewers inspect actual academic artifacts. A software review, fixture result, or coding agent's summary cannot certify academic coverage or produce learner evidence.

All module names below are relative to `apps/learning_hub/backend/learning_hub/`. The engineering coordinator assigns exact files before dispatch; workers preserve other agents' changes. Read the task DAG and contracts beside this document before starting a task. Do not create an additional role or move a task between roles merely to gain write access.

| Implementation role | Task IDs | Owned responsibility and module seam |
| --- | --- | --- |
| `hub_foundation` | H00, H02, H03 | Minimal bootstrap; `domain/{models,ports}/`, `adapters/storage/`, `adapters/evidence/`, `application/core/`, core/course/lesson API and generated frontend API; H03 is fixture-port acceptance until H09. |
| `hub_provider` | H01 | `adapters/codex/`: SIWC credentials, catalog/capabilities, app-server RPC transport, confirmed terminal events and normalized failures. |
| `hub_frontend` | H04, H05, H13 | Course/lesson player, outline/math/checkpoint UI, Agents tab; frontend consumes API contracts and never writes vault files. |
| `hub_visuals` | H06 | Reviewed visual components/configuration schemas and numeric reference cases; no AI-supplied executable scripts. |
| `hub_workflows` | H07, H08, H09, H10 | `adapters/extraction/`, owner-scoped `adapters/vault/`, `adapters/repository/`, `worker/`, workflow state orchestration, dependency invalidation and publication. |
| `hub_assessment` | H11, H12 | Assessment/retention selection and evidence/receipt application services, prepared-rubric assessment adapter; coordinate shared vault interfaces with `hub_workflows`. |
| `hub_operations` | H14 | `operations/`, `scripts/operations/`, operations tests/docs and user runbook; workflow worker orchestration remains workflows-owned. |
| `hub_qa` | H15 | Cross-feature `tests/e2e/`, `tests/fixtures/`, validation receipts; unit/contract/feature-integration tests remain with their registered module owner. |
| `hub_coordinator` | H16 | Final integration, task dependencies, documentation/review reconciliation and repository gates; no parallel authoritative course writes. |
| `hub_reviewer` | Assigned review | Read-only engineering review of changed contracts, code and final tests; findings have exact paths and reproduction steps. |

Keep HTTP/SSE routes in `api/`, workflow decisions in `application/`, pure identity/transition rules in `domain/`, external effects in adapters, and scheduling/process control in `worker/`. Avoid a general agent framework. Start with explicit use cases and a narrow provider interface. The API may request a use case; it may not declare a course Ready or an answer Passed itself.

Before every workflow launch resolve `git rev-parse --show-toplevel` and `git rev-parse --git-common-dir`; record canonical absolute paths, branch, base commit and full course ID. Validate course identity against actual year/semester/folder spelling, using NFC equivalence only for lookup. Never guess course codes, conflate similarly named courses, use a legacy vault path, or construct paths from an unvalidated uploaded filename. Resolve every script, template, state, journal, source, note and lock against the selected checkout. Reject symlink/path escapes. Pass that same root to every runtime agent and tool. Test root targeting with two fixtures having deliberately different sentinel contents.

## 2. H01: subscription provider feasibility slice

Deliver the smallest live slice first: manual local launch, supported sign-in, account-specific model selection, one bounded read-only inference with a terminal success event, streamed status, stop/restart and thread recovery. Store a sanitized feasibility report with binary/version, selected account registration reference, requested/actual model and effort, terminal status, request ID when available and limitations. Never store tokens in the report. Configuration parsing, a Connected badge, a model list or generated text before a terminal event is insufficient. Do not proceed to automated academic writes until this gate and the safe-write adapter gates pass.

### 2.1 Registration, identity and credential authority

Implement the public-client flow in the [official SIWC sign-in contract](https://developers.openai.com/siwc/token-sharing-open-source/sign-in). First registration uses `dynamic_agent_client`, stable host `ext_agent_host_id` and the actual app name; retain the callback's issued client ID. Returning sign-in uses that ID. Start a `127.0.0.1` loopback listener before authorization; preserve the exact callback URI through exchange. Generate fresh state, nonce and PKCE values. Request identity and plan scopes, including `chatgpt.tokens.use.direct`; exchange the code with the issued ID. Verify ID-token signature/JWKS, issuer, audience, expiry and nonce; use verified subject and registration identity. Validate returning identity and granted plan scope before activating credentials. A valid identity without plan scope permits signed-in UI but no inference.

Engineering defaults: callback attempt expires after 10 minutes; accept one matching callback and then close its listener. Bind only loopback. Reject duplicate callback, missing issued ID on initial registration, state mismatch, identity mismatch, or a different callback client ID on reauthorization. Do not log authorization URLs containing ID-token hints. Use a mature OIDC library and contract tests; do not hand-roll JWT verification. Capture exact upstream requirements/version in the adapter's ADR and recheck official docs when implementing.

Store credentials separately by verified subject plus issued client ID, never email alone. Use macOS Keychain behind a `CredentialStore` interface; if unavailable, implement a protected app-defined local credential file with restrictive directory/file modes and atomic replacement. Credentials live outside Git and browser storage. Keep stable host ID in durable runtime configuration; it is not an authentication secret or proof. A new sign-in remains pending until validated; failed sign-in must preserve the currently active account. Account switching applies to future dispatches; existing in-flight work retains its bound account identity until safely stopped.

Serialize rotating-token refresh per registration. Refresh near expiry (proposed 120-second margin), persist the complete replacement token set atomically before restarting app-server and resuming the saved thread. Retain registration identity on sign-out, stop dispatch, attempt documented revocation, clear local tokens, and report unconfirmed revocation honestly after network failure. Temporary errors preserve credentials; terminal invalid refresh clears unusable tokens and requires reauthorization. These account lifecycle requirements follow [Accounts and sessions](https://developers.openai.com/siwc/token-sharing-open-source/profiles-and-sessions).

### 2.2 App-server transport and inference confirmation

Launch app-server as a supervised child with an argument array, selected checkout as cwd, and token supplied only in its private child environment. The following is the documented provider configuration, not a command executed during this planning task:

```sh
codex app-server --listen stdio:// \
  -c 'model_provider="openai_chatgpt_plan"' \
  -c 'model_providers.openai_chatgpt_plan.name="ChatGPT plan"' \
  -c 'model_providers.openai_chatgpt_plan.base_url="https://api.openai.com/v1"' \
  -c 'model_providers.openai_chatgpt_plan.env_key="ACCESS_TOKEN"' \
  -c 'model_providers.openai_chatgpt_plan.wire_api="responses"' \
  -c 'model_providers.openai_chatgpt_plan.requires_openai_auth=false' \
  -c 'model_providers.openai_chatgpt_plan.supports_websockets=false'
```

The app reads its credential store and provides `ACCESS_TOKEN`; never put a literal token in this command. Initialize newline-delimited RPC with stable `clientInfo` name/title/version, await success, then send `initialized`. Start a thread with the selected model, persist its ID, start a turn and consume deltas through the terminal event. Only `turn/completed` with `turn.status == "completed"` proves turn success. Failed/interrupted turns remain incomplete. On token renewal restart, initialize and use `thread/resume`. These semantics and the configuration above are from [Codex app-server](https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server).

Generate/type-check RPC bindings against the pinned installed app-server version during H01. Validate actual exposed model/effort and subagent capabilities rather than inventing CLI flags or JSON properties. Keep request/response correlation IDs, thread IDs and turn IDs in durable provider runs. If terminal success arrives before output persistence, store a completion intent and finish artifact validation on recovery; a replay must not turn partial deltas into a committed result. Lost transport after submitted inference is an unknown outcome, not proof that it never ran. Reconcile saved thread/turn status where supported before another request; if reconciliation cannot establish a result, retain that run as unknown and start a distinct bounded attempt only after journal recovery and revision checks. There is no claimed universal exactly-once inference guarantee.

Use the selected credential for `GET https://api.openai.com/v1/models` to populate account choices from the returned `models` array, visible entries and server ordering. Treat app-server `model/list` as potentially cached. Catalog presence does not establish entitlement. For a direct diagnostic transport, only `response.completed` establishes success; `response.failed`, `response.incomplete`, stream EOF and early text do not. Quota failure may arrive after text has streamed. [Models and inference](https://developers.openai.com/siwc/token-sharing-open-source/models-and-inference) supplies these requirements.

Expose a narrow `ProviderPort`: account status, catalog/capabilities, start/resume/cancel run, events, refresh/reconnect, normalized failure. Requested settings and host-confirmed settings are separate fields. Mark unsupported/unknown combinations honestly. The interface must retain terminal status and raw diagnostic shape with redaction, never reduce all failures to a generic Retry button.

### 2.3 Supported feature envelope and failure classification

For direct HTTP preview requests require `store:false`, `stream:true` and array input. Use instructions/developer messages. Send needed history explicitly rather than HTTP `previous_response_id`. Reject unsupported fields before dispatch, including background/conversation, output/tool-call caps, metadata, prompt, sampling controls and service overrides not accepted by the route. Hosted image generation, file search, Code Interpreter, native computer use, hosted connectors and Responses `tool_search` are unavailable here. Text/images/files depend on model acceptance; the Files upload, transcription and audio/video routes are unsupported. Local shell/MCP/function tools are distinct capabilities; app-server RPC inputs must follow its schema. [Preview limitations](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations) defines the current envelope. Maintain an exact capability allowlist from that page in H01 and test every denied field/tool; the shorter list here is not an exhaustive schema.

The hub therefore stores/extracts sources locally, implements its own durable scheduler, and owns local artifact/history storage. No hosted background processing or file-search dependency is implied. Tool grants are narrow, checkout-rooted, owner-scoped and mediated by the runtime adapter. Source text cannot authorize shell commands, requests, permission changes or broader tools. Do not scrape ChatGPT, copy cookies, reuse an unrelated desktop token store, modify global Codex configuration or automatically fall back to paid API/credits.

Normalize exact HTTP status, code/parameter, redacted body shape, request ID, stream phase and retry metadata. Admission errors may contain `detail` instead of a standard error object. Classification follows [Errors and recovery](https://developers.openai.com/siwc/token-sharing-open-source/errors-and-recovery):

| Condition | Runtime action |
| --- | --- |
| Missing plan grant | `waiting_sign_in`, retain identity; enable grant only after explicit user action. |
| Confirmed invalid refresh/revocation | Stop dispatch and request sign-in; preserve work and registration. |
| `subscription_sharing_usage_limit_exceeded` / 429 | `waiting_usage`; reset scope/time may be unknown or app-specific. |
| Usage/user temporarily unavailable / 503 | Bounded transient retry, preserve credentials. |
| User not eligible / policy 403 | Block configured route; do not loop OAuth. |
| Unsupported capability / 400 | Block body; repair request configuration before another dispatch. |
| Route not supported / scope-context 403 | Block configuration/permission diagnosis; do not change billing. |
| Invalid user / admission 401 | Diagnose selected identity/grant; sign in after confirmed revocation or terminal refresh failure. |
| Unstructured admission 403 | Surface restriction; verify integration instead of blind retry. |
| Network loss or EOF after dispatch | Unknown/interrupted run; reconcile and recover journals before bounded retry. |

Tests must inject denial, identity mismatch, rotated-token races, transient refresh failures, invalid client, partial stream then quota, unknown body shape, terminal failure after valid text, and EOF without terminal success. No test may report a fake transport result as an actual account feasibility pass.

## 3. Durable scheduling and quota recovery

### 3.1 Storage schema and commit boundaries

Use a single app-state directory outside the repository, proposed macOS default `~/Library/Application Support/UniLearningHub/`. This expands from the actual user's home at runtime; it is not hard-coded to the developer account. Keep one registry/database for cooperating workers targeting the same Git common directory. Persist canonical repository registration to locate it across task worktrees. Refuse to start a second independent scheduler against the same repository with a different registry. Store worktree and course paths explicitly. SQLite is operational state; canonical academic records remain authoritative.

The workflow concepts require repository registration, jobs/steps/events, provider/account state, course reservations, sources/extraction, reviews, publication intents/pointers, sessions, receipts and canonical-write outbox. The exact table names, keys and migration order in CONTRACTS §9 are binding; do not implement a second naming/schema variant from this conceptual list. `hub_foundation` owns migrations; workflow owners consume typed repositories. Do not duplicate canonical learning outcomes in SQLite as a competing authority.

Each job stores stable ID/idempotency key, type, full course ID, source snapshot, dependency/plan/ingestion revisions, selected checkout/base, expected record hashes, role settings, stage, state/reason, attempt budgets, UTC timestamps, next eligibility, cancellation/pause intent and lease/fence. Each step stores immutable input digest, output hashes/paths, canonical transaction ID, provider run ID, terminal result and verification receipt. Append meaningful state transitions and unique outbox event IDs in the same transaction as their derived state. Never keep SQLite transactions open during inference, conversion, Git/network operations or filesystem lock waits.

Configure foreign keys, WAL and `synchronous=FULL`; use a 5-second busy timeout and short transactions. WAL is for a local filesystem, not a network share. Implement verified backups using SQLite's backup API, with linked immutable blobs and canonical records; copying only the database file while WAL is active is insufficient. Disk-full and integrity errors stop writes and preserve the last valid publication. Migrations require backup, explicit preflight, isolated restore test and no history/evidence deletion.

### 3.2 States and transitions

| State | Entry reason | Permitted exit |
| --- | --- | --- |
| `queued` | Durable accepted intent with valid inputs | `running`, `paused`, `cancelled`, `blocked` |
| `running` | Successful atomic lease claim and prerequisite/root checks | Another eligible step, waiting state, `retry_scheduled`, `blocked`, `succeeded`, safe pause/cancel |
| `waiting_usage` | Inference limit; verified retry time or unknown | `queued` after eligible availability/revision check, `paused`, `cancelled`, `blocked` |
| `waiting_sign_in` | Missing/expired authorization | `queued` after validated credentials; no automatic OAuth loop |
| `waiting_dependency` | Review, Git integration, prerequisite or earlier conflicting job pending | `queued` after actual dependency result, `blocked`, pause/cancel |
| `retry_scheduled` | Definitely retryable bounded failure | `queued` at next eligible time; `blocked` after budget exhausted |
| `blocked` | Unreadable source, missing capability, unresolved findings, approval, conflict or exhausted retries | Explicit retry/new inputs after cause addressed; pause/cancel |
| `paused` | User pause or explicit operational pause | User resume to eligible queue, cancel |
| `succeeded` | Final requested outputs validated and, when required, integrated/published | Terminal; later work has another job ID |
| `cancelled` | Stop reached a safe boundary and intent reconciled | Terminal; retained artifacts/history, explicit new job for restart |

`reason_code` and dependency IDs distinguish `blocked_review`, `blocked_approval`, `integration_blocked`, `stale_snapshot`, `provider_ineligible`, `unknown_external_outcome` and `storage_failure`. Keep pause/cancel request separate from actual state until in-flight effects are reconciled. A user cancel never deletes source versions, committed academic work, journals, evidence or a PR. Jobs waiting for quota/auth do not hold filesystem locks or a running worker lease.

### 3.3 Scheduler claim and recovery algorithm

Initial defaults are application policy, not provider guarantees: one worker supervisor, at most two concurrent inference turns total per active account; reserve the next free slot for durably received-answer grading, then interactive teaching, then mandatory review, then owner synthesis and optional drafting. At most one mutable course workflow runs per course. Do not interrupt an executing safe-write transaction to satisfy priority. A long turn may finish; reprioritize at the next step boundary. Headroom displays only actual available metadata and advisory thresholds, never invented token allowances or guaranteed weekly capacity.

1. Every second while awake, select eligible jobs by priority/age; idle scheduler may wait up to 5 seconds on local notifications. In `BEGIN IMMEDIATE`, claim using expected state/revision and store owner instance, boot/process identity, random lease token, monotonic fencing integer and UTC lease deadline. Exactly one affected row means claimed; otherwise reread. Default heartbeat 10 seconds, lease 60 seconds.
2. Before each external effect recheck lease/fence, course reservation, root, source snapshot, dependencies and expected canonical bytes. Persist submitted intent before dispatch. Effects carry stable intent IDs; adapters reject stale fencing generations. No provider success counts as canonical commit or academic approval.
3. Persist validated output/checkpoint and event in a short transaction. Renew the lease only for the same owner/token. Release only that token's lease/reservation. If a CAS fails, retain artifacts as uncommitted and stop effects; never overwrite the winner's state.
4. On startup, wake, worker death or overdue heartbeat, do not reclaim a lease solely because wall time passed. Inspect supervisor/child process identity, boot ID and thread state. Interrupt/terminate and confirm owned writer children have stopped before transfer. PID alone is insufficient because it can be reused. Recover pending owner journals and external intentions first. Ambiguous live process state holds the course in `blocked`; it does not authorize lock theft.
5. If the previous writer is confirmed gone, invalidate its fencing generation, retain its step history and resume from the last verified checkpoint. Verify actual committed bytes/transactions rather than trusting a `completed` row. A submitted network call or incomplete journal is recovery work, not a new job. Exactly-once application evidence relies on stable IDs plus owner verification, not replaying side effects blindly.

Use monotonic time for in-process heartbeats/timeouts; persist UTC for eligibility/history. Clock jumps and long sleep trigger a revalidation pass. Record actual receipt and activity timestamps with offsets; do not infer answer time from a job retry. All delayed-review calendar arithmetic remains the maintained recall utility with Europe/Prague semantics.

### 3.4 Quota and retry policy

Keep `limit_scope: account | app | unknown`, `retry_after`, `reset_at`, metadata origin and observed time independently. An HTTP 429 or usage-limit code alone cannot establish a five-hour/weekly reset or an app cap. The hub has its own advisory dispatch limits; label those separately. If actual account metadata reports reset, retain the value and check once after it plus 5 seconds. If an app-specific cap is established, show the relevant settings/action and hold inference until changed or eligible; never assume an account reset clears an app cap. Never buy credits or silently downgrade a reviewer.

Unknown reset policy: coalesce waiting jobs by account into one availability check, proposed 15, 30, 60, then 120-minute intervals, at most four checks per rolling 24 hours. First use a documented non-inference availability signal if the route exposes one; a catalog fetch does not prove quota availability. If no such signal exists, use one minimal completed diagnostic inference, labelled as consuming plan usage, without replaying the expensive course job. Persist its result; success permits one queued step and subsequent real failures reopen the circuit. A user Retry shares the same check/coalescing gate; it does not submit all waiting jobs. Unknown remains unknown in UI. After the daily budget, wait until the next permitted check or explicit resolved account/settings change.

Transient connection/unavailability retries: 30 seconds, 2 minutes, 10 minutes with bounded jitter (up to 20%); after three retries per step transition to `blocked` with a concrete retry control. Honor usable server retry metadata with its documented meaning; never retry earlier. For long quota waits release course filesystem locks, worker claims and child writer processes. Preserve the durable course workflow reservation/job association and revalidate on resumption; it prevents a second independent author from taking over silently. A newer source upload may supersede old queued work, but a submitted write/review/integration intention must first be reconciled.

Academic repairs: maximum two owner repair/recheck cycles per artifact revision. Unresolved material findings become blocked with exact locations and disagreement. New source information or explicit adjudication creates a new revision/budget; a generic Retry cannot reset the budget. Provider retry success never erases findings or missing approval. Independent reviewer unavailability queues that exact role/model; quality gates do not become optional when quota is scarce.

## 4. H14: manual launcher and process lifecycle

Implement a user-invoked launcher that starts one detached local supervisor, then opens the browser after health checks. The supervisor owns API/worker and provider/extractor children. Browser closure/disconnection stops only browser event subscriptions; it has no authority to stop jobs. No launch-at-login registration, automatic OS wake or cloud execution is configured. Sleep stops useful execution; recovery occurs on wake while service remains alive, or next manual launch after shutdown.

Define and ship these application commands in H14; they are proposed CLI contracts, not currently installed commands:

```sh
python3 -m learning_hub launch --vault-root /absolute/selected/checkout
python3 -m learning_hub status --vault-root /absolute/selected/checkout
python3 -m learning_hub stop --vault-root /absolute/selected/checkout
python3 -m learning_hub recover --vault-root /absolute/selected/checkout
```

`launch` registers/reuses repository state, obtains a local OS singleton lock, verifies stored process identity through a private health endpoint, starts a detached session with stdio attached to redacted rotating files, and exits after readiness. Prefer a Python subprocess supervisor with `start_new_session=True`; no shell `&` dependency on a terminal or browser process. Bind API to `127.0.0.1` only; proposed preferred port 8765 with an available-port fallback recorded in state. Open only the verified local URL. Protect mutating endpoints with a private local session/CSRF mechanism, strict origin/host checks and narrow CORS; localhost alone is not request authorization. Credentials are never sent to frontend.

`status` reads actual health/process/job facts; distinguish browser closed, supervisor stopped, worker failed, asleep gap, waiting quota and waiting authorization. `stop` persists stop intent, refuses new dispatch, asks running turns to interrupt through the supported RPC, and waits up to 30 seconds for safe checkpoints. If an owned child cannot stop, terminate its process group after reconciliation marks its run unknown, wait another 10 seconds, then kill only verified owned processes. Do not delete owner locks/journals on stop. A failed clean shutdown must be reported and recovered next launch. Never kill a PID merely from an old PID file.

Before service Ready: check runtime directory permissions/schema, SQLite integrity, credential-store availability, selected root, pending canonical write intentions, publications and active process reservations. Reconcile incomplete filesystem intents and outbox deliveries before serving a new current publication. If migration or recovery fails, expose a read-only diagnostic mode and last verified lessons where safe. Do not silently initialize a replacement database over a damaged one.

Detect wake with monotonic/wall-clock discrepancy or platform lifecycle notification; perform a single coordinated revalidation pass. Probe network/refresh status, recover dead children, inspect transaction readiness, recompute next eligibility and claim only due work. Do not spin through every missed retry interval or invent work done while asleep. Keep deterministic lessons usable when AI/network is unavailable.

Acceptance: launch from terminal then exit terminal and browser; worker remains healthy. Explicit stop releases only owned process resources. Restart resumes durable intents without duplicate upload/evidence. Sleep across quota reset resumes once awake after revalidation. Reboot does nothing until manual launch. Port collision uses recorded fallback. PID reuse, double launch, half-started supervisor, child crash, logout, disk-full and migration failure produce truthful status and no canonical corruption.

## 5. H07/H08: uploads, immutable originals and extraction

### 5.1 Receipt, durability and selection

Default initial upload limits match CONTRACTS §10: 100 MiB per file, 500 MiB per batch, 20 files per batch, plus 5,000 pages/slides per job. Configurable local limits are disclosed before submission. Exceeding a limit holds the batch for splitting/explicit limit adjustment; it never silently truncates coverage. Accept validated PDF, PPTX/PPT, DOCX/DOC, Markdown/plain text, images and structured data only when required extraction tools exist. Initial release rejects archives and executable uploads. MIME, extension and parser signatures must agree; unsupported or suspicious input receives a precise error.

Stream an upload into a unique staging file in durable app storage while computing SHA-256/byte count; enforce size limits during streaming. Flush/fsync it, then move atomically on the same filesystem to content-addressed immutable storage and fsync its parent. Insert source-version/receipt/batch intent only after durable bytes exist. Return accepted only after receipt commit. Crash before receipt leaves a collectible staged blob, not a falsely accepted upload; crash after receipt is recovered by intent replay. Retrying a request with its idempotency key returns the same receipt if payload identity agrees; mismatch is conflict.

Select exact course/week before upload. Logical source identity and immutable version identity are separate; same logical filename with new bytes creates a new version. Keep prior bytes and prior provenance. Never overwrite an original source or delete earlier material because a replacement omits it. Keep original basename/Unicode metadata; generate safe collision-free material version paths (including hash suffix when needed) only through ingest's authorized source-import adapter. An identical hash reuses bytes/extraction cache, but an incomplete prior pass still needs recovery. Replacement with known identical bytes does not queue unnecessary AI synthesis.

Source blobs retained outside Git are not themselves integrated vault provenance. Before ingestion, copy only the exact authorized immutable versions into the task worktree's `00_Materials/<course_id>/...` scope, verify hashes, preserve old vault files and record the mapping/receipt. Do not stage the operational blob store or private answers. If explicit user instructions require an existing source overwrite, surface a concrete preserved-version migration proposal; the app cannot infer approval from upload text or contents.

### 5.2 Same-course earlier-week scan and dependency invalidation

After every accepted batch, build a source snapshot by scanning that course's selected new/replacement versions and all earlier weeks in the same course. Include applicable shared course references only from existing authorized mappings; do not scan unrelated courses or use a week-folder name as readiness proof. Snapshot records exact paths, byte hashes, sizes, version selections, applicable successful ingestion revision/pass and later incomplete work. Hash current bytes; timestamps are only a performance hint. A changed whole-file hash does not prove which pages changed.

Compare against the latest successful checked record per source and all subsequent incomplete passes. Classify unchanged checked, unchanged unfinished, changed, new, missing, or ambiguous selection. A missing linked log/state/readability is a provenance gap, not evidence of completion. Missing or manually deleted source remains a conflict; preserve prior bytes and do not silently retire academic content. Read the ingestion index and relevant detail records, not a stale inventory/session summary alone.

Dependency graph nodes: immutable source versions/regions → checked note sections/assets → objectives/prepared lesson versions → question/rubric/visual configurations → weekly blueprint/retention variant sets/publication. Store reasons and provenance for edges. Traverse reverse edges from changed inputs; invalidation blocks affected projections immediately and preserves historical publications/evidence. Course-level fresh/stale status is derived from actual affected readiness. If graph coverage is incomplete, conservatively include the course's affected downstream candidates for owner analysis; never guess that unrecorded dependencies do not exist.

Perform deterministic native extraction and local structural comparisons first. Owner adjudicates semantic impact and scope; changed formatting does not automatically require full regeneration, and apparent text equality does not establish equivalent figures/notes. Unchanged checked artifacts retain provenance; unchanged unfinished work resumes. Source revision, notes revision, plan version and publication revision remain distinct. No automatic revision downgrade or evidence reset is permitted.

### 5.3 Coverage extraction pipeline

| Source | Required initial path | Required checks and fallback |
| --- | --- | --- |
| PDF | Native per-page text plus page dimensions/labels and local render | Inspect relevant page images, equations, tables, footnotes/appendices; sparse/garbled pages use local OCR and manual visual verification. |
| PPTX | Local XML/native slide text, tables, media and speaker notes | Enumerate hidden slides and relevant notes; render slides with a validated local renderer; preserve slide labels versus physical indices. |
| PPT / DOC | Local safe conversion in scratch directory | Verify page/slide count, notes and embedded objects; if converter cannot expose content, require accessible export rather than certify text-only coverage. |
| DOCX | Native paragraphs/tables/notes/media plus render | Cite renderer/pagination, inspect embedded objects and equations against renders. |
| Image/scanned pages | Local OCR plus original render | Verify symbols, subscripts, signs, units, axes/legends and small text visually; OCR confidence is diagnostic, not truth. |
| Data/table inputs | Native parser with schema/type/unit report | Preserve values, dimensions and definitions; no executing macros, formula side effects or embedded code. |
| Markdown/plain text | UTF-8/native line and heading extraction | Preserve equations, source line locators and linked-asset scope; active HTML/code blocks stay inert data, not tools/instructions. |

Cache by source hash, extractor/renderer/OCR version, settings and output digest. Store tool version, language, actual page/slide/region locators, errors and rendered artifact hashes. Scratch conversions remain outside the vault; originals are read-only. Proposed render density 150 dpi, 300 dpi for difficult text/equations; OCR page timeout 120 seconds, conversion timeout 300 seconds, at most two concurrent extraction processes. Resource limits stop with exact unprocessed pages. Test local tools on representative real file types before selecting dependencies; deterministic fakes do not establish fidelity.

Maintain a page/slide coverage ledger with statuses `native_extracted`, `render_inspected`, `ocr_verified`, `covered`, `optional_with_reason`, `blocked` and precise region findings. Every selected relevant region must be accounted for; the owner/checker, not an extractor, decides completed academic coverage. Blank/sparse native text must not become an automatic skip. Record optional designations and source ambiguities. Preserve figures/tables/maths and consulted-reference locators. Cloud OCR is permitted only under maintained ingest cost/approval rules; no free-cloud capability is assumed. Illegible material blocks the affected pass with filename/page/region and request for accessible copy or transcription.

Extraction runs sandboxed without macros, source-directed code, shell interpolation or arbitrary URL fetching. Source instructions, hidden/bidi/encoded layers and metadata remain untrusted content; include trust rules in helper prompts. Source-controlled strings are data passed through APIs, never executable command fragments. The app may render relevant academic material without trusting instructions embedded in it.

## 6. H09: owner adapters and reviewed academic worktrees

### 6.1 Owner-scoped write contracts

`adapters/vault/` exposes separate ingest/plan/teach/recall ports, each with an allowlisted path contract, expected hashes, stable transaction ID, actual root and recovery/verification result. Use the selected checkout's `03_Agents/scripts/records.py`, not an installed cache or copied fixed-path script. Read status before writes and recover unfinished journals with the same owner/ID after checking staged intent. Never invoke its commit while manually holding its filesystem lock. No stale lock is stolen by age. Only the owner releases its own lock token.

| Runtime owner | Existing canonical write authority | Adapter boundary |
| --- | --- | --- |
| ingest | Notes/assets/hubs, ingest source imports, index/pass records and `ingestion_state.json` | Block freshness before note writes; preservation/approval and complete source review remain mandatory. Index/pass have shared writer and detail-before-index atomic protocol. |
| plan | `learning_plan.md`, `source_manifest.md`, `lessons/`, immutable `curriculum_history/` | One matching committed bundle; old exact definitions retained; checked finished notes only. |
| teach | `learning_log.md` | Actual learner events/session state under existing schema; immutable attempts and real delivery/receipt facts. |
| recall | `recall_state.json`, verified shared project map and owned synchronization intentions | Derive from committed evidence; deterministic utility/outbox; no grading. |

The current records utility does not automatically authorize arbitrary web lesson files, multi-file note transactions, source version registries, new receipt events or every proposed app contract. H02 defines the proposed compatibility contract and H03 tests its owner port with fixtures; H09 implements the root-assigned maintained canonical changes with migrations/tests and packaging checks when applicable, and rechecks the port against actual records tools. H09 must detect unsupported contracts and return `blocked_adapter_extension`. Do not create a generic filesystem writer as a shortcut. Engineering approval of an adapter schema does not substitute for ingest approval of a substantive existing-note replacement.

Proposals must identify exact schema/owner, backward behavior, expected-byte strategy, stable IDs, crash recovery, historical preservation and test cases. The proposed schema-4 evidence/receipt extension must preserve existing schema-3 events and immutable history; readiness depends on canonical implementation, compatibility tests and owner review, not this proposal. Existing records/journals remain verifiable during migration. SQLite accepted-answer receipts are operational intake until teach confirms the canonical event; never display them as recorded academic outcomes. The evidence/receipt contract in the adjacent contracts document owns detailed event definitions; no rival evidence authority is introduced here.

### 6.2 Cross-worktree course coordination

The shared app registry keys reservations by canonical Git common directory and full course ID, not by worktree path. A reservation stores owning workflow/job, task worktree, source snapshot, fence generation and status. One mutable academic workflow may reserve a course; read-only reviewers may run against that immutable expected revision. Maintain a short-lived execution lease separately from the durable workflow reservation. Quota/auth/review waits release running leases and filesystem locks while preserving the reservation and recovery identity.

Before admitting work, inspect registered jobs, `git worktree list`, attached host worktrees when available, active relevant session records and course/journal states in overlapping checkouts. Resume the same interrupted task/worktree; do not create a fresh ingestion over pending work. Conflict with an existing external course task blocks dispatch until it is reconciled or explicitly coordinated. Per-checkout locks cannot prove absence of another writer.

For cooperating runtime writers, require reservation/fence validation before note writes, records commits, integration and publication. For work launched outside the app, a compatible shared guard must be proposed in canonical entry adapters before claiming universal serialization. Without that guard the app can detect known active work and CAS changes, but cannot prevent arbitrary manual edits; record this limitation and fail closed on discovered conflicts. Never claim SQLite fencing cancels a live external writer. Stale lease transfer requires confirmed process/agent stop, journal inspection and root/revision reread.

Teach/recall normally write the selected authoritative live checkout under their short owner locks. H03/H09 must pin this live root and its canonical tuple-reading contract in an ADR before enabling live writes. Do not let the app alternate evidence authorities between task worktrees. Academic task integration excludes evidence/recall changes from academic staging. Do not merge a stale worktree's `learning_log.md` over newer answers. Pinned sessions can continue on prior validated content while new content is prepared, subject to recorded freshness/compatibility gates; pending interpretation stays pending rather than being regraded under new criteria.

Each actual learner event receives its owner records transaction immediately; it does not require a Git commit, push or PR for every response/click. Git is an independent backup/integration boundary. Proposed evidence batching occurs at explicit session close or before an academic revision switch, with an optional 15-minute backup checkpoint while the service is awake. Persist uncommitted canonical bytes/journals through service restart; never treat a clean Git tree as proof that an answer was recorded. Never use lesson UI navigation as authorization for broader repository changes.

For primary synchronization, pause new canonical writers briefly at a safe boundary, drain/recover their actual pending intentions, verify teach/recall transactions and compare against the last recorded Git base. Preserve unrelated primary changes. If only authorized owner evidence/journal paths are modified, the repository adapter may create one scoped evidence batch commit; direct push is allowed only under repository policy/protection. Where protection requires a PR, prepare a dedicated batch branch/PR and retain the primary bytes until remote integration is confirmed; do not reset/stash them to make the tree clean. Reconcile resulting main advancement into the academic branch with fresh checks before its merge. This batching mechanism needs explicit implementation tests/ADR and cannot bypass records history or owner checks.

Fast-forward primary only when it is actually clean and on main. If unrelated edits, divergence, pending evidence integration or protection prevent that, preserve the live checkout and report sync deferred. An immutable merged content bundle can be compiled elsewhere, but a new session cannot write canonical evidence against a tuple that its live owner adapter cannot verify. Hold that new session's recording/readiness route until clean synchronization or an approved compatible live-record bridge establishes the exact tuple; keep old pinned sessions and received-answer intents intact. This avoids promising newer teach readiness solely because a Git PR merged. Do not copy compiled lessons/raw logs back blindly or mutate canonical plan files to resemble the snapshot.

### 6.3 Ordered ingestion and planning job

1. Establish accepted immutable source snapshot, exact scope and app reservation. Read authoritative index/pass/course/session records. If unfinished work exists, resume its recorded worktree/job after recovery. For each genuinely new ingestion fetch `origin/main`, create a fresh unique `codex/<task-slug>` task worktree from the fetched base before any workflow writes, including logs/freshness. Standalone substantive planning also uses a fresh task worktree; ingestion-triggered planning uses the same one.
2. Resolve the new root, copy only authorized uncommitted source inputs when absent, compare hashes with receipt/primary originals and record mapping. Run baseline vault checker and preserve issue identities/targets. Maintain a concise engineering session record with task, base, roots, scope, versions/transactions, checks and blockers.
3. Ingest owner commits blocked freshness through records utility before notes change; rereads/locks before each mutation. It prepares self-contained notes/assets and full coverage under the selected snapshot. Substantive replacements/deletions of existing manual meaning require concrete proposal and actual user approval under ingest; preserve the old content while waiting. Source upload replacement is not implicit approval to remove notes.
4. Fresh independent source reviewer reads the full originals, relevant references, ledger, notes/equations/visuals/priorities/foundations. Require exact inspected scope plus located findings or no-material-findings per dimension. Owner repairs; reviewer rechecks final bytes and affected context. Unreadable content/missing review/material findings hold ingestion incomplete.
5. Validate links/renders, rehash sources, finalize detail log then index, commit complete ingestion state, and verify its actual journal/current bytes. A logging failure or snapshot change retains/reinstates blocked freshness. Git commit alone does not validate a records transaction. Plan begins only from checked complete ingestion and committed owner journals.
6. Plan owner reads finished checked notes/provenance only; prepares all changed objectives, lesson sections, practice/answer keys/rubrics, visuals, prerequisite/repair/retention routes, required-note coverage and version compatibility. Target approximately 25-minute teaching groups with separate quizzes; duration estimates cannot hide required material. Academic gaps return to ingest, then renewed source review and plan reconciliation.
7. Fresh independent curriculum reviewer reads finished notes and every changed route/key/rubric/dependency/version/history. It does not replace finished-note authority with original sources. Plan repairs; reviewer confirms final content. Material later edits reopen relevant review. Ready flags remain blocked until final actual confirmations.
8. Verify committed plan/manifest/each indexed ready lesson transaction, preserve immutable history and canonical learner records. Run post-change vault checker with identity comparison and `git diff --check`; resolve introduced/material affected failures, disclose unrelated baseline issues. Prepare explicit scoped staging and integration intent.

Runtime model routing uses the canonical profiles below, with actual host capability checks. Never silently substitute a weaker model to fit quota. Runtime roles are not automatically available merely because a coding task has the same model.

| Runtime task | Profile | Default model/effort |
| --- | --- | --- |
| Ingest owner | `uni_ingest_owner` | GPT-6.1 Sol / high |
| Bounded read-only draft | `uni_ingest_draft` | GPT-6 Luna / medium |
| Difficult ingest reasoning | `uni_ingest_reasoning_astra` | GPT-6 Astra / high |
| Source reviewer | `uni_source_checker` | GPT-6 Astra / high |
| Plan owner | `uni_plan_owner` | GPT-6.1 Sol / high |
| Curriculum reviewer | `uni_curriculum_checker` | GPT-6 Astra / high |
| Routine teaching/assessment | `uni_teach_owner` | GPT-6 Luna / medium |
| Difficult prepared-rubric adjudication | `uni_teach_assessor` | GPT-6.1 Sol / high |
| Recall operations | `uni_recall_owner` | GPT-6 Luna / low |

Concrete complexity may invoke documented high/xhigh escalation profiles; explicit user settings take precedence and are disclosed. Record requested versus host-confirmed model/effort and actual reviewer identity. Reviewers are fresh separate agents, not authors or draft workers, and have no write grants. If the provider/host cannot establish independent subagent dispatch, block academic publication with that capability gap. Each prompt includes role marker, absolute root, owner skill, full identity/exact locators, stable job/transaction IDs, permitted writes, constraints/trust rules and expected result. Wait for actual dependent results; do not infer review completion from spawning or apparent confidence.

### 6.4 Git integration gate

The repository owner authorizes normal completion only after required gates. The repository adapter must persist integration phases and recover unknown remote outcomes before retry. Stage explicit task-owned paths; inspect staged status/diff and exclude credentials, scratch, transient locks, operational database and unrelated/evidence changes. Preserve required owner transaction journals. Commit with a clear scope. Freshly fetch `origin/main` before integration; if advanced, merge it into the branch without rewriting published history. Inspect shared ingestion index and freshness/version conflicts semantically; never choose a side blindly. Changed affected content requires owner reconciliation and renewed independent review/validation.

Push task branch, create/update a PR targeting main and attach it when host supports attachment. Internal academic/engineering review is not a fabricated GitHub approval. Persist actual PR URL/head, required checks/reviews and `ready_for_merge` session state. Merge only by a repository-allowed method after validated head and required gates; no admin override or force-push main. If permissions/checks/protection fail, retain worktree/PR with `integration_blocked` and exact cause; no current publication yet.

Verify actual merged PR state and remote main merge commit containing the expected academic outputs/journals. Fetch/fast-forward primary checkout only when clean and on main; otherwise preserve changes/divergence and report local sync deferred. Build publication from the verified merged commit snapshot rather than unsynchronized primary bytes. Only after confirmed merge and preservation of needed ignored/untracked artifacts may the adapter delete the task branches and archive/remove its own worktree via host tools. No cleanup of unrelated worktrees. A successful push is not completed integration.

Crash cases: pushed-but-no-PR recovers by branch/head lookup; uncertain PR creation reconciles existing identity; merge timeout reads actual merged state before another merge; merged-but-unsynced builds from verified remote commit while reporting local sync; cleanup timeout rechecks actual artifacts. Do not commit a predicted merge outcome or a follow-up commit solely to record its own hash.

## 7. H10: snapshot conflicts and atomic publication

### 7.1 Readiness and stale-output rejection

Every candidate publication binds full course ID, immutable source snapshot/version map, ingestion revision/transaction/pass, finished-note fingerprints, plan/source versions and committed lesson transactions, independent review receipts tied to exact output hashes, merged commit, schema/compiler versions and asset hashes. Publication readiness is derived from these gates, not a button or job status string. Missing review, unreadable scope, pending journal, stale source, unsupported extension, unresolved replacement approval, incompatible rubric/visual or incomplete coverage forbids Ready.

At each step boundary and immediately before publication compare the candidate snapshot and expected active publication generation against authoritative selected sources, course tokens, records and integration evidence. A new upload increments selection generation and records pending update; do not mutate the old job's snapshot. Cancel/reconcile safe old steps, mark their candidates superseded, and queue the new delta job. No older job can publish over a newer selected snapshot, even if its review finished later. CAS failure is `stale_snapshot`; retain artifacts/reviews for legitimate cache reuse only when exact input/output digests agree.

Keep the last verified publication accessible while an update is being prepared or blocked, labelled with its version and update state. New sessions default to current verified publication only when their required scope is ready; unavailable new content stays unavailable. Do not pretend older content incorporates a failed update.

### 7.2 Publication commit algorithm

1. Persist publication intent with stable ID, candidate identity, expected active generation and integrated commit. Export validated content from that immutable commit; compile schema-safe data into a unique staging directory in the durable publication store. Exclude answer keys/rubrics/solutions from ordinary learner payloads and serve them through authorized assessment paths only.
2. Validate all bundle/schema/link/asset/hash/coverage/visual reference cases, owner readiness and review receipts. Fsync each artifact and staging directory. Rename the complete directory to its immutable content-addressed final path on the same filesystem and fsync the parent. No in-place edits to published files. An orphan finalized directory after crash is harmless until a verified pointer exists.
3. Acquire brief course/publication guard, reread snapshot/revisions/fence and expected active generation. In one SQLite transaction insert publication, CAS the active pointer, and append `publication_committed` plus answer-free notice intent. Release guard. If another generation won, do not switch pointer. Atomic visibility uses one verified pointer to an immutable complete bundle; SQLite and filesystem are not claimed to be one distributed transaction.
4. API reads resolve one publication ID per response/session and serve only complete verified artifacts. Streamed change notifications are delivered from a durable outbox, not transient memory. Retry by event ID and retain client acknowledgement; duplicates must be harmless.
5. On startup, inspect intents. Finalized verified directory plus uncommitted intent may complete after fresh CAS/gate checks; partial staging remains unavailable. Active pointer to missing/corrupt artifacts triggers recovery to a recorded last verified pointer with explicit diagnostic, never silent evidence deletion. Do not garbage-collect artifacts referenced by current/archived sessions, evidence, variants or pending intents.

`hub_foundation` owns generic file-durability helpers; `hub_workflows` owns publication semantics. Atomic replace must use a temporary file in the target filesystem, flush/fsync bytes, replace and fsync parent. Cross-filesystem move requires copy-to-target-staging, verify, fsync and rename. A browser receipt or successful rename alone does not establish all required durable records.

### 7.3 Pinned sessions, progress and update notices

At session start pin publication/lesson/item/rubric/objective/version identities and resume position. An active session continues its exact immutable content. A delayed answer is assessed against its submitted prepared rubric and receives the old attempt identity; do not substitute new answers or regrade original evidence. Newly published content may recommend reassessment only through the plan's prepared compatibility/reassessment rules. Historical events, original attempts, assistance, corrections, exposure, due review identity and immutable curriculum definitions survive rebuilds/uploads/migrations.

After a safe lesson boundary, show an answer-free update notice with affected weeks/lessons, version, applicability and prepared reassessment need. Do not interrupt a prompt or inject a solution before original answer commit. New session resumes choose pinned old content or explicit migration according to the prepared route; position projection changes cannot imply completion/pass. A lesson version removed from navigation remains retrievable for referenced evidence and pinned sessions. No manual completion endpoint, progress reset, localStorage authority or automatic pass for reading duration is introduced.

Answer receipt and exposure delivery are separate operational facts. Durably receive the actual answer before scheduling assessment; commit teach result before feedback is sent. A generated prompt/feedback queued in the outbox is not known learner exposure until acknowledged by the supported delivery contract. Unknown historical/display timing remains unknown. User-facing pending assessment never turns into fail/pass due to timeout or quota.

Recall uses only committed verified learner evidence and course-specific prepared versions. App recommendations/review queues never mix courses or fabricate mastery; deterministic scheduling stays in maintained recall code. Todoist side effects require that workflow's verified existing project, positive task ownership/outbox/reconciliation and actual authorization. An upload does not authorize creating recall tasks; engineering orchestration must hand off through the agreed evidence/recall boundary.

## 8. Integration acceptance and fault matrix

Use isolated temporary Git vaults and deterministic transports for destructive faults; no fictional source coverage or learner events enter the real vault. Software tests verify invariants; independent academic reviews verify content. H15 records exact commands/results and H16 verifies final commit/review applicability. Add focused fixtures rather than tests that merely mirror implementation.

| Fault / acceptance case | Expected durable result |
| --- | --- |
| First registration lacks issued ID / wrong nonce / duplicate callback | No active credentials replaced, no inference; exact authentication failure. |
| Valid identity but missing plan permission | Signed-in account retained; plan inference disabled and explicit enable control. |
| Model catalog contains selected model; actual inference fails | Feasibility remains failed; requested/actual settings and terminal error preserved. |
| Text arrives then quota/failed/incomplete/EOF | No completed step/review/result; checkpoint retained and failure classified. |
| Two refreshers or token replacement crash | Single refresh reservation; latest durable token set only, no mixed-account credentials. |
| Quota unknown reset / established app cap | Coalesced bounded checks, no assumed reset; cap needs relevant eligibility/settings action. |
| Mandatory Astra review unavailable | Candidate blocked/waiting; no automatic downgrade or Ready flag. |
| Lease expires while child remains live | No second writer; confirm stop before fencing transfer. |
| Crash before/after upload fsync/receipt commit | Accepted receipts always have verified bytes; retries return same intent. |
| Same upload hash with successful versus incomplete provenance | Successful unchanged scope skips AI; incomplete scope resumes checks. |
| Earlier-week source change affects later lesson/test | Exact downstream invalidation, independent rechecks, post-lesson notice. |
| Source replacement omits old concept | Old bytes/text retained; ingest proposal/approval if substantive removal required. |
| Sparse extraction/hidden slide/notes/image equation | Explicit inspected ledger/fallback or blocked region; no text-only completion. |
| Reviewer sees material finding after initial approval | Final affected revisions require renewed check, repairs bounded. |
| Pending records journal / external edit hash mismatch | Same-owner recovery/conflict; no raw overwrite or publication. |
| Two worktrees claim same course / external task discovered | One registry reservation; other waits/blocks; external guard limitation disclosed. |
| New snapshot selected while old review finishes | Old candidate superseded; active CAS rejects old publication. |
| Origin advances / shared ingestion index conflicts | Semantic integration and affected owner/reviewer checks; no blind side selection. |
| CI/protection/permissions prevent merge | PR/worktree preserved; integration blocked; no unpublished candidate made current. |
| Crash at each publication filesystem/SQLite boundary | Only old or complete new bundle visible; intent recovery never exposes staging. |
| Answer committed/pending while publication changes | Exact attempt/rubric preserved; no evidence reset or new-version regrade. |
| Feedback generated but browser closes before delivery | Pending outbox, no invented exposure; idempotent actual delivery receipt. |
| Browser/terminal closed, sleep across retry, reboot | Browser closure harmless; wake revalidation; reboot waits for manual launch. |
| Disk full/corrupt DB/incomplete migration/restore | Stop unsafe writes, retain artifacts and last valid content; isolated verified recovery. |

For each runtime academic task run the selected checkout's checks with actual IDs, for example:

```sh
python3 03_Agents/check_vault.py
python3 03_Agents/scripts/records.py status COURSE_DIR
python3 03_Agents/scripts/records.py verify COURSE_DIR ingest INGEST_TX ingestion_state.json
python3 03_Agents/scripts/records.py verify COURSE_DIR plan PLAN_TX learning_plan.md source_manifest.md lessons/OBJECTIVE_ID.md
git diff --check
```

These are templates with real `COURSE_DIR`/transaction/objective values substituted as validated arguments at implementation time. Verify every indexed ready lesson, not one sample. Run records maintenance tests when its code changes, routing/packaging checks when canonical profiles/skills change, and focused schema/provider/worker/publication tests for the actual implementation. Compare vault issue identities and targets before/after, distinguishing absent empty mirrors in a fresh checkout from content failures. A pre-existing nonzero checker result is reported honestly; no fabricated empty course records may make it pass.

## 9. Required handoff output per implementation task

Return exact changed files/module ownership, implemented interfaces/schema migrations, actual tests/faults executed and results, unresolved capability/contract risks, documentation and commit reference. H01 includes real terminal inference confirmation or a precise feasibility blocker; H09 includes compatibility extension status and owner gate enforcement; H10/H14 include crash/restart/restore evidence. Coding agents never claim course readiness from fixture tests. H16 integrates only reviewed compatible commits, resolves module conflicts, reruns affected validation and preserves a recoverable task record. Technical feasibility gaps should produce bounded implementation work or precise blockers, not another broad product questionnaire.
