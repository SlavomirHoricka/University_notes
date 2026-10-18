# Econometrics II — source manifest

```json
{
  "schema_version": 3,
  "owner": "plan",
  "course_id": "2026_2027/Winter_Semester/Econometrics_II",
  "transaction_id": "PLAN-20261009-ECOX-P003",
  "plan_version": "P003",
  "source_version": "V002",
  "ingestion_revision": 2,
  "record_revision": 3,
  "updated_at": "2026-10-10T16:14:02.779842+02:00",
  "timezone": "Europe/Prague",
  "ingestion_pass_refs": [
    "03_Agents/runtime/ingest/logs/20261004T155737+0200_week1_courses.md",
    "03_Agents/runtime/ingest/logs/20261007T122546+0200_week2_courses.md"
  ],
  "entries": [
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main.md",
      "sha256": "9bed2fe6a28235bcccef6683df834109cb77698530564995111d6d3c498f4898",
      "bytes": 15322,
      "note_sections": [
        "Econometrics II",
        "Week 1",
        "The sample calculation and the population question",
        "Three properties, three questions",
        "From a fare question to an empirical report",
        "Preparation and unresolved source details",
        "Week 2",
        "Ordered observations change the assumptions",
        "Describe the timing of a modeled response",
        "Compare deviations from trend and calendar patterns",
        "Reading identity and scope"
      ],
      "objective_ids": [
        "O001",
        "O002",
        "O003",
        "O004",
        "O005",
        "O006",
        "O007",
        "O008",
        "O009",
        "O010",
        "O011",
        "O012",
        "O013"
      ],
      "semantic_baseline": "Week 1 synthesis; OLS sample calculation is distinct from population properties; three estimator questions; empirical report with undocumented CSV scale/provenance; preparation/admin limits. Additive Week2 hub, inspected without changes to prior Week1 academic mechanisms.",
      "change_class": "new_content",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main.md",
      "previous_hash": "63370004b1f1b1101bf8c62976af9f3e3ebbbda9cd959c83e80c2c7bec1eb387",
      "affected_objective_ids": [
        "O001",
        "O009",
        "O010",
        "O011",
        "O012",
        "O013"
      ],
      "inspection_status": "read_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Course_Organization_and_Source_Discrepancies.md",
      "sha256": "d865f97f1915a5acc993b0e7765ad1e7018c7c12b7aacc5ec2b44cc6c1b2af21",
      "bytes": 9746,
      "note_sections": [
        "Course organization and source discrepancies",
        "Course purpose and preparation",
        "Assessment and submitted work",
        "Conflicting administrative details",
        "Boundary of this Week 1 ingestion"
      ],
      "objective_ids": [
        "O001"
      ],
      "semantic_baseline": "JEB110,6 ECTS, JEB109 prerequisite;40/20/40, separate final>20; R seminars and R appendix/pairing/software wording; HA1 Oct 19/26, fractional grade thresholds, Sept 31 and midterm end unresolved; later academic methods and Chapter 10 not ingested. The source’s Week1-only boundary is historical; P003 separately includes checked Week2. O001 reconciles that current scope distinction without resolving administrative conflicts.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Course_Organization_and_Source_Discrepancies.md",
      "previous_hash": "d865f97f1915a5acc993b0e7765ad1e7018c7c12b7aacc5ec2b44cc6c1b2af21",
      "affected_objective_ids": [
        "O001"
      ],
      "inspection_status": "read_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions.md",
      "sha256": "8e76f95b0071e8625c31230e9c96e2a738e7d88251b1ba978d0bc35225fc380a",
      "bytes": 9146,
      "note_sections": [
        "OLS estimator and assumptions",
        "Population model, sample, and notation",
        "How OLS chooses the line",
        "The assumption ladder",
        "Why multiple regression uses matrix notation",
        "What to carry forward"
      ],
      "objective_ids": [
        "O002",
        "O003",
        "O004",
        "O005",
        "O006",
        "O007",
        "O008"
      ],
      "semantic_baseline": "Linear model, hats/disturbance versus residual; normal equations/centered OLS; Sxx>0; units/intercept support; residual orthogonality is not population exogeneity; six named assumptions; X dimensions/full rank/joint conditional comparison.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions.md",
      "previous_hash": "8e76f95b0071e8625c31230e9c96e2a738e7d88251b1ba978d0bc35225fc380a",
      "affected_objective_ids": [],
      "inspection_status": "read_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Transport_Demand_Regression_Seminar.md",
      "sha256": "8cb7c6b76f548352c216ae9bd1d909a788d8d8f5b8718c2721d23989ce332d7f",
      "bytes": 22651,
      "note_sections": [
        "Transport demand: regression and interpretation",
        "From economic intuition to a model",
        "Ten-city example: keep the source's measurement scale",
        "Estimate the line",
        "Fitted values and residuals",
        "Disturbance variance, slope variance, and the t statistic",
        "The CSV example: compare specifications",
        "Interpret conditional associations carefully",
        "Goodness of fit: R-squared and adjusted R-squared",
        "Assumption checks: what diagnostics can establish",
        "Normality: a plot and a moment test",
        "Homoskedasticity: a spread plot and an auxiliary regression",
        "Assumptions that remain substantive",
        "Turn the analysis into a short report"
      ],
      "objective_ids": [
        "O006",
        "O007",
        "O008"
      ],
      "semantic_baseline": "Literal thousand-passengers/hour and dollar table scale; ten-city centered summaries/slope/intercept/SSE, se, t 8 nonrejection; negative predictions/domain limits; CSV1000 rows, unknown units/sampling/DGP/u; three same-sample conditional models/conventional se; fit/adjustedfit nesting and df; JB/moments df2 and studentizedBP/Koenker squared-residual auxiliary LM df3 asymptotic tests; nonrejection not proof; bounded report/no optimal fare.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Transport_Demand_Regression_Seminar.md",
      "previous_hash": "8cb7c6b76f548352c216ae9bd1d909a788d8d8f5b8718c2721d23989ce332d7f",
      "affected_objective_ids": [],
      "inspection_status": "read_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency.md",
      "sha256": "afc4f90940a6f9e889acff6e5e1194c5fde424636cbfca31f540eee2c5051595",
      "bytes": 12594,
      "note_sections": [
        "Unbiasedness, consistency, and efficiency",
        "One decomposition drives both proofs",
        "Unbiasedness: the repeated-sample average",
        "Consistency: concentration as sample size grows",
        "Why population covariance determines the probability limit",
        "A weaker exogeneity condition",
        "How unbiasedness and consistency can differ",
        "Efficiency: specify the comparison class",
        "Normality and hypothesis tests add another requirement",
        "Distinctions to retain"
      ],
      "objective_ids": [
        "O003",
        "O004",
        "O005"
      ],
      "semantic_baseline": "Centered disturbance decomposition; fixed-X expectation plus first 4->unbiased; LLN covariance/variance limit with finite moments and positive finite variance; weaker E[u]/orthogonality including intercept; Chebyshev/dispersion distinction; first 5 BLUE conditional linear-unbiased class; sigma²/Sxx; first 6 exact classical null t/F and df.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency.md",
      "previous_hash": "afc4f90940a6f9e889acff6e5e1194c5fde424636cbfca31f540eee2c5051595",
      "affected_objective_ids": [],
      "inspection_status": "read_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p19_unbiasedness_derivation.png",
      "sha256": "99d9726164d7430cb4aa0f281a8cc2ce61f43ee3291e68e4a1fee7b3575ca6b2",
      "bytes": 86809,
      "note_sections": [],
      "objective_ids": [
        "O003"
      ],
      "semantic_baseline": "Fixed-X conditional expectation weights/denominator outside expectation; zero conditional disturbance means finish unbiasedness proof.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p19_unbiasedness_derivation.png",
      "previous_hash": "99d9726164d7430cb4aa0f281a8cc2ce61f43ee3291e68e4a1fee7b3575ca6b2",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p22_consistency_derivation.png",
      "sha256": "9bc5e56e3aaf74446e8ee0d0a805d26a178f2c111c23670cce37525db0e09604",
      "bytes": 74408,
      "note_sections": [],
      "objective_ids": [
        "O004"
      ],
      "semantic_baseline": "Centered disturbance ratio divided by n exposes population covariance/variance probability limit; regularity supplied by finished note.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p22_consistency_derivation.png",
      "previous_hash": "9bc5e56e3aaf74446e8ee0d0a805d26a178f2c111c23670cce37525db0e09604",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/seminar1_p1_ten_city_table.png",
      "sha256": "01a26a2528905cc8cf66926795d307bea50e587c9f255f8cb226b9875bd8725a",
      "bytes": 22480,
      "note_sections": [],
      "objective_ids": [
        "O006"
      ],
      "semantic_baseline": "Ten source city values/labels; literal units passengers/hour(thousand), fare dollars,0.50–1.50 fare range.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/seminar1_p1_ten_city_table.png",
      "previous_hash": "01a26a2528905cc8cf66926795d307bea50e587c9f255f8cb226b9875bd8725a",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/travel_full_model_diagnostics.png",
      "sha256": "783b15f68323991d9c54abfb0b83fa32a2858725f17ece2dd0ed18d30c535500",
      "bytes": 81367,
      "note_sections": [],
      "objective_ids": [
        "O008",
        "O007"
      ],
      "semantic_baseline": "Finished-note computed model3 residual histogram/Q–Q/spread/squaredspread; near-diagonal/tail departures, no conspicuous funnel; visual evidence limited, not proof of population assumptions.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/travel_full_model_diagnostics.png",
      "previous_hash": "783b15f68323991d9c54abfb0b83fa32a2858725f17ece2dd0ed18d30c535500",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_and_checked_against_completed_ingestion"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Static_and_Finite_Distributed_Lag_Models.md",
      "sha256": "9e8cb8c0eeff46c0f43ff601c85d5abac60a13edb674569501974f4f61867849",
      "bytes": 16551,
      "note_sections": [
        "Static and finite distributed lag models",
        "A static contemporaneous model",
        "An FDL model spreads adjustment across dates",
        "A temporary pulse and a permanent step",
        "A static model is a special case, with a source caveat",
        "Precision of the long-run sum",
        "The EET restaurant-price example",
        "A visual motivation for lagged response",
        "What to retain"
      ],
      "objective_ids": [
        "O011"
      ],
      "semantic_baseline": "Orderq has current value plusq lags. Pulse responseδ_h for h0..q then zero; step partial sums then LRP=sumδ, holding other inputs/disturbances fixed. Static retainsδ0 despite deck zero-list error; absent prehistory dropsq rows. Lag correlation affects precision, not automatic bias. Variance of sum needs covariances; θ reparameterises q2 with lag-minus-current columns. EET data/coding/causal design absent and legal dates unverified; index points are not percentages/currency. Cases/hospital visual has distinct units and testing limits, not an estimated lag.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O011"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Time_Series_OLS_and_Strict_Exogeneity.md",
      "sha256": "b15a3499dc1e95b326b898a39f5d58f9d72de24432544877ddd9d5a586775e4b",
      "bytes": 17583,
      "note_sections": [
        "Time-series OLS and strict exogeneity",
        "Temporal ordering and a stochastic process",
        "The first three assumptions",
        "Strict versus contemporaneous exogeneity",
        "Why strict exogeneity gives unbiasedness",
        "Two additional assumptions for conventional variance",
        "The covariance terms hidden in the simple-slope proof",
        "Multiple-regression precision, residual variance, and BLUE",
        "Normality and exact finite-sample inference",
        "What the assumption ladder establishes"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Ordered sample is one realisation of a stochastic process, not independent sampling. X has T×(k+1) shape and full rank. Strict E[u_t|wholeX]=0 includes future/past, yielding conditional OLS unbiasedness; contemporaneous mean condition alone fails under feedback. Deck/book TS2/TS3 names are swapped. Ω=σ²I needs equal diagonals and zero off-diagonals; AΩA′ yields variance, SSR/(T−k−1), auxiliaryR² precision and conditional linear-unbiased BLUE. Independent-X iid normal errors support exact null t/F but cannot establish rank. Failing strict exogeneity removes a guarantee, not proof of universal bias/inconsistency; Chapter11 context is bounded.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O009",
        "O010"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Trends_Detrending_and_Seasonality.md",
      "sha256": "0e7fb5c1af7cabc4ea80572915d3578a657db087254f5d6e70a4f870eabc185f",
      "bytes": 18331,
      "note_sections": [
        "Trends, detrending, and seasonality",
        "What the source's three trend plots show",
        "Choose a time form that matches the comparison",
        "Shared trends as an omitted-variable problem",
        "Include an appropriate time trend",
        "Detrend every variable using the same time form",
        "Why the slope agrees with including the trend",
        "Seasonality is a repeating calendar pattern",
        "What the adjustments establish"
      ],
      "objective_ids": [
        "O012",
        "O013"
      ],
      "semantic_baseline": "Level, log and quadratic deterministic trends differ. Omittedγt may violate zero conditional mean with trendingx. Residualise every y/x on identical controls/rows: orthogonality yields sum x_tilde y_tilde/sum x_tilde² when positive, equal to full-controls OLS slope but not proof of exogeneity. DetrendedR² uses residual-y variation (zero means undefined), versus originalTSS; retain full-modeldf and usual restricted/fullR² forF. Withm calendar positions use intercept+m−1 indicators and stable additive reference differences; identical joint trend/seasonal controls support partialling out. Adjustment is not every agency algorithm or a universal persistence/causality remedy.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012",
        "O013"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p17_error_covariance_matrix.png",
      "sha256": "bec15fb9cf2d5b6277b9245c9fe39d19f0d400eaa474e796853344ed925ec64a",
      "bytes": 42368,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Conditional disturbance covariance matrix: equal sigma² diagonal entries and zero off-diagonal covariances. It is not an assertion that regressors are serially independent.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O009",
        "O010"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p32_GDP_against_productivity.png",
      "sha256": "c724a0e3a321feb16a2008fa301690256a95f99ec4415f02d92cacb10fc62e09",
      "bytes": 62768,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012",
        "O013"
      ],
      "semantic_baseline": "Raw positive GDP/productivity association in connected level observations. Axis units and country/sample provenance are absent; no numerical or causal slope inferred.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012",
        "O013"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p33_GDP_over_time.png",
      "sha256": "491b84e5b857dfac7820dc2d482724adfd29c5e975a350e218d2d55383365e90",
      "bytes": 61421,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012",
        "O013"
      ],
      "semantic_baseline": "GDP generally rises over plotted years with late-2000s pause/decline; qualitative trend motivation only, missing source units/dataset identity.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012",
        "O013"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p34_productivity_over_time.png",
      "sha256": "063cd73b7558f951801739eb18e9a59073930050b3336c1a939c4305f19d387c",
      "bytes": 61892,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012",
        "O013"
      ],
      "semantic_baseline": "Productivity generally rises over plotted years. Together with GDP trends it motivates conditional comparison, not proof that all raw association is spurious or a supplied detrended estimate.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012",
        "O013"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p35_cases_and_hospital_patients.png",
      "sha256": "2ed7f9a90d36094f9f134e2c57ffb4919061b8f71898cf71e9b47bdd7a2f01a7",
      "bytes": 85123,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O011"
      ],
      "semantic_baseline": "Confirmed daily cases per million versus hospital-patient occupancy count in Czechia, early2022; distinct units, limited-testing undercount and source credits retained. Visual timing is not an estimated lag/causal effect.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O011"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/textbook_ch10_printed347_lag_distribution.png",
      "sha256": "27edbf71873e191bde657f77d0eabf0b6874a862739e1669f952984ec04ef339",
      "bytes": 42610,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O011"
      ],
      "semantic_baseline": "Schematic coefficient-by-lag distribution: highest at lag1, nonzero through lag2 then zero. It supplies no numerical fitted coefficients or outcome series.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O011"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    }
  ],
  "ingestion_transaction_id": "INGEST-ECONOMETRICS_II-6532655daa5c4322a07b8d4e6e26e8e0"
}
```

