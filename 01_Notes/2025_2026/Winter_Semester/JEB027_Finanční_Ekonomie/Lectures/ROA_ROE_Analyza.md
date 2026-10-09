---
course: "JEB027"
topic: "ROA, ROE a analýza výkonnosti banky — Dupont rozklad, equity multiplier"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_FINE_P04A-2025_Finanční_výkazy.pdf"
tags: [JEB027, ROA, ROE, dupont, equity-multiplier, bankova-vykonnost]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_FINE_P04A-2025_Finanční_výkazy.pdf]]
Related: [[Financni_Vykazy_Banky]], [[Komercni_Bankovnictvi]], [[Akcie_a_Oceneni]]

# ROA, ROE a analýza výkonnosti banky

## Základní ukazatele rentability

### ROA (Return on Assets)

**ROA** měří, jak efektivně banka využívá svá celková aktiva k generování zisku:

$$\boxed{ROA = \frac{\text{Čistý zisk po zdanění}}{\text{Průměrný stav aktiv}}}$$

- Typické hodnoty pro komerční banky: **0,5 % – 1,5 %**
- Nižší než u průmyslových firem, protože banky mají obrovské bilance (aktiva jsou multinásobky vlastního kapitálu)
- ROAA (Return on Average Assets) = varianta s průměrnými aktivy

### ROE (Return on Equity)

**ROE** měří výnosnost vlastního kapitálu akcionářů:

$$\boxed{ROE = \frac{\text{Čistý zisk po zdanění}}{\text{Průměrný stav vlastního kapitálu}}}$$

- Typické hodnoty: **8 % – 15 %** pro ziskové banky
- Česká bankovní scéna (Komerční banka, ČSOB, Česká spořitelna): ROE historicky 10–15 %
- Banky v eurozóně 2015–2022: ROE pod požadovanou mírou (cost of equity $r_e$), tedy $ROE < r_e$ → ničení hodnoty → $P/BV < 1$

## DuPont rozklad ROE

**DuPont analýza** rozloží ROE do komponent, čímž odhalí zdroje nebo příčiny změn výkonnosti:

$$ROE = ROA \times EM$$

kde $EM$ (Equity Multiplier) = finanční páka:

$$EM = \frac{\text{Průměrný stav aktiv}}{\text{Průměrný stav vlastního kapitálu}}$$

### Rozklad ROA

$$ROA = \text{Čistá zisková marže} \times \text{Obrat aktiv}$$

$$ROA = \frac{\text{Čistý zisk}}{\text{Výnosy}} \times \frac{\text{Výnosy}}{\text{Aktiva}}$$

### Úplný DuPont rozklad ROE

$$ROE = \underbrace{\frac{\text{Čistý zisk}}{\text{Výnosy}}}_{\text{Čistá marže}} \times \underbrace{\frac{\text{Výnosy}}{\text{Aktiva}}}_{\text{Obrat aktiv}} \times \underbrace{\frac{\text{Aktiva}}{\text{Vlastní kapitál}}}_{\text{Equity Multiplier (EM)}}$$

### Equity Multiplier (EM) — finanční páka

$$EM = \frac{\text{Aktiva}}{\text{Vlastní kapitál}} = \frac{1}{\text{Kapitálová přiměřenost}}$$

- Banky mají EM typicky **10–20x** (tj. přibližně 5–10 % kapitálová přiměřenost).
- Vysoký EM zveličuje ROE (pozitivní efekt při ROA > 0), ale zároveň zvyšuje finanční riziko (leverage risk).
- Regulace (Basel III, viz [[Bancni_Regulace_a_Basel]]) omezuje maximální EM prostřednictvím minimálních požadavků na kapitálovou přiměřenost.

## Trojúhelník vysoké ziskovosti českých bank

Přednáška identifikuje tři klíčové faktory nadprůměrné ziskovosti bank v ČR:

```
         Vysoké NIM
        (čistá úroková marže)
              ↑
      ←————————————→
Nízký C/I            Nízký NPL
(provozní efektivita) (kvalita portfolia)
```

1. **Vysoká NIM:** ČNB nastavuje vyšší nominální sazby → vyšší výnosové sazby z úvěrů vs. levná depozita (netermínované vklady domácností s blízkými nulou sazbami).
2. **Nízký C/I:** Česká bankovní scéna je oligopolní → nižší competitive pressure na náklady; banky investovaly do digitalizace.
3. **Nízký NPL:** Nízká nezaměstnanost, silná ekonomická výkonnost ČR (2015–2022) → nízké úvěrové ztráty.

## Studie: Bail-outy bank v Evropě

*(Gerhardt, M., Vander V. R., 2017. Bank Bailouts in Europe and Bank Performance. Finance Research Letters 22: 74–80)*

Klíčová zjištění (logitová regrese na vzorku 114 evropských bank zachráněných v 2007–2009):
- Hlavní determinanty státní intervence (bail-out):
  - **EM (finanční páka):** vyšší páka = vyšší pravděpodobnost bail-outu
  - **Loan Loss Provisions / Loans (NPL):** vyšší NPL = vyšší pravděpodobnost bail-outu
  - **Systemic size (aktiva/HDP):** větší banky = vyšší pravděpodobnost bail-outu (too big to fail)
- Podpořené banky **nezlepšily výkonnost** v post-intervenci období → státní podpora sama o sobě nestačí k ozdravení banky.

## Způsoby záchrany banky v problémech

Z přednášky — čtyři mechanismy:

| Mechanismus | Popis |
|-------------|-------|
| **1. Rekapitalizace (bail-out)** | Stát vstupuje jako akcionář, vkládá kapitál |
| **2. Garance za závazky** | Stát zaručuje splácení závazků banky (depozita, dluhopisy) |
| **3. Odkup aktiv** | Stát nebo speciální vehicle odkoupí toxická/nevýkonná aktiva |
| **4. Dodání likvidity** | Centrální banka poskytne nouzovou likviditní podporu (Emergency Liquidity Assistance — ELA) |

Viz [[Centralni_Bankovnictvi]] pro roli CB jako věřitele poslední instance (lender of last resort).
