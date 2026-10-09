---
course: JEB105
topic: "Joint Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_03_Multivariate_Distributions-1.pdf"
tags: [JEB105, statistics, joint-distribution, multivariate, random-vector]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_03_Multivariate_Distributions-1.pdf]]
Related: [[Random_Variable]], [[Marginal_Distribution]], [[Conditional_Distribution]], [[Independence_of_Random_Variables]], [[Covariance_and_Correlation]]

---

## Joint Distribution

### Definition

Let $X_1, \ldots, X_n$ be [[Random_Variable]]s defined on the same probability space $(\Omega, \mathcal{F}, P)$. The **random vector** $(X_1, \ldots, X_n)$ has a **joint distribution** characterised by its **joint CDF**:

$$F(x_1, \ldots, x_n) = P(X_1 \leq x_1, \ldots, X_n \leq x_n).$$

In the bivariate case $(X, Y)$:

$$F(x, y) = P(X \leq x, Y \leq y).$$

### Discrete Case: Joint PMF

For a discrete random vector, the **joint probability mass function** is:

$$p(x_i, y_j) = P(X = x_i, Y = y_j) \geq 0,$$

with normalisation $\displaystyle\sum_i \sum_j p(x_i, y_j) = 1$.

The **marginal PMFs** are recovered by summing out the other variable:

$$p_X(x_i) = \sum_j p(x_i, y_j) = p_{i\cdot}, \qquad p_Y(y_j) = \sum_i p(x_i, y_j) = p_{\cdot j}.$$

### Continuous Case: Joint PDF

For a continuous random vector, the **joint probability density function** $f: \mathbb{R}^2 \to [0, \infty)$ satisfies:

$$F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(s, t)\, dt\, ds,$$

$$f(x, y) = \frac{\partial^2 F}{\partial x \, \partial y}(x, y) \quad \text{(where it exists)},$$

$$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\, dx\, dy = 1.$$

**Marginal PDFs:**
$$f_X(x) = \int_{-\infty}^{\infty} f(x, y)\, dy, \qquad f_Y(y) = \int_{-\infty}^{\infty} f(x, y)\, dx.$$

### Properties

1. The joint distribution determines all marginal and [[Conditional_Distribution|conditional distributions]].
2. Marginal distributions do **not** determine the joint distribution in general — the dependence structure is additional information (captured by the [[Covariance_and_Correlation|copula]] or covariance).
3. Probabilities of events: $P((X,Y) \in A) = \iint_A f(x,y)\, dx\, dy$ for Borel $A \subseteq \mathbb{R}^2$.

### Derivation: Multivariate Transformations

**Theorem (Bivariate Jacobian):** Let $(X, Y)$ have joint PDF $f_{X,Y}$ and let $g: \mathbb{R}^2 \to \mathbb{R}^2$ be a bijective, differentiable transformation with inverse $(u, v) = g^{-1}(x, y)$. Then $(U, V) = g(X, Y)$ has joint PDF:

$$f_{U,V}(u, v) = f_{X,Y}(x(u,v),\, y(u,v)) \cdot |J|,$$

where $J$ is the **Jacobian determinant**:

$$J = \det \begin{pmatrix} \partial x/\partial u & \partial x/\partial v \\ \partial y/\partial u & \partial y/\partial v \end{pmatrix}.$$

**Example (Sum of two continuous RVs):** Let $Z = X + Y$. The density of $Z$ is the convolution:

$$f_Z(z) = \int_{-\infty}^{\infty} f_{X,Y}(x, z-x)\, dx.$$

If $X$ and $Y$ are independent: $f_Z(z) = \int_{-\infty}^{\infty} f_X(x) f_Y(z-x)\, dx = (f_X * f_Y)(z)$.

**Example (Lecture, Ex. 27 — Triangular Distribution):** If $X, Y \sim U(0,1)$ independent, then $Z = X + Y$ has the triangular distribution on $[0,2]$ with PDF:
$$f_Z(z) = \begin{cases} z & 0 \leq z \leq 1 \\ 2 - z & 1 < z \leq 2. \end{cases}$$

### Examples

**Example (Lecture, Ex. 22):** Let $(X, Y)$ have joint PDF $f(x, y) = cxy$ on $[0,1]^2$.
- Normalisation: $c \int_0^1 \int_0^1 xy\, dx\, dy = c/4 = 1 \implies c = 4$.
- Marginal: $f_X(x) = \int_0^1 4xy\, dy = 2x$.
- Marginal: $f_Y(y) = 2y$.
- Since $f(x,y) = f_X(x) f_Y(y)$, $X$ and $Y$ are independent.

### Interpretation

The joint distribution is the probabilistic model for how multiple random variables interact. In econometrics, the joint distribution of outcomes and regressors is the foundational object. Most statistical models are specifications of a conditional distribution derived from the joint distribution via $f(y|x) = f(x,y)/f_X(x)$.
