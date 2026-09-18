# `_dev/`

Everything to do with building and maintaining this repository, kept out of the
folders a reader traverses. Nothing in here is source material about mahjong —
it is the scaffolding that produced the folder tree.

| Path | What it is |
| --- | --- |
| [`CONVENTIONS.md`](CONVENTIONS.md) | How files are filed, named and logged; the provenance vocabulary |
| [`source-chart/`](source-chart/) | The variant family tree chart this repository's structure is built from, and the text extracted from it |
| [`data/`](data/) | The chart's contents as data: the node tree, the bibliography, the chart's own caveats |
| [`scripts/`](scripts/) | The extraction and generation scripts |

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

## Re-reading the source chart

```sh
python3 _dev/scripts/extract_chart.py > _dev/source-chart/extracted-text.txt
```

The chart is a vector PDF with no tagged text, so the tree has to be read back
out of its content stream: indentation is each label's x coordinate, family
grouping is its fill colour, and a disputed descent is a connector drawn with a
dash pattern. The script prints one line per text run as
`y, x, family, flag, label`, which is what `data/nodes.tsv` was checked against.

Two connectors in the chart are dashed — under **Nanyang variants** and
**Korean traditional** — and both are marked `disputed` / `placeholder` in the
data.
