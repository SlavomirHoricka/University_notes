---
course: JEB105
topic: "Sample Mean and Sample Variance"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, sample-mean, sample-variance, sampling-distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Random_Sample_and_Statistics]], [[Expected_Value]], [[Variance]], [[Normal_Distribution]], [[Chi_Squared_Distribution]], [[t_Distribution]], [[Central_Limit_Theorem]]

---

## Sample Mean and Sample Variance

### Definitions

Let $X_1, \ldots, X_n$ be i.i.d. random variables with $E[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2 < \infty$.

**Sample mean:**
$$\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i.$$

**Sample variance (unbiased):**
$$S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2.$$

The denominator $n-1$ (Bessel's correction) ensures unbiasedness. The biased alternative $\hat{\sigma}^2 = \frac{1}{n}\sum(X_i - \bar{X})^2$ is the MLE under normality but underestimates $\sigma^2$.

### Properties of the Sample Mean

**Expectation:**
$$E[\bar{X}_n] = \mu.$$

**Variance:**
$$\text{Var}(\bar{X}_n) = \frac{\sigma^2}{n}.$$

**Derivation:** By linearity of expectation and independence,
$$E[\bar{X}_n] = \frac{1}{n}\sum_{i=1}^n E[X_i] = \mu.$$
$$\text{Var}(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^n \text{Var}(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}.$$

### Properties of the Sample Variance

**Unbiasedness:** $E[S^2] = \sigma^2$.

**Derivation:**
$$E\!\left[\sum_{i=1}^n (X_i - \bar{X})^2\right] = E\!\left[\sum_{i=1}^n X_i^2 - n\bar{X}^2\right] = n(\sigma^2 + \mu^2) - n\!\left(\frac{\sigma^2}{n} + \mu^2\right) = (n-1)\sigma^2.$$

Hence $E[S^2] = \frac{1}{n-1}(n-1)\sigma^2 = \sigma^2$.

### Distributional Results for Normal Samples

Suppose $X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$.

**Theorem (Distribution of sample mean):**
$$\bar{X}_n \sim N\!\left(\mu, \frac{\sigma^2}{n}\right).$$

**Theorem (Distribution of scaled sample variance):**
$$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}.$$

See [[Chi_Squared_Distribution]] for properties of the chi-squared distribution.

**Key independence fact (Cochran's theorem):** $\bar{X}_n$ and $S^2$ are **independent** when sampling from a normal distribution. This is a special property of the normal distribution and underpins the derivation of the $t$-distribution.

### Student's $t$-statistic

When $\sigma^2$ is unknown, we standardise using $S$ instead of $\sigma$:

$$T = \frac{\bar{X}_n - \mu}{S/\sqrt{n}} \sim t_{n-1}.$$

This follows from the independence of $\bar{X}$ and $S^2$ and the definition of the [[t_Distribution]].

### Interpretation

- The sample mean $\bar{X}_n$ is the natural estimator of the population mean $\mu$. Its variance $\sigma^2/n$ decreases in $n$, reflecting that larger samples yield more precise estimates.
- The factor $n-1$ in $S^2$ corrects for the loss of one degree of freedom due to estimating $\mu$ by $\bar{X}$.
- The distributional results for normal samples are the foundation of classical $z$-tests, $t$-tests, and $\chi^2$-tests for the variance (see [[Standard_Tests_Catalog]]).
