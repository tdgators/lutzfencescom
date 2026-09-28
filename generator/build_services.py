# -*- coding: utf-8 -*-
"""Builds: material pages, materials hub, style pages, styles hub, commercial hub + pages, other-service pages"""
from pathlib import Path
from data import SITE, CURRENT, THEME, T, MATERIALS, STYLES, COMMERCIAL, OTHER_SERVICES, FAQS, TOWNS
from templates import write_page, page, page_hero, faq_accordion, town_chips, cta_banner, map_section, fence_illustration, warranty_callout


def write(path, html):
    write_page(CURRENT['out_dir'], path, html)


def guide_layout():
    return THEME.get("detail_layout") == "guide"


def guide_page(path, crumbs, kicker, name, tagline, c, img_kind, related_title, related, warranty_ctx,
               cta_title, meta_title, meta_desc):
    """Article-style detail page (THEME detail_layout='guide'): intro + titled sections beside an
    "at a glance" sidebar, a wide photo, then related links. `c` is the page's content dict."""
    intro = "".join(f"<p>{p_}</p>" for p_ in c.get("intro", []))
    sections = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p_}</p>" for p_ in ps) for h, ps in c.get("sections", []))
    glance = "".join(f"<li>{g}</li>" for g in c.get("glance", []))
    related_html = "".join(f"""
<a class="card related-card" href="{href}">
  <h3>{title}</h3>
  <p>{blurb}</p>
  <span class="more">{T("labels.read_more", "Read more &rarr;")}</span>
</a>""" for title, href, blurb in related)
    content = page_hero(kicker, name, tagline, crumbs)
    content += f"""
<section class="section">
  <div class="container guide">
    <article class="guide-main">{intro}{sections}</article>
    <aside class="guide-side">
      <div class="card glance">
        <h3>{c.get("glance_title", T("labels.glance", "At a Glance"))}</h3>
        <ul class="check-list">{glance}</ul>
        <a class="btn btn-red btn-block" href="contact-us.html">{T("labels.estimate", "Get a Free Estimate")}</a>
        <a class="glance-phone" href="tel:{SITE['phone_tel']}">{T("labels.or_call", "or call")} {SITE['phone']}</a>
      </div>
    </aside>
  </div>
</section>
<section class="guide-photo">
  <div class="container"><div class="tile-img wide">{fence_illustration(img_kind)}</div></div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><h2>{related_title}</h2></div>
    <div class="grid grid-3">{related_html}</div>
  </div>
</section>
{warranty_callout(warranty_ctx)}
{cta_banner(cta_title, c.get("cta_sub"))}
"""
    write(path, page(meta_title, meta_desc, path, content))


def build_materials():
    # Hub page
    tiles = "".join(f'''
<div class="card">
  <div class="tile-img" style="aspect-ratio:16/10;margin-bottom:14px">{fence_illustration(m['img'])}</div>
  <h3>{m['name']}</h3><p>{T(f"materials.{m['slug']}.tagline", m['tagline'])}</p>
  <a class="more" href="{m['slug']}.html">Learn More &rarr;</a>
</div>''' for m in MATERIALS)
    content = page_hero("Residential", T("materials_hub.title", "Fence Materials"),
        T("materials_hub.lead", f"We install every major fence material — here's how to choose the right one for your {SITE['city']}-area property."),
        [("Home", "index.html"), ("Fence Materials", None)])
    hub_intro = T("materials_hub.intro")
    hub_intro_html = f'<div class="hub-intro">{"".join(f"<p>{p_}</p>" for p_ in hub_intro)}</div>' if hub_intro else ""
    content += f'<section class="section"><div class="container">{hub_intro_html}<div class="grid grid-3">{tiles}</div></div></section>{cta_banner()}'
    write("fence-materials.html", page(f"Fence Materials | {SITE['full_brand']}",
        f"Compare vinyl, wood, aluminum, chain link, composite, and steel fence materials installed by {SITE['full_brand']}.",
        "fence-materials.html", content))

    # Individual material pages
    for m in MATERIALS:
        if guide_layout():
            c = T(f"materials.{m['slug']}")
            others = [x for x in MATERIALS if x["slug"] != m["slug"]][:3]
            guide_page(f"{m['slug']}.html",
                [("Home", "index.html"), ("Fence Materials", "fence-materials.html"), (m["name"], None)],
                "Fence Materials", m["name"], c["tagline"], c, m["img"], T("labels.related_materials", "Compare Other Materials"),
                [(x["name"], f"{x['slug']}.html", T(f"materials.{x['slug']}.tagline")) for x in others],
                f"your {m['short'].lower()} fence", c.get("cta_title", f"Ready for a {m['short']} Fence?"),
                f"{m['name']} Installation in {SITE['city']}, FL | {SITE['full_brand']}", c["meta"])
            continue
        body_html = "".join(f"<p>{p_.replace('{city}', SITE['city'])}</p>" for p_ in m["body"])
        features_html = "".join(f"<li>{f}</li>" for f in m["features"])
        other_mats = [x for x in MATERIALS if x["slug"] != m["slug"]][:4]
        related = "".join(f'''
<div class="card">
  <div class="tile-img" style="aspect-ratio:16/10;margin-bottom:14px">{fence_illustration(x['img'])}</div>
  <h3>{x['name']}</h3><p>{x['tagline']}</p>
  <a class="more" href="{x['slug']}.html">Learn More &rarr;</a>
</div>''' for x in other_mats)

        content = page_hero("Fence Materials", m["name"], m["tagline"],
            [("Home", "index.html"), ("Fence Materials", "fence-materials.html"), (m["name"], None)])
        content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>{body_html}</div>
      <div class="tile-img">{fence_illustration(m['img'])}</div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><h2>{m['name']} Features</h2></div>
    <div class="grid grid-2"><ul style="font-size:1rem">{features_html}</ul>
    <div>
      <h3>Serving {SITE['city']} &amp; Nearby Communities</h3>
      <p>We install {m['short'].lower()} fencing throughout {SITE['city']} and the surrounding {SITE['region']} area.</p>
      {town_chips(limit=10)}
    </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head"><h2>Other Fence Materials</h2></div>
    <div class="grid grid-4">{related}</div>
  </div>
