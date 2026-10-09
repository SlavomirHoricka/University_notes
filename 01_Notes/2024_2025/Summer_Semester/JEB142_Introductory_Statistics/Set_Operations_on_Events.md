---
course: JEB142
topic: Set Operations on Events
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_4_Sample_Space.pdf
tags: [JEB142, statistics, probability, set-operations, de-morgan, venn-diagram]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_4_Sample_Space.pdf]]
Related: [[Sample_Space_and_Events]], [[Sigma_Algebra]], [[Kolmogorov_Axioms]]

# Set Operations on Events

## Motivation

Events are subsets of the [[Sample_Space_and_Events|sample space]] $S$. The algebra of events borrows directly from set theory. Mastering these laws is essential for deriving probability formulas (inclusion-exclusion, total probability, Bayes).

## Laws of Operations (Definition 6)

For events $A, B, C \subseteq S$:

### a) Idempotence
$$A \cup A = A, \qquad A \cap A = A$$

### b) Double Complementation
$$(A^c)^c = A$$

### c) Absorption
$$A \cup B = B \iff A \cap B = A \iff A \subseteq B$$

### d) Commutativity
$$A \cup B = B \cup A, \qquad A \cap B = B \cap A$$

### e) Associativity
$$A \cup (B \cup C) = (A \cup B) \cup C$$
$$A \cap (B \cap C) = (A \cap B) \cap C$$

### f) Distributivity
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$

### g) De Morgan's Laws
$$(A_1 \cup \cdots \cup A_n)^c = A_1^c \cap \cdots \cap A_n^c$$
$$(A_1 \cap \cdots \cap A_n)^c = A_1^c \cup \cdots \cup A_n^c$$

De Morgan's laws extend to infinite collections:
$$\left(\bigcup_{i=1}^{\infty} A_i\right)^c = \bigcap_{i=1}^{\infty} A_i^c, \qquad \left(\bigcap_{i=1}^{\infty} A_i\right)^c = \bigcup_{i=1}^{\infty} A_i^c$$

## Venn Diagrams

Venn diagrams depict $S$ as a rectangle and events as regions within it. They provide **visual evidence** for set-algebraic identities and can guide — but not replace — formal proofs.

*Example:* $A \cap B$ is represented by the overlapping region of circles $A$ and $B$.

## Disjoint Partition

A collection $\{B_1, B_2, \dots\}$ of events is a **partition** of $S$ if:
1. $B_i \cap B_j = \emptyset$ for all $i \neq j$ (mutually exclusive), and
2. $\bigcup_i B_i = S$ (collectively exhaustive).

Partitions are central to the total probability formula (see [[Total_Probability_and_Bayes_Theorem]]).

## Decomposition into Disjoint Events

Any union of events can be rewritten as a union of **disjoint** events:
$$A_1 \cup A_2 \cup \cdots = A_1 \cup (A_1^c \cap A_2) \cup (A_1^c \cap A_2^c \cap A_3) \cup \cdots$$

Each term $B_i = A_1^c \cap \cdots \cap A_{i-1}^c \cap A_i$ is the event "$A_i$ is the first event in the sequence to occur". This decomposition is used in the proof of the inclusion-exclusion principle ([[Kolmogorov_Axioms#Inclusion-Exclusion Principle|Theorem 4]]).

## Practical Exercises

*Example 12 (from lecture):* For distinct events $A \neq B$:
1. If $A$ and $B^c$ are disjoint, then $A^c$ and $B$ are also disjoint? **False** in general.
2. If $A, B$ disjoint and $B, C$ disjoint, are $A, C$ disjoint? **False** — $A$ and $C$ can overlap.
3. $A \cup B^c = B^c \implies B \subseteq A^c$? **True** (by absorption law).
4. $A, B \subseteq C \implies C^c \subseteq A^c \cap B^c$? **True** (by De Morgan applied to $A \cup B \subseteq C$).
