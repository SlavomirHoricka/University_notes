---
course: JEB105
topic: "Random Sample and Statistics"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, random-sample, statistic, sampling-distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Random_Variable]], [[Expected_Value]], [[Variance]], [[Sample_Mean_and_Sample_Variance]], [[Central_Limit_Theorem]], [[Law_of_Large_Numbers]]

---

## Random Sample and Statistics

### Definition

A **random sample** of size $n$ from a distribution $F$ is a collection of $n$ independent, identically distributed (i.i.d.) random variables $X_1, X_2, \ldots, X_n$, each with CDF $F$ (or density/pmf $f$).

The key assumptions are:
1. **Independence:** The outcome of any $X_i$ does not influence any $X_j$ for $i \neq j$.
2. **Identical distribution:** Each $X_i$ has the same distribution, characterised by the same parameter(s) $\theta$.

### Statistic

**Definition:** A **statistic** is any measurable function $T = T(X_1, \ldots, X_n)$ of the sample. A statistic is itself a random variable.

Examples of statistics:
- Sample mean: $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$
- Sample variance: $S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$
- Sample minimum $X_{1:n}$, maximum $X_{n:n}$
- Any order statistic $X_{k:n}$

A statistic used to estimate an unknown parameter $\theta$ is called an **estimator** (see [[Point_Estimation]]).

### Sampling Distribution

The **sampling distribution** of a statistic $T$ is the probability distribution of $T$ viewed as a random variable. It describes how $T$ varies across all possible samples of size $n$ from the population.

Understanding the sampling distribution is essential for:
- Constructing [[Confidence_Intervals]]
- Performing [[Hypothesis_Testing_Framework]]
- Assessing the quality of estimators via [[Bias_and_MSE]]

### Why Simple Random Sampling?

The i.i.d. assumption provides mathematical tractability:
- Expectations and variances of statistics can be computed from the common marginal distribution.
- Laws of Large Numbers (see [[Law_of_Large_Numbers]]) guarantee convergence of sample averages.
- The [[Central_Limit_Theorem]] applies to standardised sums.

In practice, data are assumed to come from simple random sampling unless explicitly stated otherwise. This assumption underlies the entire framework of classical statistical inference.

### Interpretation

The distinction between the **population** and the **sample** is fundamental:
- The population is described by the unknown distribution $F_\theta$.
- The sample provides observed realisations $x_1, \ldots, x_n$ of the random variables $X_1, \ldots, X_n$.
- Statistics computed from the sample are used to make inference about $\theta$.

The randomness in a statistic $T(X_1, \ldots, X_n)$ comes entirely from the random draw of the sample — for a fixed realised sample $x_1, \ldots, x_n$, the value $T(x_1, \ldots, x_n)$ is a fixed number called an **estimate**.
