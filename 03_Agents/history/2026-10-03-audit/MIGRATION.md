# Migration map

Performed 2026-10-03. No raw materials, academic notes/assets, registered symlinks, course paths, or real learner records moved. Historical claims preserved. Ingestion navigation paths, historical-authority labels, and affected historical relative links were rewritten after relocation; original exact bytes remain in `original_agents/` and hashes in baseline.

| Old vault path | Final vault path | Preservation |
|---|---|---|
| `03_Agents/ingest/ingestion_log.md` | `03_Agents/runtime/ingest/ingestion_log.md` | Original SHA-256 `20169c07701dfedacd261adac3ebdb4a45f9cfae6dad1493422c7be9d671855f`; history kept |
| `03_Agents/ingest/logs/20261003T142217+0200_behavioral_week1.md` | `03_Agents/runtime/ingest/logs/20261003T142217+0200_behavioral_week1.md` | Original SHA-256 `00ca3f92ba1d9a8532348b388969cb443bd025b1e164ec40b24318f270ed6a79`; history kept |
| `03_Agents/TEACHING_SKILL_REVIEW_PROMPT.md` | `03_Agents/history/2026-10-02-teaching-review/TEACHING_SKILL_REVIEW_PROMPT.md` | Original SHA-256 `5872d2c87d83fb37202cb1c58309c1f99859af91b936e03ae550f61df93e9fd0`; history kept |
| `03_Agents/TEACHING_SKILL_REVIEW.md` | `03_Agents/history/2026-10-02-teaching-review/TEACHING_SKILL_REVIEW.md` | Original SHA-256 `3776dec9bcc76f6ce3e45a3877ed0308ec76257d66cf715edcd7e1e118af3e9a`; history kept |
| `03_Agents/STANDARDIZATION_REPORT.md` | `03_Agents/history/2026-10-02-standardization/STANDARDIZATION_REPORT.md` | Original SHA-256 `c370feeaa8c60aec84b2b69a2158492722193116236a0c331c773b27bcbd0431`; history kept |
| `03_Agents/standardization_manifest.json` | `03_Agents/history/2026-10-02-standardization/standardization_manifest.json` | Original SHA-256 `31dc2858cf8c0fadf3e15ad1eb6437b56c76a0998827ea98a8411d4445ab5208`; history kept |
| `03_Agents/plugins/uni-teach-0.1.0.zip` | `03_Agents/history/plugin-releases/uni-teach-0.1.0.zip` | Original SHA-256 `ad11d08e823034daa3a3e157e10d7107fe109c0e335e8e594a9dda91af91b727`; history kept |
| `03_Agents/plugins/uni-teach-0.2.3-update.zip` | `03_Agents/history/plugin-releases/uni-teach-0.2.3-update.zip` | Original SHA-256 `b3b9d7f8834d78d6302745b3e795dae98ab85af1b8d364f3e7db38b8f31ea26e`; history kept |

Top-level historical Markdown filenames remain explicit archive redirects. Old duplicate teaching planning-template paths remain deprecation redirects to the plan-owned templates. Generated package copies are refreshed from the canonical paths, not relocated independent sources.

Runtime ingestion logs are excluded from packaged skills. The historical standardization manifest lives with its report; its content is unchanged. No names were normalized on disk. Skill registrations remain `~/.agents/skills/ingest -> 03_Agents/ingest` and `teach -> 03_Agents/teach`. Plan/recall use the installed plugin namespace.

Obsidian lookup uses explicit vault paths to historical targets; history does not enter basename disambiguation. Maintained consuming instructions all name final storage paths. Immutable pre-audit snapshots intentionally retain original references as historical evidence, not active links.
