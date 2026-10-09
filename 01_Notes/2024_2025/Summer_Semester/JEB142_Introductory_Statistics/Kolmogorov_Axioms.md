---
course: JEB142
topic: Kolmogorov Axioms and Probability Space
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_5_Probability.pdf
tags: [JEB142, statistics, probability, Kolmogorov, axioms, probability-space, inclusion-exclusion]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_5_Probability.pdf]]
Related: [[Probability_Definitions]], [[Sample_Space_and_Events]], [[Sigma_Algebra]], [[Conditional_Probability]]

# Kolmogorov Axioms and Probability Space

## Axiomatic Definition

**Definition 15 (Axiomatic / Kolmogorov definition):** Let $\mathcal{A}$ be a $\sigma$-algebra of subsets of $S$ (see [[Sigma_Algebra]]). A **probability** $P$ is a set function $P: \mathcal{A} \to \mathbb{R}$ satisfying:

a) **Nonnegativity:** For any event $A \in \mathcal{A}$:
$$P(A) \geq 0$$

b) **Norming (Unitarity):**
$$P(S) = 1$$

c) **Countable Additivity ($\sigma$-additivity):** For any sequence $A_1, A_2, \dots$ of **pairwise disjoint** events $A_n \in \mathcal{A}$:
$$P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n)$$

**Definition 16 (Probability Space):** The triple $(S, \mathcal{A}, P)$ is called a **probability space**.

## Consequences of the Axioms (Theorem 3)

The following properties are derived from the three axioms and the properties of $\sigma$-algebras:

a) $P(\emptyset) = 0$

b) $P(A_1 \cup \cdots \cup A_n) = \sum_{i=1}^n P(A_i)$ for **pairwise disjoint** events $A_i$.

c) $A \subseteq B \Rightarrow P(A) \leq P(B)$

d) $A \subseteq B \Rightarrow P(B \setminus A) = P(B) - P(A)$

e) $P\!\left(\bigcup_{n=1}^{\infty} A_n\right) \leq \sum_{n=1}^{\infty} P(A_n)$ (**subadditivity / Boole's inequality**)

f) $P(A^c) = 1 - P(A)$

**Warning:** $P(A) = 0 \not\Rightarrow A = \emptyset$. A continuous random variable assigns probability zero to every single point, yet those points are not impossible.

## Inclusion-Exclusion Principle (Theorem 4)

For any events $A_1, \dots, A_n \in \mathcal{A}$:

$$P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i) - \sum_{1 \le i < j \le n} P(A_i A_j) + \cdots + (-1)^{n-1} P(A_1 \cdots A_n)$$

For $n = 2$:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

For $n = 3$:
$$P(A \cup B \cup C) = P(A)+P(B)+P(C) - P(AB) - P(AC) - P(BC) + P(ABC)$$

This generalises to $n$ events with alternating signs.

## Continuity of Probability (Theorem 5)

If $A_1, A_2, A_3, \dots$ is a **monotone** sequence of events (either increasing $A_1 \subseteq A_2 \subseteq \dots$ or decreasing $A_1 \supseteq A_2 \supseteq \dots$), then:

$$\lim_{n \to \infty} P(A_n) = P\!\left(\lim_{n \to \infty} A_n\right)$$

This is the measure-theoretic statement that probability is a **continuous set function** — one can pass the limit inside $P$ for monotone sequences.

## Special Cases of Probability Spaces

### Discrete Probability
$S = \{s_1, s_2, \dots, s_n\}$ with $\mathcal{A} = \mathcal{P}(S)$ (all subsets). It suffices to specify $P(\{s_i\}) = p_i \geq 0$ with $\sum_{i=1}^n p_i = 1$. Then for any $A \in \mathcal{A}$:
$$P(A) = \sum_{i: s_i \in A} p_i$$
The classical definition is the special case $p_i = 1/n$ for all $i$.

### Geometric Probability
$S \subset \mathbb{R}^n$ from the Borel $\sigma$-algebra $\mathcal{B}(\mathbb{R}^n)$, with finite positive Lebesgue measure $\lambda(S) < \infty$. For $A \in \mathcal{B}(\mathbb{R}^n)$:
$$P(A) = \frac{\lambda(A)}{\lambda(S)} = \frac{|A|}{|S|}$$
where $\lambda$ is length/area/volume. Uniform probability is distributed proportionally to geometric size.

**Example (Bertrand Paradox):** Three different geometric parameterisations of "drawing a random chord" on a circle yield probabilities 1/3, 1/2, and 1/4 for the chord being longer than the side of the inscribed equilateral triangle. All three are consistent with the axioms; the paradox shows that "at random" is not well-defined without specifying the probability space.
