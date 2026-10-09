---
course: JEB142
topic: Conditional Probability and Chain Rule
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_7_Conditional_Probability.pdf
tags: [JEB142, statistics, probability, conditional-probability, chain-rule]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_7_Conditional_Probability.pdf]]
Related: [[Kolmogorov_Axioms]], [[Total_Probability_and_Bayes_Theorem]], [[Independence_of_Events]], [[Sample_Space_and_Events]]

# Conditional Probability

## Motivation

Additional information about an experiment — knowing that some event $B$ has already occurred — changes our uncertainty about other events. Conditional probability formalises this **updating of beliefs given evidence**.

*Example:* You roll a die and are told the result is even. The probability of 6 is now $1/3$, not $1/6$.

## Definition

**Definition 20:** Let $A, B \in \mathcal{A}$ with $P(B) > 0$. The **conditional probability of $A$ given $B$** is:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Frequency Interpretation

$$P(A \mid B) = \lim_{n \to \infty} \frac{N(A \cap B)}{N(B)}$$

where $N(A \cap B)$ is the count of trials in which both $A$ and $B$ occur, and $N(B)$ counts trials where $B$ occurs. $P(A \mid B)$ approximates the relative frequency of $A$ among those trials where $B$ occurred.

### Geometric Interpretation

Conditioning on $B$ **restricts the sample space** to $B$; we then measure $A$'s portion within that restricted space.

## Multiplication Rule (Symmetric Form)

Rearranging the definition immediately gives:
$$P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$

## Chain Rule (Theorem 11)

For any events $A_1, A_2, \dots, A_n \in \mathcal{A}$ with $P(A_1 \cap \cdots \cap A_{n-1}) > 0$:

$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1) \cdot P(A_2 \mid A_1) \cdot P(A_3 \mid A_1 A_2) \cdots P(A_n \mid A_1 \cdots A_{n-1})$$

### Derivation
Apply the multiplication rule recursively:
$$P(A_1 A_2) = P(A_1)P(A_2|A_1)$$
$$P(A_1 A_2 A_3) = P(A_1 A_2) P(A_3 | A_1 A_2) = P(A_1)P(A_2|A_1)P(A_3|A_1 A_2)$$

Continuing inductively gives the general formula.

### Example (Fruit basket)
25 fruits, 20 apples. Probability three consecutively drawn fruits are all apples (without replacement):
$$P = \frac{20}{25} \cdot \frac{19}{24} \cdot \frac{18}{23} = \frac{20 \times 19 \times 18}{25 \times 24 \times 23} = \frac{6840}{13800} \approx 0.496$$

## Conditional Probability as a Probability

**Theorem 10:** If $P(B) > 0$, then $P(\cdot \mid B)$ as a function on $\mathcal{A}$ satisfies all three Kolmogorov axioms (see [[Kolmogorov_Axioms]]). That is, conditional probability is itself a valid probability measure on the **conditional sample space** $B$.

### Consequences

- $P(A^c \mid B) = 1 - P(A \mid B)$
- $P(A \mid B) + P(A^c \mid B) = 1$ — probabilities within the conditional space still sum to 1.
- All derived results (inclusion-exclusion, continuity) hold for $P(\cdot \mid B)$.

## Key Properties and Common Pitfalls

- $P(A \mid B) \neq P(B \mid A)$ in general — confusing these is the **inverse fallacy** (see Example 34, medical testing).
- $P(A \mid B)$ can be larger or smaller than $P(A)$ — conditioning may increase or decrease the probability of $A$.
- $P(A \mid B) + P(A^c \mid B) = 1$ always (they are complementary given $B$).
- $P(A \mid B) + P(A \mid B^c) \neq 1$ in general.
