---
course: JEB105
topic: "Probability Mass Function"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf"
tags: [JEB105, statistics, PMF, discrete, distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf]]
Related: [[Random_Variable]], [[Cumulative_Distribution_Function]], [[Probability_Density_Function]], [[Expected_Value]]

---

## Probability Mass Function

### Definition

For a **discrete** [[Random_Variable]] $X$ taking values in a countable set $\mathcal{X} = \{x_1, x_2, \ldots\}$, the **probability mass function** (PMF) is the function $p: \mathcal{X} \to [0,1]$ defined by

$$p(x) = P(X = x), \quad x \in \mathcal{X}.$$

### Properties

A valid PMF satisfies:

1. **Non-negativity:** $p(x) \geq 0$ for all $x$.
2. **Normalisation:** $\displaystyle\sum_{x \in \mathcal{X}} p(x) = 1$.

The [[Cumulative_Distribution_Function]] is recovered via:

$$F(x) = P(X \leq x) = \sum_{x_i \leq x} p(x_i).$$

Probabilities of any event $A \subseteq \mathcal{X}$ are computed as:

$$P(X \in A) = \sum_{x \in A} p(x).$$

### Examples

**Example 1 (Bernoulli):** $X \sim \text{Ber}(p)$, $\mathcal{X} = \{0, 1\}$.
$$p(0) = 1 - p, \quad p(1) = p.$$

**Example 2 (Binomial):** $X \sim \text{Bin}(n, p)$, $\mathcal{X} = \{0, 1, \ldots, n\}$.
$$p(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n.$$

**Example 3 (Poisson):** $X \sim \text{Poi}(\lambda)$, $\mathcal{X} = \{0, 1, 2, \ldots\}$.
$$p(k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

**Example 4 (Geometric):** $X \sim \text{Geom}(p)$ (number of trials until first success), $\mathcal{X} = \{1, 2, \ldots\}$.
$$p(k) = (1-p)^{k-1} p, \quad k = 1, 2, \ldots$$

### Interpretation

The PMF assigns a probability mass to each possible value of the discrete random variable. Unlike the [[Probability_Density_Function]], the PMF value itself is a probability. The PMF can be visualised as a bar chart where the height of each bar equals the probability of the corresponding outcome.

In the context of statistical inference, the PMF appears in the likelihood function for discrete models: if $X_1, \ldots, X_n$ are i.i.d. with PMF $p(x; \theta)$, the likelihood is $\prod_{i=1}^n p(x_i; \theta)$.
