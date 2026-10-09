---
course: JEB105
topic: "Rao-Cramér Lower Bound and Efficiency"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, Rao-Cramer, CRLB, efficiency, unbiased-estimator]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Fisher_Information]], [[Bias_and_MSE]], [[Point_Estimation]], [[Maximum_Likelihood_Estimation]]

---

## Rao-Cramér Lower Bound and Efficiency

### Theorem (Rao-Cramér / Cramér-Rao)

**Theorem 59 (Lecture):** Under regularity assumptions, for any unbiased estimator $T_n$ of a parametric function $m(\theta)$:

$$\text{Var}_\theta(T_n) \geq \frac{[m'(\theta)]^2}{n \cdot I(\theta)}.$$

For the special case $m(\theta) = \theta$ (i.e., $T_n$ estimates $\theta$ itself):

$$\text{Var}_\theta(T_n) \geq \frac{1}{n \cdot I(\theta)}.$$

This lower bound is called the **Cramér-Rao lower bound (CRLB)** or **Rao-Cramér lower bound**.

### Derivation Sketch

By the Cauchy-Schwarz inequality applied to $\text{Cov}(T_n, J(X_i, \theta))$:

$$[\text{Cov}(T_n, J)]^2 \leq \text{Var}(T_n) \cdot \text{Var}(J).$$

Under regularity and unbiasedness, differentiating $E_\theta[T_n] = \theta$ under the integral sign gives $\text{Cov}(T_n, J) = 1$. Combined with $\text{Var}(J) = I(\theta)$ (from [[Fisher_Information]]), this yields $\text{Var}(T_n) \geq 1/I(\theta)$ (for a single observation). For $n$ i.i.d. observations, $I_n(\theta) = nI(\theta)$, giving $\text{Var}(T_n) \geq 1/(nI(\theta))$.

### Efficiency

**Definition 44 (Lecture):** An unbiased estimator $T_n$ that satisfies the regularity assumption and attains the CRLB — i.e.,

$$\text{Var}_\theta(T_n) = \frac{1}{n I(\theta)}$$

— is called **efficient**.

The **efficiency** of an unbiased estimator $T_n$ is the ratio:

$$e(T_n) = \frac{1/(n I(\theta))}{\text{Var}_\theta(T_n)} \leq 1.$$

An efficient estimator has $e(T_n) = 1$.

### Relative Efficiency

If $\tilde{T}_n$ and $\hat{T}_m$ are two unbiased estimators of $\theta$, the **relative efficiency** of $\hat{T}_m$ with respect to $\tilde{T}_n$ is:

$$e(\hat{T}_m, \tilde{T}_n) = \frac{\text{Var}_\theta(\tilde{T}_n)}{\text{Var}_\theta(\hat{T}_m)}.$$

If $e > 1$, then $\hat{T}_m$ is more efficient (lower variance).

### Example: Normal Mean

For $X_i \overset{\text{i.i.d.}}{\sim} N(\theta, \sigma^2)$ (estimating $\theta = \mu$, $\sigma^2$ known):

$$I(\theta) = \frac{1}{\sigma^2}, \quad \text{CRLB} = \frac{\sigma^2}{n}.$$

The sample mean $\bar{X}_n$ achieves $\text{Var}(\bar{X}_n) = \sigma^2/n$, so $\bar{X}_n$ is **efficient**.

### Connection to MLEs

Under regularity conditions, the MLE $\hat{\theta}_{MLE}$ is asymptotically efficient: its variance approaches the CRLB as $n \to \infty$ (see [[Maximum_Likelihood_Estimation]]). For finite samples, however, the MLE need not be unbiased and may not exactly attain the CRLB.

### Interpretation

The CRLB establishes the fundamental precision limit for unbiased estimation: no unbiased estimator can have variance smaller than $1/(nI(\theta))$. The more information a single observation carries about $\theta$ (large $I(\theta)$), the tighter this bound. Efficiency measures how close a given estimator comes to this theoretical minimum.
