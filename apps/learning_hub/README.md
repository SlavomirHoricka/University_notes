# Uni Learning Hub

Partial engineering checkpoint: a loopback health API, typed SQLite/domain foundation, private provider-state storage, and a responsive course/materials React shell. Course data and save authorization are not connected to production handlers yet. Course publication, provider access, learner evidence and the detached manual launcher are not available yet. Health reports `ready: false` with `reason: scaffold_only`.

## Locked development install

Use Python **3.12**, Node **24 LTS** and uv **0.13.0**. This scaffold was verified on macOS 27.0 arm64 with Python 3.12.15 and Node 24.21.0 (npm 11.19.0). See [development.md](docs/development.md) for resolved versions and ownership.

Install uv from its [official instructions](https://docs.astral.sh/uv/getting-started/installation/) and Node from the [official LTS archive](https://nodejs.org/dist/v24.21.0/). Verify the downloaded Node archive against its SHASUMS256.txt. uv manages Python 3.12 using its [documented managed-runtime support](https://docs.astral.sh/uv/guides/install-python/). Tool binaries are not committed.

Run from this directory, with uv and Node 24 on PATH:

```sh
export UV_CACHE_DIR="$PWD/.tools/uv-cache"
export UV_PYTHON_INSTALL_DIR="$PWD/.tools/python"
export npm_config_cache="$PWD/.tools/npm-cache"
export PLAYWRIGHT_BROWSERS_PATH="$PWD/.tools/playwright"
uv python install 3.12 --no-bin
make install
make diagnostic
(cd frontend && npx --no-install playwright install chromium)
make check-all build
```

The foundation development checkout additionally has isolated uv under `.tools/` and Node under `.tools/node-v24.21.0-darwin-arm64/bin/`. To use those already installed binaries, prepend both absolute directories to PATH. Each fresh checkout needs its own dependencies; use `uv sync --locked` and `npm ci`, not an unlocked install. Node's engine range and the diagnostic reject other major versions. Runtime state and secrets belong outside Git; app-local `.runtime/` and `.private/` are ignored development scratch only.

## Foreground development

In one terminal, from this directory:

```sh
uv run --locked uvicorn learning_hub.application.core.bootstrap:create_app --factory --host 127.0.0.1 --port 8765
```

In a second terminal:

```sh
cd frontend
npm run dev
```

Open `http://127.0.0.1:5173`. Vite proxies `/api` to the loopback API. Use Ctrl-C in each terminal to stop those foreground servers. `make launch` and `make stop` intentionally fail with exit 2 until H14 supplies the detached supervisor; they do not report a successful no-op. An occupied port is an error: do not kill an unrelated process. No autostart, remote binding or account inference is enabled.

## Checks and generated API

`make check-unit` runs Ruff lint/format, strict mypy, Python unit tests and component tests. `check-contracts` validates strict health fields and generated OpenAPI/TypeScript drift. `check-integration` verifies app composition, vault isolation, Host rejection and Git boundaries. `check-ui` runs ESLint, strict TypeScript and semantic component checks. `check-e2e` starts real foreground API/Vite servers, runs Playwright and stops them. It currently exercises H00 only; no worker is implemented. `check-all` invokes all checks and propagates failure. `build` makes a backend wheel/sdist using locked build dependencies and frontend assets without source maps.

Run `make export-contracts` after an approved backend contract change, then commit both generated files. Do not edit generated TS or the OpenAPI fixture manually. Router owners request composition changes through foundation's `create_app(routers=...)` hook. No source tree or runtime directory is mounted as static web content.

Engineering tests use synthetic transports and temporary fictional vaults. They cannot certify academic readiness. Later tasks add feature acceptance tests to the same targets; a passing scaffold is not a finished application.
