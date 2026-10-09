---
course: Econometrics_II
course_id: 2026_2027/Winter_Semester/Econometrics_II
week: 1
sources:
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv
---

# Transport demand: regression and interpretation

How can a public-transport manager estimate how travel demand varies with ticket price? The first seminar moves from a research question to a regression model, hand calculations, alternative specifications, and assumption checks. The goal is to explain what the estimates mean and which conclusions the data can support, then present the analysis as a short empirical report. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF pp. 1–2]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=28|Lecture 1, PDF p. 28]]

Back to [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main#Week 1|Econometrics II — Week 1]]. [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions|OLS estimator and assumptions]] supplies the algebra; [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency|Unbiasedness, consistency, and efficiency]] explains the estimator properties that this exercise asks you to discuss.

**Status of the worked examples.** The handout gives questions and data, rather than an answer key. The choices, calculations, and diagnostic methods below are explicitly an agent-created worked solution to those questions. Numerical results were calculated from the ten printed cities and all 1,000 observations in the supplied CSV. They are not results printed in the lecture or seminar.

## From economic intuition to a model

Problem 1(i) asks about the sign and shape of demand and other influences. A plausible starting hypothesis is that a higher fare reduces public-transport use, holding relevant alternatives and service conditions fixed. A straight line imposes a constant change in demand per unit price; a curved or logarithmic relation would impose a different shape. The handout leaves the shape to discussion, so the linear model used below is a transparent choice for revising OLS, not a source-mandated demand law. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1, Problem 1(i)–(iii)]]

An initial specification is

$$
\text{travel}_i=\beta_0+\beta_1\text{price}_i+u_i.
$$

The slope is the change in the model's systematic travel demand associated with a one-unit increase in fare. The intercept is its value at zero fare. Other potential influences include city population and density, service frequency and quality, car availability, income, and the cost of driving. These are economic hypotheses offered to answer the prompt, not variables all observed in the supplied data. If such factors both affect demand and vary systematically with fare, putting them in $u_i$ can violate zero conditional mean. A negative estimated price coefficient alone therefore does not identify a causal demand curve. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1, Problem 1(i)–(ii)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=18|Lecture 1, PDF p. 18, exogeneity]]

The manager's ultimate objective is an optimal fare, but the exercise only estimates demand and evaluates the regression. Choosing an optimal fare would additionally require a defined objective, costs or capacity constraints, and a credible estimate of how fare changes affect demand. Those inputs are not supplied; no optimum is claimed here. This limitation follows from the distinction between the manager's motivating question and the tasks actually specified in Problem 1. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1]]

## Ten-city example: keep the source's measurement scale

The printed table labels the dependent variable “Passengers per hour (thousand)” and the fare “Fair price (dollars).” The values below preserve the printed numbers literally. The large passenger scale is not silently corrected. Thus a unit of $y$ means one unit on the table's stated thousand-passengers-per-hour scale, and a unit of price means one dollar. The later CSV has a different numeric scale and no supplied unit dictionary, so its results must not be assigned these table units automatically. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1, city table]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/seminar1_p1_ten_city_table.png]]

*Source crop: the original ten-city table, including its unit labels. It supplies the observations for the following calculations.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Source, PDF p. 1]]

### Estimate the line

For the ten cities, the calculated sample means and centered sums are

$$
\bar x=0.93,\qquad\bar y=1894,\qquad
S_{xx}=\sum_i(x_i-\bar x)^2=1.031,
$$

$$
S_{xy}=\sum_i(x_i-\bar x)(y_i-\bar y)=-3579.7.
$$

Applying the lecture's OLS formula gives

$$
\hat\beta_1=\frac{-3579.7}{1.031}=-3472.065955,
\qquad
\hat\beta_0=1894-(-3472.065955)(0.93)=5123.021339.
$$

Hence $\widehat{\text{travel}}_i=5123.021339-3472.065955\text{price}_i$. A fare difference of \$0.10 is associated with a fitted demand difference of $-347.206596$ units on the printed passenger scale. This is a cross-city association in the chosen linear specification. The estimated intercept is outside the observed fare range, \$0.50–\$1.50, and should not be interpreted as observed demand under a zero-fare policy. Calculations answer Problem 1(iii) using the source table and Lecture 1's centered estimator. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=15|Lecture 1, PDF p. 15]]

