---
course: Econometrics_II
course_id: 2026_2027/Winter_Semester/Econometrics_II
week: 2
sources:
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf
---

# Time-series OLS and strict exogeneity

What changes when observations describe successive dates rather than independently sampled people or firms? The OLS calculation remains the same, but temporal dependence changes the assumptions needed to interpret it. Week 2 builds a finite-sample time-series assumption ladder: strict exogeneity for unbiasedness, a spherical conditional error covariance matrix for conventional variances and BLUE, and normality for exact inference. The lecture introduces these results before later lectures relax their restrictive assumptions. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=3|Lecture 2, PDF pp. 3–7, 21]]

Back to [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main#Week 2|Econometrics II — Week 2]]. [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions|OLS estimator and assumptions]] explains the calculation and matrix notation; [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency|Unbiasedness, consistency, and efficiency]] distinguishes the properties whose time-series versions are developed here.

## Temporal ordering and a stochastic process

For cross-sectional observations, the index $i=1,\ldots,n$ distinguishes sampled units. For a time series, $t=1,\ldots,T$ distinguishes ordered periods. The model $y_t=\beta_0+\beta_1x_t+u_t$ looks like its cross-sectional counterpart, but rearranging the dates changes the meaning of lags and dynamics. The lecture treats the observed sequence as one realization of a **stochastic process**, a collection of random variables indexed by time. Random does not mean independently sampled: an unpredictable sequence can still have dependence across dates. The independence available under the cross-sectional random-sampling assumption is therefore not assumed here. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=4|Lecture 2, PDF pp. 4–7]]

The display $u_t\sim N(0,\sigma^2)$ on p. 4 describes a marginal distribution, not a complete joint distribution over time. By itself it does not establish that disturbances at different dates are independent or that they are independent of regressors. The later TS assumptions state these restrictions separately. This is an agent clarification of the contrast between the opening model and pp. 11, 16, and 19. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=4|Lecture 2, PDF p. 4]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=16|Lecture 2, PDF pp. 16–19]]

## The first three assumptions

Use the numbering in this lecture, which differs from both the Week 1 MLR list and the supplied textbook. In particular, **TS2 is strict exogeneity and TS3 is no perfect collinearity**. Let $x_t=(x_{t1},\ldots,x_{tk})$ collect the $k$ nonconstant regressors at date $t$, and let $X$ contain their values at every sample date plus an intercept column. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=10|Lecture 2, PDF pp. 10–12]]

| Assumption | Formal statement and meaning |
|---|---|
| TS1: linear in parameters | $y_t=\beta_0+\sum_{j=1}^k\beta_jx_{tj}+u_t$. Equivalently, $y=X\beta+u$, where $y,u$ are $T\times1$, $X$ is $T\times(k+1)$, and $\beta$ is $(k+1)\times1$. |
| TS2: zero conditional mean / strict exogeneity | $E[u_t\mid X]=0$ for every $t$. The mean of the date-$t$ disturbance is zero conditional on the entire regressor history in the sample, including future dates. |
| TS3: no perfect collinearity | $\operatorname{rank}(X)=k+1$. No nonconstant regressor is constant or an exact linear combination of the other columns; the intercept itself is intentionally constant. This makes $X'X$ invertible. |

The textbook reverses the deck's TS2/TS3 labels: **book TS.2 is no perfect collinearity, book TS.3 is strict exogeneity**. Names and formulas therefore matter more than bare numbers. The remaining assumption names correspond. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=378|Wooldridge, 5th ed., PDF p. 378 (printed p. 350)]]

These statements unpack the displayed equations and rank condition; $T$ is used consistently for sample length even where the slides alternate $n$ and $T$. There is no replacement assumption that observations themselves are independent. Strict exogeneity restricts regressor–disturbance relationships; it does not rule out all temporal dependence in $x_t$ or $y_t$. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=10|Lecture 2, PDF pp. 10–13]]

### Strict versus contemporaneous exogeneity

**Contemporaneous exogeneity** requires only

$$
E[u_t\mid x_t]=0.
$$

It conditions on the regressors at the same date. TS2 instead requires $E[u_t\mid x_1,\ldots,x_T]=0$. With finite relevant moments, TS2 implies that $u_t$ has zero covariance with each included regressor at every sample date $s$, including $s\ne t$. It is stronger than those covariance restrictions: zero conditional mean is not merely a statement about linear correlation. Contemporaneous zero conditional mean gives no comparable guarantee about past or future regressors. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=9|Lecture 2, PDF pp. 9–11]]

Under independent cross-sectional sampling, an observation's disturbance and regressors are independent of the other sampled observations. This lets $E[u_i\mid x_i]=0$ imply $E[u_i\mid X]=0$. A time series has no such sampling guarantee: an unexpected shock today may help determine a regressor tomorrow. The lecture therefore imposes the full-design condition explicitly. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=9|Lecture 2, PDF p. 9]]

