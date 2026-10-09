---
course: "JEB027"
topic: "Finanční instrumenty — dluhopisy, akcie, deriváty, oceňování"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P03-2025_Financni_instrumenty_final.pdf"
tags: [JEB027, financni-instrumenty, dluhopisy, akcie, derivaty, opce, futures]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P03-2025_Financni_instrumenty_final.pdf]]
Related: [[Dluhopisy_a_Oceneni]], [[Akcie_a_Oceneni]], [[Financni_Trhy]], [[Urokova_Mira_a_Casova_Hodnota_Penez]]

# Finanční instrumenty

## Klasifikace finančních instrumentů

**Finanční instrument** je kontrakt, který zakládá finanční aktivum u jedné strany a finanční závazek nebo kapitálový instrument u druhé strany.

### Základní kategorie

| Kategorie | Příklady | Charakteristika |
|-----------|----------|-----------------|
| **Nástroje peněžního trhu** | Státní pokladniční poukázky (T-bills), komerční papíry (CP), depozitní certifikáty (CD) | Splatnost do 1 roku, nízké riziko, vysoká likvidita |
| **Dluhové instrumenty (fixed income)** | Státní dluhopisy, korporátní dluhopisy, hypoteční zástavní listy | Fixní nebo variabilní kuponové platby, různé splatnosti |
| **Kapitálové instrumenty (akcie)** | Kmenové akcie, preferenční akcie | Podíl na vlastnictví firmy, reziduální nárok |
| **Hybridní instrumenty** | Konvertibilní dluhopisy, podřízený dluh | Kombinace vlastností dluhopisu a akcie |
| **Deriváty** | Opce, futures, forwardy, swapy | Odvozená hodnota od podkladového aktiva |

## Dluhopisy

Viz detailní note: [[Dluhopisy_a_Oceneni]].

**Dluhopis (bond)** je dluhový instrument, kde emitent (dlužník) se zavazuje:
- Platit pravidelné **kuponové platby** $C$
- Splatit **jmenovitou hodnotu (face value)** $F$ při splatnosti za $n$ let

**Cena dluhopisu** je současná hodnota všech budoucích cash flows:

$$P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{F}{(1+r)^n} = C \cdot \frac{1-(1+r)^{-n}}{r} + \frac{F}{(1+r)^n}$$

kde $r$ je výnos do splatnosti (Yield to Maturity, YTM). Cena a výnos dluhopisu se pohybují **inverzně**.

### Typy dluhopisů

- **Státní dluhopisy:** nejnižší kreditní riziko v dané měně (sovereign bonds)
- **Korporátní dluhopisy (investment grade vs. high yield/junk bonds)**
- **Kuponové vs. bezkuponové (zero-coupon bonds)**
- **Inflačně vázané dluhopisy (TIPS — Treasury Inflation-Protected Securities)**

## Akcie

Viz detailní note: [[Akcie_a_Oceneni]].

**Akcie (equity)** reprezentuje podíl na vlastnictví akciové společnosti — akcionář má reziduální nárok na aktiva a zisky po uspokojení všech věřitelů.

**Dividendový diskontní model (DDM):** Cena akcie je současná hodnota budoucích dividend:

$$P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1+r_e)^t}$$

**Gordonův růstový model** (konstantní růst dividend $g$):

$$P_0 = \frac{D_1}{r_e - g}$$

kde $r_e$ je požadovaná výnosová míra z akcií a $D_1 = D_0 \cdot (1+g)$.

## Deriváty

**Derivát** je finanční instrument, jehož hodnota se odvozuje (derivuje) od hodnoty jiného, **podkladového aktiva** (underlying asset): akcie, dluhopis, úroková míra, měna, komodita, index.

### Opce (Options)

Opce dává držiteli **právo, nikoli povinnost** koupit (call opce) nebo prodat (put opce) podkladové aktivum za předem stanovenou **realizační cenu (strike price)** $K$ do nebo v datum expirace $T$.

**Prémium call opce** (Black-Scholes model):

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

kde:
- $S_0$ = aktuální cena podkladového aktiva
- $K$ = realizační cena
- $r$ = bezriziková úroková míra (spojitě složená)
- $\sigma$ = volatilita podkladového aktiva
- $T$ = čas do expirace (v letech)
- $N(\cdot)$ = kumulativní distribuční funkce normálního rozdělení [[Normal_Distribution]]

| Parametr | Vliv na cenu call | Vliv na cenu put |
|----------|-------------------|-----------------|
| $\uparrow S_0$ | $\uparrow$ | $\downarrow$ |
| $\uparrow K$ | $\downarrow$ | $\uparrow$ |
| $\uparrow \sigma$ | $\uparrow$ | $\uparrow$ |
| $\uparrow T$ | $\uparrow$ | $\uparrow$ |
| $\uparrow r$ | $\uparrow$ | $\downarrow$ |

**Put-call parita:**

$$C - P = S_0 - K e^{-rT}$$

### Futures a Forwardy

| | **Forward** | **Futures** |
|--|-------------|-------------|
| Obchodování | OTC | Burza |
| Standardizace | Nesitandardizovaný | Standardizovaný |
| Clearingové centrum | Ne | Ano |
| Denní zúčtování (mark-to-market) | Ne | Ano |
| Kreditní riziko | Ano (protistrany) | Minimální (clearing) |

**Cena futures (theoretical forward price):**

$$F_0 = S_0 \cdot e^{(r + u - y) \cdot T}$$

kde $u$ jsou náklady na skladování (storage cost) a $y$ je convenience yield.

### Swapy (Swaps)

**Swap** je dohoda o výměně cashflow mezi dvěma stranami po určité období.

- **Úrokový swap (IRS — Interest Rate Swap):** výměna fixní a variabilní úrokové platby na nominální hodnotu $N$:

$$\text{Cashflow (fixed payer)} = N \cdot (L_{t} - K) \cdot \delta$$

kde $L_t$ je variabilní sazba (PRIBOR, EURIBOR), $K$ fixní sazba, $\delta$ počet dní / 360 (day count fraction).

- **Měnový swap (Cross-Currency Swap):** výměna nominálů a úrokových plateb v různých měnách. Viz [[Mezinarodni_Finance_JEB027]].

## Rizika finančních instrumentů

| Typ rizika | Popis | Relevantní instrument |
|------------|-------|-----------------------|
| **Tržní riziko (market risk)** | Změna tržní ceny (úrok, akcie, měna) | Všechny instrumenty |
| **Kreditní riziko (credit risk)** | Selhání emitenta/protistrany | Dluhopisy, deriváty OTC |
| **Likviditní riziko** | Nemožnost prodat za tržní cenu | Méně likvidní instrumenty |
| **Operační riziko** | Chyby v procesech, systémech | Deriváty, viz [[Operacni_Riziko]] |
