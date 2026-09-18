---
title: Mahjong variant family tree
description: Roughly 55 documented mahjong rulesets and their lineages, with sources and provenance notes
node_count: 61
families: [roots, cn, tw, sea, jp, kr, us]
compiled: 2026-09-13
sources_retrieved: 2026-09-13
primary_frameworks: [sloperama-faq-2b, wikidot-home]
---

# Mahjong variant family tree

Roughly 55 documented rulesets. Indentation and the `parent` column show descent.
Links marked `disputed: yes` have no source establishing the parentage.

## Family codes

| code | family | notes |
|---|---|---|
| `roots` | Roots / ancestral | Pre-1920s forms, plus modern non-descendant inventions |
| `cn` | Chinese | Mainland, Hong Kong, Cantonese, and competition standards |
| `tw` | Taiwanese | 16-tile structural fork |
| `sea` | Southeast Asian | Nanyang group; parentage disputed |
| `jp` | Japanese | Classical through modern riichi |
| `kr` | Korean | Traditional 104-tile, and the riichi-derived WMPA ruleset |
| `us` | Western / American | Babcock descent, British Empire style, NMJL line |

## Tree

- **Proto-mahjong** (c. 1870s, rules lost) `roots`
  - **Chinese archaic** (c. 1890, Wilkinson) `roots`
  - **Late Qing style** (c. 1903, Li Boyuan) `roots`
  - **Chinese pre-classical** (Mauger, 1915) `roots`
  - **Chinese classical** (1920s, 144 tiles) `cn`
    - **Shanghai / Hong Kong new style** (1920s) `cn`
      - **Hong Kong old style** (1950s, fu removed) `cn`
        - **Modern HKOS** (3-faan minimum, 1970s) `cn`
        - **Guangdong style** (1980s, additive scoring) `cn`
          - **Guangdong MCR / GMCR** (2020s) `cn`
        - **Taiwanese style** (16-tile hand, 1980s) `tw`
          - **Hong Kong Taiwanese (HKT)** `tw`
        - **Nanyang variants** (descent disputed) `sea` — *disputed link*
          - **Singapore style** (148 tiles, animal flowers) `sea`
          - **Malaysian 3-player** (84 tiles, one suit) `sea`
          - **Malaysian 4-player** (164 tiles, 24 flowers) `sea`
          - **Filipino style** (16-tile hand, honours as flowers) `sea`
            - **Bashi-Bashi** (3-player, Philippine casinos) `sea`
          - **Vietnamese classical** (160 tiles, 8 jokers) `sea`
            - **Vietnamese modern** (176+ tiles, 24+ jokers) `sea`
          - **Pong** (Malaya, 120 tiles, Dobree 1955) `sea`
        - **MCR / Chinese official** (1998, Guobiao) `cn`
          - **MCR scoring reference** `cn`
        - **Zung Jung** (Alan Kwan, 2000s) `cn`
      - **Mainland regionals** `cn`
        - **Sichuan / Hunan / Tibetan** (108 tiles) `cn`
        - **Sichuan bloody rules** (Chengdu, 1990s) `cn`
        - **Sichuan 72-tile game** (per Dragon Chang) `cn`
        - **Fuzhou style** (132 tiles) `cn`
        - **Fujian style** (124 tiles, winds as flowers) `cn`
        - **Beijing style** (drawn wild tile) `cn`
        - **Nanjing style** (dragons as flowers) `cn`
        - **Shenzhen style** (kongs only, poorly documented) `cn`
        - **Macau simplificado** (112 tiles, hold 4) `cn`
        - **Tui Dao Hu** (multiple winners) `cn`
        - **Chinese casino style** `cn`
    - **Japanese classical / arushiiaru** (1929) `jp`
      - **Houchi rules** (1952, Amano Daizou) `jp`
        - **Tokyo rules** (1957, 1-han minimum) `jp`
          - **Modern rules** (1967, ura dora, oka, bazoro) `jp`
            - **Modern riichi / yonma** (red fives, 1970) `jp`
            - **Sanma** (3-player riichi) `jp`
            - **WMPA / WMF** (Korean, riichi-based) `kr`
    - **Korean traditional** (104 tiles, no bamboo) `kr` — *disputed link*
    - **Babcock rules** (1920, the little red book) `us`
      - **Twenty Point Mah Jong** (R.F. Foster, 1924) `us`
      - **Western / British Empire style** `us`
        - **Wright-Patterson** (USAF spouses, Ohio) `us`
        - **India / Mumbai style** (rotating round rules) `us`
        - **Israeli Mah-Jongg Association** `us`
        - **Nepalese** (11-tile winning hand) `us`
        - **Pusser's Bones** (Royal Navy) `us`
      - **Regional US house rules** (1920s–30s) `us`
        - **NMJL card** (1937, annual hand list) `us`
          - **American mah jongg** (152 tiles, jokers 1961) `us`
            - **AMJA card** `us`
            - **Siamese Mah Jongg** (two-handed, 2015) `us`
