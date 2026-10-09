---
course: JEB105
topic: "Standard Tests Catalog"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, z-test, t-test, chi-squared-test, F-test, two-sample, paired, hypothesis-testing]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Hypothesis_Testing_Framework]], [[Confidence_Intervals]], [[Normal_Distribution]], [[t_Distribution]], [[Chi_Squared_Distribution]], [[F_Distribution]], [[Central_Limit_Theorem]], [[p_Value]]

---

## Standard Tests Catalog

This note collects all standard tests covered in JEB105. Throughout, $X_1,\ldots,X_m \overset{\text{i.i.d.}}{\sim} N(\mu_1,\sigma_1^2)$ and $Y_1,\ldots,Y_n \overset{\text{i.i.d.}}{\sim} N(\mu_2,\sigma_2^2)$. Denote $\bar{X}$, $\bar{Y}$ as sample means and $S_1^2$, $S_2^2$ as sample variances.

---

### One-Sample Tests

#### (i) Mean Test with $\sigma^2$ Known ($z$-test, one-sided upper)

$$H_0: \mu = \mu_0, \quad H_1: \mu > \mu_0.$$

Test statistic: $U = \dfrac{\bar{X}-\mu_0}{\sigma}\sqrt{n}$.

Critical region: $U \geq z_\alpha$.

*(For $H_1: \mu < \mu_0$: critical region $U \leq z_{1-\alpha} = -z_\alpha$.)*

#### (ii) Mean Test with $\sigma^2$ Known ($z$-test, two-sided)

$$H_0: \mu = \mu_0, \quad H_1: \mu \neq \mu_0.$$

Test statistic: $U = \dfrac{\bar{X}-\mu_0}{\sigma}\sqrt{n}$.

Critical region: $|U| \geq z_{\alpha/2}$.

#### (iii) Mean Test with $\sigma^2$ Unknown ($t$-test, one-sided upper)

$$H_0: \mu = \mu_0, \quad H_1: \mu > \mu_0.$$

Test statistic: $t = \dfrac{\bar{X}-\mu_0}{\sqrt{\tfrac{1}{n}\sum(X_i-\bar{X})^2}}\sqrt{n-1}$.

Critical region: $t \geq t_{\alpha,\,n-1}$.

#### (iv) Mean Test with $\sigma^2$ Unknown ($t$-test, two-sided)

$$H_0: \mu = \mu_0, \quad H_1: \mu \neq \mu_0.$$

Critical region: $|t| \geq t_{\alpha/2,\,n-1}$.

#### (v) Variance Test ($\chi^2$-test, one-sided)

$$H_0: \sigma^2 = \sigma_0^2, \quad H_1: \sigma^2 > \sigma_0^2 \text{ (or } \sigma^2 < \sigma_0^2).$$

Test statistic: $\chi^2 = \dfrac{\sum(X_i - \bar{X})^2}{\sigma_0^2}$.

Critical region (upper): $\chi^2 \geq \chi^2_{\alpha,\,n-1}$.

Critical region (lower): $\chi^2 \leq \chi^2_{1-\alpha,\,n-1}$.

#### (vi) Variance Test ($\chi^2$-test, two-sided)

$$H_0: \sigma^2 = \sigma_0^2, \quad H_1: \sigma^2 \neq \sigma_0^2.$$

Critical region: $\chi^2 \leq \chi^2_{1-\alpha/2,\,n-1}$ or $\chi^2 \geq \chi^2_{\alpha/2,\,n-1}$.

---

### Two-Sample Tests

#### (vii) Two Means with $\sigma^2$ Known ($z$-test, one-sided)

$$H_0: \mu_1 = \mu_2, \quad H_1: \mu_1 > \mu_2.$$

Test statistic: $U = \dfrac{\bar{X}-\bar{Y}}{\sqrt{\sigma_1^2/m + \sigma_2^2/n}}$.

Critical region: $U \geq z_\alpha$.

