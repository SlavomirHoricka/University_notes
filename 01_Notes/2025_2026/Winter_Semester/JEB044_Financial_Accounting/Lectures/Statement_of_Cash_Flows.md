---
course: JEB044
topic: Statement of Cash Flows
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/06_Cash_Flow_(act).pdf
tags: [JEB044, financial-accounting, cash-flows, SCF, indirect-method, CFO, CFI, CFF]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/06_Cash_Flow_(act).pdf]]
Related: [[Income_Statement_Structure]], [[Accruals_and_Deferrals]], [[Accounting_Framework_and_Financial_Statements]]

# Statement of Cash Flows

## Purpose

The Statement of Cash Flows (SCF) summarises all **cash receipts and outlays** during a fiscal period, divided into three activities. It answers: "where did cash come from, and where did it go?"

$$\Delta \text{Cash} = CFO + CFI + CFF$$

where $\Delta\text{Cash} = \text{Cash}_t - \text{Cash}_{t-1}$.

## Three Sections

| Section | Abbreviation | Content |
|---|---|---|
| Operating Activities | CFO | Cash effects of transactions creating revenues and expenses |
| Investing Activities | CFI | Cash from acquiring/disposing of long-term assets and investments |
| Financing Activities | CFF | Cash from issuing/repaying debt and equity; dividends paid |

### Classification Rules

- **Financing:** equity issuance or repurchase, debt issuance or repayment, dividends paid, stock buybacks.
- **Investing:** purchases/sales of PP&E, intangibles, subsidiaries, financial investments (non-operating).
- **Operating:** all remaining cash flows.

**Cost-benefit mismatch:** buying a machine (CFI outflow) generates revenues over many years (CFO inflows). This structural mismatch means young capital-intensive firms appear cash-flow negative in CFI while being positive in CFO.

## BS Derivation of the SCF

Starting from the accounting equation $\text{As} = \text{Li} + \text{Eq}$ and taking first differences:

$$\Delta\text{Cash} = \Delta\text{Eq} + \Delta\text{Li} - \Delta\text{Other Assets}$$

Expanding using BS abbreviations (COA = current operating assets, CFA = current financial assets, XA = fixed assets, COL = current operating liabilities, CFL = current financial liabilities, LTFL = long-term financial liabilities, CC = contributed capital, ARE = accumulated retained earnings):

$$\Delta\text{Cash} = \underbrace{NI + Dp - \Delta COA + \Delta COL}_{CFO} \underbrace{- CapEx}_{CFI} \underbrace{+ \Delta CC - Dv + \Delta LTFL + \Delta CFL - \Delta CFA}_{CFF}$$

where capital expenditures are linked to the BS by:

$$CapEx = Dp + \Delta XA \quad \Longleftrightarrow \quad \Delta XA = CapEx - Dp$$

**Clean Surplus identity:**

$$\Delta ARE_t = NI_t - Dv_t$$

## Interest and Dividends — Classification Differences

| Standard | Interest paid | Dividends paid | Interest received | Dividends received |
|---|---|---|---|---|
| **US GAAP** | CFO | CFF | CFO | CFO |
| **IFRS (current)** | CFO or CFF | CFO or CFF | CFO or CFI | CFO or CFI |

IFRS gives management a choice; US GAAP mandates CFO for interest.

## Indirect Method (Required for CFO)

Both US GAAP and IFRS require the **indirect method** for the CFO section (though the direct method is permitted with supplemental indirect disclosure). CFI and CFF sections always use the direct method.

The indirect method starts from Net Income and adjusts for non-cash items and changes in working capital:

$$CFO = NI + Dp - \Delta\text{Current Operating Assets} + \Delta\text{Current Operating Liabilities}$$

### Step-by-Step Indirect Method Template

```
Net Income (NI)                                     + NI
Add back non-cash expenses:
  Depreciation & Amortisation                       + Dp
Changes in working capital:
  Increase in AR                                    – (cash not yet received)
  Decrease in AR                                    + (cash received > revenue)
  Increase in Inventory                             – (cash paid > COGS)
  Decrease in Inventory                             + (COGS > cash paid)
  Increase in Prepaid Expenses                      –
  Decrease in Prepaid Expenses                      +
  Increase in Accounts Payable                      + (expense > cash paid)
  Decrease in Accounts Payable                      –
  Increase in Accrued Liabilities                   + (expense > cash paid)
  Decrease in Accrued Liabilities                   –
= Cash from Operating Activities (CFO)
```

### Why Subtract Gains on Asset Sales from CFO

When a fixed asset is sold at a gain, the total proceeds appear in CFI. The gain component (proceeds minus book value) is included in NI. To avoid double-counting, the gain is **subtracted from NI** in CFO.

## Interpretation: Cash Flow Life-Cycle Profiles

The BCG matrix framework maps company life-cycle stage to SCF profile:

| Stage | CFO | CFI | CFF | Interpretation |
|---|---|---|---|---|
| Question Mark (startup) | – | – | + | Burning cash, investing heavily, raising funds |
| Star (growth) | + | – | ± | Generating cash but investing aggressively |
| Cash Cow (mature) | ++ | – small | – | High CFO, modest maintenance CapEx, returning cash |
| Lousy Dog (decline) | – or small+ | + | – | Selling assets, no investment, paying down debt |
