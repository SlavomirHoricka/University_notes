---
course: JEB105
topic: "Marginal Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_03_Multivariate_Distributions-1.pdf"
tags: [JEB105, statistics, marginal-distribution, multivariate]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_03_Multivariate_Distributions-1.pdf]]
Related: [[Joint_Distribution]], [[Conditional_Distribution]], [[Independence_of_Random_Variables]], [[Random_Variable]]

---

## Marginal Distribution

### Definition

Given a random vector $(X, Y)$ with [[Joint_Distribution]], the **marginal distribution** of $X$ is the distribution of $X$ alone, obtained by integrating (or summing) out all other variables.

**Discrete case:** If $(X, Y)$ has joint PMF $p(x_i, y_j)$, then the marginal PMF of $X$ is:

$$p_X(x_i) = P(X = x_i) = \sum_{j} p(x_i, y_j).$$

**Continuous case:** If $(X, Y)$ has joint PDF $f(x, y)$, then the marginal PDF of $X$ is:

$$f_X(x) = \int_{-\infty}^{\infty} f(x, y)\, dy.$$

Similarly for $Y$: $f_Y(y) = \int_{-\infty}^{\infty} f(x, y)\, dx$.

### Properties

1. Each marginal distribution is a valid probability distribution.
2. The joint distribution determines the marginals, but **not vice versa**. Two random vectors can have the same marginals but different joint distributions — the missing information is the dependence structure.
3. If $X$ and $Y$ are [[Independence_of_Random_Variables|independent]], then the joint distribution is the product of the marginals: $f(x,y) = f_X(x) f_Y(y)$.

### Derivation

The marginal CDF is obtained from the joint CDF:

$$F_X(x) = \lim_{y \to \infty} F(x, y) = P(X \leq x, Y < \infty) = P(X \leq x).$$

For continuous variables, differentiation yields the marginal PDF as above.

### Examples

**Example 1:** Joint PDF $f(x,y) = 6x$ for $0 \leq x \leq y \leq 1$.
- $f_X(x) = \int_x^1 6x\, dy = 6x(1-x)$, for $x \in [0,1]$.
- $f_Y(y) = \int_0^y 6x\, dx = 3y^2$, for $y \in [0,1]$.

**Example 2 (Lecture):** Joint PDF $f(x,y) = cxy^2$ on $[0,1]^2$. Marginals: $f_X(x) = cx/3$ and $f_Y(y) = cy^2/2$.

**Example 3 (Bivariate Normal):** If $(X, Y) \sim N_2(\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho)$, then $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ marginally (regardless of the correlation $\rho$).

### Interpretation

The marginal distribution answers: "What is the distribution of $X$, if we discard all information about $Y$?" It is the natural single-variable summary in a multivariate setting. In regression analysis, the marginal distribution of $Y$ is the unconditional distribution of the outcome, which is the mixture of conditional distributions $f(y|x)$ weighted by $f_X(x)$.
