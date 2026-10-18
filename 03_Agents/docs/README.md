# Workspace documentation

Shared guidance is maintained here. Execution instructions and skill-owned templates, references, utilities and assets live together in [skills/](../skills/README.md).

| Document | Authority |
| --- | --- |
| [Learning architecture](LEARNING_ARCHITECTURE.md) | Shared ownership, freshness, versions, recovery and handoffs across the four core stages and optional html-course export. |
| [Naming conventions](NAMING_CONVENTIONS.md) | New filenames, course identities and link rules. |
| [Learning methods](LEARNING_METHODS.md) | Evidence and limitations behind study defaults. |
| [Lesson content](LESSON_CONTENT.md) | Self-contained lessons, note reuse and bounded teaching additions. |
| [Model routing](MODEL_ROUTING.md) | Owner, helper and independent reviewer contracts. |
| [Plugin README source](PLUGIN_README.md) | Maintained source of the generated distribution README. Its package-relative paths describe the installed package layout. |

The [workspace README](../README.md) and [vault map](../VAULT_MAP.md) are the only top-level files in `03_Agents/`. Maintenance tools, including `check_vault.py`, live in [scripts/](../scripts/README.md). Historical reports retain dated paths; publication receipts and previous ZIPs preserve their original bytes.

## Standalone registration migration

The standalone names `~/.agents/skills/ingest` and `~/.agents/skills/teach` stay the same. After the primary checkout includes this layout, their symlink targets need to become `/Users/slavomirhoricka/Desktop/University_notes/03_Agents/skills/ingest` and `/Users/slavomirhoricka/Desktop/University_notes/03_Agents/skills/teach`.

At the 2026-10-18 audit, the primary checkout has unrelated uncommitted materials, so its fast-forward and these two external link changes are deferred together. Existing links continue to target its existing folders. Do not point personal registrations into a temporary worktree. Verify current checkout/link state before migration; installed plugin caches are separate versioned snapshots and are never edited in place.
