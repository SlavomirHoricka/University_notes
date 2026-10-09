---
course: JEB105
topic: "Variance"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf"
tags: [JEB105, statistics, variance, spread, moments]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf]]
Related: [[Expected_Value]], [[Covariance_and_Correlation]], [[Standard_Error]], [[Moment_Generating_Function]], [[Measures_of_Dispersion]]

---

## Variance

### Definition

The **variance** of a [[Random_Variable]] $X$ with mean $\mu = E[X]$ is:

$$\text{Var}(X) = \sigma^2 = E\!\left[(X - \mu)^2\right].$$

Equivalently:

$$\text{Var}(X) = E[X^2] - (E[X])^2.$$

The **standard deviation** is $\sigma = \sqrt{\text{Var}(X)}$.

### Properties

1. **Non-negativity:** $\text{Var}(X) \geq 0$, with equality iff $X$ is a.s. constant.
2. **Shift invariance:** $\text{Var}(X + c) = \text{Var}(X)$ for any constant $c$.
3. **Scaling:** $\text{Var}(aX) = a^2 \text{Var}(X)$ for any constant $a$.
4. **Sum formula:** $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y)$.
5. **Independence:** If $X \perp Y$: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$.
6. **General linear combination:** $\text{Var}\!\left(\sum_i a_i X_i\right) = \sum_i a_i^2 \text{Var}(X_i) + 2\sum_{i < j} a_i a_j \text{Cov}(X_i, X_j)$.

### Derivation of the Computational Formula

$$\text{Var}(X) = E[(X-\mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2.$$

Since $E[X] = \mu$: $\text{Var}(X) = E[X^2] - 2\mu^2 + \mu^2 = E[X^2] - \mu^2$.

### Variance of Common Distributions

**Bernoulli $\text{Ber}(p)$:**
$$\text{Var}(X) = E[X^2] - p^2 = p - p^2 = p(1-p).$$

**Binomial $\text{Bin}(n,p)$:** By independence of Bernoulli trials:
$$\text{Var}(X) = n \cdot p(1-p).$$

**Poisson $\text{Poi}(\lambda)$:**
$$\text{Var}(X) = \lambda.$$
(Mean equals variance — a key identifying property of the Poisson.)

**Uniform $U(a,b)$:**
$$\text{Var}(X) = \frac{(b-a)^2}{12}.$$

**Exponential $\text{Exp}(\lambda)$:**
$$\text{Var}(X) = \frac{1}{\lambda^2}.$$

**Normal $N(\mu, \sigma^2)$:** Variance is $\sigma^2$ by definition of the parametrisation.

### Chebyshev's Inequality

Variance controls tail probabilities via [[Expected_Value|Chebyshev's Inequality]]:

$$P(|X - \mu| \geq k) \leq \frac{\text{Var}(X)}{k^2} \quad \text{for all } k > 0.$$

Equivalently, $P(|X - \mu| \geq k\sigma) \leq 1/k^2$.

This is distribution-free and applies to any random variable with finite variance.

### Interpretation

Variance measures the **spread** of a distribution around its mean. Larger variance means values are more spread out. The standard deviation $\sigma$ is in the same units as $X$ and is typically more interpretable.

In estimation, the variance of an estimator $\hat{\theta}$ quantifies its precision (see [[Point_Estimation]]). The trade-off between bias and variance is a central theme of estimation theory: the MSE decomposes as $\text{MSE}(\hat{\theta}) = \text{Bias}^2 + \text{Var}(\hat{\theta})$.
