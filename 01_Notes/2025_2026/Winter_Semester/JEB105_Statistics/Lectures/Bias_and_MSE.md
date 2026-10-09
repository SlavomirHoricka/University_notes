---
course: JEB105
topic: "Bias, Consistency, and Mean Squared Error"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, bias, MSE, consistency, unbiasedness, estimation]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Point_Estimation]], [[Convergence_of_Random_Variables]], [[Fisher_Information]], [[Rao_Cramer_Lower_Bound]], [[Sample_Mean_and_Sample_Variance]]

---

## Bias, Consistency, and Mean Squared Error

### Consistency

**Definition 40 (Lecture):** Let $T_n = T_n(X_1, \ldots, X_n)$ be an estimator. Then $T_n$ is called:
- **Weakly consistent** if $T_n \xrightarrow{P} \theta$.
- **Strongly consistent** if $T_n \xrightarrow{a.s.} \theta$.

Consistency means: "Increasing the sample size improves accuracy of the estimator, bringing it closer to the true value of the parameter."

### Unbiasedness

**Definition 41 (Lecture):** Let $T_n = T_n(X_1, \ldots, X_n)$. Then $T_n$ is called:
- **Unbiased** if $E_\theta(T_n) = \theta$ for every $n$.
- **Biased** if $E_\theta(T_n) \neq \theta$; the difference $B_\theta(T_n) = E_\theta(T_n) - \theta$ is called the **bias**.
- **Asymptotically unbiased** if $\lim_{n\to\infty} E_\theta(T_n) = \theta$.

Unbiasedness means: "If we repeat the sampling, the estimate will, on average, equal the true value of the parameter."

### Mean Squared Error

**Definition 42 (Lecture):**

$$\text{MSE}_\theta(T) = E_\theta[(T(X_1,\ldots,X_n) - \theta)^2].$$

**Theorem 57 (Lecture):** For any estimator $T$:

$$\text{MSE}_\theta(T) = \text{Var}_\theta(T) + [B_\theta(T)]^2.$$

**Derivation:**
$$E[(T-\theta)^2] = E[(T - E[T] + E[T] - \theta)^2] = E[(T-E[T])^2] + (E[T]-\theta)^2 = \text{Var}(T) + B^2(T),$$
using that the cross-term $2E[(T-E[T])](E[T]-\theta) = 0$.

### Example: Estimators of $\theta$ in $U[0,\theta]$

For $X_1,\ldots,X_n \overset{\text{i.i.d.}}{\sim} U[0,\theta]$ (Example 82):

| Estimator | $E[T]$ | $\text{Var}(T)$ | $\text{MSE}_\theta(T)$ |
|---|---|---|---|
| $T_1 = X_{n:n}$ | $\frac{n}{n+1}\theta$ | $\frac{n\theta^2}{(n+1)^2(n+2)}$ | $\frac{2\theta^2}{(n+1)(n+2)}$ |
| $T_2 = \frac{n+1}{n}X_{n:n}$ | $\theta$ | $\frac{\theta^2}{n(n+2)}$ | $\frac{\theta^2}{n(n+2)}$ |
| $T_3 = (n+1)X_{1:n}$ | $\theta$ | $\frac{n\theta^2}{n+2}$ | $\frac{n\theta^2}{n+2}$ |
| $T_4 = 2\bar{X}$ | $\theta$ | $\frac{\theta^2}{3n}$ | $\frac{\theta^2}{3n}$ |

$T_2$ and $T_4$ are unbiased. $T_1$ is biased but consistent (bias $\to 0$). $T_3$ is unbiased but **not consistent** (variance does not vanish).

### Test of Consistency (using Chebyshev)

1. Determine whether $T_n$ is unbiased.
2. Compute $\text{Var}(T_n)$ and bias $B(T_n)$.
3. Check:
   - An **unbiased** estimator is consistent if $\text{Var}(T_n) \to 0$.
   - A **biased** estimator is consistent if both $\text{Var}(T_n) \to 0$ and $B(T_n) \to 0$.

**Example 83:** The sample mean $\bar{X}$ is a consistent estimator of $\mu$: $\text{Var}(\bar{X}) = \sigma^2/n \to 0$.

### Bias-Variance Trade-off

MSE = Variance + Bias$^2$ reveals a fundamental trade-off:
- An unbiased estimator has $\text{MSE} = \text{Var}$, but may have high variance.
- A biased estimator can have lower MSE if the reduction in variance outweighs the squared bias.

This trade-off is central in modern statistics (ridge regression, shrinkage estimators) and machine learning (regularisation).

### Additional Desirable Properties

Beyond unbiasedness and consistency, we may require:
- **Minimum variance** among unbiased estimators (see [[Rao_Cramer_Lower_Bound]]).
- **Efficiency** (see [[Fisher_Information]]).
- **Linearity** (e.g., BLUE in the Gauss-Markov theorem).
