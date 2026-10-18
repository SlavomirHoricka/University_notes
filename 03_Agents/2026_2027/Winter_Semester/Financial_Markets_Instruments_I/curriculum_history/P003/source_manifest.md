# Financial Markets Instruments I — source manifest

```json
{
  "schema_version": 3,
  "owner": "plan",
  "course_id": "2026_2027/Winter_Semester/Financial_Markets_Instruments_I",
  "transaction_id": "PLAN-20261009-FMI-P003",
  "plan_version": "P003",
  "source_version": "V002",
  "ingestion_revision": 2,
  "record_revision": 3,
  "updated_at": "2026-10-10T16:09:27.157425+02:00",
  "timezone": "Europe/Prague",
  "ingestion_pass_refs": [
    "03_Agents/runtime/ingest/logs/20261004T155737+0200_week1_courses.md",
    "03_Agents/runtime/ingest/logs/20261007T122546+0200_week2_courses.md"
  ],
  "ingestion_transaction_id": "INGEST-FINANCIAL_MARKETS_INSTRUMENTS_I-ccde853ce42a4bd9a56bb46e241f3338",
  "entries": [
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md",
      "sha256": "12acb3a4ec118be8accf95e57e840efa6bcb31a40d1d9fd85f79b019312a7658",
      "bytes": 18726,
      "note_sections": [
        "Financial Markets Instruments I",
        "Week 1",
        "Source selection for this week",
        "Week 2",
        "Week 2 source scope and limitations",
        "Course organization",
        "Teaching and communication",
        "Assessment and the handbook's cutoff ambiguity",
        "Listed examination dates and materials"
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
      "semantic_baseline": "Course JEM035/English/6ECTS, futures/options syllabus context not complete content; selected Week1 boundary.20 seminar/80 exam,minimum40/80 eligibility,exactly50total conflict retained;theory40+four10 exercises and step explanation. Source-listed changeable dates and rooms not live verified or learner deadline;formula list/nonprogrammable calculator context;external books not ingested. Additive Week2 hub, inspected without changes to prior Week1 academic mechanisms.",
      "change_class": "new_content",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md",
      "previous_hash": "199e68a304dd3a158c826e740555949393de86d877afda43db602a7b9aaf5133",
      "affected_objective_ids": [
        "O009",
        "O010",
        "O011",
        "O012",
        "O013"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Basis_Convergence_and_Futures_Hedging.md",
      "sha256": "b3e4487925e9bd1ca9c2c341990863be4d2ff9f9a1e8e2211e1742e1bc4e5956",
      "bytes": 12935,
      "note_sections": [
        "Basis, convergence and futures hedging",
        "Basis and calendar spread are different comparisons",
        "Why the prices converge at delivery",
        "A purchase hedge, derived step by step",
        "A sale hedge and early termination",
        "The lecture's value convention",
        "What to carry forward"
      ],
      "objective_ids": [
        "O006",
        "O007",
        "O008"
      ],
      "semantic_baseline": "B=S−F, D=earlyF−lateF; course contango/backwardation and lecture normal orderings. Two delivery arbitrage directions conditional on eligibility/execution and ignored costs; EDSP defined not universal; endpoint not monotonic. Buyer E=X(F0+B),CF=−E,sellerR=X(F0+B);early basis risk/zero-basis lock only matching; source sign-label error. Lecture V_long=X(Ft−F0)/(1+rΔt),short opposite, assumed deferred payment not daily-account valuation.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Basis_Convergence_and_Futures_Hedging.md",
      "previous_hash": "b3e4487925e9bd1ca9c2c341990863be4d2ff9f9a1e8e2211e1742e1bc4e5956",
      "affected_objective_ids": [],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Introduction_to_Futures_Seminar_Exercises.md",
      "sha256": "b10a0ed1ddfde242583a447a4246738dc8f31af4dca1c5f77970596782335d04",
      "bytes": 13216,
      "note_sections": [
        "Introduction to futures — seminar exercises",
        "Problem 1: offsetting contracts",
        "Problem 2: a short wheat contract",
        "Problem 3: copper and maximum loss",
        "Problem 4: a daily margin table",
        "Problem 5: clearing a larger long position",
        "Problem 6: two orange-juice contracts",
        "The seminar's film illustration",
        "What to carry forward"
      ],
      "objective_ids": [
        "O001",
        "O002",
        "O003",
        "O004",
        "O005"
      ],
      "semantic_baseline": "All six conditional solutions: equivalent offsets; wheat short call>2.70 and W1500 retainI <=2.20/retainM<=2.40; copper long max19500 only nonnegative;20-contract table final120 deposits180 loss60 underR100;85+15 cohort net31250,new margin30000,EOD extra0/temporary30000;orange long call<1.50 andW2000 retainI>=1.666666…/M>=1.566666…;short film gain508500 without account/legal content.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Introduction_to_Futures_Seminar_Exercises.md",
      "previous_hash": "b10a0ed1ddfde242583a447a4246738dc8f31af4dca1c5f77970596782335d04",
      "affected_objective_ids": [],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Margins_and_Marking_to_Market.md",
      "sha256": "c92b574f4c33c97bdbefad673c63cc8029a344a79d7b1da69ed2bba44076e313",
      "bytes": 12176,
      "note_sections": [
        "Margins and marking to market",
        "The three margin concepts",
        "Daily profit and loss, with units",
        "From daily result to an account balance",
        "The handout's five-day example",
        "Payoff and the size of possible losses",
        "What to carry forward"
      ],
      "objective_ids": [
        "O002",
        "O003",
        "O004",
        "O005",
        "O007",
        "O008"
      ],
      "semantic_baseline": "G_long=Nq delta F, short opposite; fixed-position telescope; I deposit,M minimum,R explicit target; A^- previous+G, C=R−A^- only belowM, A=A^-+C−W. Variation margin terminology differs. Balance+withdrawals−deposits=P/L. Source five-day opposite tables; linear payoff at matching maturity; finite long max requires F>=0, short unbounded without upper bound.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Margins_and_Marking_to_Market.md",
      "previous_hash": "c92b574f4c33c97bdbefad673c63cc8029a344a79d7b1da69ed2bba44076e313",
      "affected_objective_ids": [],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Spot_Forward_and_Futures_Contracts.md",
      "sha256": "ed4177199ebe557e2c52129bcd94b690b22e553a5eafba9ce5f4dc19656c3045",
      "bytes": 18244,
      "note_sections": [
        "Spot, forward and futures contracts",
        "Topic map",
        "When the agreement, payment and delivery happen",
        "Standardized futures specifications",
        "Positions, open interest and the clearing house",
        "How the obligation ends",
        "Trading limits and market abuse",
        "What to carry forward"
      ],
      "objective_ids": [
        "O001",
        "O002"
      ],
      "semantic_baseline": "Spot/future spot/forward timing; standardized underlying/grade/location/month/size; tick=multiplier×tick size; fractional quotation division by32 and label inconsistency; long/short/OI; clearing with own-broker warning and unresolved contrary wording; identical offset; physical/cash EDSP; daily/position limits and cornering. Introductory months/maturities/percentages are attributed rather than universal rules.",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Spot_Forward_and_Futures_Contracts.md",
      "previous_hash": "ed4177199ebe557e2c52129bcd94b690b22e553a5eafba9ce5f4dc19656c3045",
      "affected_objective_ids": [],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Long_Short_Payoffs.png",
      "sha256": "0031c88b703a27700f6bfb39b64c4c8b9b64abfe97f1aa4d2e6e1fb62f96c7be",
      "bytes": 15695,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O002"
      ],
      "semantic_baseline": "opposite linear P/L slopes and break-even F0; axis not account balance",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Long_Short_Payoffs.png",
      "previous_hash": "0031c88b703a27700f6bfb39b64c4c8b9b64abfe97f1aa4d2e6e1fb62f96c7be",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Margin_Table.png",
      "sha256": "791b5a8ad0c57b141534941e4d758d4d07b5999c6d66d55ad2b0502dba061e11",
      "bytes": 71163,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O003",
        "O007"
      ],
      "semantic_baseline": "five-day opposite normalized daily transfers/calls/balances,finallong−100/short+100",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Margin_Table.png",
      "previous_hash": "791b5a8ad0c57b141534941e4d758d4d07b5999c6d66d55ad2b0502dba061e11",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Clearing_Arrangement.png",
      "sha256": "7e782a762b3ab6cb0f8270aaa82f495a4e1ba7bfcebc0d5e2b94c5e867adc8c9",
      "bytes": 563220,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O001"
      ],
      "semantic_baseline": "interposed clearing and explicit own-broker warning",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Clearing_Arrangement.png",
      "previous_hash": "7e782a762b3ab6cb0f8270aaa82f495a4e1ba7bfcebc0d5e2b94c5e867adc8c9",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Convergence_Patterns.png",
      "sha256": "a582e9824ebc65437ce015f53e559e4c7dd6c2d238cb527111c38f3a73a3d05c",
      "bytes": 138212,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O006",
        "O007"
      ],
      "semantic_baseline": "each futures endpoint meets spot at own delivery; curved paths not monotonic prediction",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Convergence_Patterns.png",
      "previous_hash": "a582e9824ebc65437ce015f53e559e4c7dd6c2d238cb527111c38f3a73a3d05c",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Forward_Timeline.png",
      "sha256": "caaeedc9f48c35dcfb8971aa6383f583e26345893f42e6acc88e15c98b6be011",
      "bytes": 63778,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O001"
      ],
      "semantic_baseline": "specification now,payment/delivery later",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Forward_Timeline.png",
      "previous_hash": "caaeedc9f48c35dcfb8971aa6383f583e26345893f42e6acc88e15c98b6be011",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Spot_Timelines.png",
      "sha256": "746d6df8f88c67a407ffcb14e9401dc8ce66e2b1d6f33d94d6d7976565b360f4",
      "bytes": 551194,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O001"
      ],
      "semantic_baseline": "S/P/D current versus all delayed; intention does not fix future price",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Spot_Timelines.png",
      "previous_hash": "746d6df8f88c67a407ffcb14e9401dc8ce66e2b1d6f33d94d6d7976565b360f4",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_Seminar_Problem_4_Table.png",
      "sha256": "9897534491e124b69f9affcf92729f1e94596fc293a4837a701a29c06e4d696f",
      "bytes": 93426,
      "note_sections": [
        "whole image; finished-note caption interpretation"
      ],
      "objective_ids": [
        "O003"
      ],
      "semantic_baseline": "source blank table includes82,84,78,81,79 and account columns;used only during supported example",
      "change_class": "unchanged",
      "previous_path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_Seminar_Problem_4_Table.png",
      "previous_hash": "9897534491e124b69f9affcf92729f1e94596fc293a4837a701a29c06e4d696f",
      "affected_objective_ids": [],
      "inspection_status": "visually_inspected_finished_asset"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Bond_Futures_Conversion_Factors_and_Delivery.md",
      "sha256": "a9656034a515703d258f470320f1ea171d1dcd964701cf8a1f19c755171cfec1",
      "bytes": 14361,
      "note_sections": [
        "Bond futures, conversion factors and delivery",
        "The notional contract and its monetary scale",
        "A short closing trade",
        "Clean price, full price and coupon dates",
        "Conversion factor: price at the contract's reference yield",
        "Follow the source's valuation steps",
        "The conversion-factor example has a day-count error",
        "The short's cost-of-carry transaction",
        "Delivery timing under the source's carry rule",
        "What to carry forward"
      ],
      "objective_ids": [
        "O012"
      ],
      "semantic_baseline": "Clean quote per100 and face100000 imply multiplier1000, tickUSD10. CF is month-specific clean reference-yield price/100. Source P_AN discounts22 coupons4 and face100 at periodic0.035; earlier full value=(P_AN+4)/(1.035)^fraction, then subtract accrued coupon and divide100. Source171/170 discrepancy is exposed. Invoice=FP×CF+delivery AC; daily carry=coupon/365−fullPP×funding/365. Positive-last/negative-first timing is a simplified constant-carry rule; CTD requires eligible cash-flow comparison.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Implied_Repo_Rate_and_Cheapest_to_Deliver.md",
      "sha256": "cc1472840d045ac50e647cb4be41302f7eeca6bf21ea19e86c7d6305b27d2153",
      "bytes": 12264,
      "note_sections": [
        "Implied repo rate and cheapest to deliver",
        "Why the return resembles a repo loan",
        "Notation, units and assumptions",
        "One coupon before delivery",
        "Recompute the source's numerical example",
        "No coupon before delivery",
        "Compare eligible bonds and choose CTD",
        "What to carry forward"
      ],
      "objective_ids": [
        "O013"
      ],
      "semantic_baseline": "Full PP=clean market+purchase AC; full IP=FP×CF+delivery AC. Simple actual/365 one-coupon identity PP(1+rn/365)=IP+C(1+rm/365), with coupon reinvested at impliedr, gives r=(IP+C−PP)365/(PPn−Cm), nonzero denominator. No coupon: r=(IP−PP)365/(PPn). Source43/180 accrued coupon yields3.61742%, not printed3.57%. CTD maximises comparable eligible IRR; actual funding/fees are separate and actual basket absent. This is not compounded project IRR.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O013"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Short_Term_Interest_Rate_Futures.md",
      "sha256": "60171e496c1089e75dcac3575612a0518e958cac6a80dbe02da9b438b622a003",
      "bytes": 9220,
      "note_sections": [
        "Short-term interest rate futures",
        "Quotation, tick value and the deposit period",
        "Closing the futures before the deposit begins",
        "Cash settlement and the effective deposit rate",
        "The slide's day-count and payment-timing qualification",
        "Physical delivery and compensation for a lower deposit rate",
        "What to carry forward"
      ],
      "objective_ids": [
        "O011"
      ],
      "semantic_baseline": "F=100−annual rate in percent; tick0.01 quote point is one basis point, worth EUR12.50 on EUR500000 with quarter-year0.25. Lender long, borrower short. Effective rate=i_spot+G/(Lτ); physical placement below benchmark adds separate L×rate difference×τ compensation. Source91/365 versus0.25 and discounted/undiscounted payment timing remain unreconciled; no universal exact hedge/account value.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O011"
      ],
      "inspection_status": "read_finished_note"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Stock_Index_and_Currency_Futures.md",
      "sha256": "9934681819e12121ce3bdcd2bf33e74747d3ecc2cf2232b8981de7f2236997ac",
      "bytes": 12162,
      "note_sections": [
        "Stock index and currency futures",
        "Read the contract before calculating",
        "SIFT 500: index points become euros",
        "Closing after five days",
        "Holding until cash settlement",
        "ECFT: identify the traded and invoice currencies",
        "Closing after ten days",
        "Physical delivery fixes the effective purchase rate",
        "What to carry forward"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Hypothetical index multiplier EUR10/point and tick0.5 imply EUR5/tick. Close and held EDSP are alternative signed payoff paths. Currency quantity EUR25000, quote USD/EUR, tick0.0001 imply USD2.50/tick; matching invoice XFT minus long gain X(FT−F0) leaves XF0 without funding/fees. EDSP follows declared sampling/trim rules. Margin return and simple annualisation are not underlying yield or forecast; specifications are pedagogical.",
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
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Bond_Delivery_Timeline.png",
      "sha256": "50f81e2d20373c3aee536abde2f8b02c08fca9789aec45a51504e797b19c7181",
      "bytes": 560506,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Bond_Specification.png",
      "sha256": "aa1185a85ac76a4e5b192193b570e5f71474b38ff908f459dca34bc5abcfd051",
      "bytes": 483413,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Conversion_Factor_Example.png",
      "sha256": "f5b486a139dabb06effd422c420833a52cf4f5c1135c0c9dc9c8ba2e09fd311b",
      "bytes": 653884,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Cost_of_Carry_Flows.png",
      "sha256": "904037172cf5ca319c1c05ad9b0b99ce13f41368790b073d7f08569c08d62917",
      "bytes": 510729,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O012"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O012"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Currency_Closing_and_Delivery.png",
      "sha256": "72533b3b482f8adefb48df1116fce28fe45522aa22c9765b710e425eec05ec45",
      "bytes": 655568,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
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
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Currency_Specification.png",
      "sha256": "41331195927a28988b3e17c5e93d5aea1741cb7acf2bb11666becfd88bec5199",
      "bytes": 521880,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
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
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_IRR_Formulas.png",
      "sha256": "7110fa1a1ce876ffc387e310e867173dd9aeac45a0f9da2b73757cdd5fef912c",
      "bytes": 655914,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O013"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O013"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Index_Closing_and_Settlement.png",
      "sha256": "a3b220febac0005f69d4a083e237292585f3f5fcba3890313a51081c3bfa9251",
      "bytes": 694949,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
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
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Index_Specification.png",
      "sha256": "a8430c714ece0c16ee9368aa1c8919076cc7495ca50c130319752d08b40014d5",
      "bytes": 493084,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O009",
        "O010"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
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
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Short_Rate_Settlement.png",
      "sha256": "3c2f0f5cd2dc703ba5accbee04e937faeda109215173f18e09510c0cb129a8f3",
      "bytes": 664828,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O011"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O011"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    },
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Short_Rate_Specification.png",
      "sha256": "a3514c97e0b637d3634d010fca4a409ace334314546a3cfe7a5a6cedb0602669",
      "bytes": 493074,
      "note_sections": [
        "whole image; finished-note caption and interpretation"
      ],
      "objective_ids": [
        "O011"
      ],
      "semantic_baseline": "Source-faithful visual and qualification described beside its finished-note embed; interpretation incorporated in mapped objectives.",
      "change_class": "new_content",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O011"
      ],
      "inspection_status": "read_finished_asset_and_verified_ingest_review"
    }
  ]
}
```

