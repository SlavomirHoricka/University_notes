---
course: Econometrics_II
course_id: 2026_2027/Winter_Semester/Econometrics_II
week: 2
sources:
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf
---

# Static and finite distributed lag models

Does a change in an explanatory variable affect the outcome immediately, over several later periods, or both? A static time-series model represents a contemporaneous relationship. A finite distributed lag (FDL) model lets the adjustment unfold over a specified number of periods. Distinguishing a temporary pulse from a permanent change is essential: a coefficient describes the response at one lag, while a sum of coefficients describes the eventual response to a maintained change. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=22|Lecture 2, PDF pp. 22–24]]

Back to [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main#Week 2|Econometrics II — Week 2]]. These specifications can be estimated by OLS, but [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Time_Series_OLS_and_Strict_Exogeneity|Time-series OLS and strict exogeneity]] explains the assumptions needed for unbiasedness and inference. Model coefficients are not automatically causal effects.

## A static contemporaneous model

The lecture's static specification is

$$
y_t=\beta_0+\beta_1z_t+u_t,\qquad t=1,\ldots,T.
$$

Here $z_t$ is the explanatory variable at the same date as outcome $y_t$, and $u_t$ collects other influences. The coefficients are time-invariant. Holding the disturbance unchanged, a change in $z$ gives $\Delta y_t=\beta_1\Delta z_t$; the contemporaneous slope has units of outcome per unit of $z$. This is the source's comparison with $\Delta u_t=0$. It does not say that real observed outcomes change only because of $z$, or that disturbances necessarily stay fixed between successive calendar dates. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=22|Lecture 2, PDF p. 22]]

The source's demand example is $D_t=\beta_0+\beta_1Price_t+u_t$, a same-period tradeoff between consumption and price. The specification assumes that the intercept and slope do not change over time. Whether price is exogenous is an additional question: writing a demand equation does not establish that price changes independently of unobserved demand influences. This qualification connects the example to the source's TS2 requirement. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=22|Lecture 2, PDF p. 22]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=11|Strict exogeneity, PDF p. 11]]

## An FDL model spreads adjustment across dates

For lag order $q$, write

$$
y_t=\alpha_0+\delta_0z_t+\delta_1z_{t-1}+\cdots+\delta_qz_{t-q}+u_t.
$$

The lagged variable $z_{t-j}$ is the value $j$ periods earlier. There are $q$ lagged values plus the current value, so an FDL of order two has three slope coefficients. Each $\delta_j$ has units of $y$ per unit of $z$ and describes the model's date-$t$ response to a change in the value of $z$ at date $t-j$, holding the other included values and disturbances fixed. The period is set by data frequency: one lag in monthly data means one month. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=23|Lecture 2, PDF pp. 23, 25]]

Wooldridge likewise treats the static model as current-value-only and the FDL as a current value plus a finite set of earlier values. Its fertility example makes the lag rationale explicit: biological and behavioral decisions can delay the response of births to the tax value of a child. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=374|Wooldridge, 5th ed., PDF p. 374 (printed p. 346)]]

Constructing lags requires earlier observations. If the available raw series begins at date 1 and no earlier $z$ is supplied, a model with $q$ lags can first use date $q+1$. Its estimation sample length is the number of usable rows, not automatically the original series length. This is an agent bookkeeping implication of the displayed indices, relevant when using $T-k-1$ degrees of freedom from the OLS note. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=23|Lecture 2, PDF p. 23]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=18|Residual degrees of freedom, PDF p. 18]]

## A temporary pulse and a permanent step

**Agent derivation of the source's response interpretation.** Compare two regressor paths that share the same disturbance path and all other model inputs. With a one-unit temporary pulse at date $s$, $\Delta z_s=1$ and $\Delta z_t=0$ at all other dates. Substituting in the FDL gives

$$
\Delta y_{s+h}=\delta_h\quad(0\le h\le q),
\qquad
\Delta y_{s+h}=0\quad(h>q).
$$

The **impact propensity** is $\delta_0$, the immediate response. The date-$s+1$ response is $\delta_1$, and so on. From $q+1$ periods onward the pulse has left every included regressor position, so it has no further response in this finite-lag specification. This conclusion is a model implication, not a guarantee about an economic system whose effects might last longer than the chosen lag order. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=23|Lecture 2, PDF p. 23, temporary increase]]