#### (viii) Two Means with $\sigma^2$ Known (two-sided)

Critical region: $|U| \geq z_{\alpha/2}$.

#### (ix) Two Means with $\sigma_1^2 = \sigma_2^2$ Unknown (pooled $t$-test, one-sided)

$$H_0: \mu_1 = \mu_2, \quad H_1: \mu_1 > \mu_2.$$

Pooled test statistic:

$$T = \frac{\bar{X}-\bar{Y}}{\sqrt{(m-1)S_1^2+(n-1)S_2^2}}\sqrt{\frac{m+n-2}{\tfrac{1}{m}+\tfrac{1}{n}}}.$$

Critical region: $T \geq t_{\alpha,\,m+n-2}$.

#### (x) Two Means with $\sigma_1^2 = \sigma_2^2$ Unknown (two-sided)

Critical region: $|T| \geq t_{\alpha/2,\,m+n-2}$.

#### (xi) Equality of Variances ($F$-test, one-sided)

$$H_0: \sigma_1^2 = k\sigma_2^2, \quad H_1: \sigma_1^2 > k\sigma_2^2.$$

Test statistic: $F = \dfrac{\sum(X_i-\bar{X})^2/(m-1)}{k\cdot\sum(Y_j-\bar{Y})^2/(n-1)}$.

Critical region: $F \geq F_{\alpha,\,m-1,\,n-1}$.

#### (xii) Equality of Variances ($F$-test, two-sided)

$$H_0: \sigma_1^2 = k\sigma_2^2, \quad H_1: \sigma_1^2 \neq k\sigma_2^2.$$

Critical region: $F \leq F_{1-\alpha/2,\,m-1,\,n-1}$ or $F \geq F_{\alpha/2,\,m-1,\,n-1}$.

---

### Large-Sample Tests Based on CLTs

#### Binomial Proportion Test (one-sample)

$X \sim \text{Bin}(n, p)$, large $n$. Test $H_0: p = p_0$.

$$Z = \frac{X/n - p_0}{\sqrt{p_0(1-p_0)/n}} \overset{\text{approx}}{\sim} N(0,1).$$

#### Two-Sample Proportion Test

$X \sim \text{Bin}(n_1, p_1)$, $Y \sim \text{Bin}(n_2, p_2)$, $n_1, n_2$ large. Test $H_0: p_1 = p_2 = p$.

$$Z = \frac{X/n_1 - Y/n_2}{\sqrt{\hat{p}_{\text{MLE}}\left(1-\hat{p}_{\text{MLE}}\right)\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}} \overset{\text{approx}}{\sim} N(0,1),$$

where $\hat{p}_{\text{MLE}} = \frac{X+Y}{n_1+n_2}$.

---

### Paired Test vs. Two-Sample Test

When data come in matched pairs $(X_i, Y_i)$, define $Z_i = X_i - Y_i$. Test $\mu_X = \mu_Y$ using the **one-sample $t$-test** on $Z_1, \ldots, Z_n$ with $H_0: \mu_Z = 0$.

| Situation | Test to use |
|---|---|
| $n_1 \neq n_2$ | Two-sample test |
| $n_1 = n_2$, independent | Two-sample test |
| $n_1 = n_2$, paired (same subjects) | Paired $t$-test |

**Warning:** Applying the two-sample test to paired data requires a much larger sample to achieve the same power. The paired design reduces variance by eliminating between-subject variability.

---

### Notation Recap

| Symbol | Meaning |
|---|---|
| $\alpha$ | Significance level |
| $1-\beta$ | Power |
| $z_p$ | Upper $p$-th quantile of $N(0,1)$ |
| $t_{p,\nu}$ | Upper $p$-th quantile of $t_\nu$ |
| $\chi^2_{p,\nu}$ | Upper $p$-th quantile of $\chi^2_\nu$ |
| $F_{p,\nu_1,\nu_2}$ | Upper $p$-th quantile of $F_{\nu_1,\nu_2}$ |
