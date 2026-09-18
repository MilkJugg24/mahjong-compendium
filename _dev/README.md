# `_dev/`

Everything to do with building and maintaining this repository, kept out of the
folders a reader traverses. Nothing in here is source material about mahjong —
it is the scaffolding that produced the folder tree.

| Path | What it is |
| --- | --- |
| [`CONVENTIONS.md`](CONVENTIONS.md) | How files are filed, named and logged; the provenance vocabulary |
| [`source-chart/`](source-chart/) | The variant family tree chart this repository's structure is built from: the author's Markdown export (authoritative), the original PDF, and the text extracted from that PDF |
| [`data/`](data/) | The chart's contents as data: the node tree, the bibliography, the chart's own caveats, and the cross-comparison claims |
| [`scripts/`](scripts/) | The extraction and generation scripts |

## The cross-comparison pass

[`data/claims.json`](data/claims.json) holds, per variant, what each source was
read to say and a verdict on the state of the sourcing. It drives the
`## Cross-comparison` section in every variant README and the whole of
[`FINDINGS.md`](../FINDINGS.md).

Sources were fetched with `curl` and rendered to text locally. Three sites answer
automated requests with a Cloudflare challenge and could not be read at all
(riichi.wiki, mahjongg.org, BoardGameGeek); two more are served over HTTP or with
an expired certificate and were read through the Wayback Machine, as was the
Mahjong Wiki. Raw fetched pages are deliberately **not** committed: this
repository keeps extracted claims with attribution, not wholesale copies of other
people's pages.

Nothing enters `claims.json` that was not read at its source. A search-result
summary is a lead, not evidence — see [`CONVENTIONS.md`](CONVENTIONS.md).

## Regenerating the tree

```sh
python3 _dev/scripts/generate_structure.py
```

This rewrites every variant `README.md`, the root `README.md` and
`REFERENCES.md` from `_dev/data/`. It is safe to rerun: a variant README is only
rewritten *above* its `## Collected files` heading, so anything logged in that
table by hand survives. It never touches collected files themselves.

To add, rename or re-parent a variant, edit
[`data/nodes.tsv`](data/nodes.tsv) and rerun. Note that renaming a variant
changes its folder name; move the existing folder yourself first, then rerun, or
the old folder will be left behind alongside the new one.

## The source chart, and checking against it

`source-chart/` holds two forms of the same chart. The Markdown export,
`mahjong-variant-family-tree.md`, is authoritative: it carries the node table
with each variant's canonical source, which the PDF does not. To check the
repository against it:

```sh
python3 _dev/scripts/verify_against_export.py
```

That compares every node's label, depth, family, parent and disputed flag, and
every reference's URL, against the export, and exits non-zero on any
difference. Run it after editing `data/`.

The PDF came first and is kept as the original artefact. It is a vector PDF with no tagged text, so the tree has to be read back
out of its content stream: indentation is each label's x coordinate, family
grouping is its fill colour, and a disputed descent is a connector drawn with a
dash pattern:

```sh
python3 _dev/scripts/extract_chart.py > _dev/source-chart/extracted-text.txt
```

It prints one line per text run as `y, x, family, flag, label`. The tree was
first built from this, then verified against the Markdown export.

Two connectors in the chart are dashed — under **Nanyang variants** and
**Korean traditional** — and both are marked `disputed` / `placeholder` in the
data.
