# Maintenance utilities

Run commands from the repository root. Canonical utilities live here; generated package copies are not maintained sources.

| Utility | Purpose |
| --- | --- |
| [Vault reference checker](../check_vault.py) | Read-only local file, heading, block, source-metadata, hub and course-mirror checks. Includes root documentation and Excalidraw files. |
| [records.py](records.py) | Owner-scoped locks, expected-byte checks, atomic transactions and recovery. Preserves journals and staged bytes. |
| [sync_plugin.py](sync_plugin.py) | Generate/check distribution, role copies and the exact current versioned ZIP; refuses to overwrite differing snapshots. Does not publish or install. |
| [test_vault.py](test_vault.py), [test_records.py](test_records.py), [test_model_routing.py](test_model_routing.py) | Isolated maintenance regression tests. Use Python 3.11+ to include TOML validation. |
| [Recall scheduler](../recall/scripts/schedule.py) | Deterministic recall calculations; see the recall skill for its self-test command and synchronization contract. |

```sh
python3 03_Agents/check_vault.py
python3 -m unittest discover -s 03_Agents/scripts -p 'test_*.py'
python3 03_Agents/scripts/sync_plugin.py --check
```

Full package checks reject missing, unreadable or mismatched ZIPs. Changed snapshot content needs an unused manifest version. For unreleased loose-copy work use `sync_plugin.py --source-only` and `sync_plugin.py --check --source-only`; these preserve ZIPs and explicitly exclude snapshot parity. Neither mode publishes or installs.

The vault check reports structural issues; it does not establish academic accuracy, coverage or learner mastery. Missing course mirrors can be absent empty directories in fresh Git checkouts. See the [audit baseline](../history/2026-10-17-repository-audit/REPORT.md) and [subsequent note-reference repairs](../history/2026-10-17-repository-audit/NOTE_REFERENCE_REPAIRS.md) for the issue history.

For a selected course, inspect `records.py status COURSE` before any workflow write. Verification uses `records.py verify COURSE OWNER TRANSACTION_ID OWNED_RECORD...`; recovery belongs to the owning skill. Committed transaction journals and `.stage` files are recovery/provenance data, not disposable cache files.
