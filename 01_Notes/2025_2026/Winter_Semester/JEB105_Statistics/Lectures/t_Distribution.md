---
course: JEB105
topic: "Student's t-Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, t-distribution, Student, sampling-distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Normal_Distribution]], [[Chi_Squared_Distribution]], [[F_Distribution]], [[Sample_Mean_and_Sample_Variance]], [[Confidence_Intervals]], [[Standard_Tests_Catalog]]

---

## Student's $t$-Distribution

### Definition

Let $Z \sim N(0,1)$ and $V \sim \chi^2_\nu$ be independent. Then the random variable

$$T = \frac{Z}{\sqrt{V/\nu}}$$

has the **Student's $t$-distribution with $\nu$ degrees of freedom**, written $T \sim t_\nu$.

### PDF

$$f(t) = \frac{\Gamma\!\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\;\Gamma\!\left(\frac{\nu}{2}\right)} \left(1 + \frac{t^2}{\nu}\right)^{-(\nu+1)/2}, \quad t \in \mathbb{R}.$$

### Mean and Variance

$$E[T] = 0 \quad (\nu > 1), \qquad \text{Var}(T) = \frac{\nu}{\nu - 2} \quad (\nu > 2).$$

### Properties

- **Symmetry:** $f(t) = f(-t)$; the distribution is symmetric about 0.
- **Heavier tails than normal:** For small $\nu$, the tails are considerably heavier than $N(0,1)$. This reflects extra uncertainty from estimating $\sigma$.
- **Convergence to normal:** As $\nu \to \infty$, $t_\nu \to N(0,1)$ in distribution.
- **Quantiles:** $t_{\alpha/2, \nu}$ denotes the $(1-\alpha/2)$-quantile. Since $t_\nu \to N(0,1)$, for large $\nu$, $t_{\alpha/2,\nu} \approx z_{\alpha/2} = 1.96$ for $\alpha = 0.05$.

### Derivation: One-Sample $t$-Statistic

For $X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$ with $\sigma^2$ unknown:

$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1), \qquad \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1},$$

and $\bar{X} \perp S^2$ (Cochran's theorem). Therefore:

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} = \frac{Z}{\sqrt{\frac{(n-1)S^2}{\sigma^2(n-1)}}} = \frac{Z}{\sqrt{V/(n-1)}} \sim t_{n-1}.$$

This is the fundamental result enabling the one-sample $t$-test and $t$-based confidence intervals for $\mu$ when $\sigma^2$ is unknown.

### Quantiles and Notation

The lecture uses $t_{\alpha,\nu}$ to denote the $(1-\alpha)$-lower quantile of $t_\nu$:
$$P(T \leq t_{\alpha,\nu}) = 1 - \alpha.$$

For two-sided inference: $P(|T| \leq t_{\alpha/2, \nu}) = 1 - \alpha$.

### Applications

- **One-sample $t$-test** for $\mu$ with $\sigma^2$ unknown (see [[Standard_Tests_Catalog]])
- **Two-sample $t$-test** for equality of means with equal unknown variances
- **Confidence intervals** for $\mu$: $\bar{X} \pm t_{\alpha/2,\, n-1} \cdot \frac{S}{\sqrt{n}}$ (see [[Confidence_Intervals]])

### Interpretation

The $t$-distribution arises naturally whenever the population standard deviation $\sigma$ must be replaced by its sample estimate $S$. This introduces additional variability — captured by the heavier tails — that disappears only as $n \to \infty$. In practice, for $n \geq 30$ the $t$ and $z$ critical values are nearly indistinguishable.
