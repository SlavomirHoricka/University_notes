---
course: JEB105
topic: "Order Statistics"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, order-statistics, sample-minimum, sample-maximum]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Random_Sample_and_Statistics]], [[Cumulative_Distribution_Function]], [[Point_Estimation]]

---

## Order Statistics

### Definition

Let $X_1, \ldots, X_n$ be i.i.d. random variables. The **order statistics** $X_{1:n} \leq X_{2:n} \leq \cdots \leq X_{n:n}$ are the sample values sorted in non-decreasing order.

- $X_{1:n} = \min(X_1, \ldots, X_n)$ — the **sample minimum**
- $X_{n:n} = \max(X_1, \ldots, X_n)$ — the **sample maximum**
- $X_{k:n}$ — the **$k$-th order statistic**

### CDF of the $k$-th Order Statistic

Let $F$ be the common CDF and $f$ the PDF of each $X_i$. The CDF of $X_{k:n}$ is:

$$F_{k:n}(x) = \sum_{j=k}^n \binom{n}{j} [F(x)]^j [1-F(x)]^{n-j}.$$

This counts the probability that at least $k$ of the $n$ values fall at or below $x$.

### PDF of the $k$-th Order Statistic

Differentiating:

$$f_{k:n}(x) = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1}[1-F(x)]^{n-k} f(x).$$

### Special Cases

**Sample minimum $X_{1:n}$:**
$$F_{1:n}(x) = 1 - [1-F(x)]^n, \qquad f_{1:n}(x) = n[1-F(x)]^{n-1}f(x).$$

**Sample maximum $X_{n:n}$:**
$$F_{n:n}(x) = [F(x)]^n, \qquad f_{n:n}(x) = n[F(x)]^{n-1}f(x).$$

### Example: Uniform Distribution

Let $X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} U[0,\theta]$. Then $F(x) = x/\theta$ for $x \in [0,\theta]$.

**Sample maximum $X_{n:n}$:**
$$F_{n:n}(x) = \left(\frac{x}{\theta}\right)^n, \qquad E[X_{n:n}] = \frac{n}{n+1}\theta.$$

This is the $T_1$ estimator from Lecture 8 (Example 82). The bias is $E[X_{n:n}] - \theta = -\frac{\theta}{n+1}$, so $T_1$ is biased but consistent.

### Applications

Order statistics appear in:
- **Non-parametric inference:** Rank-based tests.
- **Estimation:** The sample maximum and minimum as estimators of distribution endpoints.
- **Extreme value theory:** The distribution of maxima over large samples, relevant in finance (tail risk) and hydrology (flood levels).
- **Reliability theory:** The minimum order statistic models the lifetime of a system of $n$ components in series.

### Interpretation

Order statistics reveal the structure of the sample beyond what summary statistics like $\bar{X}$ and $S^2$ capture. The sample maximum $X_{n:n}$ is the natural estimator for the upper endpoint of a distribution's support. The gap $X_{n:n} - X_{1:n}$ is the sample range — a crude measure of spread.
