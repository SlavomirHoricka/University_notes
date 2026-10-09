---
course: JEB105
topic: "Random Variable"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf"
tags: [JEB105, statistics, probability, random-variable, distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf]]
Related: [[Cumulative_Distribution_Function]], [[Probability_Mass_Function]], [[Probability_Density_Function]], [[Expected_Value]], [[Variance]], [[Sample_Space_and_Events]]

---

## Random Variable

### Definition

A **random variable** is a measurable function $X: \Omega \to \mathbb{R}$ from a probability space $(\Omega, \mathcal{F}, P)$ to the real line, such that for every Borel set $B \subseteq \mathbb{R}$,

$$\{\omega \in \Omega : X(\omega) \in B\} \in \mathcal{F}.$$

In the lecture notation (Definition 1), a random variable is described via its **distribution** — the probability measure $P_X$ on $\mathbb{R}$ induced by $X$:

$$P_X(B) = P(X \in B) \quad \text{for Borel sets } B.$$

The key insight is that a random variable is not itself random — it is a deterministic function. The randomness lives in the underlying experiment. The variable $X$ maps outcomes of the experiment to real numbers, allowing mathematical manipulation.

### Classification

Random variables are classified by the nature of their range:

- **Discrete** random variable: $X$ takes values in a countable set $\{x_1, x_2, \ldots\}$.
- **Continuous** random variable: $X$ has a density function; $P(X = x) = 0$ for every single point $x$.
- **Mixed**: possesses both discrete mass points and a continuous part.

### Properties

Every random variable $X$ induces a [[Cumulative_Distribution_Function]] (CDF):

$$F_X(x) = P(X \leq x), \quad x \in \mathbb{R}.$$

The CDF completely characterises the distribution of $X$. Key properties of any CDF:
1. $F$ is non-decreasing.
2. $F$ is right-continuous: $\lim_{y \downarrow x} F(y) = F(x)$.
3. $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$.
4. $P(a < X \leq b) = F(b) - F(a)$.

### Discrete Case

For a discrete random variable, the distribution is fully characterised by its [[Probability_Mass_Function]] (PMF):

$$p(x_i) = P(X = x_i) \geq 0, \quad \sum_{i} p(x_i) = 1.$$

The CDF is then a step function:

$$F(x) = \sum_{x_i \leq x} p(x_i).$$

### Continuous Case

For a continuous random variable, the distribution is fully characterised by its [[Probability_Density_Function]] (PDF) $f: \mathbb{R} \to [0, \infty)$ satisfying:

$$F(x) = \int_{-\infty}^{x} f(t)\, dt, \quad \int_{-\infty}^{\infty} f(t)\, dt = 1.$$

Probabilities are computed via:

$$P(a \leq X \leq b) = \int_a^b f(x)\, dx.$$

Note: $f(x)$ is not a probability — it can exceed 1. Only integrals of $f$ over intervals are probabilities.

### Derivation: Functions of a Random Variable

**Theorem (Lecture, Theorem 1):** Let $X$ have CDF $F_X$ and let $g: \mathbb{R} \to \mathbb{R}$ be a strictly monotone differentiable function. Then $Y = g(X)$ has PDF:

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d}{dy} g^{-1}(y)\right|.$$

**Derivation sketch:** For $g$ strictly increasing,
$$F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y)).$$
Differentiating gives the result.

### Examples

**Example 1 (Discrete):** Let $X$ be the result of a fair die roll. Then $X$ takes values in $\{1,2,3,4,5,6\}$ with $p(k) = 1/6$ for each $k$.

**Example 2 (Continuous):** Let $X \sim U(0,1)$ (uniform on $[0,1]$). Then $f(x) = 1$ for $x \in [0,1]$ and $F(x) = x$.

**Example (Lecture, Example 2):** Quantile function. For $X$ continuous with strictly increasing CDF $F$, the quantile $Q(p) = F^{-1}(p)$ satisfies $P(X \leq Q(p)) = p$. For $X \sim U(0,1)$, $Q(p) = p$.

**Probability integral transform (Theorem 2, Lecture):** If $X$ is a continuous random variable with CDF $F_X$, then $Y = F_X(X) \sim U(0,1)$.

### Interpretation

A random variable is the bridge between abstract probability theory and data. It converts qualitative outcomes (heads/tails, die faces) into numbers amenable to algebraic manipulation. The distribution of $X$ summarises all probabilistic information about $X$, and is the fundamental object studied in statistics.

Understanding whether a variable is discrete or continuous determines which mathematical tools (sums vs. integrals) apply throughout statistical inference.
