---
course: Econometrics_II
course_id: 2026_2027/Winter_Semester/Econometrics_II
week: 1
sources:
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf
---

# Unbiasedness, consistency, and efficiency

What does it mean for an econometric estimator to be reliable? Week 1 distinguishes three questions: whether its repeated-sample average equals the population parameter, whether it approaches that parameter as the sample grows, and whether it is as precise as other estimators in a specified class. A single observed coefficient cannot answer these questions on its own. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=16|Lecture 1, PDF pp. 16–24]]

Back to [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main#Week 1|Econometrics II — Week 1]]. The notation and assumptions are developed in [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions|OLS estimator and assumptions]].

## One decomposition drives both proofs

For $y_i=\beta_0+\beta_1x_i+u_i$, centering gives $y_i-\bar y=\beta_1(x_i-\bar x)+(u_i-\bar u)$. Substitute this into the OLS numerator:

$$
\begin{aligned}
\hat\beta_1
&=\frac{\sum_i(x_i-\bar x)[\beta_1(x_i-\bar x)+(u_i-\bar u)]}{S_{xx}}\\
&=\beta_1+\frac{\sum_i(x_i-\bar x)(u_i-\bar u)}{S_{xx}}\\
&=\beta_1+\frac{\sum_i(x_i-\bar x)u_i}{S_{xx}}.
\end{aligned}
$$

The final step uses $\sum_i(x_i-\bar x)=0$, so subtracting $\bar u$ changes nothing. This algebra identifies the estimation error: sample co-movement between the regressor and disturbance, divided by sample regressor variation. The lecture uses the uncentered-disturbance version for unbiasedness and the centered version for consistency. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=19|Lecture 1, PDF p. 19]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=22|Lecture 1, PDF p. 22]]

## Unbiasedness: the repeated-sample average

An estimator is unbiased when $E[\hat\beta_j]=\beta_j$. Expectation refers to repeated sampling from the population under the model, not to averaging different coefficients from a single fitted regression. The lecture's theorem states that the linear-in-parameters, random-sampling, no-perfect-collinearity, and zero-conditional-mean assumptions imply unbiasedness for all OLS coefficients. Homoskedasticity and normality are not required for this result. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=16|Lecture 1, PDF pp. 16–18]]

To see the role of exogeneity, condition on the observed regressor sample $X=(x_1,\ldots,x_n)$. Then $S_{xx}$ and the weights $x_i-\bar x$ are fixed. Linearity of conditional expectation gives

$$
E[\hat\beta_1\mid X]
=\beta_1+\frac{1}{S_{xx}}\sum_{i=1}^n(x_i-\bar x)E[u_i\mid X]
=\beta_1.
$$

The zero-conditional-mean assumption, together with random sampling, supplies $E[u_i\mid X]=0$. Taking expectation again gives $E[\hat\beta_1]=E[E[\hat\beta_1\mid X]]=\beta_1$. Linearity of the model supplies the initial decomposition; no perfect collinearity makes the denominator positive; random sampling supports the move from observation-level exogeneity to conditioning on the full sample design. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=19|Lecture 1, PDF p. 19, conditional-expectation derivation]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p19_unbiasedness_derivation.png]]

*Source crop: Lecture 1, PDF p. 19. The weights and denominator can leave the conditional expectation because $X$ is held fixed; exogeneity makes the remaining conditional disturbance means zero.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=19|Source, PDF p. 19]]

Unbiasedness means there is no systematic overestimation or underestimation across repeated samples. It does not guarantee that the estimate from a particular sample is close to the truth: dispersion can be large even when its center is correct. That is why precision and consistency are separate questions. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=17|Lecture 1, PDF p. 17]]

## Consistency: concentration as sample size grows

Consistency is convergence in probability: $\hat\beta_{j,n}\xrightarrow{p}\beta_j$. More explicitly, for every fixed tolerance $\varepsilon>0$,

$$
\lim_{n\to\infty}P(|\hat\beta_{j,n}-\beta_j|>\varepsilon)=0.
$$

The subscript $n$ emphasizes a sequence of estimators indexed by sample size. Consistency says that the probability of an error larger than any fixed tolerance approaches zero. It does not promise monotonic improvement for every realized sequence of samples. The lecture states OLS consistency under the first four assumptions and then shows that zero conditional mean is stronger than necessary for this particular large-sample result. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=20|Lecture 1, PDF pp. 20–21]]

### Why population covariance determines the probability limit

Divide both parts of the disturbance ratio by $n$:

$$
\hat\beta_1=\beta_1+
\frac{n^{-1}\sum_i(x_i-\bar x)(u_i-\bar u)}
{n^{-1}\sum_i(x_i-\bar x)^2}.
$$

Under random sampling and finite moments sufficient for the law of large numbers, the numerator converges in probability to $\operatorname{Cov}(x,u)$ and the denominator to $\operatorname{Var}(x)$. With a positive finite population regressor variance, taking the ratio therefore gives

$$
\operatorname{plim}\hat\beta_1
=\beta_1+\frac{\operatorname{Cov}(x,u)}{\operatorname{Var}(x)}.
$$

