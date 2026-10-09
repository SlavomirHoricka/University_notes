---
course: "JEB027"
topic: "Bankovní regulace a Basel Framework — kapitálová přiměřenost, Basel I/II/III, LCR, NSFR"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P05-2025_Komerční_bankovnictvi.pdf"
tags: [JEB027, Basel, bankovni-regulace, kapitalova-primerenost, LCR, NSFR, Tier1]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P05-2025_Komerční_bankovnictvi.pdf]]
Related: [[Komercni_Bankovnictvi]], [[Financni_Vykazy_Banky]], [[ROA_ROE_Analyza]], [[Centralni_Bankovnictvi]], [[Operacni_Riziko]]

# Bankovní regulace a Basel Framework

## Rationale pro regulaci bank

Banky jsou **systémově důležité** instituce — selhání jedné banky může prostřednictvím **contagion efektu** vyvolat řetězovou reakci (finanční krize). Regulace adresuje:

1. **Informační asymetrie:** Vkladatelé nemají dostatek informací o rizikovosti banky (morální hazard).
2. **Systémové riziko:** Propojení bank přes mezibankovní trh → too big to fail (TBTF) problém.
3. **Ochrana vkladatelů:** Stabilita platebního styku a důvěra veřejnosti v bankovní systém.

## Basel Accord — historický vývoj

### Basel I (1988)

Zavedl **minimální kapitálovou přiměřenost**:

$$CAR = \frac{\text{Regulatorní kapitál}}{\text{Rizikově vážená aktiva (RWA)}} \geq 8\%$$

Omezení: Hrubá klasifikace rizikových vah (aktiva rozdělena pouze do 5 kategorií); nerespektuje operační riziko ani tržní riziko.

### Basel II (2004)

**Tři pilíře:**

| Pilíř | Název | Obsah |
|-------|-------|-------|
| **Pilíř 1** | Minimální kapitálové požadavky | Kreditní, tržní a operační riziko |
| **Pilíř 2** | Dohledová kontrola (SREP) | Individuální posouzení rizikovosti banky regulátorem |
| **Pilíř 3** | Tržní disciplína | Povinné zveřejňování informací (disclosure) |

Přístupy pro výpočet RWA:
- **Standardizovaný přístup (SA):** Použití externích ratingů
- **IRB přístup (Internal Ratings-Based):** Použití interních modelů banky (Foundation IRB a Advanced IRB)

### Basel III (2010/2013, plné zavedení 2023+)

Odpověď na globální finanční krizi 2007–2009:

#### Kapitál (kvalita i kvantita)

Struktura regulatorního kapitálu:

| Složka | Obsah | Min. požadavek |
|--------|-------|---------------|
| **CET1 (Common Equity Tier 1)** | Kmenové akcie + nerozdělený zisk | ≥ 4,5 % RWA |
| **Tier 1** | CET1 + AT1 (Additional Tier 1 — hybridní nástroje) | ≥ 6 % RWA |
| **Tier 2** | Podřízený dluh s min. splatností 5 let | ≥ 8 % RWA (celkový CAR) |
| **Capital Conservation Buffer** | Extra CET1 jako „polštář" | 2,5 % RWA |
| **Countercyclical Capital Buffer (CCyB)** | Proticyklický polštář (0–2,5 %) — aktivuje ČNB | Variabilní |
| **GSIB Surcharge** | Příplatek pro globálně systémově důležité banky | 1–3,5 % RWA |

#### Pákový poměr (Leverage Ratio)

Nezávislý na rizikových vahách — doplnění k RWA:

$$\text{Leverage Ratio} = \frac{\text{Tier 1 kapitál}}{\text{Celková expozice (bilanční + mimobilanční)}} \geq 3\%$$

#### Likviditní požadavky

**LCR (Liquidity Coverage Ratio):** Zajistit krátkodobou likviditu (30denní stresový horizont):

$$LCR = \frac{\text{Vysoce likvidní aktiva (HQLA)}}{\text{Čistý odliv hotovosti za 30 dní}} \geq 100\%$$

**NSFR (Net Stable Funding Ratio):** Strukturální (dlouhodobá) likvidita:

$$NSFR = \frac{\text{Dostupné stabilní financování (ASF)}}{\text{Požadované stabilní financování (RSF)}} \geq 100\%$$

## Regulatorní rámec EU

- **CRD IV/V** (Capital Requirements Directive): transponuje Basel III do práva EU
- **CRR** (Capital Requirements Regulation): přímo aplikovatelné nařízení
- **BRRD** (Bank Recovery and Resolution Directive): řeší resolution — **bail-in** nástroj (věřitelé nesou ztráty namísto daňových poplatníků)
- **SSM** (Single Supervisory Mechanism): ECB přímo dohlíží nad „significantními institucemi" v eurozóně (aktiva > 30 mld. EUR)
- **SRM** (Single Resolution Mechanism): Jednotný výbor pro řešení krizí (SRB)

### Bail-in vs. Bail-out

| | **Bail-out** | **Bail-in** |
|--|-------------|-------------|
| Kdo nese ztráty | Daňoví poplatníci | Věřitelé banky (v hierarchii: subordinovaný dluh → senior dluh → depozita nad 100K EUR) |
| Regulatorní postoj | Zamítavý (morální hazard) | Preferovaný od BRRD 2014/2019 |

## Pojištění vkladů

**Fond pojistenia vkladů (FPV) / Deposit Guarantee Scheme (DGS):**

- Chrání vklady do **100 000 EUR** na osobu na banku
- EU Direktiva 2014/49/EU
- Zvyšuje důvěru vkladatelů → snižuje riziko bank runu

Viz [[Centralni_Bankovnictvi]] pro roli ČNB jako lender of last resort.
