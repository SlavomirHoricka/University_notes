---
course: "JEB027"
topic: "Blockchain a smart kontrakty — architektura, konsenzus, využití ve financích"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06-2025_DEFI_a_Fintech.pdf"
tags: [JEB027, blockchain, smart-kontrakty, DLT, Proof-of-Work, Proof-of-Stake, Ethereum]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06-2025_DEFI_a_Fintech.pdf]]
Related: [[Decentralizovane_Finance]], [[Kryptoaktiva]], [[Kapitalovy_Trh_a_DEFI]]

# Blockchain a smart kontrakty

## Blockchain — definice a architektura

**Blockchain** je **distribuovaná databáze (DLT — Distributed Ledger Technology)** sdílená na síti počítačových uzlů (nodes). Název odráží strukturu dat: transakce jsou seskupeny do **bloků**, které jsou kryptograficky provázány do **řetězce (chain)**.

### Struktura bloku

Každý blok obsahuje:
- **Seznam transakcí** (data layer)
- **Hash (kryptografický otisk) předchozího bloku** — zajišťuje neměnnost; změna jednoho bloku invaliduje všechny následující
- **Nonce** (číslo použité jednou) — při PoW consensu slouží k řešení hashovací hádanky
- **Timestamp**
- **Merkle Root** — kryptografický souhrn všech transakcí v bloku

### Klíčové vlastnosti

| Vlastnost | Popis |
|-----------|-------|
| **Decentralizace** | Žádný centrální správce; konsenzus distribuovaný mezi uzly |
| **Neměnnost (Immutability)** | Jednou potvrzené transakce nelze zpět měnit bez přepsání celého řetězce |
| **Transparentnost** | Veřejné blockchainy jsou plně průhledné — každý může ověřit každou transakci |
| **Bezpečnost** | Kryptografické hashing (SHA-256 u Bitcoinu) a konsensuální algoritmy |

## Typy blockchainů

| Typ | Přístup | Příklady | Použití |
|-----|---------|----------|---------|
| **Veřejný (Public)** | Permissionless — kdokoliv | Bitcoin, Ethereum | Kryptoaktiva, DeFi |
| **Privátní (Private)** | Permissioned — jen oprávněné entity | Hyperledger Fabric | Interní bankovní systémy |
| **Konsorcijní (Consortium)** | Permissioned — skupina organizací | R3 Corda | Mezibankovní clearing |

## Konsenzuální algoritmy

**Konsenzuální algoritmus** zajišťuje, že všechny uzly sítě souhlasí se stavem databáze — přidání nového bloku musí být odsouhlaseno distribuovanou sítí.

### Proof of Work (PoW)

Používáno Bitcoinem. Validátoři (miners) soutěží o právo přidat blok tím, že jako první vyřeší kryptografickou hashovací hádanku:

$$\text{Najít }n: H(\text{block\_data} || n) < T$$

kde $H$ je kryptografická hashovací funkce a $T$ je cílový práh (difficulty target).

**Nevýhody:** Extrémně vysoká energetická náročnost (Bitcoin spotřebuje srovnatelně s celou zemí).

### Proof of Stake (PoS)

Používáno Ethereem (od merge v září 2022). Validátoři jsou vybíráni na základě množství **stakovaných** kryptoaktiv — čím více zastaví, tím vyšší šance být vybrán:

- Stakers nemohou jednat nepoctivě bez rizika „slashingu" (ztrátý části stakovaných prostředků)
- Energetická úspornost: Ethereum snížilo energetickou spotřebu o ~99,95 % po přechodu na PoS

### Další algoritmy

- **Delegated Proof of Stake (DPoS):** EOS, Tron — delegovaní reprezentanti validují
- **Proof of Authority (PoA):** Privátní/konsorcijní blockchainy — identifikovaní validátoři

## Smart kontrakty

**Smart kontrakty** jsou **samo-vykonávající** programy uložené na blockchainu, jejichž podmínky jsou zapsány přímo v kódu. Klíčový princip: *"Code is Law."*

**Vlastnosti:**
- Automaticky se vykonají při splnění definovaných podmínek (if-then logika)
- Eliminují potřebu trustovaných zprostředkovatelů
- Jsou nezměnitelné a transparentní po nasazení
- Nemohou být cenzurovány ani zastaveny

**Frameworky:** Ethereum (Solidity), Solana (Rust), Cardano (Plutus)

### Příklady smart kontraktů ve financích

| Aplikace | Protokol | Popis |
|----------|----------|-------|
| Decentralizovaná burza (DEX) | Uniswap, Curve | Automatizovaný market maker (AMM) bez tradičního order booku |
| Lending/Borrowing | Aave, Compound | Automatické úvěry zajištěné kryptoaktivy; likvidace při poklesu kolaterálu |
| Stablecoiny | MakerDAO (DAI) | Vydávání stablecoinu zajištěného přezajištěnými kryptoaktivy |
| Deriváty | dYdX | Perpetual futures na kryptoaktiva |

### Smart kontrakty vs. tradiční kontrakty

| | Tradiční kontrakt | Smart kontrakt |
|--|-------------------|----------------|
| Vymáhání | Právní systém, soudy | Automatické — kód |
| Zprostředkovatelé | Advokáti, notáři | Blockchain protokol |
| Rychlost | Dny až týdny | Sekundy |
| Náklady | Vysoké (právní poplatky) | Nízké (gas fee) |
| Flexibilita | Vysoká | Nízká (kód nelze měnit) |

## Blockchain jako platební infrastruktura

Tradiční platební systém: transakce prochází vydavatelem karty, zpracovatelem platby, platební sítí, clearingem → nákupní cena $2 kávy generfuje transakční náklady ~$0,30 (cca 15 %) a vypořádání trvá 1–3 dny.

Blockchain platba: přímý transfer hodnoty mezi odesílatelem a příjemcem → transakční náklady výrazně nižší, vypořádání v sekundách.

**Aplikace:** přeshraniční platby (cross-border payments) — SWIFT vs. blockchain (Ripple/XRP).

## Rizika blockchainu

| Riziko | Popis |
|--------|-------|
| **51% útok** | Pokud jeden subjekt ovládne >50 % hash rate (PoW), může revidovat transakce |
| **Smart contract bugs** | Chyby v kódu mohou být zneužity (DAO hack 2016 — 60M USD) |
| **Key management** | Ztráta privátního klíče = trvalá ztráta prostředků |
| **Regulatory risk** | Zákaz kryptoaktiv v určitých jurisdikcích |
| **Oracle problem** | Smart kontrakty potřebují spolehlivá data z reálného světa (Chainlink jako řešení) |

Viz [[Operacni_Riziko]] pro obecný rámec operačního rizika.
