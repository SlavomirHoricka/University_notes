---
course: JEB044
topic: Sales Returns and Allowances
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/04_Accounts_Receivable_(act).pdf
tags: [JEB044, financial-accounting, sales-returns, contra-revenue, SRA]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/04_Accounts_Receivable_(act).pdf]]
Related: [[Accounts_Receivable_and_Credit_Sales]], [[Income_Statement_Structure]], [[Inventory_Cost_Flow_Assumptions]]

# Sales Returns and Allowances

## Definition

**Sales Returns and Allowances (SRA)** is a **contra-revenue** account that records the value of goods returned by customers or price concessions granted for defective/unsatisfactory goods. It is deducted from Gross Sales to arrive at **Net Sales**:

$$\text{Net Sales} = \text{Gross Sales} - SRA - \text{Sales Discounts}$$

Using a separate contra-revenue account (rather than simply reversing the original sales credit) preserves a clear audit trail of gross sales activity while still correctly reducing reported revenue.

## Journal Entries

### On a Credit-Sale Return (Goods Not Yet Paid)

The customer returns goods; the receivable is cancelled and inventory is restored:

| Account | Dr | Cr |
|---|---|---|
| Sales Returns and Allowances (SRA) | Selling Price | |
| Accounts Receivable | | Selling Price |
| Inventory | Purchase Cost | |
| Cost of Goods Sold | | Purchase Cost |

SRA is debited (contra-revenue account increases on the debit side) and AR is credited (the claim is extinguished). The inventory is restored at its original carrying cost, which simultaneously reverses the COGS entry.

### On a Cash-Sale Return (Refund Issued)

| Account | Dr | Cr |
|---|---|---|
| Sales Returns and Allowances (SRA) | Selling Price | |
| Cash | | Selling Price |
| Inventory | Purchase Cost | |
| COGS | | Purchase Cost |

### Allowance Granted (No Physical Return)

A price reduction granted for minor defects without return of goods:

| Account | Dr | Cr |
|---|---|---|
| Sales Returns and Allowances (SRA) | Allowance Amount | |
| Accounts Receivable / Cash | | Allowance Amount |

No inventory or COGS entry — the goods were not returned.

## Allowance for Sales Returns (ASRA)

Under IFRS 15, a firm must estimate expected returns at the point of sale and record a refund liability:

$$\text{Net Revenue} = \text{Gross Revenue} - \text{Estimated Returns}$$

The **Asset for Recovery of Returned Goods (ASRA)** is a contra-asset (debit-normal) that represents the expected inventory to be recovered from anticipated returns. It is the mirror of the refund liability on the other side of the balance sheet:

- Dr Refund Liability (or SRA) / Cr Deferred Revenue
- Dr ASRA (estimated recovery) / Cr COGS

ASRA sits as a current asset separate from inventory until goods are actually returned.

## Income Statement Presentation

SRA typically appears as a deduction line in the revenue section:

```
Gross Sales                  1,000
  Less: Sales Returns           (40)
  Less: Sales Discounts         (10)
Net Sales                      950
```

Analysts scrutinise the SRA/Gross Sales ratio for trends — an increasing ratio may signal product quality problems or channel-stuffing reversals.
