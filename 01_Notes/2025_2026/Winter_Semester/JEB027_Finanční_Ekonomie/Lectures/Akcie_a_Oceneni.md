---
course: "JEB027"
topic: "Akcie a jejich oceňování — DDM, DCF, P/E, P/BV, CAPM"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P03-2025_Financni_instrumenty_final.pdf"
tags: [JEB027, akcie, DDM, DCF, CAPM, PE-ratio, oceneni-akcii]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P03-2025_Financni_instrumenty_final.pdf]]
Related: [[Financni_Instrumenty]], [[Financni_Trhy]], [[Hypoteza_Efektivnich_Trhu]], [[Financni_Vykazy_Banky]], [[ROA_ROE_Analyza]]

# Akcie a jejich oceňování

## Základní charakteristiky akcií

**Akcie (share / equity)** je cenný papír reprezentující podíl na vlastnictví akciové společnosti. Akcionáři jsou rezidualními věřiteli — mají nárok na majetek a zisk firmy **až po uspokojení všech věřitelů** (dluhopisáři, banky).

### Práva akcionáře

- **Hlasovací právo** (voting right) — podíl na rozhodování na valné hromadě
- **Právo na dividendu** — podíl na zisku po rozhodnutí představenstva
- **Přednostní právo na upisování nových akcií** (pre-emption right)
- **Právo na likvidační zůstatek** — reziduální nárok při zániku společnosti

### Druhy akcií

| Druh | Popis |
|------|-------|
| **Kmenová akcie (ordinary share)** | Hlasovací právo, variabilní dividenda |
| **Preferenční akcie (preferred share)** | Fixní (prioritní) dividenda, obvykle bez hlasovacích práv |
| **Akcie s rozdílnými hlasovacími právy (dual class shares)** | Např. Google (Alphabet) — třída A a třída C bez hlasovacích práv |

## Dividendový diskontní model (DDM)

**Základní princip:** Cena akcie je současná hodnota všech budoucích dividend:

$$P_0 = \sum_{t=1}^{\infty} \frac{D_t}{(1 + r_e)^t}$$

kde $r_e$ je požadovaná výnosová míra z akcií (cost of equity).

### Gordonův růstový model (Gordon Growth Model)

Předpoklad: dividendy rostou konstantní mírou $g$ navždy:

$$\boxed{P_0 = \frac{D_1}{r_e - g} = \frac{D_0 \cdot (1+g)}{r_e - g}}$$

**Podmínka konvergence:** $r_e > g$

**Intuice parametrů:**
- $\uparrow D_1$: vyšší příští dividenda → vyšší cena
- $\uparrow g$: vyšší trvalý růst → vyšší cena
- $\uparrow r_e$: vyšší požadovaný výnos (vyšší riziko) → nižší cena

**Výnosový pohled:** z DDM lze odvodit implicitní $r_e$:

$$r_e = \frac{D_1}{P_0} + g = \text{Dividendový výnos} + \text{Kapitálový zisk}$$

## Oceňování diskontováním cashflow (DCF)

V praxi se pro oceňování akcií (a firem) více používá metoda **Free Cash Flow to Firm (FCFF):**

$$\text{EV} = \sum_{t=1}^{n} \frac{FCFF_t}{(1+WACC)^t} + \frac{TV_n}{(1+WACC)^n}$$

kde:
- $\text{EV}$ = Enterprise Value (celková tržní hodnota firmy)
- $FCFF_t$ = volný peněžní tok pro věřitele i vlastníky v čase $t$
- $WACC$ = vážené průměrné náklady kapitálu (*Weighted Average Cost of Capital*)
- $TV_n$ = terminální hodnota (terminal value) — $TV_n = \frac{FCFF_{n+1}}{WACC - g}$

**Cena akcie** z DCF:

$$P_0 = \frac{\text{EV} - \text{Čistý dluh (Net Debt)}}{\text{Počet akcií}}$$

### WACC

$$WACC = \frac{E}{V} \cdot r_e + \frac{D}{V} \cdot r_d \cdot (1-\tau)$$

kde $E$ = tržní hodnota vlastního kapitálu, $D$ = tržní hodnota dluhu, $V = E + D$, $r_d$ = náklady dluhu, $\tau$ = sazba daně z příjmů.

## CAPM (Capital Asset Pricing Model)

**CAPM** (Sharpe, 1964; Lintner, 1965) určuje požadovanou výnosnost akcií jako funkci systematického rizika:

$$r_e = r_f + \beta \cdot (r_m - r_f)$$

kde:
- $r_f$ = bezriziková sazba (výnos státního dluhopisu)
- $r_m$ = očekávaný výnos tržního portfolia
- $(r_m - r_f)$ = tržní riziková prémie (equity risk premium, ERP)
- $\beta$ = systematické riziko akcie (koeficient citlivosti na tržní pohyby)

$$\beta = \frac{\text{Cov}(r_i, r_m)}{\text{Var}(r_m)} = \frac{\sigma_{im}}{\sigma_m^2}$$

| $\beta$ | Interpretace |
|---------|-------------|
| $\beta > 1$ | Cyklická akcie (tech, finance); pohybuje se více než trh |
| $\beta = 1$ | Pohybuje se shodně s trhem |
| $0 < \beta < 1$ | Defenzivní akcie (utilities, potraviny) |
| $\beta < 0$ | Negativní korelace s trhem (vzácné; např. zlato) |

## Relativní oceňování — tržní násobky (Multiples)

### P/E (Price-to-Earnings)

$$P/E = \frac{P_0}{EPS}$$

kde $EPS$ = zisk na akcii (Earnings Per Share). Vyjadřuje, kolik investor platí za jednotku zisku.

Nízké P/E = potenciálně podhodnocená akcie (value stock) nebo pesimistická makro situace; vysoké P/E = growth stock nebo nadhodnocení.

### P/BV (Price-to-Book Value)

$$P/BV = \frac{P_0}{\text{Účetní hodnota vlastního kapitálu na akcii}}$$

Viz [[ROA_ROE_Analyza]] pro diskusi $P/BV < 1$ u evropských bank (implikace pro ziskovost).

### EV/EBITDA

$$EV/EBITDA = \frac{\text{Enterprise Value}}{EBITDA}$$

Populární pro mezifiremní srovnání (eliminuje vliv kapitálové struktury a daní).

## IPO (Initial Public Offering)

**IPO** je prvotní veřejná nabídka akcií, při níž soukromá firma vstupuje na burzovní trh. Probíhá na **primárním trhu** (viz [[Financni_Trhy]]) prostřednictvím investičních bank jako underwriters.

**Underpricing phenomenon:** Empiricky IPO akcie v prvním dni obchodování průměrně vzrostou nad emisní cenu (~15 % v USA) — anomálie vysvětlovaná informační asymetrií (winner's curse).
