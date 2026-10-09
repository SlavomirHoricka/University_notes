# Teaching skill review — historical rationale

Implementation update, 2026-10-02: [teach/SKILL.md](../../teach/SKILL.md) is now the single maintained teaching skill, installed via `~/.agents/skills/teach`. It accepts a course/week folder and “teach me this week's content,” resolves dated scope or asks one necessary clarification, and initializes course memory automatically. The original is archived, not an alternative active skill. The review below records the earlier design rationale and research limits.

Reviewed 2026-10-02. The original's strongest feature is its preference for motivated explanations and connected knowledge. Keep that preference. Replace its guarantees about memory, compulsory search for failure, and immediate quiz-based confirmation with bounded diagnosis, explicit assessment criteria, independent work, and dated delayed checks.

The supplied skill was reviewed as an artifact, **not executed**. No course was taught, no learner assessment took place, no course plans were populated, and no scheduler was activated.

## Deliverables

- [Current teaching skill](../../teach/SKILL.md).
- [Record, source-freshness, and scheduler contract](../../teach/references/RECORDS.md).
- Blank templates: [course plan](../../teach/templates/learning_plan.md), [learning log and canonical current state](../../teach/templates/learning_log.md), [source manifest](../../teach/templates/source_manifest.md).
- [Seven behavioral walkthroughs and boundary cases](../../teach/references/WALKTHROUGH.md).
- [Archived audit copy of the original](../../.backups/teaching-review-2026-10-02/ORIGINAL_SKILL.md). Original supplied path: `/Users/slavomirhoricka/Downloads/SKILL.md`; SHA-256: `180d78f5bd65e2f251dab60c716ac5874727595a28377e58590c1aac526ada80`. Line references below refer to this unchanged 146-line document.

## Vault findings that affect the design

Read the preparation documents first, then sampled three contrasting hubs and relevant linked notes; this was not a full content audit. The existing structural checker found the already documented four missing concept targets and no ambiguous file links, missing source-metadata targets, hub-name violations, or course-mirror differences. It does not check heading anchors, academic correctness, or attachment contents.

| Inspected source | Finding and design consequence |
|---|---|
| [Econometrics I hub](../../../01_Notes/2025_2026/Summer_Semester/JEB109_Econometrics_I/JEB109_Econometrics_I_main.md), concept index, theorem section, textbook integration, cross-course connections | A synthesis hub links topic notes, textbook chapters and other courses. A course link can be a useful application or extension, not a prerequisite. Do not traverse all connected courses. |
| [Gauss–Markov note](../../../01_Notes/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Gauss_Markov_Theorem.md) and linked [MLR assumptions note](../../../01_Notes/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/MLR_Assumptions_and_OLS_Unbiasedness.md) | Conditions are central to the subject. The Gauss–Markov proof moves between conditional and unconditioned notation; its WLS and historical claims deserve source checks before teaching. This review flags these as inspection needs, not completed academic corrections. The linked lecture PDF exists but its pages were not inspected here. |
| [Mergers and Acquisitions hub](../../../01_Notes/2026_2027/Winter_Semester/JEM231_Mergers_and_Acquisitions/JEM231_Mergers_and_Acquisitions_main.md), opening links and exam-preparation sections; linked [Takeover](../../../01_Notes/2026_2027/Winter_Semester/JEM231_Mergers_and_Acquisitions/Takeover.md) and [shared resource](../../../02_Resources/Shareholder_Activist.md) | Content includes image embeds, heading aliases, answers, corrections, and an instruction to await completed answers. Those are source content, not current authorization or verified dated assessments. Prior assistance, note access, authorship and attempt dates are not established. |
| [Auctions hub](../../../01_Notes/2025_2026/Summer_Semester/JEB160_Auctions_and_Game_Theory/JEB160_Auctions_and_Game_Theory_main.md) | Explicitly a materials navigation index, not a syllabus or summary. Having a hub does not imply conceptual notes or learned content. |

