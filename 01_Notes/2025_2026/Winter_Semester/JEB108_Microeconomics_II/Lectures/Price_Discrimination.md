---
course: "JEB108"
topic: "Price Discrimination"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/8_price_discrimination.pdf"
tags: [JEB108, microeconomics, price-discrimination, monopoly, welfare]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/8_price_discrimination.pdf]]
Related: [[Monopoly]], [[Consumer_Surplus_and_Welfare_Measures]], [[Industry_Equilibrium]], [[Oligopoly_Models]]

# Price Discrimination

## Definition

**Price discrimination** occurs when a firm sells the same or similar product at **different prices** to different buyers for reasons **not attributable** to cost differences.

**Conditions required:**
1. **Market power** — the firm must be able to set prices (price-maker).
2. **Segmentable market** — the firm must be able to identify and separate buyer groups.
3. **No arbitrage** — buyers in the cheap segment cannot resell to buyers in the expensive segment.

---

## First-Degree (Perfect) Price Discrimination

The firm charges each buyer their **maximum willingness to pay** (reservation price), extracting **all consumer surplus**.

**Outcome:**
- Each unit sold at its individual demand price.
- Firm's revenue = entire area under the demand curve (up to sold quantity).
- **Consumer surplus = 0** (all transferred to firm as profit).
- **No deadweight loss:** every unit where $p \geq MC$ is traded → efficient outcome.
- Output equals the competitive output level $y^{PC}$.

**Formula:**

$$\pi^{PD1} = \int_0^{y^*} [p(y) - MC(y)]\, dy$$

where $y^*$ is determined by $p(y^*) = MC(y^*)$.

**Limitation:** Perfect information about each buyer's willingness to pay is required. In practice, approximated by:
- **Individual negotiation** (car dealerships, salary negotiations)
- **Versioning** (software editions, airline seats)

---

## Second-Degree Price Discrimination

The firm cannot identify individual types but charges different prices for **different quantities or versions** of the good, relying on buyers to **self-select**.

### Non-Linear Pricing

The firm sets a **price schedule** $p(y)$ rather than a single unit price. Buyers choose how much to buy.

**Block pricing:** different per-unit prices for different quantity ranges.

**Two-part tariff:** $T(y) = A + p \cdot y$

- $A$: fixed access fee (extracts consumer surplus)
- $p$: per-unit price

**Optimal two-part tariff (homogeneous consumers):**
- Set $p = MC$ (eliminates DWL)
- Set $A = CS(p = MC)$ (extracts all surplus as fixed fee)
- Efficient and profit-maximizing simultaneously.

**Volume discounts / bundling**: used when consumers differ in quantity demanded.

### Bundling

**Pure bundling:** goods sold only as a package.
**Mixed bundling:** goods sold both separately and as a bundle.

Bundling is profitable when consumers have **negatively correlated** willingness to pay across goods (one consumer values $A$ more than $B$, another values $B$ more than $A$).

### Quality Discrimination (Versioning)

Firm offers multiple quality levels at different prices. Higher-type consumers self-select into higher-quality/higher-price version.

**Application:** First-class vs. economy airline tickets; premium vs. standard software.

**Puzzle from Lecture:** Why do budget airlines charge for meals while luxury hotels charge for WiFi?
- Budget airlines: meal is a differentiating add-on; its cost is borne by those who value it (enables self-selection).
- Luxury hotels: WiFi is expected by all clients; charging separately reduces total consumer surplus — instead, they include it and raise room rates.

---

## Third-Degree Price Discrimination

The firm can **identify** buyer groups (markets) but cannot observe individual reservation prices within each group. It charges **different prices** in different market segments.

### Optimization Problem

Maximize total profit across $n$ segments:

$$\pi = \sum_{i=1}^n [p_i \cdot y_i - c(\sum_i y_i)]$$

**FOC for each segment $i$:**

$$MR_i(y_i) = MC(Y) \quad \forall i$$

All segments are operated at the output where segment-specific MR equals the common MC.

**Implication:** Segment with **less elastic demand** gets charged a **higher price**.

From the Lerner index in each segment:

$$\frac{p_i - MC}{p_i} = \frac{1}{|\varepsilon_i^D|}$$

$$\frac{p_1}{p_2} = \frac{1 - 1/|\varepsilon_2^D|}{1 - 1/|\varepsilon_1^D|}$$

If $|\varepsilon_1^D| < |\varepsilon_2^D|$ (segment 1 less elastic) → $p_1 > p_2$.

### Examples

| Context | High-price segment | Low-price segment |
|---|---|---|
| Pharmaceutical | Developed markets (inelastic) | Developing markets (elastic) |
| Rail tickets | Business travellers (inelastic) | Leisure travellers (elastic) |
| Cinema | Peak times (inelastic) | Off-peak / students (elastic) |
| Software | Commercial users | Academic / student |

### Welfare Effects

Third-degree price discrimination:
- May increase or decrease total output compared to uniform pricing.
- Always **reduces consumer surplus** in the high-price segment; may increase it in the low-price segment.
- Total welfare effect **ambiguous** — depends on whether the discriminating firm serves markets it would otherwise abandon.
- **Output increases in at least one segment** (otherwise discrimination is not profitable), so new trade is created.

---

## Comparison of Discrimination Degrees

| Degree | Information required | DWL | CS | Efficiency |
|---|---|---|---|---|
| 1st (perfect) | Individual willingness to pay | 0 | 0 (all to firm) | Efficient |
| 2nd (self-selection) | Quantity choices, versions | Partial | Partially extracted | Closer to efficient |
| 3rd (market segments) | Group membership | Reduced vs. monopoly | Mixed | Ambiguous |
| Uniform monopoly | Only aggregate demand | Full DWL | Highest consumer share | Inefficient |