The textbook gives an economic feedback example: a city's murder-rate disturbance can influence how many police officers it hires in the following year. Even if current police numbers are uncorrelated with the current disturbance, future police numbers can react to today's unexpected murder-rate change, violating strict exogeneity. Adding past explanatory variables does not automatically remove feedback to future values. This explains why policy variables chosen in response to past outcomes need particular scrutiny. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=379|Wooldridge, 5th ed., PDF p. 379 (printed p. 351)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=380|Wooldridge, 5th ed., PDF p. 380 (printed p. 352)]]

## Why strict exogeneity gives unbiasedness

Under TS1 and TS3, OLS satisfies

$$
\hat\beta=(X'X)^{-1}X'y
=\beta+(X'X)^{-1}X'u.
$$

Conditional on $X$, the matrix multiplying $u$ is fixed. Taking conditional expectation and applying TS2 gives

$$
E[\hat\beta\mid X]
=\beta+(X'X)^{-1}X'E[u\mid X]
=\beta.
$$

Taking expectation again yields $E[\hat\beta]=\beta$, when the relevant expectations exist. This is an agent matrix expansion of the source's scalar proof and matrix theorem. For simple regression its error term is $\sum_t(x_t-\bar x)u_t/\sum_t(x_t-\bar x)^2$; every weight is fixed only after conditioning on all of $X$, which is exactly why same-date exogeneity is insufficient for this proof. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=8|Lecture 2, PDF pp. 8–13]]

TS1–TS3 establish finite-sample conditional unbiasedness without homoskedasticity, no serial correlation, or normality. The lecture warns that failing strict exogeneity can produce bias even with contemporaneous exogeneity. Read this as loss of the unbiasedness guarantee: failure of a sufficient condition does not logically prove that every coefficient in every special design is biased. Nor does failure of this finite-sample result settle consistency; the lecture assigns large-sample issues to the next week. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=13|Lecture 2, PDF pp. 11, 13, 31]]

## Two additional assumptions for conventional variance

TS4 requires $\operatorname{Var}(u_t\mid X)=\sigma^2$ for each date: the conditional variance is constant over time and does not depend on any sample-date regressors. TS5 requires $\operatorname{Cov}(u_t,u_s\mid X)=0$ for $t\ne s$; the slide writes the equivalent zero-correlation condition when variances are positive. Nonzero covariance across dates is **serial correlation**, also called autocorrelation. These are different restrictions: constant variance does not make cross-date covariances zero. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=15|Lecture 2, PDF pp. 15–17]]

Together they give the $T\times T$ covariance matrix

$$
\operatorname{Var}(u\mid X)=\sigma^2 I_T.
$$

Every diagonal element is the same variance and every off-diagonal element is zero. The lower matrix on source p. 17 omits the conditioning symbol; the text and upper equation explicitly condition on $X$, which is the interpretation used here. Under TS2 and constant conditional variance, the law of total variance also gives $\operatorname{Var}(u_t)=\sigma^2$, explaining the unconditional equality printed on p. 15. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=17|Lecture 2, PDF pp. 15, 17]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p17_error_covariance_matrix.png]]

*Source crop: Lecture 2, PDF p. 17. Equal diagonal entries express homoskedasticity; zero off-diagonal entries express no conditional serial correlation. The matrix concerns disturbances, not an assertion that regressors at different dates are uncorrelated.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=17|Source, PDF p. 17]]

### The covariance terms hidden in the simple-slope proof

Define $S_{xx}=\sum_t(x_t-\bar x)^2$ and $a_t=(x_t-\bar x)/S_{xx}$. Conditional on $X$, the slope error is $\sum_t a_tu_t$. Expanding its variance gives

$$
\operatorname{Var}(\hat\beta_1\mid X)
=\sum_t a_t^2\operatorname{Var}(u_t\mid X)
+2\sum_{t<s}a_ta_s\operatorname{Cov}(u_t,u_s\mid X).
$$

TS5 removes the second sum. TS4 then replaces each variance by $\sigma^2$, leaving

$$
\operatorname{Var}(\hat\beta_1\mid X)
=\frac{\sigma^2\sum_t(x_t-\bar x)^2}{S_{xx}^2}
=\frac{\sigma^2}{S_{xx}}.
$$

This expansion supplies the intermediate justification requested by p. 14. More regressor variation reduces slope uncertainty under these conditions. Serial correlation need not destroy unbiasedness under TS1–TS3, but its covariance terms invalidate this simplified variance formula. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=14|Lecture 2, PDF pp. 14–18]]

## Multiple-regression precision, residual variance, and BLUE

Under TS1–TS5,