Course materials were checked by path, not read in full. Relevant PDFs, image contents, spreadsheet calculations, and the compressed shared drawing remain uninspected for academic content. No conclusions about syllabus completeness or this learner's ability follow from this sample. Preserve the existing notes and links; the proposed skill requires inspecting actual sources before teaching their claims.

## Prioritized critique of the original loop

Priority 1 affects accuracy or learning validity; priority 2 affects efficiency and continuity. The replacement wording is embodied in the proposed skill and protocol. Research labels and links appear in the next section.

| Priority and location | Problem and consequence | Concrete replacement |
|---|---|---|
| **1 — lines 10, 20, 24, 30–36:** “Understood facts don't”; instantaneous safe commitment | Understanding is valuable, but felt coherence and immediate performance cannot establish durable retention. The proposed brain mechanism is asserted without evidence and invites premature stopping. | “Connect ideas and check understanding, then assess independent use and delayed retrieval. Treat a subjective click as a report, not proof.” See learning/performance and calibration research below. |
| **1 — lines 28–45, 118, 130:** caveat-free foundations; never start from a derived fact | Forces conditional theories into universals and can recurse indefinitely. It also contradicts line 32's permission to accept derived foundations. Definitions and axioms are not facts outside all systems; empirical assumptions require scope. | “Start from relevant, sufficiently understood definitions, assumptions and results; state conditions. Revisit a prerequisite when performance shows it is needed.” |
| **1 — lines 88–97:** both a correct floor and incorrect ceiling are mandatory; “If he never misses, you never found the edge” | No finite stopping criterion; uncalibrated questions do not form an ordered difficulty scale. Fatigue or an ambiguous item can be mistaken for a knowledge boundary. | “Sample within the requested scope, stop when the next teaching decision is supported, and cap diagnosis. Correct target-level work can end diagnosis without failure.” |
| **1 — lines 62, 97, 131–135:** gradable means quiz; one node check confirms landing | Recognition, recent exposure and clues can produce success without independent production. Knowing which option is correct does not reveal exactly why another was chosen. | Use a rubric and response format matched to the objective; preserve first unaided response, hints, and subsequent correction separately. Require distinct independent checks and later retention evidence. |
| **1 — lines 67–137:** no closure, persistence or resumption procedure | The loop ends at teaching. A new agent cannot reliably distinguish planned coverage, actual performance and unresolved gaps; it may repeat or skip work. | Maintain three course Markdown files; checkpoint actual events and one canonical current state; resume from committed evidence. |
| **1 — same lifecycle, entire document:** no source reconciliation | Updated notes can invalidate instruction, criteria or prerequisites while the learner status still looks current. | Compare a bounded content-hash manifest, inspect semantic changes, preserve old versions/evidence, and require targeted reassessment of affected learned claims. |
| **1 — lines 133–137:** “stop and fix” has no procedure | May become repeated explanation, repeated guesses, or answer imitation with no error diagnosis. | Identify the error, supply task-focused correction or a worked example, then assess a fresh variant; cap repeated attempts. |
| **2 — lines 86–99:** diagnosis before learning-goal resolution | The “relevant strands” cannot be selected reliably until the requested scope is understood. | Resolve request plus hub first; ask only material clarifications; reuse adequate recent evidence. |
| **2 — lines 49–65:** effort and Socratic discovery imply stronger locking-in | Generating a response can help, but guessing without adequate knowledge or later consolidation can waste time and entrench errors. | Offer a bounded prediction when feasible; otherwise explain or model. Always consolidate attempted generation with accurate instruction. |
| **2 — lines 69, 113–120, 126:** rigid three phases, compulsory DAG and approval for every explanation | Adds friction even for a narrow question; conceptual graphs can contain cycles and mutually supporting concepts. | Use the full lifecycle for study sessions, a compact answer for a factual question; offer a brief sequence and optional map. Respect requested approval, without making it routine. |
| **2 — lines 71, 105:** mandatory `researcher`; lines 62–99: assumed tools | Tool names and agent availability are environment-specific. A second model's answer is not source verification. | Verify against the underlying source with available tools; plain chat works for questions. Disclose uncertainty rather than assuming a subagent removes it. |
| **2 — lines 75–82:** useful MCQ constraints but an overstrong diagnostic claim | Parallel options and plausible distractors reduce cues, but a selected distractor can still reflect guessing or wording. | Retain sensible option construction, vary answer position, inspect reasoning where needed, and confirm important conclusions with an independent constructed response. |
| **2 — lines 141–146:** assumes all output is in Obsidian | Math delimiters can differ between the stored note and the chat renderer. | Preserve Obsidian LaTeX in saved Markdown; adapt chat display to its renderer. |

