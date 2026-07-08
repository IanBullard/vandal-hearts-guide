#!/usr/bin/env python3
"""Build a single self-contained walkthrough HTML file for PixelGuide.

PixelGuide (the Android guide viewer used on the AYN Thor) imports ONE
self-contained HTML file and renders it in an offline WebView. The main site is
a multi-page just-the-docs Jekyll site whose search, sidebar, and styling all
load external JS/CSS from absolute paths that don't resolve offline -- so its
dynamic features break there.

This script extracts the DISTILLED "Quick Reference" content that is authored
directly into the walkthrough pages -- the `.quick-ref`, `.shop-strategy`, and
`.story-callout` blocks -- and assembles them into one self-contained HTML file
(inline CSS, no JavaScript, PixelGuide-friendly). Everything in the export
therefore already exists, verbatim, in the main guide: the export can only ever
be a subset of designated blocks, never a place where new information is added.

Run `bundle exec jekyll build` first (this script attempts it for you), then:
    python3 tools/build-pixelguide.py

Pilot scope: Act 1 only. Add acts to ACTS as they get quick-ref cards authored.
"""

import html
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "_site" / "walkthrough"
OUT = REPO / "walkthrough-pixelguide.html"

# Sections included in the export, in reading order. The Trials of Toroah come
# last, after Act 6 -- they are optional and unlocked across the acts.
# (id, built fragment, title)
ACTS = [
    ("act1", "act1/index.html", "Act 1: A Premonition of War"),
    ("act2", "act2/index.html", "Act 2: Island of Madness"),
    ("act3", "act3/index.html", "Act 3: Escape to Tomorrow"),
    ("act4", "act4/index.html", "Act 4: The Successor"),
    ("act5", "act5/index.html", "Act 5: The Legacy"),
    ("act6", "act6/index.html", "Act 6: A Fool's Epitaph"),
    ("trials", "trials/index.html", "Trials of Toroah"),
]

CARD_CLASSES = ("quick-ref", "shop-strategy", "story-callout")

# Site-internal links point at pages not in this single-file export (detailed
# trials pages, other sections). Strip the anchor, keep the text -- no dead links.
DEAD_LINK = re.compile(
    r'<a\s+href="/vandal-hearts-guide/[^"]*"[^>]*>(.*?)</a>', re.DOTALL
)

# One ordered pass over the page body: match a heading OR a designated card,
# in document order, so battle titles and their cards stay interleaved.
TOKEN = re.compile(
    r'<h([12])\b[^>]*>(?P<h>.*?)</h\1>'
    r'|<div class="(?P<cls>' + "|".join(CARD_CLASSES) + r')">(?P<card>.*?)</div>',
    re.DOTALL,
)
TAGS = re.compile(r"<[^>]+>")
SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    return SLUG_STRIP.sub("-", text.lower()).strip("-") or "section"


def main_region(page: str) -> str:
    m = re.search(r"<main\b[^>]*>(.*?)</main>", page, re.DOTALL)
    if not m:
        sys.exit("could not locate <main> in built page (theme layout changed?)")
    return m.group(1)


def clean_heading(inner_html: str) -> str:
    return html.unescape(TAGS.sub("", inner_html)).strip()


def parse_act(page: str):
    """Return (title, [ (section_title, [card_html, ...]) ]) for one act page.

    A section is a battle (or the act overview). Sections with no cards -- the
    per-page TOC, the prose-only 'Complete Summary', 'Next Steps' -- are dropped.
    """
    body = main_region(page)
    sections = []  # list of [title, [cards]]
    current = None
    for m in TOKEN.finditer(body):
        if m.group("card") is not None:
            card = DEAD_LINK.sub(r"\1", m.group("card").strip())
            if "<div" in card:
                # Cards must not contain nested divs (e.g. a table-wrapper) or
                # this regex would truncate them. Kept as a guard for the day
                # someone puts a markdown table in a card.
                sys.exit(
                    "a card contains a nested <div>; switch extraction to a "
                    "depth-aware parser before using tables inside cards."
                )
            if current is None:
                current = ["", []]  # cards before any heading (unlikely)
            current[1].append((m.group("cls"), card))
        else:
            title = clean_heading(m.group("h"))
            if title.lower() == "table of contents":
                continue
            if current is not None:
                sections.append(current)
            current = [title, []]
    if current is not None:
        sections.append(current)
    return [s for s in sections if s[1]]


def render_card(cls: str, inner: str) -> str:
    return f'<div class="{cls}">{inner}</div>'


def render_section(title: str, cards, anchor: str) -> str:
    # quick-ref first, then story/shop as they read post-battle.
    order = {"quick-ref": 0, "story-callout": 1, "shop-strategy": 2}
    cards = sorted(cards, key=lambda c: order.get(c[0], 9))
    body = "\n".join(render_card(cls, inner) for cls, inner in cards)
    return f'<section id="{anchor}">\n<h2>{html.escape(title)}</h2>\n{body}\n</section>'