### Fitted values and residuals

For each city, calculate $\hat y_i$ from the fitted line and subtract it from actual travel: $\hat u_i=y_i-\hat y_i$. Positive residuals mean actual travel exceeds the line's prediction; negative residuals mean actual travel is lower. Rounded results are:

| City | Printed travel | Fare ($) | Fitted travel | Residual |
|---|---:|---:|---:|---:|
| $C_1$ | 2073 | 0.85 | 2171.765 | −98.765 |
| $C_2$ | 2136 | 0.75 | 2518.972 | −382.972 |
| $C_3$ | 1879 | 0.60 | 3039.782 | −1160.782 |
| $C_4$ | 938 | 1.00 | 1650.955 | −712.955 |
| $C_5$ | 7343 | 0.50 | 3386.988 | 3956.012 |
| $C_6$ | 838 | 0.85 | 2171.765 | −1333.765 |
| $C_7$ | 1648 | 1.00 | 1650.955 | −2.955 |
| $C_8$ | 739 | 0.75 | 2518.972 | −1779.972 |
| $C_9$ | 1071 | 1.50 | −85.078 | 1156.078 |
| $C_{10}$ | 275 | 1.50 | −85.078 | 360.078 |

The fitted line predicts negative travel at \$1.50, illustrating a limitation of this unrestricted linear specification even at an observed fare. The unusually high travel in $C_5$ also leaves a large positive residual. Neither observation licenses deleting a city; both motivate checking specification and omitted factors. This table is an agent calculation from the source observations, answering Problem 1(iv). [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1]]

### Disturbance variance, slope variance, and the t statistic

The true disturbances $u_i$ and their variance $\sigma^2$ are unknown. In a simple regression with an intercept, the conventional variance estimator uses $n-2$ residual degrees of freedom:

$$
\hat\sigma^2=\frac{\sum_i\hat u_i^2}{n-2}
=\frac{24{,}075{,}579.500}{8}
=3{,}009{,}447.437.
$$

Two estimated coefficients consume two degrees of freedom. Under the homoskedastic model, the slope's theoretical conditional variance is $\sigma^2/S_{xx}$; replacing the unknown $\sigma^2$ with $\hat\sigma^2$ estimates that variance. The corresponding calculated standard error is

$$
\widehat{\operatorname{Var}}(\hat\beta_1\mid X)=\frac{\hat\sigma^2}{1.031},
\qquad
\operatorname{se}(\hat\beta_1)=1708.496323.
$$

For $H_0:\beta_1=0$, $t=-3472.065955/1708.496323=-2.032235$. An exact two-sided test compares its absolute value with the appropriate $t_8$ critical value, under the full classical assumptions. At the conventional 5% level it does not reject zero: $|t|$ is below the approximately 2.306 critical value. This does not prove no relationship; ten observations and substantial residual variation leave considerable uncertainty. The formulas and computation are the worked solution to the handout's variance and $t$-statistic tasks, interpreted using the lecture's inference statement. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF pp. 1–2, Problem 1(iv)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=26|Lecture 1, PDF p. 26]]

## The CSV example: compare specifications

The supplied [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|travel.csv]] contains 1,000 rows and five numeric columns: `travel`, `price`, `income`, `gasoline`, and `u`; all 5,000 data cells are numeric and no entries are missing. No dictionary specifies their units, collection method, population, or generating equation. The column named `u` is retained in the raw data, but its name alone does not establish that it is an observed structural disturbance or a valid explanatory variable. The models below use the economically interpretable named controls `income` and `gasoline`, while preserving `u` as an undocumented column. This avoids treating unavailable real-world error information as an ordinary control. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 1(v)–(vi)]]

**Agent-computed model comparison.** Each model has an intercept, uses all 1,000 observations, and is estimated by OLS. Parentheses contain conventional homoskedastic standard errors, not heteroskedasticity-robust ones. Values remain in the CSV's own units.

