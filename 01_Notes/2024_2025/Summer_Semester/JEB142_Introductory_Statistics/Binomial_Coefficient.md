---
course: JEB142
topic: Binomial Coefficient
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_6_Counting.pdf
tags: [JEB142, statistics, combinatorics, binomial-coefficient, Newton-binomial, Pascal-triangle]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_6_Counting.pdf]]
Related: [[Counting_Techniques]], [[Probability_Definitions]]

# Binomial Coefficient

## Definition

The **binomial coefficient** $\binom{n}{k}$ (read "$n$ choose $k$") counts the number of $k$-element subsets of an $n$-element set:

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}, \quad n,k \in \mathbb{N} \cup \{0\},\; k \leq n$$

Convention: $\binom{n}{k} = 0$ for $k > n$ or $k < 0$.

## Properties (Theorem 9)

For $n, k \in \mathbb{N} \cup \{0\}$ with $k \leq n$:

### a) Boundary values
$$\binom{n}{n} = \binom{n}{0} = 1$$

### b) Symmetry
$$\binom{n}{k} = \binom{n}{n-k}$$

*Interpretation:* Choosing $k$ items to include is equivalent to choosing $n-k$ items to exclude.

### c) Pascal's Recurrence
$$\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$$

*Derivation:* Condition on whether element $n+1$ is in the chosen subset. If not, choose $k$ from $n$: $\binom{n}{k}$ ways. If yes, choose $k-1$ from $n$: $\binom{n}{k-1}$ ways.

This recurrence generates **Pascal's triangle**.

### d) Newton's Binomial Formula
For any $n > 0$ and real $x, y$:

$$\boxed{(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}}$$

*Example:* $(x+y)^2 = \binom{2}{0}y^2 + \binom{2}{1}xy + \binom{2}{2}x^2 = y^2 + 2xy + x^2$.

### e) Sum of all binomial coefficients
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$

*Proof:* Set $x = y = 1$ in Newton's binomial formula. *Interpretation:* A set of $n$ elements has $2^n$ subsets in total.

### f) Alternating sum
$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0 \quad (n \geq 1)$$

*Proof:* Set $x = 1, y = -1$ in Newton's formula.

### g) Vandermonde's Identity
$$\sum_{j=0}^{k} \binom{n}{j}\binom{n}{k-j} = \binom{2n}{k}$$

*Interpretation:* Choosing $k$ items from two disjoint groups of $n$ items each.

## Applications in Probability

The binomial coefficient appears whenever we count subsets in the classical probability model (see [[Counting_Techniques]]). It is also the key ingredient in the **binomial probability distribution** studied in JEB105:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
which gives the probability of exactly $k$ successes in $n$ independent Bernoulli trials with success probability $p$.
