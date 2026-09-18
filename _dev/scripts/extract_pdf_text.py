#!/usr/bin/env python3
"""Extract text from a PDF whose body is drawn through several subset fonts.

Written for the Pusser's Bones rules book, whose text looked unextractable: a
naive reader returns only the headings, because the body is drawn as hex glyph
ids rather than literal strings.


Each font carries its own ToUnicode CMap, and different fonts reuse the same
glyph ids for different characters, so the maps must be kept apart and selected
by the current /Fx Tf font. Merging them scrambles the capitals.
"""
import re, sys, zlib

OBJ = re.compile(rb"(\d+)\s+0\s+obj\b(.*?)\bendobj", re.S)

def objects(data):
    return {int(n): body for n, body in OBJ.findall(data)}

def stream_of(body):
    m = re.search(rb"stream\r?\n(.*?)endstream", body, re.S)
    if not m:
        return None
    try:
        return zlib.decompress(m.group(1))
    except zlib.error:
        return m.group(1)

def parse_cmap(raw):
    cmap = {}
    t = raw.decode("latin-1")
    for block in re.findall(r"beginbfchar(.*?)endbfchar", t, re.S):
        for src, dst in re.findall(r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            cmap[int(src, 16)] = "".join(
                chr(int(dst[i:i + 4], 16)) for i in range(0, len(dst), 4))
    for block in re.findall(r"beginbfrange(.*?)endbfrange", t, re.S):
        for lo, hi, dst in re.findall(
                r"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", block):
            base = int(dst, 16)
            for i, code in enumerate(range(int(lo, 16), int(hi, 16) + 1)):
                cmap[code] = chr(base + i)
    return cmap

def font_maps(data, objs):
    """Resource name (/F1 …) -> ToUnicode map, per page resource dictionary."""
    tounicode = {}                       # font object number -> cmap
    for num, body in objs.items():
        m = re.search(rb"/ToUnicode\s+(\d+)\s+0\s+R", body)
        if m:
            raw = stream_of(objs.get(int(m.group(1)), b""))
            if raw:
                tounicode[num] = parse_cmap(raw)
    # /Font << /F1 12 0 R /F2 15 0 R >> — collect every such mapping in the file
    byname = {}
    for body in objs.values():
        for fm in re.finditer(rb"/Font\s*<<(.*?)>>", body, re.S):
            for name, ref in re.findall(rb"/(\w+)\s+(\d+)\s+0\s+R", fm.group(1)):
                cm = tounicode.get(int(ref))
                if cm:
                    byname.setdefault(name.decode(), {}).update(cm)
    return byname

def unescape(b):
    b = re.sub(rb"\\([0-7]{1,3})", lambda m: bytes([int(m.group(1), 8) & 0xFF]), b)
    return re.sub(rb"\\(.)", rb"\1", b)

TOKENS = re.compile(
    rb"/(\w+)\s+[\d.]+\s+Tf|\[([^]]*)\]\s*TJ|(\((?:\\.|[^()\\])*\))\s*Tj"
    rb"|<([0-9A-Fa-f]+)>\s*Tj|(T\*|Td|TD|ET)", re.S)
PIECES = re.compile(rb"\((?:\\.|[^()\\])*\)|<([0-9A-Fa-f]+)>", re.S)

GLOBAL = {}

def decode_hex(h, cmap):
    out = []
    for i in range(0, len(h) - 1, 4):
        code = int(h[i:i + 4], 16)
        ch = cmap.get(code)
        if ch is None:
            ch = GLOBAL.get(code, "")
        out.append(ch)
    return "".join(out)

def page_text(stream, byname):
    out, cur = [], {}
    for m in TOKENS.finditer(stream):
        if m.group(1):
            cur = byname.get(m.group(1).decode(), {})
        elif m.group(5):
            out.append("\n")
        elif m.group(4):
            out.append(decode_hex(m.group(4).decode("latin-1"), cur))
        elif m.group(3):
            out.append(unescape(m.group(3)[1:-1]).decode("latin-1"))
        else:
            arr = m.group(2)
            for tok in re.finditer(
                    rb"\((?:\\.|[^()\\])*\)|<([0-9A-Fa-f]+)>|(-?\d+(?:\.\d+)?)", arr, re.S):
                if tok.group(2) is not None:
                    if float(tok.group(2)) <= -120:
                        out.append(" ")
                elif tok.group(1):
                    out.append(decode_hex(tok.group(1).decode("latin-1"), cur))
                else:
                    out.append(unescape(tok.group(0)[1:-1]).decode("latin-1"))
    return "".join(out)

def main(path):
    data = open(path, "rb").read()
    objs = objects(data)
    byname = font_maps(data, objs)
    for cm in byname.values():
        for k, v in cm.items():
            GLOBAL.setdefault(k, v)
    sys.stderr.write(f"fonts: {len(byname)} " +
                     " ".join(f"{k}:{len(v)}" for k, v in sorted(byname.items())) + "\n")
    chunks = []
    for body in objs.values():
        s = stream_of(body)
        if s and (b"TJ" in s or b"Tj" in s):
            chunks.append(page_text(s, byname))
    text = "\n".join(chunks)
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text)

if __name__ == "__main__":
    sys.stdout.write(main(sys.argv[1]))