| Term or statistic | (1) Price | (2) Price + income | (3) Price + income + gasoline |
|---|---:|---:|---:|
| Intercept | 989.829132 (8.768602) | 1054.376214 (2.778548) | 999.902291 (3.274125) |
| Price | −3.544463 (0.044685) | −2.708089 (0.016201) | −2.704248 (0.013120) |
| Income | — | −0.150823 (0.001544) | −0.150102 (0.001251) |
| Gasoline | — | — | 0.811474 (0.035433) |
| Observations | 1000 | 1000 | 1000 |
| $R^2$ | 0.863096 | 0.987044 | 0.991513 |
| Adjusted $R^2$ | 0.862959 | 0.987018 | 0.991488 |
| Estimated disturbance variance | 1522.184385 | 144.194430 | 94.549248 |

This comparison answers the seminar's request to present multiple specifications in a table; it is calculated from the CSV, rather than copied from a supplied answer key. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 1(vi)–(vii)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|CSV, all observations]]

### Interpret conditional associations carefully

In model (3), a one-file-unit increase in price is associated with approximately 2.704 fewer travel units, holding income and gasoline fixed. One additional income unit is associated with 0.150 fewer travel units, holding the other included variables fixed. One additional gasoline unit is associated with 0.811 more travel units. The negative price sign matches the starting hypothesis. A positive gasoline sign is compatible with more expensive driving making public transport relatively attractive. A negative income sign is compatible with substitution toward private transport as income rises, although this is a proposed mechanism, not a mechanism identified by these estimates. The dataset's unknown units prevent interpretation as dollars, percentages, or a particular number of passengers. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, interpretation prompt]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|Computed from travel.csv]]

The price slope becomes much less negative after income is included. The specifications answer different questions: model (1) summarizes unconditional price–travel association, whereas models (2) and (3) compare observations at the same included control values. The change is compatible with omitted-variable effects in the simple model; it does not prove that model (3) has zero conditional mean or that all relevant controls have been included. The model (3) slope $t$ statistics for zero null values are about $-206.11$, $-119.99$, and $22.90$ for price, income, and gasoline. Each is far from zero relative to its conventional standard error, so all three would be significant at ordinary levels under the maintained inference assumptions. Statistical significance still does not establish causal identification or economic importance in unspecified units. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 1(vii)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=26|Lecture 1, PDF p. 26]]

## Goodness of fit: R-squared and adjusted R-squared

Problem 2 asks for both measures. **Worked explanation:** with an intercept, define total sum of squares $\mathrm{SST}=\sum_i(y_i-\bar y)^2$ and residual sum of squares $\mathrm{SSE}=\sum_i\hat u_i^2$. The latter notation explicitly means residual, rather than explained, sum of squares here. OLS orthogonality gives the decomposition into fitted variation around the mean and residual variation. Therefore

$$
R^2=1-\frac{\mathrm{SSE}}{\mathrm{SST}}.
$$

For model (3), $\mathrm{SSE}=94{,}171.050600$ and $\mathrm{SST}=11{,}096{,}411.524222$, so $R^2=0.991513$. The fitted model accounts for approximately 99.1513% of the sample variation in travel around its mean. This is a description of sample fit; it is not a statement that the included variables causally explain that share, nor a guarantee of performance on new data. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 2]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|Computed from travel.csv]]

Adding regressors to the same OLS sample cannot increase the minimized SSE: the original model remains available by setting each new coefficient to zero. Thus $R^2$ cannot decrease merely because more regressors were allowed. Adjusted $R^2$ accounts for residual degrees of freedom:

$$
\bar R^2
=1-\frac{\mathrm{SSE}/(n-k-1)}{\mathrm{SST}/(n-1)}
=1-(1-R^2)\frac{n-1}{n-k-1},
$$

where $k$ counts nonconstant regressors. It can fall if the reduction in SSE is too small to compensate for the additional parameters, and can be negative for a poorly fitting model. Comparisons should use the same dependent variable and observations. Here both fit measures rise across the three specifications, but that alone cannot determine whether a coefficient has a causal interpretation. For the ten-city regression, $R^2=0.340477$ and adjusted $R^2=0.258037$; these are separate results from a separate dataset. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 2]]

## Assumption checks: what diagnostics can establish

Problem 3 requests plots and formal tests of residual normality and homoskedasticity. The following agent-selected diagnostic methods implement that open-ended instruction for model (3). They are not named in the handout. Tests are interpreted at a stated 5% significance level and use large-sample reference distributions; failing to reject is evidence of compatibility, not proof of an assumption. Residuals estimate disturbances and are constrained by OLS fitting, so tests based on them require their own statistical justification. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 3]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/travel_full_model_diagnostics.png]]

