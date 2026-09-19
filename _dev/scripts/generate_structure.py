#!/usr/bin/env python3
"""Build the browsable variant folder tree from the chart data.

Reads _dev/data/nodes.tsv and _dev/data/references.json and writes:

  * one folder per chart node, nested by descent, each with a README.md
    ledger for the files collected into it
  * README.md at the repository root (the glossary)
  * REFERENCES.md at the repository root (the chart's bibliography)

Rerunning is safe: a node README is only rewritten above its "Collected files"
table, so anything logged there by hand survives regeneration.

Usage:  python3 _dev/scripts/generate_structure.py
"""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "_dev", "data")
LEDGER_HEADING = "## Collected files"

EVIDENCE = {
    "corroborated": "two or more independent sources agree on the facts that define this variant",
    "partial": "sources agree on some points and are silent or divided on others",
    "conflicting": "sources disagree materially, or one source contradicts itself",
    "single-source": "only one source was found; nothing independent confirms it",
    "unsupported": "the sources checked do not carry the claim this node makes",
}

FAMILY_NAMES = {
    "roots": "Roots / ancestral",
    "chinese": "Chinese",
    "taiwanese": "Taiwanese",
    "southeast-asian": "Southeast Asian",
    "japanese": "Japanese",
    "korean": "Korean",
    "western-american": "Western / American",
}

CONFIDENCE = {
    "documented": "a published ruleset or rule description exists and is cited below",
    "catalogued": "listed in a variant catalogue with tile counts and hand sizes, but no rules text has been verified",
    "single-informant": "the whole entry rests on one report from one person",
    "disputed": "the descent shown here is contested; the chart drew this link dashed",
    "placeholder": "no source establishes the descent at all; the parent link is a guess",
    "lost": "no rules text survives",
}

EMPTY_LEDGER = """
Collected documents live in this folder. Log each one here as it lands, so the
file's origin can be checked later. Provenance values are defined in
[`_dev/CONVENTIONS.md`]({dev}/CONVENTIONS.md).

| File | Kind | Source | Retrieved | Provenance |
| --- | --- | --- | --- | --- |
| _nothing collected yet_ | | | | |
"""


def slugged(index, slug):
    return f"{index:02d}-{slug}"


def load_nodes():
    """Return the flat node list with parent / child / path links resolved."""
    with open(os.path.join(DATA, "nodes.tsv")) as f:
        nodes = list(csv.DictReader(f, delimiter="\t"))
    refs_by_slug = {r["slug"]: r["id"] for r in
                    json.load(open(os.path.join(DATA, "references.json")))["references"]}
    claims_path = os.path.join(DATA, "claims.json")
    claims = json.load(open(claims_path)) if os.path.exists(claims_path) else {}
    for n in nodes:
        n["depth"] = int(n["depth"])
        n["children"] = []
        # The chart's node table names one canonical source per node; the rest are supporting
        # references matched by subject. The canonical one leads and is marked as such.
        n["canonical"] = refs_by_slug[n["source"]]
        supporting = [int(r) for r in n["refs"].split(",") if r and int(r) != n["canonical"]]
        n["refs"] = [n["canonical"]] + supporting

    stack = {}
    counters = {}
    for n in nodes:
        parent = stack.get(n["depth"] - 1)
        n["parent"] = parent
        key = parent["slug"] if parent else "/"
        counters[key] = counters.get(key, 0) + 1
        folder = slugged(counters[key], n["slug"])
        n["path"] = os.path.join(parent["path"], folder) if parent else folder
        if parent:
            parent["children"].append(n)
        n["claims"] = claims.get(n["slug"])
        stack[n["depth"]] = n
        for deeper in [d for d in stack if d > n["depth"]]:
            del stack[deeper]
    return nodes


def family_name(node):
    """Display name for a node's legend group.

    The chart draws the modern inventions in the same grey as the ancestral
    roots, so the colour alone would file them under "Roots / ancestral"; the
    chart's own label for that block is used instead.
    """
    if lineage(node)[0]["slug"] == "modern-inventions":
        return "Modern inventions (not descendants)"
    return FAMILY_NAMES[node["family"]]


def title(node):
    return node["label"] + (f' ({node["detail"]})' if node["detail"] else "")


def lineage(node):
    chain, cur = [], node
    while cur:
        chain.append(cur)
        cur = cur["parent"]
    return list(reversed(chain))