- **Modern inventions** (not descendants) `roots`
  - **Duplicate mahjong** (prebuilt walls, no luck) `roots`
  - **Mhing** (card version) `roots`
  - **Mahjong Masters Millions** `roots`

## Node table

Flat form of the same data, for diffing. `parent` is the slug of the immediate ancestor.

| id | name | family | parent | disputed | source |
|---|---|---|---|---|---|
| `proto-mahjong` | Proto-mahjong (c. 1870s, rules lost) | roots | — | no | sloperama-faq-11 |
| `chinese-archaic` | Chinese archaic (c. 1890, Wilkinson) | roots | `proto-mahjong` | no | sloperama-analysis |
| `late-qing` | Late Qing style (c. 1903, Li Boyuan) | roots | `proto-mahjong` | no | sloperama-analysis |
| `chinese-pre-classical` | Chinese pre-classical (Mauger, 1915) | roots | `proto-mahjong` | no | sloperama-analysis |
| `chinese-classical` | Chinese classical (1920s, 144 tiles) | cn | `proto-mahjong` | no | wikidot-chinese-classical |
| `shanghai-hk-new-style` | Shanghai / Hong Kong new style (1920s) | cn | `chinese-classical` | no | wikidot-hk-new-style |
| `hkos` | Hong Kong old style (1950s, fu removed) | cn | `shanghai-hk-new-style` | no | wikidot-hkos |
| `modern-hkos` | Modern HKOS (3-faan minimum, 1970s) | cn | `hkos` | no | wikipedia-hk-scoring |
| `guangdong-style` | Guangdong style (1980s, additive scoring) | cn | `hkos` | no | wikidot-guangdong |
| `gmcr` | Guangdong MCR / GMCR (2020s) | cn | `guangdong-style` | no | wikidot-gmcr |
| `taiwanese-style` | Taiwanese style (16-tile hand, 1980s) | tw | `hkos` | no | wikidot-taiwanese |
| `hkt` | Hong Kong Taiwanese (HKT) | tw | `taiwanese-style` | no | wikidot-taiwanese |
| `nanyang` | Nanyang variants (descent disputed) | sea | `hkos` | **yes** | wikidot-home |
| `singapore-style` | Singapore style (148 tiles, animal flowers) | sea | `nanyang` | no | sloperama-faq-2b |
| `malaysian-3p` | Malaysian 3-player (84 tiles, one suit) | sea | `nanyang` | no | sloperama-malaysian |
| `malaysian-4p` | Malaysian 4-player (164 tiles, 24 flowers) | sea | `nanyang` | no | sloperama-malaysian |
| `filipino-style` | Filipino style (16-tile hand, honours as flowers) | sea | `nanyang` | no | sloperama-faq-2b |
| `bashi-bashi` | Bashi-Bashi (3-player, Philippine casinos) | sea | `filipino-style` | no | sloperama-faq-2b |
| `vietnamese-classical` | Vietnamese classical (160 tiles, 8 jokers) | sea | `nanyang` | no | sloperama-faq-2b |
| `vietnamese-modern` | Vietnamese modern (176+ tiles, 24+ jokers) | sea | `vietnamese-classical` | no | sloperama-faq-2b |
| `pong-malaya` | Pong (Malaya, 120 tiles, Dobree 1955) | sea | `nanyang` | no | sloperama-faq-2b |
| `mcr` | MCR / Chinese official (1998, Guobiao) | cn | `hkos` | no | wikidot-mcr |
| `mcr-scoring` | MCR scoring reference | cn | `mcr` | no | mcr-rulebook |
| `zung-jung` | Zung Jung (Alan Kwan, 2000s) | cn | `hkos` | no | wikidot-zung-jung |
| `mainland-regionals` | Mainland regionals | cn | `shanghai-hk-new-style` | no | wikidot-mainland |
| `sichuan-108` | Sichuan / Hunan / Tibetan (108 tiles) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `sichuan-bloody` | Sichuan bloody rules (Chengdu, 1990s) | cn | `mainland-regionals` | no | wikidot-mainland |
| `sichuan-72` | Sichuan 72-tile game (per Dragon Chang) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `fuzhou-style` | Fuzhou style (132 tiles) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `fujian-style` | Fujian style (124 tiles, winds as flowers) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `beijing-style` | Beijing style (drawn wild tile) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `nanjing-style` | Nanjing style (dragons as flowers) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `shenzhen-style` | Shenzhen style (kongs only, poorly documented) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `macau-simplificado` | Macau simplificado (112 tiles, hold 4) | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `tui-dao-hu` | Tui Dao Hu (multiple winners) | cn | `mainland-regionals` | no | maque-games |
| `chinese-casino` | Chinese casino style | cn | `mainland-regionals` | no | sloperama-faq-2b |
| `japanese-classical` | Japanese classical / arushiiaru (1929) | jp | `chinese-classical` | no | wikidot-japanese-classical |
| `houchi-rules` | Houchi rules (1952, Amano Daizou) | jp | `japanese-classical` | no | chombo-club |
| `tokyo-rules` | Tokyo rules (1957, 1-han minimum) | jp | `houchi-rules` | no | chombo-club |
| `modern-rules-1967` | Modern rules (1967, ura dora, oka, bazoro) | jp | `tokyo-rules` | no | chombo-club |
| `modern-riichi` | Modern riichi / yonma (red fives, 1970) | jp | `modern-rules-1967` | no | wikidot-japanese-modern |
| `sanma` | Sanma (3-player riichi) | jp | `modern-rules-1967` | no | wikipedia-japanese-mahjong |
| `wmpa-wmf` | WMPA / WMF (Korean, riichi-based) | kr | `modern-rules-1967` | no | sloperama-faq-2b |
| `korean-traditional` | Korean traditional (104 tiles, no bamboo) | kr | `chinese-classical` | **yes** | sloperama-faq-2b |
| `babcock-rules` | Babcock rules (1920, the little red book) | us | `chinese-classical` | no | sloperama-faq-2b |
| `twenty-point` | Twenty Point Mah Jong (R.F. Foster, 1924) | us | `babcock-rules` | no | sloperama-faq-2b |
| `western-british` | Western / British Empire style | us | `babcock-rules` | no | sloperama-faq-2b |
| `wright-patterson` | Wright-Patterson (USAF spouses, Ohio) | us | `western-british` | no | mahjong-line |
| `india-mumbai` | India / Mumbai style (rotating round rules) | us | `western-british` | no | sloperama-faq-2b |
| `israeli-mja` | Israeli Mah-Jongg Association | us | `western-british` | no | sloperama-faq-2b |
| `nepalese` | Nepalese (11-tile winning hand) | us | `western-british` | no | sloperama-faq-2b |
| `pussers-bones` | Pusser's Bones (Royal Navy) | us | `western-british` | no | gunplot |
| `regional-us-house` | Regional US house rules (1920s–30s) | us | `babcock-rules` | no | wikipedia-american |
| `nmjl-card` | NMJL card (1937, annual hand list) | us | `regional-us-house` | no | wikidot-american |
| `american-mah-jongg` | American mah jongg (152 tiles, jokers 1961) | us | `nmjl-card` | no | wikipedia-american |
| `amja-card` | AMJA card | us | `american-mah-jongg` | no | wikipedia-american |
| `siamese-mah-jongg` | Siamese Mah Jongg (two-handed, 2015) | us | `american-mah-jongg` | no | mahjongg-org |
| `modern-inventions` | Modern inventions (not descendants) | roots | — | no | sloperama-faq-2b |
| `duplicate-mahjong` | Duplicate mahjong (prebuilt walls, no luck) | roots | `modern-inventions` | no | mil-duplicate |
| `mhing` | Mhing (card version) | roots | `modern-inventions` | no | sloperama-faq-2b |
| `mahjong-masters-millions` | Mahjong Masters Millions | roots | `modern-inventions` | no | sloperama-faq-2b |

