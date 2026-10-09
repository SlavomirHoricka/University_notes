---
course: JEB105
topic: "Conditional Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_05_Conditional_Distributions.pdf"
tags: [JEB105, statistics, conditional-distribution, conditioning, Bayes]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_05_Conditional_Distributions.pdf]]
Related: [[Joint_Distribution]], [[Marginal_Distribution]], [[Conditional_Expectation]], [[Independence_of_Random_Variables]], [[Total_Probability_and_Bayes_Theorem]]

---

## Conditional Distribution

### Definition

**Definition 25 (Lecture):** The **conditional distribution** of $X$ given $Y = y$ describes the distribution of $X$ when the value of $Y$ is fixed at $y$.

**Discrete case:** If $P(Y = y_j) > 0$:

$$P(X = x_i \mid Y = y_j) = \frac{P(X = x_i, Y = y_j)}{P(Y = y_j)} = \frac{p(x_i, y_j)}{p_{\cdot j}}.$$

This is a valid PMF in $x_i$ for each fixed $y_j$.

**Continuous case (conditional density):** The **conditional PDF** of $X$ given $Y = y$ is:

$$g_{12}(x \mid y) = \frac{f(x, y)}{f_Y(y)}, \quad \text{provided } f_Y(y) > 0.$$

Similarly, the conditional density of $Y$ given $X = x$ is:

$$g_{21}(y \mid x) = \frac{f(x, y)}{f_X(x)}, \quad \text{provided } f_X(x) > 0.$$

### Properties

1. $g_{12}(x \mid y) \geq 0$ and $\int_{-\infty}^{\infty} g_{12}(x \mid y)\, dx = 1$ — it is a valid density.
2. **Reconstruction of joint:** $f(x, y) = g_{12}(x \mid y) \cdot f_Y(y) = g_{21}(y \mid x) \cdot f_X(x)$.
3. **Independence:** $X \perp Y \iff g_{12}(x \mid y) = f_X(x)$ for all $x, y$.
4. **Conditional CDF:** $F_X(t \mid Y \in Q_2) = P(X \leq t \mid Y \in Q_2)$.

### Conditional Expectation

**Definition 26 (Lecture):** The **conditional expectation** $E(X \mid Y)$ is the random variable with value $E(X \mid Y = y)$ when $Y = y$:

**Discrete:** $E(X \mid Y = y_j) = \sum_i x_i P(X = x_i \mid Y = y_j)$.

**Continuous:** $E(X \mid Y = y) = \int_{-\infty}^{\infty} x \, g_{12}(x \mid y)\, dx$.

More generally, for a function $g$:
$$E(g(X) \mid Y = y) = \int_{-\infty}^{\infty} g(x) \, g_{12}(x \mid y)\, dx.$$

### Key Theorems

**Theorem 30 — Iterated Expectation (Law of Total Expectation, Lecture):**

$$E\!\left[E(g(X) \mid Y)\right] = E[g(X)],$$

provided $E[g(X)]$ exists.

**Proof sketch (discrete):**
$$E[E(X \mid Y)] = \sum_j E(X \mid Y = y_j) P(Y = y_j) = \sum_j \sum_i x_i p_{ij} = \sum_i x_i p_{i\cdot} = E[X]. \quad \square$$

**Theorem 31 — Iterated Variance (Law of Total Variance, Lecture):**

$$\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}(E[X \mid Y]).$$

**Proof:** Let $m(Y) = E[X|Y]$. Then:
$$\text{Var}(X) = E[X^2] - (E[X])^2.$$
$$E[\text{Var}(X|Y)] = E[E[X^2|Y] - m(Y)^2] = E[X^2] - E[m(Y)^2].$$
$$\text{Var}(m(Y)) = E[m(Y)^2] - (E[m(Y)])^2 = E[m(Y)^2] - (E[X])^2.$$
Summing: $E[\text{Var}(X|Y)] + \text{Var}(m(Y)) = E[X^2] - (E[X])^2 = \text{Var}(X)$.

**Theorem 32 — Substitution Theorem (Lecture):** For any measurable $g$:

$$E[g(X, Y) \mid Y = y] = E[g(X, y) \mid Y = y].$$

### Mixture of Distributions

**Lecture (Example 60):** If $Y$ takes values $y_1, \ldots, y_n$ with $P(Y = y_i) = p_i$, and $X \mid Y = y_i$ has density $\varphi_i$, then the marginal density of $X$ is the **mixture**:

$$f_X(x) = \sum_{i=1}^n p_i \varphi_i(x).$$

### Examples

**Example (Lecture, Ex. 57):** $X_1, X_2$ = outcomes of two die rolls, $Z = |X_1 - X_2|$. Find distribution of $Z \mid X_1 = 5$.

**Example (Lecture, Ex. 58):** Joint density $f(x,y) = cxy^2$ on $0 \leq x \leq 1, 0 \leq y \leq 1, x+y \geq 1$.

Conditional: $g_{12}(x \mid y) = \frac{cxy^2}{f_Y(y)}$.

**Example (Lecture, Ex. 59 — Binomial Thinning):** $Y \sim \text{Poi}(\lambda)$ eggs; each hatches independently with probability $p$. Then $X \mid Y = n \sim \text{Bin}(n, p)$. 

By iterated expectation: $E[X \mid Y] = Yp$, so $E[X] = E[Yp] = \lambda p$. And $X \sim \text{Poi}(\lambda p)$.

### Interpretation

The conditional distribution captures how information about one variable updates the distribution of another — a fundamental operation in both probability (Bayesian updating) and statistics (regression). The law of total expectation says the marginal expectation can always be computed by first conditioning and then averaging. The law of total variance decomposes variability into "within-group" and "between-group" components, fundamental to ANOVA and hierarchical models.