def refs_by_id_for(slug, refs_by_slug):
    return refs_by_slug[slug]


def node_readme(node, refs_by_id, refs_by_slug):
    depth = node["depth"] + 1
    up = "/".join([".."] * depth)
    dev = f"{up}/_dev"
    chain = lineage(node)
    trail = " → ".join(
        f"**{n['label']}**" if n is node else f"[{n['label']}]({'/'.join(['..'] * (depth - i - 1)) or '.'}/)"
        for i, n in enumerate(chain)
    )

    out = []
    out.append("---")
    out.append(f"node: {node['label']}")
    if node["detail"]:
        out.append(f"detail: {node['detail']}")
    out.append(f"family: {node['family']}")
    out.append(f"confidence: {node['confidence']}")
    out.append(f"parent: {node['parent']['label'] if node['parent'] else '(none)'}")
    out.append(f"chart_id: {node['alias']}")
    out.append(f"canonical_source: {node['source']}")
    out.append(f"chart_refs: [{', '.join(str(r) for r in node['refs'])}]")
    if node.get("claims"):
        out.append(f"evidence: {node['claims']['evidence']}")
    out.append("---")
    out.append("")
    out.append(f"# {node['label']}")
    out.append("")
    if node["detail"]:
        out.append(f"*{node['detail']}*")
        out.append("")
    out.append(f"**Lineage** · {trail}")
    out.append("")
    out.append(f"**Family** · {family_name(node)}")
    out.append("")
    out.append(
        f"**Confidence** · `{node['confidence']}` — {CONFIDENCE[node['confidence']]} "
        f"([vocabulary]({dev}/CONVENTIONS.md#provenance-vocabulary))"
    )
    out.append("")

    if node["children"]:
        out.append("## Descends into")
        out.append("")
        for c in node["children"]:
            suffix = f" — {c['detail']}" if c["detail"] else ""
            out.append(f"- [{c['label']}]({os.path.basename(c['path'])}/){suffix}")
        out.append("")

    if node["note"]:
        out.append("## Caveat from the source chart")
        out.append("")
        out.append(f"> {node['note']}")
        out.append("")

    out.append("## Sources the chart cites for this node")
    out.append("")
    if node["refs"]:
        out.append("| # | Source | URL | Role |")
        out.append("| --- | --- | --- | --- |")
        for r in node["refs"]:
            ref = refs_by_id[r]
            mark = "**canonical**" if r == node["canonical"] else "supporting"
            out.append(
                f"| [{r}]({up}/REFERENCES.md#ref-{r}) | {ref['citation']} | <{ref['url']}> | {mark} |"
            )
        out.append("")
        out.append(
            "The canonical source is the one the chart's node table names for this variant. Supporting "
            "references are matched by subject and were not attributed to it by the chart."
        )
    else:
        out.append("None. This node is grouped here for convenience, not on a cited claim.")
    out.append("")
    if node.get("claims"):
        c = node["claims"]
        out.append("## Cross-comparison")
        out.append("")
        out.append(
            f"**Evidence** · `{c['evidence']}` — {EVIDENCE[c['evidence']]}"
        )
        out.append("")
        out.append("What each source actually says, as fetched and read:")
        out.append("")
        FIELDS = ("tiles", "hand", "flowers", "scoring", "payout")
        measured = [o for o in c["observations"] if any(o.get(f) for f in FIELDS)]
        notes = [(refs_by_id_for(o["source"], refs_by_slug), o["note"])
                 for o in c["observations"] if o.get("note")]
        if measured:
            out.append("| Source | Tiles | Hand | Flowers | Scoring | Payout |")
            out.append("| --- | --- | --- | --- | --- | --- |")
            for o in measured:
                rid = refs_by_id_for(o["source"], refs_by_slug)
                label = f"[{rid}]({up}/REFERENCES.md#ref-{rid})"
                cells = [o.get(f, "") or "—" for f in FIELDS]
                out.append("| " + label + " | " + " | ".join(cells) + " |")
            out.append("")
        if notes:
            for rid, note in notes:
                out.append(f"- **[{rid}]({up}/REFERENCES.md#ref-{rid})** — {note}")
            out.append("")
        out.append("**Reading it:** " + c["assessment"])
        out.append("")
        out.append(
            f"All sources above were fetched and read on {c['observations'][0]['retrieved']}. "
            "Nothing here is second-hand: a claim that could not be read at its source is not in this table."
        )
        out.append("")
    out.append(LEDGER_HEADING)
    out.append(EMPTY_LEDGER.format(dev=dev).rstrip())
    out.append("")
    return "\n".join(out)


