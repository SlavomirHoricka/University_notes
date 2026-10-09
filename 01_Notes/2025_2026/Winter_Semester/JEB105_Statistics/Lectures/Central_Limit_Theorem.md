---
course: JEB105
topic: "Central Limit Theorem"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, CLT, central-limit-theorem, normal-approximation, asymptotic]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Law_of_Large_Numbers]], [[Normal_Distribution]], [[Convergence_of_Random_Variables]], [[Sample_Mean_and_Sample_Variance]], [[Confidence_Intervals]], [[Standard_Tests_Catalog]]

---

## Central Limit Theorem

### Statement

Let $X_1, X_2, \ldots$ be i.i.d. random variables with $E[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2 \in (0, \infty)$. Then as $n \to \infty$:

$$\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1).$$

Equivalently, $\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \sigma^2)$.

### Practical Approximation

For large $n$, we write (approximately):

$$\bar{X}_n \overset{\text{approx}}{\sim} N\!\left(\mu, \frac{\sigma^2}{n}\right),$$

or equivalently,

$$\sum_{i=1}^n X_i \overset{\text{approx}}{\sim} N(n\mu, n\sigma^2).$$

This approximation is used to compute probabilities and construct confidence intervals without knowing the true distribution of $X_i$.

### Proof Sketch (via MGFs)

Under the MGF existence assumption, let $Z_i = (X_i - \mu)/\sigma$, so $E[Z_i] = 0$, $E[Z_i^2] = 1$. The MGF of the standardised sum $S_n^* = \frac{1}{\sqrt{n}}\sum Z_i$ is:

$$M_{S_n^*}(t) = \left[M_{Z}(t/\sqrt{n})\right]^n.$$

Expanding $M_Z(t/\sqrt{n}) = 1 + \frac{t^2}{2n} + O(n^{-3/2})$:

$$\left[M_{Z}(t/\sqrt{n})\right]^n \to e^{t^2/2} \quad \text{as } n \to \infty,$$

which is the MGF of $N(0,1)$. Convergence of MGFs implies convergence in distribution.

### Continuity Correction

When approximating a **discrete** distribution by the normal, a continuity correction improves accuracy:

$$P(X \leq k) \approx \Phi\!\left(\frac{k + \frac{1}{2} - \mu}{\sigma}\right).$$

Example: For $X \sim \text{Bin}(n,p)$ with $np$ and $n(1-p)$ both large, $X \approx N(np, np(1-p))$ with continuity correction.

### Extensions

- **Lindeberg-Feller CLT:** The CLT holds for independent but not necessarily identically distributed random variables, under the Lindeberg condition (no single observation dominates the variance).
- **CLT for functions of the mean (Delta method):** If $\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} N(0, \sigma^2)$ and $g$ is differentiable at $\mu$ with $g'(\mu) \neq 0$, then:

$$\sqrt{n}(g(\bar{X}_n) - g(\mu)) \xrightarrow{d} N(0, [g'(\mu)]^2 \sigma^2).$$

### Applications in JEB105

- **Large-sample confidence intervals:** When $\sigma$ is estimated by $S$, Slutsky's theorem gives $\frac{\bar{X}_n - \mu}{S/\sqrt{n}} \xrightarrow{d} N(0,1)$, justifying $z$-based CIs for large $n$.
- **Asymptotic CI for the MLE:** The CLT combined with Fisher information gives the approximate CI $\hat{\theta} \pm \frac{z_{\alpha/2}}{\sqrt{nI(\hat{\theta})}}$ (see [[Rao_Cramer_Lower_Bound]], [[Confidence_Intervals]]).
- **Tests based on CLTs:** For $X \sim \text{Bin}(n,p)$, $Z = \frac{X/n - p_0}{\sqrt{p_0(1-p_0)/n}} \overset{\text{approx}}{\sim} N(0,1)$ under $H_0: p = p_0$ (see [[Standard_Tests_Catalog]]).

### Interpretation

The CLT is arguably the most important theorem in statistics. It explains why the normal distribution appears everywhere: regardless of the shape of the original distribution, sample averages are approximately normally distributed for large $n$. This universality underpins the validity of many classical statistical procedures even when the data are not themselves normally distributed.

The rate of convergence is $O(1/\sqrt{n})$: each factor of 4 in sample size improves precision by a factor of 2.
