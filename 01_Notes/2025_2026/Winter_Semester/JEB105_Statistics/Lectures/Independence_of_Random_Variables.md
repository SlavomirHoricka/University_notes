---
course: JEB105
topic: "Independence of Random Variables"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_03_Multivariate_Distributions-1.pdf"
tags: [JEB105, statistics, independence, random-variable, joint-distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_03_Multivariate_Distributions-1.pdf]]
Related: [[Joint_Distribution]], [[Marginal_Distribution]], [[Covariance_and_Correlation]], [[Independence_of_Events]]

---

## Independence of Random Variables

### Definition

Random variables $X$ and $Y$ are **independent** if for all Borel sets $A, B \subseteq \mathbb{R}$:

$$P(X \in A, Y \in B) = P(X \in A) \cdot P(Y \in B).$$

**Equivalent characterisations:**

1. **Via CDF:** $F(x, y) = F_X(x) \cdot F_Y(y)$ for all $x, y \in \mathbb{R}$.
2. **Via PDF (continuous case):** $f(x, y) = f_X(x) \cdot f_Y(y)$ for all $x, y$.
3. **Via PMF (discrete case):** $p(x_i, y_j) = p_X(x_i) \cdot p_Y(y_j)$ for all $i, j$.

More generally, $X_1, \ldots, X_n$ are **mutually independent** if:

$$P(X_1 \in A_1, \ldots, X_n \in A_n) = \prod_{i=1}^n P(X_i \in A_i)$$

for all Borel sets $A_1, \ldots, A_n$.

### Properties

**Theorem:** If $X$ and $Y$ are independent, then for any measurable functions $g$ and $h$:

$$E[g(X) h(Y)] = E[g(X)] \cdot E[h(Y)],$$

provided the expectations exist.

**Corollary:** Independence implies zero [[Covariance_and_Correlation|covariance]]:

$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0.$$

**Warning:** $\text{Cov}(X,Y) = 0$ (uncorrelatedness) does NOT imply independence in general. The converse holds for jointly normal variables: if $(X,Y)$ is bivariate normal and $\text{Cov}(X,Y) = 0$, then $X \perp Y$.

**Product of MGFs:** If $X \perp Y$, then the MGF of $Z = X + Y$ satisfies:

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t).$$

### Testing Independence

In the discrete bivariate case, a necessary and sufficient condition for independence is that the joint PMF factors:

$$p_{ij} = p_{i\cdot} \cdot p_{\cdot j} \quad \text{for all } i, j.$$

This can be checked by computing the product of marginals and comparing with the joint table.

### Derivation: Independence and Functions

**Theorem:** If $X_1, \ldots, X_n$ are mutually independent and $g_i$ are measurable functions, then $g_1(X_1), \ldots, g_n(X_n)$ are also mutually independent.

**Proof sketch:** For Borel sets $B_i$: $P(g_i(X_i) \in B_i) = P(X_i \in g_i^{-1}(B_i))$. Independence of $X_i$'s then gives the result.

### Examples

**Example 1:** Let $X, Y \sim U(0,1)$ i.i.d. Then $f(x,y) = 1$ on $[0,1]^2$, and $f_X(x) = f_Y(y) = 1$, so $f(x,y) = f_X(x) f_Y(y)$ — independent.

**Example 2 (Dependence):** Let $(X,Y)$ have joint PDF $f(x,y) = 2$ on $\{0 < x < y < 1\}$. Marginals: $f_X(x) = 2(1-x)$, $f_Y(y) = 2y$. Product: $4y(1-x) \neq 2 = f(x,y)$ — not independent.

**Example 3 (Zero covariance, not independent):** Let $X \sim U(-1,1)$ and $Y = X^2$. Then $\text{Cov}(X,Y) = E[X^3] - E[X]E[X^2] = 0 - 0 = 0$, yet $Y$ is a deterministic function of $X$.

### Interpretation

Independence is the probabilistic formalisation of "knowing $X$ tells you nothing about $Y$." It is the key assumption enabling tractable statistical inference: if observations are i.i.d. (independent and identically distributed), the joint likelihood factors into a product of marginal likelihoods, which is the basis of classical estimation theory (see [[Maximum_Likelihood_Estimation]], [[Point_Estimation]]).
