---
course: "JEB027"
topic: "Finanční výkazy banky — rozvaha, výkaz zisku/ztráty, ROA, ROE, NIM"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_FINE_P04A-2025_Finanční_výkazy.pdf"
tags: [JEB027, financni-vykazy, rozvaha, ROA, ROE, NIM, bankovni-analyza]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_FINE_P04A-2025_Finanční_výkazy.pdf]]
Related: [[ROA_ROE_Analyza]], [[Komercni_Bankovnictvi]], [[Bancni_Regulace_a_Basel]], [[Akcie_a_Oceneni]]

# Finanční výkazy banky

## Rozvaha komerční banky (Balance Sheet)

Rozvaha zachycuje **stav** aktiv, pasiv a vlastního kapitálu banky k určitému datu. Na rozdíl od nefinančních firem má bankovní rozvaha specifickou strukturu.

### Aktiva banky (Assets)

| Položka | Popis |
|---------|-------|
| **Hotovost a rezervy u CB** | Povinné minimální rezervy + dobrovolné rezervy; nejlikvidnější položka |
| **Cenné papíry** | Státní dluhopisy, korporátní dluhopisy — likvidní rezerva a investiční portfolio |
| **Úvěry (Loans)** | Největší část aktiv; hypoteční úvěry, korporátní úvěry, spotřebitelské úvěry |
| **Mezibankovní pohledávky** | Vklady u jiných bank (např. přes mezibankovní trh) |
| **Ostatní aktiva** | Hmotný majetek, goodwill, pohledávky |

### Pasiva a vlastní kapitál (Liabilities & Equity)

| Položka | Popis |
|---------|-------|
| **Depozita (klientská)** | Netermínované (current accounts) a termínované (time deposits) vklady — nejdůležitější pasivum |
| **Mezibankovní závazky** | Výpůjčky od jiných bank na mezibankovním trhu |
| **Vydané dluhopisy / CDO** | Dlouhodobé refinancování |
| **Podřízený dluh** | Zahrnuje se do Tier 2 kapitálu |
| **Vlastní kapitál (Equity)** | Základní kapitál + nerozdělený zisk; tvoří regulatorní Tier 1 kapitál |

### Klíčová vlastnost: transformace splatností

Banka přijímá **krátkodobé závazky** (depozita — netermínovaná, splatná na požádání) a vytváří **dlouhodobá aktiva** (hypoteční úvěry — splatnost 15–30 let). Tato **transformace splatností** (maturity transformation) je zdrojem bankovního zisku i rizika (interest rate risk, liquidity risk).

## Výkaz zisku a ztráty banky (Income Statement / P&L)

```
Čisté úrokové výnosy (NII = Net Interest Income)
+ Čisté poplatky a provize
+ Výnosy z obchodování
= Celkové provozní výnosy (Total Operating Income)
- Provozní náklady (operating expenses, incl. personnel)
= Provozní zisk (EBITDA-like)
- Opravné položky na úvěrové ztráty (Loan Loss Provisions / LLP)
= Zisk před zdaněním (EBT)
- Daň z příjmů
= Čistý zisk (Net Income)
```

### Čistá úroková marže (NIM — Net Interest Margin)

Klíčový ukazatel ziskovosti banky:

$$\boxed{NIM = \frac{\text{Čisté úrokové výnosy}}{\text{Průměrný stav úrokových aktiv}}}$$

$$NIM = \frac{\text{Úrokové výnosy} - \text{Úrokové náklady}}{\text{Průměrný stav aktiv}}$$

- NIM v ČR je historicky vysoká (v porovnání s eurozónou): důvod — ČNB nastavuje vyšší základní sazby, levná depozita domácností (captive depositor base).
- Nízká NIM v eurozóně (2015–2022): důsledek záporných nebo nulových repo sazeb ECB.

## Klíčové ukazatele výkonnosti banky

Detailní rozbor viz [[ROA_ROE_Analyza]].

### Ukazatel C/I (Cost-to-Income Ratio)

$$C/I = \frac{\text{Provozní náklady}}{\text{Celkové provozní výnosy}}$$

Nižší hodnota = vyšší efektivita. Evropské banky mají C/I typicky 55–70 %, česká banka (Komerční banka, ČSOB) cca 40–50 %.

### NPL Ratio (Non-Performing Loans)

$$NPL\% = \frac{\text{Nevýkonné úvěry (NPL)}}{\text{Celkové úvěry}} \times 100$$

Nevýkonný úvěr = úvěr se splátkami v prodlení déle než 90 dní. Vysoký NPL signalizuje zhoršenou kvalitu úvěrového portfolia.

### P/BV (Price-to-Book Value)

$$P/BV = \frac{\text{Tržní kapitalizace}}{\text{Účetní hodnota vlastního kapitálu}}$$

$P/BV < 1$ u bank v eurozóně (2015–2022) implikuje, že trh oceňuje banku **pod** její účetní hodnotou — signál nižšího ziskového potenciálu (nízké sazby, vysoké regulatorní náklady, strukturální problémy).

## Datová analytika v bankách

Přednáška zdůrazňuje roli datové analytiky při finančním rozhodování:

| Typ analytiky | Otázka | Příklad v bankovnictví |
|---------------|--------|------------------------|
| **Deskriptivní** | Co se stalo? | Reporting výkonnosti úvěrového portfolia |
| **Diagnostická** | Proč se to stalo? | Analýza příčin nárůstu NPL |
| **Prediktivní** | Co se stane? | Credit scoring, predikce defaultu |
| **Preskriptivní** | Co dělat? | Optimalizace cenové politiky úvěrů |
| **Adaptivní** | Jak se poučit? | Kontinuální rekalibracea modelů ML |

Viz [[Decentralizovane_Finance]] a [[ESG_Finance]] pro moderní technologické trendy ovlivňující bankovní byznys model.
