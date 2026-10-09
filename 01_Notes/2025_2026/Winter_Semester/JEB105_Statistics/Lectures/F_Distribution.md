---
course: JEB105
topic: "F-Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, F-distribution, sampling-distribution, variance-ratio]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Chi_Squared_Distribution]], [[t_Distribution]], [[Normal_Distribution]], [[Standard_Tests_Catalog]]

---

## $F$-Distribution

### Definition

Let $U \sim \chi^2_{\nu_1}$ and $V \sim \chi^2_{\nu_2}$ be independent. The random variable

$$F = \frac{U/\nu_1}{V/\nu_2}$$

has the **$F$-distribution with $\nu_1$ numerator and $\nu_2$ denominator degrees of freedom**, written $F \sim F_{\nu_1, \nu_2}$.

### PDF

$$f(x) = \frac{\sqrt{\frac{(\nu_1 x)^{\nu_1}\,\nu_2^{\nu_2}}{(\nu_1 x + \nu_2)^{\nu_1+\nu_2}}}}{x\,B\!\left(\frac{\nu_1}{2},\frac{\nu_2}{2}\right)}, \quad x > 0,$$

where $B$ is the beta function.

### Mean and Variance

$$E[F] = \frac{\nu_2}{\nu_2 - 2} \quad (\nu_2 > 2), \qquad \text{Var}(F) = \frac{2\nu_2^2(\nu_1+\nu_2-2)}{\nu_1(\nu_2-2)^2(\nu_2-4)} \quad (\nu_2 > 4).$$

### Key Properties

- **Right-skewed:** The $F$-distribution is always non-negative and right-skewed.
- **Reciprocal property:** If $F \sim F_{\nu_1,\nu_2}$, then $1/F \sim F_{\nu_2,\nu_1}$.
- **Relation to $t$:** If $T \sim t_\nu$, then $T^2 \sim F_{1,\nu}$.
- **Quantile notation:** $F_{\alpha,\nu_1,\nu_2}$ denotes the $(1-\alpha)$-lower quantile.

### Application: Ratio of Sample Variances

For two independent normal samples $X_1,\ldots,X_m \overset{\text{i.i.d.}}{\sim} N(\mu_1,\sigma_1^2)$ and $Y_1,\ldots,Y_n \overset{\text{i.i.d.}}{\sim} N(\mu_2,\sigma_2^2)$:

$$F = \frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2} \sim F_{m-1,\, n-1}.$$

Under the null hypothesis $H_0: \sigma_1^2 = k\sigma_2^2$, the test statistic becomes:

$$F = \frac{\sum(X_i - \bar{X})^2/(m-1)}{k\cdot\sum(Y_j - \bar{Y})^2/(n-1)} \sim F_{m-1,\, n-1}.$$

This is the basis of the $F$-test for equality of variances and of ANOVA (see [[Standard_Tests_Catalog]]).

### Interpretation

The $F$-distribution compares the variability in two independent samples, each scaled by their respective degrees of freedom. A large $F$ statistic indicates that the numerator variance is much larger than the denominator variance — evidence against equal variances (or, in ANOVA, evidence that group means differ). The two degrees-of-freedom parameters $(\nu_1, \nu_2)$ characterise the exact shape of the distribution and are determined by the sample sizes.