Here $\operatorname{plim}$ means probability limit. Finite moments and a nonzero limiting denominator are the regularity requirements needed to interpret the lecture's law-of-large-numbers step; the slide does not spell them out. If $\operatorname{Cov}(x,u)=0$, the additional term vanishes. If it is nonzero, more observations concentrate OLS around the wrong value. A larger sample therefore cannot by itself cure regressor–disturbance correlation. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=22|Lecture 1, PDF p. 22, probability-limit derivation]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture1_p22_consistency_derivation.png]]

*Source crop: Lecture 1, PDF p. 22. Centering and division by $n$ turn the estimation-error ratio into sample covariance over sample variance, which exposes its population limit.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=22|Source, PDF p. 22]]

### A weaker exogeneity condition

For consistency, the lecture replaces zero conditional mean by the weaker conditions

$$
E[u]=0,
\qquad
\operatorname{Cov}(x_j,u)=0\quad\text{for each nonconstant regressor }j=1,\ldots,k.
$$

The first condition handles the intercept, and the covariance conditions handle the slopes. The slide writes its index as $j=0,\ldots,k$; with a constant regressor $x_0=1$, its covariance with $u$ is automatically zero. This weaker condition, together with the other sampling, model, nondegeneracy, and moment conditions, supports consistency but need not imply finite-sample unbiasedness. Zero conditional mean implies these unconditional moments, whereas unconditional zero covariance need not imply a zero conditional mean at every regressor value. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=21|Lecture 1, PDF p. 21]]

### How unbiasedness and consistency can differ

The lecture states that an unbiased estimator is consistent if its variance tends to zero. **Agent explanation:** when $E[\hat\theta_n]=\theta$, Chebyshev's inequality bounds $P(|\hat\theta_n-\theta|>\varepsilon)$ by $\operatorname{Var}(\hat\theta_n)/\varepsilon^2$, so a vanishing variance implies convergence in probability. Unbiasedness alone does not control the variance. Conversely, finite-sample bias can vanish as $n$ grows, so a biased estimator can still be consistent. These are properties of the sampling sequence, not a classification that can be proved by examining one estimate. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=21|Lecture 1, PDF p. 21]]

## Efficiency: specify the comparison class

The Gauss–Markov theorem says that under linearity in parameters, random sampling, no perfect collinearity, zero conditional mean, and homoskedasticity, OLS is **BLUE conditional on $X$**: the best linear unbiased estimator. “Linear” means linear in the dependent-variable observations, with weights determined by $X$. “Unbiased” restricts the comparison to estimators centered on the target parameter. “Best” means smallest conditional variance within that class, coefficient by coefficient. This does not claim that every conceivable estimator has a larger variance, or that OLS minimizes all possible loss functions. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=23|Lecture 1, PDF pp. 23–24]]

For the simple-regression slope, the decomposition provides an explanatory variance calculation. Under conditional independence and common disturbance variance $\sigma^2$,

$$
\operatorname{Var}(\hat\beta_1\mid X)
=\frac{1}{S_{xx}^2}\sum_i(x_i-\bar x)^2\sigma^2
=\frac{\sigma^2}{S_{xx}}.
$$

Cross-observation covariance terms vanish under the sampling assumptions. More variation in $x$ supplies a more precise slope, while more disturbance variation reduces precision. This equation answers the seminar's slope-variance question and explains why homoskedasticity matters for the usual standard error. With heteroskedasticity, zero conditional mean can still preserve unbiasedness and suitable conditions can preserve consistency, but the stated BLUE theorem and conventional variance formula no longer follow. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=24|Lecture 1, PDF p. 24]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, slope-variance task]]

## Normality and hypothesis tests add another requirement

The lecture adds normality to the preceding assumptions to obtain a conditional normal distribution for OLS coefficients and exact null $t$ and $F$ distributions. This is a finite-sample inference statement, separate from unbiasedness, consistency, and BLUE. For a null slope value $\beta_{1,0}$,

$$
t=\frac{\hat\beta_1-\beta_{1,0}}{\operatorname{se}(\hat\beta_1)}.
$$

Under the classical assumptions, in a regression with $k$ nonconstant regressors this statistic has a $t$ distribution with $n-k-1$ residual degrees of freedom under the null. An $F$ statistic addresses joint coefficient restrictions. The formula and degrees of freedom are an agent expansion of the lecture's null-distribution statement, used in the seminar's requested slope test. A small standard error or a large absolute $t$ statistic cannot establish exogeneity; inference is conditional on the maintained model assumptions. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=25|Lecture 1, PDF pp. 25–26]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2]]

## Distinctions to retain

| Question | Property | Week 1 OLS conditions and qualification |
|---|---|---|
| Is the repeated-sample center correct? | Unbiasedness | First four assumptions; an individual estimate can still be far from the parameter. |
| Does error become improbable as $n$ grows? | Consistency | First four assumptions are sufficient with regularity; weaker orthogonality moments can replace zero conditional mean. |
| Is the estimator most precise in the stated class? | BLUE efficiency | First five assumptions; the class is linear unbiased estimators conditional on $X$. |
| Are the stated finite-sample null distributions exact? | Classical inference | First six assumptions; normality is an additional requirement. |

These distinctions summarize Lecture 1, PDF pp. 16–26. [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Transport_Demand_Regression_Seminar|The transport-demand seminar]] turns them into interpretation questions: fit the model, identify what the evidence measures, and assess which assumptions can plausibly support it.