## Structural caveats

Solid links follow the Mahjong Wiki family tree and timeline, cross-checked against Tom Sloper's
FAQ 2b variant catalogue. Disputed links are marked in the table above.

Known distortions in any tree layout of this material:

- Guangdong was influenced first by Hong Kong, later by Taiwanese; the arrow should run both ways.
- Mainland regionals began on a Chinese Classical frame and later adopted HKOS's simplified scoring.
- All Pairs and All Green flowed backwards from Western Mah Jong into most other modern rulesets,
  meaning the `us` branch fed the `cn` branch, which no tree layout shows.
- The eleven mainland nodes stand in for a hundred-plus real variants, most undocumented in English.
- Several entries (Shenzhen, Tui Dao Hu, Fujian) rest on a single informant report.
- No source establishes how Korean 104-tile mahjong descends from anything; the link is a placeholder.
- Filipino style sits under Nanyang despite a 16-tile hand resembling Taiwanese. The distinguishing
  test is that Filipino play treats winds and dragons as flowers.

## References

### Variant catalogues and lineage frameworks

1. **Sloper, Tom. "FAQ 2b: Identifying a Mah-Jongg Variant." Sloperama.** — Tile counts, hand sizes, flower handling and scoring for roughly 50 named variants. Primary source for most leaf nodes in this chart. <https://www.sloperama.com/mjfaq/mjfaq02b.html> `id: sloperama-faq-2b`
2. **Sloper, Tom. "The Mah-Jongg Family Tree." Sloperama.** — Illustrated tree; source for the Matiao / Khanhoo / dominoes root structure. <https://www.sloperama.com/mjfaq/tree.htm> `id: sloperama-tree`
3. **Sloper, Tom. "FAQ 11: History of Mah-Jongg." Sloperama.** — Regional branching in the 1930s and 40s; Racster 1924 on Shanghai versus Hong Kong base scores; the author's own note that the tree illustration predates later findings. <https://www.sloperama.com/mjfaq/mjfaq11f.html> `id: sloperama-faq-11`
4. **Sloper, Tom. "Comparative Analysis of Early Mah-Jongg Forms." Sloperama.** — Chinese Archaic, Late Qing and Pre-Classical rule comparisons. <https://www.sloperama.com/mahjongg/analysis.html> `id: sloperama-analysis`
5. **Sloper, Tom. "Malaysian Mah-Jongg." Sloperama.** — The 84-tile three-player and 164-tile four-player Malaysian games. <https://www.sloperama.com/mahjongg/malaysian.html> `id: sloperama-malaysian`
6. **Sloper, Tom. "FAQ 22: Chinese Official Scoring Explained." Sloperama.** — Confirms the 1998 People's Sports Publishing House edition of the competition rules. <https://sloperama.com/mjfaq/mjfaq22.html> `id: sloperama-faq-22`
7. **Mahjong Wiki. "Family Tree and Timeline." mahjong.wikidot.com.** — The decade-by-decade timeline and the branch structure this chart follows, including the caveat that each variant's evolution has been cross-cultural. <http://mahjong.wikidot.com/> `id: wikidot-home`
8. **Mahjong Wiki. "Hong Kong Old Style Overview."** — The 1950s simplification, removal of fu, the 1970s 3-3 system, and the late-1980s split into Taiwanese and Guangdong styles. <http://mahjong.wikidot.com/rules:hong-kong-old-style-overview> `id: wikidot-hkos`
9. **Mahjong Wiki. "Chinese Official (MCR) Overview."** — 1998 release; the 1996 PRC push for sport recognition; Cantonese objections around the handover. <http://mahjong.wikidot.com/rules:chinese-official-overview> `id: wikidot-mcr`

