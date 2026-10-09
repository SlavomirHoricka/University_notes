---
course: JEB044
topic: Double-Entry Bookkeeping
source: 00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/01_Accounting_Framework_(act).pdf
tags: [JEB044, financial-accounting, bookkeeping, T-account, debits, credits]
created: 2026-04-20
---
Parent: [[JEB044_Financial_Accounting_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB044_Financial_Accounting/Lectures/01_Accounting_Framework_(act).pdf]]
Related: [[Accounting_Framework_and_Financial_Statements]], [[Balance_Sheet_Elements]], [[Income_Statement_Structure]]

# Double-Entry Bookkeeping

## Core Principle

Every economic transaction affects at least two accounts such that:

$$\sum \text{Debits} = \sum \text{Credits}$$

This invariant ensures the accounting equation $\text{Assets} = \text{Liabilities} + \text{Equity}$ holds after every transaction. An entry that would violate this equality is arithmetically impossible within the double-entry system.

## T-Account Structure

Each general ledger account is visualised as a T-account:

```
        Account Name
    ┌──────────┬──────────┐
    │  Debit   │  Credit  │
    │  (left)  │  (right) │
    └──────────┴──────────┘
```

The **balance** of an account = (sum of debits) – (sum of credits) for debit-normal accounts, or the reverse for credit-normal accounts.

## Normal Balance Conventions

| Account Category | Normal Balance | Increases on | Decreases on |
|---|---|---|---|
| Assets | Debit | Debit | Credit |
| Expenses | Debit | Debit | Credit |
| Contra-assets (e.g. AUA) | Credit | Credit | Debit |
| Liabilities | Credit | Credit | Debit |
| Equity | Credit | Credit | Debit |
| Revenues | Credit | Credit | Debit |

Contra-accounts carry the opposite normal balance of the account they offset and are subtracted from their paired account on the balance sheet.

## Journal Entry Format

Transactions are first recorded in the **general journal** as journal entries, then posted to individual T-accounts in the **general ledger**.

Standard format (debit lines first, indented credits):

```
Dr  Account A          XXX
    Cr  Account B              XXX
    Cr  Account C              XXX
```

## Worked Examples

### Example 1 — Cash Sale

Sell goods costing $300 for $500 cash.

| Step | Account | Dr | Cr |
|---|---|---|---|
| Record revenue | Cash | 500 | |
| | Sales Revenue | | 500 |
| Record COGS | Cost of Goods Sold | 300 | |
| | Inventory | | 300 |

Check: Dr total = 800; Cr total = 800 ✓

### Example 2 — Credit Purchase of Inventory

Purchase $200 of inventory on account.

| Account | Dr | Cr |
|---|---|---|
| Inventory | 200 | |
| Accounts Payable | | 200 |

### Example 3 — Payment of Wages

Pay $150 in wages in cash.

| Account | Dr | Cr |
|---|---|---|
| Wages Expense | 150 | |
| Cash | | 150 |

## Trial Balance

Before preparing financial statements, an accountant prepares a **trial balance** — a listing of all account balances verifying that total debits equal total credits. It catches arithmetic errors but not errors of omission or incorrect account classification.

## Relationship to Financial Statements

Debit/credit flows map directly onto statement construction:

- Revenue accounts (Cr-normal): closed to Retained Earnings at period end, feeding the IS.
- Expense accounts (Dr-normal): closed to Retained Earnings at period end.
- Permanent accounts (Assets, Liabilities, Equity): balances carry forward to the next period's BS.
