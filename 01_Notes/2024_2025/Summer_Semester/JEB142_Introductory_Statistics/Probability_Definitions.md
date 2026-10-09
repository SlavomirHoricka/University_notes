---
course: JEB142
topic: Definitions of Probability
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_5_Probability.pdf
tags: [JEB142, statistics, probability, classical-probability, frequency-probability, subjective-probability, Kolmogorov]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_5_Probability.pdf]]
Related: [[Sample_Space_and_Events]], [[Kolmogorov_Axioms]], [[Sigma_Algebra]]

# Definitions of Probability

Probability evolved from an intuitive notion of chance to a rigorous mathematical structure. Three pre-axiomatic definitions existed historically; the modern approach supersedes them with Kolmogorov's axioms (see [[Kolmogorov_Axioms]]).

## 1. Classical (Logical) Definition

**Definition 12:** Let $S$ be the sample space for an experiment with a **finite** number $N(S)$ of **equally likely** outcomes. Let $A \subset S$ contain $N(A)$ elements. Then:

$$P(A) = \frac{N(A)}{N(S)}$$

### Strengths
- Simple and intuitive for games of chance (fair dice, fair coins, random draws from urns).
- Counting methods (permutations, combinations — see [[Counting_Techniques]]) are sufficient.

### Limitations
- **Sample space must be finite.**
- **All outcomes must be equally likely** — assumption fails for biased coins, loaded dice, or any real-world situation with heterogeneous probabilities.

## 2. Frequency (Empirical) Definition

**Definition 13:** Let $n$ be the number of times an experiment is repeated under **identical conditions**, and let $n(A)$ count how often event $A$ occurs. Then:

$$P(A) = \lim_{n \to \infty} \frac{n(A)}{n}$$

### Strengths
- Applies to infinite sample spaces.
- Outcomes need not be equally likely.
- Bridges probability and observed data.

### Limitations
- Some experiments **cannot be repeated** under identical conditions (one-off economic events, historical counterfactuals).
- The existence and uniqueness of the limit is not guaranteed by definition — it requires the **Law of Large Numbers** (proven formally in JEB105; the limit exists almost surely under independence and identical distribution).

## 3. Subjective Definition

**Definition 14:** $P(A)$ is a real number in $[0,1]$ chosen to express the **degree of personal belief** in the likelihood of $A$, with $P(A) = 1$ representing certainty.

### Strengths
- Applicable to unrepeatable events ("probability of recession next year") and to experiments with non-equally-likely outcomes.
- Foundation of Bayesian statistics.

### Limitations
- The assigned probability can **vary across individuals** with the same information.
- Requires consistency constraints (coherence axioms) to avoid arbitrage — a subjective agent who violates the Kolmogorov axioms can be "Dutch-booked" (made to accept a combination of bets that guarantees a loss).

## 4. Axiomatic (Kolmogorov) Definition

The axiomatic approach, introduced by Andrei Kolmogorov in 1933, unifies and supersedes the three definitions above. It defines probability abstractly as a **set function** satisfying three axioms, without requiring any physical interpretation. See [[Kolmogorov_Axioms]] for the full treatment.

## Comparison

| Property | Classical | Frequency | Subjective | Axiomatic |
|----------|-----------|-----------|------------|-----------|
| Finite $S$ required | Yes | No | No | No |
| Equal likelihood required | Yes | No | No | No |
| Repeatability required | No | Yes | No | No |
| Unique assignment | Yes | Yes (limit) | No | Conditional on axioms |
| Rigorous foundation | Partial | Partial | No | Yes |