def write_node_readme(path, text):
    """Write the README, preserving any hand-written ledger already there."""
    if os.path.exists(path):
        existing = open(path).read()
        if LEDGER_HEADING in existing and "_nothing collected yet_" not in existing:
            text = text.split(LEDGER_HEADING)[0] + LEDGER_HEADING + existing.split(LEDGER_HEADING, 1)[1]
    with open(path, "w") as f:
        f.write(text)


def tree_block(nodes):
    lines = []
    for n in nodes:
        indent = "  " * n["depth"]
        flag = "" if n["confidence"] in ("documented", "catalogued") else f"  [{n['confidence']}]"
        lines.append(f"{indent}{title(n)}{flag}")
    return "\n".join(lines)


def root_readme(nodes, data):
    out = []
    out.append("# Mahjong Compendium")
    out.append("")
    out.append(
        "A collection of files gathered from around the web, filed by mahjong variant, so that each "
        "file's origin and legitimacy can be checked and proper rulebooks can eventually be built from "
        "material that has been verified rather than assumed."
    )
    out.append("")
    out.append(
        "The folder tree mirrors the variant family tree in "
        "[`_dev/source-chart/`](_dev/source-chart/): "
        "**one folder per variant, nested by descent**. Drop a collected file into the folder for the variant "
        "it documents, and log it in that folder's `README.md` table. Every folder's README carries the "
        "variant's lineage, the sources the chart cites for it, and how much those sources are actually worth."
    )
    out.append("")
    out.append("## How to use this repository")
    out.append("")
    out.append("| If you want to | Go to |")
    out.append("| --- | --- |")
    out.append("| Read it as a website | [compendium.pandaren.org](https://compendium.pandaren.org/) |")
    out.append("| Find the folder for a variant | The [glossary](#glossary) below |")
    out.append("| See how variants descend from each other | The [family tree](#family-tree) below |")
    out.append("| See what the sources say against each other | [`FINDINGS.md`](FINDINGS.md) |")
    out.append("| Check where a claim comes from | [`REFERENCES.md`](REFERENCES.md) |")
    out.append("| File a new document, or learn the conventions | [`_dev/CONVENTIONS.md`](_dev/CONVENTIONS.md) |")
    out.append("| See how the tree was derived from the chart | [`_dev/`](_dev/) |")
    out.append("")
    out.append(
        "Everything relating to the development of this repository — the source chart, the extracted data, "
        "and the scripts that generate the tree — lives in [`_dev/`](_dev/), separate from the folders you browse."
    )
    out.append("")
    out.append("## Confidence")
    out.append("")
    out.append(
        "Each variant folder is tagged with how good the underlying sourcing is. This is a property of the "
        "**sources**, not of the variant: a `placeholder` tag means nobody has established where the game came "
        "from, not that the game is doubtful."
    )
    out.append("")
    out.append("| Tag | Meaning | Folders |")
    out.append("| --- | --- | --- |")
    for key, meaning in CONFIDENCE.items():
        count = sum(1 for n in nodes if n["confidence"] == key)
        out.append(f"| `{key}` | {meaning} | {count} |")
    out.append("")
    out.append("## Family tree")
    out.append("")
    out.append(
        f"{len(nodes)} documented rulesets. Indentation shows descent. Two links in the source chart were drawn "
        "dashed, meaning no source establishes the descent at all: **Nanyang variants** and **Korean traditional**."
    )
    out.append("")
    out.append("```")
    out.append(tree_block(nodes))
    out.append("```")
    out.append("")
    out.append("## Glossary")
    out.append("")
    out.append("Every variant in the tree, alphabetically, with the folder that holds its files.")
    out.append("")
    out.append("| Variant | Family | Confidence | Evidence | Folder |")
    out.append("| --- | --- | --- | --- | --- |")
    for n in sorted(nodes, key=lambda n: n["label"].lower()):
        detail = f" — {n['detail']}" if n["detail"] else ""
        out.append(
            f"| **{n['label']}**{detail} | {family_name(n)} | `{n['confidence']}` | "
            f"`{n['claims']['evidence']}` | [`{n['path']}`]({n['path']}/) |"
            if n.get("claims") else
            f"| **{n['label']}**{detail} | {family_name(n)} | `{n['confidence']}` | — | "
            f"[`{n['path']}`]({n['path']}/) |"
        )
    out.append("")
    out.append("## What the source chart admits about itself")
    out.append("")
    out.append(
        "The chart this tree is built from is explicit about where it is weak, and those warnings belong on the "
        "front page rather than buried in a folder:"
    )
    out.append("")
    for line in data["distortions"]:
        out.append(f"- {line}")
    out.append("")
    out.append(
        "Sourcing is uneven by region rather than absent: Cantonese material is credited, most of the rest is not. "
        "Weight the tree accordingly — and weight anything filed into it accordingly too. Correcting the tree is "
        "as welcome as filling it."
    )
    out.append("")
    return "\n".join(out)


