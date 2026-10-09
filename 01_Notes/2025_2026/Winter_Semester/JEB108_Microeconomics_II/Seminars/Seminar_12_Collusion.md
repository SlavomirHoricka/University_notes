---
course: "JEB108"
topic: "Seminar Applications — Advanced Oligopoly: Collusion and Bertrand"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_12_Solution-1.pdf"
tags: [JEB108, microeconomics, seminars, oligopoly, collusion, bertrand, cournot, stackelberg]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_12_Solution-1.pdf]]
Related: [[Oligopoly_Models]], [[Monopoly]], [[Industry_Equilibrium]]

# Seminar Applications — Advanced Oligopoly: Collusion (Seminar 12)

Exercises on the stability of collusion versus Stackelberg/Cournot outcomes, and cartel profit redistribution.

---

## Collusion vs. Stackelberg: Individual Rationality

**Setup:** Duopoly with $D(p) = 12 - p$, so inverse demand $p = 24 - 2Y$ (where $y_i$ are in half-units).

$TC_1 = 10y_1 + 2$, $TC_2 = \frac{y_2^2}{2} + 6y_2$

### Stackelberg Equilibrium

Follower 2 reaction: $\frac{\partial \pi_2}{\partial y_2} = 24 - 2y_1 - 4y_2 - 6 = 0 \Rightarrow R_2(y_1) = \frac{9 - y_1}{3}$

Leader 1 substitutes: $y_1^{SL} = 3$, $y_2^{SF} = 2$, $p = 14$

$$\Pi_1 = 14(3) - 10(3) - 2 = 42 - 30 - 2 = 10, \quad \Pi_2 = 14(2) - 2 - 12 = 12$$

### Collusion Offer (with monitoring costs)

Cartel maximizes joint profit. Optimal outputs shift to $y_1^k = 1.5$, $y_2^k = 2$.

Firm 1's collusion profit (net of monitoring cost $FC = 1$, no leader position cost $= -2$): $\Pi_1^k = 9.5$

Firm 2's collusion profit: $\Pi_2^k = 17$

**Individual rationality check for Firm 1:**
$$\Pi_1^{Stackelberg} = 10 > 9.5 = \Pi_1^k$$

**→ Firm 1 has no incentive to accept the collusion offer.** As the Stackelberg leader, it earns more under non-cooperation than under the proposed cartel arrangement.

**Key insight:** Collusion requires **individual rationality** — every participant must weakly prefer the cartel to their outside option. Here, the leader's first-mover advantage is so valuable that even a jointly profit-maximizing cartel cannot compensate it.

---

## Cournot vs. Collusion: When Cooperation Dominates

**Setup:** $D(p) = 140 - p$, $TC_1 = y_1^2 + 35y_1 + 58$, $TC_2 = 3.5y_2^2 + 60.5$

**Cournot equilibrium:**

$MC_1 = 2y_1 + 35$, $MC_2 = 7y_2$

Reaction functions: $MR_i = MC_i$

Firm 1: $140 - 2y_1 - y_2 = 2y_1 + 35 \Rightarrow y_1 = \frac{105 - y_2}{4}$

Firm 2: $140 - y_1 - 2y_2 = 7y_2 \Rightarrow y_2 = \frac{140 - y_1}{9}$

Solving: $y_1^C = 23$, $y_2^C = 13$, $p^C = 104$, $Y^C = 36$

$$\Pi_1^C \approx 1000, \quad \Pi_2^C \approx 700$$

**Cartel equilibrium:** Joint profit maximization yields $y_1^k \approx 21$, $y_2^k \approx 11$, $p^k \approx 108$

$$\Pi_1^k \approx 1034, \quad \Pi_2^k \approx 704$$

Both firms earn higher profit under collusion: $\Pi_i^k > \Pi_i^C$ for $i = 1, 2$.

**→ Both firms willing to cooperate.** Joint profit redistribution can further stabilize the arrangement.

**Consumer welfare:** Cournot ($p^C = 104 < p^k = 108$, $Y^C = 36 > Y^k \approx 21$) is better for consumers — lower price and greater quantity. Collusion is **Pareto inferior** from a social perspective.

---

## Conceptual Lessons

1. **The Prisoner's Dilemma of Oligopoly:** Even when collusion would be jointly profit-improving (as in the Cournot case above), each firm has an incentive to **secretly defect** by producing more than the cartel quota — capturing neighbors' customers while they restrict output.

2. **Cartel stability conditions:**
   - Low discount rate (firms value future profits highly)
   - Easy detection of defection
   - Low number of firms
   - Symmetric firms (harder to divide surplus otherwise)
   - Repeated interaction

3. **Antitrust implications:** Cartel agreements (price-fixing, market allocation) are illegal under EU Art. 101 and US Sherman Act §1. **Leniency programs** (reduced penalties for whistleblowers) are designed to destabilize cartels by making defection more attractive.
