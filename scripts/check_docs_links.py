#!/usr/bin/env python3
"""Check internal links and anchors in the docs/ site.

Verifies, across every *.html file in docs/:
  1. every same-page anchor (href="#id") resolves to an element id on that page
  2. every cross-page link (page.html or page.html#id) resolves to an existing
     file — and, when it carries a fragment, to an existing id in that file
  3. every relative asset reference (favicon, images, .skill package) exists

External links (http/https/mailto) are not checked — this is a structural
check, not a liveness check.

Usage:
    python scripts/check_docs_links.py [docs-dir]   # default: docs
Exit code 1 if any broken link is found.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class PageScan(HTMLParser):
    """Collect ids, href targets, and src references from one HTML page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.hrefs: list[str] = []
        self.srcs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if a.get("href") is not None:
            self.hrefs.append(a["href"])
        if a.get("src") is not None:
            self.srcs.append(a["src"])


EXTERNAL = re.compile(r"^(https?:|mailto:|data:|//)")


def main() -> int:
    docs = Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
    pages = sorted(docs.glob("*.html"))
    if not pages:
        print(f"no HTML pages found under {docs}/", file=sys.stderr)
        return 1

    scans: dict[str, PageScan] = {}
    for page in pages:
        scan = PageScan()
        scan.feed(page.read_text(encoding="utf-8"))
        scans[page.name] = scan

    errors: list[str] = []
    for name, scan in scans.items():
        for href in scan.hrefs:
            if not href or EXTERNAL.match(href):
                continue
            if href.startswith("#"):  # same-page anchor
                frag = href[1:]
                if frag and frag not in scan.ids:
                    errors.append(f"{name}: broken anchor {href!r}")
                continue
            path, _, frag = href.partition("#")
            target = docs / path
            if not target.exists():
                errors.append(f"{name}: missing target file {href!r}")
                continue
            if frag and target.name in scans and frag not in scans[target.name].ids:
                errors.append(f"{name}: {path} has no id {frag!r} (link {href!r})")
        for src in scan.srcs:
            if not src or EXTERNAL.match(src):
                continue
            if not (docs / src.partition("#")[0]).exists():
                errors.append(f"{name}: missing asset {src!r}")

    if errors:
        print(f"FAIL — {len(errors)} broken link(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    total = sum(len(s.hrefs) + len(s.srcs) for s in scans.values())
    print(f"OK — {len(pages)} page(s), {total} references checked, no broken internal links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