*Agent-computed diagnostic plots from all CSV observations for the price–income–gasoline model. The histogram is roughly symmetric; the normal Q–Q plot compares sorted standardized residuals with standard-normal quantiles (red diagonal). Residuals against fitted values show no conspicuous funnel. Squared residuals show the remaining spread more directly. These are calculated visual evidence, not figures in the supplied PDF.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|Data: travel.csv]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Task: Seminar 1, PDF p. 2]]

### Normality: a plot and a moment test

A Q–Q plot matches ordered standardized residuals to normal quantiles: an approximately straight diagonal is compatible with a normal shape, while curvature and tail departures indicate shape differences. The displayed residual histogram is broadly bell-shaped, and the Q–Q points lie near the diagonal, with some tail departures. Neither visual establishes exact conditional normality.

For a formal check, the Jarque–Bera statistic compares sample skewness $S$ and kurtosis $K$ with their normal-distribution values of zero and three. Using centered residual moments $m_r=n^{-1}\sum_i\hat u_i^r$, set $S=m_3/m_2^{3/2}$ and $K=m_4/m_2^2$. Residual means are zero apart from numerical rounding because the model has an intercept. The statistic is

$$
\mathrm{JB}=n\left(\frac{S^2}{6}+\frac{(K-3)^2}{24}\right).
$$

Under the usual large-sample conditions and a normal null, its reference distribution is $\chi^2_2$. Here $S=0.031493$, $K=3.051706$, $\mathrm{JB}=0.276697$, and the asymptotic $p$ value is $0.870795$. We do not reject normality at 5%. This is a selected moment-based check, not proof of all aspects of conditional normality. These definitions and results are the agent's worked method for the source's requested normality test. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 3]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|Calculated from travel.csv]]

### Homoskedasticity: a spread plot and an auxiliary regression

Homoskedasticity means constant conditional disturbance variance. A widening or narrowing residual band against fitted values would raise concerns, while roughly similar spread is compatible with constant variance. The plots show no obvious systematic funnel, but a single projection can miss variance patterns associated with individual regressors.

For a formal check, use an auxiliary regression of squared residuals on an intercept and the three included regressors. The studentized Breusch–Pagan / Koenker form tests whether those regressors explain residual variance. If its $R^2$ is $R^2_{\mathrm{aux}}$, its statistic is $\mathrm{LM}=nR^2_{\mathrm{aux}}$, with a large-sample $\chi^2_3$ reference under the homoskedastic null and the usual independent-sampling and moment conditions. The three degrees of freedom count the nonconstant auxiliary regressors.

Here $R^2_{\mathrm{aux}}=0.004737882$, $\mathrm{LM}=4.737882$, and $p\approx0.192028$. We do not reject homoskedasticity at 5% against this particular alternative. A different auxiliary specification could detect different variance patterns. This is the agent-selected solution method for the handout's homoskedasticity task, rather than a theorem or test named by the handout. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 3]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/travel.csv|Calculated from travel.csv]]

### Assumptions that remain substantive

The sample design matrix can be checked for full rank; the three CSV specifications have full rank and hence unique OLS coefficients. Functional form remains a modeling choice. The file alone does not document random sampling or representativeness, and residual orthogonality cannot verify population exogeneity. Adding controls may improve a plausible specification, but omitted causes, simultaneity, or measurement error could still invalidate the desired interpretation. Passing residual diagnostics therefore does not prove OLS unbiasedness, consistency, or causality. Those properties follow from the conditions developed in [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency|Unbiasedness, consistency, and efficiency]], not from a high $R^2$. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=18|Lecture 1, PDF p. 18]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problems 1(v), 3]]

## Turn the analysis into a short report

A report should state the research question, define variables and known units, justify the specification, describe the observations, show a readable regression table, interpret coefficient magnitudes and uncertainty, explain fit and diagnostic results, and identify the assumptions that remain unsupported. For this exercise, the numerical contrast between simple and multiple regression is central: the estimated price association changes when income is held fixed. The important limitation is equally central: no documented sampling process, structural-error definition, or unit dictionary is supplied for the CSV. The exercise develops empirical reasoning, while the source leaves those provenance details unspecified. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, model comparison and interpretation]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=11|Lecture 1, PDF p. 11, empirical-analysis goals]]
