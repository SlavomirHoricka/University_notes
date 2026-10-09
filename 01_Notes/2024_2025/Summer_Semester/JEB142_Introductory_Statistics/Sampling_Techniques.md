---
course: JEB142
topic: Sampling Techniques
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_8_Sampling_Techniques.pdf
tags: [JEB142, statistics, sampling, simple-random-sample, stratified, cluster, systematic, convenience, sampling-error]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_8_Sampling_Techniques.pdf]]
Related: [[Data_Types_and_Variables]], [[Measures_of_Central_Tendency]], [[Measures_of_Dispersion]]

# Sampling Techniques

## Motivation and Basic Concepts

A **sample** is a subset of the **population** (sampled population). We collect data from the sample to make **inferences** about population parameters we cannot observe in full.

**Sampling error**: because the sample is only a fraction of the population, sample statistics (e.g., $\bar{x}$, $s$, $\hat{p}$) differ from the corresponding population parameters ($\mu$, $\sigma$, $p$). Sampling error is an **inherent**, unavoidable feature of statistical inference — not a computational mistake. Statistics quantifies and controls this error.

**Point estimates** are sample statistics used to estimate population parameters:

| Population Parameter | Symbol | Sample Estimator | Symbol |
|---------------------|--------|-----------------|--------|
| Mean annual salary | $\mu = \$51{,}800$ | Sample mean | $\bar{x} = \$51{,}814$ |
| Standard deviation | $\sigma = \$4{,}000$ | Sample SD | $s = \$3{,}348$ |
| Proportion trained | $p = 0.60$ | Sample proportion | $\hat{p} = 0.63$ |

**Sampling distribution of $\bar{x}$**: different random samples of the same size $n$ from the same population yield different values of $\bar{x}$. The distribution of these values across all possible samples is the **sampling distribution** — the foundation for interval estimation and hypothesis testing in JEB105.

## Finite vs. Infinite Populations

| Population | Frame | Sampling approach |
|------------|-------|-------------------|
| **Finite** | Complete list of all $N$ elements (frame) can be constructed | Label elements 1 to $N$, use random number table or RNG |
| **Infinite** | Frame cannot be constructed | Elements must be drawn from the same distribution and independently |

## Probability Sampling Techniques

All probability methods guarantee that every element has a **known, positive probability** of selection, enabling valid statistical inference and probability analysis.

### 1. Simple Random Sample (SRS)

A **simple random sample** of size $n$ from a population of size $N$ is selected such that **every possible sample of size $n$ has the same probability** of being chosen.

**Implementation for finite population:**
1. Number all $N$ elements.
2. Use a random number table (or PRNG): extract $d$-digit numbers where $d$ matches the number of digits in $N$; include if $\leq N$, discard otherwise; repeat until $n$ elements selected.
3. **Sampling without replacement** (standard SRS) vs. **sampling with replacement** (if a number is selected again, it re-enters the sample).

**Strengths:** Simple, unbiased, basis for theoretical guarantees.
**Weaknesses:** Requires a complete frame; can be inefficient (high variance) when the population is heterogeneous.

### 2. Stratified Random Sampling

1. Divide the population into **strata** (subgroups) based on a relevant characteristic (age, region, industry type).
2. Draw a **simple random sample from each stratum**.
3. Combine stratum-level estimates using a weighted average formula.

**When to use:** Works best when strata are internally **homogeneous** (low within-stratum variance) and differ from each other. This reduces sampling error compared to SRS with the same total $n$.

**Example:** Stratify a national health survey by age group (18–25, 26–40, 41–60, 60+), then draw SRS within each group.

### 3. Cluster Sampling

1. Divide the population into **clusters** (e.g., city blocks, schools, districts).
2. Draw a random sample **of clusters**.
3. Within selected clusters, either survey all elements or take a further SRS.

**When to use:** Works best when clusters are internally **heterogeneous** (each cluster is a microcosm of the whole population). Clusters themselves should be as alike as possible to each other to enable generalisation.

**Advantage:** Cost-effective — reduces travel and administrative burden.
**Disadvantage:** Typically larger standard errors than SRS or stratified sampling for the same $n$ (intra-cluster correlation inflates variance).

### 4. Systematic Sampling

1. Order the $N$ elements in the sampling frame.
2. Choose a random starting point $r \in \{1, \dots, k\}$ where $k = \lfloor N/n \rfloor$ (the **skip**).
3. Select elements $r,\; r+k,\; r+2k,\; \dots$

**Equal probability property:** every element has probability $n/N$ of selection.

**When to use:** Population is homogeneous and the sampling frame contains no hidden periodicity that could coincide with the skip $k$.

**Caveat:** If the list has a periodic pattern with period $k$ (e.g., a weekly pattern when every 7th item is sampled), systematic sampling can introduce severe bias.

## Non-Probability Sampling Techniques

In non-probability methods, not every population element has a known or positive chance of selection. These **cannot** support valid probability inference or generalisability claims.

### 5. Convenience Sampling

Elements are selected based on ease of access (volunteers, Facebook friends, wildlife captures near the researcher's base).

- **Advantage:** Fast and inexpensive.
- **Disadvantage:** Cannot establish representativeness; results may not generalise.

### 6. Snowball Sampling

An initial small group of respondents recruit further participants from their social networks, creating a "snowball" effect.

- **Typical application:** Hard-to-reach populations (e.g., substance users, undocumented workers).
- **Disadvantage:** Selection bias — respondents are not independent; the sample is clustered around existing networks.

## Comparison: Probability vs. Non-Probability

| Feature | Probability | Non-probability |
|---------|-------------|-----------------|
| Known selection probability | Yes | No |
| Representative? | Yes (by design) | Not guaranteed |
| Can compute sampling error | Yes | No |
| Can do statistical inference | Yes | Very limited |
| Cost | Higher | Lower |

## Connection to Statistical Inference

The **sampling distribution** of $\bar{x}$ (and other statistics) depends critically on how the sample was drawn. With SRS and large $n$, the **Central Limit Theorem** (JEB105) guarantees the sampling distribution of $\bar{x}$ is approximately normal:
$$\bar{x} \sim \mathcal{N}\!\left(\mu,\; \frac{\sigma^2}{n}\right)$$
This underpins confidence intervals and hypothesis tests. Non-probability samples do not satisfy the conditions for these results.
