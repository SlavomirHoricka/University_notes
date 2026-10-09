---
course: JEB142
topic: Independence of Events
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_7_Conditional_Probability.pdf
tags: [JEB142, statistics, probability, independence, mutual-independence, pairwise-independence]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_7_Conditional_Probability.pdf]]
Related: [[Conditional_Probability]], [[Total_Probability_and_Bayes_Theorem]], [[Kolmogorov_Axioms]]

# Independence of Events

## Pairwise Independence (Two Events)

**Definition 22:** Two events $A, B \in \mathcal{A}$ with $P(A) > 0$ and $P(B) > 0$ are **independent** if:
$$P(A \mid B) = P(A) \quad \Longleftrightarrow \quad P(B \mid A) = P(B)$$

### Equivalent Characterisation

Because $P(A \mid B) = P(A \cap B)/P(B)$, the condition simplifies to:

$$\boxed{P(A \cap B) = P(A)\,P(B)}$$

This form is preferred because it:
1. Does not require $P(A) > 0$ or $P(B) > 0$ (it extends independence to zero-probability events).
2. Is symmetric in $A$ and $B$ by inspection.

### Interpretation

Independence means knowledge that $B$ occurred conveys **no information** about the probability of $A$, and vice versa. The unconditional and conditional probabilities coincide.

### Dependence

If $P(A \cap B) \neq P(A)P(B)$, events $A$ and $B$ are **dependent**.

### Preserved Independence (Theorem 14)

If $A$ and $B$ are independent, then so are all pairs: $(A, B^c)$, $(A^c, B)$, $(A^c, B^c)$.

*Proof sketch:* $P(A \cap B^c) = P(A) - P(A \cap B) = P(A) - P(A)P(B) = P(A)(1-P(B)) = P(A)P(B^c)$. $\square$

## Mutual Independence (Multiple Events)

**Definition 23:** Events $A_1, A_2, \dots, A_n$ are **(mutually) independent** if for **every** subset of indices $i_1 < i_2 < \cdots < i_k$ with $1 \leq k \leq n$:

$$P(A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_k}) = P(A_{i_1})\,P(A_{i_2})\cdots P(A_{i_k})$$

This must hold for **all** $2^n - n - 1$ subsets of size $\geq 2$.

An infinite sequence $A_1, A_2, \dots$ is independent if $A_1, \dots, A_n$ are independent for **every** $n \in \mathbb{N}$.

## Pairwise vs. Mutual Independence

**Pairwise independence does NOT imply mutual independence.** The additional conditions involving triples, quadruples, etc., can fail even when all pairs are independent.

**Example 35 (Lecture):** $S = \{s_1, s_2, s_3, s_4\}$ with $P(s_i) = 1/4$. Set $A = \{s_1, s_2\}$, $B = \{s_1, s_3\}$, $C = \{s_1, s_4\}$.
- $P(A) = P(B) = P(C) = 1/2$
- $P(AB) = P(AC) = P(BC) = 1/4 = P(A)P(B)$ — **pairwise independent**
- $P(ABC) = P(\{s_1\}) = 1/4 \neq 1/8 = P(A)P(B)P(C)$ — **not mutually independent**

**Example 36 (Lecture):** $S = \{s_1,\dots,s_5\}$ with $P(s_1)=P(s_2)=P(s_3) = 8/27$, $P(s_4) = 1/27$, $P(s_5)=2/27$.

This example demonstrates that even more complex configurations can be pairwise but not mutually independent.

## Theorem 15: Independence of Complements

If $A_1, \dots, A_n$ are independent, then for any $0 < m \leq n$, replacing any subset of the $A_i$'s with their complements preserves independence:
$$A_1^c, \dots, A_m^c, A_{m+1}, \dots, A_n \text{ are independent.}$$

## Independence vs. Disjointness

These are often confused but are **opposite** notions for events with positive probability:

| Property | Condition | Implication |
|----------|-----------|-------------|
| **Disjoint** ($A \cap B = \emptyset$) | Cannot both occur | $P(A \cap B) = 0$ |
| **Independent** | One's occurrence doesn't affect the other's probability | $P(A \cap B) = P(A)P(B)$ |

If $P(A) > 0$ and $P(B) > 0$:
- Disjoint $\Rightarrow$ dependent (knowing $B$ occurred makes $A$ impossible, so $P(A \mid B) = 0 < P(A)$).
- Independent $\Rightarrow$ not disjoint (since $P(A \cap B) = P(A)P(B) > 0$).

*Control session statement (iii): "If $A$ and $B$ are independent, then they must be disjoint" — **False**.*

## Application

Independence is a foundational assumption in many statistical models:
- IID (independent and identically distributed) samples underlie virtually all classical statistical inference.
- The product rule for independent events makes probability calculations tractable.
- Violations of independence (e.g., clustered sampling, time-series autocorrelation) require specialised methods covered in JEB105 and [[JEB109_Econometrics_I_main]].
