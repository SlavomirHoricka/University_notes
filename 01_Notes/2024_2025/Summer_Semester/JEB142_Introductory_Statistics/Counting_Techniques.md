---
course: JEB142
topic: Counting Techniques
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_6_Counting.pdf
tags: [JEB142, statistics, counting, combinatorics, permutations, combinations, Cartesian-product]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_6_Counting.pdf]]
Related: [[Probability_Definitions]], [[Binomial_Coefficient]], [[Sample_Space_and_Events]]

# Counting Techniques

## Motivation

In the **classical definition of probability** $P(A) = N(A)/N(S)$, computing probabilities reduces to counting the elements of $A$ and $S$. Combinatorics provides systematic techniques for this counting when simple enumeration is infeasible.

The four fundamental sampling paradigms distinguish whether objects are selected **with or without replacement** and whether the **order** of selection matters.

## a) Sampling with Replacement, Ordered — Cartesian Product

**Definition 17 (Cartesian Product):** For sets $A$ and $B$, the Cartesian product $A \times B$ is the set of all ordered pairs $(a,b)$ with $a \in A$, $b \in B$.

**Theorem 6 (Multiplication Rule):** If $A_1, \dots, A_n$ are finite sets with $|A_i| = k_i$, then:
$$|A_1 \times \cdots \times A_n| = \prod_{i=1}^n k_i$$

**Interpretation:** Counts ordered sequences of length $n$ where the $i$-th element is drawn from $A_i$ (with replacement implied by the Cartesian structure).

**Example 23:** Czech initials (first + last name) from a 42-letter alphabet: $42^2 = 1764$ possible two-letter initials.

**Birthday Problem (Example 25):** $r$ persons, each birthday equally likely among 365 days. The probability that no two share a birthday is:
$$p_r = \frac{365 \times 364 \times \cdots \times (365-r+1)}{365^r} = \frac{P_{365}^r}{365^r}$$
For $r = 23$ this already drops below $0.5$.

## b) Sampling without Replacement, Ordered — Permutations

**Definition 18 (Permutation):** An ordered sequence of $k$ elements selected without replacement from $n$ distinct elements ($n \geq k$) is called a **permutation of $k$ out of $n$**.

**Theorem 7:** The number of such permutations, denoted $P_n^k$, is:
$$P_n^k = n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!}$$

The special case $P_n^n = n!$ counts all orderings of $n$ distinct objects.

Convention: $0! = 1$.

**Example:** Number of ways to arrange the top-3 podium from 10 athletes: $P_{10}^3 = 10 \times 9 \times 8 = 720$.

## c) Sampling without Replacement, Unordered — Combinations

**Definition 19 (Combination):** A subset of size $k$ from a set of $n$ distinct elements, regardless of order, is a **combination of $k$ out of $n$**.

**Theorem 8:** The number of such combinations, denoted $C_n^k$ or $\binom{n}{k}$, is:
$$C_n^k = \binom{n}{k} = \frac{P_n^k}{k!} = \frac{n!}{k!\,(n-k)!}$$

$\binom{n}{k}$ is called the **binomial coefficient** (see [[Binomial_Coefficient]] for properties).

**Example 26:** 10 fish (3 yellow, 7 black), choose 3. Probability exactly 1 is yellow:
$$P = \frac{\binom{3}{1}\binom{7}{2}}{\binom{10}{3}} = \frac{3 \times 21}{120} = \frac{63}{120} = 0.525$$

## d) Sampling with Replacement, Unordered

Choose $k$ indistinguishable objects from $n$ types, with repetition allowed. This is equivalent to placing $k$ objects into $n$ boxes, or equivalently choosing $k$ positions from $n-1+k$ total (the "stars and bars" model):

$$\binom{n + k - 1}{k}$$

**Example 27:** A cake recipe calls for 5 pinches of spice from 9 different spices (repetition allowed, order irrelevant):
$$\binom{9+5-1}{5} = \binom{13}{5} = 1287 \text{ possible cakes}$$

## Summary Table

| Order | Replacement | Formula | Name |
|-------|-------------|---------|------|
| Yes | Yes | $k_1 \cdot k_2 \cdots k_n$ | Multiplication rule / Cartesian product |
| Yes | No | $P_n^k = \dfrac{n!}{(n-k)!}$ | Permutation |
| No | No | $C_n^k = \dbinom{n}{k} = \dfrac{n!}{k!(n-k)!}$ | Combination |
| No | Yes | $\dbinom{n+k-1}{k}$ | Multiset coefficient |