### Japanese lineage

10. **Yuria (Hassouhatsu Club). "A Brief History of Japanese Mahjong." Kraków Chombo Club, 2 Aug 2026.** — Arushiiaru rules and scoring; Amano Daizou; the Houchi Shinbun serial of 11 Nov – 5 Dec 1952; the 1957 Tokyo rules and 1967 modern rules; bazoro; the Federation's 2016 acceptance of riichi. <https://chombo.club/en/blog/2026/08/02/a-brief-history-of-japanese-mahjong/> `id: chombo-club`
11. **Japanese Mahjong Wiki. "Japanese Mahjong." riichi.wiki.** — Arrival in Japan in 1909; the post-1969 popularity surge; Tenhou.net in 2007. <https://riichi.wiki/index.php?title=Japanese_mahjong> `id: riichi-wiki`
12. **Wikipedia. "Japanese Mahjong."** — The riichi declaration, dora, furiten and ordered discards. <https://en.wikipedia.org/wiki/Japanese_mahjong> `id: wikipedia-japanese-mahjong`

### Western and American lineage

13. **Wikipedia. "American Mahjong."** — Racks, jokers, the Charleston, and the NMJL / AMJA annual card. <https://en.wikipedia.org/wiki/American_mahjong> `id: wikipedia-american`
14. **MahjongCompare. "Mahjong History and Origin."** — NMJL founders (Cecil, Meyerson, Jacobs, Potter), the 1937 Essex House meeting, and jokers entering the official rules in 1961. <https://mahjongcompare.com/history> `id: mahjong-compare`
15. **The Mahjong Line. "History of the Game."** — Wright-Patterson origins among Air Force officers' spouses at Wright Field, Ohio. <https://themahjongline.com/pages/history> `id: mahjong-line`
16. **The Charleston Club. "The History of American Mah Jongg."** — Babcock's 1920 translation and the Parker Brothers / Milton Bradley licensing. <https://thecharlestonclubaz.com/blogs/the-journal/the-history-of-american-mah-jongg-from-1920s-import-to-a-century-old-american-tradition> `id: charleston-club`
17. **Grokipedia. "American Mahjong."** — Jokers appearing in sets from the 1940s; the NMJL mandate from the 1960–61 season. <https://grokipedia.com/page/American_mahjong> `id: grokipedia-american`

