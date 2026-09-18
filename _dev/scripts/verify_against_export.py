#!/usr/bin/env python3
"""Check the repository's data against the chart author's Markdown export.

Compares every node's label, depth, family, parent and disputed flag, and every
reference's URL and slug, against _dev/source-chart/mahjong-variant-family-tree.md.
Exits non-zero if anything differs, so it can gate a change to _dev/data/.

Usage:  python3 _dev/scripts/verify_against_export.py
"""
import csv
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "_dev", "data")
EXPORT = os.path.join(ROOT, "_dev", "source-chart", "mahjong-variant-family-tree.md")

FAMILY = {
    "roots": "roots", "cn": "chinese", "tw": "taiwanese", "sea": "southeast-asian",
    "jp": "japanese", "kr": "korean", "us": "western-american",
}


def norm(text):
    """Compare on content, not on typography: dashes, quotes, accents, emphasis."""
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("–", "-").replace("—", "-").replace("’", "'")
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", text.replace("*", "")).strip()


def export_nodes(md):
    """The export states the tree twice; both forms are parsed and cross-checked."""
    tree = []
    section = md.split("## Tree", 1)[1].split("## Node table", 1)[0]
    for line in section.splitlines():
        m = re.match(r"^(\s*)- \*\*(.+?)\*\*(.*)$", line)
        if not m:
            continue
        detail = re.match(r"\s*\(([^)]*)\)", m.group(3))
        family = re.search(r"`(\w+)`", m.group(3))
        tree.append({
            "depth": len(m.group(1)) // 2,
            "name": norm(m.group(2) + (f" ({detail.group(1)})" if detail else "")),
            "family": FAMILY[family.group(1)],
            "disputed": "disputed link" in m.group(3),
        })

    table = []
    section = md.split("## Node table", 1)[1].split("## Structural caveats", 1)[0]
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        table.append({
            "alias": cells[0].strip("`"), "name": norm(cells[1]), "family": FAMILY[cells[2]],
            "parent": cells[3].strip("` ") if cells[3] != "—" else None,
            "disputed": "yes" in cells[4], "source": cells[5].strip("`"),
        })
    return tree, table


def repo_nodes():
    with open(os.path.join(DATA, "nodes.tsv")) as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    stack = {}
    for r in rows:
        r["depth"] = int(r["depth"])
        r["name"] = norm(r["label"] + (f' ({r["detail"]})' if r["detail"] else ""))
        parent = stack.get(r["depth"] - 1)
        r["parent_name"] = parent["name"] if parent else None
        stack[r["depth"]] = r
        for deeper in [d for d in stack if d > r["depth"]]:
            del stack[deeper]
    return rows


def main():
    md = open(EXPORT).read()
    tree, table = export_nodes(md)
    rows = repo_nodes()
    problems = []

    if not len(tree) == len(table) == len(rows):
        problems.append(f"node counts differ: export tree {len(tree)}, "
                        f"export table {len(table)}, repo {len(rows)}")
    else:
        by_alias = {t["alias"]: t for t in table}
        for t, e, r in zip(tree, table, rows):
            where = r["slug"]
            if t["name"] != e["name"]:
                problems.append(f"{where}: export disagrees with itself, "
                                f"{t['name']!r} vs {e['name']!r}")
            if r["name"] != e["name"]:
                problems.append(f"{where}: name {r['name']!r} != export {e['name']!r}")
            if r["depth"] != t["depth"]:
                problems.append(f"{where}: depth {r['depth']} != export {t['depth']}")
            if r["family"] != e["family"]:
                problems.append(f"{where}: family {r['family']} != export {e['family']}")
            if r["alias"] != e["alias"]:
                problems.append(f"{where}: chart id {r['alias']} != export {e['alias']}")
            if r["source"] != e["source"]:
                problems.append(f"{where}: canonical source {r['source']} != export {e['source']}")
            expected_parent = by_alias[e["parent"]]["name"] if e["parent"] else None
            if r["parent_name"] != expected_parent:
                problems.append(f"{where}: parent {r['parent_name']!r} != export {expected_parent!r}")
            is_disputed = r["confidence"] in ("disputed", "placeholder")
            if is_disputed != e["disputed"]:
                problems.append(f"{where}: disputed {is_disputed} != export {e['disputed']}")

    refs = json.load(open(os.path.join(DATA, "references.json")))["references"]
    numbered = re.findall(
        r"^(\d+)\. \*\*(.+?)\*\* — (.+?) <(\S+?)> `id: ([\w-]+)`", md, re.M)
    wiki = re.findall(r"^\| `([\w-]+)` \| (.+?) \| <(\S+?)> \|", md, re.M)
    expected = {int(n): (url, slug) for n, _c, _n, url, slug in numbered}
    expected.update({39 + i: (url, slug) for i, (slug, _p, url) in enumerate(wiki)})
    if len(refs) != len(expected):
        problems.append(f"reference count {len(refs)} != export {len(expected)}")
    for ref in refs:
        want = expected.get(ref["id"])
        if not want:
            problems.append(f"reference {ref['id']} is not in the export")
        elif (ref["url"], ref["slug"]) != want:
            problems.append(f"reference {ref['id']}: {(ref['url'], ref['slug'])} != export {want}")

    used = {n["source"] for n in rows}
    known = {r["slug"] for r in refs}
    for slug in sorted(used - known):
        problems.append(f"canonical source {slug} has no reference entry")

    if problems:
        print(f"{len(problems)} difference(s) against the export:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"{len(rows)} nodes and {len(refs)} references match the export")
    return 0


if __name__ == "__main__":
    sys.exit(main())
