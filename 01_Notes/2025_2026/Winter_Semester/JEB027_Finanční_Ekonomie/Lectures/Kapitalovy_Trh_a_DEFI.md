---
course: "JEB027"
topic: "Kapitálový trh a DeFi — tokenizace cenných papírů, DEX vs. CEX, DeFi protokoly"
source: "00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06B-2025_Kapitálový_trh_DEFI_(O.Dusílek).pdf"
tags: [JEB027, kapitalovy-trh, DeFi, tokenizace, DEX, AMM, Uniswap]
created: 2026-04-19
---

Parent: [[JEB027_Finanční_Ekonomie_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie/Lectures/JEB027_P06B-2025_Kapitálový_trh_DEFI_(O.Dusílek).pdf]]
Related: [[Decentralizovane_Finance]], [[Kryptoaktiva]], [[Blockchain_a_Smart_Kontrakty]], [[Financni_Trhy]]

# Kapitálový trh a DeFi

## Průnik DeFi a tradičních kapitálových trhů

Přednáška (O. Dusílek) se zaměřuje na průnik decentralizovaných financí s tradičními kapitálovými trhy — zejména tokenizaci aktiv a roli DEX (decentralizovaných burz).

## DEX vs. CEX (Centralizovaná burza)

| Dimenze | CEX (Centralizovaná burza) | DEX (Decentralizovaná burza) |
|---------|---------------------------|------------------------------|
| **Správa aktiv** | Custodial — burza drží aktiva uživatelů | Non-custodial — uživatel kontroluje své klíče |
| **KYC/AML** | Vyžadováno | Obecně nevyžadováno |
| **Likvidita** | Order book (tradiční) | Automated Market Maker (AMM) nebo on-chain order book |
| **Regulace** | Regulovaná (např. Coinbase, Binance mají licence) | Minimální až žádná přímá regulace |
| **Riziko hacknutí** | Centralizovaná honeypot (Mt. Gox, FTX) | Riziko smart contract bugs |
| **Příklady** | Coinbase, Binance, Kraken | Uniswap, Curve, dYdX, SushiSwap |

## Automated Market Maker (AMM)

**AMM** je protokol DEX, který nahrazuje tradiční párování příkazů (order book) **matematickým vzorcem** pro tvorbu cen z likviditního poolu.

### Constant Product Market Maker (Uniswap v2)

Základní invariantura:

$$x \cdot y = k$$

kde $x$ a $y$ jsou množství dvou tokenů v poolu a $k$ je konstanta. Při nákupu tokenu $x$ (odběru $\Delta x$) se cena automaticky přizpůsobí:

$$(x + \Delta x)(y - \Delta y) = k \implies \Delta y = y - \frac{k}{x + \Delta x}$$

**Cena tokenu X v termínech Y:**

$$P_X = \frac{y}{x}$$

**Impermanent Loss (Dočasná ztráta):** Liquidity providers (LP) trpí impermanent loss, pokud se ceny tokenů v poolu divergují od okamžiku vkladu likvidity. Čím větší divergence, tím vyšší IL. Formálně:

$$IL = \frac{2\sqrt{r}}{1+r} - 1$$

kde $r$ je poměr nové k původní ceně tokenu.

### Koncentrovaná likvidita (Uniswap v3)

LP mohou definovat **cenový rozsah** $[P_a, P_b]$, ve kterém chtějí poskytovat likviditu — výrazně zvyšuje kapitálovou efektivitu (až 4000× pro stablecoins).

## Tokenizace na kapitálových trzích

**Real World Assets (RWA) on-chain:** Tokenizace reálných cenných papírů — State Street, Franklin Templeton, BlackRock (BUIDL fund — tokenizovaný money market fund na Ethereum).

**Výhody tokenizace pro kapitálové trhy:**
- **T+0 settlement:** Okamžité vypořádání oproti T+1 nebo T+2 na tradičních burzách
- **Frakcionalizace:** Nižší minimální investice
- **Globální přístup:** 24/7 obchodování bez geografických omezení
- **Transparentnost:** On-chain ověřitelné vlastnictví

**Příklady RWA projektů:**
- **Ondo Finance:** Tokenizované US Treasury bills (yield)
- **Maple Finance:** Korporátní úvěry on-chain
- **Centrifuge:** Tokenizace reálných pohledávek

## DeFi Lending Protokoly

### Overcollateralized Lending (Aave, Compound)

Úvěry jsou vždy **přezajištěné** — uživatel musí deposznit kolaterál vyšší hodnoty, než si půjčuje (typicky 150 % LTV).

**Health Factor:**

$$HF = \frac{\sum_i \text{Collateral}_i \cdot LT_i}{\text{Total Borrowed}} > 1$$

Pokud $HF < 1$, nastane **automatická liquidace** — smart kontrakt prodá část kolaterálu za tržní cenu.

**Úrokové sazby** jsou dynamicky stanoveny dle míry využití (utilization rate $U = \text{Borrowed} / \text{Available}$):

$$r_{\text{borrow}}(U) = r_{\text{base}} + U \cdot \text{slope}_1 \quad \text{nebo} \quad r_{\text{base}} + \text{kink} + (U - U_{\text{opt}}) \cdot \text{slope}_2$$

### Flash Loans

Bezkolaterálové úvěry, které musí být splaceny v **rámci jedné blockchain transakce** (atomic transaction). Nevyplatí-li se půjčka ve stejné transakci, celá transakce se rollbackuje.

Příklad použití: Arbitráž mezi DEX, refinancování pozic, manipulace s cenou (price oracle attack).

## Rizika DeFi kapitálových trhů

| Riziko | Popis | Příklad |
|--------|-------|---------|
| **Smart contract risk** | Chyby v kódu → exploit | Cream Finance hack ($130M, 2021) |
| **Oracle risk** | Manipulace cenových dat z oracle | Mango Markets hack ($117M, 2022) |
| **Impermanent loss** | Ztráta LP při divergenci cen | Viz vzorec výše |
| **Liquidity risk** | Stažení likvidity (bank run na poolu) | — |
| **Regulatory risk** | SEC action, MiCA compliance | — |

Viz [[Operacni_Riziko]] pro obecný rámec identifikace a řízení operačního rizika.
