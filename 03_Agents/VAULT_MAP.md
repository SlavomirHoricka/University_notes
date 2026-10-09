# Vault map

Filesystem verified 2026-10-03. Navigation only; note counts and existing files do not prove coverage or learning.

- `00_Materials/<year>/<semester>/<course>/`: user-owned raw sources.
- `01_Notes/<year>/<semester>/<course>/`: course notes, hubs and assets.
- `02_Resources/`: shared resources.
- `03_Agents/<year>/<semester>/<course>/`: mirrored course runtime records; exclusive owners in [[03_Agents/LEARNING_ARCHITECTURE]].
- `03_Agents/{ingest,plan,teach,recall}/`: canonical maintained skills.
- `03_Agents/runtime/ingest/`: ingestion index and pass records.
- `03_Agents/history/`: historical reviews, migration/audit results and releases.
- `03_Agents/validation/`: sample curriculum and contract rehearsals, never learner outcomes.

## Verified course inventory

| Course identity under notes and agent mirror | Markdown notes | Hub | Existing course records |
|---|---:|---|---|
| `2024_2025/Summer_Semester/JEB004_Ekonomie_II` | 0 | — | — |
| `2024_2025/Summer_Semester/JEB006_Matematika_II` | 0 | — | — |
| `2024_2025/Summer_Semester/JEB024_Základy_Soukromého_Práva` | 0 | — | — |
| `2024_2025/Summer_Semester/JEB046_Účetnictví_I` | 0 | — | — |
| `2024_2025/Summer_Semester/JEB059_Seminář_Matematické_Analýzy_a_Algebry_II` | 0 | — | — |
| `2024_2025/Summer_Semester/JEB104_Microeconomics_I` | 18 | `JEB104_Microeconomics_I_main.md` | — |
| `2024_2025/Summer_Semester/JEB142_Introductory_Statistics` | 18 | `JEB142_Introductory_Statistics_main.md` | — |
| `2024_2025/Summer_Semester/JLB004_Angličtina_pro_Ekonomy_II` | 0 | — | — |
| `2024_2025/Summer_Semester/JPB198_Úvod_do_Politologie` | 0 | — | — |
| `2024_2025/Winter_Semester/JEB005_Matematika_I` | 0 | — | — |
| `2024_2025/Winter_Semester/JEB023_Úvod_do_Studia_Práva` | 0 | — | — |
| `2024_2025/Winter_Semester/JEB055_Seminář_k_Aktualitám_I` | 0 | — | — |
| `2024_2025/Winter_Semester/JEB058_Seminář_Matematické_Analýzy_I` | 0 | — | — |
| `2024_2025/Winter_Semester/JEB101_Principles_of_Economics_I` | 0 | — | — |
| `2024_2025/Winter_Semester/JEB111_Advanced_Data_Analysis_in_MS_Excel` | 0 | — | — |
| `2024_2025/Winter_Semester/JLB003_Angličtina_pro_Ekonomy_I` | 0 | — | — |
| `2025_2026/Summer_Semester/JEB010_Makroekonomie_II` | 14 | `JEB010_Makroekonomie_II_main.md` | — |
| `2025_2026/Summer_Semester/JEB029_Matematika_IV` | 0 | — | — |
| `2025_2026/Summer_Semester/JEB050_International_Finance` | 13 | `JEB050_International_Finance_main.md` | — |
| `2025_2026/Summer_Semester/JEB109_Econometrics_I` | 17 | `JEB109_Econometrics_I_main.md` | learning_log.md, learning_plan.md, source_manifest.md |
| `2025_2026/Summer_Semester/JEB154_Bachelors_Thesis_Seminar_I` | 0 | — | — |
| `2025_2026/Summer_Semester/JEB160_Auctions_and_Game_Theory` | 1 | `JEB160_Auctions_and_Game_Theory_main.md` | — |
| `2025_2026/Winter_Semester/JEB009_Makroekonomie_I` | 13 | `JEB009_Makroekonomie_I_main.md` | — |
| `2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie` | 25 | `JEB027_Finanční_Ekonomie_main.md` | — |
| `2025_2026/Winter_Semester/JEB033_Matematika_III` | 0 | — | — |
| `2025_2026/Winter_Semester/JEB044_Financial_Accounting` | 17 | `JEB044_Financial_Accounting_main.md` | — |
| `2025_2026/Winter_Semester/JEB105_Statistics` | 43 | `JEB105_Statistics_main.md` | — |
| `2025_2026/Winter_Semester/JEB108_Microeconomics_II` | 19 | `JEB108_Microeconomics_II_main.md` | — |
| `2025_2026/Winter_Semester/JEB157_Data_Analysis_in_R` | 0 | — | — |
| `2026_2027/Winter_Semester/Behavioral_Economics` | 0 | — | — |
| `2026_2027/Winter_Semester/Comparative_Economics` | 4 | `Comparative_Economics_main.md` | — |
| `2026_2027/Winter_Semester/Econometrics_II` | 0 | — | — |
| `2026_2027/Winter_Semester/Economics_of_Green_Deal` | 0 | — | — |
| `2026_2027/Winter_Semester/Financial_Markets_Instruments_I` | 0 | — | — |
| `2026_2027/Winter_Semester/JEM231_Mergers_and_Acquisitions` | 4 | `JEM231_Mergers_and_Acquisitions_main.md` | — |

## Scope and freshness facts

Comparative Economics Week 1 is covered by the completed ingestion pass linked from [[03_Agents/runtime/ingest/ingestion_log]]. Its historical run ID includes behavioral because the user-supplied folder was originally elsewhere; the actual course identity and authorized relocation are preserved in that pass. Behavioral Economics has no finished notes. Legacy Econometrics I contains a real prior BLUE lesson, plan and source manifest; they are preserved exactly, with partial acquisition and unknown current readiness. No course ingestion-state or recall-state files were invented by this audit.

The old map's assertion that no teaching sessions existed and that teach established source manifests was stale. Plan now owns manifests; ingest owns academic completion. A course without explicit ingestion completion needs adoption/verification, not presumed readiness. User edits outside workflow require explicit plan freshness check.

Four pre-existing missing conceptual targets remain; the expanded checker also identifies two pre-existing note heading links. Academic content repairs belong to ingest with source verification. Run `python3 03_Agents/check_vault.py`; generated packages/history are excluded from live target disambiguation. Unicode NFC/NFD forms compare equivalently; write links with actual filesystem spelling.
