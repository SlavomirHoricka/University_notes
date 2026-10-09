---
course: JEB105
topic: "Neyman-Pearson Lemma"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, Neyman-Pearson, UMP, most-powerful-test, likelihood-ratio]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Hypothesis_Testing_Framework]], [[Power_Function]], [[Type_I_and_Type_II_Errors]], [[Generalized_Likelihood_Ratio_Test]], [[Maximum_Likelihood_Estimation]]

---

## Neyman-Pearson Lemma

### Motivation: Simple vs. Simple Testing

Suppose both $H_0: \theta = \theta_0$ and $H_1: \theta = \theta_1$ are simple. We want to find the critical region $C^*$ that:
- Has fixed type I error probability $\alpha = P(X \in C^* \mid H_0)$.
- **Minimises** type II error $\beta = P(X \notin C^* \mid H_1)$, equivalently **maximises** power $\pi_{C^*}(\theta_1)$.

### Reduction Principle

The key insight: restrict attention to critical regions based on the **likelihood ratio**:

$$C_K = \left\{x : \frac{f(x, \theta_1)}{f(x, \theta_0)} \geq K\right\}.$$

For large $K$, $C_K$ is small (few observations lead to rejection). As $K$ decreases, $C_K$ grows.

### Theorem 62: Neyman-Pearson Lemma

**Statement:** Let $\Theta_0 = \{\theta_0\}$ and $\Theta_1 = \{\theta_1\}$. Let $C^*$ be a critical region such that there exists a constant $K > 0$ for which:

- **(a)** $\frac{f(x,\theta_1)}{f(x,\theta_0)} > K \implies x \in C^*$.
- **(b)** $\frac{f(x,\theta_1)}{f(x,\theta_0)} < K \implies x \notin C^*$.

Let $C$ be any other critical region with $\alpha_C \leq \alpha_{C^*}$. Then $\beta_C \geq \beta_{C^*}$. Moreover, if $\alpha_C < \alpha_{C^*}$, then $\beta_C > \beta_{C^*}$.

**In words:** $C^*$ is the **most powerful test** at level $\alpha_{C^*}$: no other test with the same or smaller type I error achieves smaller type II error.

### Proof Sketch

Partition the sample space into four regions based on whether $x \in C$ and $x \in C^*$:
- $A_1 = \{x: f(x,\theta_1) = 0, f(x,\theta_0) > 0\}$: Including $A_1$ in $C^*$ cannot increase $\beta$ and does not help.
- $A_2 = \{x: f(x,\theta_0) > 0, f(x,\theta_1) = 0\}$: Excluding from $C^*$ is optimal — rejecting here never helps detect $\theta_1$.
- $A_3 = \{x: f(x,\theta_0) > 0, f(x,\theta_1) > 0\}$: The key region; partition based on the likelihood ratio.

For $A_3$: reject $H_0$ when $f(x,\theta_1)/f(x,\theta_0) \geq K$ gives the best trade-off between $\alpha$ and $\beta$.

### Example: Normal Mean (One-Sided)

$X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$, $H_0: \mu = \mu_0$ vs. $H_1: \mu = \mu_1 > \mu_0$.

Likelihood ratio:
$$\frac{f(x,\mu_1)}{f(x,\mu_0)} = \exp\!\left(\frac{\mu_1-\mu_0}{\sigma^2}\sum x_i - \frac{n(\mu_1^2-\mu_0^2)}{2\sigma^2}\right).$$

This is increasing in $\bar{x} = \frac{1}{n}\sum x_i$. So $C^* = \{\bar{X} \geq c\}$ for some threshold $c$. Choosing $c = \mu_0 + z_\alpha \sigma/\sqrt{n}$ gives the UMP test for $H_1: \mu > \mu_0$ at significance level $\alpha$.

### Extension to Composite Alternatives

The Neyman-Pearson lemma applies only to simple-vs-simple testing. For composite hypotheses, the generalisation uses the **generalised likelihood ratio** (see [[Generalized_Likelihood_Ratio_Test]]).

### Interpretation

The Neyman-Pearson lemma is the most important theoretical result in hypothesis testing. It:
1. Identifies the **optimal** decision rule for simple hypotheses — the likelihood ratio test.
2. Provides the **conceptual foundation** for why likelihood-ratio-based tests (e.g., the $z$-test, $t$-test) are standard.
3. Frames hypothesis testing as a **resource allocation problem**: given a fixed budget of type I errors (significance level), maximise the ability to detect the alternative.
