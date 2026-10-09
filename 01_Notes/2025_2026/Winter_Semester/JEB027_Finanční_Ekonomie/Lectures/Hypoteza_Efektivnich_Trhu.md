---
course: "JEB027"
topic: "Hypotéza efektivních trhů — formy efektivity, anomálie, behaviorální finance"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P02-2025_Financni_trhy.pdf"
tags: [JEB027, EMH, efektivni-trhy, behavioralni-finance, Fama, anomalie]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P02-2025_Financni_trhy.pdf]]
Related: [[Financni_Trhy]], [[Akcie_a_Oceneni]], [[Kryptoaktiva]]

# Hypotéza efektivních trhů (EMH)

## Definice a historický kontext

**Hypotéza efektivních trhů** (Efficient Market Hypothesis, EMH) byla formulována Eugenem Famou v seminárním článku *"Efficient Capital Markets: A Review of Theory and Empirical Evidence"* (1970). Fama obdržel za příspěvek k EMH Nobelovu cenu za ekonomii v roce 2013.

**Definice:** Trh je efektivní v informačním smyslu, pokud ceny finančních aktiv plně, okamžitě a správně odrážejí veškeré relevantní dostupné informace.

$$P_t = E\left[P_{t+1} \mid \Omega_t\right] \cdot \frac{1}{1+r}$$

kde $\Omega_t$ je informační množina dostupná v čase $t$ a $r$ je požadovaná výnosová míra.

Implikace: Abnormální výnosy (výnosy nad risk-adjusted benchmark) **nelze konzistentně dosahovat** za použití informací obsažených v $\Omega_t$.

## Tři formy efektivity

### Slabá forma (Weak Form EMH)

**Informační množina:** Historické ceny a objemy obchodů.

$$\Omega_t^{\text{weak}} = \{P_{t-1}, P_{t-2}, \ldots, V_{t-1}, V_{t-2}, \ldots\}$$

**Implikace:**
- Vývoj cen sleduje **náhodný průchod** (*random walk*): $P_t = P_{t-1} + \varepsilon_t$, kde $E[\varepsilon_t] = 0$.
- **Technická analýza** (analýza grafů, klouzavé průměry, oscilátory) nemůže konzistentně přinášet abnormální výnosy.

**Empirické testy:** Testy sériové korelace výnosů, filtrační pravidla.

### Polosilná forma (Semi-Strong Form EMH)

**Informační množina:** Všechny veřejně dostupné informace (ceny, výroční zprávy, makrodata, rating, atd.).

**Implikace:**
- **Fundamentální analýza** (ocenění firem na základě finančních výkazů, diskontování cash flows) neposkytuje trvalou výhodu.
- Ceny se okamžitě a správně přizpůsobí novým veřejným informacím.

**Empirické testy:** Event studies — zkoumání abnormálních výnosů kolem oznámení (earnings announcements, M&A, změna dividendy).

### Silná forma (Strong Form EMH)

**Informační množina:** Veškeré informace, veřejné i neveřejné (insider information).

**Implikace:**
- Ani insideři (manažeři, členové představenstva) nemohou konzistentně dosahovat abnormálních výnosů.
- Tato forma je empiricky nejproblemičtější — **insider trading** empiricky přináší vyšší výnosy (přijetí silné formy EMH je obecně odmítáno).

## Anomálie trhu

Četné empirické studie identifikovaly odchylky od EMH:

### Anomálie kalibru a hodnoty

| Anomálie | Popis |
|----------|-------|
| **Size effect (efekt velikosti)** | Akcie malých firem (small-cap) dlouhodobě překonávají velké firmy risk-adjusted |
| **Value premium** | Akcie s nízkým P/B (value stocks) překonávají akcie s vysokým P/B (growth stocks) |
| **Momentum effect** | Akcie s nedávno vysokými výnosy tendují k dalšímu růstu (Jegadeesh & Titman, 1993) |

### Sezónní anomálie

| Anomálie | Popis |
|----------|-------|
| **January effect** | Akcie malých firem mají tendenci růst v lednu (kaňon prodejů na konci roku) |
| **Monday effect** | Výnosy v pondělí jsou systematicky nižší než v ostatní dny |

### Příklady z přednášky

**TrumpCoin:** Kryptoaktivum, jehož cena v lednu 2025 prudce vzrostla na základě politických událostí a poklesla poté, co se spekulace nenaplnily. Cena reagovala na veřejné informace (tweetový sentiment) — konzistentní s polosilnou formou EMH (trh reaguje na nové info), ale nadměrná volatilita naznačuje i přítomnost behaviorálních jevů.

## Behaviorální finance

Behaviorální finance (Kahneman & Tversky, Thaler, Shiller) nabízejí alternativní rámec vysvětlující anomálie trhu prostřednictvím systematických kognitivních chyb:

| Jev | Popis |
|-----|-------|
| **Overconfidence** | Investoři nadhodnocují svou přesnost a schopnosti |
| **Herding (stádní chování)** | Investoři kopírují chování okolí i přes vlastní signály |
| **Loss aversion** | Ztráty jsou psychologicky výraznější než stejně velké zisky ($\lambda \approx 2$) |
| **Anchoring** | Přílišný vliv počáteční (anchor) informace na odhady |
| **Mental accounting** | Separátní mentální „účty" pro různé části portfolia |
| **Disposition effect** | Tendence prodávat vítěze příliš brzy, držet poraženýe příliš dlouho |

### Prospektová teorie (Kahneman & Tversky, 1979)

Investoři nevyhodnocují výsledky v absolutních hodnotách bohatství, ale jako **odchylky od referenčního bodu** (gains vs. losses). Hodnotová funkce je:
- Konkávní pro zisky (risk aversion v doméně zisků)
- Konvexní pro ztráty (risk seeking v doméně ztrát)
- Asymetrická: $v(\text{loss}) > v(\text{gain})$ pro $|\text{loss}| = |\text{gain}|$

$$V = \sum_i \pi(p_i) \cdot v(x_i)$$

kde $\pi$ je váhovací funkce pravděpodobnosti (nadhodnocuje malé pravděpodobnosti).

## Praktický závěr

EMH má zásadní implikace pro správu portfolia:
- Aktivní portfolio management konzistentně nepřekonává pasivní strategie (indexové fondy) po odečtení nákladů (Sharpe, 1991).
- **Pasivní investování** (ETF, indexové fondy) je racionální strategií v efektivním trhu.
- Abnormální výnosy, pokud existují, jsou buď odměnou za riziko (nejsou „free lunch") nebo projevem dočasné neefektivity.