$$
\operatorname{Var}(\hat\beta\mid X)=\sigma^2(X'X)^{-1},
\qquad
\operatorname{Var}(\hat\beta_j\mid X)=
\frac{\sigma^2}{SST_j(1-R_j^2)},\quad j=1,\ldots,k.
$$

Here $SST_j=\sum_t(x_{tj}-\bar x_j)^2$. The auxiliary-regression $R_j^2$ comes from regressing regressor $j$ on an intercept and the other explanatory variables; it is not the $R^2$ of the original outcome regression. The product $SST_j(1-R_j^2)$ is variation in regressor $j$ left after the other regressors explain it. When that independent variation is small, separating coefficient $j$ is imprecise. Perfect collinearity makes it zero and violates TS3; substantial but imperfect correlation raises variance without itself creating bias. The matrix formula is an agent derivation from the source's covariance matrix and scalar theorem. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=18|Lecture 2, PDF pp. 17–18]]

Let $\hat u_t=y_t-\hat y_t$ and define the residual sum of squares $SSR=\sum_t\hat u_t^2$. The source uses $SSR$ for this residual quantity. With $k$ nonconstant regressors plus an intercept,

$$
\hat\sigma^2=\frac{SSR}{T-k-1}
$$

is unbiased for $\sigma^2$ under TS1–TS5. The denominator is residual degrees of freedom, not $T$, because $k+1$ coefficients have been estimated. Substituting $\hat\sigma^2$ in the coefficient variance formula and taking its square root gives the conventional estimated standard error. These variance estimates require the assumptions used in deriving them; a regression program printing a standard error does not verify those assumptions. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=18|Lecture 2, PDF p. 18, Theorems 2–3]]

The same assumptions yield the time-series Gauss–Markov theorem: OLS is **best linear unbiased conditional on $X$**. Linear means linear in the observed outcomes with weights determined by $X$; best means smallest conditional variance in the linear-unbiased comparison class. It is not a comparison with every possible biased or nonlinear estimator. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=18|Lecture 2, PDF p. 18, Theorem 4]]

## Normality and exact finite-sample inference

TS6 states that disturbances are independent of $X$ and independently and identically distributed as $N(0,\sigma^2)$. Together with linearity and full rank this makes $\hat\beta\mid X$ normal. The source's full TS1–TS6 list yields exact null $t$ and $F$ distributions. For one coefficient and null value $\beta_{j,0}$,

$$
t_j=\frac{\hat\beta_j-\beta_{j,0}}{\operatorname{se}(\hat\beta_j)}
\sim t_{T-k-1}\quad\text{under }H_0.
$$

Joint tests compare multiple restrictions using an $F$ statistic. The displayed $t$ formula and degrees of freedom are an agent expansion of Theorem 5, using the residual degrees of freedom supplied on p. 18. Normality adds an exact-distribution conclusion; it was not required for the preceding unbiasedness or BLUE results. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=19|Lecture 2, PDF pp. 18–20]]

**Source numbering error.** Page 19 says “TS6 implies TS3–TS5.” In this deck TS3 is full rank (p. 12), which cannot follow from a distributional assumption on disturbances: two identical regressor columns remain identical even with independent normal errors. TS6 does imply the source's zero-conditional-mean, constant-variance, and no-serial-correlation conditions (TS2, TS4, TS5), but TS3 must be checked separately. The supplied textbook resolves the origin of this discrepancy: its corresponding statement is correct because **book TS.3 is strict exogeneity**, while the deck assigned that name to TS2. Thus the implication survives by name, but the deck's copied number range does not. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=383|Wooldridge, 5th ed., PDF p. 383 (printed p. 355)]] [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=19|Lecture 2, PDF p. 19, last line]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=12|TS3 definition, PDF p. 12]]

Chapter 11 clarifies the boundary without changing the Week 2 theorem: with the book's suitable weak-dependence, linear-model and full-rank conditions, contemporaneous exogeneity can yield **consistency without finite-sample unbiasedness**. Weak dependence means sufficiently limited dependence at widely separated dates for the relevant limit arguments. This is contextual support for why the next lecture relaxes strict exogeneity, not a complete treatment of next-week asymptotic theory. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=412|Wooldridge, 5th ed., PDF p. 412 (printed p. 384)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=413|Wooldridge, 5th ed., PDF p. 413 (printed p. 385)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=414|Wooldridge, 5th ed., PDF p. 414 (printed p. 386)]]

## What the assumption ladder establishes

TS1–TS3 provide a conditional-unbiasedness guarantee. TS4–TS5 justify conventional variances, unbiased residual-variance estimation, and conditional BLUE. TS6 supplies exact finite-sample normal and null-test distributions. Strict exogeneity and no serial correlation are restrictive in many social-science time series; the lecture does not claim they hold automatically. Its next-week preparation is Chapter 11 and revision of expected value, variance, covariance, and large-sample OLS properties. The supplied Fifth Edition places Chapter 10 at printed pp. 344–379 (PDF pp. 372–407) and Chapter 11 at printed pp. 380–411 (PDF pp. 408–439), rather than the different-edition page ranges on slide p. 2. Chapter 10 supports these same explanations. Chapter 11 remains next-week reading; only passages directly needed to clarify the current assumption boundary were used, and the linked video was not opened. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=21|Lecture 2, PDF pp. 21, 31]]