### Chinese competition rules

18. **Wikipedia. "Hong Kong Mahjong Scoring Rules."** — Faan scoring, the common 3-faan minimum and the 13-faan ceiling. <https://en.wikipedia.org/wiki/Hong_Kong_mahjong_scoring_rules> `id: wikipedia-hk-scoring`
19. **Wikipedia. "World Mahjong Championship."** — Mahjong certified as China's 255th sport in January 1998; unified rules codified that September. <https://en.wikipedia.org/wiki/World_Mahjong_Championship> `id: wikipedia-wmc`
20. **World Mahjong Organization. Mahjong Competition Rules, English edition.** — The 1998 ruleset itself. <http://mahjong-europe.org/portal/images/docs/mcr_EN.pdf> `id: mcr-rulebook`
21. **The World of Chinese. "Tales of the Tile," November 2019.** — The 1998 State Sports Commission publication of the Guobiao rules; WMO founded 2006. <https://www.theworldofchinese.com/2019/11/tales-of-the-tile/> `id: world-of-chinese`

### Individual variants

22. **Mahjong International League. "Duplicate Mahjong Rules."** — Prebuilt walls intended to remove luck for mind-sport recognition. <http://mahjong-mil.org/rules_dup.html> `id: mil-duplicate`
23. **Grad, Gladys. Siamese Mah Jongg. mahjongg.org.** — The two-handed variant, 2015. <https://mahjongg.org/> `id: mahjongg-org`
24. **maque.games. "Tui Dao Hu."** — Twelve ways of going out; more than one player may win. <https://maque.games/post/323/> `id: maque-games`
25. **Gunplot. "Pusser's Mahjongg (Pusser's Bones)."** — The Royal Navy adaptation of the Western game. <http://www.gunplot.net/mahjongg/mahjongg2.html> `id: gunplot`
26. **Stanwick, Michael and Hongbing Xu. "Flowers and Kings." themahjongtileset.co.uk.** — Early ma que tile-set research underlying the Hua Maque and Wang Maque material. <http://www.themahjongtileset.co.uk/tile-set-history/flowers-and-kings-an-hypothesis-of-their-function-in-early-ma-que/> `id: stanwick-xu`

### Additional wiki pages referenced by node rows

