---
course: JEB044
topic: Goodwill and Mergers & Acquisitions
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/13_Extra_Mergers_&_Acquisitions.pdf
tags: [JEB044, financial-accounting, goodwill, mergers, acquisitions, purchase-price-allocation, consolidation]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/13_Extra_Mergers_&_Acquisitions.pdf]]
Related: [[Minority_Interest]], [[Balance_Sheet_Elements]]

# Goodwill and Mergers & Acquisitions

## Goodwill — Definition

> "Goodwill is an **intangible asset** that arises as a result of the acquisition of one company by another for a **premium value**. The value of a company's brand name, solid customer base, good customer relations, good employee relations and any patents or proprietary technology represent goodwill." — *Investopedia (as cited in lecture)*

Goodwill is recognised **only in a business combination** — it cannot be internally generated and capitalised. It represents the excess of the purchase price over the fair value of identifiable net assets acquired.

## M&A Mechanics

When BuyerCo acquires a **controlling stake** (>50%) in TargetCo:
1. TargetCo becomes a **subsidiary** of BuyerCo.
2. TargetCo's assets and liabilities are **consolidated** onto BuyerCo's balance sheet.
3. TargetCo's net assets ($As - Li$) are **revalued** to fair value through **purchase price allocation (PPA)**.
4. Goodwill is recognised as the residual:

$$Gw = \text{Purchase Price} - \text{Revalued Net Assets}$$

## Case 1 — 100% Acquisition (No Minority Interest)

**Setup:** TargetCo — book value of assets: 1,000; revalued assets: 1,500; liabilities: 300 (at market). BuyerCo pays **1,700** for 100%.

$$Gw = 1,700 - (1,500 - 300) = 1,700 - 1,200 = \mathbf{500}$$

**Consolidated BS entry (BuyerCo):**

| Assets | Liabilities & Equity |
|---|---|
| Cash: –1,700 | Liabilities: +300 |
| Identifiable Assets: +1,500 | (No minority interest — 100% owned) |
| Goodwill: +500 | |

**Verification:** $1,500 + 500 = 1,700 + 300$ ✓ ($\Sigma$Debits = $\Sigma$Credits)

## Case 2 — Partial Acquisition with Minority Interest

### Basic Setup (No Revaluation Premium)

SubCo: $As = 1,000$, $Li = 400$, $Eq = 600$. MajorCo buys 75% for $P = 0.75 \times 600 = 450$ (no premium). See [[Minority_Interest]] for full treatment.

### Setup with Revaluation Premium

SubCo: book $As = 1,000$, revalued $As = 1,070$; $Li = 400$; $BV(NA) = 600$; $\text{Revalued } NA = 670$. MajorCo buys **75%** for **570**. MinorCo holds remaining 25%.

**Acquisition premium (MajorCo paid vs. 75% of book NA):**

$$Prem = P_{\text{MajorCo}} - BV(75\% \, NA) = 570 - (0.75 \times 600) = 570 - 450 = \mathbf{120}$$

The premium decomposes as: revaluation of net assets + goodwill:

$$Prem = \text{Reval}(NA) + Gw$$

The split between revaluation and goodwill depends on the **minority interest valuation method**.

## Two Minority Interest Valuation Methods

### Method A — MI on Book Values (Acquisition Premium to Majority Only)

Assumes the acquisition premium belongs **entirely to the majority stake**. Minority interest is valued at book value of net assets.

$$MI = Pct_{\text{minority}} \times BV(NA) = 0.25 \times (1,000 - 400) = \mathbf{150}$$

$$Gw = (P_{\text{MajorCo}} + MI) - \text{Revalued}(NA) = (570 + 150) - (1,070 - 400) = 720 - 670 = \mathbf{50}$$

Check: $Prem = \text{Reval}(NA) + Gw = (1,070 - 1,000) + 50 = 70 + 50 = 120$ ✓

**Consolidated BS:**

| Assets | Liabilities & Equity |
|---|---|
| Cash: 570 | Liabilities: 400 |
| Identifiable Assets: 1,070 | Minority Interest: 150 |
| Goodwill: 50 | |

### Method B — MI on Market Values (Premium Distributed Proportionally)

Assumes the acquisition premium is **distributed proportionally** to both majority and minority.

$$MV(NA) = \frac{P_{\text{MajorCo}}}{0.75} = \frac{570}{0.75} = \mathbf{760}$$

$$MI = MV(NA) \times Pct_{\text{minority}} = 760 \times 0.25 = \mathbf{190}$$

$$Gw = MV(NA) - \text{Revalued}(NA) = 760 - (1,070 - 400) = 760 - 670 = \mathbf{90}$$

**Implied premium for 100% NA:**

$$Impl = \frac{Prem}{0.75} = \frac{120}{0.75} = 160$$

Check: $\text{Reval}(NA) + Gw = 70 + 90 = 160$ ✓

**Consolidated BS:**

| Assets | Liabilities & Equity |
|---|---|
| Cash: 570 | Liabilities: 400 |
| Identifiable Assets: 1,070 | Minority Interest: 190 |
| Goodwill: 90 | |

## Comparison of the Two Methods

| Dimension | Method A (Book Value MI) | Method B (Market Value MI) |
|---|---|---|
| Assumption | Majority paid premium; minority did not | Both majority and minority would pay proportional premium |
| MI value | Lower ($150) | Higher ($190) |
| Goodwill | Lower ($50) | Higher ($90) |
| IFRS standard | Permitted (partial goodwill) | Preferred (full goodwill — IFRS 3 default) |

Under **IFRS 3**, the full goodwill method (Method B) is preferred because it presents a complete picture of the acquired entity's fair value.

## Goodwill Impairment

Unlike other intangible assets, goodwill is **not amortised** (US GAAP post-2001; IFRS). Instead, it is subject to an **annual impairment test**. If the carrying value of the reporting unit falls below its recoverable amount, goodwill is written down — reducing both the asset and NI.
