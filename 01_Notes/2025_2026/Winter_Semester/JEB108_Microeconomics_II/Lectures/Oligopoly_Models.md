---
course: "JEB108"
topic: "Oligopoly Models"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/9_oligopoly-1.pdf"
tags: [JEB108, microeconomics, oligopoly, game-theory, cournot, bertrand, stackelberg]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/9_oligopoly-1.pdf]]
Related: [[Monopoly]], [[Industry_Equilibrium]], [[Price_Discrimination]], [[Firm_Supply_Curve]]

# Oligopoly Models

## Overview

**Oligopoly:** A market structure with a **small number of strategically interdependent firms** — firms make decisions knowing that rivals will respond. The central tool is **game theory**; each model differs in:
- What the strategic variable is (quantity or price)
- Whether firms move **simultaneously** or **sequentially**

All oligopoly models sit between pure monopoly ($n = 1$) and perfect competition ($n \to \infty$).

---

## I. Sequential Quantity Setting — Stackelberg Model

### Setup

Two firms: a **quantity leader** (Firm 1) and a **quantity follower** (Firm 2).

- Leader commits to quantity $y_1$ first (publicly observable).
- Follower observes $y_1$ and then chooses $y_2$.

Solved by **backward induction** (from the follower's problem backward to the leader's).

### Follower's Problem

Follower maximizes profit given $y_1$:

$$\max_{y_2} p(y_1 + y_2) y_2 - c_2(y_2)$$

**FOC:** $p(y_1 + y_2) + \frac{\partial p}{\partial y_2} y_2 = MC_2(y_2)$

This yields the **follower's reaction function** $y_2^*(y_1)$: optimal $y_2$ for each $y_1$.

### Leader's Problem

Leader anticipates the follower's response and maximizes:

$$\max_{y_1} p(y_1 + y_2^*(y_1)) y_1 - c_1(y_1)$$

### Linear Demand Solution

Assume: $p = a - b(y_1 + y_2)$, $MC_1 = MC_2 = c$.

**Follower's reaction curve:**

$$y_2^*(y_1) = \frac{a - by_1 - c}{2b} = \frac{a-c}{2b} - \frac{y_1}{2}$$

**Leader's optimum:** Substitute $y_2^*(y_1)$ into leader's profit and maximize:

$$y_1^* = \frac{a-c}{2b}$$

**Equilibrium outcomes:**

| Variable | Formula |
|---|---|
| Leader output | $y_1^* = \dfrac{a-c}{2b}$ |
| Follower output | $y_2^* = \dfrac{a-c}{4b}$ |
| Total output | $Y^* = \dfrac{3(a-c)}{4b}$ |
| Price | $p^* = \dfrac{a+3c}{4}$ |
| Leader profit | $\pi_1^* = \dfrac{(a-c)^2}{8b}$ |
| Follower profit | $\pi_2^* = \dfrac{(a-c)^2}{16b}$ |

**First-mover advantage:** $\pi_1^* > \pi_2^*$ — the leader earns strictly more profit than the follower.

### With $n$ Followers

Leader: $y_1^* = \dfrac{a-c}{2b}$ (independent of $n$).

Each follower: $y_i^* = \dfrac{a-c}{4nb}$ (decreasing in $n$).

As $n \to \infty$: $p^* \to c$ (perfect competition).

---

## II. Simultaneous Quantity Setting — Cournot Model

### Setup

$n$ firms choose quantities **simultaneously**, each forming beliefs about rivals' choices. **Cournot equilibrium:** each firm's quantity is a best response to the others' quantities, and beliefs are confirmed.

### Best Response Functions

Firm $i$ maximizes:

$$\max_{y_i} p\left(\sum_j y_j\right) y_i - c_i(y_i)$$

**FOC:** $p(Y) + \frac{\partial p}{\partial Y} y_i = MC_i(y_i)$, where $Y = \sum_j y_j$.

This yields **reaction function (best response)** $y_i^*(y_{-i})$, giving optimal $y_i$ for any choices of the other firms.

**Cournot equilibrium:** intersection of all firms' reaction functions.

### Two-Firm Linear Demand Solution

