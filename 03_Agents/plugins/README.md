# Generated plugin and release status

| Path | Purpose |
| --- | --- |
| [uni-teach/](uni-teach/) | Generated distribution. Edit canonical skill/reference sources, then regenerate. |
| [uni-teach-release.json](uni-teach-release.json) | Receipt for the last confirmed private publication and separately observed host activation. |
| [uni-teach-0.5.2.zip](uni-teach-0.5.2.zip) | Exact archive named by the confirmed 0.5.2 receipt; preserved unchanged. |
| [uni-teach-0.5.3.zip](uni-teach-0.5.3.zip) | Prepared repository-cleanup package; not published or installed by this task. |
| [Earlier releases](../history/plugin-releases/README.md) | Superseded archives, preserved in history. |

From the repository root:

```sh
python3 03_Agents/scripts/sync_plugin.py
python3 03_Agents/scripts/sync_plugin.py --check
```

The synchronizer checks source parity and builds the ZIP matching the package manifest version. Assign a new version before regenerating changed content; preserve previously published ZIPs and the receipt. Publication and host reload are separate operations. This cleanup prepares local artifacts only.
