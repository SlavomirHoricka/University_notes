---
course: "JEB108"
topic: "Cost Curves"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/4_cost_curves.pdf"
tags: [JEB108, microeconomics, cost-curves, average-cost, marginal-cost]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/4_cost_curves.pdf]]
Related: [[Cost_Minimization]], [[Profit_Maximization_Firm]], [[Firm_Supply_Curve]], [[Returns_to_Scale]]

# Cost Curves

## Total Cost Decomposition

Total costs decompose into fixed and variable components:

$$TC(y) = FC + VC(y)$$

| Component | Symbol | Definition |
|---|---|---|
| Total Cost | $TC$ | $FC + VC(y)$ |
| Fixed Cost | $FC$ | Independent of output; unavoidable in short run |
| Variable Cost | $VC(y)$ | Depends on output |
| Average Total Cost | $ATC$ | $TC(y)/y = AFC + AVC$ |
| Average Fixed Cost | $AFC$ | $FC/y$ — always decreasing in $y$ |
| Average Variable Cost | $AVC$ | $VC(y)/y$ |
| Marginal Cost | $MC$ | $dTC/dy = dVC/dy$ |

**Note:** In the short run, the firm always pays $FC$ regardless of output. In the long run, all costs are variable (no fixed costs) — though **quasi-fixed costs** (paid only at $y > 0$) may exist.

---

## Geometric Relationships

### MC, ATC, AVC

Key relationships that determine the characteristic U-shaped cost curves:

1. **MC cuts ATC and AVC at their minima:**

   When $MC < ATC$: $\frac{d(ATC)}{dy} = \frac{MC - ATC}{y} < 0$ → ATC is falling.
   
   When $MC > ATC$: ATC is rising.
   
   Therefore: $MC = ATC$ at $\min(ATC)$. Same logic applies to AVC.

2. **AVC lies below ATC** by $AFC = FC/y > 0$.

3. **ATC and AVC converge** as $y \to \infty$ (since $AFC \to 0$).

### Derivation: Why MC = ATC at Minimum

$$ATC(y) = \frac{TC(y)}{y}$$

$$\frac{d(ATC)}{dy} = \frac{MC \cdot y - TC}{y^2} = \frac{MC - ATC}{y} = 0 \iff MC = ATC$$

---

## Short-Run vs. Long-Run Cost Curves

### Short-Run Cost Curves (SRATC, SRAVC, SRMC)

- With fixed input $\bar{x}_2$: firm can only adjust $x_1$.
- Short-run TC: $STC(y, \bar{x}_2) = w_1 x_1^s(y, \bar{x}_2) + w_2 \bar{x}_2$
- The fixed cost $w_2 \bar{x}_2$ creates a wedge between $STC$ and $SVC$.

### Long-Run Cost Curves (LRATC, LRMC)

- All inputs optimally adjusted: $LTC(y) = c(w, y)$.
- **No fixed costs** in the long run.
- Shape determined by returns to scale:
  - IRS → LRATC decreasing
  - CRS → LRATC constant (horizontal)
  - DRS → LRATC increasing

### Relationship: Envelope Theorem

The long-run cost curve is the **lower envelope** of all short-run cost curves:

$$LTC(y) = \min_{\bar{x}_2} STC(y, \bar{x}_2)$$

At the output level where the fixed input is optimally chosen, $LTC$ and $STC$ are tangent:

$$LTC(y_0) = STC(y_0, x_2^*(y_0)), \quad \frac{dLTC}{dy}\bigg|_{y_0} = \frac{dSTC}{dy}\bigg|_{y_0}$$

This means $LRMC = SRMC$ at the point of tangency, but $LRATC \leq SRATC$ everywhere, with equality at $y_0$.

---

## U-Shaped Average Cost Curves

The typical **U-shape** of SRATC arises from:
- **Decreasing ATC phase:** Increasing returns (input specialisation, fixed cost spreading) dominate.
- **Minimum ATC:** Efficient scale of production.
- **Increasing ATC phase:** Diminishing marginal product (fixed inputs become bottleneck).

---

## Cost Curves and Returns to Scale

| Returns to Scale | Long-Run MC | Long-Run ATC |
|---|---|---|
| IRS ($a+b > 1$ in CDS) | Decreasing | Decreasing ($LMC < LRATC$) |
| CRS ($a+b = 1$) | Constant | Constant ($LMC = LRATC$) |
| DRS ($a+b < 1$) | Increasing | Increasing ($LMC > LRATC$) |

**Proof for Cobb-Douglas** $f = x_1^a x_2^b$:

Cost function: $c(w, y) \propto y^{1/(a+b)}$

$$LMC = \frac{\partial c}{\partial y} \propto \frac{1}{a+b} y^{1/(a+b)-1}, \quad LRATC = \frac{c}{y} \propto y^{1/(a+b)-1}$$

$LMC < LRATC \iff \frac{1}{a+b} < 1 \iff a+b > 1$ (IRS). ✓

---

## Applications

### Milk vs. Soft Drink Containers (Puzzle from Lecture 3)

Milk is sold in rectangular cartons, soft drinks in cylindrical cans. **Cost minimization explains this:**
- Cylindrical cans minimize material cost for a given volume ($\pi r^2 h$ content, $2\pi r h + 2\pi r^2$ surface).
- However, milk is stored in **refrigerated grocery cases** where rectangular containers pack more efficiently, reducing wasted space and logistics costs.
- Soft drinks are displayed on **open shelving** where the visual appeal of cylinders aids marketing.
- → **Different cost structures** (logistics vs. display) produce different optimal container shapes.

### Drive-Up ATM Braille (Puzzle from Lecture 3)

Braille dots on drive-up ATM keypads: **Cost minimization logic** — it is cheaper to produce a single standardized keypad for all ATMs than to manufacture two separate versions for drive-up and walk-up machines. The marginal cost of adding Braille to a drive-up keypad is essentially zero.
