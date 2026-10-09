---
course: JEB105
topic: "p-Value"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, p-value, significance, hypothesis-testing]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Hypothesis_Testing_Framework]], [[Type_I_and_Type_II_Errors]], [[Standard_Tests_Catalog]]

---

## $p$-Value

### Definition

**Definition 52 (Lecture):** The **$p$-value** is the lowest significance level at which $H_0$ is rejected given the observed data.

Equivalently, the $p$-value is the probability, computed under $H_0$, of observing a test statistic at least as extreme as the one actually observed.

$$p\text{-value} = P_{H_0}(T \geq t_{\text{obs}})$$

for a one-sided upper-tail test, where $t_{\text{obs}}$ is the observed value of the test statistic $T$.

### Computation for Different Alternative Hypotheses

Let $Z \sim N(0,1)$ (or an appropriate test statistic) and $z$ be the observed value:

| Alternative | $p$-value |
|---|---|
| $H_1: \mu > \mu_0$ (one-sided upper) | $P(Z \geq z)$ |
| $H_1: \mu < \mu_0$ (one-sided lower) | $P(Z \leq z)$ |
| $H_1: \mu \neq \mu_0$ (two-sided) | $P(\|Z\| \geq \|z\|) = P(Z \leq -\|z\|) + P(Z \geq \|z\|)$ |

Analogously for $t$, $\chi^2$, $F$ distributions.

### Decision Rule

Reject $H_0$ at significance level $\alpha$ if and only if:

$$p\text{-value} \leq \alpha.$$

### Why Report $p$-Values?

The statement "$H_0$ was rejected at $\alpha = 0.05$" is less informative than reporting $p = 0.02$:
- $p = 0.02$ allows the reader to know the result is also significant at $\alpha = 0.05$ but not at $\alpha = 0.01$.
- $p = 0.04$ is significant at $\alpha = 0.05$ but borderline — very different from $p = 0.001$.

The smaller the $p$-value, the stronger the evidence against $H_0$:
- $p < 0.001$: Very strong evidence against $H_0$.
- $p \approx 0.05$: Marginal evidence.
- $p > 0.10$: Weak or no evidence against $H_0$ (given the sample size).

### Misinterpretations to Avoid

1. **$p$-value is NOT** the probability that $H_0$ is true.
2. **$p$-value is NOT** the probability that the observed result occurred by chance.
3. **$p$-value does NOT measure** the size or practical importance of an effect.
4. **Statistical significance $\neq$ practical significance:** A tiny effect can be highly significant with large $n$.

### Discrete Case

In the discrete case (e.g., binomial), there may be no test with type I error exactly equal to $\alpha_0$. The $p$-value is still well-defined as the probability of observing a result at least as extreme as observed, computed under $H_0$.

### Interpretation

The $p$-value is the most widely reported quantity in applied statistics. It summarises the evidence in the data against $H_0$ in a scale-free, standardised way. A pre-specified significance level $\alpha$ converts the $p$-value into a binary decision; reporting the $p$-value itself leaves the decision to the reader and allows for replication and meta-analysis. Understanding both what the $p$-value means and what it does not mean is essential for scientific literacy in the quantitative social sciences.
