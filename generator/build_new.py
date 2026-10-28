# -*- coding: utf-8 -*-
"""Builds the P1 pages in new_pages.py (pool fences, pool inspection guide, gates, driveway
gates, dog fences, fence replacement, storm/hurricane repair) for the current site."""
from data import SITE, CURRENT, T
from build_services import guide_page
from new_pages import BASE, RELATED_LABELS
from content.new_local import LOCAL
from content.new_variants import VARIANTS


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
