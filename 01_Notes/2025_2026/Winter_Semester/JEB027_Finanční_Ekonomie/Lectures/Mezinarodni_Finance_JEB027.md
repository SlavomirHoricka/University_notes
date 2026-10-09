---
course: "JEB027"
topic: "Mezinárodní finance — platební bilance, devizový kurz, parita kurzů, kapitálové toky"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P11-2025_Mezinárodní_finance.pdf"
tags: [JEB027, mezinarodni-finance, platebni-bilance, devizovy-kurz, PPP, UIP, IRP]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P11-2025_Mezinárodní_finance.pdf]]
Related: [[Urokova_Mira_a_Casova_Hodnota_Penez]], [[Centralni_Bankovnictvi]], [[Verejne_Finance]], [[Hospodarska_Politika]]

# Mezinárodní finance

## Devizový kurz

**Devizový kurz (exchange rate)** je cena jedné měny vyjádřená v jiné měně.

- **Přímá kotace:** Kolik CZK za 1 EUR? → Např. 25,0 CZK/EUR
- **Nepřímá kotace:** Kolik EUR za 1 CZK? → Např. 0,04 EUR/CZK

### Apreciace vs. depreciace

- **Apreciace domácí měny:** Domácí měna posiluje → importy levnější, exporty dražší
- **Depreciace domácí měny:** Domácí měna oslabuje → importy dražší, exporty levnější

### Systémy měnových kurzů

| Režim | Popis | Příklady |
|-------|-------|---------|
| **Plovoucí (floating)** | Kurz určen trhem (nabídka/poptávka) | USD, EUR, GBP, CZK |
| **Řízené plovoucí (managed float)** | Centrální banka občasně intervenuje | ČNB v roce 2013–2017 |
| **Pevný (fixed / peg)** | Kurz zafixován vůči jiné měně nebo koši | HK dolar (peg k USD), SAR |
| **Currency board** | Plné krytí domácí MB zahraniční měnou | Bulharsko (BGN/EUR) |
| **Eurozóna** | Společná měna — nutnost splnit konvergenční kritéria | Viz [[Verejne_Finance]] |

## Paritní teorie (Parity Conditions)

### Parita kupní síly (PPP — Purchasing Power Parity)

**Absolutní PPP:** Kurz by měl zajistit, aby totožné zboží mělo stejnou cenu v obou zemích (zákon jedné ceny):

$$E = \frac{P^{dom}}{P^{for}}$$

kde $E$ = devizový kurz (domácí měna za jednotku zahraniční), $P^{dom}$ = domácí cenová hladina, $P^{for}$ = zahraniční cenová hladina.

**Relativní PPP:** Změny kurzu reflektují rozdíly v inflačních tempech:

$$\frac{E_1}{E_0} = \frac{(1+\pi^{dom})}{(1+\pi^{for})} \approx 1 + (\pi^{dom} - \pi^{for})$$

**Balassa-Samuelson efekt:** Vyspělé ekonomiky mají strukturálně vyšší price level (zejména ve službách) kvůli vyšší produktivitě v obchodovatelném sektoru → PPP není splněna pro absolutní cenové úrovně.

### Nepokrytá úroková parita (UIP — Uncovered Interest Rate Parity)

V podmínkách volných kapitálových toků a neutrálnosti rizika by měly platit:

$$i^{dom} = i^{for} + E\left[\frac{\Delta E}{E}\right]$$

kde $E[\Delta E / E]$ je očekávaná změna (apreciace/depreciace) kurzu.

**Interpretace:** Vyšší nominální sazby v ČR vs. eurozóně by měly být „kompenzovány" depreciací CZK — v praxi UIP krátkodobě selhává (UIP puzzle).

### Pokrytá úroková parita (CIP — Covered Interest Rate Parity)

Platí bezarbitrážně při využití forwardového kurzu $F$:

$$\frac{F}{E} = \frac{1+i^{dom}}{1+i^{for}}$$

CIP platí spolehlivě na likvidních trzích — odchylky (CIP deviation) jsou ukazatelem tržního napětí nebo regulatorní arbitráže.

### Fisherova mezinárodní parita

Reálné úrokové sazby by se měly vyrovnat přes hranice (International Fisher Effect):

$$r^{dom} \approx r^{for}$$

## Platební bilance

**Platební bilance (Balance of Payments, BOP)** je systematický záznam všech ekonomických transakcí mezi rezidenty a nerezidenty za dané období. Skládá se z:

| Složka | Obsah | Rovnováha |
|--------|-------|-----------|
| **Běžný účet (BÚ / CA)** | Vývoz/dovoz zboží, služby, prvotní/sekundární důchody | $CA = X - M + \text{Net income} + \text{Transfers}$ |
| **Kapitálový účet (KA)** | Kapitálové transfery (strukturální fondy EU) | Malý v ČR |
| **Finanční účet (FA)** | PZI, portfoliové investice, ostatní investice, rezervy | Pohyby kapitálu |

**Základní identita BOP:**

$$CA + KA + FA = 0$$

Schodek BÚ je financován přítokem kapitálu (kladný FA — pasiva rostou nebo aktiva klesají).

### Pozice ČR

ČR je tradičně zemí s deficitem BÚ (schodek obchodní bilance ve službách, výrazný odliv dividend PZI firem) kompenzovaným přítokem PZI (positive FA).

## Mezinárodní kapitálové toky

| Typ | Popis | Specifika |
|-----|-------|-----------|
| **PZI (FDI)** | Přímé zahraniční investice — >= 10 % podíl | Relativně stabilní, long-term |
| **Portfoliové investice** | Nákup CP pod 10 % podílu | Volatilní, citlivé na sazby a sentiment |
| **Ostatní investice** | Mezibankovní půjčky, obchodní úvěry | — |
| **Rezervy** | Devizové rezervy centrální banky | Intervence — viz [[Centralni_Bankovnictvi]] |

### Příčiny náhlých zastavení kapitálových toků (Sudden Stops)

- Náhlé obrácení toku kapitálu (capital flow reversal) může způsobit měnovou a platební krizi (viz Mexiko 1994, Asie 1997, Rusko 1998, ČR 1997)
- **Currency Crisis:** Spekulativní útok na kurz — CB vynakládá rezervy na obranu peggingu; pokud rezervy nestačí, kurz se zhroutí

## Devizové intervence ČNB (2013–2017)

**Kontextuální příklad:** ČNB zavedla v listopadu 2013 devizový závazek (FX commitment) — udržení kurzu CZK/EUR ≥ 27 CZK/EUR jako nástroj nestandardní měnové politiky (*quantitative easing přes devizový kurz*).

- Mechanismus: ČNB nakupovala eura, prodávala CZK → bezprecedentní nárůst devizových rezerv ČNB (z ~30 mld. USD na ~130 mld. USD)
- Dopad: CZK oslabila, inflace vzrostla, vývoz byl stimulován
- Ukončení: Duben 2017 — exit ze závazku, CZK apreciovala

Viz [[Centralni_Bankovnictvi]] pro kontext nekonvenčních nástrojů měnové politiky.
