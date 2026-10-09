---
course: "JEB027"
topic: "Decentralizované finance (DeFi) — blockchain, smart kontrakty, kryptoaktiva, regulace"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06-2025_DEFI_a_Fintech.pdf"
tags: [JEB027, DeFi, blockchain, smart-kontrakty, MiCA, CBDC, Fintech]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06-2025_DEFI_a_Fintech.pdf]]
Related: [[Kryptoaktiva]], [[Blockchain_a_Smart_Kontrakty]], [[Kapitalovy_Trh_a_DEFI]], [[Penize_a_jejich_Funkce]], [[Komercni_Bankovnictvi]]

# Decentralizované finance (DeFi)

## Definice a základní pojmy

**Decentralizované finance (DeFi)** jsou finanční služby postavené na **DLT (Distributed Ledger Technology)**, které eliminují potřebu tradičních finančních zprostředkovatelů. Počátek DeFi: 2015 — vznik platformy Ethereum.

Klíčové vlastnosti DeFi:
- Finanční transakce prováděny **přímo mezi účastníky** (peer-to-peer) za použití **smart kontraktů**
- Přístup k finančním službám bez bankovních účtů (finanční inkluze)
- Transparentnost — veškeré transakce viditelné na blockchainu
- Permissionless — kdokoliv s připojením k internetu může participovat

**Příklady DeFi aplikací:** úvěry (MakerDAO, Aave), obchodování s kryptoaktivy (Uniswap, Curve), pojištění, stablecoiny.

## DeFi vs. tradiční finance (TradFi)

| Kritérium | Tradiční finance (TradFi) | Decentralizované finance (DeFi) |
|-----------|--------------------------|----------------------------------|
| Zprostředkovatelé | Banky, burzy, pojišťovny | Smart kontrakty, decentralizované platformy |
| Přístup | Omezený (KYC, schválení institucí) | Otevřený, pseudonymní, bez schválení |
| Rychlost transakcí | Dny až hodiny | Minuty až sekundy |
| Transparentnost | Omezená, neveřejná | Plná — veřejné blockchainy |
| Regulace | Přísně regulované | Minimální až žádná regulace |
| Bezpečnost | Pod dohledem institucí | Závislá na kvalitě kódu (smart contract vulnerabilities) |
| Inovace | Pomalejší, postupná | Rychlá, experimentální |

## Výhody a nevýhody DeFi

### Výhody

1. **Transparentnost:** Všechny transakce viditelné na blockchainu
2. **Dostupnost:** Globální přístup bez geografických omezení
3. **Rychlost:** Real-time transakce
4. **Nízké poplatky:** Nižší než u tradičních finančních institucí
5. **Finanční inkluze:** Přístup pro unbanked populaci

### Nevýhody

1. **Bezpečnostní rizika:** Zranitelnosti v kódu smart kontraktů (hacky)
2. **Vysoká volatilita:** Hodnota kryptoaktiv silně kolísá
3. **Právní nejistoty:** Dynamičnost regulace DeFi
4. **Složitost UI:** Matoucí pro nové uživatele
5. **Riziko podvodů:** Rug pulls, scam projekty

## Technologie: Blockchain

Viz detailní note: [[Blockchain_a_Smart_Kontrakty]].

**Blockchain** je distribuovaná databáze (DLT) sdílená mezi uzly sítě. Každý blok obsahuje:
- Seznam transakcí
- Kryptografický otisk (hash) předchozího bloku
- Timestamp a metadata

Vlastnosti: neměnnost, transparentnost, decentralizace.

**Konsenzuální algoritmy:**
- **Proof of Work (PoW):** Mining — výpočetně náročný (Bitcoin) → vysoká energetická náročnost
- **Proof of Stake (PoS):** Validátoři drží (stake) kryptoaktivum jako záruku (Ethereum po merge 2022) → energeticky úspornější

**Analogie „obchodního centra"** (Kacerovský, 2025): Blockchain umožňuje konsolidaci fragmentovaných finančních služeb na jednu transparentní platformu — podobně jako obchodní centra konsolidovala fragmentovaný maloobchod.

## Gartnerův Hype Cycle

**Gartner Hype Cycle** graficky znázorní životní cyklus nových technologií:

1. **Innovation Trigger** — technologie vzbuzuje zájem, ale není dostupná
2. **Peak of Inflated Expectations** — přehnaná očekávání a humbuk
3. **Trough of Disillusionment** — realita nesplňuje očekávání, zájem opadá
4. **Slope of Enlightenment** — pochopení skutečných přínosů
5. **Plateau of Productivity** — technologie je přijata a přináší reálné přínosy

DeFi/kryptoaktiva (2024): Dle Gartner Hype Cycle 2024 — většina DeFi technologií stále prochází fázemi 2–4.

## Kryptoaktiva

Viz [[Kryptoaktiva]] pro detailní rozbor.

## Aktuální trendy v DeFi

1. **Real World Assets (RWA) on-chain:** Tokenizace reálných aktiv (nemovitosti, státní dluhopisy, pohledávky) a jejich integrace do DeFi protokolů
2. **Restaking:** Protokoly jako EigenLayer umožňují opakované využití staked ETH pro zabezpečení dalších protokolů
3. **DeFi 2.0:** Zlepšení kapitálové efektivity (Curve v2, GMX, Uniswap v4)
4. **Cross-chain interoperabilita:** LayerZero, Wormhole — bezproblémová komunikace mezi různými blockchainy
5. **Compliance:** Tlak institucionálních investorů na KYC/AML integraci

## Regulace DeFi

### EU

- **MiCA (Markets in Crypto-Assets):** Regulace kryptoasset service providers (CASPs), stablecoinů; platné od 2024
- **MiFID II / AMLD:** Ochrana investorů, AML
- Dohled: ESMA (European Securities and Markets Authority), EBA

### USA

- **FinCEN:** Dohled nad AML pro kryptoaktiva
- **SEC:** Cenné papíry a compliance
- **STABLE Act, GENIUS Act:** Připravovaná regulace stablecoinů

## Fintech a BigTech

**Fintech:** Technologické firmy nabízející finanční služby (Revolut, N26, Wise, PayPal)
**BigTech:** Velké technologické firmy vstupující do finančního sektoru (Apple Pay, Google Pay, Amazon Lending)

**PSD2 (Payment Services Directive 2) v EU:**
- Otevřené bankovnictví (open banking): banky musí na žádost zákazníka sdílet jejich data s licencovanými třetími stranami (AISP, PISP)
- Umožňuje Fintechům a BigTechům přistupovat k bankovním datům → narušení tradičního bankovního byznys modelu

Viz [[Komercni_Bankovnictvi]] pro diskusi o uberizaci bankovnictví (PSD2 scénář).
