---
course: JEB105
topic: "Cumulative Distribution Function"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf"
tags: [JEB105, statistics, CDF, distribution, random-variable]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf]]
Related: [[Random_Variable]], [[Probability_Mass_Function]], [[Probability_Density_Function]], [[Kolmogorov_Axioms]]

---

## Cumulative Distribution Function

### Definition

The **cumulative distribution function** (CDF) of a random variable $X$ is the function $F_X: \mathbb{R} \to [0,1]$ defined by

$$F_X(x) = P(X \leq x), \quad x \in \mathbb{R}.$$

The CDF is the canonical representation of a [[Random_Variable]]'s distribution. Unlike the PDF or PMF, every random variable — discrete, continuous, or mixed — possesses a CDF.

### Properties

**Theorem (Characterisation of CDFs):** A function $F: \mathbb{R} \to [0,1]$ is a valid CDF if and only if:

1. **Non-decreasing:** $x_1 \leq x_2 \implies F(x_1) \leq F(x_2)$.
2. **Right-continuous:** $\lim_{y \downarrow x} F(y) = F(x)$ for all $x$.
3. **Boundary limits:** $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to +\infty} F(x) = 1$.

These three properties are necessary and sufficient.

Additional derived identities:
- $P(a < X \leq b) = F(b) - F(a)$
- $P(X > x) = 1 - F(x)$ (the **survival function** or **CCDF**)
- $P(X = x) = F(x) - F(x^-)$ where $F(x^-) = \lim_{y \uparrow x} F(y)$ is the left limit.
- For continuous $X$: $P(X = x) = 0$ for all $x$, and $F$ is continuous everywhere.

### Discrete Case

For a discrete random variable with PMF $p(x_i)$, the CDF is a right-continuous step function:

$$F(x) = \sum_{x_i \leq x} p(x_i).$$

The CDF jumps at each mass point $x_i$ by $p(x_i)$.

### Continuous Case

For a continuous random variable with PDF $f$:

$$F(x) = \int_{-\infty}^{x} f(t)\, dt.$$

At every point where $f$ is continuous, $F'(x) = f(x)$ by the Fundamental Theorem of Calculus.

### Derivation: Probability Computation

For any interval $(a, b]$:

$$P(a < X \leq b) = F(b) - F(a).$$

**Proof:** $\{X \leq b\} = \{X \leq a\} \cup \{a < X \leq b\}$ (disjoint union), so by [[Kolmogorov_Axioms]] countable additivity: $P(X \leq b) = P(X \leq a) + P(a < X \leq b)$.

### Examples

**Example 1:** $X \sim \text{Bernoulli}(p)$. Then
$$F(x) = \begin{cases} 0 & x < 0 \\ 1-p & 0 \leq x < 1 \\ 1 & x \geq 1. \end{cases}$$

**Example 2:** $X \sim U(a,b)$ (uniform). Then
$$F(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b. \end{cases}$$

**Example 3:** $X \sim \text{Exp}(\lambda)$. Then $F(x) = 1 - e^{-\lambda x}$ for $x \geq 0$.

### Interpretation

The CDF gives the probability that $X$ does not exceed a given threshold. It provides a unified, complete description of the distribution that does not require distinguishing between discrete and continuous cases. In statistics, CDFs are used to:

- Compute quantiles: $Q(p) = \inf\{x : F(x) \geq p\}$.
- Define the **probability integral transform**: if $F$ is continuous and strictly increasing, $F(X) \sim U(0,1)$.
- Compare distributions via the **empirical CDF** in non-parametric tests (see [[Kolmogorov_Smirnov_Test]]).
