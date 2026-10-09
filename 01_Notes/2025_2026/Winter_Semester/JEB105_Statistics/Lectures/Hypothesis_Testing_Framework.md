---
course: JEB105
topic: "Hypothesis Testing Framework"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, hypothesis-testing, null-hypothesis, alternative-hypothesis, critical-region]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Type_I_and_Type_II_Errors]], [[Power_Function]], [[Neyman_Pearson_Lemma]], [[p_Value]], [[Confidence_Intervals]], [[Standard_Tests_Catalog]]

---

## Hypothesis Testing Framework

### Setup

Assume a random sample $X_1, \ldots, X_n$ from a distribution with likelihood function $f(x, \theta)$, where $\theta$ is unknown. The key question shifts from "what is $\theta$?" to "does $\theta$ belong to a specific subset $\Theta_0$ of $\Theta$?"

We test:
- **Null hypothesis** $H_0: \theta \in \Theta_0$
- **Alternative hypothesis** $H_1: \theta \notin \Theta_0$, i.e., $\theta \in \Theta_1 = \Theta \setminus \Theta_0$

**Example 94:** Testing whether a coin is fair: $H_0: \theta \in \{1/2\}$ vs. $H_1: \theta \notin \{1/2\}$.

### Test and Critical Region

**Definition 47 (Lecture):** A **test** is a decision rule that says, for every possible sample $X = x$: either "reject $H_0$" or "do not reject $H_0$".

The **critical region** (rejection region) $C$ is the set of sample values for which we reject $H_0$:
$$X \in C \implies \text{reject } H_0.$$

**Definition 48 (Lecture):** A hypothesis $H_i: \theta \in \Theta_i$ is called:
- **Simple** if it completely specifies the distribution (e.g., $\Theta_i = \{\theta_0\}$).
- **Composite** if multiple parameter values remain (e.g., $H_1: \mu \neq \mu_0$).

### Size, Level, and Significance Level

**Definition 49 (Lecture):** The **size** of a test $C$ is:

$$\bar{\alpha}(C) = \sup_{\theta \in \Theta_0} \pi_C(\theta),$$

where $\pi_C(\theta) = P_\theta(X \in C)$ is the [[Power_Function]].

For a simple null $\Theta_0 = \{\theta_0\}$, the size equals the type I error probability $\alpha(\theta_0) = P(X \in C \mid \theta = \theta_0)$.

**Definition 50 (Lecture):** Any $\alpha \geq \bar{\alpha}(C)$ is called the **level** of the test $C$. A test satisfying $\bar{\alpha}(C) \leq \alpha$ is an **$\alpha$-level test**.

**Definition 51 (Lecture):** The **significance level** $\alpha_0$ is the smallest $\alpha$ such that we consider only tests with $\bar{\alpha}(C) \leq \alpha_0$.

In continuous distributions we can always find a test with size exactly equal to the desired significance level $\alpha_0$. In discrete distributions this may not be possible.

### Example: Testing the Mean in $N(\theta, 1)$ (Example 97)

$H_0: \mu = \mu_0$ (simple) vs. $H_1: \mu \neq \mu_0$ (composite, two-sided).

If the sample mean deviates too much from $\mu_0$, reject $H_0$. For threshold $K$:
$$C = \{X: |\bar{X} - \mu_0| > K\}.$$

Power function:
$$\pi_C(\mu) = P_\mu(|\bar{X} - \mu_0| > K) = 1 - P\!\left(\frac{-K+\mu_0-\mu}{1/\sqrt{n}} \leq Z \leq \frac{K+\mu_0-\mu}{1/\sqrt{n}}\right).$$

Under $H_0$ ($\mu = \mu_0$): $\pi_C(\mu_0) = P(|Z| > K\sqrt{n}) = \alpha$. Choose $K = z_{\alpha/2}/\sqrt{n}$ to achieve size $\alpha$.

### Link to Confidence Intervals

There is an **inversion duality** between tests and CIs: the set of $\theta_0$ values not rejected by the $\alpha$-level test $H_0: \theta = \theta_0$ against $H_1: \theta \neq \theta_0$ is exactly the $(1-\alpha)$-CI for $\theta$ (see [[Confidence_Intervals]]).

Formally, let $A(\theta_0) = \{x: L(x) \leq \theta_0 \leq U(x)\}$ be the acceptance region. Then $C = [A(\theta_0)]^c$ is the critical region, and $P_{\theta_0}(X \in A(\theta_0)) = 1-\alpha$.

### Philosophical Note (Neyman, 1950)

"To accept hypothesis $H$ means only to take an action $A$ rather than $B$. This does not mean that we necessarily believe that the hypothesis $H$ is true." Rejection or acceptance are practical decisions based on observed data, not definitive statements about truth. The phrase "do not reject $H_0$" is preferred over "accept $H_0$."

### Interpretation

Hypothesis testing provides a formal framework for making binary decisions under uncertainty. The setup — null hypothesis, critical region, size, level — is the common language of classical statistical inference. Understanding what the test does and does not establish (the asymmetry between $H_0$ and $H_1$, the role of the significance level) is essential for correct scientific practice.
