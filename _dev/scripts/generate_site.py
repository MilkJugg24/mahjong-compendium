#!/usr/bin/env python3
"""Build the public website into docs/ from the same data the Markdown uses.

The landing page is a 3D flythrough of the family tree; every variant also gets
a plain readable page, so the evidence stays linkable, citable and usable
without WebGL. Both come from _dev/data/, so there is one source of truth.

Usage:  python3 _dev/scripts/generate_site.py
"""
import csv
import html
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "_dev", "data")
OUT = os.path.join(ROOT, "docs")
DOMAIN = "compendium.pandaren.org"
TITLE = "Mahjong Compendium"
# how many sibling variants a footnote names before deferring to the bibliography
SEE_ALSO = 6

# Family hues, warmed to sit on the Pandaria green-and-brown ground while
# staying separable from one another at tree-node size.
FAMILY = {
    "roots":            ("Roots / ancestral", "#d9cba3"),
    "chinese":          ("Chinese",           "#52b98d"),
    "taiwanese":        ("Taiwanese",         "#a3c45c"),
    "southeast-asian":  ("Southeast Asian",   "#5aa9c9"),
    "japanese":         ("Japanese",          "#a78bd0"),
    "korean":           ("Korean",            "#d97a8e"),
    "western-american": ("Western / American", "#e0954a"),
}

EVIDENCE = {
    "corroborated":    "two or more independent sources agree on the facts that define this variant",
    "partial":         "sources agree on some points and are silent or divided on others",
    "conflicting":     "sources disagree materially, or one source contradicts itself",
    "single-source":   "only one source was found; nothing independent confirms it",
    "unsupported":     "the sources checked do not carry the claim this node makes",
}

CONFIDENCE = {
    "documented": "a published ruleset or rule description exists and is cited",
    "catalogued": "listed in a variant catalogue with tile counts and hand sizes, but no rules text verified",
    "single-informant": "the whole entry rests on one report from one person",
    "disputed": "the descent shown is contested; the chart drew this link dashed",
    "placeholder": "no source establishes the descent at all; the parent link is a guess",
    "lost": "no rules text survives",
}


# ---------------------------------------------------------------- data

def load():
    with open(os.path.join(DATA, "nodes.tsv")) as f:
        nodes = list(csv.DictReader(f, delimiter="\t"))
    refs = json.load(open(os.path.join(DATA, "references.json")))
    claims = json.load(open(os.path.join(DATA, "claims.json")))
    distortions = json.load(open(os.path.join(DATA, "distortions.json")))
    by_slug = {r["slug"]: r for r in refs["references"]}
    by_id = {r["id"]: r for r in refs["references"]}

    stack = {}
    for n in nodes:
        n["depth"] = int(n["depth"])
        parent = stack.get(n["depth"] - 1)
        n["parent"] = parent["slug"] if parent else None
        n["children"] = []
        if parent:
            parent["children"].append(n["slug"])
        stack[n["depth"]] = n
        for deeper in [d for d in stack if d > n["depth"]]:
            del stack[deeper]
        n["claims"] = claims.get(n["slug"])
        n["ref_ids"] = ([by_slug[n["source"]]["id"]] +
                        [int(x) for x in n["refs"].split(",") if x and by_slug[n["source"]]["id"] != int(x)])
    return {n["slug"]: n for n in nodes}, nodes, refs, by_slug, by_id, distortions


def citation_map(nodes_list, by_slug):
    """Reference id -> the variant nodes that cite it, in tree order.

    Both the per-page footnotes and the master bibliography read this, so the
    two can never disagree about who cites what.
    """
    cited, seen = {}, {}
    for n in nodes_list:
        ids = list(n["ref_ids"])
        if n.get("claims"):
            ids += [by_slug[o["source"]]["id"] for o in n["claims"]["observations"]]
        for rid in ids:
            if n["slug"] not in seen.setdefault(rid, set()):
                seen[rid].add(n["slug"])
                cited.setdefault(rid, []).append(n)
    return cited


