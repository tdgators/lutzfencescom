# -*- coding: utf-8 -*-
"""Builds sitemap.xml and robots.txt from the pages written during this build.

Each URL's <lastmod> only changes when that page's HTML actually changes: content
hashes and dates are kept in sitemap-state.json (commit it along with the site)."""
import hashlib, json
from datetime import date
from pathlib import Path
from data import SITE
from templates import WRITTEN_PAGES

OUT = Path(__file__).resolve().parent.parent
STATE = Path(__file__).resolve().parent / "sitemap-state.json"


def build_sitemap():
    if not WRITTEN_PAGES:
        raise SystemExit("No pages were built — run build_all.py, not build_sitemap.py directly.")
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    today = date.today().isoformat()
    new_state = {}
    for url, html in WRITTEN_PAGES.items():
        digest = hashlib.sha256(html.encode("utf-8")).hexdigest()
        prev = state.get(url)
        lastmod = prev["lastmod"] if prev and prev["hash"] == digest else today
        new_state[url] = {"hash": digest, "lastmod": lastmod}
    # Homepage first, then alphabetical
    urls = sorted(new_state, key=lambda u: (u != "/", u))
    entries = "".join(
        f"  <url>\n    <loc>https://{SITE['domain']}{u}</loc>\n    <lastmod>{new_state[u]['lastmod']}</lastmod>\n  </url>\n"
        for u in urls)
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: https://{SITE['domain']}/sitemap.xml\n", encoding="utf-8")
    STATE.write_text(json.dumps({u: new_state[u] for u in urls}, indent=1) + "\n")
    print(f"wrote sitemap.xml ({len(urls)} URLs) and robots.txt")
