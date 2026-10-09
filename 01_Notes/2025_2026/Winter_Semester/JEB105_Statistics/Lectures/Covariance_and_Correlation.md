---
course: JEB105
topic: "Covariance and Correlation"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf"
tags: [JEB105, statistics, covariance, correlation, dependence]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf]]
Related: [[Expected_Value]], [[Variance]], [[Independence_of_Random_Variables]], [[Joint_Distribution]], [[Measures_of_Association]]

---

## Covariance and Correlation

### Definition

**Covariance:** For random variables $X$ and $Y$ with means $\mu_X = E[X]$ and $\mu_Y = E[Y]$, the **covariance** is:

$$\text{Cov}(X, Y) = E\!\left[(X - \mu_X)(Y - \mu_Y)\right] = E[XY] - E[X] E[Y].$$

**Correlation (Pearson):** The **correlation coefficient** standardises the covariance:

$$\rho(X, Y) = \text{Corr}(X, Y) = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)} \cdot \sqrt{\text{Var}(Y)}} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}.$$

### Properties

**Theorem (Cauchy-Schwarz Inequality):** $|\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y$, hence $-1 \leq \rho(X,Y) \leq 1$.

- $\rho = 1$: Perfect positive linear relationship ($Y = aX + b$ a.s., $a > 0$).
- $\rho = -1$: Perfect negative linear relationship.
- $\rho = 0$: **Uncorrelated** (but not necessarily independent).

**Symmetry:** $\text{Cov}(X, Y) = \text{Cov}(Y, X)$.

**Self-covariance:** $\text{Cov}(X, X) = \text{Var}(X)$.

**Bilinearity:**
$$\text{Cov}(aX + bY, Z) = a \, \text{Cov}(X, Z) + b \, \text{Cov}(Y, Z).$$

**Independence implies zero covariance:**

If $X \perp Y$, then $\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = E[X]E[Y] - E[X]E[Y] = 0$.

**Converse fails:** $\text{Cov}(X,Y) = 0$ does not imply independence.

### Covariance Matrix

For a random vector $\mathbf{X} = (X_1, \ldots, X_n)^T$, the **covariance matrix** is:

$$\Sigma = \text{Cov}(\mathbf{X}) = E\!\left[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T\right],$$

with $\Sigma_{ij} = \text{Cov}(X_i, X_j)$. The covariance matrix is always **positive semi-definite**.

For a linear transformation $\mathbf{Y} = A\mathbf{X}$: $\text{Cov}(\mathbf{Y}) = A \Sigma A^T$.

### Variance of a Sum

Using bilinearity:

$$\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2 \sum_{i < j} \text{Cov}(X_i, X_j).$$

If all $X_i$ are pairwise uncorrelated: $\text{Var}\!\left(\sum X_i\right) = \sum \text{Var}(X_i)$.

### Derivation of Cauchy-Schwarz

For any $t \in \mathbb{R}$: $0 \leq \text{Var}(X + tY) = \text{Var}(X) + 2t\,\text{Cov}(X,Y) + t^2 \text{Var}(Y)$.

This quadratic in $t$ is non-negative, so its discriminant $\leq 0$:

$$4\,\text{Cov}(X,Y)^2 - 4\,\text{Var}(X)\,\text{Var}(Y) \leq 0 \implies |\text{Cov}(X,Y)| \leq \sigma_X \sigma_Y.$$

### Examples

**Example 1:** $(X,Y)$ joint PDF $f(x,y) = 4xy$ on $[0,1]^2$. Since $X \perp Y$ (joint = product of marginals), $\text{Cov}(X,Y) = 0$.

**Example 2:** $X \sim U(-1,1)$, $Y = X^2$. Then $\text{Cov}(X,Y) = E[X^3] - E[X]E[X^2] = 0 - 0 \cdot \frac{1}{3} = 0$, yet $Y$ is a deterministic function of $X$.

**Example 3:** For the bivariate normal distribution with parameters $\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho$: $\text{Corr}(X,Y) = \rho$, and $X \perp Y \iff \rho = 0$.

### Interpretation

Covariance measures the direction of linear co-movement between $X$ and $Y$. Positive covariance means $X$ and $Y$ tend to be above their means together. Correlation normalises this to a dimensionless quantity bounded in $[-1, 1]$, making it comparable across different scales.

In econometrics, correlation is the starting point for studying linear relationships between variables, leading to regression analysis. In portfolio theory, the covariance matrix of asset returns determines portfolio variance.