</section>
{warranty_callout(f"your {m['short'].lower()} fence").replace('section warranty-strip', 'section section-alt warranty-strip')}
{cta_banner(f"Ready for a {m['short']} Fence?", "Get a free, no-obligation estimate for your property.")}
'''
        write(f"{m['slug']}.html", page(f"{m['name']} Installation | {SITE['full_brand']}",
            f"{m['tagline']} Professional {m['short'].lower()} fence installation in {SITE['city']}, FL by {SITE['full_brand']}.",
            f"{m['slug']}.html", content))


def build_styles():
    tiles = "".join(f'''
<div class="card"><h3>{s['name']}</h3><p>{T(f"styles.{s['slug']}.desc", s['desc'])}</p>
<a class="more" href="{s['slug']}.html">Learn More &rarr;</a></div>''' for s in STYLES)
    content = page_hero("Residential", T("styles_hub.title", "Fence Styles"), T("styles_hub.lead", f"The most common fence styles we build for homeowners across the {SITE['region']} area."),
        [("Home", "index.html"), ("Fence Styles", None)])
    content += f'<section class="section"><div class="container"><div class="grid grid-3">{tiles}</div></div></section>{cta_banner()}'
    write("fence-styles.html", page(f"Fence Styles | {SITE['full_brand']}",
        f"Privacy, semi-privacy, horizontal, picket, and split rail fence styles installed by {SITE['full_brand']}.",
        "fence-styles.html", content))

    style_kind = {
        "privacy-fence": "vinyl", "semi-privacy-fence": "composite", "horizontal-fence": "horizontal",
        "picket-fence": "picket", "split-rail-fence": "split-rail",
    }
    for s in STYLES:
        if guide_layout():
            c = T(f"styles.{s['slug']}")
            others = [x for x in STYLES if x["slug"] != s["slug"]][:3]
            guide_page(f"{s['slug']}.html",
                [("Home", "index.html"), ("Fence Styles", "fence-styles.html"), (s["name"], None)],
                "Fence Styles", s["name"], c["tagline"], c, style_kind.get(s['slug'], 'vinyl'), T("labels.related_styles", "Other Styles to Consider"),
                [(x["name"], f"{x['slug']}.html", T(f"styles.{x['slug']}.desc")) for x in others],
                f"your {s['name'].lower()}", c.get("cta_title", f"Planning a {s['name']}?"),
                f"{s['name']} Installation in {SITE['city']}, FL | {SITE['full_brand']}", c["meta"])
            continue
        mat_tiles = "".join(f'''<div class="card">
<div class="tile-img" style="aspect-ratio:16/10;margin-bottom:14px">{fence_illustration(m['img'])}</div>
<h3>{m['name']}</h3><a class="more" href="{m['slug']}.html">Learn More &rarr;</a></div>''' for m in MATERIALS[:4])
        content = page_hero("Fence Styles", s["name"], s["desc"],
            [("Home", "index.html"), ("Fence Styles", "fence-styles.html"), (s["name"], None)])
        content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div><p>{s['desc']}</p><p>We build {s['name'].lower()}s in multiple materials — pick the look and budget that's right for your property, and we'll help you choose the best material for the job.</p></div>
      <div class="tile-img">{fence_illustration(style_kind.get(s['slug'], 'vinyl'))}</div>
    </div>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-head"><h2>Available Materials</h2></div>
    <div class="grid grid-4">{mat_tiles}</div>
  </div>
</section>
{warranty_callout(f"your {s['name'].lower()}")}
{cta_banner()}
'''
        write(f"{s['slug']}.html", page(f"{s['name']} Installation | {SITE['full_brand']}",
            f"{s['desc'][:140]} Installed by {SITE['full_brand']} in {SITE['city']}, FL.",
            f"{s['slug']}.html", content))


