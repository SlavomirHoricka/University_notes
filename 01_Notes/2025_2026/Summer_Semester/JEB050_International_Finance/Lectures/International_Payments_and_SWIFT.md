---
course: JEB050
topic: International Payments, SWIFT Architecture, and Financial Sanctions
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_2/Week2_Slides.pdf
tags: [JEB050, SWIFT, correspondent-banking, financial-sanctions, international-payments]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_2/Week2_Slides.pdf]]
Related: [[BOP_and_IIP]]

# International Payments, SWIFT Architecture, and Financial Sanctions

## Correspondent Banking

Cross-border payments are executed primarily through **correspondent banking** — a network in which banks hold accounts (called **nostro accounts** — "our account at your bank") at each other internationally.

**Payment chain example** (Czech company paying a US supplier):
1. Czech company instructs its Czech bank (Bank A) to transfer USD to the supplier's US bank (Bank B).
2. Bank A does not hold a USD account directly at Bank B. Instead, it uses its **correspondent bank** (Bank C) in the US.
3. Bank A's nostro account at Bank C is debited; Bank C then credits Bank B's account (or its own nostro at Bank B if they are also correspondents).

Each correspondent banking relationship involves:
- **Account maintenance** and liquidity management
- **Compliance checks** (AML/KYC) at each link in the chain

## SWIFT

**SWIFT** (Society for Worldwide Interbank Financial Telecommunication) is the global messaging network that transmits payment instructions between financial institutions. It does **not** hold funds or execute settlements — it carries the messages.

| Feature | Detail |
|---|---|
| Founded | 1973; headquartered in La Hulpe, Belgium |
| Members | ~11,000+ financial institutions in 200+ countries |
| Traffic | ~50 million messages/day (2020s) |
| Message standards | **MT** (traditional) and **MX/ISO 20022** (modern XML-based) |

### BIC Code

Every SWIFT member is identified by a **Business Identifier Code (BIC)**, also known as a SWIFT code:
- 4-letter bank code + 2-letter country + 2-letter location + optional 3-letter branch
- Example: `CNBACZPP` = Czech National Bank, Czech Republic, Prague

### Key Message Types (MT)
| Code | Purpose |
|---|---|
| MT103 | Customer credit transfer (cross-border payment) |
| MT202 | Bank-to-bank payment (interbank funds transfer) |
| MT700 | Documentary credit (letter of credit) |
| MT950 | Statement message |

## Compliance and AML

Every bank in the correspondent chain is subject to:
- **AML (Anti-Money Laundering)** — Know Your Customer (KYC), screening transactions
- **OFAC (Office of Foreign Assets Control)** — US Treasury sanctions lists; any bank touching USD is subject to US jurisdiction
- **FinCEN** — US Financial Crimes Enforcement Network reporting requirements

Banks are exposed to **de-risking**: exiting high-risk correspondent relationships to avoid regulatory penalties, which can reduce financial access in developing economies.

## Financial Sanctions as an International Policy Tool

Financial sanctions — particularly exclusion from SWIFT — have become a primary instrument of foreign policy (Cipriani, Goldberg, La Spada, 2023).

### SWIFT Exclusion of Russia (2022)

Following the Russian invasion of Ukraine in February 2022, major Russian banks were excluded from SWIFT by EU/US/UK decision. Effects:
- Russian banks could no longer transmit standard international payment messages
- Trade settlement with Russia became complicated for non-sanctioned banks
- Russia pivoted to bilateral arrangements and its domestic **SPFS** (System for Transfer of Financial Messages)

### Alternatives to SWIFT

| System | Country | Usage |
|---|---|---|
| **SPFS** | Russia | Alternative messaging post-2014/2022; limited to ~500 members |
| **CIPS** | China | Cross-Border Interbank Payment System; yuan-denominated; ~100 direct members |
| **TIPS/T2** | EU | TARGET2 for euro settlements (European CB) |

### Implications for USD Hegemony

Dollar dominance in international transactions gives the US **extraterritorial enforcement** power: any institution using correspondent accounts in the US falls under US sanctions jurisdiction. This creates incentives for non-US actors to develop dollar-free payment systems, though de-dollarisation remains limited due to network effects and liquidity advantages of USD.