## Completion provenance and semantic reconciliation

P003 fingerprints all selected finished Week1/Week2 notes and their required assets at completed ingestion revision2. The linked current run documents independent source checks and bounded exclusions. SHA-256 measures bytes; change classes follow finished-note inspection. Week1 academic notes/assets remain unchanged. Hub additions and new Week2 inputs are new_content, affecting the new capabilities only; no old criteria/conditions change. Each entry records actual headings, prior hash/path, claim/assumption digest and objective mapping. Access was stable and no selected input was deleted or moved.

| Finished input | Hash / bytes | Objectives / change |
|---|---|---|
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md]] | `12acb3a4ec118be8accf95e57e840efa6bcb31a40d1d9fd85f79b019312a7658` / 18726 | O001, O002, O003, O004, O005, O006, O007, O008, O009, O010, O011, O012, O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Basis_Convergence_and_Futures_Hedging.md]] | `b3e4487925e9bd1ca9c2c341990863be4d2ff9f9a1e8e2211e1742e1bc4e5956` / 12935 | O006, O007, O008 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Introduction_to_Futures_Seminar_Exercises.md]] | `b10a0ed1ddfde242583a447a4246738dc8f31af4dca1c5f77970596782335d04` / 13216 | O001, O002, O003, O004, O005 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Margins_and_Marking_to_Market.md]] | `c92b574f4c33c97bdbefad673c63cc8029a344a79d7b1da69ed2bba44076e313` / 12176 | O002, O003, O004, O005, O007, O008 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Spot_Forward_and_Futures_Contracts.md]] | `ed4177199ebe557e2c52129bcd94b690b22e553a5eafba9ce5f4dc19656c3045` / 18244 | O001, O002 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Long_Short_Payoffs.png]] | `0031c88b703a27700f6bfb39b64c4c8b9b64abfe97f1aa4d2e6e1fb62f96c7be` / 15695 | O002 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Margin_Table.png]] | `791b5a8ad0c57b141534941e4d758d4d07b5999c6d66d55ad2b0502dba061e11` / 71163 | O003, O007 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Clearing_Arrangement.png]] | `7e782a762b3ab6cb0f8270aaa82f495a4e1ba7bfcebc0d5e2b94c5e867adc8c9` / 563220 | O001 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Convergence_Patterns.png]] | `a582e9824ebc65437ce015f53e559e4c7dd6c2d238cb527111c38f3a73a3d05c` / 138212 | O006, O007 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Forward_Timeline.png]] | `caaeedc9f48c35dcfb8971aa6383f583e26345893f42e6acc88e15c98b6be011` / 63778 | O001 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Spot_Timelines.png]] | `746d6df8f88c67a407ffcb14e9401dc8ce66e2b1d6f33d94d6d7976565b360f4` / 551194 | O001 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_Seminar_Problem_4_Table.png]] | `9897534491e124b69f9affcf92729f1e94596fc293a4837a701a29c06e4d696f` / 93426 | O003 / unchanged |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Bond_Futures_Conversion_Factors_and_Delivery.md]] | `a9656034a515703d258f470320f1ea171d1dcd964701cf8a1f19c755171cfec1` / 14361 | O012 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Implied_Repo_Rate_and_Cheapest_to_Deliver.md]] | `cc1472840d045ac50e647cb4be41302f7eeca6bf21ea19e86c7d6305b27d2153` / 12264 | O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Short_Term_Interest_Rate_Futures.md]] | `60171e496c1089e75dcac3575612a0518e958cac6a80dbe02da9b438b622a003` / 9220 | O011 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Stock_Index_and_Currency_Futures.md]] | `9934681819e12121ce3bdcd2bf33e74747d3ecc2cf2232b8981de7f2236997ac` / 12162 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Bond_Delivery_Timeline.png]] | `50f81e2d20373c3aee536abde2f8b02c08fca9789aec45a51504e797b19c7181` / 560506 | O012 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Bond_Specification.png]] | `aa1185a85ac76a4e5b192193b570e5f71474b38ff908f459dca34bc5abcfd051` / 483413 | O012 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Conversion_Factor_Example.png]] | `f5b486a139dabb06effd422c420833a52cf4f5c1135c0c9dc9c8ba2e09fd311b` / 653884 | O012 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Cost_of_Carry_Flows.png]] | `904037172cf5ca319c1c05ad9b0b99ce13f41368790b073d7f08569c08d62917` / 510729 | O012 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Currency_Closing_and_Delivery.png]] | `72533b3b482f8adefb48df1116fce28fe45522aa22c9765b710e425eec05ec45` / 655568 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Currency_Specification.png]] | `41331195927a28988b3e17c5e93d5aea1741cb7acf2bb11666becfd88bec5199` / 521880 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_IRR_Formulas.png]] | `7110fa1a1ce876ffc387e310e867173dd9aeac45a0f9da2b73757cdd5fef912c` / 655914 | O013 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Index_Closing_and_Settlement.png]] | `a3b220febac0005f69d4a083e237292585f3f5fcba3890313a51081c3bfa9251` / 694949 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Index_Specification.png]] | `a8430c714ece0c16ee9368aa1c8919076cc7495ca50c130319752d08b40014d5` / 493084 | O009, O010 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Short_Rate_Settlement.png]] | `3c2f0f5cd2dc703ba5accbee04e937faeda109215173f18e09510c0cb129a8f3` / 664828 | O011 / new_content |
| [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Short_Rate_Specification.png]] | `a3514c97e0b637d3634d010fca4a409ace334314546a3cfe7a5a6cedb0602669` / 493074 | O011 / new_content |

## Preserved history and verification

The exact replaced P002 bundle is preserved under curriculum_history/P002; existing P001 history is untouched. Current tuple: PLAN-20261009-FMI-P003 / P003 / V002 / ingestion2. The active ingest transaction is INGEST-FINANCIAL_MARKETS_INSTRUMENTS_I-ccde853ce42a4bd9a56bb46e241f3338. Active bytes must match their committed owner journal. Subsequent outside-workflow note changes need explicit freshness reconciliation; no watcher is introduced.

## Uncovered material and assumptions

Later option/pricing chapters, external videos and legal/broker claims remain outside supported ingestion. Exactly50 overall assessment points and live timetable details remain unresolved course-team context. Week2 source examples are hypothetical; interest-rate timing/day-count, bond conversion-factor170/171 and printed repo-return discrepancies stay explicit. Prepared tasks use declared consistent inputs, not the erroneous arithmetic or universal market claims. No raw sources were read or hashed by planning. No learner evidence or scheduling records were created.
