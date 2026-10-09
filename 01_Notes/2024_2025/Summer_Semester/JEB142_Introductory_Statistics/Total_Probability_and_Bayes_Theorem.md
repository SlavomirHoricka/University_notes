---
course: JEB142
topic: Total Probability Formula and Bayes' Theorem
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_7_Conditional_Probability.pdf
tags: [JEB142, statistics, probability, Bayes-theorem, total-probability, prior, posterior, partition]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_7_Conditional_Probability.pdf]]
Related: [[Conditional_Probability]], [[Independence_of_Events]], [[Kolmogorov_Axioms]], [[Set_Operations_on_Events]]

# Total Probability Formula and Bayes' Theorem

## Partition of the Sample Space

**Definition 21 (Partition):** A collection $\{B_n\}$ is a **partition** of $S$ if:
1. $P(\bigcup_n B_n) = 1$ (collectively exhaustive)
2. $B_n \cap B_m = \emptyset$ for $n \neq m$ (mutually exclusive)
3. $P(B_n) > 0$ for all $n$

Think of $\{B_n\}$ as **mutually exclusive, complete hypotheses** about the "state of the world". The $B_n$'s describe subpopulations; $P(B_n)$ are the **prior probabilities** of each state.

## Total Probability Formula (Theorem 12)

Let $\{B_n\}$ be a finite or countably infinite partition of $S$ with $P(B_n) > 0$ for all $n$. Then for any $A \in \mathcal{A}$:

$$\boxed{P(A) = \sum_n P(A \mid B_n) \cdot P(B_n)}$$

### Derivation
$$P(A) = P\!\left(A \cap \bigcup_n B_n\right) = P\!\left(\bigcup_n (A \cap B_n)\right) = \sum_n P(A \cap B_n) = \sum_n P(A \mid B_n)P(B_n)$$
The second equality uses that $A \cap B_n$ are disjoint (since $B_n$ are disjoint), and the third uses countable additivity.

### Interpretation
$P(A)$ is a **weighted average** of the conditional probabilities $P(A \mid B_n)$, weighted by the prior probabilities $P(B_n)$.

**Example:** Investment choice among 15 stocks, 10 bonds, 5 mutual funds, each equally likely ($P(B_1) = 15/30, P(B_2) = 10/30, P(B_3) = 5/30$). Given the instrument was not a bond, what is $P(\text{stock})$?

$$P(\text{stock} \mid \text{not bond}) = \frac{P(\text{stock} \cap \text{not bond})}{P(\text{not bond})} = \frac{15/30}{20/30} = \frac{15}{20} = 0.75$$

## Bayes' Theorem (Theorem 13)

Given a partition $\{B_n\}$ with $P(B_n) > 0$ for all $n$, for any $A \in \mathcal{A}$ with $P(A) > 0$:

$$\boxed{P(B_m \mid A) = \frac{P(A \mid B_m)\,P(B_m)}{\displaystyle\sum_n P(A \mid B_n)\,P(B_n)}}$$

### Derivation
Numerator: $P(A \mid B_m)P(B_m) = P(A \cap B_m)$ by the multiplication rule.
Denominator: $P(A)$ by the total probability formula.
$$P(B_m \mid A) = \frac{P(A \cap B_m)}{P(A)} = \frac{P(A \mid B_m)P(B_m)}{\sum_n P(A \mid B_n)P(B_n)}$$

### Interpretation
Bayes' theorem **inverts** conditional probability. Given that $A$ has occurred, it updates the prior probabilities $P(B_n)$ to **posterior probabilities** $P(B_n \mid A)$.

| Quantity | Name | Meaning |
|----------|------|---------|
| $P(B_m)$ | **Prior** | Probability of state $B_m$ before observing $A$ |
| $P(A \mid B_m)$ | **Likelihood** | Probability of evidence $A$ if state $B_m$ is true |
| $P(B_m \mid A)$ | **Posterior** | Updated probability of $B_m$ after observing $A$ |

### Canonical Example: Medical Diagnosis (Example 34)

- Disease prevalence: $P(D) = 0.01$, so $P(D^c) = 0.99$.
- Test sensitivity: $P(T^+ \mid D) = 0.98$.
- False positive rate: $P(T^+ \mid D^c) = 0.005$.

$P(D \mid T^+) = ?$

$$P(T^+) = 0.98 \times 0.01 + 0.005 \times 0.99 = 0.0098 + 0.00495 = 0.01475$$

$$P(D \mid T^+) = \frac{0.98 \times 0.01}{0.01475} \approx 0.664$$

Even with a 98% sensitive test, a positive result corresponds to only a ~66% posterior probability of disease when prevalence is low. This counterintuitive result demonstrates why base rates ($P(D)$) profoundly affect diagnostic accuracy.

## Bayesian Updating with Multiple Pieces of Evidence

**Theorem 16 (Bayes for updated evidence):** If after observing $A$ we additionally observe $A'$, then:

$$P(B_m \mid A A') = \frac{P(A' \mid A B_m)\,P(B_m \mid A)}{\sum_n P(A' \mid A B_n)\,P(B_n \mid A)}$$

The posterior from observing $A$ becomes the new prior for updating on $A'$. Bayesian updating is **sequential**: each new piece of evidence transforms the current posterior into a new prior.

## Conditional Independence (Definition 24)

Events $A$ and $A'$ are **conditionally independent given $B$** if:
$$P(A A' \mid B) = P(A \mid B)\,P(A' \mid B)$$

**Theorem 17:** When $A$ and $A'$ are conditionally independent given $\{B_n\}$, Bayes' formula simplifies to:
$$P(B_m \mid A A') = \frac{P(A \mid B_m)\,P(A' \mid B_m)\,P(B_m)}{\sum_n P(A \mid B_n)\,P(A' \mid B_n)\,P(B_n)}$$

This is the **naive Bayes** assumption — test results are independent given disease status — and greatly simplifies inference when multiple signals are available.
