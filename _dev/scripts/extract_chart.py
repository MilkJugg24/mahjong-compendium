#!/usr/bin/env python3
"""Extract the node tree and bibliography text out of the source chart PDF.

The chart was produced as a vector PDF with no tagged text, so the tree has to
be read back out of the content stream: indentation is the x coordinate of each
label, family grouping is the fill colour, and a disputed link is a connector
drawn with a dash pattern set.

Usage:  python3 _dev/scripts/extract_chart.py [pdf] > extracted.txt
"""
import base64
import re
import sys
import zlib

PDF = sys.argv[1] if len(sys.argv) > 1 else "_dev/source-chart/mahjong-variant-family-tree.pdf"

FAMILIES = {
    (".172549", ".172549", ".164706"): "roots",
    (".015686", ".203922", ".172549"): "chinese",
    (".090196", ".203922", ".015686"): "taiwanese",
    (".015686", ".172549", ".32549"): "southeast-asian",
    (".14902", ".129412", ".360784"): "japanese",
    (".294118", ".082353", ".156863"): "korean",
    (".290196", ".105882", ".047059"): "western-american",
}


def streams(data):
    for raw in re.findall(rb"stream\r?\n(.*?)endstream", data, re.S):
        try:
            yield zlib.decompress(raw)
        except zlib.error:
            yield raw


def content_stream(data):
    """Return the page content stream, ASCII85 decoded where needed."""
    for s in streams(data):
        body = s.strip()
        if body.startswith(b"/CIDInit") or body.startswith(b"\x00\x01\x00\x00"):
            continue
        if not body.lstrip().startswith(b"1 0 0 1"):
            body = body[:-2] if body.endswith(b"~>") else body
            body = zlib.decompress(base64.a85decode(body))
        return body.decode("latin-1")
    raise SystemExit("no content stream found")


def cid_map(data):
    """Byte -> character map for the embedded CJK subset font."""
    for s in streams(data):
        if not s.startswith(b"/CIDInit"):
            continue
        text = s.decode("latin-1")
        return {
            int(a, 16): chr(int(b, 16))
            for a, b in re.findall(r"<([0-9A-Fa-f]{2})> <([0-9A-Fa-f]{4})>", text)
            if int(b, 16) > 0x7F
        }
    return {}


def unescape(text, cids):
    text = re.sub(r"\\(\d{1,3})", lambda m: cids.get(int(m.group(1), 8), ""), text)
    return re.sub(r"\\([()\\])", r"\1", text)


def main():
    data = open(PDF, "rb").read()
    content = content_stream(data)
    cids = cid_map(data)

    # Dashed connectors mark a disputed descent claim. Record the y of each.
    dashed, dash_state = [], None
    for m in re.finditer(r"\[([^\]]*)\]\s*[\d.]+\s*d|n ([\d.]+) ([\d.]+) m ([\d.]+) ([\d.]+) l", content):
        if m.group(1) is not None:
            dash_state = m.group(1).strip()
        elif dash_state:
            dashed.append(float(m.group(3)))

    pattern = (
        r"([\d.]+) ([\d.]+) ([\d.]+) rg"
        r"|BT 1 0 0 1 ([\d.]+) ([\d.]+) Tm (?:/\S+ [\d.]+ Tf [\d.]+ TL )?\((.*?)\) Tj"
    )
    colour = None
    for m in re.finditer(pattern, content):
        if m.group(1):
            colour = (m.group(1), m.group(2), m.group(3))
            continue
        x, y, label = float(m.group(4)), float(m.group(5)), unescape(m.group(6), cids)
        family = FAMILIES.get(colour, "-")
        flag = "disputed" if any(abs(y + 3.2 - dy) < 2 for dy in dashed) else ""
        print(f"{y:9.1f}\t{x:6.1f}\t{family:16s}\t{flag:8s}\t{label}")


if __name__ == "__main__":
    main()
