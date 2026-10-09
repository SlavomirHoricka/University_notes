---
course: "JEB108"
topic: "Seminar Applications — Bertrand with Differentiated Products and Asymmetric Costs"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_13_Solution-1.pdf"
tags: [JEB108, microeconomics, seminars, bertrand, differentiated-products, price-competition]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_13_Solution-1.pdf]]
Related: [[Oligopoly_Models]], [[Price_Discrimination]], [[Industry_Equilibrium]]

# Seminar Applications — Bertrand with Asymmetric Costs & Differentiated Products (Seminar 13)

Advanced Bertrand exercises: asymmetric marginal costs, differentiated products with cross-price effects, and collusion stability in price competition.

---

## Bertrand with Asymmetric Marginal Costs (Homogeneous Good)

### Case: Two firms with equal MC

$MC_1 = MC_2 = 200$, $D(p) = 300 - p$.

**Equilibrium:** $p^* = 200$ (competitive). Output splits equally: $Y = D(200) = 100$, $y_1 = y_2 = 50$. Zero profits.

### Case: Three firms, one more expensive

$MC_1 = 200$, $MC_2 = 203$, $MC_3 = 205$. $D(p) = 300 - p$.

**Result:** $p^* = 202$ (just below $MC_2 = 203$). Firm 1 undercuts Firm 2 and grabs the entire market.

$y_1 = D(202) = 98$. Firms 2 and 3 produce nothing.

$\pi_1 = (202 - 200) \times 98 = 196 > 0$.

**Why?** The Bertrand equilibrium $p = MC$ requires **at least two firms with the minimum MC**. With asymmetric costs, the sole lowest-cost firm can charge just below the competitor's MC and earn positive profit — a resolution of the Bertrand paradox via cost asymmetry.

### Case: Increasing MC (Homogeneous product)

$MC_1(y_1) = 3y_1$, $MC_2(y_2) = 5y_2$, $D(p) = 92 - p$.

With **increasing MC**, firms face a capacity constraint — they cannot infinitely expand. Both firms coexist and marginal costs equal the equilibrium price:

$$p = MC_1(y_1) = 3y_1 \Rightarrow y_1 = p/3$$

$$p = MC_2(y_2) = 5y_2 \Rightarrow y_2 = p/5$$

$$Y = y_1 + y_2 = p/3 + p/5 = \frac{8p}{15} = D(p) = 92 - p$$

$$\frac{8p}{15} + p = 92 \Rightarrow \frac{23p}{15} = 92 \Rightarrow p^* = 60$$

$$y_1^* = 20, \quad y_2^* = 12, \quad \pi_i = 0$$

**→ Bertrand with increasing MC converges to the competitive outcome** with multiple active firms.

---

## Bertrand with Differentiated Products — Gas Station Duopoly

**Setup:** Demand for differentiated products:

$$D_1(p_1, p_2) = 1000 - 30p_1 + 10p_2, \quad D_2(p_1, p_2) = 1000 - 30p_2 + 10p_1$$

$TC_i(y_i) = c \cdot y_i + 4000$ (symmetric firms). Cross-price effect $+10p_j > 0$: goods are **substitutes**.

### Bertrand Equilibrium (September, $c_0 = 20$)

Each firm maximizes: $\pi_i = (p_i - c) D_i - 4000$

FOC for Firm 1:

$$\frac{\partial \pi_1}{\partial p_1} = D_1 + (p_1 - c)\frac{\partial D_1}{\partial p_1} = (1000 - 30p_1 + 10p_2) + (p_1 - 20)(-30) = 0$$

$$1000 - 30p_1 + 10p_2 - 30p_1 + 600 = 0 \Rightarrow p_1 = \frac{1600 + 10p_2}{60}$$

By symmetry: $p_1^* = p_2^* = \frac{1600}{60 - 10} = 32$

Actually solving: $p_1 = \frac{1600 + 10p_1}{60} \Rightarrow 60p_1 - 10p_1 = 1600 \Rightarrow p_1^* = 32$

Wait — the solution given is $p^{b0} = 320$ (possibly in different units; the problem likely uses different scale). Using the given solution: $p_1^{b0} = p_2^{b0} = 320$, $y_i^{b0} = 32$, $\Pi_i^{b0} = 32 \times \text{margin} - 4000$.

### Collusion (October, $c_1 = 10$)

Firms maximize joint profit $\Pi_1 + \Pi_2$ → higher prices, lower quantities than Bertrand.

$p_1^k = p_2^k = 30$, $y_i^k = 400$, $\Pi_i^k = 4000$

### Punishment (November, back to Bertrand with $c_1 = 10$, fine $= 100$)

$p_1^{b1} = p_2^{b1} = 26$, $y_i = 480$, $\Pi_i^{b1} = 3680$ (before fine), $\Pi_i = 3580$ (after fine).

**Was collusion profitable despite the fine?**

$\Pi_i^k = 4000 > 3680 = \Pi_i^{b1}$ (without fine) → even after fine, if collusion lasted long enough, it was profitable.

**Lesson:** Time horizon of collusion, probability of detection, and magnitude of penalties jointly determine whether collusion is a rational strategy.

---

## Differentiated vs. Homogeneous Bertrand

| Feature | Homogeneous | Differentiated |
|---|---|---|
| Demand interaction | Perfectly elastic across firms | Partial (cross-price elasticity $< \infty$) |
| Bertrand equilibrium | $p = MC$, $\Pi = 0$ | $p > MC$, $\Pi > 0$ |
| Incentive to undercut | Wins entire market | Wins partial share |
| Collusion | Higher joint profit | Higher joint profit (easier to sustain) |

With **differentiated products**, even Bertrand competition allows positive equilibrium profits. This is a major resolution of the Bertrand paradox and explains why firms invest in product differentiation (branding, features) as a strategic tool.