## Completion provenance and semantic reconciliation

P003 fingerprints all selected finished Week1/Week2 notes and their required assets at completed ingestion revision2. The linked current run documents independent source checks and bounded exclusions. SHA-256 measures bytes; change classes follow finished-note inspection. Week1 academic notes/assets remain unchanged. Hub additions and new Week2 inputs are new_content, affecting new O009–O013 and the current-scope reconciliation in O001; O001’s current-scope criterion changes to O001-C2, while all other old criteria/conditions remain unchanged. Each entry records actual headings, prior hash/path, claim/assumption digest and objective mapping. Access was stable and no selected input was deleted or moved.

| Finished input | Hash / bytes | Objectives / change |
|---|---|---|
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main.md]] | `9bed2fe6a28235bcccef6683df834109cb77698530564995111d6d3c498f4898` / 15322 | O001, O002, O003, O004, O005, O006, O007, O008, O009, O010, O011, O012, O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Course_Organization_and_Source_Discrepancies.md]] | `d865f97f1915a5acc993b0e7765ad1e7018c7c12b7aacc5ec2b44cc6c1b2af21` / 9746 | O001 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions.md]] | `8e76f95b0071e8625c31230e9c96e2a738e7d88251b1ba978d0bc35225fc380a` / 9146 | O002, O003, O004, O005, O006, O007, O008 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Transport_Demand_Regression_Seminar.md]] | `8cb7c6b76f548352c216ae9bd1d909a788d8d8f5b8718c2721d23989ce332d7f` / 22651 | O006, O007, O008 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency.md]] | `afc4f90940a6f9e889acff6e5e1194c5fde424636cbfca31f540eee2c5051595` / 12594 | O003, O004, O005 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p19_unbiasedness_derivation.png]] | `99d9726164d7430cb4aa0f281a8cc2ce61f43ee3291e68e4a1fee7b3575ca6b2` / 86809 | O003 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p22_consistency_derivation.png]] | `9bc5e56e3aaf74446e8ee0d0a805d26a178f2c111c23670cce37525db0e09604` / 74408 | O004 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/seminar1_p1_ten_city_table.png]] | `01a26a2528905cc8cf66926795d307bea50e587c9f255f8cb226b9875bd8725a` / 22480 | O006 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/travel_full_model_diagnostics.png]] | `783b15f68323991d9c54abfb0b83fa32a2858725f17ece2dd0ed18d30c535500` / 81367 | O008, O007 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Static_and_Finite_Distributed_Lag_Models.md]] | `9e8cb8c0eeff46c0f43ff601c85d5abac60a13edb674569501974f4f61867849` / 16551 | O011 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Time_Series_OLS_and_Strict_Exogeneity.md]] | `b15a3499dc1e95b326b898a39f5d58f9d72de24432544877ddd9d5a586775e4b` / 17583 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Trends_Detrending_and_Seasonality.md]] | `0e7fb5c1af7cabc4ea80572915d3578a657db087254f5d6e70a4f870eabc185f` / 18331 | O012, O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p17_error_covariance_matrix.png]] | `bec15fb9cf2d5b6277b9245c9fe39d19f0d400eaa474e796853344ed925ec64a` / 42368 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p32_GDP_against_productivity.png]] | `c724a0e3a321feb16a2008fa301690256a95f99ec4415f02d92cacb10fc62e09` / 62768 | O012, O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p33_GDP_over_time.png]] | `491b84e5b857dfac7820dc2d482724adfd29c5e975a350e218d2d55383365e90` / 61421 | O012, O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p34_productivity_over_time.png]] | `063cd73b7558f951801739eb18e9a59073930050b3336c1a939c4305f19d387c` / 61892 | O012, O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p35_cases_and_hospital_patients.png]] | `2ed7f9a90d36094f9f134e2c57ffb4919061b8f71898cf71e9b47bdd7a2f01a7` / 85123 | O011 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/textbook_ch10_printed347_lag_distribution.png]] | `27edbf71873e191bde657f77d0eabf0b6874a862739e1669f952984ec04ef339` / 42610 | O011 / new_content |

## Preserved history and verification

The exact replaced P002 bundle is preserved under curriculum_history/P002; existing P001 history is untouched. Current tuple: PLAN-20261009-ECOX-P003 / P003 / V002 / ingestion2. The active ingest transaction is INGEST-ECONOMETRICS_II-6532655daa5c4322a07b8d4e6e26e8e0. Active bytes must match their committed owner journal. Subsequent outside-workflow note changes need explicit freshness reconciliation; no watcher is introduced.

## Uncovered material and assumptions

Overall semester coverage remains partial: a complete Chapter11/asymptotic curriculum, missing board work/video, EET data/coding/causal design and current legal dates are outside the checked scope. Week1 course organizational ambiguities remain context. Supported finite-sample assumptions, FDL responses/precision and deterministic trend/seasonal comparisons are executable; their conditions do not automatically hold in data. No unsupported policy estimate or universal detrending guarantee is introduced. No raw sources were read or hashed by planning. No learner evidence or scheduling records were created.
