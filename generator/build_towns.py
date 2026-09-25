# -*- coding: utf-8 -*-
"""Builds one landing page per service-area town."""
from pathlib import Path
from data import SITE, TOWNS, MATERIALS, FAQS
from templates import page, page_hero, faq_accordion, town_chips, cta_banner, map_section, fence_illustration, warranty_callout

OUT = Path(__file__).resolve().parent.parent

def write(path, html):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")


INTRO_VARIANTS = [
    "When you're ready to add a fence in {town}, you want a contractor who shows up, pulls the right permits, and builds something that holds up to Florida weather for years to come. That's what {brand} does for homeowners and businesses across {town} every week.",
    "Looking for a fence company near {town}, {state}? {brand} installs and repairs residential and commercial fencing throughout {town} and the surrounding {region} area, with free estimates and no pressure.",
    "{brand} is proud to serve {town} with professional fence installation, repair, and maintenance — from a simple backyard privacy fence to a full commercial security perimeter.",
    "Homeowners and businesses in {town} trust {brand} for fence installation because we handle the permitting, the install, and anything that needs fixing down the road, all under one roof.",
]

WHY_VARIANTS = [
    "We're locally owned and operated, backed by the training and manufacturer relationships of the national {brand} network — so you get big-company buying power with small-business accountability.",
    "Every {town} estimate is free, and every installation is backed by the manufacturer's warranty plus our own <a href=\"warranty.html\">76-Week Limited Workmanship Warranty</a>.",
    "We're licensed, bonded, and insured in all 50 states, and we handle the local permitting process for most {town} projects as part of your price.",
]

PERMIT_VARIANTS = [
    "Most fence projects in {state} require a local permit, and if your property has a pool, your fence or gate also needs to meet Florida's residential pool safety barrier code. We handle that process for {town} homeowners so you don't have to.",
    "If you're part of an HOA in {town}, your community likely requires board approval before installation — we're happy to help put together what your HOA needs to review your project.",
]

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
        intro = INTRO_VARIANTS[i % len(INTRO_VARIANTS)].format(
            town=name, state=SITE['state'], brand=SITE['full_brand'], region=SITE['region'])
        why = WHY_VARIANTS[i % len(WHY_VARIANTS)].format(town=name, brand=SITE['full_brand'])
        permit = PERMIT_VARIANTS[i % len(PERMIT_VARIANTS)].format(town=name, state=SITE['state_full'])
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


if __name__ == "__main__":
    build_towns()
    print(f"{len(TOWNS)} town pages done")
