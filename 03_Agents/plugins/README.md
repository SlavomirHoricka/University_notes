# Generated plugin and release status

| Path | Purpose |
| --- | --- |
| [uni-teach/](uni-teach/) | Generated distribution. Edit canonical skill/reference sources, then regenerate. |
| [uni-teach-release.json](uni-teach-release.json) | Receipt for the last confirmed private publication and separately observed host activation. |
| [uni-teach-0.5.2.zip](uni-teach-0.5.2.zip) | Preserved 0.5.2 archive; its previous receipt is retained in history. |
| [uni-teach-0.5.3.zip](uni-teach-0.5.3.zip) | Preserved repository-cleanup snapshot; later loose-copy role formatting is absent from this ZIP. |
| [uni-teach-0.5.4.zip](uni-teach-0.5.4.zip) | Published private 0.5.4 release; installed cache and all four host skill reads verified against the audited package. |
| [Earlier releases](../history/plugin-releases/README.md) | Superseded archives, preserved in history. |

From the repository root:

```sh
python3 03_Agents/scripts/sync_plugin.py
python3 03_Agents/scripts/sync_plugin.py --check
```

The synchronizer checks source/role parity and every ZIP entry against the package manifest version. Missing/corrupt/differing ZIPs fail full checks. Generation refuses to overwrite a differing existing snapshot; assign an unused version for changed snapshot content. Identical existing snapshots retain their exact bytes. For unreleased loose-copy work use `sync_plugin.py --source-only` and `sync_plugin.py --check --source-only`; these preserve all ZIPs and do not assert release parity. Preserve all previous snapshots and the publication receipt. Publication, installed-cache verification and conversation activation are separate facts. The current receipt confirms 0.5.4 publication and installation; start a new chat to use the updated skill snapshot. The [previous 0.5.2 receipt](../history/plugin-releases/uni-teach-0.5.2-release.json) is preserved as dated evidence.
