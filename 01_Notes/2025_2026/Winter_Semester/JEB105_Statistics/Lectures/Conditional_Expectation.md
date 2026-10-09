---
course: JEB105
topic: "Conditional Expectation"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_05_Conditional_Distributions.pdf"
tags: [JEB105, statistics, conditional-expectation, law-of-total-expectation]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_05_Conditional_Distributions.pdf]]
Related: [[Conditional_Distribution]], [[Expected_Value]], [[Variance]], [[Joint_Distribution]]

---

## Conditional Expectation

### Definition

**Definition 26 (Lecture):** For random variables $X$ and $Y$, the **conditional expectation** $E(X \mid Y)$ is defined as the random variable that takes the value

$$E(X \mid Y = y) = \begin{cases} \displaystyle\sum_i x_i P(X = x_i \mid Y = y) & \text{(discrete)} \\ \displaystyle\int_{-\infty}^{\infty} x \, g_{12}(x \mid y)\, dx & \text{(continuous)} \end{cases}$$

whenever $Y = y$. Crucially, $E(X \mid Y)$ is itself a **random variable** (a function of $Y$), not a number.

### Properties

1. **Linearity:** $E(aX + bZ \mid Y) = a E(X \mid Y) + b E(Z \mid Y)$.
2. **Pulling out known factors:** $E(g(Y) X \mid Y) = g(Y) E(X \mid Y)$.
3. **Tower property (iterated expectation):** $E[E(X \mid Y)] = E[X]$.
4. **Conditioning on the known:** $E(X \mid X) = X$.
5. **Independence:** If $X \perp Y$, then $E(X \mid Y) = E[X]$.

### Law of Total Expectation

**Theorem 30 (Lecture):** For any function $g$ with $E[|g(X)|] < \infty$:

$$E[g(X)] = E\!\left[E(g(X) \mid Y)\right].$$

**Application — Iterated Expectation in Practice:**

The law allows us to compute unconditional expectations by conditioning strategically:

$$E[X] = \sum_j E(X \mid Y = y_j) P(Y = y_j) \quad \text{(discrete $Y$)},$$

$$E[X] = \int_{-\infty}^{\infty} E(X \mid Y = y) f_Y(y)\, dy \quad \text{(continuous $Y$)}.$$

### Law of Total Variance

**Theorem 31 (Lecture):** If $E[X^2] < \infty$:

$$\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E[X \mid Y]).$$

The two terms represent:
- $E[\text{Var}(X \mid Y)]$: **within-group variance** — expected variability within each level of $Y$.
- $\text{Var}(E[X \mid Y])$: **between-group variance** — variability of the conditional means across levels of $Y$.

### Substitution Theorem

**Theorem 32 (Lecture):** For any measurable $g$ and conditioning on $Y = y$:

$$E[g(X, Y) \mid Y = y] = E[g(X, y) \mid Y = y].$$

This allows substituting the known value $y$ for $Y$ inside the expectation.

### Examples

**Example (Lecture, Ex. 59 — Eggs):** $Y \sim \text{Poi}(\lambda)$, $X \mid Y = n \sim \text{Bin}(n, p)$.
- $E(X \mid Y = n) = np$, so $E(X \mid Y) = Yp$.
- $E[X] = E[Yp] = \lambda p$. (Same as $\text{Poi}(\lambda p)$ mean.)

**Law of Total Variance applied:**
- $\text{Var}(X \mid Y = n) = np(1-p)$, so $E[\text{Var}(X \mid Y)] = E[Yp(1-p)] = \lambda p(1-p)$.
- $E[X \mid Y] = Yp$, so $\text{Var}(E[X \mid Y]) = \text{Var}(Yp) = p^2 \lambda$.
- $\text{Var}(X) = \lambda p(1-p) + \lambda p^2 = \lambda p = \text{Var}(\text{Poi}(\lambda p))$. ✓

**Example (Lecture, Ex. 59 cont. — Unhatched eggs):** Let $Z = Y - X$ (unhatched). $E(Z \mid Y = n) = n(1-p)$, which follows from the substitution theorem.

### Interpretation

The conditional expectation $E(X \mid Y)$ is the **best predictor** of $X$ given $Y$ in the mean-squared-error sense — a fundamental result of prediction theory. It is the foundation of regression analysis: the regression function $m(y) = E(X \mid Y = y)$ minimises $E[(X - g(Y))^2]$ over all measurable functions $g$. In Bayesian statistics, $E(\theta \mid X)$ is the posterior mean, the Bayes estimate under squared-error loss.
