# Vault naming conventions

Established 2026-10-02. Apply these conventions to new files and folder changes.

- Course paths: `<root>/<YYYY_YYYY>/<Winter_Semester|Summer_Semester>/<course>/`. Materials, notes, and agent memory use the same course path. `02_Resources` remains shared until course-specific resources actually exist.
- Course folders: `<CODE>_<Course_Name>` when the course code is known; otherwise retain the descriptive course name. Never guess a missing code. Preserve the language, diacritics, acronyms, and mathematical symbols' letter case.
- Course hub: `<course_folder>_main.md`, at the course root. A hub is navigation/content, not evidence that the course was learned. Empty courses do not need placeholder hubs.
- Note filenames: descriptive words separated by single underscores, with existing meaningful capitalization. Preserve conventional `p_Value`, `t_Distribution`, Czech conjunctions and similar intentional case. Shared concept notes follow the same rule, e.g. `Shareholder_Activist.md`.
- Use underscores for spaces; avoid repeated underscores and standalone `_-_` separators. Preserve meaningful hyphens in dates, author names, ranges, and version suffixes. Preserve source titles rather than translating or guessing corrections to academic names.
- Standard collection folders: `Lectures`, `Seminars`, `Textbook`, `Textbook_Chapters`, `Additional_Reading`, and `Week_<number>`. Images stay in the conventional lowercase `assets` folder. A course need not have every collection.
- Keep `.excalidraw.md` and other application-specific extensions intact. Hidden configuration, plugin code, and system filenames retain application conventions.
- Internal links must target existing filenames/paths exactly. Spaces in display labels are fine: `[[Shareholder_Activist|shareholder activist]]`. Use a vault-relative path when a basename is shared by multiple courses. Preserve aliases, heading/block anchors, and escaped pipes in Markdown tables.
- Source metadata and `Source: [[...]]` links use vault-relative paths with file extensions. Update both when files move.
- Course agent records use `learning_plan.md` and `learning_log.md`. Shared maintenance documents may use uppercase names such as `README.md` and `VAULT_MAP.md`; utility scripts use lowercase snake_case.

Run `python3 03_Agents/check_vault.py` from the vault root to check note link targets, source metadata, hub names, and the notes/agent course-folder mirror. The checker reports unresolved content references and exits nonzero until they are resolved; it does not validate course content, PDF internals, or heading/block anchors.
