---
course: JEB142
topic: Sample Space and Events
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_4_Sample_Space.pdf
tags: [JEB142, statistics, probability, sample-space, events, experiment]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_4_Sample_Space.pdf]]
Related: [[Set_Operations_on_Events]], [[Sigma_Algebra]], [[Kolmogorov_Axioms]], [[Probability_Definitions]]

# Sample Space and Events

## Experiments

**Definition 1 (Experiment):** An experiment is any process, possibly under partial control, that we may observe and for which the final state of affairs cannot be specified in advance, but for which a set containing all potential final states of affairs can be identified.

The goal of formalising experiments is to assign a **quantitative measure of uncertainty** — probability — to their possible outcomes.

*Examples:* tossing a coin, rolling a die, recording whether a patient recovers, measuring daily stock returns.

## Outcomes and the Sample Space

**Definition 2 (Outcome):** An outcome is a final result, observation, or measurement occurring from an experiment.

Outcomes must:
- **exclude each other** (mutually exclusive — only one outcome can occur per trial), and
- **exhaust all logical possibilities** (collectively exhaustive — one outcome must occur).

**Definition 3 (Sample Space):** The sample space, denoted $S$, is the set of **all** outcomes of an experiment. The elements of $S$ are called **elementary outcomes** or **sample points**.

### Classification of Sample Spaces

| Type | Description | Example |
|------|-------------|---------|
| **Finite (discrete)** | $S$ has finitely many elements | $S = \{1,2,3,4,5,6\}$ for a single die |
| **Countably infinite (discrete)** | $S$ is infinite but enumerable | $S = \{0,1,2,\dots\}$ for number of arrivals |
| **Uncountable (continuous)** | $S$ is a continuous set | $S = [0, \infty)$ for a lifetime |

**Note:** The same physical experiment can be described via different sample spaces depending on the information recorded. For example, tossing two dice: if we record the individual faces, $S = \{(i,j): i,j \in \{1,\dots,6\}\}$ has 36 elements; if we record only the sum, $S = \{2,3,\dots,12\}$ has 11 elements.

## Events

**Definition 4 (Event):** An event is a **subset** $A \subseteq S$ of the sample space. An **elementary event** is a singleton set $\{s\}$ for some $s \in S$.

We say the event $A$ **has occurred** if the observed outcome belongs to $A$.

*Example:* In two tosses of a die recording only the sum, the event "the sum equals 7" is $A = \{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}$ — a subset of the full sample space $\{(i,j)\}$.

## Basic Terminology for Events

**Definition 5:** For events $A, B, C \subset S$:

| Symbol | Name | Meaning |
|--------|------|---------|
| $A = \emptyset$ | **Null / impossible event** | $A$ can never occur |
| $A = S$ | **Sure event** | $A$ always occurs |
| $A \subset B$ | $A$ is a **subevent** of $B$ | If $A$ occurs then $B$ occurs |
| $B = A^c = S \setminus A$ | **Complement** of $A$ | $B$ occurs when $A$ does not |
| $C = A \cup B$ | **Union** | $C$ occurs when $A$ or $B$ (or both) occur |
| $C = A \cap B$ | **Intersection** | $C$ occurs when both $A$ and $B$ occur |
| $C = A \setminus B$ | **Difference** | $C$ occurs when $A$ occurs but $B$ does not |
| $A \cap B = \emptyset$ | **Disjoint / mutually exclusive** | $A$ and $B$ cannot both occur |

These operations are visualised using **Venn diagrams**, where $S$ is a rectangle and events are regions within it.

## Infinite Sequences of Events

For an infinite sequence $A_1, A_2, \dots$:

$$\bigcup_{i=1}^{\infty} A_i = A_1 \cup (A_2 \cup (\dots)) \quad \text{— "at least one } A_i \text{ occurs''}$$

$$\bigcap_{i=1}^{\infty} A_i = A_1 \cap (A_2 \cap (\dots)) \quad \text{— "all } A_i \text{ occur''}$$

**Definition 7 (limsup and liminf):**

$$\limsup_{n\to\infty} A_n = \bigcap_{k=1}^{\infty} \bigcup_{i=k}^{\infty} A_i \quad \text{— "infinitely many } A_i\text{'s occur''}$$

$$\liminf_{n\to\infty} A_n = \bigcup_{k=1}^{\infty} \bigcap_{i=k}^{\infty} A_i \quad \text{— "all except finitely many } A_i\text{'s occur''}$$

Always: $\limsup_{n\to\infty} A_n \supseteq \liminf_{n\to\infty} A_n$.

**Definition 8 (Limit of a sequence of events):** If $\limsup_{n\to\infty} A_n = \liminf_{n\to\infty} A_n$, the sequence converges and:
$$\lim_{n\to\infty} A_n = \limsup_{n\to\infty} A_n = \liminf_{n\to\infty} A_n.$$

**Theorem 1:** If $\{A_n\}$ is increasing ($A_1 \subset A_2 \subset \dots$) then $\lim_{n\to\infty} A_n = \bigcup_{n=1}^{\infty} A_n$. If decreasing ($A_1 \supset A_2 \supset \dots$) then $\lim_{n\to\infty} A_n = \bigcap_{n=1}^{\infty} A_n$.

These limit concepts are prerequisites for the continuity-of-probability result (see [[Kolmogorov_Axioms]]).
