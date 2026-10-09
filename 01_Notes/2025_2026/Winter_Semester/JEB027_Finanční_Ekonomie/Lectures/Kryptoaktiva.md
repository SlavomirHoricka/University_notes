---
course: "JEB027"
topic: "Kryptoaktiva — definice, typy, CBDC vs. kryptoaktiva, tokenizace, stablecoiny"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06-2025_DEFI_a_Fintech.pdf"
tags: [JEB027, kryptoaktiva, CBDC, stablecoiny, tokenizace, Bitcoin, Ethereum, MiCA]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06-2025_DEFI_a_Fintech.pdf]]
Related: [[Decentralizovane_Finance]], [[Blockchain_a_Smart_Kontrakty]], [[Penize_a_jejich_Funkce]], [[Kapitalovy_Trh_a_DEFI]]

# Kryptoaktiva

## Definice

**Kryptoaktivum** = digitální aktivum, které může být převáděno mezi držiteli elektronicky pomocí technologie distribuovaného registru (DLT) s využitím kryptografie k zabezpečení (ČNB, 2022).

**Kryptoaktivum = nehmotná movitá věc.** Termín „kryptoměna" je nepřesný, protože kryptoaktiva obecně nesplňují definici peněz jako *numéraire*:
- Nestabilní hodnota (neplní funkci uchovatele hodnoty spolehlivě)
- Omezená akceptace jako prostředek směny
- Nekvalifikuje jako zúčtovací jednotka v ekonomice

Výjimky: Stablecoiny (viz níže) se definici peněz přibližují.

## Typy kryptoaktiv

| Kategorie | Příklady | Charakteristika |
|-----------|----------|-----------------|
| **Platební kryptoaktiva** | Bitcoin (BTC), Litecoin (LTC) | Primárně jako prostředek směny/uchování hodnoty |
| **Utility tokeny** | Chainlink (LINK) | Přístup ke specifické platformě/službě |
| **Security tokeny** | Tokenizované akcie | Reprezentují vlastnická práva; podléhají cenné papírové regulaci |
| **Stablecoiny** | USDT (Tether), USDC, DAI | Navázány na stabilní aktivum (USD, EUR, komodity) |
| **NFT (Non-Fungible Tokens)** | CryptoPunks, Bored Apes | Unikátní digitální aktiva; nezaměnitelné |
| **Governance tokeny** | UNI (Uniswap), AAVE | Hlasovací práva v DeFi protokolech |
| **CBDC** | Digital Yuan, Digital Euro | Digitální forma peněz centrální banky |

## Přehled klíčových kryptoaktiv (k 1. říjnu 2025)

| # | Název | Ticker | Cena (USD) | Tržní kap. (USD) | Meziroční změna |
|---|-------|--------|------------|-----------------|----------------|
| 1 | Bitcoin | BTC | 118 660 | 2,35 bil. | +94,9 % |
| 2 | Ethereum | ETH | 4 146 | 521 mld. | +72,8 % |
| 3 | Tether | USDT | 1,00 | 175 mld. | 0 % (stablecoin) |
| 4 | XRP | XRP | — | — | — |
| 5 | BNB | BNB | — | — | — |

## CBDC vs. Kryptoaktiva — srovnání

| Dimenze | CBDC | Kryptoaktivum |
|---------|------|---------------|
| **Emitent** | Centrální banka (závazek CB) | Soukromý subjekt / komunita |
| **Stabilita hodnoty** | Rovna hodnotě národní měny | Vysoce volatilní (tržní cena) |
| **Právní status** | Zákonné platidlo (legal tender) | Nehmotná movitá věc; není legálním platidlem* |
| **Regulace** | Plně regulované | Variabilní, závisí na jurisdikci |
| **Technologie** | Může, ale nemusí používat blockchain | Většinou blockchain |
| **Anonymita** | Nižší (AML/KYC) | Pseudonymita |
| **Měnová politika** | Součást měnové politiky CB | Bez vazby na státní měnovou politiku |
| **Maximální množství** | Neomezeno (CB kontroluje) | Často pevně dané (Bitcoin max. 21M BTC) |

*Výjimka: V Salvadoru byl Bitcoin uznán jako zákonné platidlo (2021), v praxi přijetí omezené.

## Stablecoiny

**Stablecoin** je kryptoaktivum navázané na stabilní aktivum, jehož cílem je minimalizovat volatilitu:

| Typ zajištění | Příklady | Mechanismus |
|---------------|----------|-------------|
| **Fiat-collateralized** | USDT (Tether), USDC | 1:1 krytí USD rezervami |
| **Crypto-collateralized** | DAI (MakerDAO) | Přezajištěno ETH (overcollateralization) |
| **Algorithmic** | TerraUSD (UST — selhalo 2022) | Algoritmický mechanismus stabilizace |
| **Commodity-backed** | PAXG (zlato) | Backed fyzickým zlatem |

### Selhání TerraUSD (2022)

Algoritmický stablecoin TerraUSD (UST) udržoval navázání na USD prostřednictvím arbitráže s párovým tokenem LUNA. Při šoku v důvěře nastala spirála depeggingu: UST → $0; LUNA → $0. Tržní kapitalizace ztracena: ~$40 mld. v týdnu. Ukázkový případ systémového rizika v DeFi.

### Regulace stablecoinů

- **MiCA (EU):** Kategorizace — Asset-Referenced Tokens (ART) a E-Money Tokens (EMT); přísné kapitálové a likviditní požadavky pro velké stablecoiny
- **STABLE Act, GENIUS Act (USA):** Navrhovaná regulace stablecoinů (vyžadovat bankovní licenci nebo licensing framework)

## Tokenizace aktiv

**Tokenizace** = převod vlastnických práv k reálnému aktivu do podoby digitálního tokenu na blockchainu.

Tokenizovatelná aktiva:
- Nemovitosti (fractional ownership)
- Státní dluhopisy (BlackRock BUIDL fund na Ethereum)
- Akcie (security tokens)
- Umělecká díla, IP práva
- Pohledávky, infrastruktura

**Výhody tokenizace:**
- **Frakcionalizace:** Nízký vstupní práh pro malé investory
- **Likvidita:** 24/7 obchodování bez burzovní infrastruktury
- **Transparentnost:** On-chain vlastnictví a history
- **Efektivita:** Automatické zúčtování (T+0 vs. T+1 na tradičních burzách)

Viz [[Kapitalovy_Trh_a_DEFI]] pro detailní rozbor tokenizace kapitálových trhů.

## Energetická náročnost

Bitcoin (PoW) spotřebuje ročně více energie než mnoho středně velkých zemí (cca 130–150 TWh/rok, srovnatelné s Polskem nebo Argentinou). Důvod: hash rate soutěž miners — energy cost je součástí bezpečnostního mechanismu. Ethereum po přechodu na PoS snížilo spotřebu o ~99,95 %.

Viz [[ESG_Finance]] pro diskusi o environmentálních otázkách kryptoaktiv.
