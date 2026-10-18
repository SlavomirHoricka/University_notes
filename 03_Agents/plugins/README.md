# Generated plugin and release status

| Path | Purpose |
| --- | --- |
| [uni-teach/](uni-teach/) | Generated distribution. Edit canonical skill/reference sources, then regenerate. |
| [uni-teach-release.json](uni-teach-release.json) | Receipt for the last confirmed private publication and separately observed host activation. |
| [uni-teach-0.5.2.zip](uni-teach-0.5.2.zip) | Exact archive named by the confirmed 0.5.2 receipt; preserved unchanged. |
| [uni-teach-0.5.3.zip](uni-teach-0.5.3.zip) | Preserved repository-cleanup snapshot; later loose-copy role formatting is absent from this ZIP. |
| [uni-teach-0.5.4.zip](uni-teach-0.5.4.zip) | Current prepared workflow-consistency package; no private publication or installation performed. |
| [Earlier releases](../history/plugin-releases/README.md) | Superseded archives, preserved in history. |

From the repository root:

```sh
python3 03_Agents/scripts/sync_plugin.py
python3 03_Agents/scripts/sync_plugin.py --check
```

The synchronizer checks source/role parity and every ZIP entry against the package manifest version. Missing/corrupt/differing ZIPs fail full checks. Generation refuses to overwrite a differing existing snapshot; assign an unused version for changed snapshot content. Identical existing snapshots retain their exact bytes. For unreleased loose-copy work use `sync_plugin.py --source-only` and `sync_plugin.py --check --source-only`; these preserve all ZIPs and do not assert release parity. Preserve all previous snapshots and the publication receipt. Publication and host reload are separate operations. This cleanup prepares local artifacts only.
