---
course: JEB105
topic: "Method of Moments Estimation"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, method-of-moments, MoM, estimation, moments]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Point_Estimation]], [[Maximum_Likelihood_Estimation]], [[Expected_Value]], [[Variance]], [[Law_of_Large_Numbers]], [[Exponential_Distribution]]

---

## Method of Moments Estimation

### Principle

The **method of moments (MoM)** estimates population parameters by equating **sample moments** to the corresponding theoretical **population moments** and solving for the unknown parameters.

For $k$ unknown parameters $\theta_1, \ldots, \theta_k$, set up $k$ equations:

$$\frac{1}{n}\sum_{i=1}^n X_i^j = E_\theta[X^j], \quad j = 1, \ldots, k.$$

Solve these equations simultaneously to obtain the MoM estimator $\hat{\theta}_{\text{MoM}}$.

### Procedure

1. Identify the $k$ unknown parameters.
2. Compute the first $k$ (or other convenient) population moments as functions of $\theta$.
3. Replace population moments by their sample counterparts.
4. Solve the resulting system of equations.

**Practical Rule:** Use moments of the lowest possible order to simplify computation.

### Example 86: Exponential Distribution

$X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} \text{Exp}(\theta)$ with $E[X_i] = 1/\theta$.

**First moment estimator:**
$$\bar{X} = \frac{1}{\theta} \implies T_1 = \frac{1}{\bar{X}}.$$

**Second moment estimator:** Since $E[X^2] = 2/\theta^2$:
$$\frac{1}{n}\sum X_i^2 = \frac{2}{\theta^2} \implies T_2 = \sqrt{\frac{2n}{\sum_{i=1}^n X_i^2}}.$$

Both $T_1$ and $T_2$ are valid MoM estimators of $\theta$. For a derived quantity such as $p = P(X \geq 3) = e^{-3\theta}$:
$$p_1 = \exp\!\left(-\frac{3}{\bar{X}}\right), \qquad p_2 = \exp\!\left(-3\sqrt{\frac{2n}{\sum X_i^2}}\right).$$

### Example 87: Normal Distribution ($\mu$ and $\sigma^2$ unknown)

With $\theta = (\mu, \sigma^2)^\top$:

Population moments:
$$E[X] = \mu, \qquad E[X^2] = \sigma^2 + \mu^2.$$

Sample moment equations:
$$\bar{X} = \hat{\mu}, \qquad \frac{1}{n}\sum X_i^2 = \hat{\sigma}^2 + \hat{\mu}^2.$$

Solving:
$$\hat{\mu} = \bar{X}, \qquad \hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})^2.$$

Note: the MoM variance estimator uses $n$ in the denominator (biased), while the sample variance $S^2$ uses $n-1$ (unbiased). See [[Sample_Mean_and_Sample_Variance]].

### Properties

**Consistency:** Under mild conditions, if $\theta$ is a continuous function of the moments (which is typical), MoM estimators are consistent: $\hat{\theta}_{\text{MoM}} \xrightarrow{P} \theta$ as $n \to \infty$. This follows from the [[Law_of_Large_Numbers]] applied to sample moments plus the continuous mapping theorem.

**Relation to MLE:** In many cases (e.g., normal, exponential), the MoM estimator coincides with the MLE. In other cases, MoM estimators can be less efficient than MLEs.

### Advantages and Disadvantages

| Advantages | Disadvantages |
|---|---|
| Quick and straightforward | Solutions may not be unique |
| Easily computed by hand | May be less efficient than MLE |
| Does not require full likelihood | Moment equations choice is arbitrary |

### Interpretation

MoM is an intuitively appealing method: the idea of "matching sample statistics to their population counterparts" is natural. For example, setting $\bar{X} = E[X]$ is simply applying the [[Law_of_Large_Numbers]] — for large $n$, the sample mean will be close to the population mean. MoM provides a first-pass estimator that is often consistent and sometimes optimal, with a simplicity that makes it useful for multi-parameter problems where the likelihood is complex.
