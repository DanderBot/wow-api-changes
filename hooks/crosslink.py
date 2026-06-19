"""MkDocs post-build hook: cross-link struct/enum/constants mentions to their definitions.

Markdown can't place a link inside an inline code span, so this runs after the build
and edits the rendered HTML directly:

1. Pass 1 — scan every page's <article> for definition entries (a `<code>` whose
   following text starts with "(struct)", "(enum)" or "(constants)"), tag each with an
   anchor id, and record symbol -> (page, anchor, definition text).
2. Pass 2 — in every inline <code>, wrap whole-word mentions of those known symbols in
   <a class="xref"> links to the definition, carrying the definition text in data-peek
   for the hover popover (peek.js).

Only symbols actually defined in the doc are linked, so primitives (number, bool,
cstring, table, ...) and externally-defined types are never touched. Code blocks
(```...```) and a symbol's own definition element are skipped.
"""

import glob
import os
import re

from bs4 import BeautifulSoup

DEF_RE = re.compile(r"^\s*\((struct|enum|constants)\b")
IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")
ARTICLE_RE = re.compile(r"(<article\b[^>]*>)(.*?)(</article>)", re.S)
PEEK_MAX = 320


def _definition_marker(code):
    """If this <code> introduces a type, return the text node carrying its '(kind)'."""
    host = code.parent if (code.parent and code.parent.name == "strong") else code
    nxt = host.next_sibling
    if isinstance(nxt, str):
        return nxt
    return nxt.get_text() if hasattr(nxt, "get_text") and nxt is not None else ""


def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]
    pages = glob.glob(os.path.join(site_dir, "**", "*.html"), recursive=True)

    docs = []          # {path, text, match, soup, dirty}
    registry = {}      # symbol -> (abs_path, anchor, peek_text)

    # ---- Pass 1: collect definitions ----
    for path in pages:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        m = ARTICLE_RE.search(text)
        if not m:
            continue
        soup = BeautifulSoup(m.group(2), "html.parser")
        doc = {"path": path, "text": text, "match": m, "soup": soup, "dirty": False}
        docs.append(doc)

        for code in soup.find_all("code"):
            if code.find_parent("pre"):
                continue
            name = code.get_text()
            if not IDENT_RE.match(name) or name in registry:
                continue
            if DEF_RE.match(_definition_marker(code)):
                anchor = "ref-" + name
                code["id"] = anchor
                doc["dirty"] = True
                container = code.find_parent(["li", "p"]) or code
                peek = " ".join(container.get_text().split())
                if len(peek) > PEEK_MAX:
                    peek = peek[: PEEK_MAX - 1] + "…"
                registry[name] = (path, anchor, peek)

    if not registry:
        return

    symbols = sorted(registry, key=len, reverse=True)
    mention_re = re.compile(
        r"(?<![A-Za-z0-9_])(" + "|".join(map(re.escape, symbols)) + r")(?![A-Za-z0-9_])"
    )

    # ---- Pass 2: link mentions ----
    for doc in docs:
        soup = doc["soup"]
        for code in soup.find_all("code"):
            if code.find_parent("pre"):
                continue
            if str(code.get("id", "")).startswith("ref-"):
                continue  # don't self-link a definition's own name
            for text_node in list(code.find_all(string=True, recursive=False)):
                s = str(text_node)
                if not mention_re.search(s):
                    continue
                parts, last = [], 0
                for mt in mention_re.finditer(s):
                    sym = mt.group(1)
                    if mt.start() > last:
                        parts.append(soup.new_string(s[last:mt.start()]))
                    target_path, anchor, peek = registry[sym]
                    rel = os.path.relpath(target_path, os.path.dirname(doc["path"]))
                    rel = rel.replace(os.sep, "/")
                    link = soup.new_tag("a", href=f"{rel}#{anchor}")
                    link["class"] = "xref"
                    link["data-peek"] = peek
                    link.string = sym
                    parts.append(link)
                    last = mt.end()
                if last < len(s):
                    parts.append(soup.new_string(s[last:]))
                text_node.replace_with(*parts)
                doc["dirty"] = True

    # ---- Write back only the <article> body of changed pages ----
    linked = 0
    for doc in docs:
        if not doc["dirty"]:
            continue
        m = doc["match"]
        new_inner = str(doc["soup"])
        new_text = doc["text"][: m.start(2)] + new_inner + doc["text"][m.end(2):]
        with open(doc["path"], "w", encoding="utf-8") as fh:
            fh.write(new_text)
        linked += 1

    print(f"[crosslink] {len(registry)} definitions, links injected across {linked} page(s)")