The original has no Bloom alignment, distributed practice, successive relearning, distinct transfer assessment, scheduler evidence contract, or dated retention tracking. These are additions requested by the review prompt, not hidden features credited to the original. “Structured forgetting” does not appear in the attached skill; it is assessed below because the review prompt explicitly requests it.

## Learning-science synthesis and tutor decisions

This is a targeted research synthesis, not a preregistered systematic review or an exhaustive search of all publications through 2026. Searches covered the named techniques and terminology, prioritized research articles, original frameworks, systematic reviews and meta-analyses, and checked relevant full-text sections where accessible. “Robust” below describes replicated average benefits across relevant studies, not a guarantee for every learner, subject or AI implementation. Individual-study findings and mechanisms are identified separately. The numbered limits in the skill are **pragmatic heuristics**, not effect-size-derived cutoffs.

### Retrieval practice and immediate performance

**Robust average benefit, with task limits.** A systematic classroom review found benefits across subjects, ages and test formats, but only a small fraction of included experiments came from non-WEIRD settings. This supports bringing studied information to mind rather than relying entirely on rereading; it does not justify testing unknown material indefinitely. [Agarwal, Nunes & Blunt, 2021](https://link.springer.com/article/10.1007/s10648-021-09595-9).

**Primary experimental illustration.** Roediger and Karpicke contrasted study and testing with prose materials; the delayed advantage of testing need not match immediate performance. Generalizing from such tasks to long proofs or real-world decisions requires care. [Roediger & Karpicke, 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x).

**Implementation:** obtain a response before feedback, match retrieval to the objective, then correct errors. Use an explanation or fresh problem to assess independent production. Retrieval can include conceptual reasoning; it is not confined to vocabulary. **Risk:** test anxiety, missing prerequisite knowledge, answer leakage, and repeated failure can make a poorly designed quiz unproductive. Shorten or teach when needed; maintain both the unaided and helped outcomes.

**Interpretive framework:** observed fluency during learning can diverge from later retention or transfer. Consequently, immediate checks guide instruction but cannot certify durable learning. [Soderstrom & Bjork, 2015](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/11/soderstorm_ra_learningvsperformance.pdf).

### Distributed practice, spacing, and “structured forgetting”

**Robust average benefit.** A large meta-analysis of verbal recall found that effective spacing depends jointly on the interstudy gap and the intended retention interval. It does not identify one optimal interval for every task or learner. Its verbal-memory emphasis limits direct numerical scheduling recommendations for complex university problem solving. [Cepeda et al., 2006](https://pubmed.ncbi.nlm.nih.gov/16719566/).

**Implementation:** record actual attempts, instruction/restudy exposure, elapsed time and the retention horizon; hand these to the scheduling agent. Do later retrieval before re-explanation, then correct and relearn. Too-long gaps can leave insufficient retrievable knowledge; too-short gaps can mainly measure recent activation. Unknown intervening exposure must remain visible. Do not intentionally withhold help until the learner forgets, fit an Ebbinghaus curve from two answers, or promise that an expanding schedule is always superior. “Structured forgetting” is an informal user label; **spaced retrieval practice / retrieval scheduling** describes the supported intended behavior more accurately.

### Successive relearning

**Supported, with a narrower evidence base than generic retrieval/spacing.** Successive relearning combines reaching a performance criterion with reaching it again in later spaced sessions. It is not simply rereading on a schedule. Studies of concept learning and recall support its usefulness, but laboratory criteria and schedules should not be transplanted uncritically to essay quality or multi-step reasoning. [Rawson & Dunlosky, 2011](https://doi.org/10.1037/a0023956); [their 2022 research review](https://www.psychologicalscience.org/journals/current-directions/09637214221100484/).

**Implementation:** use a clear objective-specific criterion, then renew retrieval later. Preserve first-attempt results: many prompted retries are not equivalent to effortless independent recall. **Risk:** chasing a pass can consume a session and conceal fragile learning. Stop locally after a bounded number of attempts and record another need. The proposal's two-check advancement criterion is not the authors' universally established optimum.

### Interleaving versus blocking

**Context-dependent.** A meta-analysis found an overall interleaving benefit with substantial variation by material; advantages were stronger for some visual category tasks, smaller for mathematics, and blocking could be better for word materials. The authors caution against indiscriminate extrapolation across domains. [Brunmair & Richter, 2019](https://doi.org/10.1037/bul0000209).

**Implementation:** after a learner can execute a method, mix confusable methods so selection must be justified—for example, identify which hypothesis-test structure a problem requires before solving it. **Risk:** mixing unrelated topics or interleaving before a novice understands any component increases task switching without necessarily teaching discrimination. Begin with a brief blocked example/practice sequence when needed; change ordering based on method-selection evidence. Interleaving and spacing can co-occur but are distinct manipulations: changing category order is not itself a specified temporal interval.

### Feedback and error correction

**Robust aggregate benefit, heterogeneous treatment.** A meta-analysis of 435 studies found that effects depend substantially on the information supplied by feedback; “feedback” is not a single uniform intervention. This supports actionable task/process information rather than assuming a score or praise is sufficient. [Wisniewski, Zierer & Hattie, 2020](https://pubmed.ncbi.nlm.nih.gov/32038429/).

**Implementation:** preserve the initial response; identify the erroneous step, explain why, offer a corrected model and ask for a new application. Give a plausible slip a brief chance for self-correction. **Risk:** revealing the answer before an assessment invalidates the intended independence claim; unverified AI feedback can introduce errors. Verify contentious grading and accept valid alternatives. Prompt correction is the practical default here, not a claim that immediate feedback universally dominates delayed feedback. Use a fresh delayed check to see whether correction survives.

### Worked examples, fading, and cognitive load

**Primary evidence plus instructional theory.** Experiments studied transitions from worked examples to problem solving using faded steps and self-explanation prompts. They support designing a transition to independent work rather than treating example study as the final outcome. Task and transfer effects depend on the particular design. [Atkinson, Renkl & Merrill, 2003](https://doi.org/10.1037/0022-0663.95.4.774).

**Framework with empirical instructional effects.** Cognitive load theory motivates reducing unnecessary simultaneous demands; guidance that helps a novice may become redundant with expertise. It is not a license to infer a numeric working-memory capacity from chat behavior. [Sweller, van Merriënboer & Paas, 2019](https://link.springer.com/article/10.1007/s10648-019-09465-5).

**Implementation:** model a problem with its method-selection rationale, omit a step for completion, then remove the example for a fresh problem. Integrate formulas and their explanations, and simplify the current subtask when the learner cannot coordinate its elements. **Risk:** premature fading leaves the learner guessing; permanent guidance measures support-following rather than independence. A lengthy derivation of every foundation can itself overload a novice. Fade or restore support from observed performance, not an assumed universal “best” lesson size.

### Self-explanation and elaboration

**Positive aggregate evidence for prompted self-explanation.** A meta-analysis of 69 effect sizes found learning benefits from prompts to generate causal/conceptual connections across varied tasks. This does not establish that explaining every line is worth its time cost. [Bisra et al., 2018](https://link.springer.com/article/10.1007/s10648-018-9434-x).

**More conditional evidence for elaborative interrogation.** Asking why a stated fact makes sense may help integrate knowledge, with prior knowledge an important moderator; evidence is less comprehensive across tasks and long delays than for retrieval and spacing. [Dunlosky et al., 2013, sections 1–2](https://journals.sagepub.com/doi/pdf/10.1177/1529100612453266).

**Implementation:** ask one discriminating question: why this step is valid, which assumption it uses, or how two cases differ. Check the answer against the source. **Risk:** unsupported explanations can sound coherent while being wrong, and repetitive paraphrase can consume practice time. Provide an explanation when the learner lacks the background to generate one. The user's preference for connected ideas is worth preserving without turning it into an unsupported universal brain mechanism.

### Generation and discovery before explanation

**Context-dependent.** A meta-analysis supports a generation effect on memory in studied conditions, but generating constrained information is not equivalent to independently discovering a complex theory. [Bertsch et al., 2007](https://doi.org/10.3758/BF03193441).

Research comparing problem solving followed by instruction with instruction-first designs finds that well-designed preparatory problem solving can help; learner characteristics and implementation matter. Merely letting someone fail is not the productive-failure design. [Sinha & Kapur, 2021](https://journals.sagepub.com/doi/full/10.3102/00346543211019105).

**Implementation:** use a short prediction/attempt when prerequisite knowledge makes it plausible, then connect the attempt to explicit instruction. Explain directly when the task is inaccessible or the learner requests delivery. **Risk:** unbounded discovery adds frustration and can leave misconceptions uncorrected. Do not label all effort beneficial or insist that every fact must feel inevitable. Conventions, historical choices and empirical results may have alternatives rather than a unique derivation.

### Metacognitive calibration

**Primary evidence, task-specific.** Studies of college students learning definitions connected inaccurate self-evaluation with poorer retention; giving component-level standards can improve evaluation of text learning. These tasks support caution about confidence, not a universal causal diagnosis of this learner. [Dunlosky & Rawson, 2012](https://www.sciencedirect.com/science/article/pii/S0959475211000685); [Dunlosky et al., 2011](https://pubmed.ncbi.nlm.nih.gov/20700858/).

**Implementation:** sometimes ask confidence before feedback, compare it with rubric-scored performance, and ask the learner to identify missing components or an appropriate study strategy. Record confidence separately; keep it optional to limit burden. **Risk:** asking “does that feel obvious?” can reinforce fluency-based overconfidence, while excessive confidence reporting interrupts learning. A single calibration mismatch is weak evidence; inspect patterns over actual attempts.

### Prerequisite knowledge

**Important but not a universal prediction of learning gains.** A large meta-analysis distinguishes the association between prior and final knowledge from prediction of learning gains; the latter is more variable and depends on measurement and conditions. A prior score should not become a fixed ability label. [Simonsmeier et al., 2022](https://www.uni-trier.de/fileadmin/fb1/prof/PSY/PAE/Team/Schneider/SimonsmeierEtAl2021.pdf).

**Implementation:** infer a task dependency from the subject matter, sample the necessary skill, and repair a gap if it blocks progress. Treat evidence as provisional and local. **Risk:** testing every possible foundation delays learning, while assuming every graph link is a prerequisite invents dependencies. Incorrect prior knowledge needs a contrast and correction, not merely more detail. A missing course note is a source gap; it says nothing by itself about what the learner knows.

### Transfer

**Supported but bounded.** A meta-analysis of test-enhanced learning found transfer benefits moderated by task relationships and practice characteristics; evidence is richer for nearer transfer than for transfer across distant domains. Retention of the same answer and success on a novel problem are different outcomes. [Pan & Rickard, 2018](https://pdf.retrievalpractice.org/transfer/Pan_Rickard_2018.pdf).

**Implementation:** vary context, representation, assumptions, or the choice between methods, and require a reason for choosing a method. Record what changed. A near-transfer success can justify the next task but does not certify broad transfer. **Risk:** a familiar question with new numbers may only test the same procedure; an overly distant task can fail because of unrelated background demands. Progress from purposeful variation to more distant cases only when that serves the goal.

## Revised Bloom's taxonomy: useful alignment, limited inference

Krathwohl's overview treats the revision as a framework linking kinds of knowledge with cognitive processes; its hierarchy permits overlap. Use it to expose a mismatch such as “explain and evaluate assumptions” being assessed only by term recognition. It does not supply a calibrated difficulty scale, an instructional schedule, or a retention measurement. [Krathwohl, 2002](https://www.upgrade.chemnet.edu.au/sites/default/files/files/Blooms_taxonomy_2002_Krathwohl.pdf).

Primary experiments found that higher-order and mixed retrieval questions improved higher-order performance where factual quizzes alone did not. This challenges a blanket fact-drill-first prescription; it does not mean facts or genuine prerequisites are unnecessary. [Agarwal, 2019](https://pdf.poojaagarwal.com/Agarwal_2019_JEdPsych.pdf).

The following are **illustrative objective designs, not a populated course plan or learner assessment**:

| Knowledge emphasis | Process and possible task | Evidence to collect |
|---|---|---|
| Factual | Remember notation and the stated assumptions of a named result. | Unaided recall with necessary qualifications; later revisit. |
| Conceptual | Understand/analyze why an assumption matters; contrast cases. | Explanation connecting the assumption to a consequence; counterexample interpretation. |
| Procedural | Apply an appropriate method to a fresh problem. | Method selection, valid steps and result under the stated conditions. |
| Metacognitive | Evaluate whether an answer meets a rubric and choose a remedy. | Confidence versus actual performance, identified missing component, justified next study action. |

“Create” belongs only where designing a model, example or argument serves the actual objective. A sophisticated-sounding verb does not make an easy familiar task difficult, nor does a difficult recall item measure deep understanding. Delayed and changed-context evidence remain separate dimensions.

## Terminology corrections

| Phrase or concept | Appropriate term and intended behavior | Operational distinction for this tutor |
|---|---|---|
| “Binary-search the edge” | Bounded adaptive diagnostic questioning | Choose a question that informs the next teaching decision. No sorted calibrated scale, deterministic pass/fail boundary, or logarithmic-search guarantee exists here. |
| Diagnostic versus formative assessment | Diagnose current needs; use evidence to adapt learning | A diagnostic becomes formative through its use in the next decision. Merely asking or grading questions does not complete that loop. [Black & Wiliam, 2009](https://kclpure.kcl.ac.uk/portal/en/publications/developing-the-theory-of-formative-assessment/). |
| Adaptive testing | Responses influence subsequent item selection | A conversational tutor can adapt informally without claiming a standardized ability estimate. |
| Computerized adaptive testing (CAT) | A formal adaptive measurement procedure | Classical IRT-based CAT uses calibrated item banks, a specified latent-trait model, response-based estimation and stopping criteria. Dimensionality must fit the model (often unidimensional, sometimes explicitly multidimensional); local independence and model fit matter. Generated chat questions have not established these properties. [Weiss, 1982](https://journals.sagepub.com/doi/10.1177/014662168200600408); [ETS on local independence](https://www.ets.org/research/policy_research_reports/publications/report/1984/hwgu.html). |
| Learner model | A representation of observed knowledge and uncertainty | Here it is an objective/evidence ledger, not a fitted probability model. Knowledge tracing is a formal alternative with additional assumptions and data requirements; do not print invented mastery probabilities. [Corbett & Anderson, 1995](https://link.springer.com/article/10.1007/BF01099821). |
| Scaffolding | Contingent instructional support | Change hints, examples or task decomposition to help performance, then remove support and observe independence. An assisted answer is not an independent one. The original tutoring study concerned young children, so adult AI use is an adaptation. [Wood, Bruner & Ross, 1976](https://acamh.onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-7610.1976.tb00381.x). |
| Dynamic assessment | Deliberate assessment through intervention and response to mediation | Observe an unaided attempt, specified help, response to help, and a fresh unaided task. This is a dynamic-assessment-inspired routine, not a validated learning-potential score or a synonym for any hint. [Black & Wiliam, 2009, discussion of dynamic assessment](https://kclpure.kcl.ac.uk/ws/portalfiles/portal/9119063/Black2009_Developing_the_theory_of_formative_assessment.pdf). |
| Zone of proximal development (ZPD) | A developmental theoretical construct involving independent and mediated performance | It is not the interval between a quiz success and failure. Its developmental meaning is broader than “what can be done with any help”; the distinction cautions against claiming that a short adult quiz measures a ZPD. [Chaiklin, 2003](https://blogs.ubc.ca/vygotsky/files/2013/11/chaiklin.zpd_.pdf). |
| “Structured forgetting” | Spaced retrieval, distributed practice, retrieval scheduling | Deliberately space opportunities and inspect performance, rather than prescribe forgetting. “Desirable difficulty” describes a difficulty that improves later learning in suitable conditions, not every struggle. See spacing and learning/performance evidence above. |
| “Locks in,” “the click,” “proof he knows” | Subjective fluency/insight; observed task performance | Record self-report separately, retain conditions and rubric, then test later and on new tasks. Do not convert a pleasant explanation into mastery. |
| “Unconditional truth,” “axiom” | Definition, model assumption, theorem under assumptions, or empirical claim | Name the epistemic role and scope. An axiom is accepted within a formal system; personal confidence does not establish universal truth. |

The relationships are functional, not interchangeable names: **diagnosis selects a need; formative use changes instruction; scaffolding supplies help; a dynamic assessment deliberately studies response to help; a learner model stores the resulting evidence; adaptive testing selects items; CAT can estimate ability only under its measurement design; ZPD is a theoretical interpretation, not the score output by this workflow.**

## Why the practical rules take this form

The six-item/ten-minute diagnostic cap, two distinct independent checks, two-hint fallback, three-attempt assessment stop, 24-hour delayed-label default, status vocabulary and file protocol are adjustable engineering/pedagogical decisions. None is an empirically established universal optimum. They prevent foreseeable failures while leaving the actual rubric, difficulty and pacing responsive to the subject and learner.

The plan stores objective-level evidence rather than a single “mastery” number. Independent acquisition, delayed retention, transfer, confidence and source validity can disagree. Keeping those distinctions visible is more useful than collapsing them into a false precision score. Learning can advance while retention checks remain pending; it cannot quietly pass a known changed-content prerequisite gate.

Source manifests retain compact prior meaning and criteria as well as hashes. This meets reconciliation needs without copying the vault. It cannot reconstruct a detail never preserved: the required response is an explicit uncertainty and targeted inspection, not a claim to have detected every semantic change. Cooperative locking, revision checks and a commit journal protect shared Markdown state; they cannot prevent an unrelated editor from ignoring the lock, so conflicts must stop replacement.

## Evidence and access limitations

The complete skill has not been experimentally evaluated, and no study cited here validates this exact AI tutor, this learner, Czech university materials, or these record thresholds. Much research uses short controlled tasks; reviews aggregate different populations, materials and comparison conditions. Mechanisms, population-average benefits, and a practical application to this vault are different levels of claim. AI-generated questions and feedback add unmeasured validity risks.

Full-text sections were accessible for the main interleaving, transfer, prior-knowledge, productive-failure, cognitive-load and learning-techniques reviews, the Bloom overview and Bloom experiment, the worked-example study, and formative-assessment/ZPD analyses. Some references were available only through publisher abstracts, indexed abstracts or research summaries: notably the classroom retrieval systematic review, self-explanation meta-analysis, feedback abstract, and some older memory/measurement papers. DOI requests and PubMed access were intermittently unavailable. No unavailable full text is represented as fully audited. The 2011 successive-relearning study is supported here by its bibliographic/abstract record and the authors' later review, not an audited reproduction of its protocol.

Validation: local deliverable links and fenced blocks pass; Ruby's YAML parser accepts the skill frontmatter and template schema blocks; separate checks confirm supported frontmatter fields, valid name/description lengths, no unfinished skill placeholders, the unchanged original checksum, and no per-course learner records. The bundled Python skill validator could not run because PyYAML is absent from both available Python environments; no dependency was installed for this document task. The walkthrough is a desk check, not a live tutoring trial. The existing vault checker still documents four pre-existing missing concept links, outside this task's scope.

No required input is missing. What remains unknown is actual learner performance, authoritative coverage of any selected course, and the effectiveness of these choices in use. Those should be established during future requested teaching, not invented during this review.
