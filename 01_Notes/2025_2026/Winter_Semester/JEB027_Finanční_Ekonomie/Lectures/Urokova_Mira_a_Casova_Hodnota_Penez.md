---
course: "JEB027"
topic: "Úroková míra a časová hodnota peněz — nominální vs. reálná sazba, výnosová křivka"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P01B-2025_ZS_Penize_a_urokova_mira_final.pdf"
tags: [JEB027, urokova-mira, casova-hodnota-penez, Fisher-rovnice, vynosova-krivka]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P01B-2025_ZS_Penize_a_urokova_mira_final.pdf]]
Related: [[Penize_a_jejich_Funkce]], [[Dluhopisy_a_Oceneni]], [[Centralni_Bankovnictvi]], [[Financni_Trhy]]

# Úroková míra a časová hodnota peněz

## Časová hodnota peněz

Klíčový princip finanční ekonomie: **peněžní jednotka dnes má vyšší hodnotu než tatáž jednotka v budoucnosti**, a to ze tří důvodů:

1. **Inflace** — kupní síla peněz v čase klesá.
2. **Příležitostné náklady** — peníze lze dnes investovat a vydělat výnos.
3. **Riziko** — budoucí platby jsou nejisté.

### Současná hodnota (Present Value)

Současná hodnota budoucí peněžní částky $FV$ splatné za $n$ let při diskontní sazbě $r$:

$$PV = \frac{FV}{(1+r)^n}$$

Pro **anuitu** (pravidelné platby $C$ po $n$ let):

$$PV_{\text{anuita}} = C \cdot \frac{1 - (1+r)^{-n}}{r}$$

Pro **věčnou rentu (perpetuitu)** — platby $C$ navždy:

$$PV_{\text{perpetuita}} = \frac{C}{r}$$

### Budoucí hodnota (Future Value)

$$FV = PV \cdot (1+r)^n$$

**Složené úročení** (compounding): úroky se v každém období přičítají k jistině a v dalším období se samy úročí. Při $m$ úrokových obdobích za rok:

$$FV = PV \cdot \left(1 + \frac{r}{m}\right)^{m \cdot n}$$

**Spojité úročení** (limiting case $m \to \infty$):

$$FV = PV \cdot e^{r \cdot n}$$

## Nominální vs. reálná úroková míra

### Fisherova rovnice

Vztah mezi nominální úrokovou mírou $i$, reálnou úrokovou mírou $r$ a inflací $\pi$:

$$1 + i = (1 + r)(1 + \pi)$$

**Přibližná verze** (platí pro malé hodnoty):

$$i \approx r + \pi$$

- **Nominální úroková míra** $i$: pozorovaná tržní sazba (např. sazba ČNB nebo bankovního depozita).
- **Reálná úroková míra** $r$: nominální sazba očištěná o inflaci; vyjadřuje skutečnou výnosnost z hlediska kupní síly.
- **Inflace** $\pi$: míra růstu cenové hladiny (CPI, PPI).

### Exante vs. expost reálná sazba

- **Exante reálná sazba:** počítaná s očekávanou inflací $\pi^e$: $r^e = i - \pi^e$
- **Expost reálná sazba:** počítaná se skutečnou inflací: $r = i - \pi$

## Výnosová křivka (Yield Curve)

**Výnosová křivka** zobrazuje vztah mezi výnosem do splatnosti (YTM) a dobou splatnosti dluhových instrumentů stejného emitenta (typicky státního). Je klíčovým nástrojem finanční analýzy.

### Tvary výnosové křivky

| Tvar | Popis | Ekonomická interpretace |
|------|-------|------------------------|
| **Normální (rostoucí)** | Dlouhé sazby > krátké sazby | Ekonomika roste, trh očekává vyšší inflaci v budoucnu |
| **Inverzní (klesající)** | Krátké sazby > dlouhé sazby | Trh anticipuje recesi; CB zpřísňuje politiku |
| **Plochá** | Krátké ≈ dlouhé sazby | Přechodové období; nejistota |
| **Hrbolatá (humped)** | Maximum ve středním splatnosti | Méně časté, viz Liquidity Premium Theory |

### Teorie výnosové křivky

1. **Teorie očekávání (Pure Expectations Theory):** Dlouhé sazby jsou geometrickým průměrem očekávaných budoucích krátkých sazeb:

$$\left(1 + {}_{0}i_n\right)^n = \left(1 + {}_{0}i_1\right)\left(1 + {}_{1}i_1^e\right)\cdots\left(1 + {}_{n-1}i_1^e\right)$$

2. **Teorie likviditní prémie (Liquidity Premium Theory):** Investoři požadují prémii za delší splatnost (likviditní/termínová prémie $l_t > 0$):

$${}_{0}i_n = \frac{{}_{0}i_1 + {}_{1}i_1^e + \cdots + {}_{n-1}i_1^e}{n} + l_n$$

3. **Teorie segmentovaných trhů (Market Segmentation Theory):** Různé segmenty trhu (krátkodobý, dlouhodobý) jsou od sebe odděleny a ceny se tvoří nezávisle dle lokální nabídky a poptávky.

## Druhy úrokových sazeb v praxi

| Sazba | Popis |
|-------|-------|
| **2T Repo sazba ČNB** | Klíčová sazba ČNB pro 2týdenní repo operace; kotva krátkodobých sazeb |
| **PRIBOR** | Prague Interbank Offered Rate; referenční sazba mezibankovního trhu v ČR |
| **EURIBOR** | Euro Interbank Offered Rate; eurozóna |
| **LIBOR (historicky)** | London Interbank Offered Rate; globální benchmark (nahrazen SOFR, SONIA atd.) |
| **OIS (Overnight Index Swap)** | Swapová sazba navázaná na referenční overnight sazbu |

Viz [[Centralni_Bankovnictvi]] pro roli ČNB při řízení krátkodobých sazeb a [[Dluhopisy_a_Oceneni]] pro aplikaci výnosové křivky při oceňování dluhopisů.
