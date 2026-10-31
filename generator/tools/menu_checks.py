"""Write menu_checks.json: for each site, the nav menu -> submenu path to the newer pages and
headings that should be on each page. Reads the built HTML, so run it after build_all.py.

Run: python3 tools/menu_checks.py
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sites import SITES

PAGES = ["pool-fence", "pool-fence-inspection-florida", "fence-gates", "driveway-gates", "dog-fence",
         "fence-replacement", "hurricane-fence-repair", "fence-care", "reviews", "financing"]
BOILERPLATE = ("Common Questions", "Related Pages", "Ready to", "Warranty", "Had Us Build")
FIXED = {  # pages whose headings come from shared templates
    "reviews": ["Google: Lutz Office", "Google: Tampa Office", "Facebook"],
    "financing": ["Wisetack", "Four Simple Steps", "The Fine Print"],
}
OUT = Path(__file__).resolve().parent.parent / "menu_checks.json"


def text(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def nav_map(index_html):
    """href -> (top menu label, link text), from the primary nav."""
    nav = index_html[index_html.find('<nav class="primary-nav"'):index_html.find("</nav>")]
    out = {}
    for li in re.findall(r"<li[^>]*>(.*?)</li>", nav, re.S):
        top = re.search(r'<button class="nav-toggle"[^>]*>(.*?)<span', li, re.S)
        if not top:
            continue
        for href, label in re.findall(r'<a href="([^"]+)">(.*?)</a>', li, re.S):
            out.setdefault(href.strip("/"), (text(top.group(1)), text(label)))
    return out


def page_checks(slug, body):
    if slug in FIXED:
        return FIXED[slug]
    h2s = [text(h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S)]
    checks = [h for h in h2s if not h.startswith(BOILERPLATE)][:3]
    if "Common Questions" in h2s:
        checks += ["Common Questions"]
    return checks


def main():
    sites = []
    for domain, cfg in SITES.items():
        out_dir = cfg["out_dir"]
        nav = nav_map((out_dir / "index.html").read_text())
        items = []
        for slug in PAGES:
            page = out_dir / slug / "index.html"
            if slug not in nav or not page.exists():
                sys.exit(f"{domain}: {slug} is not in the menu or not built")
            raw = page.read_text()
            body = raw[raw.find("</header>"):raw.find("<footer")]
            checks = page_checks(slug, body)
            plain = text(body)
            missing = [c for c in checks if c not in plain]
            if missing:
                sys.exit(f"{domain}/{slug}: check text not on page: {missing}")
            menu, submenu = nav[slug]
            items.append(dict(menu=menu, submenu=submenu, onPageChecks=checks))
        sites.append(dict(site=domain, url=f"https://{domain}/", menuItems=items))
    OUT.write_text(json.dumps(dict(websites=sites), indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUT} ({len(sites)} sites, {len(PAGES)} items each)")


if __name__ == "__main__":
    main()
