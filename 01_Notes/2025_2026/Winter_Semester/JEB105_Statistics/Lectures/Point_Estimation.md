---
course: JEB105
topic: "Point Estimation"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, estimation, estimator, parameter, inference]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Random_Sample_and_Statistics]], [[Bias_and_MSE]], [[Fisher_Information]], [[Rao_Cramer_Lower_Bound]], [[Method_of_Moments]], [[Maximum_Likelihood_Estimation]], [[Least_Squares_Estimation]]

---

## Point Estimation

### The Statistical Inference Setup

Suppose we observe $X_1, \ldots, X_n$ drawn i.i.d. from a distribution $f(x, \theta)$ where $\theta \in \Theta$ is an unknown parameter. The parameter space $\Theta$ may be a subset of $\mathbb{R}$ (scalar case) or $\mathbb{R}^k$ (vector case).

**Estimation** is the process of extracting information about $\theta$ from the sample. In the language of decision theory, we are in one of the "worlds" $\theta_1, \theta_2, \ldots$ and we want to determine which one.

### Estimator vs. Estimate

**Definition 39 (Lecture):** A statistic $T = T(X_1, \ldots, X_n)$ is called an **estimator** of $\theta$ if it is used to approximate $\theta$.

- An **estimator** is a random variable (a function of the random sample).
- An **estimate** is the realised value $T(x_1, \ldots, x_n)$ for a particular observed sample — a fixed number.

There may be many possible estimators for the same parameter. For example, for $\theta$ in $X_i \sim U[0,\theta]$, all of the following are estimators:
- $T_1 = X_{n:n}$ (sample maximum)
- $T_2 = \frac{n+1}{n} X_{n:n}$
- $T_3 = (n+1) X_{1:n}$
- $T_4 = 2\bar{X}$

### Desired Properties

The quality of an estimator is assessed by several properties (see [[Bias_and_MSE]]):

1. **Unbiasedness:** $E_\theta[T_n] = \theta$ for every $n$.
2. **Consistency:** $T_n \xrightarrow{P} \theta$ as $n \to \infty$ (see [[Convergence_of_Random_Variables]]).
3. **Low variance / efficiency:** Among unbiased estimators, prefer the one with smallest variance. The [[Rao_Cramer_Lower_Bound]] provides the best achievable variance.
4. **Mean squared error:** $\text{MSE}_\theta(T) = \text{Var}_\theta(T) + [B_\theta(T)]^2$ balances bias and variance (see [[Bias_and_MSE]]).

### Construction Methods

Three main methods for constructing estimators (covered in Lecture 8):

| Method | Principle |
|---|---|
| [[Method_of_Moments]] | Equate sample moments to population moments |
| [[Maximum_Likelihood_Estimation]] | Maximise the likelihood $L(\theta; x)$ |
| [[Least_Squares_Estimation]] | Minimise sum of squared residuals $S(\theta)$ |

### Why $\bar{X}$ as an Estimator of the Mean?

Assuming $X_i$ i.i.d. with $E[X_i] = \theta$ and $\text{Var}(X_i) = \sigma^2 < \infty$:
- $\bar{X}$ is **unbiased**: $E[\bar{X}] = \theta$.
- $\bar{X}$ is **consistent**: $\bar{X} \xrightarrow{P} \theta$ by the [[Law_of_Large_Numbers]].
- $\bar{X}$ has $\text{MSE}_\theta(\bar{X}) = \sigma^2/n$, which is **parameter-free** — it does not depend on $\theta$.
- $\text{MSE}$ decreases at rate $1/n$.
- $\bar{X}$ is **linear** in the observations.

These properties make $\bar{X}$ the natural starting point, though it is not always optimal (e.g., for heavy-tailed distributions the sample median may outperform it).

### Interpretation

Point estimation reduces the infinite-dimensional uncertainty about $\theta$ to a single number. However, a point estimate alone conveys no information about its precision. This motivates [[Confidence_Intervals]] (interval estimation) and [[Hypothesis_Testing_Framework]] (testing specific values of $\theta$).
