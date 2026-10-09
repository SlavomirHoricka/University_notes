---
course: JEB105
topic: "Confidence Intervals"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_09_Interval_Estimation-1.pdf"
tags: [JEB105, statistics, confidence-interval, interval-estimation, coverage]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_09_Interval_Estimation-1.pdf]]
Related: [[Point_Estimation]], [[Normal_Distribution]], [[t_Distribution]], [[Chi_Squared_Distribution]], [[Fisher_Information]], [[Maximum_Likelihood_Estimation]], [[Hypothesis_Testing_Framework]], [[Standard_Tests_Catalog]]

---

## Confidence Intervals

### Motivation

A point estimator $\hat{\theta}$ produces a single number approximating $\theta$, but provides no information about the precision of this approximation. A confidence interval is an interval estimator that includes $\theta$ with a prescribed probability.

### Definition

**Definition 46 (Lecture):** Let $X = (X_1, \ldots, X_n)$ be a random sample from $f(x,\theta)$ and $\alpha \in (0,1)$ fixed. A pair of statistics $L(X)$ and $U(X)$ is a **$(1-\alpha)$-level confidence interval** for $\theta$ if for all $\theta \in \Theta$:

$$P_\theta(L(X) \leq \theta \leq U(X)) = 1 - \alpha.$$

- $L(X)$ is a $(1-\alpha)$-level **lower confidence bound** if $P_\theta(L(X) \leq \theta) = 1-\alpha$ for all $\theta$.
- $U(X)$ is a $(1-\alpha)$-level **upper confidence bound** if $P_\theta(U(X) \geq \theta) = 1-\alpha$ for all $\theta$.

### Terminology and Notation

- The interval $(L(X), U(X))$ is a **random interval** — it varies from sample to sample.
- The probability $1-\alpha$ is the **coverage probability** — the fraction of samples for which the interval covers $\theta$.
- For a specific realised sample $x$, the interval $(L(x), U(x))$ either contains $\theta$ or does not — no probability remains.
- Typical values: $\alpha = 0.05$ giving a 95% CI; $\alpha = 0.01$ giving a 99% CI.

**Notation:**
- $z_\alpha$: $(1-\alpha)$-lower quantile of $N(0,1)$; $P(Z \leq z_\alpha) = 1-\alpha$.
- $t_{\alpha,\nu}$: $(1-\alpha)$-lower quantile of $t_\nu$.
- $\chi^2_{\alpha,n}$: $(1-\alpha)$-lower quantile of $\chi^2_n$.
- $F_{\alpha,\nu_1,\nu_2}$: $(1-\alpha)$-lower quantile of $F_{\nu_1,\nu_2}$.

### Classical Normal-Model Confidence Intervals

#### Case 1: Mean of $N(\theta, \sigma^2)$ with $\sigma^2$ Known (Example 90)

Since $\bar{X} \sim N(\theta, \sigma^2/n)$ exactly, and $\frac{\bar{X}-\theta}{\sigma/\sqrt{n}} \sim N(0,1)$:

$$\left(\bar{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}},\; \bar{X} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right)$$

is a $(1-\alpha)$-level CI for $\theta$.

**Proof:** $P\!\left(-z_{\alpha/2} < \frac{\bar{X}-\theta}{\sigma/\sqrt{n}} < z_{\alpha/2}\right) = 1-\alpha$ by definition of quantiles and symmetry of $N(0,1)$.

#### Case 2: Mean of $N(\theta, \sigma^2)$ with $\sigma^2$ Unknown (Example 92)

Set $S^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$. Then $T = \frac{\bar{X}-\theta}{S/\sqrt{n}} \sim t_{n-1}$:

$$\left(\bar{X} - t_{\alpha/2,\,n-1}\frac{S}{\sqrt{n}},\; \bar{X} + t_{\alpha/2,\,n-1}\frac{S}{\sqrt{n}}\right)$$

is a $(1-\alpha)$-level CI for $\theta$.

#### Case 3: Variance of $N(\mu, \sigma^2)$ with $\mu$ Known (Example 93)

$$U = \frac{\sum_{i=1}^n (X_i - \mu)^2}{\sigma^2} \sim \chi^2_n.$$

$$P\!\left(\chi^2_{1-\alpha/2,\, n} < \frac{\sum(X_i-\mu)^2}{\sigma^2} < \chi^2_{\alpha/2,\,n}\right) = 1-\alpha.$$

Inverting: $\sigma^2 \in \left(\frac{\sum(X_i-\mu)^2}{\chi^2_{\alpha/2,n}},\; \frac{\sum(X_i-\mu)^2}{\chi^2_{1-\alpha/2,n}}\right)$.

#### Case 4: Variance with $\mu$ Unknown

Replace $\mu$ by $\bar{X}$: $V = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$. The CI for $\sigma^2$ uses $\chi^2_{n-1}$ quantiles:

$$\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2,\,n-1}},\; \frac{(n-1)S^2}{\chi^2_{1-\alpha/2,\,n-1}}\right).$$

Note: Knowing $\mu$ gives a shorter CI (more degrees of freedom).

### Large-Sample CIs Based on CLTs

**Theorem 60 (Lecture):** If $T$ is an efficient estimator of $\theta$ from a distribution $f(x,\theta)$, then $\sqrt{nI(\theta)}(T-\theta) \xrightarrow{d} N(0,1)$.

**Theorem 61 (Lecture):** Let $\hat{\theta}_n$ be the MLE satisfying the conditions of Theorem 60. Then for large $n$:

$$\left(\hat{\theta}_n - \frac{z_{\alpha/2}}{\sqrt{nI(\hat{\theta}_n)}},\; \hat{\theta}_n + \frac{z_{\alpha/2}}{\sqrt{nI(\hat{\theta}_n)}}\right)$$

is an approximate $(1-\alpha)$-CI for $\theta$.

**Example 91 (Bernoulli):** With $\hat{p} = \bar{X}$ the MLE of $p$ and $I(p) = 1/(p(1-p))$:

$$\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}.$$

### Link to Hypothesis Tests

There is a duality between CIs and hypothesis tests: the $(1-\alpha)$-CI for $\theta$ consists exactly of all null hypothesis values $\theta_0$ that would **not** be rejected by the $\alpha$-level test $H_0: \theta = \theta_0$ against $H_1: \theta \neq \theta_0$ (see [[Hypothesis_Testing_Framework]]).

### Interpretation

A 95% CI $(L(x), U(x))$ does not mean "there is a 95% probability that $\theta$ lies in this interval" — $\theta$ is fixed. The correct interpretation is: "If we repeated the sampling procedure many times and computed a CI each time, 95% of those intervals would contain the true $\theta$."
