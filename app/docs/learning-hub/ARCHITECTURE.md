# Engineering architecture and ownership

The application is a modular monolith with a separate durable worker. Use Python/FastAPI/Pydantic for backend contracts and existing Python utility integration, React/TypeScript/Vite for the frontend, SQLite for operational state, and the vault's owner records for academic/evidence authority. Final dependency versions are resolved and locked in H00 from supported releases; document installed versions and use the same locks in CI. Baseline Python 3.12 and a supported Node LTS; install isolated runtimes if the host system Python is too old. Do not require Docker, Redis, hosted vector databases or separate SaaS accounts for the initial app.

## Source tree and single owners

```text
apps/learning_hub/
  README.md                     # operations-owned user setup/manual launch
  pyproject.toml, uv.lock        # foundation establishes; edits serialized
  frontend/package.json, package-lock.json
  frontend/src/
    app/                        # frontend router/providers/layout
    features/courses/
    features/lessons/
    features/assessments/
    features/reviews/
    features/agents/
    components/{math,outline,questions}/
    components/visuals/         # visuals-owned implementations
    api/{generated,client}/     # generated from backend schema; foundation owns generator
    styles/                     # frontend tokens/layout; visuals uses them
  backend/learning_hub/
    domain/{models,ports}/      # foundation: schema and typed interfaces
    domain/{grading,selection,review_policy}/ # assessment
    application/core/          # foundation composition/config/receipt projections
    application/{attempts,assessments,reviews}/ # assessment
    application/{uploads,ingestion,publication}/ # workflows
    adapters/storage/          # foundation SQLite repositories/migrations
    adapters/evidence/         # foundation receipt-to-teach adapter interface
    adapters/codex/            # provider OAuth/RPC/process/model adapter
    adapters/{vault,extraction,repository}/ # workflows owner wrappers and source processing
    api/core/                  # foundation common errors/session/SSE core
    api/{courses,lessons}/      # foundation reads; player requests defined in CONTRACTS
    api/provider/              # provider authentication/model/usage endpoints
    api/workflows/             # workflows upload/job/publication endpoints
    api/assessments/            # assessment submissions/results/reviews
    worker/                    # workflows leases/execution/dependency orchestration
    operations/                # operations lifecycle/backup/health CLI
  scripts/                     # operations launcher; foundation schema export script
  tests/{unit,contracts,integration}/ # each owner adds its feature tests
  tests/e2e/                   # QA cross-feature Playwright acceptance
  tests/fixtures/               # synthetic/permissioned inputs; never real learner outcomes
  docs/                        # runbooks by module owner, operations assembles
docs/learning-hub/              # this fixed instruction package, coordinator-owned changes
.codex/agents/hub_*.toml         # engineering roles, coordinator-owned changes
```

No worker edits another owner's module by convenience. A needed interface change is a proposed patch; root assigns it to the owner and serializes changes. H00 creates minimal package entry points and quality tooling; root records its exact bootstrap files, then transfers future feature edits to the registered owner. Longest matching owned-path prefix wins: visuals owns `frontend/tests/visuals/`, frontend owns the other frontend tests. Later owners register routers/components through declared composition hooks; root routes shared composition edits to foundation. Foundation owns all migrations, models and generated contract tooling, including additions requested by other owners. This prevents competing SQL schemas and drifting hand-written frontend types.

Typed protocols include `Clock`, `IdGenerator`, `ReceiptRepository`, `EvidenceWriter`, `CurriculumReader`, `SourceInventory`, `PublicationStore`, `ProviderClient`, `JobRepository`, `CourseReservation`, `RepositoryIntegrator`. Use concrete implementations at the composition root; pure grading/selection functions need no network/file dependencies. Do not build a generic dependency-injection framework.

## Runtime topology

`hub launch` starts a detached local supervisor if none is running, waits for health, and opens the default browser. Supervisor manages one HTTP server, one worker and provider subprocesses. Closing the browser does not signal shutdown. `hub stop` requests graceful quiescence; a job checkpoint/held transaction is recovered before later retry. H14 defines/implements actual console commands and the double-click launcher; commands here are target behavior, not currently installed executables.

