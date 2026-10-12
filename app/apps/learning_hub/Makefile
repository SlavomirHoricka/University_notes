UV ?= uv
NPM ?= npm
RUN = $(UV) run --locked
.PHONY: install diagnostic check-unit check-contracts check-integration check-ui check-e2e check-all build export-contracts launch stop
install:
	$(UV) sync --locked
	cd frontend && $(NPM) ci --no-audit --no-fund

diagnostic:
	$(RUN) python scripts/diagnostic.py

check-unit:
	$(RUN) ruff check backend scripts tests
	$(RUN) ruff format --check backend scripts tests
	$(RUN) mypy
	$(RUN) pytest tests/unit
	cd frontend && $(NPM) run test

check-contracts:
	$(RUN) pytest tests/contracts
	$(RUN) python scripts/export_contracts.py --check

check-integration:
	$(RUN) pytest tests/integration

check-ui:
	cd frontend && $(NPM) run lint
	cd frontend && $(NPM) run typecheck
	cd frontend && $(NPM) run test

check-e2e:
	cd frontend && $(NPM) run test:e2e

check-all: check-unit check-contracts check-integration check-ui check-e2e

build: check-contracts
	$(RUN) python -m build --no-isolation
	cd frontend && $(NPM) run build

export-contracts:
	$(RUN) python scripts/export_contracts.py

launch stop:
	@echo "H14 launcher/supervisor is not implemented. See README for foreground development servers." >&2
	@exit 2
