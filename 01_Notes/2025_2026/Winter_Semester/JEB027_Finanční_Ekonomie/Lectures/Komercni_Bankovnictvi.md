---
course: "JEB027"
topic: "Komerční bankovnictví — funkce, bilance, regulace, Basel, budoucnost"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P05-2025_Komerční_bankovnictvi.pdf"
tags: [JEB027, komercni-bankovnictvi, bankovni-regulace, Basel, NIM, transformace-splatnosti]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P05-2025_Komerční_bankovnictvi.pdf]]
Related: [[Financni_Vykazy_Banky]], [[ROA_ROE_Analyza]], [[Bancni_Regulace_a_Basel]], [[Centralni_Bankovnictvi]], [[Decentralizovane_Finance]]

# Komerční bankovnictví

## Definice a základní funkce

**Komerční banka** je finanční instituce, jejíž klíčové funkce jsou:

1. **Přijímání depozit:** Banka je zákonným správcem vkladů domácností a firem.
2. **Poskytování úvěrů:** Transformace depozit na úvěry (alokace kapitálu).
3. **Realizace platebního styku:** Zprostředkování transakcí v ekonomice.
4. **Transformace splatností:** Krátkodobé závazky (depozita) → dlouhodobá aktiva (úvěry).

Transformace splatností je ekonomicky hodnotná (banka profituje z výnosové křivky), ale generuje strukturální **riziko likvidity** a **úrokové riziko**.

## Rozvaha komerční banky — zjednodušený model

```
AKTIVA                         PASIVA
────────────────────────────────────────
Hotovost            │ Depozita (krátkodobé)
Cenné papíry        │ Mezibankovní zdroje
Úvěry (dlouhodobé)  │ Vydané dluhopisy
Ostatní aktiva      │ Vlastní kapitál
────────────────────────────────────────
```

**Klíčové napětí:** aktiva jsou méně likvidní a delší splatnosti než pasiva → tzv. **maturity gap**.

## Výkonnost bank — Baltespergerův model (1980)

Přednáška pracuje s modelem, ve kterém je banka optimalizující podnik maximalizující zisk:

$$\Pi = \underbrace{r_L \cdot L + r_S \cdot S}_{\text{Výnosy}} - \underbrace{r_D \cdot D + r_M \cdot M + C(L, D)}_{\text{Náklady}}$$

kde:
- $L$ = úvěry (loans), $S$ = cenné papíry (securities)
- $D$ = depozita, $M$ = mezibankovní výpůjčky
- $r_L, r_S, r_D, r_M$ = příslušné úrokové sazby
- $C(L, D)$ = provozní náklady (rostoucí v objemu úvěrů a depozit)

Banka nastaví $L, D$ tak, aby mezní výnos = mezní náklady.

## Ukazatele výkonnosti

Viz [[ROA_ROE_Analyza]] pro detailní rozbor. Klíčové ukazatele:

- **ROE** (Return on Equity): výnosnost vlastního kapitálu → viz DuPont rozklad
- **NIM** (Net Interest Margin): čistá úroková marže
- **C/I** (Cost-to-Income): efektivita nákladů
- **NPL** (Non-Performing Loans): kvalita úvěrového portfolia
- **P/BV**: tržní ocenění vs. účetní hodnota

**Vysvětlení vysoké ziskovosti bank v ČR:**
- Vysoká NIM (ČNB sazby > ECB sazby)
- Nízký C/I (oligopolní struktura, digitalizace)
- Nízký NPL (silná ekonomika, nízká nezaměstnanost)

## TOP globální banky — vzestup Číny

| Banka | Země | Aktiva (přibližně) |
|-------|------|--------------------|
| Industrial and Commercial Bank of China (ICBC) | Čína | >4 bil. USD |
| China Construction Bank (CCB) | Čína | >3,5 bil. USD |
| Agricultural Bank of China (ABC) | Čína | >3,5 bil. USD |
| JPMorgan Chase | USA | ~4 bil. USD |

Čína dominuje žebříčkům podle aktiv — klíčová otázka: je tato dominance udržitelná? (Výzvy: NPL u nemovitostního sektoru, geopolitická rizika.)

## Trendy v komerčním bankovnictví

### Umělá inteligence (AI)

- Úvěrové scorování (credit scoring)
- Detekce podvodů (fraud detection)
- Automatizace KYC/AML procesů
- Personalizace bankovních produktů
- Chatboti a zákaznický servis

### ESG integrace

Viz [[ESG_Finance]]. Banky začleňují ESG kritéria do:
- Úvěrových procesů (green lending, sustainability-linked loans)
- Řízení rizik (transition risk, physical risk)
- Reportingu (TCFD, SFDR)

### 3 scénáře budoucnosti bankovnictví

1. **Transformace:** Banky se přizpůsobí — digitalizace poboček, AI, ESG
2. **Uberizace (platformizace):** PSD2 v EU otevírá data třetím stranám (open banking) → BigTech a Fintech narušují bankovní byznys model
3. **Blockchain/DEFI:** Decentralizované finance vytlačují tradiční zprostředkovatele → viz [[Decentralizovane_Finance]]

## Regulace komerčních bank

Viz [[Bancni_Regulace_a_Basel]] pro detailní rozbor Basel Framework. Klíčové principy:

- Minimální kapitálová přiměřenost (CAR — Capital Adequacy Ratio)
- Požadavky na likviditu (LCR, NSFR)
- Dohled ČNB a ECB (SSM — Single Supervisory Mechanism v eurozóně)
- Ochrana vkladatelů: Fond pojištění vkladů (FPV) — pojistí vklady do 100 000 EUR

## Způsoby záchrany bank v krizi

| Mechanismus | Popis |
|-------------|-------|
| **Rekapitalizace (bail-out)** | Státní vstup jako akcionář |
| **Garance za závazky** | Záruky za splácení závazků banky |
| **Odkup aktiv** | Stát/SPOV odkoupí toxická aktiva |
| **Dodání likvidity** | Emergency Liquidity Assistance (ELA) od CB |

Viz [[ROA_ROE_Analyza]] pro empirické výsledky o efektivitě bail-outů (Gerhardt & Vander Vennet, 2017).
