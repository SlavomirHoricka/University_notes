---
course: JEB105
topic: "Expected Value"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf"
tags: [JEB105, statistics, expectation, expected-value, moments]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf]]
Related: [[Random_Variable]], [[Variance]], [[Moment_Generating_Function]], [[Covariance_and_Correlation]], [[Conditional_Expectation]]

---

## Expected Value

### Definition

The **expected value** (or **expectation**, or **mean**) of a [[Random_Variable]] $X$ is:

**Discrete case:** If $X$ takes values $x_1, x_2, \ldots$ with PMF $p(x_i)$:

$$E[X] = \sum_i x_i \, p(x_i),$$

provided $\sum_i |x_i| p(x_i) < \infty$ (absolute convergence required).

**Continuous case:** If $X$ has PDF $f$:

$$E[X] = \int_{-\infty}^{\infty} x \, f(x)\, dx,$$

provided $\int_{-\infty}^{\infty} |x| f(x)\, dx < \infty$.

**General (LOTUS — Law of the Unconscious Statistician):** For any measurable function $g$:

$$E[g(X)] = \sum_i g(x_i) p(x_i) \quad \text{(discrete)}, \qquad E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x)\, dx \quad \text{(continuous)}.$$

### Properties

**Theorem (Linearity of Expectation):** For random variables $X, Y$ and constants $a, b$:

$$E[aX + bY] = a E[X] + b E[Y],$$

regardless of whether $X$ and $Y$ are independent.

**Theorem (Monotonicity):** If $X \leq Y$ a.s., then $E[X] \leq E[Y]$.

**Theorem (Independence):** If $X \perp Y$, then $E[XY] = E[X] E[Y]$.

### Moments

The **$k$-th moment** of $X$ about the origin is $\mu'_k = E[X^k]$.

The **$k$-th central moment** is $\mu_k = E[(X - \mu)^k]$ where $\mu = E[X]$.

Key moments:
- $\mu'_1 = E[X] = \mu$ (mean)
- $\mu_2 = E[(X-\mu)^2] = \text{Var}(X)$ (variance)
- $\mu_3 / \sigma^3$ = skewness
- $\mu_4 / \sigma^4 - 3$ = excess kurtosis

### Variance

The **variance** of $X$ is:

$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2.$$

**Proof of the identity:**
$$E[(X-\mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - \mu^2.$$

**Standard deviation:** $\sigma = \sqrt{\text{Var}(X)}$.

**Variance of a linear combination:** $\text{Var}(aX + b) = a^2 \text{Var}(X)$.

**Variance of a sum:** $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$.

If $X \perp Y$: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$.

### Examples of Standard Distributions

| Distribution | $E[X]$ | $\text{Var}(X)$ |
|---|---|---|
| $\text{Ber}(p)$ | $p$ | $p(1-p)$ |
| $\text{Bin}(n,p)$ | $np$ | $np(1-p)$ |
| $\text{Poi}(\lambda)$ | $\lambda$ | $\lambda$ |
| $U(a,b)$ | $(a+b)/2$ | $(b-a)^2/12$ |
| $\text{Exp}(\lambda)$ | $1/\lambda$ | $1/\lambda^2$ |
| $N(\mu, \sigma^2)$ | $\mu$ | $\sigma^2$ |

### Derivation: E[X] for Exponential

Let $X \sim \text{Exp}(\lambda)$ with $f(x) = \lambda e^{-\lambda x}$:

$$E[X] = \int_0^{\infty} x \lambda e^{-\lambda x}\, dx.$$

Integration by parts with $u = x$, $dv = \lambda e^{-\lambda x} dx$:

$$= \left[-x e^{-\lambda x}\right]_0^{\infty} + \int_0^{\infty} e^{-\lambda x}\, dx = 0 + \left[-\frac{1}{\lambda} e^{-\lambda x}\right]_0^{\infty} = \frac{1}{\lambda}.$$

### Inequalities

**Jensen's Inequality:** If $g$ is convex and $E[X]$ exists:
$$g(E[X]) \leq E[g(X)].$$

Consequence: $E[X]^2 \leq E[X^2]$, $(E[X])^{1/2} \geq E[X^{1/2}]$ (for non-negative $X$).

**Markov's Inequality:** For $X \geq 0$ and $a > 0$:
$$P(X \geq a) \leq \frac{E[X]}{a}.$$

**Chebyshev's Inequality:** For any $k > 0$:
$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}.$$

### Interpretation

The expected value is the probability-weighted average of all possible values of $X$. It is the "centre of mass" of the distribution. In repeated experiments, the sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$ converges to $E[X]$ by the [[Law_of_Large_Numbers]] — the foundational justification for using averages as estimates of means.