In production the backend serves built frontend assets and `/api/v1` on a single loopback origin, default `127.0.0.1:8765`. If that port is occupied, discover the existing app instance by its instance identity; never kill the other process or silently expose a different service. A non-app conflict yields a clear alternate-port action and persisted configured origin. During development Vite proxies `/api` to the local backend; fixed allowed origins are documented. No wildcard CORS/Host matching.

Keep a dedicated user data directory outside Git (macOS default `~/Library/Application Support/UniLearningHub/`). Configure an absolute primary vault path and separately selected content-worktree roots. Secrets use Keychain through an abstraction; any supported fallback file has owner-only access and is never logged or copied into a worktree. Runtime databases, uploads cache, logs and PID/instance files are outside repository source control. Keep source originals/authoritative academic records in their declared vault paths. Do not couple the app lifetime to a Codex desktop window.

SQLite uses migrations, foreign keys, busy timeout and explicit short transactions. WAL is local-machine only; do not put it on a network filesystem or copy only the `.db` file while active. Backup through a consistent database API plus canonical-record snapshot, as specified by H14. Operational DB loss cannot be repaired by inventing evidence: rebuild projections from verified records and show missing pending receipts honestly. [SQLite WAL behavior](https://sqlite.org/wal.html).

## Boundaries and trust

- UI can submit actual answers and navigation receipts, never scores, mastery flags, course file paths or trusted completion.
- Backend owns deterministic grading and version checks. AI assesses written answers only against prepared private criteria. Keys and unseen retention banks stay off ordinary learner payloads.
- Source/learner text is untrusted. Wrappers allow only declared tools/paths, validating output schemas and owner permissions. Never concatenate uploaded instructions into privileged prompts or grant source text tool authority.
- Notes, plans, evidence and schedules retain separate owners. Receipt/outbox/projection DB is not a second academic authority. Site completion is a process projection; objective acquisition and retention remain evidence-based.
- Owner writes go through compatible current/proposed records contracts and verify journals. Concurrent course content work is reserved across worktrees, not just inside each checkout's lock.
- Runtime ingestion/planning uses task worktree/branch and existing independent checks/normal protected integration. Frequent teach/recall writes use owner transactions in the configured runtime vault under coordination, not a new content PR per click. Git must never overwrite dirty actual learner records during a primary fast-forward; separate staging/preservation/reconciliation is required.
- Public publication is one immutable versioned snapshot plus atomic pointer; private assessments map to it. Sessions pin versions. Source freshness can block affected new work without destroying the last valid snapshot or prior evidence.

## Contract extension gate

H02 specifies proposed site-facing and owner-record extensions; H09 implements canonical compatibility support, validator updates, migrations and tests. They are engineering maintenance changes, not permission to mutate historic learner events. Preserve byte-identical legacy prefixes and existing schema-3 events. New web process state must not masquerade as existing acquisition events. Source provenance and readiness remain current-skill rules.

Never make the backend directly call an LLM to rewrite course records and then label them verified. Each stage executes its owner and journals. Web manifests are plan-owned artifacts only after the contract supports them; otherwise a read-only export derives from checked canonical artifacts and records exact source tuples. Contract choice in CONTRACTS is binding after its gate passes.

## Engineering quality/release

Implement one vertical slice per ticket. Avoid app-wide stringly typed dictionaries, mega-hooks, global mutable service state, or duplicated frontend/backend grading. Keep public interfaces typed and errors explicit. Document invariants and reasons, not every line. Every required acceptance case must map to a named test or observed pilot evidence.

H00 establishes Ruff, mypy/pyright (choose one and document), pytest, ESLint, TypeScript strict checks, frontend component tests and Playwright. H15 uses synthetic fault-injection provider and temporary vaults; H16 separately proves supported real account inference and real checked course publication. Network/provider access is mocked in ordinary CI; required real tests produce redacted receipts rather than credentials in logs.

The complete release includes a setup/diagnostic command, launcher, health/readiness views, working upload-to-study flow, quota recovery, immutable attempts, recovery/restore tests and operation docs. A browser-only prototype or schema migration without tests is not deliverable.

Later mobile support replaces only the loopback exposure/auth/deployment layer and extends responsive UI; it must revisit OAuth deployment eligibility, TLS, user identity, sync/conflicts and offline submission. Do not expose app-server or filesystem access directly to phones. It is outside H00–H16.
