---
course: JEB044
topic: Minority Interest (Non-Controlling Interest)
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/11_Extra_Minority_Interest_(act).pdf
tags: [JEB044, financial-accounting, minority-interest, consolidation, non-controlling-interest, subsidiary]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/11_Extra_Minority_Interest_(act).pdf]]
Related: [[Balance_Sheet_Elements]], [[Goodwill_and_Mergers_Acquisitions]]

# Minority Interest (Non-Controlling Interest)

## Definition

> **Minority interest** (or non-controlling interest, NCI) is the portion of a subsidiary corporation's stock that is **not owned by the parent corporation**. It is reported on the consolidated balance sheet to reflect the claim on assets belonging to other, non-controlling shareholders. — *wikipedia.com (as cited in lecture)*

Minority interest arises when a parent company acquires a **controlling stake** (>50% but <100%) of a subsidiary. The subsidiary is consolidated — all its assets and liabilities appear on the parent's BS — but the minority shareholders' claim must be separately recognised.

## Three Consolidation Methods

| Method | Description | Status |
|---|---|---|
| **1. No consolidation** | All three firms report BS separately | ✗ Not acceptable |
| **2. Proportional consolidation** | Parent reports only its % share of subsidiary As and Li | ✗ Not acceptable under IFRS/US GAAP for subsidiaries |
| **3. Consolidation with minority interest** | Parent reports **100%** of subsidiary As and Li; minority claim recognised in equity | ✓ Required |

Under method 3, the consolidated BS includes all of the subsidiary's assets (even the minority-owned share), with the minority interest appearing in the **equity section** as a separate line.

## Basic Numerical Example (No Goodwill)

SubCo: $As = 1,000$, $Li = 400$, $Eq = 600$. MajorCo acquires 75% of SubCo. Market values equal book values; no acquisition premium.

$$BV(NA) = As - Li = 1,000 - 400 = 600$$

$$MI = 0.25 \times BV(NA) = 0.25 \times 600 = \mathbf{150}$$

$$P(\text{75\% NA}) = MV(\text{75\% NA}) = 0.75 \times 600 = \mathbf{450}$$

**Consolidated BS entry:**

| Assets | Liabilities & Equity |
|---|---|
| Cash: –450 (paid) | Liabilities: +400 |
| Identifiable Assets: +1,000 | Minority Interest (in Eq): +150 |

MajorCo raises equity of 150 from MinorCo and uses 150 + 450 = 600 total to acquire all net assets.

## General Formula for Minority Interest

$$MI = (\text{Revalued Net Assets} + \text{Goodwill}) - \text{Purchase Price}$$

More precisely, MI is the **minority shareholders' share of the subsidiary's total fair value** (net assets + any goodwill attributable to minority). The exact figure depends on whether goodwill is computed on book values or market values (see [[Goodwill_and_Mergers_Acquisitions]]).

## Treatment in Valuation and ROE

- **ROE computation:** minority interest is typically included as part of equity (denominator).
- **Per-share valuation:** the minority claim is **subtracted from total firm value** before dividing by shares outstanding held by the parent's shareholders.

This prevents double-counting: the parent's equity value includes the subsidiary's total earnings but must net out the minority's proportional claim.
