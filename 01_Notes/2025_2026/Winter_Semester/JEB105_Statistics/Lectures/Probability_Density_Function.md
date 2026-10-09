---
course: JEB105
topic: "Probability Density Function"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf"
tags: [JEB105, statistics, PDF, continuous, distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_02_Random_Variables-4.pdf]]
Related: [[Random_Variable]], [[Cumulative_Distribution_Function]], [[Probability_Mass_Function]], [[Expected_Value]], [[Normal_Distribution]]

---

## Probability Density Function

### Definition

A [[Random_Variable]] $X$ is **continuous** if there exists a non-negative, integrable function $f: \mathbb{R} \to [0, \infty)$ — called the **probability density function** (PDF) — such that the [[Cumulative_Distribution_Function]] satisfies

$$F(x) = P(X \leq x) = \int_{-\infty}^{x} f(t)\, dt, \quad \forall x \in \mathbb{R}.$$

### Properties

A valid PDF satisfies:

1. **Non-negativity:** $f(x) \geq 0$ for all $x$.
2. **Normalisation:** $\displaystyle\int_{-\infty}^{\infty} f(x)\, dx = 1$.
3. **Point probabilities:** $P(X = x) = 0$ for any single point $x$.
4. **Interval probabilities:** $P(a \leq X \leq b) = \displaystyle\int_a^b f(x)\, dx$.
5. **Density recovery:** At points of continuity of $f$: $f(x) = F'(x)$.

**Important:** $f(x)$ is NOT a probability. It can exceed 1 (e.g., $U(0, 0.1)$ has $f(x) = 10$). Only integrals of $f$ yield probabilities.

### Derivation: PDF of a Transformed Variable

Let $X$ have PDF $f_X$ and let $Y = g(X)$ where $g$ is strictly increasing and differentiable. Then:

$$F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y)).$$

Differentiating:

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d}{dy}g^{-1}(y).$$

For strictly decreasing $g$, the formula uses the absolute value:

$$f_Y(y) = f_X(g^{-1}(y)) \cdot \left|\frac{d}{dy}g^{-1}(y)\right|.$$

### Examples

**Example 1 (Uniform):** $X \sim U(a, b)$:
$$f(x) = \frac{1}{b-a} \cdot \mathbf{1}_{[a,b]}(x).$$

**Example 2 (Exponential):** $X \sim \text{Exp}(\lambda)$, $\lambda > 0$:
$$f(x) = \lambda e^{-\lambda x} \cdot \mathbf{1}_{[0,\infty)}(x).$$

**Example 3 (Normal):** $X \sim N(\mu, \sigma^2)$:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).$$

**Example 4 (Transformation):** If $X \sim U(0,1)$ and $Y = -\ln(X)/\lambda$, then $Y \sim \text{Exp}(\lambda)$. Proof via CDF: $P(Y \leq y) = P(X \geq e^{-\lambda y}) = 1 - e^{-\lambda y}$.

### Interpretation

The PDF is a "density" in the sense of density from physics: $f(x)$ tells us how much probability mass is concentrated near the point $x$ per unit length. The probability of $X$ falling in a small interval $(x, x + dx)$ is approximately $f(x)\, dx$.

In Bayesian statistics, continuous prior and posterior distributions are represented as PDFs. In maximum likelihood estimation (see [[Maximum_Likelihood_Estimation]]), the PDF evaluated at observed data gives the likelihood contribution of each observation.