Reaction curves for $MC_1 = MC_2 = c$:

$$y_1^*(y_2) = \frac{a - by_2 - c}{2b}, \quad y_2^*(y_1) = \frac{a - by_1 - c}{2b}$$

**Symmetric equilibrium:** $y_1^* = y_2^* = y^{Cournot}$:

$$y^C = \frac{a-c}{3b}$$

**Cournot outcomes (2 firms):**

| Variable | Formula |
|---|---|
| Each firm's output | $\dfrac{a-c}{3b}$ |
| Total output | $\dfrac{2(a-c)}{3b}$ |
| Price | $\dfrac{a+2c}{3}$ |
| Each firm's profit | $\dfrac{(a-c)^2}{9b}$ |

### $n$-Firm Cournot

$$y_i^* = \frac{a-c}{(n+1)b}, \quad Y^* = \frac{n(a-c)}{(n+1)b}, \quad p^* = \frac{a+nc}{n+1}$$

$$\pi_i^* = \frac{(a-c)^2}{n(n+1)^2 b}, \quad \Pi^* = \frac{(a-c)^2}{(n+1)^2 b}$$

- $n = 1$: **monopoly**.
- $n \to \infty$: **perfect competition** ($p^* \to c$, $\Pi^* \to 0$).

---

## III. Simultaneous Price Setting — Bertrand Model

### Setup

$n$ firms choose **prices simultaneously** (quantity adjusts to meet demand at chosen prices). Assumes **homogeneous goods**.

### Bertrand Equilibrium (Homogeneous goods, constant MC)

**Undercutting logic:** If Firm 1 sets $p_1 > MC$, Firm 2 can set $p_2 \in (MC, p_1)$ and capture the entire market. Firm 1 retaliates. This continues until:

$$\boxed{p_1^* = p_2^* = MC}$$

**Bertrand Paradox:** Just **two firms** competing in prices produce the **competitive outcome** — zero profits, $p = MC$, despite having market power in quantity.

**Outcomes:**

| Variable | Formula |
|---|---|
| Prices | $p_1^* = p_2^* = c$ |
| Total output | $\dfrac{a-c}{b}$ |
| Total profit | $\Pi^* = 0$ |

### Bertrand with Heterogeneous MC

- Firm with lowest MC captures entire market.
- Price = second-lowest MC (competitive constraint).

### Bertrand with Increasing MC

- With symmetric increasing MC: equilibrium at $p = MC$ for both firms; output split equally.
- This gives the competitive outcome even with increasing costs.

---

## Comparison of Oligopoly Models

| Model | Variable | Timing | Output | Price | Profit |
|---|---|---|---|---|---|
| Monopoly | either | — | $(a-c)/2b$ | $(a+c)/2$ | $(a-c)^2/4b$ |
| Stackelberg | quantity | sequential | $3(a-c)/4b$ | $(a+3c)/4$ | L: $(a-c)^2/8b$; F: $(a-c)^2/16b$ |
| Cournot | quantity | simultaneous | $2(a-c)/3b$ | $(a+2c)/3$ | $(a-c)^2/9b$ each |
| Bertrand | price | simultaneous | $(a-c)/b$ | $c$ | $0$ |
| Perfect comp. | — | — | $(a-c)/b$ | $c$ | $0$ |

**Output ranking:** Monopoly < Stackelberg < Cournot < Bertrand = Perfect Competition.

**Price ranking:** Monopoly > Stackelberg > Cournot > Bertrand = Perfect Competition.

---

## Collusion and Cartel

**Cartel:** Firms collectively agree to restrict output and raise prices to the monopoly level. The cartel acts as a single monopolist, splitting profits among members.

**Problem:** Each firm has an incentive to **defect** (secretly over-produce) — this is the classic **Prisoner's Dilemma** of repeated interaction.

**Stability of collusion depends on:**
- Number of firms (harder with more firms)
- Observability of defection
- Discount factor (future vs. present profits)
- Frequency of interaction

**Antitrust:** Cartel agreements are illegal in most jurisdictions (EU Art. 101, US Sherman Act §1). Leniency programs (whistleblower incentives) destabilize cartels.