| id | page | url |
|---|---|---|
| `wikidot-chinese-classical` | Chinese Classical Overview | <http://mahjong.wikidot.com/rules:chinese-classical-overview> |
| `wikidot-hk-new-style` | Hong Kong New Style Overview | <http://mahjong.wikidot.com/rules:hong-kong-new-style-overview> |
| `wikidot-hkos-scoring` | Hong Kong Old Style Scoring | <http://mahjong.wikidot.com/rules:hong-kong-old-style-scoring> |
| `wikidot-guangdong` | Guangdong Style Overview | <http://mahjong.wikidot.com/rules:guangdong-style-overview> |
| `wikidot-gmcr` | Guangdong MCR Overview | <http://mahjong.wikidot.com/rules:gmcr-overview> |
| `wikidot-taiwanese` | Taiwanese Overview | <http://mahjong.wikidot.com/rules:taiwanese-overview> |
| `wikidot-zung-jung` | Zung Jung Overview | <http://mahjong.wikidot.com/rules:zung-jung-overview> |
| `wikidot-mainland` | Mainland Mahjong Overview | <http://mahjong.wikidot.com/rules:mainland-mahjong-overview> |
| `wikidot-japanese-classical` | Japanese Classical Overview | <http://mahjong.wikidot.com/rules:japanese-classical-overview> |
| `wikidot-japanese-modern` | Japanese Modern Overview | <http://mahjong.wikidot.com/rules:japanese-modern-overview> |
| `wikidot-american` | American Overview | <http://mahjong.wikidot.com/rules:american-overview> |
| `wikidot-western` | Western Mah Jong Scoring | <http://mahjong.wikidot.com/rules:western-mah-jong-scoring> |

### Primary sources cited within the above, not consulted directly

Wilkinson (c. 1889–95) on Chinese Archaic rules and Kun Pai cards; Culin (1924) on Khanhoo;
Li Boyuan, *Officialdom Unmasked* (1903–05); Mauger (1915); J.P. Babcock, *Rules for Mah-Jongg* (1920);
Olga Racster (1924); R.F. Foster, *Twenty Point Mah Jong* (1924); C.T. Dobree, *Gambling Games of Malaya*
(1955); Amano Daizou's rules serialised in *Houchi Shinbun* (Nov–Dec 1952); and *Chinese Mahjong
Competition Rules*, People's Sports Publishing House (1998), ISBN 7-5009-1630-2.

All web sources retrieved 13 September 2026. Where Sloperama and the Mahjong Wiki disagree, this chart
follows the Mahjong Wiki, whose material is more recent. Tile counts and hand sizes come from Sloperama,
the only catalogue that records them systematically.

---

## Appendix: where the Mahjong Wiki's information comes from

The Mahjong Wiki supplies the lineage structure of this chart, and it carries no bibliography, no about
page, and no per-claim citations. It is also a rebuild: the author states the earlier wiki had become
extremely outdated and links an archived snapshot of it. What follows is an attempt to trace the material
anyway. None of this is confirmed by the author. It is the set of sources the wiki's distinctive claims
can be matched to, plus an honest account of what cannot be traced at all.

### What the wiki itself credits

- The Hong Kong Old Style scoring page is the only page that names anything. It sets its fan lists out in
  three labelled columns: HKOS, "Let's Mahjong!", and "Perlmen & Chan".
- The same page appeals to "several Cantonese sources" without naming them, saying they agree that the
  conditions in "Let's Mahjong!" represent the New Chapter standard.
- It names three Cantonese fan-list traditions with almost no English-language presence: New6 (六獨),
  New18 (十八番), and a larger uncodified set the Hong Kong New Style page calls 無奇不有.
- Its core taxonomy, Clear Chapter (清章) and New Chapter (新章), is Cantonese terminology rather than a
  Western coinage. This is the strongest single sign that the author works from Cantonese material.
- It credits Alan Kwan for Zung Jung, and names British Mahjong as the origin of several imported fan,
  including the Jewel Dragons and Seven Pairs.
- Its diagrams are served from a Blogger account, so the author keeps a blog; the wiki never links it.

### Sources the wiki names or can be matched to

