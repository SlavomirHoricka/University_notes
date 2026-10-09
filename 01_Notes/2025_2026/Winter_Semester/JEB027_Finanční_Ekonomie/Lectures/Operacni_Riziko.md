---
course: "JEB027"
topic: "Operační riziko — definice, Basel přístupy, kategorie ztrát, řízení"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P07B-2025_Operační_riziko_M.Němec.pdf"
tags: [JEB027, operacni-riziko, Basel, RCSA, OpRisk, ztratove-udalosti]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P07B-2025_Operační_riziko_M.Němec.pdf]]
Related: [[Bancni_Regulace_a_Basel]], [[Komercni_Bankovnictvi]], [[ESG_Finance]]

# Operační riziko

## Definice

**Operační riziko** (*Operational Risk*, OpRisk) je dle Basel II/III definováno jako:

> Riziko ztráty vyplývající z nedostatečných nebo selhávajících interních procesů, lidí a systémů nebo z externích událostí. Tato definice zahrnuje i **právní riziko**, ale vylučuje strategické a reputační riziko.

Přednáška (M. Němec) zdůrazňuje, že operační riziko je **třetím pilířem bankovní regulace** vedle kreditního a tržního rizika.

## Kategorie ztrátových událostí (Basel Loss Event Types)

Basel definuje 7 kategorií operačních ztrát:

| Kategorie | Zkratka | Příklady |
|-----------|---------|---------|
| Interní podvody | IF | Neoprávněný přístup, zpronevěra zaměstnanců |
| Externí podvody | EF | Phishing, hacky, falešné faktury |
| Pracovní podmínky a pracovní právo | EPWS | Diskriminace, BOZP, zaměstnanecké žaloby |
| Klienti, produkty a obchodní postupy | CPBP | Misselling, únik dat klientů, manipulace trhu |
| Poškození hmotného majetku | DAMA | Živelné katastrofy, vandalismus |
| Přerušení podnikání a systémové selhání | BDSF | Výpadky IT, kybernetické útoky |
| Provádění, dodávka a řízení procesů | EDPM | Settlement chyby, chyby v datech, outsourcing selhání |

## Basel přístupy pro výpočet kapitálové požadavku

### Základní indikátorový přístup (BIA — Basic Indicator Approach)

$$K_{BIA} = \frac{\sum_{i=1}^{3} \max(GI_i, 0)}{n} \times \alpha$$

kde $GI_i$ = hrubý příjem (gross income) v roce $i$, $n$ = počet let s kladným $GI$, $\alpha = 15\%$.

### Standardizovaný přístup (SA)

Hrubý příjem banky je rozdělen do 8 business lines, každá s vlastním beta faktorem ($\beta$):

| Business Line | $\beta$ |
|---------------|---------|
| Corporate Finance | 18 % |
| Trading & Sales | 18 % |
| Retail Banking | 12 % |
| Commercial Banking | 15 % |
| Payment & Settlement | 18 % |
| Agency Services | 15 % |
| Asset Management | 12 % |
| Retail Brokerage | 12 % |

$$K_{SA} = \sum_{i=1}^{8} GI_i \times \beta_i$$

### Pokročilé přístupy (AMA — Advanced Measurement Approaches)

Banky s regulatorním souhlasem mohou používat vlastní interní modely (Loss Distribution Approach, Scenario Analysis, etc.). Basel IV (2023+): AMA bylo zrušeno — nový Standardised Approach (SA) je povinný pro všechny banky.

## Basel IV — nový Standardisovaný Přístup (2023+)

Basel IV nahradil AMA jednotným **Business Indicator Component (BIČ) přístupem**:

$$K_{OpRisk} = BIC \times ILM$$

kde: 
- **BIC (Business Indicator Component):** funkce Business Indicator (BI) = sum of tří složek (ILDC + SC + FC) v pásmech
- **ILM (Internal Loss Multiplier):** funkce historických ztrát banky

## Nástroje řízení operačního rizika

### RCSA (Risk and Control Self-Assessment)

Systematická identifikace a hodnocení operačních rizik ve všech procesech banky:
1. Identifikace rizik (risk identification)
2. Hodnocení inherentního rizika (inherent risk)
3. Hodnocení kontrol (control effectiveness)
4. Residuální riziko (residual risk = inherent − control)

### KRI (Key Risk Indicators)

Klíčové ukazatele rizika — varovné signály (leading indicators) budoucích ztrát:
- Počet neuspokojených reklamací
- % chybných transakcí
- Dostupnost IT systémů (uptime)
- Počet bezpečnostních incidentů

### Ztratová databáze (Loss Event Database)

Historické záznamy o ztrátách sloužící pro:
- Výpočet kapitálového požadavku (historické ztráty)
- Identifikaci systémových problémů
- Regulatorní reporting
- Srovnání s externími daty (ORX consortium)

## Klíčová rizika v současném prostředí

| Riziko | Trend | Příklad |
|--------|-------|---------|
| **Kybernetické riziko** | Stoupající | Ransomware, DDoS, phishing na banky |
| **Riziko třetích stran (outsourcing)** | Vysoké | Cloud providers (AWS, Azure) jako single point of failure |
| **Riziko AI/ML modelů** | Nové | Model risk — bias, chyby v credit scoring AI |
| **Geopolitické riziko** | Stoupající | Sankce, válečné konflikty narušující operace |
| **ESG operační riziko** | Rostoucí | Viz [[ESG_Finance]] — fyzická rizika klimatu, regulatorní sankce |
| **DeFi/krypto operační riziko** | Nové | Smart contract bugs — viz [[Blockchain_a_Smart_Kontrakty]] |

## Třetí pilíř — Tržní disciplína

Banky jsou povinny zveřejňovat:
- Přístupy pro měření operačního rizika
- Výši kapitálových požadavků
- Historii ztrátových událostí (nad prahem)
- Strukturu řízení operačního rizika

Viz [[Bancni_Regulace_a_Basel]] pro celkové propojení s Basel framework.