def build_commercial():
    tiles = "".join(f'''<div class="card"><h3>{c['name']}</h3><p>{T(f"commercial.{c['slug']}.desc", c['desc'])}</p>
<a class="more" href="{c['slug']}.html">Learn More &rarr;</a></div>''' for c in COMMERCIAL)
    content = page_hero("Commercial", T("commercial_hub.title", "Commercial Fence Contractor"),
        T("commercial_hub.lead", f"We handle commercial and industrial fencing projects of every size across {SITE['city']} and the {SITE['region']} area — from a single gate repair to a full-site security perimeter."),
        [("Home", "index.html"), ("Commercial Fencing", None)])
    content += f'''
<section class="section">
  <div class="container">
    <p style="max-width:760px">{T("commercial_hub.intro", "Unlike the large national fence outfits, our clients aren't just a number in a queue. We install aluminum, chain link, steel, vinyl, and wood commercial fencing, with chain link the most common choice for its durability and cost — 6' to 8' heights are typical for commercial applications, with security fencing running taller. We also handle commercial gate systems, including cantilever slide gates for sites like warehouses, schools, and government or utility facilities.")}</p>
    <div class="grid grid-4">{tiles}</div>
  </div>
</section>
{warranty_callout("your fence").replace('section warranty-strip', 'section section-alt warranty-strip')}
{cta_banner("Need a Commercial Quote?", "Tell us about your property and we'll put together a free estimate.")}
'''
    write("commercial-fencing.html", page(f"Commercial Fencing | {SITE['full_brand']}",
        f"Commercial and industrial fence installation, repair, and security fencing in {SITE['city']}, FL and the {SITE['region']} area.",
        "commercial-fencing.html", content))

    commercial_kind = {
        "industrial-fencing": "chain-link", "security-fencing": "security",
        "hoa-fencing": "aluminum", "dumpster-enclosures": "vinyl",
    }
    for c in COMMERCIAL:
        if guide_layout():
            cc = T(f"commercial.{c['slug']}")
            others = [x for x in COMMERCIAL if x["slug"] != c["slug"]][:3]
            guide_page(f"{c['slug']}.html",
                [("Home", "index.html"), ("Commercial Fencing", "commercial-fencing.html"), (c["name"], None)],
                "Commercial", c["name"], cc["tagline"], cc, commercial_kind.get(c['slug'], 'chain-link'), T("labels.related_commercial", "More Commercial Services"),
                [(x["name"], f"{x['slug']}.html", T(f"commercial.{x['slug']}.desc")) for x in others],
                "your fence", cc.get("cta_title", "Need a Commercial Quote?"),
                f"{c['name']} in {SITE['city']}, FL | {SITE['full_brand']}", cc["meta"])
            continue
        content = page_hero("Commercial", c["name"], c["desc"],
            [("Home", "index.html"), ("Commercial Fencing", "commercial-fencing.html"), (c["name"], None)])
        content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div><p>{c['desc']}</p><p>We serve {SITE['city']} and the greater {SITE['region']} area for {c['name'].lower()} projects of any size, with free estimates and a dedicated point of contact from quote through completion.</p></div>
      <div class="tile-img">{fence_illustration(commercial_kind.get(c['slug'], 'chain-link'))}</div>
    </div>
  </div>
</section>
{warranty_callout("your fence").replace('section warranty-strip', 'section section-alt warranty-strip')}
{cta_banner()}
'''
        write(f"{c['slug']}.html", page(f"{c['name']} | {SITE['full_brand']}",
            f"{c['desc'][:150]}", f"{c['slug']}.html", content))


def build_other_services():
    other_kind = {
        "fence-repair": "wood", "fence-staining": "wood", "artificial-grass": "split-rail",
        "diy-fence": "picket", "deck-railing": "composite", "retaining-walls": "split-rail",
    }
    for o in OTHER_SERVICES:
        if guide_layout():
            c = T(f"other.{o['slug']}")
            others = [x for x in OTHER_SERVICES if x["slug"] != o["slug"]][:3]
            guide_page(f"{o['slug']}.html",
                [("Home", "index.html"), ("Other Services", None), (o["name"], None)],
                "Services", o["name"], c["tagline"], c, other_kind.get(o['slug'], 'wood'), T("labels.related_other", "Other Ways We Can Help"),
                [(x["name"], f"{x['slug']}.html", T(f"other.{x['slug']}.tagline")) for x in others],
                "your fence", c.get("cta_title", "Let's Talk About Your Project"),
                f"{o['name']} in {SITE['city']}, FL | {SITE['full_brand']}", c["meta"])
            continue
        body_html = "".join(f"<p>{p_}</p>" for p_ in o["body"])
        content = page_hero("Services", o["name"], o["tagline"],
            [("Home", "index.html"), ("Other Services", None), (o["name"], None)])
        content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>{body_html}<p>Serving {SITE['city']} and the surrounding {SITE['region']} area.</p></div>
      <div class="tile-img">{fence_illustration(other_kind.get(o['slug'], 'wood'))}</div>
    </div>
  </div>
</section>
{cta_banner()}
'''
        write(f"{o['slug']}.html", page(f"{o['name']} | {SITE['full_brand']}",
            f"{o['tagline']} {o['name']} service from {SITE['full_brand']} in {SITE['city']}, FL.",
            f"{o['slug']}.html", content))
