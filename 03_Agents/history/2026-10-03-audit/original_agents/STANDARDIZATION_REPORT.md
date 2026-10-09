# Standardization report

Completed: 2026-10-02. Scope: vault filenames, directory structure, note navigation/source references, and affected Obsidian workspace paths. Course explanations and source-file contents were preserved.

## Changes

- Renamed 11 existing course hubs to `<course_folder>_main.md` and updated references.
- Aligned materials with notes: `Year_1` → `2024_2025`, `Year_2` → `2025_2026`, `Year_3` → `2026_2027`; added the missing `Winter_Semester` level for Mergers and Acquisitions.
- Standardized Mergers and Acquisitions to `JEM231_Mergers_and_Acquisitions` in all three course trees.
- Standardized separator usage and collection folders (`Seminars`, `Lectures`, `Textbook_Chapters`, `Additional_Reading`); fixed the unambiguous `Texbook_tables.pdf` typo. Preserved original languages, diacritics, meaningful hyphens and version suffixes.
- Renamed the shared concept note to `Shareholder_Activist.md` and repaired its reference and the image link with a space/underscore mismatch.
- Closed 178 malformed source wikilinks and one malformed Bernoulli wikilink. Repaired 12 distinct stale source paths in both links and metadata.
- Corrected mistyped links and references to existing course hubs. Qualified the duplicate `Teorie_Investic` targets by course path. Redirected the standard-normal and isoquant/TRS links to existing coverage, preserving their display labels.
- Created a navigation-only Auctions and Game Theory hub listing existing materials, repairing three references to a previously absent hub. No topic explanations or learning claims were invented.
- Updated obsolete paths in `.obsidian/workspace.json` and refreshed the preparation prompt, README, and vault map.

420 existing file paths changed (mostly because their parent folders moved); 64 existing directory paths changed. The complete mapping is in `standardization_manifest.json`; do not load it during ordinary teaching sessions.

## Verification

- All 623 original files remain present at their mapped paths. All 417 non-Markdown files, including PDFs, images, spreadsheets and system metadata files, passed SHA-256 comparison.
- Checked 1911 nonempty wikilink targets in course notes: no ambiguous links, malformed source lines, missing source metadata targets, legacy hub names, or course-directory mirror mismatches remain.
- Four links still point to absent conceptual notes, listed below. These are content gaps, not resolvable naming errors.
- The read-only checker is `python3 03_Agents/check_vault.py`. It intentionally exits nonzero for the four remaining missing notes. Heading/block anchors, PDF-internal links, compressed Excalidraw data, and academic correctness are outside its checks.

## Remaining content gaps

| Missing note | Referring note |
|---|---|
| `Descriptive_Statistics_Overview` | [[01_Notes/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Data_Types_and_Variables|Data_Types_and_Variables]] (line 10) |
| `Bernoulli_Distribution` | [[01_Notes/2025_2026/Winter_Semester/JEB105_Statistics/Lectures/Binomial_Distribution|Binomial_Distribution]] (line 11) |
| `Kolmogorov_Smirnov_Test` | [[01_Notes/2025_2026/Winter_Semester/JEB105_Statistics/Lectures/Cumulative_Distribution_Function|Cumulative_Distribution_Function]] (line 81) |
| `Standard_Error` | [[01_Notes/2025_2026/Winter_Semester/JEB105_Statistics/Lectures/Variance|Variance]] (line 11) |

No placeholder content was created for these concepts. Five empty current-year course folders have no supplied course code; their descriptive names were retained. Courses without notes remain without fabricated hubs or learning plans.

## Rollback records

- Durable archive: `03_Agents/.backups/2026-10-02_standardization.zip`. It contains original text/config files, original hashes, and the full original-to-new path mapping. Archive integrity was checked.
- `03_Agents/standardization_manifest.json` records path changes, source-path repairs and the added hub.
- Binary files were moved without content edits, so the path mapping is sufficient to move them back. Text/config originals are in the archive. Restore only after accounting for subsequent user edits; do not overwrite later work blindly.

For future additions, follow [[NAMING_CONVENTIONS]].
