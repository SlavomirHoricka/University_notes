---
course: JEB105
topic: "Type I and Type II Errors"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, type-I-error, type-II-error, hypothesis-testing, significance]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Hypothesis_Testing_Framework]], [[Power_Function]], [[Neyman_Pearson_Lemma]], [[p_Value]]

---

## Type I and Type II Errors

### The Two Types of Error

When making a binary decision (reject or do not reject $H_0$), two kinds of mistakes are possible:

| Decision \ Truth | $\theta \in \Theta_0$ ($H_0$ true) | $\theta \in \Theta_1$ ($H_1$ true) |
|---|---|---|
| Reject $H_0$ ($X \in C$) | **Type I error** | Correct (power) |
| Do not reject $H_0$ ($X \notin C$) | Correct | **Type II error** |

**Type I error:** Rejecting $H_0$ when $H_0$ is actually true. Probability:
$$\alpha(\theta) = P_\theta(X \in C) \quad \text{for } \theta \in \Theta_0.$$

**Type II error:** Failing to reject $H_0$ when $H_1$ is actually true. Probability:
$$\beta(\theta) = P_\theta(X \notin C) = 1 - P_\theta(X \in C) \quad \text{for } \theta \in \Theta_1.$$

### Asymmetry of Errors

**Example 95 (Lecture):** Legal trial. $H_0$: prisoner innocent; $H_1$: prisoner guilty.
- **Type I error:** Innocent prisoner convicted — miscarriage of justice.
- **Type II error:** Guilty prisoner acquitted — criminal goes free.

The seriousness depends on context. In most statistical settings, a **type I error is considered more severe** and is controlled first by fixing the significance level $\alpha$.

### Trade-Off

- Reducing $\alpha$ (type I error probability) by making $C$ smaller generally **increases** $\beta$ (type II error probability) and vice versa.
- This trade-off leads to **Pareto-optimal** solutions: beyond a certain point, improving one criterion necessarily worsens the other.
- The Neyman-Pearson approach fixes $\alpha$ and then minimises $\beta$ — see [[Neyman_Pearson_Lemma]].

### The Power Function

Both $\alpha(\theta)$ and $\beta(\theta)$ are derived from the **power function**:

$$\pi_C(\theta) = P_\theta(X \in C).$$

- For $\theta \in \Theta_0$: $\pi_C(\theta) = \alpha(\theta)$ (type I error probability).
- For $\theta \in \Theta_1$: $\pi_C(\theta) = 1 - \beta(\theta)$ (**power** of the test at $\theta$).

A good test has $\pi_C(\theta)$ small for $\theta \in \Theta_0$ and large for $\theta \in \Theta_1$. See [[Power_Function]] for a detailed analysis.

### Power and Sample Size

For a fixed significance level $\alpha$, the power $1-\beta$ increases with:
- **Larger $n$:** More data provides more information.
- **Larger effect size** $|\theta - \theta_0|$: Parameters further from the null are easier to detect.

In practice, **power analysis** (computing the required $n$ to achieve a target power $1-\beta$) is performed before data collection to ensure the study is adequately powered.

### Interpretation

Type I and type II errors formalise the cost of uncertainty in decision-making. Fixing $\alpha = 0.05$ means we accept a 5% chance of incorrectly rejecting a true null hypothesis. The complementary type II error rate $\beta$ depends on the true parameter value — it is lowest (power is highest) when $\theta$ is far from $\Theta_0$ and the sample is large. Understanding both error types is essential for interpreting statistical results correctly and avoiding misleading conclusions.
