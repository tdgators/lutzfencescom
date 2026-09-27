# -*- coding: utf-8 -*-
"""Builds one landing page per service-area town."""
from pathlib import Path
from data import SITE, TOWNS, COPY, CURRENT, MATERIALS, FAQS
from templates import write_page, page, page_hero, faq_accordion, town_chips, cta_banner, map_section, fence_illustration, warranty_callout


def write(path, html):
    write_page(CURRENT['out_dir'], path, html)


MATERIAL_SNIPPETS = {
    "vinyl-fence": "vinyl privacy and semi-privacy fencing that never needs painting",
    "wood-fence": "cedar and pressure-treated wood fencing in classic and modern styles",
    "aluminum-fence": "rust-proof aluminum fencing, popular for pool enclosures",
    "chain-link-fence": "budget-friendly galvanized and vinyl-coated chain link",
    "composite-fence": "premium, nearly maintenance-free composite fencing",
    "steel-wrought-iron-fence": "ornamental steel and wrought-iron-style security fencing",
}


def neighbors(idx):
    n = len(TOWNS)
    return [TOWNS[(idx - 1) % n], TOWNS[(idx + 1) % n], TOWNS[(idx + 2) % n]]


TOWN_HERO_KINDS = ["vinyl", "wood", "aluminum", "chain-link", "composite", "steel", "picket", "split-rail"]


def build_towns():
    for i, (name, slug) in enumerate(TOWNS):
        fmt = dict(town=name, state=SITE['state'], state_full=SITE['state_full'], brand=SITE['full_brand'], region=SITE['region'])
        intro = COPY['town_intros'][i % len(COPY['town_intros'])].format(**fmt)
        why = COPY['town_why'][i % len(COPY['town_why'])].format(**fmt)
        permit = COPY['town_permit'][i % len(COPY['town_permit'])].format(**fmt)
        near = neighbors(i)
        near_links = ", ".join(f'<a href="fence-company-{s}-fl.html">{n}</a>' for n, s in near)

        mat_cards = "".join(f'''
<div class="card">
  <div class="tile-img" style="aspect-ratio:16/10;margin-bottom:14px">{fence_illustration(m['img'])}</div>
  <h3>{m['name']}</h3>
  <p>{MATERIAL_SNIPPETS.get(m['slug'], m['tagline'])}, installed for {name} properties.</p>
  <a class="more" href="{m['slug']}.html">Learn More &rarr;</a>
</div>''' for m in MATERIALS[:6])

        town_faqs = [FAQS[5], FAQS[16], FAQS[22], FAQS[24]]

        content = page_hero(f"Serving {name}, {SITE['state']}", f"Fence Company in {name}, {SITE['state']}",
            f"Residential &amp; commercial fence installation, repair, and maintenance for {name} and the surrounding {SITE['region']} area.",
            [("Home", "index.html"), ("Service Areas", "service-areas.html"), (name, None)])

        content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <p>{intro}</p>
        <p>{why}</p>
        <p>{permit}</p>
      </div>
      <div class="tile-img">{fence_illustration(TOWN_HERO_KINDS[i % len(TOWN_HERO_KINDS)])}</div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Materials</div>
      <h2>Fence Materials We Install in {name}</h2>
    </div>
    <div class="grid grid-3">{mat_cards}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split rev">
      <div class="split-media">{map_section()}</div>
      <div>
        <h2>Also Serving Nearby</h2>
        <p>Along with {name}, we regularly work in {near_links}, and dozens of other {SITE['region']}-area communities.</p>
        {town_chips(exclude_slug=slug, limit=12)}
        <div style="margin-top:16px"><a class="btn btn-navy-outline" href="service-areas.html">See All Cities We Serve</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div style="max-width:800px;margin:0 auto">
      <div class="section-head"><h2>{name} Fence FAQs</h2></div>
      {faq_accordion(town_faqs)}
    </div>
  </div>
</section>

{warranty_callout("your fence")}
{cta_banner(f"Ready for a Free {name} Estimate?", f"Call, text, or request a quote online and we'll get right back to you.")}
'''
        title = f"Fence Company in {name}, {SITE['state']} | {SITE['full_brand']}"
        desc = f"{SITE['full_brand']} installs and repairs vinyl, wood, aluminum, chain link, and composite fencing in {name}, {SITE['state']}. Free estimates — call {SITE['phone']}."
        write(f"fence-company-{slug}-fl.html", page(title, desc, f"fence-company-{slug}-fl.html", content))