def top_nav(nav_items) -> str:
    lis = "\n".join(
        f'  <li><a href="#{anchor}">{html.escape(title)}</a></li>'
        for anchor, title in nav_items
    )
    return f'<nav id="toc" aria-label="Contents">\n  <ol>\n{lis}\n  </ol>\n</nav>'


def jekyll_build() -> None:
    try:
        subprocess.run(
            ["bundle", "exec", "jekyll", "build", "--quiet"], cwd=REPO, check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        if not SITE.exists():
            sys.exit(
                f"Jekyll build failed ({exc}) and {SITE} does not exist.\n"
                "Put the Ruby toolchain on PATH, run `bundle exec jekyll build`, "
                "then re-run this script."
            )
        print(f"warning: jekyll build failed ({exc}); using existing _site.")


def main() -> None:
    jekyll_build()

    sections_html = []
    nav_items = []
    seen = set()
    for act_id, src, act_title in ACTS:
        path = SITE / src
        if not path.exists():
            sys.exit(f"missing rendered fragment: {path}")
        sections_html.append(f"<h1>{html.escape(act_title)}</h1>")
        for title, cards in parse_act(path.read_text(encoding="utf-8")):
            anchor = slugify(f"{act_id}-{title}")
            while anchor in seen:
                anchor += "x"
            seen.add(anchor)
            nav_items.append((anchor, title))
            sections_html.append(render_section(title, cards, anchor))

    body = top_nav(nav_items) + "\n\n" + "\n\n".join(sections_html)
    OUT.write_text(PAGE.format(body=body), encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} ({OUT.stat().st_size // 1024} KB, "
          f"{len(nav_items)} sections)")


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vandal Hearts - Walkthrough (PixelGuide)</title>
<style>
:root {{
  --bg:#fff; --fg:#1b1b1f; --muted:#5c5f66; --rule:#d7d9de; --link:#1a56db; --card:#f5f6f8;
  --qr:#1a56db; --qr-bg:#eaf1fe; --shop:#1e7e45; --shop-bg:#e7f6ec;
  --story:#7c3aed; --story-bg:#f3ecfe; --vand:#c0392b; --vand-bg:#fbe4e0;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg:#16161a; --fg:#e6e6ea; --muted:#a0a3ab; --rule:#33343a; --link:#7aa2ff; --card:#1f2026;
    --qr:#7aa2ff; --qr-bg:#1b2436; --shop:#57c98a; --shop-bg:#152a1e;
    --story:#b794f6; --story-bg:#241a33; --vand:#ef6a5c; --vand-bg:#3a1f1b;
  }}
}}
* {{ box-sizing:border-box; }}
html {{ -webkit-text-size-adjust:100%; }}
body {{
  margin:0 auto; max-width:52rem; padding:1rem 1.1rem 4rem;
  background:var(--bg); color:var(--fg);
  font:1rem/1.55 -apple-system,"Segoe UI",Roboto,system-ui,sans-serif; overflow-wrap:break-word;
}}
a {{ color:var(--link); }}
h1 {{ font-size:1.6rem; border-bottom:2px solid var(--rule); padding-bottom:.3em; margin:1.4em 0 .5em; }}
h2 {{ font-size:1.25rem; margin:1.6em 0 .4em; }}
section {{ scroll-margin-top:1rem; }}
p, ul {{ margin:.4em 0; }}
ul {{ padding-left:1.2em; }}
li {{ margin:.15em 0; }}
#toc {{ background:var(--card); border:1px solid var(--rule); border-radius:8px; padding:.4em 1.1em .9em; }}
#toc ol {{ margin:.3em 0; padding-left:1.3em; }}
/* Card blocks -- mirror the website styling, self-contained here. */
.quick-ref, .shop-strategy, .story-callout {{
  border-radius:6px; padding:.55rem .85rem; margin:.5rem 0 1.1rem; font-size:.92rem;
}}
.quick-ref > :first-child, .shop-strategy > :first-child, .story-callout > :first-child {{ margin-top:0; }}
.quick-ref > :last-child, .shop-strategy > :last-child, .story-callout > :last-child {{ margin-bottom:0; }}
.quick-ref {{ border:1px solid var(--rule); border-left:4px solid var(--qr); background:var(--qr-bg); }}
.shop-strategy {{ border-left:4px solid var(--shop); background:var(--shop-bg); }}
.story-callout {{ border-left:4px solid var(--story); background:var(--story-bg); }}
.vandalier {{
  display:block; border:2px solid var(--vand); background:var(--vand-bg);
  border-radius:6px; padding:.45rem .7rem; margin:.5rem 0; font-weight:600;
}}
</style>
</head>
<body>
{body}
</body>
</html>
"""


if __name__ == "__main__":
    main()