27. **Perlmen, Samuel K. and Mark Kai-Chi Chan. *The Chinese Game of Mahjong*. Book Marketing Ltd., Hong Kong, 1979. ISBN 962-211-0169.** — The only book the wiki cites by name, used as a whole fan-list column. Sloper's book FAQ describes it as covering both Old Style and New Style as played in Hong Kong, which is precisely the distinction the wiki's taxonomy is built on. This is the likeliest backbone of its HKOS material. <https://www.goodreads.com/book/show/658815.The_Chinese_Game_of_Mahjong> `id: perlmen-chan-1979`
28. **"Let's Mahjong!" ruleset, as tabulated on the Mahjong Wiki HKOS scoring page.** — Cited as a second fan-list column and treated as the representative New Chapter standard. The wiki describes it as the transition from HKOS to Guangdong Style. It is a ruleset, not a scholarly source, and the wiki gives no publication details for it. <http://mahjong.wikidot.com/rules:hong-kong-old-style-scoring> `id: lets-mahjong`
29. **Cantonese fan lists: New6 (六獨), New18 (十八番), and 無奇不有.** — Named on the HKOS and Hong Kong New Style pages. These are traditions internal to Hong Kong play. The wiki's own caveat is that NEW18 may not in fact be standardised at all. <http://mahjong.wikidot.com/rules:hong-kong-new-style-overview> `id: cantonese-fan-lists`
30. **Kwan, Alan. Zung Jung scoring system.** — Named on the wiki and independently documented; the World Series of Mahjong used a modified form of it. <http://mahjong.wikidot.com/rules:zung-jung-overview> `id: kwan-zung-jung`
31. **Chinese Mahjong Competition Rules, People's Sports Publishing House, 1998.** — Underlies the wiki's MCR pages, though it cites no edition. <http://mahjong-europe.org/portal/images/docs/mcr_EN.pdf> `id: cmcr-1998`
32. **British Mahjong scoring, as tabulated on the wiki's own Western Mah Jong page.** — The wiki attributes All Green, Seven Pairs and the Jewel Dragons to this tradition flowing back into Chinese rulesets. No book is named. <http://mahjong.wikidot.com/rules:western-mah-jong-scoring> `id: british-mahjong-scoring`
33. **Archived earlier version of the Mahjong Wiki, 30 March 2025.** — The author's own predecessor site, linked from the current front page. Useful for seeing which claims are new to the rebuild and which were carried over. <https://web.archive.org/web/20250330002121/http://mahjong.wikidot.com/> `id: wikidot-archive-2025`

### What remains untraceable

- The decade-by-decade timeline, which is the single most load-bearing thing this chart takes from the
  wiki, carries no citation on any page. The 1950s gambling-house adoption of Clear Chapter, the 1970s
  3-3 system, and the late-1980s move to additive scoring are asserted and never sourced.
- The Japanese pages cite nothing whatsoever. One glossary entry still reads "[coming soon]".
- The Nanyang, Korean and mainland claims carry no sources either, which is at least consistent with the
  wiki openly flagging those as unresolved questions rather than presenting them as settled.
- Sourcing is therefore uneven by region, not absent: Cantonese material is credited, everything else is
  not. Weight the wiki accordingly, and weight this chart accordingly.

### Where to check the wiki independently

34. **Sloper, Tom. "FAQ 3: Books About Mah-Jongg."** — Identifies Perlmen & Chan in full and lists the other Hong Kong Old Style books: Constantino, Li, Tsui, Lo. <https://sloperama.com/mjfaq/mjfaq03.html> `id: sloperama-faq-3`
35. **rec.games.mahjong newsgroup archive.** — Where much of the English-language variant research was originally argued out, and the origin of several single-informant reports in Sloper's catalogue. <https://groups.google.com/g/rec.games.mahjong> `id: rec-games-mahjong`
36. **Tsui, Cofa. *International Mahjong Rules*, 1998.** — An independent Hong Kong Old Style codification, useful as a check on the wiki's fan tables. <http://www.cofatsui.com/mahjong.html> `id: cofa-tsui`
37. **Cantonese Wikipedia: 香港麻雀.** — Cantonese-language treatment of the Hong Kong game, in the register the wiki appears to draw from. <https://zh-yue.wikipedia.org/wiki/%E9%A6%99%E6%B8%AF%E9%BA%BB%E9%9B%80> `id: yue-wikipedia-hk-mahjong`
38. **Chinese Wikipedia: 香港麻雀胡牌列表.** — Hong Kong winning-hand list, a direct comparison point for the wiki's NEW6 and NEW18 tables. <https://zh.wikipedia.org/zh-hant/%E9%A6%99%E6%B8%AF%E9%BA%BB%E9%9B%80%E8%83%A1%E7%89%8C%E5%88%97%E8%A1%A8> `id: zh-wikipedia-hk-hands`
