# HTML course utility

`course.py` uses Python 3.9+ and the standard library. Its skill folder supplies the approved theme, bundled fonts and KaTeX. Runtime output opens without Python, Node, installation or a server.

| Command | Result |
|---|---|
| `snapshot --vault ROOT --course ID --objectives O001 O002 --out SNAPSHOT` | Verifies committed readiness and captures ready lessons plus selected checked note sections. Prerequisites are included automatically. Repeat `--asset VAULT_RELATIVE_PATH` for required note figures. |
| `build --vault ROOT --snapshot SNAPSHOT --draft DRAFT --candidate NEW_DIRECTORY` | Checks freshness and coverage, renders a new isolated candidate and creates its exact-byte manifest. Never overwrites an existing candidate. |
| `check --candidate DIRECTORY` | Verifies candidate/version hashes, unique HTML IDs, local assets and link/anchor targets. Does not certify academic coverage or browser behavior. |
| `publish --vault ROOT --candidate DIRECTORY --review REPORT --qa REPORT` | Rechecks sources and final reviews, preserves prior versions and atomically updates the default course contents page. |

`publish --output DEDICATED_DIRECTORY` selects another empty or positively owned export root. `--allow-scope-reduction` is for an explicitly requested narrower live scope, not ordinary refresh. Earlier versions stay intact. Omission of a previously exported objective otherwise blocks publication unless the current plan retires it.

## Draft format

`../templates/course.json` is a format example, not ready material. Replace its sample content with complete supported explanations and set the actual snapshot fingerprint. JSON strings contain normal HTML and escaped LaTeX backslashes. Use `\(...\)` and `\[...\]` for math, converting source dollar delimiters; literal currency dollars are plain text. Course title, scope and week/lesson labels are plain text; section and interaction content are HTML. Convert Markdown/Obsidian links to local HTML links. Do not paste raw source instructions or metadata as executable code.

Every snapshot `source_units[].key` needs exactly one coverage entry. `included` maps to one or more existing `lesson-id#section-id` anchors. `operational_only` needs a reason and is restricted to the narrow tutor-routing, record-metadata and navigation headings recognized by the utility. A complete map is a review aid, not a semantic coverage certificate.

Lesson objects have stable `id`, `title`, `week`, `objective_ids`, `prerequisite_lessons` and `sections`. A section has `id`, `title`, `html` and optional `interactions`. Use `additional_weeks` for cross-week synthesis. Weeks are checked against selected note paths; material without week paths needs an explicit `week_basis` recording the user/plan basis. Do not infer a week from page order.

## Student presentation profile

Set `student_profile: 1` for new or refreshed student courses and follow [the presentation contract](../references/student_presentation.md). The helper adds the bundled student CSS/runtime, sidebar lesson dropdowns, section links and local quiz controls. The outline must be first; `introduction`, `definitions`, `practice` and `sources` are required section IDs. Give numbered subsection headings stable IDs. Draft metadata may retain original policies/provenance; sections marked for agent audiences are rejected rather than silently exposed. Keep old anchor aliases when refreshing.

A student quiz uses four distinct visible HTML choices, one strict integer `correct_index` from0 through3, and `feedback`: a list of four nonempty choice-specific explanations. Interaction IDs must be unique throughout a lesson. The complete local key supports empty/wrong/correct states, check-all, answer changes and reset without a network connection. Author the topic-specific content; the runtime supplies no academic answers.

## Interaction objects

All interactions have a unique `id`, `kind`, `prompt_html` and `solution_html`.

| Kind | Additional fields |
|---|---|
| `numeric` | Finite `answer`, nonnegative absolute `tolerance` (default 0.000001). |
| `choice` | `choices`: at least two HTML strings; `correct_index`: zero-based index. Balance answer cues without distorting content. |
| `reflection` | No extra fields. Browser-local draft and model explanation; no automatic grading of prose. |
| `residual-plot` | `points`: finite xy pairs; fixed `intercept`; initial `slope`; slider `minimum`, `maximum`, positive `step`. Shows a candidate line and squared residuals. The solution explains what varying only the slope establishes. |

For a needed custom component, declare a draft asset and add its target to `custom_scripts`. Scripts load after the built-in runtime, use DOM hooks from section HTML, and must not fetch dependencies or communicate externally. Review their code, equations and UI states. Do not modify the installed skill while generating a course.

An asset has `origin` (`vault` or `draft`), `path`, `target` and actual byte `sha256`. A vault asset must be one of the snapshot's selected assets. A custom draft asset lives under `assets/` beside the draft JSON. Targets use `assets/figures/` or `assets/custom/`. In lesson HTML, reference `../assets/figures/...`; lesson links are `other-lesson-id.html#section-id`.

## Final reports

Reports live outside the candidate so adding evidence does not change the reviewed digest. The reviewing agent supplies the academic report from its actual inspection. Do not generate a passed report as a test substitute in real publication.

```json
{
  "kind": "academic",
  "status": "passed",
  "reviewer": "ACTUAL_INDEPENDENT_REVIEWER",
  "candidate_digest": "THE_REVIEWED_CANDIDATE_DIGEST",
  "objective_ids": ["O001"],
  "evidence": "Path to the actual full-scope comparison and final confirmation",
  "findings": []
}
```

The browser report uses `kind: browser`, its actual tester in `reviewer`, the same `candidate_digest`, nonempty `evidence`, `status: passed`, `findings: []`, and:

```json
{"checks":{"links":true,"math":true,"interactions":true,"desktop":true,"compact":true,"offline_dependencies":true}}
```

The helper checks report identity/scope/digests, not whether a human or agent actually performed the review. Honest dispatch, source comparison and browser evidence remain mandatory skill work.

## Recovery and preservation

The root contents page is the single atomic activation pointer. Complete immutable versions contain their draft, snapshot, pages, asset hashes and reports. A complete version copied before interrupted activation can be verified and reused by an identical publish retry. An incomplete `.stage-*` or held lock is preserved for explicit inspection, not discarded. Inspect its actual bytes, recorded process/host and current root pointer before a recovery decision. Unknown edits stop publication. Browser drafts use course, lesson and content-revision keys; older answers are not silently applied to changed content.
