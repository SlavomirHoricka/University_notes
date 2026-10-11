# H00 development baseline

Input integration SHA: `2d7a8215aa7e08bfc5155f4ad9fa133c2e6e97c0`. Role: hub_foundation, requested native `gpt-6.1-sol` / high; host role declaration specifies those settings, independent runtime telemetry is unavailable.

Python is constrained to 3.12; uv.lock pins the full Python graph and hashes. Frontend direct versions and package-lock.json pin the npm graph and integrity. The installed baseline is Python 3.12.15, uv 0.13.0, Node 24.21.0 LTS, npm 11.19.0 on macOS 27.0 arm64. [Node release archive](https://nodejs.org/dist/v24.21.0/), [uv Python support](https://docs.astral.sh/uv/reference/policies/python/), and [Vite runtime requirements](https://vite.dev/guide/) document supported tooling. Registry release metadata is retained in the dependency locks.

| Tool | Resolved version |
| --- | --- |
| FastAPI | 0.143.0 |
| Pydantic | 2.14.0 |
| Uvicorn | 0.54.0 |
| Ruff | 0.17.0 |
| mypy | 1.20.2 |
| pytest | 9.1.1 |
| build / hatchling | 1.6.1 / 1.32.4 |
| React / React DOM | 19.3.0 |
| TypeScript | 5.9.3 |
| Vite | 8.3.4 |
| Vitest | 5.0.3 |
| ESLint | 10.12.0 |
| Playwright | 1.64.0 |
| openapi-typescript | 7.13.0 |

The Python checker is **mypy strict**, selected to cover domain ports, composition, scripts and tests. No missing-import or blanket lint/type suppression is configured. Third-party stub internals are skipped by TypeScript's skipLibCheck; application checking remains strict, including unchecked indexed access and exact optional fields. Generated TS is lint-excluded because it is owned by openapi-typescript, but remains part of strict TypeScript checking. React development runs under StrictMode.

The current Starlette TestClient accepts httpx 0.28.1 and emits a deprecation warning recommending httpx2. It remains visible; tests neither suppress warnings nor substitute production provider success. A future test-client transport update should be reviewed with the locked FastAPI/Starlette version.

## Bootstrap ownership transfer

H00 creates only empty Python feature namespaces outside foundation's prefix, the initial React app/main/style/test files, Playwright configuration/smoke test, and initial README. After root acceptance, feature namespace entrypoints transfer to the role owning their longest registry prefix; frontend app/main/styles/component tests transfer to frontend, e2e test/config to QA, README to operations. Foundation retains shared Makefile, dependency/quality configs, package-parent entrypoints, schema generator, generated API, core/bootstrap/health/runtime ports and foundation tests. Owners must request shared config or composition changes through root/foundation. This document records bootstrap scope; root records the definitive accepted file list in its receipt.

## Acceptance scope

H00 health is liveness only. There are no public course, session or evidence mutations, no private answer bank, no database migration, no provider dispatch, and no production test fixture. Only the health path is exported to OpenAPI. Namespace entrypoints do not imply implemented capabilities. Later H02/H03 own models/storage/receipts; H08 owns worker; H14 owns operations. Tests deliberately assert missing course/manual-completion routes and readiness false.

The test transport only accepts `https://fixture.invalid/status` and returns a known synthetic failure. Temporary fixture vaults have no real course/learner history. Playwright's smoke test talks to actual loopback HTTP; it cannot establish missing worker or subscription behavior.

Install diagnostics report versions and missing tooling/lockfiles, with a nonzero result for unsupported runtime. They do not inspect credentials, academic records or remote account eligibility. Runtime ignore rules are app-scoped and preserve canonical journal visibility outside the app.
