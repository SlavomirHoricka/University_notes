---
course: "JEB027"
topic: "Pojišťovny a pojistný trh — principy pojištění, Solvency II, druhy pojištění"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P09-2025_Pojišťovny.pdf"
tags: [JEB027, pojistovnictvi, Solvency-II, pojistny-trh, riziko, zakon-velkych-cisel]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P09-2025_Pojišťovny.pdf]]
Related: [[Financni_Trhy]], [[ESG_Finance]], [[Bancni_Regulace_a_Basel]], [[Operacni_Riziko]]

# Pojišťovny a pojistný trh

## Základní principy pojištění

**Pojištění** je mechanismus pro přenos finanční nejistoty z jednotlivce (nebo firmy) na pojišťovnu za úhradu **pojistného (prémia)**. Pojišťovna sdílediverzifikovatelné riziko napříč velkým počtem pojistníků.

### Klíčové principy

1. **Zákon velkých čísel (Law of Large Numbers):** S rostoucím počtem pojistníků se průměrná pojistná ztráta blíží očekávané hodnotě — variance klesá:

$$\bar{X}_n \xrightarrow{p} \mu \quad \text{kde } \mu = E[X_i]$$

Pojišťovna tak může **předvídat** celkové pojistné plnění s přijatelnou přesností.

2. **Sdílení rizika (Risk Pooling):** Pojistníci vkládají malé jisté platby (prémia) a výměnou získávají pokrytí velkých nejistých ztrát.

3. **Pojistná událost** musí být: náhodná, měřitelná, uzákonitelná, neplyne z úmyslného jednání pojistníka.

4. **Morální hazard (Moral Hazard):** Po pojištění má pojistník nižší motivaci předcházet pojistné události (ex-post morální hazard). Řeší se: spoluúčasta (deductible), limity plnění.

5. **Negativní selekce (Adverse Selection):** Pojistníci s vyšším rizikem mají větší tendenci uzavírat pojistky. Řeší se: aktuárská diferenciace prémií, povinné pojištění, underwriting.

## Druhy pojištění

### Životní pojištění (Life Insurance)

| Produkt | Popis |
|---------|-------|
| **Rizikové životní pojištění** | Plnění při smrti pojistníka v době trvání pojistky |
| **Kapitálové životní pojištění** | Spoření s pojistnou složkou; plnění při dožití nebo smrti |
| **Důchodové pojištění** | Pravidelná renta poplatníkovi od určitého věku |
| **Investiční životní pojištění** | Unit-linked — spoření vázané na podílové fondy |

Klíčový parametr ocenění: **aktuárská hodnota** = $E[\text{PV budoucích plnění}]$ minus $E[\text{PV budoucích prémií}]$.

### Neživotní pojištění (Non-Life / P&C Insurance)

| Kategorie | Příklady |
|-----------|---------|
| **Majetkové** | Pojištění nemovitostí, vozidel (KASKO) |
| **Odpovědnostní** | Pojištění odpovědnosti za škodu, D&O (Directors & Officers) |
| **Zdravotní a úrazové** | Soukromé zdravotní pojištění |
| **Pojištění pohledávek** | Kreditní pojištění — viz interakce s [[Dluhopisy_a_Oceneni]] |
| **Pojištění přepravy / cargo** | Námořní, letecké, pozemní přepravy |
| **Kyber pojištění** | Krytí kybernetických incidentů — viz [[Operacni_Riziko]] |

### Zajištění (Reinsurance)

Pojišťovny přenášejí část svého rizika na **zajišťovny** (Munich Re, Swiss Re, Hannover Re). Mechanismy:
- **Proporcionální zajištění (Quota Share, Surplus):** dělba prémií a plnění v pevném poměru
- **Neproporcionální zajištění (Excess of Loss, Stop Loss):** zajišťovna plní až při překročení retence

## Struktura billance pojišťovny

### Aktiva

| Položka | Popis |
|---------|-------|
| Investiční portfolio | Dluhopisy, akcie, nemovitosti — krytí technických rezerv |
| Pohledávky z pojistného | Nezaplacené pojistné |
| Ostatní aktiva | Ostatní majetek |

### Pasiva a vlastní kapitál

| Položka | Popis |
|---------|-------|
| **Technické rezervy** | Klíčová pasivní položka — budoucí pojistná plnění (Claim reserves + Unearned premium) |
| Závazky | Závazky z pojistného plnění, daně |
| **Vlastní kapitál (Solvency Capital)** | Buffer pro neočekávané ztráty |

## Solvency II — Regulace pojišťoven v EU

**Solvency II** (platné od 2016) je regulatorní rámec EU pro pojišťovny — analogie Basel III pro banky.

### Tři pilíře Solvency II

| Pilíř | Obsah |
|-------|-------|
| **Pilíř 1** | Kvantitativní požadavky — SCR (Solvency Capital Requirement), MCR (Minimum Capital Requirement) |
| **Pilíř 2** | Governance a risk management — ORSA (Own Risk and Solvency Assessment) |
| **Pilíř 3** | Transparentnost — SFCR (Solvency and Financial Condition Report) |

### SCR (Solvency Capital Requirement)

Kapitál, který pojišťovna musí udržovat jako polštář (99,5 % Value-at-Risk v jednoročním horizontu):

$$SCR = VaR_{99.5\%}(\Delta \text{NAV}_{1Y})$$

Móduly SCR: tržní riziko, kreditní riziko, underwriting riziko (životní, neživotní), operační riziko.

## Pojistno-technické ukazatele (Non-Life)

### Combined Ratio

$$\text{Combined Ratio} = \frac{\text{Pojistná plnění + Provozní náklady}}{\text{Zaslané pojistné}} = \text{Loss Ratio} + \text{Expense Ratio}$$

- **Combined Ratio < 100 %:** Underwriting profit (zisk z pojišťovací činnosti)
- **Combined Ratio > 100 %:** Underwriting loss — pojišťovna musí vydělat na investicích

### Loss Ratio

$$\text{Loss Ratio} = \frac{\text{Pojistná plnění (incurred losses)}}{\text{Zaslané pojistné (earned premium)}}$$

## Klimatické riziko v pojišťovnictví

Pojišťovny jsou přímou první linii klimatického rizika:
- Nárůst pojistných plnění z přírodních katastrof (záplavy, bouře, sucha)
- Riziko **uninsurability** — v některých oblastech se pojištění klimatických rizik stává nepojistitelným (např. záplavy v níže položených oblastech)
- Zpětná vazba: pokud pojišťovny přestanou krýt určitá rizika → ztráta hodnoty nemovitostí → finanční riziko bank

Viz [[ESG_Finance]] pro regulatorní rámec TCFD a klimatického stresstesting.
