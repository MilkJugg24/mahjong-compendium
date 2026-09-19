# Mahjong Compendium

A collection of files gathered from around the web, filed by mahjong variant, so that each file's origin and legitimacy can be checked and proper rulebooks can eventually be built from material that has been verified rather than assumed.

The folder tree mirrors the variant family tree in [`_dev/source-chart/`](_dev/source-chart/): **one folder per variant, nested by descent**. Drop a collected file into the folder for the variant it documents, and log it in that folder's `README.md` table. Every folder's README carries the variant's lineage, the sources the chart cites for it, and how much those sources are actually worth.

## How to use this repository

| If you want to | Go to |
| --- | --- |
| Read it as a website | [compendium.pandaren.org](https://compendium.pandaren.org/) |
| Find the folder for a variant | The [glossary](#glossary) below |
| See how variants descend from each other | The [family tree](#family-tree) below |
| See what the sources say against each other | [`FINDINGS.md`](FINDINGS.md) |
| Check where a claim comes from | [`REFERENCES.md`](REFERENCES.md) |
| File a new document, or learn the conventions | [`_dev/CONVENTIONS.md`](_dev/CONVENTIONS.md) |
| See how the tree was derived from the chart | [`_dev/`](_dev/) |

Everything relating to the development of this repository — the source chart, the extracted data, and the scripts that generate the tree — lives in [`_dev/`](_dev/), separate from the folders you browse.

## Confidence

Each variant folder is tagged with how good the underlying sourcing is. This is a property of the **sources**, not of the variant: a `placeholder` tag means nobody has established where the game came from, not that the game is doubtful.

| Tag | Meaning | Folders |
| --- | --- | --- |
| `documented` | a published ruleset or rule description exists and is cited below | 28 |
| `catalogued` | listed in a variant catalogue with tile counts and hand sizes, but no rules text has been verified | 26 |
| `single-informant` | the whole entry rests on one report from one person | 4 |
| `disputed` | the descent shown here is contested; the chart drew this link dashed | 1 |
| `placeholder` | no source establishes the descent at all; the parent link is a guess | 1 |
| `lost` | no rules text survives | 1 |

## Family tree

61 documented rulesets. Indentation shows descent. Two links in the source chart were drawn dashed, meaning no source establishes the descent at all: **Nanyang variants** and **Korean traditional**.

```
Proto-mahjong (c. 1870s, rules lost)  [lost]
  Chinese archaic (c. 1890, Wilkinson)
  Late Qing style (c. 1903, Li Boyuan)
  Chinese pre-classical (Mauger, 1915)
  Chinese classical (1920s, 144 tiles)
    Shanghai / Hong Kong new style (1920s)
      Hong Kong old style (1950s, fu removed)
        Modern HKOS (3-faan minimum, 1970s)
        Guangdong style (1980s, additive scoring)
          Guangdong MCR / GMCR (2020s)
        Taiwanese style (16-tile hand, 1980s)
          Hong Kong Taiwanese (HKT)
        Nanyang variants (descent disputed)  [disputed]
          Singapore style (148 tiles, animal flowers)
          Malaysian 3-player (84 tiles, one suit)
          Malaysian 4-player (164 tiles, 24 flowers)
          Filipino style (16-tile hand, honours as flowers)
            Bashi-Bashi (3-player, Philippine casinos)
          Vietnamese classical (160 tiles, 8 jokers)
            Vietnamese modern (176+ tiles, 24+ jokers)
          Pong (Malaya, 120 tiles, Dobree 1955)
        MCR / Chinese official (1998, Guobiao)
          MCR scoring reference
        Zung Jung (Alan Kwan, 2000s)
      Mainland regionals
        Sichuan / Hunan / Tibetan (108 tiles)
        Sichuan bloody rules (Chengdu, 1990s)
        Sichuan 72-tile game (per Dragon Chang)  [single-informant]
        Fuzhou style (132 tiles)
        Fujian style (124 tiles, winds as flowers)  [single-informant]
        Beijing style (drawn wild tile)
        Nanjing style (dragons as flowers)
        Shenzhen style (kongs only, poorly documented)  [single-informant]
        Macau simplificado (112 tiles, hold 4)
        Tui Dao Hu (multiple winners)  [single-informant]
        Chinese casino style
    Japanese classical / arushiiaru (1929)
      Houchi rules (1952, Amano Daizou)
        Tokyo rules (1957, 1-han minimum)
          Modern rules (1967, ura dora, oka, bazoro)
            Modern riichi / yonma (red fives, 1970)
            Sanma (3-player riichi)
            WMPA / WMF (Korean, riichi-based)
    Korean traditional (104 tiles, no bamboo)  [placeholder]
    Babcock rules (1920, the little red book)
      Twenty Point Mah Jong (R.F. Foster, 1924)
      Western / British Empire style
        Wright-Patterson (USAF spouses, Ohio)
        India / Mumbai style (rotating round rules)
        Israeli Mah-Jongg Association
        Nepalese (11-tile winning hand)
        Pusser's Bones (Royal Navy)
      Regional US house rules (1920s-30s)
        NMJL card (1937, annual hand list)
          American mah jongg (152 tiles, jokers 1961)
            AMJA card
            Siamese Mah Jongg (two-handed, 2015)
Modern inventions (not descendants)
  Duplicate mahjong (prebuilt walls, no luck)
  Mhing (card version)
  Mahjong Masters Millions
```

## Glossary

Every variant in the tree, alphabetically, with the folder that holds its files.

| Variant | Family | Confidence | Evidence | Folder |
| --- | --- | --- | --- | --- |
| **American mah jongg** — 152 tiles, jokers 1961 | Western / American | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/01-american-mah-jongg`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/01-american-mah-jongg/) |
| **AMJA card** | Western / American | `documented` | `partial` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/01-american-mah-jongg/01-amja-card`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/01-american-mah-jongg/01-amja-card/) |
| **Babcock rules** — 1920, the little red book | Western / American | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/) |
| **Bashi-Bashi** — 3-player, Philippine casinos | Southeast Asian | `catalogued` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/04-filipino-style/01-bashi-bashi`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/04-filipino-style/01-bashi-bashi/) |
| **Beijing style** — drawn wild tile | Chinese | `catalogued` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/06-beijing-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/06-beijing-style/) |
| **Chinese archaic** — c. 1890, Wilkinson | Roots / ancestral | `documented` | `corroborated` | [`01-proto-mahjong/01-chinese-archaic`](01-proto-mahjong/01-chinese-archaic/) |
| **Chinese casino style** | Chinese | `catalogued` | `single-source` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/11-chinese-casino-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/11-chinese-casino-style/) |
| **Chinese classical** — 1920s, 144 tiles | Chinese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical`](01-proto-mahjong/04-chinese-classical/) |
| **Chinese pre-classical** — Mauger, 1915 | Roots / ancestral | `documented` | `corroborated` | [`01-proto-mahjong/03-chinese-pre-classical`](01-proto-mahjong/03-chinese-pre-classical/) |
| **Duplicate mahjong** — prebuilt walls, no luck | Modern inventions (not descendants) | `documented` | `corroborated` | [`02-modern-inventions/01-duplicate-mahjong`](02-modern-inventions/01-duplicate-mahjong/) |
| **Filipino style** — 16-tile hand, honours as flowers | Southeast Asian | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/04-filipino-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/04-filipino-style/) |
| **Fujian style** — 124 tiles, winds as flowers | Chinese | `single-informant` | `single-source` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/05-fujian-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/05-fujian-style/) |
| **Fuzhou style** — 132 tiles | Chinese | `catalogued` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/04-fuzhou-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/04-fuzhou-style/) |
| **Guangdong MCR / GMCR** — 2020s | Chinese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/02-guangdong-style/01-guangdong-mcr`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/02-guangdong-style/01-guangdong-mcr/) |
| **Guangdong style** — 1980s, additive scoring | Chinese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/02-guangdong-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/02-guangdong-style/) |
| **Hong Kong old style** — 1950s, fu removed | Chinese | `documented` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/) |
| **Hong Kong Taiwanese** — HKT | Taiwanese | `catalogued` | `partial` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/03-taiwanese-style/01-hong-kong-taiwanese`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/03-taiwanese-style/01-hong-kong-taiwanese/) |
| **Houchi rules** — 1952, Amano Daizou | Japanese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/) |
| **India / Mumbai style** — rotating round rules | Western / American | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/02-india-mumbai-style`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/02-india-mumbai-style/) |
| **Israeli Mah-Jongg Association** | Western / American | `catalogued` | `single-source` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/03-israeli-mah-jongg-association`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/03-israeli-mah-jongg-association/) |
| **Japanese classical / arushiiaru** — 1929 | Japanese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/) |
| **Korean traditional** — 104 tiles, no bamboo | Korean | `placeholder` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/03-korean-traditional`](01-proto-mahjong/04-chinese-classical/03-korean-traditional/) |
| **Late Qing style** — c. 1903, Li Boyuan | Roots / ancestral | `documented` | `corroborated` | [`01-proto-mahjong/02-late-qing-style`](01-proto-mahjong/02-late-qing-style/) |
| **Macau simplificado** — 112 tiles, hold 4 | Chinese | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/09-macau-simplificado`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/09-macau-simplificado/) |
| **Mahjong Masters Millions** | Modern inventions (not descendants) | `catalogued` | `corroborated` | [`02-modern-inventions/03-mahjong-masters-millions`](02-modern-inventions/03-mahjong-masters-millions/) |
| **Mainland regionals** | Chinese | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/) |
| **Malaysian 3-player** — 84 tiles, one suit | Southeast Asian | `catalogued` | `partial` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/02-malaysian-3-player`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/02-malaysian-3-player/) |
| **Malaysian 4-player** — 164 tiles, 24 flowers | Southeast Asian | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/03-malaysian-4-player`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/03-malaysian-4-player/) |
| **MCR / Chinese official** — 1998, Guobiao | Chinese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/05-mcr-chinese-official`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/05-mcr-chinese-official/) |
| **MCR scoring reference** | Chinese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/05-mcr-chinese-official/01-mcr-scoring-reference`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/05-mcr-chinese-official/01-mcr-scoring-reference/) |
| **Mhing** — card version | Modern inventions (not descendants) | `catalogued` | `corroborated` | [`02-modern-inventions/02-mhing`](02-modern-inventions/02-mhing/) |
| **Modern HKOS** — 3-faan minimum, 1970s | Chinese | `documented` | `partial` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/01-modern-hkos`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/01-modern-hkos/) |
| **Modern inventions** — not descendants | Modern inventions (not descendants) | `catalogued` | `unsupported` | [`02-modern-inventions`](02-modern-inventions/) |
| **Modern riichi / yonma** — red fives, 1970 | Japanese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/01-modern-riichi-yonma`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/01-modern-riichi-yonma/) |
| **Modern rules** — 1967, ura dora, oka, bazoro | Japanese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/) |
| **Nanjing style** — dragons as flowers | Chinese | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/07-nanjing-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/07-nanjing-style/) |
| **Nanyang variants** — descent disputed | Southeast Asian | `disputed` | `unsupported` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/) |
| **Nepalese** — 11-tile winning hand | Western / American | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/04-nepalese`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/04-nepalese/) |
| **NMJL card** — 1937, annual hand list | Western / American | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/) |
| **Pong** — Malaya, 120 tiles, Dobree 1955 | Southeast Asian | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/06-pong-malaya`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/06-pong-malaya/) |
| **Proto-mahjong** — c. 1870s, rules lost | Roots / ancestral | `lost` | `corroborated` | [`01-proto-mahjong`](01-proto-mahjong/) |
| **Pusser's Bones** — Royal Navy | Western / American | `documented` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/05-pussers-bones`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/05-pussers-bones/) |
| **Regional US house rules** — 1920s-30s | Western / American | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/) |
| **Sanma** — 3-player riichi | Japanese | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/02-sanma`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/02-sanma/) |
| **Shanghai / Hong Kong new style** — 1920s | Chinese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/) |
| **Shenzhen style** — kongs only, poorly documented | Chinese | `single-informant` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/08-shenzhen-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/08-shenzhen-style/) |
| **Siamese Mah Jongg** — two-handed, 2015 | Western / American | `documented` | `partial` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/01-american-mah-jongg/02-siamese-mah-jongg`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/03-regional-us-house-rules/01-nmjl-card/01-american-mah-jongg/02-siamese-mah-jongg/) |
| **Sichuan / Hunan / Tibetan** — 108 tiles | Chinese | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/01-sichuan-hunan-tibetan`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/01-sichuan-hunan-tibetan/) |
| **Sichuan 72-tile game** — per Dragon Chang | Chinese | `single-informant` | `single-source` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/03-sichuan-72-tile`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/03-sichuan-72-tile/) |
| **Sichuan bloody rules** — Chengdu, 1990s | Chinese | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/02-sichuan-bloody-rules`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/02-sichuan-bloody-rules/) |
| **Singapore style** — 148 tiles, animal flowers | Southeast Asian | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/01-singapore-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/01-singapore-style/) |
| **Taiwanese style** — 16-tile hand, 1980s | Taiwanese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/03-taiwanese-style`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/03-taiwanese-style/) |
| **Tokyo rules** — 1957, 1-han minimum | Japanese | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/) |
| **Tui Dao Hu** — multiple winners | Chinese | `single-informant` | `conflicting` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/10-tui-dao-hu`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/02-mainland-regionals/10-tui-dao-hu/) |
| **Twenty Point Mah Jong** — R.F. Foster, 1924 | Western / American | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/01-twenty-point-mah-jong`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/01-twenty-point-mah-jong/) |
| **Vietnamese classical** — 160 tiles, 8 jokers | Southeast Asian | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/05-vietnamese-classical`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/05-vietnamese-classical/) |
| **Vietnamese modern** — 176+ tiles, 24+ jokers | Southeast Asian | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/05-vietnamese-classical/01-vietnamese-modern`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/04-nanyang-variants/05-vietnamese-classical/01-vietnamese-modern/) |
| **Western / British Empire style** | Western / American | `documented` | `partial` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/) |
| **WMPA / WMF** — Korean, riichi-based | Korean | `catalogued` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/03-wmpa-wmf`](01-proto-mahjong/04-chinese-classical/02-japanese-classical-arushiiaru/01-houchi-rules/01-tokyo-rules/01-modern-rules/03-wmpa-wmf/) |
| **Wright-Patterson** — USAF spouses, Ohio | Western / American | `documented` | `corroborated` | [`01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/01-wright-patterson`](01-proto-mahjong/04-chinese-classical/04-babcock-rules/02-western-british-empire-style/01-wright-patterson/) |
| **Zung Jung** — Alan Kwan, 2000s | Chinese | `documented` | `partial` | [`01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/06-zung-jung`](01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/06-zung-jung/) |

## Known limits of this tree

The chart this tree is built from is explicit about where it is weak, and those warnings belong on the front page rather than buried in a folder. Each one is written up at greater length on the site's [about page](https://compendium.pandaren.org/about/):

- **Influence ran both ways between Hong Kong and Taiwan.** Guangdong was influenced first by Hong Kong, later by Taiwanese; the arrow should run both ways.
- **The mainland branch changed its frame mid-history.** Mainland regionals began on a Chinese Classical frame and later adopted HKOS's simplified scoring.
- **Some scoring travelled backwards, from West to East.** All Pairs and All Green flowed backwards from Western Mah Jong into most other modern rulesets, meaning the `us` branch fed the `cn` branch, which no tree layout shows.
- **Eleven nodes stand in for more than a hundred games.** The eleven mainland nodes stand in for a hundred-plus real variants, most undocumented in English.
- **Three entries rest on one person's report.** Several entries (Shenzhen, Tui Dao Hu, Fujian) rest on a single informant report.
- **The Korean 104-tile game has no established parent.** No source establishes how Korean 104-tile mahjong descends from anything; the link is a placeholder.
- **Filipino style sits on a branch its hand size argues against.** Filipino style sits under Nanyang despite a 16-tile hand resembling Taiwanese. The distinguishing test is that Filipino play treats winds and dragons as flowers.

Sourcing is uneven by region rather than absent: Cantonese material is credited, most of the rest is not. Weight the tree accordingly — and weight anything filed into it accordingly too. Correcting the tree is as welcome as filling it.