For a permanent one-unit increase starting at $s$, $\Delta z_t=1$ for every $t\ge s$. At the first date only the current regressor has changed. One period later both the current and first-lag regressor have changed. Continuing this substitution gives

$$
\Delta y_{s+h}=\sum_{j=0}^{\min(h,q)}\delta_j,
\qquad
LRP=\sum_{j=0}^{q}\delta_j.
$$

The **long-run propensity** (LRP) is the final level difference once all included lags carry the maintained change. It is not the effect in the first period, nor an estimate of a percentage change unless the model's units or transformations justify that interpretation. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=23|Lecture 2, PDF p. 23, permanent increase]]

For order two, the contrast is:

| Period relative to change | Temporary one-unit pulse | Permanent one-unit increase |
|---|---|---|
| $s$ | $\delta_0$ | $\delta_0$ |
| $s+1$ | $\delta_1$ | $\delta_0+\delta_1$ |
| $s+2$ | $\delta_2$ | $\delta_0+\delta_1+\delta_2$ |
| $s+3$ and later | $0$ | $\delta_0+\delta_1+\delta_2$ |

*Agent-created table derived from the order-two equation and temporary/permanent comparisons on Lecture 2, PDF p. 23.* For example, hypothetical coefficients $(2,0.5,-0.5)$ give pulse responses $(2,0.5,-0.5,0,\ldots)$ and step responses $(2,2.5,2,2,\ldots)$. A negative later response can offset part of an initial increase, so a large impact propensity does not require an equally large long-run propensity. These numbers are an illustration, not an estimated course result. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=23|Source model, PDF p. 23]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/textbook_ch10_printed347_lag_distribution.png]]

*Source Figure 10.1: an illustrative lag distribution, with the largest pulse response at lag 1 and a zero response after lag 2. The horizontal axis is lag, and the vertical axis is a coefficient, not a measured outcome series. The diagram is schematic and contains no numerical coefficient estimates.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=375|Wooldridge, 5th ed., PDF p. 375 (printed p. 347)]]

The textbook's explicit substitutions for a temporary pulse and maintained step give the same response sequences as the table above. Whether an economic response really ends after the chosen number of lags remains an empirical specification question. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=375|Wooldridge, 5th ed., PDF p. 375 (printed p. 347)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=376|Wooldridge, 5th ed., PDF p. 376 (printed p. 348)]]

## A static model is a special case, with a source caveat

Setting **only the lag coefficients** $\delta_1,\ldots,\delta_q$ to zero leaves $y_t=\alpha_0+\delta_0z_t+u_t$, the static model. The arrows on p. 24 show zeros under the lagged terms. Its accompanying text, however, says to set $\delta_0,\delta_1,\ldots,\delta_q$ to zero. Taken literally, that also removes the contemporaneous regressor and leaves an intercept-only model. The static-model definition on p. 22 and the p. 24 arrows support retaining $\delta_0$; the inconsistent source wording is explicitly recorded here. Wooldridge states the special case unambiguously by setting $\delta_1,\ldots,\delta_q$ to zero while retaining the current-value coefficient. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=376|Wooldridge, 5th ed., PDF p. 376 (printed p. 348)]] [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=24|Lecture 2, PDF p. 24]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=22|Static definition, PDF p. 22]]

Values of $z$ at nearby dates are often strongly correlated. This can make the individual $\delta_j$ estimates imprecise, because there is little independent variation to distinguish their contributions. Substantial lag correlation is imperfect multicollinearity; exact dependence violates full rank. The distinction follows the multiple-regression variance denominator $SST_j(1-R_j^2)$ in the OLS note. Adding lags is therefore an economic modeling choice with a precision cost, not a mechanical way to improve identification. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=24|Lecture 2, PDF p. 24, lag correlation]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=18|Variance theorem, PDF p. 18]]

### Precision of the long-run sum

Imprecise individual lag estimates do not imply that their sum is equally imprecise. In the textbook's annual fertility illustration (United States, 1913–1984; 70 usable rows after two lags), the coefficients on current and lagged real personal-exemption values are approximately $0.073$, $-0.0058$, and $0.034$. Their individual standard errors are large, but their estimated sum is about $0.101$ births per 1,000 women of childbearing age per dollar, with standard error $0.030$. The source reports a 95% interval of approximately $0.041$ to $0.160$, conditional on its maintained model. This is a textbook result, not a recomputed result from a supplied dataset. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=386|Wooldridge, 5th ed., PDF p. 386 (printed p. 358)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=387|Wooldridge, 5th ed., PDF p. 387 (printed p. 359)]]