SMALL_WORDS = {"and", "or", "to", "the", "a", "an", "of", "in", "for", "by", "with"}


def headline(text):
    """Title-case a section heading from the chart's all-caps bibliography."""
    words = text.lower().split()
    return " ".join(
        w if 0 < i < len(words) - 1 and w in SMALL_WORDS else w.capitalize()
        for i, w in enumerate(words)
    )


def references_md(nodes, data):
    refs = data["references"]
    cited_by = {r["id"]: [] for r in refs}
    for n in nodes:
        for r in n["refs"]:
            cited_by[r].append(n)

    out = []
    out.append("# References")
    out.append("")
    out.append(
        "The bibliography of "
        "[the source chart](_dev/source-chart/mahjong-variant-family-tree.md), transcribed verbatim, with "
        "back-links to the variant folders each reference is cited for. References 1-38 are the chart's "
        "numbered bibliography; 39-50 are the Mahjong Wiki pages its node table cites directly for "
        "individual variants. All web sources were retrieved on "
        f'{data["retrieved"]} by the chart\'s author; nothing here has been re-checked since.'
    )
    out.append("")
    section = None
    for ref in refs:
        if ref["section"] != section:
            section = ref["section"]
            out.append(f"## {headline(section)}")
            out.append("")
        out.append(f'<a id="ref-{ref["id"]}"></a>')
        out.append("")
        out.append(f'**{ref["id"]}. {ref["citation"]}**')
        out.append("")
        out.append(ref["note"])
        out.append("")
        out.append(f'<{ref["url"]}>')
        out.append("")
        if cited_by[ref["id"]]:
            hits = cited_by[ref["id"]]
            links = ", ".join(f'[{n["label"]}]({n["path"]}/)' for n in hits)
            if len(hits) > 6:
                out.append(f"<details><summary><em>Cited for {len(hits)} variants</em></summary>")
                out.append("")
                out.append(links)
                out.append("")
                out.append("</details>")
            else:
                out.append(f"*Cited for:* {links}")
        else:
            out.append("*Cited for:* no variant folder yet.")
        out.append("")
    out.append("## Primary sources cited within the above, not consulted directly for the chart")
    out.append("")
    out.append(data["primary_sources_not_consulted"])
    out.append("")
    out.append("## Where the chart's sources disagree")
    out.append("")
    out.append(
        "Where Sloperama and the Mahjong Wiki disagree, the chart follows the Mahjong Wiki, whose material is "
        "more recent. Tile counts and hand sizes come from Sloperama, the only catalogue that records them "
        "systematically. The Mahjong Wiki itself carries no bibliography and no per-claim citations; references "
        "27-33 are the sources its distinctive claims can be matched to, and references 34-38 are where to check "
        "it independently. See [`_dev/source-chart/`](_dev/source-chart/) for the chart's full appendix on this."
    )
    out.append("")
    return "\n".join(out)


