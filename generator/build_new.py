# -*- coding: utf-8 -*-
"""Builds the P1 pages in new_pages.py (pool fences, pool inspection guide, gates, driveway
gates, dog fences, fence replacement, storm/hurricane repair) for the current site."""
from data import SITE, CURRENT, T
from articles import ARTICLES, SHARED_GUIDES
from build_services import guide_page, write
from new_pages import BASE, RELATED_LABELS
from templates import cta_banner, page, page_hero
from content.new_local import LOCAL
from content.new_variants import VARIANTS
from content import puppy_picket

for _site, _copy in puppy_picket.LOCAL.items():  # per-site copy for the puppy picket page
    LOCAL[_site]["puppy-picket-fence"] = _copy
for _site, _copy in puppy_picket.VARIANTS.items():
    VARIANTS[_site]["puppy-picket-fence"] = _copy


def _label(slug):
    if slug in BASE:
        return BASE[slug]["name"], LOCAL[CURRENT["content"]][slug]["tagline"]
    return RELATED_LABELS[slug]


def build_new_pages():
    local = LOCAL[CURRENT["content"]]
    fmt = dict(city=SITE["city"], brand=SITE["full_brand"])
    for slug, b in BASE.items():
        lc = local[slug]
        title, paras = lc["local"]
        v = VARIANTS.get(CURRENT["content"], {}).get(slug, b)  # the site's rewrite of the shared body
        sections = list(v["sections"])
        sections.insert(1, (title, paras))  # the site's own section, after the opening one
        c = dict(intro=lc["intro"], sections=sections, glance=v["glance"], faqs=v["faqs"],
                 photo_alt=b["photo_alt"], cta_sub=lc.get("cta_sub"))
        crumbs = [("Home", "index.html"), (b["kicker"], None), (b["name"], None)]
        related = [(*_label(r), f"{r}.html") for r in b["related"][:3]]
        related = [(t, href, blurb) for t, blurb, href in related]
        guide_page(f"{slug}.html", crumbs, b["kicker"], b["name"], lc["tagline"], c, b["photo"],
                   T("labels.related_new", "Related Pages"), related, "your fence",
                   lc.get("cta_title", "Ready to Get Started?"),
                   b["meta_title"].format(**fmt), b["meta"].format(**fmt))


def build_articles():
    """The articles this site carries, then its /fence-guides/ hub."""
    site = CURRENT["content"]
    fmt = dict(city=SITE["city"], brand=SITE["full_brand"])
    guides = []
    for slug, a in ARTICLES.items():
        if site not in a["sites"]:
            continue
        v = a["sites"][site]
        crumbs = [("Home", "index.html"), ("Fence Guides", "fence-guides.html"), (v["name"], None)]
        c = dict(intro=v["intro"], sections=v["sections"], glance=v["glance"], faqs=v["faqs"], photo_alt=a["photo_alt"])
        guide_page(f"{slug}.html", crumbs, a["kicker"], v["name"], v["tagline"], c, a["photo"],
                   T("labels.related_new", "Related Pages"), v["related"], "your fence", "Ready to Get Started?",
                   v["meta_title"].format(**fmt), v["meta"].format(**fmt))
        guides.append((v["name"], f"{slug}.html", a["blurb"]))
    cards = "".join(f"""
<a class="card related-card" href="{href}">
  <h3>{title}</h3>
  <p>{blurb}</p>
  <span class="more">{T("labels.read_more", "Read more &rarr;")}</span>
</a>""" for title, href, blurb in guides + SHARED_GUIDES)
    content = page_hero("Resources", "Fence Guides", f"Plain answers for {SITE['city']}-area fence projects.",
                        [("Home", "index.html"), ("Fence Guides", None)])
    content += f'<section class="section"><div class="container"><div class="grid grid-3">{cards}</div></div></section>{cta_banner()}'
    write("fence-guides.html", page(f"Fence Guides for {SITE['city']}, FL | {SITE['full_brand']}",
                                    f"Fence guides for {SITE['city']}-area homes and businesses, from {SITE['full_brand']}.",
                                    "fence-guides.html", content))
