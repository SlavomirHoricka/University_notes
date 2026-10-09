---
course: JEB105
topic: "Law of Large Numbers"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, LLN, weak-LLN, strong-LLN, convergence, consistency]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Convergence_of_Random_Variables]], [[Central_Limit_Theorem]], [[Expected_Value]], [[Sample_Mean_and_Sample_Variance]], [[Bias_and_MSE]]

---

## Law of Large Numbers

### Statement

Let $X_1, X_2, \ldots$ be i.i.d. random variables with $E[X_i] = \mu < \infty$.

**Weak Law of Large Numbers (WLLN):**

$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i \xrightarrow{P} \mu \quad \text{as } n \to \infty.$$

For every $\varepsilon > 0$: $\lim_{n\to\infty} P(|\bar{X}_n - \mu| > \varepsilon) = 0$.

**Strong Law of Large Numbers (SLLN):**

$$\bar{X}_n \xrightarrow{a.s.} \mu \quad \text{as } n \to \infty.$$

$P\!\left(\lim_{n\to\infty} \bar{X}_n = \mu\right) = 1$.

### Proof of the WLLN (via Chebyshev)

If additionally $\text{Var}(X_i) = \sigma^2 < \infty$, a simple proof uses Chebyshev's inequality:

$$P(|\bar{X}_n - \mu| > \varepsilon) \leq \frac{\text{Var}(\bar{X}_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0.$$

The SLLN requires a more subtle argument (martingale theory or truncation) and holds under only the first moment condition $E|X_i| < \infty$.

### Implications for Estimation

The LLN guarantees that the sample mean $\bar{X}_n$ is a consistent estimator of $\mu$:

$$\bar{X}_n \xrightarrow{P} \mu.$$

More generally, by the **continuous mapping theorem**, if $g$ is continuous then:

$$g(\bar{X}_n) \xrightarrow{P} g(\mu).$$

**Application — Method of Moments:** If $E[g(X_i)] = h(\theta)$ for some function $g$, then $\frac{1}{n}\sum g(X_i) \xrightarrow{P} h(\theta)$ by LLN. Setting the sample moment equal to $h(\theta)$ and solving gives a consistent MoM estimator (see [[Method_of_Moments]]).

### Intuition

The LLN formalises the intuition behind frequency probability: if we repeat an experiment many times, the empirical average of outcomes converges to the theoretical mean. For example:
- Rolling a die many times: the average converges to 3.5.
- Tossing a fair coin: the proportion of heads converges to 0.5.

### Weak vs. Strong

| Property | WLLN | SLLN |
|---|---|---|
| Mode of convergence | In probability | Almost surely |
| Required moment | $E|X| < \infty$ (+ finite variance for Chebyshev proof) | $E|X| < \infty$ |
| Strength | Weaker | Stronger |

In practice, the distinction rarely matters for statistical applications — the WLLN suffices to establish consistency of most estimators.

### Connection to the Central Limit Theorem

The LLN tells us that $\bar{X}_n \to \mu$. The [[Central_Limit_Theorem]] goes further and describes the rate of convergence and the limiting distribution of the normalised deviation $\sqrt{n}(\bar{X}_n - \mu)$.
