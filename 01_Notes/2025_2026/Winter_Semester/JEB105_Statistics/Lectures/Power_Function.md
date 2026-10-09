---
course: JEB105
topic: "Power Function"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, power-function, power, hypothesis-testing]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Hypothesis_Testing_Framework]], [[Type_I_and_Type_II_Errors]], [[Neyman_Pearson_Lemma]], [[Standard_Tests_Catalog]]

---

## Power Function

### Definition

For a test with critical region $C$, the **power function** is:

$$\pi_C(\theta) = P_\theta(X \in C), \quad \theta \in \Theta.$$

The power function traces out, for each possible true value of $\theta$, the probability that the test rejects $H_0$.

### Interpretation at Different Points

- $\theta \in \Theta_0$ (null is true): $\pi_C(\theta) = \alpha(\theta)$ is the **type I error probability**. We want $\pi_C(\theta)$ to be **small** here.
- $\theta \in \Theta_1$ (alternative is true): $\pi_C(\theta) = 1 - \beta(\theta)$ is the **power** — the probability of correctly rejecting $H_0$. We want $\pi_C(\theta)$ to be **large** here.

Ideal power function: 0 for all $\theta \in \Theta_0$ and 1 for all $\theta \in \Theta_1$. In practice, a trade-off is unavoidable.

### Example: Two-Sided Normal Mean Test

$X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$ (known $\sigma^2$), testing $H_0: \mu = \mu_0$ vs. $H_1: \mu \neq \mu_0$.

Critical region: $C = \{|\bar{X} - \mu_0| > K\}$.

Power function:
$$\pi_C(\mu) = 1 - P\!\left(\frac{-K + \mu_0 - \mu}{\sigma/\sqrt{n}} \leq Z \leq \frac{K + \mu_0 - \mu}{\sigma/\sqrt{n}}\right)$$
$$= 1 - \Phi\!\left(\frac{K + \mu_0 - \mu}{\sigma/\sqrt{n}}\right) + \Phi\!\left(\frac{-K + \mu_0 - \mu}{\sigma/\sqrt{n}}\right).$$

Properties of this power function:
- **Minimum at $\mu = \mu_0$:** $\pi_C(\mu_0) = \alpha$ (the size of the test).
- **Symmetric about $\mu_0$:** $\pi_C(\mu_0 + \delta) = \pi_C(\mu_0 - \delta)$.
- **Increasing as $|\mu - \mu_0|$ grows:** Larger deviations are easier to detect.
- **Approaches 1 as $|\mu - \mu_0| \to \infty$:** The test is consistent.

For fixed $n$ and $\alpha = 0.1$, $\mu_0 = 2$, $\sigma^2 = 0.04$, the power function has a characteristic U-shape centred at $\mu_0 = 2$ (as shown in Lecture slide 14/35).

### Comparing Tests

Given two critical regions $C_1$ and $C_2$ with the same size $\bar{\alpha}(C_1) = \bar{\alpha}(C_2) = \alpha$, we prefer $C_1$ if:

$$\pi_{C_1}(\theta) \geq \pi_{C_2}(\theta) \quad \text{for all } \theta \in \Theta_1.$$

We call $C_1$ **more powerful** than $C_2$ if this holds strictly for some $\theta \in \Theta_1$.

A test is **uniformly most powerful (UMP)** at level $\alpha$ if it has the highest power among all $\alpha$-level tests for every $\theta \in \Theta_1$. The [[Neyman_Pearson_Lemma]] constructs the UMP test for simple hypotheses.

### Power and Effect Size

The power of a test for $H_0: \mu = \mu_0$ vs. $H_1: \mu = \mu_1$ increases with:
1. **Effect size** $|\mu_1 - \mu_0|/\sigma$: larger standardised difference.
2. **Sample size** $n$: the standard error $\sigma/\sqrt{n}$ decreases.
3. **Significance level** $\alpha$: larger $\alpha$ gives more rejections (at the cost of more type I errors).

### Interpretation

The power function is the complete performance characterisation of a test. A test with a power function that stays close to $\alpha$ everywhere on $\Theta_1$ is nearly useless — it fails to detect the alternative. A good test has power approaching 1 quickly as $\theta$ moves away from $\Theta_0$. In practice, reporting the power at the effect size of scientific interest is essential for interpreting non-significant results (a non-significant test with low power is inconclusive, not evidence for $H_0$).
