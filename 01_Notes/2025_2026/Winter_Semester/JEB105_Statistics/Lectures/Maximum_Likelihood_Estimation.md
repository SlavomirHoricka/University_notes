---
course: JEB105
topic: "Maximum Likelihood Estimation"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, MLE, maximum-likelihood, likelihood-function, estimation]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Point_Estimation]], [[Fisher_Information]], [[Rao_Cramer_Lower_Bound]], [[Method_of_Moments]], [[Confidence_Intervals]], [[Generalized_Likelihood_Ratio_Test]]

---

## Maximum Likelihood Estimation

### The Likelihood Function

Given observations $x_1, \ldots, x_n$ from a random sample with density/pmf $f(x, \theta)$, the **likelihood function** of the sample is:

$$L(\theta; x) = \prod_{i=1}^n f(x_i, \theta).$$

$L(\theta; x)$ is interpreted as the probability of observing the particular sample $(x_1, \ldots, x_n)$ as a function of the parameter $\theta$ — with the sample fixed and $\theta$ varying.

The **log-likelihood** is:

$$\ell(\theta; x) = \log L(\theta; x) = \sum_{i=1}^n \log f(x_i, \theta).$$

Maximising $\ell$ instead of $L$ is equivalent (since $\log$ is monotone) and is computationally simpler.

### The MLE

**Definition 45 (Lecture):** Given the sample $x = (x_1, \ldots, x_n)$, the value $\hat{\theta}(x)$ maximising $L(\theta; x)$ over $\theta \in \Theta$ is called the **maximum likelihood estimate (MLE)** of $\theta$.

The corresponding random variable $\hat{\theta}(X_1, \ldots, X_n)$ is the MLE **estimator**.

In regular cases, the MLE satisfies the first-order conditions (**score equations**):

$$\frac{\partial}{\partial \theta} \ell(\theta; x) = \sum_{i=1}^n \frac{\partial}{\partial\theta} \log f(x_i, \theta) = 0.$$

### Examples

**Example 88:** Five Bernoulli trials with 3 successes and 2 failures.

$$L(\theta; x) = \theta^3(1-\theta)^2, \quad \ell = 3\log\theta + 2\log(1-\theta).$$

Score equation: $\frac{3}{\theta} - \frac{2}{1-\theta} = 0 \implies \hat{\theta}_{\text{MLE}} = \frac{3}{5}.$

**Example 89:** Two observations $x_1 = 3$, $x_2 = -2$ from $N(0, \theta^2)$.

$$\ell(\theta; x) = -\log 2\pi - 2\log\theta - \frac{13}{2\theta^2}.$$

Score equation: $-\frac{2}{\theta} + \frac{13}{\theta^3} = 0 \implies \hat{\theta}^2_{\text{MLE}} = \frac{13}{2}.$

### Properties of the MLE

**1. Invariance principle:** If $\hat{\theta}$ is the MLE of $\theta$, then for any function $h(\cdot)$, the estimator $h(\hat{\theta})$ is the MLE of $h(\theta)$.

*Example:* If $\hat{\theta}$ is the MLE of the variance $\sigma^2$, then $\sqrt{\hat{\theta}}$ is the MLE of $\sigma$.

**2. Likelihood principle:** Consider two data sets from the same population. If the ratio of their likelihoods $L_1(\theta, x)/L_2(\theta, y)$ does not depend on $\theta$, then both data sets contain the same information about $\theta$ and should yield the same estimate.

**3. Asymptotic properties:** Under regularity conditions, as $n \to \infty$:
- $\hat{\theta}_{\text{MLE}} \xrightarrow{P} \theta$ (consistency).
- $\sqrt{n}(\hat{\theta}_{\text{MLE}} - \theta) \xrightarrow{d} N(0, 1/I(\theta))$.
- The MLE is **asymptotically efficient** — it asymptotically attains the [[Rao_Cramer_Lower_Bound]].

### Asymptotic Confidence Interval

From the asymptotic normality of the MLE (Theorem 60, Lecture):

$$\hat{\theta}_n \pm \frac{z_{\alpha/2}}{\sqrt{n I(\hat{\theta}_n)}}$$

is an approximate $(1-\alpha)$-confidence interval for $\theta$ (see [[Confidence_Intervals]]).

### Interpretation

The MLE chooses the parameter value that makes the observed data most probable. It is the most widely used estimation method in statistics because:
- It is automatic: the same procedure applies regardless of the model.
- Under regularity conditions, it is asymptotically optimal (efficient).
- The invariance property allows estimation of any function of the parameter.

The MLE is foundational for the [[Generalized_Likelihood_Ratio_Test]] and the construction of asymptotic confidence intervals.
