---
course: "JEB009"
topic: "Systém národních účtů a měření HDP"
source: "00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf"
tags: [JEB009, makroekonomie, HDP, národní-účty, I-O-analýza]
created: 2026-04-19
---
Parent: [[JEB009_Makroekonomie_I_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB009_Makroekonomie_I/Lectures/Makro_1_Prednaska_1_3.pdf]]
Related: [[Makroekonomicke_Indexy]], [[Neoklasicky_Model]], [[Vymezeni_a_Metody_Makroekonomie]]

# Systém národních účtů a měření HDP

## Systém národních účtů (SNA)

SNA (navrženo S. Kuznetem, NP 1971) zachycuje toky příjmů a výdajů mezi čtyřmi sektory:

**Dvousektorová ekonomika (Domácnosti + Firmy + Finanční systém):**

Základní identity:
$$Y_D \equiv C + S_D = W + R$$
$$\text{HDP} = C + I = W + R + N + \text{odpisy}$$
$$\therefore Y_D = \text{HDP} - N - \text{odpisy}$$
$$I = S_D + S_F + \text{odpisy} \implies I_{NET} = S_D + S_F$$

**Přidání veřejného sektoru:**
$$Y_D \equiv C + S_D = W + R + TR - TAD$$
$$\text{HDP} = C + I + G = W + R + N + \text{odpisy} + TAF$$
$$Y_D = \text{HDP} - N - \text{odpisy} - TAF - TAD + TR$$

Rozpočtový schodek:
$$BD = TR + G - TA$$

**Přidání zahraničí:**
$$\text{HDP} = C + I + G + NX = W + R + N + \text{odpisy} + TAF$$
$$I = S_D + S_F - BD + \text{odpisy} - NFI$$
$$NX + BI - NFI = 0 \quad \text{(platební bilance)}$$

kde $NX$ = čistý export, $BI$ = bilance výnosů (net factor income), $NFI$ = čistý zahraniční investiční tok.

## Input–Output analýza (W. Leontiev, NP 1973)

### Setup

Nechť $X_{ij}$ je dodávka sektoru $i$ do sektoru $j$, $Y_i$ finální výstup sektoru $i$, $X_i$ celková produkce sektoru $i$.

**Koeficienty přímé spotřeby** (považovány v čase za stabilní):
$$a_{ij} = \frac{X_{ij}}{X_j}$$

### Tři využití I-O analýzy

**1. Výpočet výroby z finálního výstupu:**
$$A \cdot X + Y = X \implies (I - A) \cdot X = Y$$

**2. Výpočet finálního výstupu z dané úrovně výroby:**
$$Y = (I - A) \cdot X$$

**3. Výpočet výroby nutné pro zajištění cílového finálního výstupu (Leontievova inverze):**
$$X = (I - A)^{-1} \cdot Y$$

$(I - A)^{-1}$ je **Leontievova inverzní matice** — zachycuje přímé i nepřímé efekty.

### Spojení s národním účetnictvím

| Metoda výpočtu HDP | Vzorec z I-O tabulky |
|---|---|
| **Výdajová** | $Y = \sum_i Y_i = C + I + G + NX$ |
| **Důchodová** | $Y = \sum_j (w_j + \pi_j + \text{depr}_j)$ |
| **Produkční** | $Y = \sum_i VA_i = \sum_i (X_i - \sum_j X_{ij})$ |

## HDP vs. příbuzné ukazatele

| Ukazatel | Vztah k HDP | Poznámka |
|---|---|---|
| **HDP** (GDP) | Základ | Produkce na území dané země |
| **HNP** (GNP) | $\text{HNP} = \text{HDP} + \text{NFI}$ | Zahrnuje příjmy rezidentů ze zahraničí |
| **NDP** (Net Domestic Product) | $\text{NDP} = \text{HDP} - \text{odpisy}$ | Po odečtení amortizace |
| **Disponibilní důchod** $Y_D$ | $Y_D = \text{HDP} - N - \text{odpisy} - TAF - TAD + TR + BI$ | Co zůstane domácnostem |
