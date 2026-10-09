---
course: JEB105
topic: "Chi-Squared Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, chi-squared, sampling-distribution, normal]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Normal_Distribution]], [[Gamma_Distribution]], [[t_Distribution]], [[F_Distribution]], [[Sample_Mean_and_Sample_Variance]], [[Standard_Tests_Catalog]]

---

## Chi-Squared Distribution

### Definition

If $Z_1, Z_2, \ldots, Z_k \overset{\text{i.i.d.}}{\sim} N(0,1)$, then the random variable

$$Q = \sum_{i=1}^k Z_i^2 \sim \chi^2_k$$

has the **chi-squared distribution with $k$ degrees of freedom**.

### Connection to the Gamma Distribution

The chi-squared distribution is a special case of the [[Gamma_Distribution]]:

$$\chi^2_k = \text{Gamma}\!\left(\frac{k}{2}, \frac{1}{2}\right).$$

The PDF of $\chi^2_k$ is:

$$f(x) = \frac{1}{2^{k/2}\,\Gamma(k/2)}\, x^{k/2-1} e^{-x/2}, \quad x > 0.$$

### Mean and Variance

$$E[\chi^2_k] = k, \qquad \text{Var}(\chi^2_k) = 2k.$$

**Derivation of the mean:** Since $E[Z_i^2] = \text{Var}(Z_i) = 1$ for $Z_i \sim N(0,1)$, by linearity:
$$E[Q] = \sum_{i=1}^k E[Z_i^2] = k.$$

### Reproductive Property

If $Q_1 \sim \chi^2_{k_1}$ and $Q_2 \sim \chi^2_{k_2}$ are independent, then:

$$Q_1 + Q_2 \sim \chi^2_{k_1 + k_2}.$$

This follows immediately from the definition — summing more squared standard normals increases the degrees of freedom.

### MGF

$$M_Q(t) = (1 - 2t)^{-k/2}, \quad t < \frac{1}{2}.$$

### Quantiles

The $(1-\alpha)$-lower quantile of $\chi^2_k$, denoted $\chi^2_{\alpha,k}$, satisfies $P(\chi^2_k \leq \chi^2_{\alpha,k}) = 1-\alpha$. Standard tables or software (e.g. `qchisq(1-alpha, df=k)` in R) provide these values.

### Key Application: Distribution of Sample Variance

For a normal random sample $X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$:

$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}.$$

This result (see [[Sample_Mean_and_Sample_Variance]]) is the basis for:
- Confidence intervals for $\sigma^2$ (see [[Confidence_Intervals]])
- Chi-squared tests for the variance (see [[Standard_Tests_Catalog]])

### Interpretation

The chi-squared distribution describes the sum of squared standard normal random variables. The degrees of freedom parameter $k$ counts the number of independent squared terms. In regression and ANOVA contexts, $k$ corresponds to the number of free parameters; in one-sample variance inference, $k = n-1$ because one degree of freedom is "used" to estimate the mean.

The distribution is right-skewed for small $k$ and approaches normality as $k \to \infty$ (by the CLT applied to the $Z_i^2$).