# ------------------------------------------------------------ rendering

INLINE = [
    (re.compile(r"\*\*(.+?)\*\*", re.S), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", re.S), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
]

def inline(text):
    out = html.escape(text, quote=False)
    for pattern, repl in INLINE:
        out = pattern.sub(repl, out)
    return out

def paragraphs(text):
    return "\n".join(f"<p>{inline(p.strip())}</p>"
                     for p in re.split(r"\n\s*\n", text.strip()) if p.strip())

def esc(s):
    return html.escape(s or "", quote=True)


def page(title, body, depth, description="", extra_head="", extra_body=""):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/site.css">
{extra_head}
</head>
<body>
<header class="bar">
  <a class="brand" href="{up}">Mahjong&nbsp;Compendium</a>
  <nav>
    <a href="{up}">Tree</a>
    <a href="{up}variants/">Variants</a>
    <a href="{up}findings/">Findings</a>
    <a href="{up}references/">References</a>
    <a href="{up}method/">Method</a>
  </nav>
</header>
<main>
{body}
</main>
<footer class="bar foot">
  <span>Evidence recorded as read at source. Nothing here reproduces a copyrighted ruleset.</span>
  <a href="https://github.com/MilkJugg24/mahjong-compendium">Source on GitHub</a>
</footer>
{extra_body}
</body>
</html>
"""


# ------------------------------------------------------------ variant page

def page_sources(n, by_slug):
    """Every source this page uses, numbered locally in order of first appearance.

    A page is self-contained: the footnote a reader lands on carries the full
    citation, the annotation and the outbound link, so no page depends on the
    bibliography to say what [3] is.
    """
    order, seen = [], set()

    def use(rid):
        if rid not in seen:
            seen.add(rid)
            order.append(rid)

    observed = {}
    if n.get("claims"):
        obs = n["claims"]["observations"]
        fields = ("tiles", "hand", "flowers", "scoring", "payout")
        for o in [o for o in obs if any(o.get(f) for f in fields)]:
            use(by_slug[o["source"]]["id"])
        for o in [o for o in obs if o.get("note")]:
            use(by_slug[o["source"]]["id"])
        for o in obs:
            observed.setdefault(by_slug[o["source"]]["id"], o)
    for rid in n["ref_ids"]:
        use(rid)

    canonical = by_slug[n["source"]]["id"]
    num = {rid: i + 1 for i, rid in enumerate(order)}
    role = {rid: ("canonical" if rid == canonical
                  else "supporting" if rid in n["ref_ids"] else "cross-check")
            for rid in order}
    return order, num, role, observed


def variant_page(n, nodes, by_id, by_slug, cited):
    up = "../../"
    order, num, role, observed = page_sources(n, by_slug)
    fam_name, fam_colour = FAMILY[n["family"]]
    if n["depth"] == 0 or nodes[n["slug"]]["slug"] == "modern-inventions":
        pass
    # lineage breadcrumb
    chain, cur = [], n
    while cur:
        chain.append(cur)
        cur = nodes[cur["parent"]] if cur["parent"] else None
    chain.reverse()
    crumb = " <span class=\"sep\">›</span> ".join(
        f"<strong>{esc(c['label'])}</strong>" if c is n
        else f'<a href="{up}variants/{c["slug"]}/">{esc(c["label"])}</a>'
        for c in chain)

    b = [f'<article class="variant" style="--fam:{fam_colour}">']
    b.append('<p class="crumb">' + crumb + '</p>')
    b.append(f'<h1>{esc(n["label"])}</h1>')
    if n["detail"]:
        b.append(f'<p class="lede">{esc(n["detail"])}</p>')

    ev = n["claims"]["evidence"] if n.get("claims") else None
    b.append('<ul class="tags">')
    b.append(f'<li class="fam">{esc(fam_name)}</li>')
    b.append(f'<li class="c-{esc(n["confidence"])}" title="{esc(CONFIDENCE[n["confidence"]])}">'
             f'confidence: {esc(n["confidence"])}</li>')
    if ev:
        b.append(f'<li class="e-{esc(ev)}" title="{esc(EVIDENCE[ev])}">evidence: {esc(ev)}</li>')
    b.append('</ul>')

    if n["children"]:
        b.append('<section><h2>Descends into</h2><ul class="kids">')
        for c in n["children"]:
            k = nodes[c]
            d = f' — {esc(k["detail"])}' if k["detail"] else ""
            b.append(f'<li><a href="{up}variants/{c}/">{esc(k["label"])}</a>{d}</li>')
        b.append('</ul></section>')

    if n["note"]:
        b.append(f'<section class="caveat"><h2>Caveat from the source chart</h2>'
                 f'<p>{inline(n["note"])}</p></section>')

    if n.get("claims"):
        c = n["claims"]
        b.append('<section><h2>Cross-comparison</h2>')
        b.append(f'<p class="verdict e-{esc(c["evidence"])}"><strong>{esc(c["evidence"])}</strong> — '
                 f'{esc(EVIDENCE[c["evidence"]])}</p>')
        fields = ("tiles", "hand", "flowers", "scoring", "payout")
        measured = [o for o in c["observations"] if any(o.get(f) for f in fields)]
        if measured:
            b.append('<div class="scroll"><table class="cmp"><thead><tr>'
                     '<th>Source</th><th>Tiles</th><th>Hand</th><th>Flowers</th>'
                     '<th>Scoring</th><th>Payout</th></tr></thead><tbody>')
            for o in measured:
                r = by_slug[o["source"]]
                cells = "".join(f'<td>{inline(o.get(f) or "—")}</td>' for f in fields)
                b.append(f'<tr><td class="src"><a href="#src-{num[r["id"]]}">[{num[r["id"]]}]</a></td>{cells}</tr>')
            b.append('</tbody></table></div>')
        notes = [(by_slug[o["source"]], o["note"]) for o in c["observations"] if o.get("note")]
        if notes:
            b.append('<ul class="notes">')
            for r, note in notes:
                b.append(f'<li><a href="#src-{num[r["id"]]}">[{num[r["id"]]}]</a> {inline(note)}</li>')
            b.append('</ul>')
        b.append('<h3>Reading it</h3>')
        b.append(paragraphs(c["assessment"]))
        b.append('</section>')

    b.append('<section><h2>Sources</h2><ol class="srcs">')
    for rid in order:
        r, o = by_id[rid], observed.get(rid)
        others = [m for m in cited.get(rid, []) if m["slug"] != n["slug"]]
        shown = ", ".join(f'<a href="{up}variants/{m["slug"]}/">{esc(m["label"])}</a>'
                          for m in others[:SEE_ALSO])
        rest = len(others) - min(len(others), SEE_ALSO)
        also = (f'Also cited on: {shown}' + (f' and {rest} more' if rest else '')
                if shown else 'Only cited here')
        when = (f' <span class="when">checked {esc(o["retrieved"])}</span>'
                if o and o.get("retrieved") else '')
        b.append(f'<li id="src-{num[rid]}" class="{role[rid]}">'
                 f'<p class="cite">{esc(r["citation"])}'
                 f' <span class="role">{role[rid]}</span>{when}</p>'
                 f'<p class="dim">{esc(r["note"])}</p>'
                 f'<p class="url"><a href="{esc(r["url"])}" rel="nofollow noopener">'
                 f'{esc(r["url"])}</a></p>'
                 f'<p class="cited">{also} \u00b7 '
                 f'<a href="{up}references/#ref-{rid}">bibliography #{rid}</a></p>'
                 '</li>')
    b.append('</ol></section>')

    b.append(f'<p class="back"><a href="{up}">← back to the tree</a></p>')
    b.append('</article>')
    desc = f'{n["label"]}: {n["detail"]}' if n["detail"] else n["label"]
    return page(f'{n["label"]} — {TITLE}', "\n".join(b), 2, desc)


# --------------------------------------------------------------- indexes

def variants_index(nodes_list):
    b = ['<h1>Variants</h1>',
         '<p class="lede">All 61 entries, alphabetically. Each carries its lineage, '
         'what every source was read to say, and a verdict on the state of its sourcing.</p>',
         '<div class="scroll"><table class="list"><thead><tr><th>Variant</th><th>Family</th>'
         '<th>Confidence</th><th>Evidence</th></tr></thead><tbody>']
    for n in sorted(nodes_list, key=lambda x: x["label"].lower()):
        ev = n["claims"]["evidence"] if n.get("claims") else "—"
        detail = f' <span class="dim">{esc(n["detail"])}</span>' if n["detail"] else ""
        b.append(f'<tr><td><a href="../variants/{n["slug"]}/">{esc(n["label"])}</a>{detail}</td>'
                 f'<td>{esc(FAMILY[n["family"]][0])}</td>'
                 f'<td><span class="pill c-{esc(n["confidence"])}">{esc(n["confidence"])}</span></td>'
                 f'<td><span class="pill e-{esc(ev)}">{esc(ev)}</span></td></tr>')
    b.append('</tbody></table></div>')
    return page(f"Variants — {TITLE}", "\n".join(b), 1,
                "Every mahjong variant in the compendium, with its sourcing state.")


def findings_page(nodes_list):
    by_ev = {}
    for n in nodes_list:
        if n.get("claims"):
            by_ev.setdefault(n["claims"]["evidence"], []).append(n)
    order = ["conflicting", "unsupported", "partial", "single-source", "corroborated"]
    heads = {
        "conflicting": ("Where sources disagree",
                        "The entries where cross-comparison changes what you should believe."),
        "unsupported": ("Where the sources do not carry the claim",
                        "The node asserts something its own cited source does not contain."),
        "partial": ("Where the sources are partly silent",
                    "Agreement on some defining facts, silence or division on others."),
        "single-source": ("Where one account stands alone",
                          "Confirmed as far as one source goes, with nothing independent behind it."),
        "corroborated": ("Where independent sources agree",
                         "Two or more sources, read separately, agree on the defining facts."),
    }
    b = ['<h1>Findings</h1>',
         '<p class="lede">What the sources say when set against each other. Every claim was read at '
         'its source; a source that could not be fetched is recorded as unreachable rather than '
         'summarised from search results.</p>',
         '<div class="counts">']
    for k in order:
        b.append(f'<div class="count e-{k}"><b>{len(by_ev.get(k, []))}</b><span>{k}</span></div>')
    b.append('</div>')
    for k in order:
        if not by_ev.get(k):
            continue
        h, blurb = heads[k]
        b.append(f'<section><h2>{esc(h)}</h2><p class="dim">{esc(blurb)}</p>')
        for n in sorted(by_ev[k], key=lambda x: x["label"].lower()):
            b.append(f'<details class="finding"><summary><a href="../variants/{n["slug"]}/">'
                     f'{esc(n["label"])}</a></summary>{paragraphs(n["claims"]["assessment"])}</details>')
        b.append('</section>')
    return page(f"Findings — {TITLE}", "\n".join(b), 1,
                "Where the sources agree, disagree, and fall silent, variant by variant.")


def references_page(refs, nodes_list, by_slug, cited):
    b = ['<h1>References</h1>',
         f'<p class="lede">{inline(refs["note"])}</p>',
         '<p class="dim">Every source is quoted in full on the variant pages that use it; '
         'this page is the index across all of them.</p>']
    section = None
    for r in refs["references"]:
        if r["section"] != section:
            section = r["section"]
            b.append(f'<h2>{esc(section.title())}</h2>')
        uniq = cited.get(r["id"], [])
        links = ", ".join(f'<a href="../variants/{n["slug"]}/">{esc(n["label"])}</a>' for n in uniq)
        b.append(f'<div class="ref" id="ref-{r["id"]}">'
                 f'<p class="cite"><b>{r["id"]}.</b> {esc(r["citation"])}</p>'
                 f'<p class="dim">{esc(r["note"])}</p>'
                 f'<p class="url"><a href="{esc(r["url"])}" rel="nofollow noopener">{esc(r["url"])}</a></p>'
                 + (f'<p class="cited">Cited for: {links}</p>' if links else
                    '<p class="cited uncited">Not cited by any variant \u2014 background reading '
                    'carried over from the source chart\u2019s bibliography.</p>')
                 + '</div>')
    return page(f"References — {TITLE}", "\n".join(b), 1,
                "Every source used, with back-links to the variants it was cited for.")


# ------------------------------------------------------- landing + method

def landing(nodes_list, distortions):
    counts = {}
    for n in nodes_list:
        if n.get("claims"):
            counts[n["claims"]["evidence"]] = counts.get(n["claims"]["evidence"], 0) + 1
    legend = "".join(
        f'<li><i style="background:{c}"></i>{esc(name)}</li>'
        for name, c in FAMILY.values())
    caveats = "".join(f"<li>{inline(d)}</li>" for d in distortions)
    body = f"""
<section class="hero">
  <div class="stage">
    <canvas id="tree"></canvas>
    <div id="hud">
      <div id="labels"></div>
      <div id="tip" hidden></div>
      <p class="hint">drag to orbit · scroll to zoom · click a node to open it</p>
      <noscript><p class="hint">This view needs JavaScript. The
        <a href="variants/">variant list</a> has everything without it.</p></noscript>
    </div>
  </div>
  <div class="intro">
    <h1>Mahjong variant family tree</h1>
    <p class="lede">{len(nodes_list)} documented rulesets, filed by descent. Every entry records
      what each source was read to say, and how far those sources actually agree.</p>
    <ul class="legend">{legend}</ul>
    <p class="cta"><a class="btn" href="variants/">Browse all variants</a>
       <a class="btn ghost" href="findings/">Read the findings</a></p>
  </div>
</section>

<section class="counts wide">
  {''.join(f'<div class="count e-{k}"><b>{v}</b><span>{k}</span></div>' for k, v in
           sorted(counts.items(), key=lambda kv: -kv[1]))}
</section>

<section class="pitch">
  <h2>What this is</h2>
  <p>A collection of material gathered from around the web, filed by variant, so each claim's origin
     can be checked. The tree records descent <em>as the source chart claims it</em> — not a judgement
     that the claim is correct. Where a claim is weak, the entry says so.</p>
  <h2>What the chart admits about itself</h2>
  <ul class="caveats">{caveats}</ul>
</section>
"""
    head = ('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" '
            'integrity="sha512-dLxUelApnYxpLt6K2iomGngnHO83iUvZytA3YjDUCjT0HDOHKXnVYdf3hU4JjM8uEhxf9nD1/ey98U3t2vZ0qQ==" '
            'crossorigin="anonymous" referrerpolicy="no-referrer"></script>')
    tail = '<script src="assets/tree.js"></script>'
    return page(TITLE, body, 0,
                "A cross-checked family tree of mahjong variants, with the evidence for each.",
                extra_head=head, extra_body=tail)


def method_page():
    dev_readme = open(os.path.join(ROOT, "_dev", "CONVENTIONS.md")).read()
    vocab = re.search(r"## Provenance vocabulary(.*?)(?=\n## )", dev_readme, re.S)
    body = f"""
<h1>Method</h1>
<p class="lede">How the compendium is built, and the rules it holds itself to.</p>

<h2>One source of truth</h2>
<p>Every page here and every Markdown file in the repository is generated from the same data in
   <code>_dev/data/</code>: the node tree, the bibliography, and the per-variant claims. Nothing is
   written twice, so nothing can drift.</p>

<h2>Read at source, or not recorded</h2>
<p>A claim enters the data only if the source was fetched and read. A search-result summary is a lead,
   not evidence; a page that could not be fetched is recorded as unreachable. Where a source contradicts
   itself, both readings are recorded rather than one being picked silently. There is exactly one entry
   in the compendium not read at source, and it says so.</p>

<h2>Two different judgements</h2>
<p><b>Confidence</b> describes the sourcing behind a variant. <b>Evidence</b> describes what happened
   when sources were set against each other. They are not the same thing, and a variant can be
   well documented by one witness or thinly documented by several.</p>

<h2>How sources are cited</h2>
<p>Every variant page carries its own numbered sources at the foot of the page, with the full citation,
   what the source was consulted for, and a link to the source itself. Numbering is local to each page,
   so <code>[1]</code> on one variant is not <code>[1]</code> on another; each footnote names its entry
   in the <a href="../references/">bibliography</a>, which indexes every source across the whole
   compendium. Each footnote also lists the other variants citing the same source, so a source can be
   followed sideways through the tree the way lineage is followed downwards.</p>
<p>A source is marked <b>canonical</b> where the chart drew the variant from it, <b>supporting</b> where
   the chart cites it alongside, and <b>cross-check</b> where it was fetched afterwards to test what the
   chart claimed.</p>

<h2>What is never filed here</h2>
<p>Live copyrighted rulesets. The NMJL and AMJA annual cards for any year, <i>Mah Jongg Made Easy</i>,
   and any variant's in-copyright rulebook. Game mechanics are recorded as facts, exactly as tile counts
   are for every variant; the text of those works is not reproduced.</p>

{'<h2>Provenance vocabulary</h2>' + paragraphs(vocab.group(1)) if vocab else ''}

<p class="back"><a href="https://github.com/MilkJugg24/mahjong-compendium">The repository, including
   the generators and the raw data</a></p>
"""
    return page(f"Method — {TITLE}", body, 1, "How the compendium is built and the rules it follows.")


# ------------------------------------------------------------------ build

def tree_json(nodes_list):
    return [{
        "slug": n["slug"], "label": n["label"], "detail": n["detail"],
        "family": n["family"], "colour": FAMILY[n["family"]][1],
        "depth": n["depth"], "parent": n["parent"],
        "confidence": n["confidence"],
        "evidence": n["claims"]["evidence"] if n.get("claims") else None,
        "children": n["children"],
    } for n in nodes_list]


def main():
    nodes, nodes_list, refs, by_slug, by_id, distortions = load()
    cited = citation_map(nodes_list, by_slug)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

    here = os.path.dirname(os.path.abspath(__file__))
    for asset in ("site.css", "tree.js"):
        shutil.copyfile(os.path.join(here, "site", asset), os.path.join(OUT, "assets", asset))

    json.dump(tree_json(nodes_list), open(os.path.join(OUT, "assets", "tree.json"), "w"),
              separators=(",", ":"))

    open(os.path.join(OUT, "index.html"), "w").write(landing(nodes_list, distortions))
    open(os.path.join(OUT, "CNAME"), "w").write(DOMAIN + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")

    for name, content in (("variants", variants_index(nodes_list)),
                          ("findings", findings_page(nodes_list)),
                          ("references", references_page(refs, nodes_list, by_slug, cited)),
                          ("method", method_page())):
        os.makedirs(os.path.join(OUT, name), exist_ok=True)
        open(os.path.join(OUT, name, "index.html"), "w").write(content)

    for n in nodes_list:
        d = os.path.join(OUT, "variants", n["slug"])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(variant_page(n, nodes, by_id, by_slug, cited))

    print(f"docs/ built: {len(nodes_list)} variant pages, {len(refs['references'])} references, "
          f"CNAME {DOMAIN}")


if __name__ == "__main__":
    main()
