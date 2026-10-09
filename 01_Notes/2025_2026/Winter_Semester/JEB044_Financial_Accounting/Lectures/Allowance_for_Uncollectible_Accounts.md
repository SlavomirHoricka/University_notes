---
course: JEB044
topic: Allowance for Uncollectible Accounts (Bad Debts)
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/04_Accounts_Receivable_(act).pdf
tags: [JEB044, financial-accounting, bad-debts, allowance-method, direct-write-off, aging-schedule]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/04_Accounts_Receivable_(act).pdf]]
Related: [[Accounts_Receivable_and_Credit_Sales]], [[Accounting_Conservatism_and_Contingencies]], [[Income_Statement_Structure]]

# Allowance for Uncollectible Accounts

## The Bad Debt Problem

Credit sales generate AR, but some customers will not pay. Two competing methods exist for recognising this loss:

| Method | Principle | Required by |
|---|---|---|
| **Direct Write-Off** | Record bad debt expense only when a specific account is confirmed uncollectible | Tax accounting (reliability) |
| **Allowance Method** | Estimate and pre-recognise expected losses in the same period as the related sales | Financial accounting / GAAP / IFRS (relevance) |

### Why Financial Accounting Requires the Allowance Method

The Direct Write-Off method violates the matching principle: bad debt expense is recognised in a later period than the associated revenue. This **overstates net income** in the sale period and understates it in the write-off period. The allowance method corrects this (the "dating game" — match the loss to the revenue).

### Why Tax Accounting Requires Direct Write-Off

The tax authority requires actual confirmation before allowing a deduction. Estimates are not accepted because they could be inflated to suppress taxable income (the "begging game" — only recognise the loss when it is clearly real).

## The Allowance for Uncollectible Accounts (AUA)

AUA is a **contra-asset** account (credit-normal balance) that offsets gross AR on the balance sheet:

$$\text{Net AR} = AR_{\text{gross}} - AUA$$

Alternative names used in practice:
- Allowance for Doubtful Accounts
- Allowance for Bad Debts
- Provision for Credit Losses

## Journal Entries

### Recognising Bad Debt Expense (End of Period)

| Account | Dr | Cr |
|---|---|---|
| Bad Debt Expense | Estimated Amount | |
| Allowance for Uncollectible Accounts (AUA) | | Estimated Amount |

This entry reduces NI and reduces Net AR, without yet identifying which specific customer will default.

### Writing Off a Specific Account (When Default is Confirmed)

| Account | Dr | Cr |
|---|---|---|
| AUA | Amount Written Off | |
| Accounts Receivable (specific customer) | | Amount Written Off |

This entry **does not affect Net AR** (both gross AR and AUA decrease by the same amount) and **does not affect NI** (expense was already recognised).

### Subsequent Recovery (Reversing a Write-Off)

First restore the receivable, then record the cash collection:

| Step | Account | Dr | Cr |
|---|---|---|---|
| Restore | Accounts Receivable | Recovered Amount | |
| | AUA | | Recovered Amount |
| Collect | Cash | Recovered Amount | |
| | Accounts Receivable | | Recovered Amount |

## Estimating the AUA

### Method 1 — Income Statement Approach (% of Credit Sales)

Estimate bad debt expense as a fixed percentage of credit sales for the period:

$$\text{Bad Debt Expense} = \% \times \text{Net Credit Sales}$$

Focus is on the IS (matching). AUA is a by-product.

### Method 2 — Balance Sheet Approach (Aging Schedule)

Estimate the **ending balance of AUA** required based on the age composition of outstanding AR. Older receivables are more likely to default:

| Age Bucket | Typical Default Rate |
|---|---|
| < 30 days | 1% |
| 30–60 days | 3% |
| > 60 days | 10% |

$$AUA_{\text{target}} = \sum_i (\text{AR in bucket}_i \times \text{rate}_i)$$

$$\text{Bad Debt Expense} = AUA_{\text{target}} - AUA_{\text{current balance (before adjustment)}}$$

Focus is on the BS (NRV of AR). NI is a by-product.

Alternatively a single overall percentage of total AR or a **specific account analysis** may be applied.

## Worked Example

Given:
- $AUA_{2000} = 22$
- $AR_{2001} = 300$ (gross, end of year)
- During 2001, accounts totalling $2 were written off (i.e. $AUA_{\text{temporary, after write-offs}} = 22 - 2 = 20$, but the target AUA is computed fresh)
- Aging analysis implies $AUA_{\text{target}, 2001} = 28$

$$\text{Bad Debt Expense}_{2001} = 28 - (22 - 2) = 28 - 20 = 8$$

Resulting balances:
- $AUA_{2001} = 28$
- $\text{Net AR}_{2001} = 300 - 28 = 272$

## Balance Sheet Disclosure

The BS shows only **Net AR**; the gross amount and AUA balance are typically disclosed in the notes:

> *Accounts receivable, net of allowance for uncollectible accounts of $28 …………… $272*