def findings_md(nodes):
    """The cross-comparison read across the whole tree."""
    by = {}
    for n in nodes:
        if n.get("claims"):
            by.setdefault(n["claims"]["evidence"], []).append(n)

    out = []
    out.append("# Findings")
    out.append("")
    out.append(
        "What the sources say when set against each other, variant by variant. Every claim here was read "
        "at its source; a source that could not be fetched is recorded as unreachable rather than "
        "summarised from search results. Each variant's full comparison table lives in its own folder — "
        "this page is the read across the whole tree."
    )
    out.append("")
    out.append("| Evidence | Meaning | Variants |")
    out.append("| --- | --- | --- |")
    for key, meaning in EVIDENCE.items():
        out.append(f"| `{key}` | {meaning} | {len(by.get(key, []))} |")
    out.append("")
    out.append(
        "A `single-source` tag is not a criticism of a variant. For most of the mainland and Southeast "
        "Asian entries there simply is one English-language account, usually a newsgroup report, and the "
        "honest record is that it stands alone."
    )
    out.append("")

    order = ["conflicting", "unsupported", "partial", "single-source", "corroborated"]
    HEADS = {
        "conflicting": ("Where sources disagree",
                        "These are the entries where cross-comparison actually changes what you should "
                        "believe. Each one names what conflicts and, where the evidence allows, which "
                        "account is likelier."),
        "unsupported": ("Where the sources do not carry the claim",
                        "The node asserts something its own cited source does not contain. None of these "
                        "means the variant is not real; it means the citation does not support the entry "
                        "as written."),
        "partial": ("Where the sources are partly silent",
                    "Agreement on some defining facts, silence or division on others."),
        "single-source": ("Where one account stands alone",
                          "Confirmed as far as one source goes, with nothing independent behind it."),
        "corroborated": ("Where independent sources agree",
                         "Two or more sources, read separately, agree on the facts that define the "
                         "variant. These are the entries a rulebook could be built on first."),
    }
    for key in order:
        if not by.get(key):
            continue
        heading, blurb = HEADS[key]
        out.append(f"## {heading}")
        out.append("")
        out.append(blurb)
        out.append("")
        for n in sorted(by[key], key=lambda n: n["label"].lower()):
            out.append(f"### [{n['label']}]({n['path']}/)")
            out.append("")
            out.append(n["claims"]["assessment"])
            out.append("")
    out.append("## What this pass did not settle")
    out.append("")
    out.append(
        "Three sites refuse automated requests with a Cloudflare challenge: riichi.wiki, mahjongg.org and "
        "BoardGameGeek. Two of the three were still read, through the Wayback Machine, and their evidence "
        "is in the tables above. Only BoardGameGeek remains unread: its archived copies are thin and its "
        "official XML API now requires an account. No attempt was made to defeat the bot protection on any "
        "of them, and none is needed for the two that archives cover."
    )
    out.append("")
    out.append(
        "Three further sites, maque.games, gunplot.net and mahjong-europe.org, serve broken or expired "
        "TLS certificates. They were read through the Wayback Machine rather than over an unverified "
        "connection: a source fetched over a channel that cannot be authenticated is not one this "
        "compendium can honestly record as read at source, and a dated archive snapshot is better "
        "provenance in any case.\n\n"
        "The Mahjong Wiki itself was read through the Wayback Machine throughout, because the live site "
        "is not reachable here. Its pages carry a footnote marker on at least one claim, which is worth "
        "noting against the source chart's appendix asserting that the wiki has no per-claim citations "
        "anywhere — that is nearly, but not quite, true."
    )
    out.append("")
    out.append(
        "Nothing in this pass touches the content of the NMJL or AMJA annual cards, or of *Mah Jongg "
        "Made Easy*. Those are live copyrighted works: this compendium records what they are and how the "
        "game is structured around them, never what is printed on them."
    )
    out.append("")
    return "\n".join(out)


def main():
    nodes = load_nodes()
    data = json.load(open(os.path.join(DATA, "references.json")))
    data["distortions"] = json.load(open(os.path.join(DATA, "distortions.json")))
    refs_by_id = {r["id"]: r for r in data["references"]}
    refs_by_slug = {r["slug"]: r["id"] for r in data["references"]}

    for n in nodes:
        os.makedirs(os.path.join(ROOT, n["path"]), exist_ok=True)
        write_node_readme(os.path.join(ROOT, n["path"], "README.md"),
                          node_readme(n, refs_by_id, refs_by_slug))

    open(os.path.join(ROOT, "README.md"), "w").write(root_readme(nodes, data))
    open(os.path.join(ROOT, "REFERENCES.md"), "w").write(references_md(nodes, data))
    if any(n.get("claims") for n in nodes):
        open(os.path.join(ROOT, "FINDINGS.md"), "w").write(findings_md(nodes))
    print(f"{len(nodes)} variant folders, README.md and REFERENCES.md written")


if __name__ == "__main__":
    main()
