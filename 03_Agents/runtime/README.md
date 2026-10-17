# Workflow runtime navigation

| Records | Owner and use |
| --- | --- |
| [Ingestion index](ingest/ingestion_log.md) | Ingest-owned navigation to source scopes and complete/incomplete passes. |
| [Pass records](ingest/logs/) | Coverage, source locators and review results; authoritative detail behind the index. |
| [Todoist project map](recall/project_map.json) | Recall-owned factual mappings to verified existing projects. |
| [Engineering sessions](sessions/) | Task handoffs, checks, PR/merge evidence and recovery steps; never learner evidence. |

Course-specific runtime files stay under `03_Agents/<year>/<semester>/<course>/`, alongside the corresponding curriculum. Use the [vault map](../VAULT_MAP.md) to navigate. The [architecture](../LEARNING_ARCHITECTURE.md) defines the owner of each file.

Read a session's full handoff before resuming: an older `ready_for_merge` line may precede later integration evidence. Verify current Git/worktree/remote state rather than inferring ongoing work from a historical heading. Locks and transaction journals must be inspected before course mutations; do not remove recovery data as housekeeping.