To see why separate standard errors are insufficient, an agent expansion of the variance-of-a-sum identity gives

$$
\operatorname{Var}(\widehat{LRP}\mid X)
=\sum_{j=0}^q\operatorname{Var}(\hat\delta_j\mid X)
+2\sum_{j<\ell}\operatorname{Cov}(\hat\delta_j,\hat\delta_\ell\mid X).
$$

The coefficient covariances are needed. The book obtains the sum's standard error by reparameterizing an order-two model with $\theta=\delta_0+\delta_1+\delta_2$:

$$
y_t=\alpha_0+\theta z_t
+\delta_1(z_{t-1}-z_t)+\delta_2(z_{t-2}-z_t)+u_t.
$$

This follows by substituting $\delta_0=\theta-\delta_1-\delta_2$. A regression on these transformed columns estimates the same model, with the coefficient on $z_t$ directly equal to the LRP and its reported standard error attached to that sum. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=386|Wooldridge, 5th ed., PDF p. 386 (printed p. 358)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=387|Wooldridge, 5th ed., PDF p. 387 (printed p. 359)]]

## The EET restaurant-price example

The lecture asks whether electronic sales reporting (EET), introduced to reduce tax evasion, affects restaurant prices. It proposes monthly restaurant-price-index data from the Czech Statistical Office and a four-lag model:

$$
priceindex_t=\alpha_0+\delta_0EET_t+\delta_1EET_{t-1}
+\delta_2EET_{t-2}+\delta_3EET_{t-3}+\delta_4EET_{t-4}+u_t.
$$

The source gives no dataset, coefficient estimates, exact variable coding, or identification design. **Conditional coding explanation:** if $EET_t$ is a zero/one indicator for an active regime, a maintained switch from zero to one has immediate model difference $\delta_0$ and final difference $\delta_0+\cdots+\delta_4$, in price-index points. Other influences on prices remain in $u_t$, so this response becomes a causal policy effect only with a defensible exogeneity/specification argument. A fitted intervention model alone cannot establish that argument. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=25|Lecture 2, PDF p. 25]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=11|Exogeneity requirement, PDF p. 11]]

A price index needs a base period and base value: an index-point change is different from a percentage change or a currency-unit change. For positive index values, the percentage change from date $a$ to $b$ is $100(I_b/I_a-1)$. The slide does not specify the restaurant index's base. This brief index clarification is supplied by the textbook and prevents treating the displayed coefficient as a price change in crowns or as a percentage by default. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=388|Wooldridge, 5th ed., PDF p. 388 (printed p. 360)]]

**Source-context boundary:** p. 25 states introduction in December 2016, cancellation on January 1, 2023, and reintroduction on January 1, 2027. These are the lecture's policy-context statements; their current legal/calendar accuracy was not independently verified against an authorized external source. They must not be used as confirmed current policy facts. The econometric exercise does not require accepting the claimed future date. No external media or statistical-office link was opened during this ingestion. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=25|Lecture 2, PDF p. 25, opening paragraph]]

## A visual motivation for lagged response

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p35_cases_and_hospital_patients.png]]

*Original embedded image from Lecture 2, PDF p. 35. Upper panel: daily newly confirmed COVID-19 cases **per million people** in Czechia; lower panel: the **number of patients in hospital**. Both cover dates in early 2022. The upper panel explicitly warns that limited testing means confirmed cases undercount infections; the original source/credit text is preserved.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=35|Lecture 2, PDF p. 35]]

The source places these plots under “Lagged effects.” The waves appear at different stages, motivating a model in which an explanatory series can precede an outcome response. The units differ, and hospital occupancy is not a count of newly admitted patients; comparing peak heights is therefore not a response coefficient. The image supplies neither an estimated lag length nor an FDL fit, and its timing alone does not identify causation. It illustrates why immediate-only specifications may miss dynamics. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=35|Lecture 2, PDF p. 35, both panels]]

## What to retain

A static model contains the current explanatory variable; an FDL additionally contains its lags. Read $\delta_j$ as the date-$j$ response to a temporary unit pulse, and read their sum as the final response to a permanent unit step, under the model and held-fixed disturbance comparison. Strong correlation between lags affects precision; assumptions about disturbances determine whether these modeled comparisons support unbiased or causal interpretation. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=23|Lecture 2, PDF pp. 23–25]]
