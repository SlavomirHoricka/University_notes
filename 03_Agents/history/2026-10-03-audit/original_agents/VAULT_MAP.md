# Vault map

Updated: 2026-10-02 after standardization. Paths are vault-relative. This is navigation, not a learner assessment.

## Layout

- `00_Materials/<academic_year>/<semester>/<course>/`: original sources, mostly PDFs.
- `01_Notes/<academic_year>/<semester>/<course>/`: Markdown notes, `<course_folder>_main.md` hubs, and assets.
- `02_Resources/`: shared resources; no course tree currently exists.
- `03_Agents/<academic_year>/<semester>/<course>/`: mirrors all 35 note-course folders for future plans and logs.

## Course inventory

| Course path under 01_Notes and 03_Agents | Markdown files | Hub |
|---|---:|---|
| `2024_2025/Summer_Semester/JEB004_Ekonomie_II` | 0 | None; no topic notes |
| `2024_2025/Summer_Semester/JEB006_Matematika_II` | 0 | None; no topic notes |
| `2024_2025/Summer_Semester/JEB024_Základy_Soukromého_Práva` | 0 | None; no topic notes |
| `2024_2025/Summer_Semester/JEB046_Účetnictví_I` | 0 | None; no topic notes |
| `2024_2025/Summer_Semester/JEB059_Seminář_Matematické_Analýzy_a_Algebry_II` | 0 | None; no topic notes |
| `2024_2025/Summer_Semester/JEB104_Microeconomics_I` | 18 | `JEB104_Microeconomics_I_main.md` |
| `2024_2025/Summer_Semester/JEB142_Introductory_Statistics` | 18 | `JEB142_Introductory_Statistics_main.md` |
| `2024_2025/Summer_Semester/JLB004_Angličtina_pro_Ekonomy_II` | 0 | None; no topic notes |
| `2024_2025/Summer_Semester/JPB198_Úvod_do_Politologie` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JEB005_Matematika_I` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JEB023_Úvod_do_Studia_Práva` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JEB055_Seminář_k_Aktualitám_I` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JEB058_Seminář_Matematické_Analýzy_I` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JEB101_Principles_of_Economics_I` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JEB111_Advanced_Data_Analysis_in_MS_Excel` | 0 | None; no topic notes |
| `2024_2025/Winter_Semester/JLB003_Angličtina_pro_Ekonomy_I` | 0 | None; no topic notes |
| `2025_2026/Summer_Semester/JEB010_Makroekonomie_II` | 14 | `JEB010_Makroekonomie_II_main.md` |
| `2025_2026/Summer_Semester/JEB029_Matematika_IV` | 0 | None; no topic notes |
| `2025_2026/Summer_Semester/JEB050_International_Finance` | 13 | `JEB050_International_Finance_main.md` |
| `2025_2026/Summer_Semester/JEB109_Econometrics_I` | 17 | `JEB109_Econometrics_I_main.md` |
| `2025_2026/Summer_Semester/JEB154_Bachelors_Thesis_Seminar_I` | 0 | None; no topic notes |
| `2025_2026/Summer_Semester/JEB160_Auctions_and_Game_Theory` | 1 | `JEB160_Auctions_and_Game_Theory_main.md` |
| `2025_2026/Winter_Semester/JEB009_Makroekonomie_I` | 13 | `JEB009_Makroekonomie_I_main.md` |
| `2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie` | 25 | `JEB027_Finanční_Ekonomie_main.md` |
| `2025_2026/Winter_Semester/JEB033_Matematika_III` | 0 | None; no topic notes |
| `2025_2026/Winter_Semester/JEB044_Financial_Accounting` | 17 | `JEB044_Financial_Accounting_main.md` |
| `2025_2026/Winter_Semester/JEB105_Statistics` | 43 | `JEB105_Statistics_main.md` |
| `2025_2026/Winter_Semester/JEB108_Microeconomics_II` | 19 | `JEB108_Microeconomics_II_main.md` |
| `2025_2026/Winter_Semester/JEB157_Data_Analysis_in_R` | 0 | None; no topic notes |
| `2026_2027/Winter_Semester/Behavioral_Economics` | 0 | None; no topic notes |
| `2026_2027/Winter_Semester/Comparative_Economics` | 0 | None; no topic notes |
| `2026_2027/Winter_Semester/Econometrics_II` | 0 | None; no topic notes |
| `2026_2027/Winter_Semester/Economics_of_Green_Deal` | 0 | None; no topic notes |
| `2026_2027/Winter_Semester/Financial_Markets_Instruments_I` | 0 | None; no topic notes |
| `2026_2027/Winter_Semester/JEM231_Mergers_and_Acquisitions` | 4 | `JEM231_Mergers_and_Acquisitions_main.md` |

## File counts

- `00_Materials`: 298 .pdf, 1 .xlsx
- `01_Notes`: 202 .md, 99 .png
- `02_Resources`: 2 .md

## Relevant facts

- The original teaching skill was subsequently supplied and reviewed on 2026-10-02; see [TEACHING_SKILL_REVIEW.md](TEACHING_SKILL_REVIEW.md). No teaching sessions or per-course learner-state files have been generated.
- Twelve hubs exist: eleven renamed existing hubs and one navigation-only Auctions hub listing available materials.
- Four conceptual note targets remain absent; see [[STANDARDIZATION_REPORT]]. All source-file links and source metadata checked by the audit resolve.
- Same-named investment-theory notes in two courses are intentionally distinct; their links now use explicit paths.
- Unicode diacritics are preserved; treat composed/decomposed Unicode filenames as equivalent during lookup.
- Follow [[NAMING_CONVENTIONS]]; run `python3 03_Agents/check_vault.py` for structural checks.
- Read course sources on demand. Maintenance manifests/backups are not tutoring inputs.
- This snapshot is not a source-freshness baseline for learning; the installed [teach skill](teach/SKILL.md) establishes per-course source manifests when teaching begins.
