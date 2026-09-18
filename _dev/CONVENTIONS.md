# Conventions

## The folder tree

One folder per variant, nested by descent, mirroring the source chart in
[`source-chart/`](source-chart/). Sibling folders are numbered in the chart's own
order, which is roughly chronological, so the numbers are part of the name:

```
01-proto-mahjong/04-chinese-classical/01-shanghai-hong-kong-new-style/01-hong-kong-old-style/
```

The nesting records **descent as the chart claims it**, not a judgement that the
claim is correct. Where the chart's own descent claim is weak, the folder's
README says so, and the glossary in the root `README.md` tags it.

Folder names are lower case, hyphenated, and derived from the variant's name
without its parenthetical detail. They are generated from
[`data/nodes.tsv`](data/nodes.tsv) — don't rename a folder without editing that
file, or the next regeneration will recreate the old one.

## Filing a collected file

1. Put the file in the folder of the variant it documents. If it covers several
   variants, file it under their nearest common ancestor rather than duplicating
   it.
2. Name it `YYYY-MM-DD-short-description.ext`, dated by when it was *retrieved*,
   not by when it was written. A file's own publication date belongs in the
   ledger, not the filename.
3. Log it in that folder's `README.md`, in the `## Collected files` table, with
   its source URL and a provenance value from the vocabulary below.
4. Keep the file as it was found. Corrections, transcriptions and reconciliations
   go in a separate file beside it, never by editing the original — the point of
   this repository is that an artefact can be checked against its origin.

If a file's origin cannot be established at all, it is still worth keeping, filed
with provenance `unknown` and whatever is known about where it came from. An
unattributed file that is honestly labelled is useful; one that is quietly
promoted to a source is not.

## What must never be filed here

Some works are live copyrighted material. This repository records **what they are
and how the game is structured around them**, and never their contents:

- **NMJL and AMJA annual cards, for any year.** No scans, no photographs, no
  transcriptions, no hand lists, no partial reproductions of a card's contents.
  That a card exists, is issued annually, costs what it costs, and that players
  must make hands from it, is history and structure, and belongs here.
- **_Mah Jongg Made Easy_ and the League's other publications.** No rulebook text.
  Describing what the book covers is fine; reproducing it is not.

This is not only about American mahjong. The Pusser's Bones rules book is
© 2023 Hot Rod Handbooks, all rights reserved, and sells commercially: its game
mechanics are recorded in that variant's cross-comparison as facts, exactly as
tile counts are for every other variant, but its text is not reproduced and the
file is not filed here.

The same principle applies to any variant's in-copyright rulebook. A file whose
value is that it *is* the copyrighted work does not belong in this repository,
however easy it would be to find elsewhere. If a file arrives that breaches this,
remove the file, keep the ledger row, and record what happened in it.

Comparative discussion is unaffected: how American mah jongg's fixed-hand
structure differs from a fan or pattern system is analysis, not reproduction.

## Provenance vocabulary

For a **collected file**, in the ledger table:

| Value | Meaning |
| --- | --- |
| `primary` | The ruleset itself, from the body that issued it |
| `facsimile` | A scan or verbatim reproduction of a primary source |
| `secondary` | Someone's description or translation of a ruleset |
| `informant` | An account of how a game is played, from a player, with no published rules behind it |
| `derived` | Assembled from other sources, including anything reconstructed here |
| `unknown` | Origin not established |

For a **variant folder**, in the README front matter and the root glossary:

| Value | Meaning |
| --- | --- |
| `documented` | A published ruleset or rule description exists and is cited |
| `catalogued` | Listed in a variant catalogue with tile counts and hand sizes, but no rules text has been verified |
| `single-informant` | The whole entry rests on one report from one person |
| `disputed` | The descent shown is contested; the chart drew this link dashed |
| `placeholder` | No source establishes the descent at all; the parent link is a guess |
| `lost` | No rules text survives |

These describe the **sources**, not the game. `placeholder` means nobody has
established where a game came from, not that the game is doubtful.

## Cross-comparison

Each variant folder's README carries a `## Cross-comparison` section, generated
from [`data/claims.json`](data/claims.json): a table of what each source actually
says about tiles, hand size, flowers, scoring and payout, the notes that do not
fit a table, and a reading of where the sources agree and disagree.

Its `evidence` verdict describes the **state of the sourcing**, which is not the
same as the `confidence` tag on the node:

| Verdict | Meaning |
| --- | --- |
| `corroborated` | Two or more independent sources agree on the defining facts |
| `partial` | Sources agree on some points and are silent or divided on others |
| `conflicting` | Sources disagree materially, or one source contradicts itself |
| `single-source` | Only one source was found; nothing independent confirms it |
| `unsupported` | The sources checked do not carry the claim the node makes |

Two rules govern what may go in:

1. **Only what was read at the source.** A claim from a search-result summary, or
   from a page that could not be fetched, does not go in the table. Record the
   source as unreachable instead. The whole point of the section is that a reader
   can check it.
2. **Quote or paraphrase closely, and say which source.** Where a source
   contradicts itself, record both readings rather than picking one silently.

The read across all variants is generated into [`FINDINGS.md`](../FINDINGS.md).

## Variant README structure

Generated, and regenerated in place, by
[`scripts/generate_structure.py`](scripts/generate_structure.py):

- YAML front matter: node, detail, family, confidence, parent, chart references
- Lineage trail, family, confidence
- Child variants
- The chart's caveat for this node, where it has one
- The sources the chart cites for this node, linked to `REFERENCES.md`
- `## Collected files` — the ledger, maintained by hand

Everything above `## Collected files` is generated and will be overwritten.
Everything from that heading down is yours.
