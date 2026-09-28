# -*- coding: utf-8 -*-
"""Builds: homepage, about, service-areas, contact, faq, gallery, pricing, privacy-policy"""
from pathlib import Path
from data import SITE, TOWNS, COPY, CURRENT, THEME, T, MATERIALS, STYLES, COMMERCIAL, OTHER_SERVICES, FAQS, PRICING_TABLE, WARRANTY
from templates import write_page, write_404, page, page_hero, faq_accordion, mini_quote_form, contact_form_card, map_section, town_chips, cta_banner, fence_illustration, warranty_seal, warranty_callout


def write(path, html):
    write_page(CURRENT['out_dir'], path, html)


def sec_head(eyebrow, title, intro=None):
    intro_html = f"\n      <p>{intro}</p>" if intro else ""
    return f"""<div class="section-head">
      <div class="eyebrow">{eyebrow}</div>
      <h2>{title}</h2>{intro_html}
    </div>"""


def section(inner, alt=False, extra_cls=""):
    cls = "section" + (" section-alt" if alt else "") + (f" {extra_cls}" if extra_cls else "")
    return f"""
<section class="{cls}">
  <div class="container">
    {inner}
  </div>
</section>
"""


def site_faqs():
    """The FAQ list for this site: its own (content FAQ) or local extras + the shared defaults."""
    return T("faqs") or (COPY['local_faqs'] + FAQS)


# ---------------------------------------------------------------- HOMEPAGE sections
def home_hero():
    variant = THEME.get("hero", "split")
    eyebrow = T("home.hero.eyebrow", SITE['full_brand'])
    h1 = T("home.hero.h1", f"The Trusted Fence Company in {SITE['city']}, {SITE['state']}")
    lead = T("home.hero.lead", COPY['hero_lead'])
    badges = T("home.hero.badges", ["Licensed &amp; Fully Insured", "Free Estimates",
        '<a href="warranty.html" style="color:inherit">76-Week Workmanship Warranty</a>', "Family Owned &amp; Locally Operated"])
    badges_html = "".join(f'\n        <div class="hero-badge"><span class="dot"></span>{b}</div>' for b in badges)
    photo = THEME.get("hero_image")
    style = f' style="--hero-photo:url(\'/assets/images/{photo}\')"' if photo else ""
    text = f"""<div>
      <div class="eyebrow">{eyebrow}</div>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="cta-row">
        <a class="btn btn-red" href="contact-us.html">{T("home.hero.cta", "Get a Free Estimate")}</a>
        <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
      </div>
      <div class="hero-badges">{badges_html}
      </div>
    </div>"""
    if variant == "centered":  # headline only; the estimate form gets its own section further down
        return f"""
<section class="hero hero-centered{' hero-photo' if photo else ''}"{style}>
  <div class="container">
    {text}
  </div>
</section>
"""
    cls = "hero hero-photo" if variant == "image" and photo else "hero"
    return f"""
<section class="{cls}"{style}>
  <div class="container">
    {text}
    {mini_quote_form()}
  </div>
</section>
"""


def home_services(alt=False):
    tiles = "".join(f"""
<div class="card">
  <div class="tile-img" style="aspect-ratio:16/10;margin-bottom:14px">{fence_illustration(m['img'])}</div>
  <h3>{m['name']}</h3>
  <p>{T(f"materials.{m['slug']}.tagline", m['tagline'])}</p>
  <a class="more" href="{m['slug']}.html">{T("home.services.more", "Learn More &rarr;")}</a>
</div>""" for m in MATERIALS)
    return section(sec_head(T("home.services.eyebrow", "What We Install"),
        T("home.services.title", f"Fencing Services in {SITE['city']} &amp; the {SITE['region']} Area"),
        T("home.services.intro", "From a simple backyard privacy fence to a full commercial security perimeter, we install and stand behind every material we offer."))
        + f'\n    <div class="grid grid-3">{tiles}</div>', alt)


def home_local(alt=False):
    sec = T("home.local", COPY.get('local_section'))
    if not sec:
        return ""
    cards = "".join(f"""
<div class="card">
  <h3>{t}</h3>
  <p>{d}</p>
</div>""" for t, d in sec['cards'])
    return section(sec_head(sec['eyebrow'], sec['title'], sec['intro']) + f'\n    <div class="grid grid-4">{cards}</div>', alt)


GALLERY_TILES = [
    ("Vinyl Privacy Fence", "vinyl", "vinyl-fence.html"), ("Aluminum Pool Enclosure", "aluminum", "aluminum-fence.html"),
    ("Wood Privacy Fence", "wood", "wood-fence.html"), ("Chain Link Install", "chain-link", "chain-link-fence.html"),
    ("Composite Fence", "composite", "composite-fence.html"), ("Commercial Security Fence", "security", "security-fencing.html"),
    ("Picket Fence", "picket", "picket-fence.html"), ("HOA Community Fencing", "steel", "hoa-fencing.html"),
]


def home_gallery(alt=True):
    tiles = "".join(f"""
<a class="tile-img tile-link" href="{href}">{fence_illustration(kind)}
  <div class="tile-label">{label} &rarr;</div>
</a>""" for label, kind, href in T("home.gallery.tiles", GALLERY_TILES))
    return section(sec_head(T("home.gallery.eyebrow", "Our Work"),
        T("home.gallery.title", f"Recent {SITE['city']}-Area Fence Installations"),
        T("home.gallery.intro", "We're building out our full photo gallery of local installs — in the meantime, here's a look at the styles and materials we install most."))
        + f'\n    <div class="grid grid-4">{tiles}</div>'
        + f'\n    <div class="center" style="margin-top:28px"><a class="btn btn-navy-outline" href="fence-gallery.html">{T("home.gallery.button", "View Full Gallery")}</a></div>', alt)


def home_why(alt=False):
    items = T("home.why.items", [
        ("Licensed &amp; Fully Insured", f"Licensed in {SITE['licensed_in']}, with general liability and workers' compensation insurance on every job."),
        ("Free Estimates", "Every estimate is free, with no obligation and no pressure."),
        ("76-Week Workmanship Warranty", "Every installation is backed by our <a href=\"warranty.html\">76-Week Limited Workmanship Warranty</a>, plus the manufacturer's warranty on materials."),
        COPY['why_local'],
        ("We Handle Your Permit", "In most cases we manage the local permitting process for you, included in your price."),
        ("Flexible Financing", "Ask about flexible financing options to make your project fit your budget."),
    ])
    cards = "".join(f"""
<div class="card">
  <div class="icon">✓</div>
  <h3>{t}</h3>
  <p>{d}</p>
</div>""" for t, d in items)
    return section(sec_head(T("home.why.eyebrow", "Why 76 FENCE"),
        T("home.why.title", f"Why Homeowners Choose {SITE['full_brand']}"),
        T("home.why.intro", f"We're part of the {SITE['brand']} network — bringing national buying power and manufacturer relationships to a locally owned, locally operated business."))
        + f'\n    <div class="grid grid-3">{cards}</div>', alt)


def home_warranty(alt=True):
    html = warranty_callout()
    return html.replace('section warranty-strip', 'section section-alt warranty-strip') if alt else html


def pricing_table():
    first_size = list(PRICING_TABLE.keys())[0]
    header_cols = "".join(f"<th>{m}</th>" for m in PRICING_TABLE[first_size].keys())
    rows = "".join(f"<tr><td>{size}</td>" + "".join(f"<td>{v}</td>" for v in mats.values()) + "</tr>"
                   for size, mats in PRICING_TABLE.items())
    return f"""<div class="table-scroll"><table class="pricing">
          <tr><th>Yard Size</th>{header_cols}</tr>
          {rows}
        </table></div>"""


def home_pricing(alt=True):
    return section(f"""<div class="split">
      <div>
        <div class="eyebrow">{T("home.pricing.eyebrow", "Pricing")}</div>
        <h2>{T("home.pricing.title", "What Does a Fence Cost?")}</h2>
        <p>{T("home.pricing.intro", f"Every project is different, but here's a general idea of what {SITE['city']}-area homeowners typically invest based on yard size and material. Get a free, no-obligation quote for exact pricing on your property.")}</p>
        <a class="btn btn-blue" href="fence-pricing.html">{T("home.pricing.button", "See Full Pricing Breakdown")}</a>
      </div>
      <div>
        {pricing_table()}
        <p class="small" style="margin-top:10px">Estimates only. Actual pricing depends on linear footage, material, gates, and site conditions.</p>
      </div>
    </div>""", alt)


def home_commercial(alt=False):
    tiles = "".join(f"""
<div class="card">
  <h3>{c['name']}</h3>
  <p>{T(f"commercial.{c['slug']}.desc", c['desc'])}</p>
  <a class="more" href="{c['slug']}.html">Learn More &rarr;</a>
</div>""" for c in COMMERCIAL)
    return section(sec_head(T("home.commercial.eyebrow", "Commercial"),
        T("home.commercial.title", "Commercial &amp; Industrial Fencing"),
        T("home.commercial.intro", "We handle commercial fencing projects of every size — from a single dumpster enclosure to a full industrial security perimeter."))
        + f'\n    <div class="grid grid-4">{tiles}</div>'
        + '\n    <div class="center" style="margin-top:28px"><a class="btn btn-navy-outline" href="commercial-fencing.html">See All Commercial Services</a></div>', alt)


def home_diy(alt=True):
    tiles = "".join(f"""
<div class="card">
  <h3>{t}</h3><p>{d}</p>
</div>""" for t, d in T("home.diy.tiles", [
        ("Materials Only", "Buy fence materials at contractor pricing and install it yourself."),
        ("Post Hole Digging", "We dig the holes; you handle the rest of the build."),
        ("Installation Consultation", "A paid on-site visit to plan layout, materials, and permitting before you start."),
    ]))
    return section(sec_head(T("home.diy.eyebrow", "DIY"), T("home.diy.title", "Building Your Own Fence?"),
        T("home.diy.intro", "Not every project needs a full install — here's how we can help without taking over the whole job."))
        + f'\n    <div class="grid grid-3">{tiles}</div>'
        + '\n    <div class="center" style="margin-top:24px"><a class="btn btn-blue" href="diy-fence.html">Ask About DIY</a></div>', alt)


def home_reviews(alt=False):
    return section(sec_head(T("home.reviews.eyebrow", "Reviews"),
        T("home.reviews.title", f"See What {SITE['city']}-Area Customers Are Saying"),
        T("home.reviews.intro", "Read our latest reviews on Google and Facebook, or leave us one of your own after your project."))
        + f"""
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-navy-outline" href="{SITE['google']}" target="_blank" rel="noopener">Read Our Google Reviews</a>
      <a class="btn btn-navy-outline" href="{SITE['fb']}" target="_blank" rel="noopener">Read Our Facebook Reviews</a>
    </div>""", alt)


def home_areas(alt=True):
    return section(f"""<div class="split rev">
      <div class="split-media">{map_section()}</div>
      <div>
        <div class="eyebrow">{T("home.areas.eyebrow", "Service Area")}</div>
        <h2>{T("home.areas.title", f"Proudly Serving {SITE['city']} &amp; the {SITE['region']} Area")}</h2>
        <p>{T("home.areas.intro", f"We install and repair fences throughout {SITE['city']} and dozens of surrounding communities.")}</p>
        {town_chips(limit=14)}
        <div style="margin-top:20px"><a class="btn btn-blue" href="service-areas.html">See All Cities We Serve</a></div>
      </div>
    </div>""", alt)


def home_faq(alt=False):
    return section(sec_head(T("home.faq.eyebrow", "FAQ"), T("home.faq.title", "Frequently Asked Questions")) + f"""
    <div style="max-width:800px;margin:0 auto">
      {faq_accordion(site_faqs()[:6], open_first=True)}
      <div class="center" style="margin-top:24px"><a class="btn btn-navy-outline" href="faq.html">See All FAQs</a></div>
    </div>""", alt)


def home_process(alt=False):
    sec = T("home.process")
    steps = "".join(f"""
<div class="card">
  <h3>{t}</h3>
  <p>{d}</p>
</div>""" for t, d in sec['steps'])
    return section(sec_head(sec['eyebrow'], sec['title'], sec.get('intro')) + f'\n    <div class="grid grid-4 steps">{steps}</div>', alt)


def home_styles(alt=False):
    sec = T("home.styles")
    tiles = "".join(f"""
<a class="card style-card" href="{s['slug']}.html">
  <h3>{s['name']}</h3>
  <p>{T(f"styles.{s['slug']}.desc", s['desc'])}</p>
  <span class="more">{sec.get('more', 'See the style &rarr;')}</span>
</a>""" for s in STYLES)
    return section(sec_head(sec['eyebrow'], sec['title'], sec.get('intro')) + f'\n    <div class="grid grid-3">{tiles}</div>', alt)


def home_estimate(alt=True):
    sec = T("home.estimate")
    points = "".join(f"<li>{p_}</li>" for p_ in sec.get('points', []))
    return section(f"""<div class="split estimate-split">
      <div>
        <div class="eyebrow">{sec['eyebrow']}</div>
        <h2>{sec['title']}</h2>
        <p>{sec['intro']}</p>
        <ul class="check-list">{points}</ul>
      </div>
      {contact_form_card()}
    </div>""", alt)


def home_budget(alt=False):
    sec = T("home.budget")
    cards = "".join(f"""
<div class="card">
  <h3>{t}</h3>
  <p>{d}</p>
</div>""" for t, d in sec['cards'])
    return section(sec_head(sec['eyebrow'], sec['title'], sec.get('intro')) + f'\n    <div class="grid grid-3">{cards}</div>'
        + f'\n    <div class="center" style="margin-top:24px"><a class="btn btn-blue" href="fence-pricing.html">{sec.get("button", "See Typical Pricing")}</a></div>', alt)


HOME_SECTIONS = {
    "services": home_services, "local": home_local, "gallery": home_gallery, "why": home_why,
    "warranty": home_warranty, "pricing": home_pricing, "commercial": home_commercial, "diy": home_diy,
    "reviews": home_reviews, "areas": home_areas, "faq": home_faq, "process": home_process,
    "styles": home_styles, "estimate": home_estimate, "budget": home_budget,
}
# Lutz's layout; a site's THEME['home_sections'] lists its own (section, alt background) order.
DEFAULT_HOME = [("services", False), ("local", False), ("gallery", True), ("why", False), ("warranty", True),
                ("pricing", True), ("commercial", False), ("diy", True), ("reviews", False), ("areas", True), ("faq", False)]


def build_home():
    body = "".join(HOME_SECTIONS[name](alt) for name, alt in THEME.get("home_sections", DEFAULT_HOME))
    content = home_hero() + body + f"\n{cta_banner()}\n"
    write("index.html", page(
        T("home.meta_title", f"{SITE['full_brand']} | Fence Company in {SITE['city']}, {SITE['state']}"),
        T("home.meta_description", f"{SITE['full_brand']} installs and repairs vinyl, wood, aluminum, chain link, composite, and steel fencing for homes and businesses in {SITE['city']}, FL and the greater {SITE['region']} area. Free estimates — call {SITE['phone']}."),
        "index.html", content))


# ---------------------------------------------------------------- ABOUT
def build_about():
    content = page_hero("About Us", T("about.title", f"Meet the {SITE['full_brand']} Team"),
        T("about.lead", COPY['about_lead']),
        [("Home", "index.html"), ("About", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">{T("about.story_eyebrow", "Our Story")}</div>
        <h2>{T("about.story_title", "Local Ownership. National Backing.")}</h2>
        {"".join(f"<p>{p_}</p>" for p_ in T("about.story", COPY['about_story']))}
      </div>
      <div class="tile-img"><img src="assets/images/team/tom-kate-donnelly.jpg" alt="Tom and Kate Donnelly, owners of {SITE['full_brand']}, in front of their branded truck" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">{T("about.owners_eyebrow", "Ownership")}</div>
      <h2>{T("about.owners_title", "Meet the Owners")}</h2>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <h3>Tom Donnelly &mdash; Owner</h3>
        <p>{T("about.tom", f"Tom brings over 20 years of experience in information technology within the finance and banking industries, having served as both a principal engineer and a people leader managing global teams. As owner of {SITE['full_brand']}, Tom is focused on building a trusted, locally operated business that delivers exceptional craftsmanship and customer service, bringing the strength and professionalism of the {SITE['brand']} brand to the {SITE['city']} community.")}</p>
      </div>
      <div class="card">
        <h3>Kate Donnelly &mdash; Owner</h3>
        <p>{T("about.kate", f"Kate brings over 20 years of experience serving the federal government as an intelligence analyst, with a master's degree and deep experience in strategic analysis and attention to detail. As owner of {SITE['full_brand']}, Kate is committed to building a business grounded in integrity, operational excellence, and outstanding customer service for every {SITE['city']}-area project.")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-4 center">
      <div class="badge">Licensed — {SITE['licensed_short']}</div>
      <div class="badge">Fully Insured</div>
      <a class="badge" href="warranty.html">76-Week Workmanship Warranty</a>
      <div class="badge">Family Owned &amp; Operated</div>
    </div>
  </div>
</section>

{cta_banner(T("about.cta_title", "Ready to Work With Us?"), T("about.cta_sub", f"Get a free estimate from the {SITE['full_brand']} team today."))}
'''
    write("about-us.html", page(f"Meet the Team | {SITE['full_brand']}",
        T("about.meta", f"Meet Tom and Kate Donnelly, the owners of {SITE['full_brand']}, a locally owned fence company serving {SITE['city']}, FL and the {SITE['region']} area."),
        "about-us.html", content))


# ---------------------------------------------------------------- SERVICE AREAS
def build_service_areas():
    content = page_hero("Service Areas", T("areas.title", f"Cities We Serve Near {SITE['city']}, {SITE['state']}"),
        T("areas.lead", f"{SITE['full_brand']} provides fence installation, repair, and maintenance across {SITE['city']} and the entire {SITE['region']} region."),
        [("Home", "index.html"), ("Service Areas", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <h2>{T("areas.h2", "Proudly Serving the Following Communities")}</h2>
        <p>{T("areas.intro", "Don't see your city listed? Give us a call — we likely still serve your area.")}</p>
        {town_chips()}
      </div>
      <div>{map_section()}</div>
    </div>
  </div>
</section>
{cta_banner()}
'''
    write("service-areas.html", page(f"Service Areas | {SITE['full_brand']}",
        COPY['service_areas_meta'],
        "service-areas.html", content))


# ---------------------------------------------------------------- CONTACT
def build_contact():
    content = page_hero("Contact Us", T("contact.title", "Get Your Free Fence Estimate"),
        T("contact.lead", f"Call, text, or send us a message and the {SITE['full_brand']} team will get back to you fast."),
        [("Home", "index.html"), ("Contact", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      {contact_form_card()}
      <div>
        <h3>Other Ways to Reach Us</h3>
        <p><strong>Call or Text:</strong> <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></p>
        <p><strong>Email:</strong> <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
        <p><strong>Service Area:</strong> {SITE['city']}, {SITE['state']} &amp; the greater {SITE['region']} area</p>
        <div class="footer-social" style="margin-top:16px">
          <a href="{SITE['fb']}" target="_blank" rel="noopener" style="background:#eef1f5;color:#17356b" aria-label="Facebook">f</a>
          <a href="{SITE['ig']}" target="_blank" rel="noopener" style="background:#eef1f5;color:#17356b" aria-label="Instagram">IG</a>
          <a href="{SITE['google']}" target="_blank" rel="noopener" style="background:#eef1f5;color:#17356b" aria-label="Google">G</a>
        </div>
        {T("contact.side_html", "")}<div class="divider"></div>
        {map_section()}
      </div>
    </div>
  </div>
</section>
'''
    write("contact-us.html", page(f"Contact Us | {SITE['full_brand']}",
        f"Contact {SITE['full_brand']} for a free fence estimate in {SITE['city']}, FL. Call or text {SITE['phone']} or email {SITE['email']}.",
        "contact-us.html", content))


# ---------------------------------------------------------------- FAQ
def build_faq():
    content = page_hero("FAQ", T("faq.title", "Frequently Asked Questions"),
        T("faq.lead", COPY['faq_lead']),
        [("Home", "index.html"), ("FAQ", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div style="max-width:820px;margin:0 auto">
      {faq_accordion(site_faqs(), open_first=True)}
    </div>
  </div>
</section>
{cta_banner(T("faq.cta_title", "Still Have Questions?"), T("faq.cta_sub", "Give us a call and we'll walk you through it."))}
'''
    write("faq.html", page(f"FAQ | {SITE['full_brand']}",
        f"Answers to common questions about fence installation, pricing, permits, and materials from {SITE['full_brand']}.",
        "faq.html", content))


# ---------------------------------------------------------------- GALLERY
def build_gallery():
    cats = [  # (label, image kind, detail page)
        ("Vinyl Privacy", "vinyl", "vinyl-fence.html"), ("Wood Stockade", "wood", "wood-fence.html"),
        ("Aluminum", "aluminum", "aluminum-fence.html"), ("Chain Link", "chain-link", "chain-link-fence.html"),
        ("Composite", "composite", "composite-fence.html"), ("Commercial / Security", "security", "security-fencing.html"),
        ("Picket", "picket", "picket-fence.html"), ("Split Rail", "split-rail", "split-rail-fence.html"),
        ("Horizontal", "horizontal", "horizontal-fence.html"), ("Steel & Wrought Iron", "steel", "steel-wrought-iron-fence.html"),
    ]
    tiles = "".join(f'''
<a class="tile-img tile-link" href="{href}">{fence_illustration(kind)}
  <div class="tile-label">{T("gallery.label", "{cat} Fence — {city}, {state} area").format(cat=cat, city=SITE['city'], state=SITE['state'])} &rarr;</div>
</a>''' for cat, kind, href in T("gallery.tiles", cats))
    content = page_hero("Gallery", T("gallery.title", "Fence Gallery"),
        T("gallery.lead", f"A look at the fence materials and styles we install across {SITE['city']} and the {SITE['region']} area."),
        [("Home", "index.html"), ("Gallery", None)])
    content += f'''
<section class="section">
  <div class="container">
    {T("gallery.intro_html", "")}<div class="grid grid-4">{tiles}</div>
  </div>
</section>
{cta_banner()}
'''
    write("fence-gallery.html", page(f"Fence Gallery | {SITE['full_brand']}",
        T("gallery.meta", f"Browse vinyl, wood, aluminum, chain link, and composite fence styles installed by {SITE['full_brand']}."),
        "fence-gallery.html", content))


# ---------------------------------------------------------------- PRICING
def build_pricing():
    factors = T("pricing.factors", [
        ("Yard Size", "The single biggest driver of your total price — more linear footage means more material and labor."),
        ("Existing Fence Removal", "Removing and hauling away an old fence typically adds a few dollars per linear foot."),
        ("Gates", "Gates typically add a few hundred dollars each on top of your overall fence quote, depending on size and hardware."),
    ])
    factor_cards = "".join(f'\n      <div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in factors)
    content = page_hero("Pricing", T("pricing.title", "What Does a Fence Cost?"),
        T("pricing.lead", f"General pricing guidance for fence installation in {SITE['city']} and the {SITE['region']} area. Get a free quote for exact pricing."),
        [("Home", "index.html"), ("Pricing", None)])
    content += f'''
<section class="section">
  <div class="container">
    {T("pricing.intro_html", "")}{pricing_table()}
    <p class="small" style="margin-top:14px">Estimates only, based on typical residential installations. Actual pricing depends on linear footage, material, existing fence removal, gates, and site conditions. Composite and custom-colored vinyl typically run 50%-100% above standard vinyl pricing.</p>

    <div class="divider"></div>

    <div class="grid grid-3">{factor_cards}
    </div>
  </div>
</section>
{cta_banner(T("pricing.cta_title", "Want an Exact Price?"), T("pricing.cta_sub", "Every yard is different — get a free, no-obligation estimate for yours."))}
'''
    write("fence-pricing.html", page(f"Fence Pricing | {SITE['full_brand']}",
        T("pricing.meta", f"See typical fence installation pricing by material and yard size in {SITE['city']}, FL, or get a free custom quote."),
        "fence-pricing.html", content))


# ---------------------------------------------------------------- WARRANTY
def build_warranty():
    W = WARRANTY
    covered = "".join(f"<li>{x}</li>" for x in W["covered"])
    not_covered = "".join(f"<li>{x}</li>" for x in W["not_covered"])
    terms = "".join(f"<h3>{h}</h3><p>{t}</p>" for h, t in W["terms"])
    pillars = [
        ("✓", "Covers Our Workmanship", "Defects in our installation and assembly. If it's our workmanship, we'll make it right."),
        (f"{W['weeks']}", f"{W['weeks']} Weeks of Coverage", f"Coverage runs {W['weeks']} weeks ({W['approx']}) from the date your installation is completed."),
        ("$0", "No Charge to You", "If an issue is covered, we repair or correct it at no cost — parts and labor for the workmanship fix."),
    ]
    pillars_html = "".join(f'''
<div class="card">
  <div class="icon" style="font-weight:800;color:var(--navy);font-size:1.05rem">{i}</div>
  <h3>{t}</h3>
  <p>{d}</p>
</div>''' for i, t, d in pillars)
    warranty_faqs = [
        ("When does the 76 weeks start?",
         "Coverage starts on your installation completion date — the day our crew finishes the job, as recorded in our system. The clock starts then no matter when the final invoice is paid."),
        ("Does my project need to be paid in full?",
         "Yes. Warranty coverage applies once your project is paid in full. We don't perform warranty service on projects with an outstanding balance, and the 76 weeks aren't extended by a payment delay."),
        ("What's the difference between the workmanship warranty and the manufacturer warranty?",
         "Our workmanship warranty covers <em>how</em> we installed your fence: setting posts, assembling panels, hanging gates, and so on. The manufacturer's warranty covers the materials themselves — things like fading, rust, warping, or cracking. Between the two, both the install and the product are backed."),
        ("Is storm or hurricane damage covered?",
         f"No. Weather events like storms, hurricanes, high winds, and flooding aren't covered by the workmanship warranty — check your homeowner's insurance. We do offer <a href=\"fence-repair.html\">fence repair</a> if you need storm damage fixed."),
        ("Does the warranty cover fence repairs or DIY services?",
         f"The {W['short']} applies to fence installations performed by {W['issuer']}. Ask us about coverage for any other service when you get your estimate."),
        ("How do I file a warranty claim?",
         f"Call or text our Tampa line at <a href=\"tel:{SITE['tampa_phone_tel']}\">{SITE['tampa_phone']}</a> or our Lutz line at <a href=\"tel:{SITE['lutz_phone_tel']}\">{SITE['lutz_phone']}</a>, or email <a href=\"mailto:{SITE['email']}\">{SITE['email']}</a> with your installation address and a description or photos of the issue. We'll follow up to evaluate it."),
    ]
    content = f'''
<section class="page-hero">
  <div class="container warranty-hero">
    <div>
      <div class="breadcrumbs"><a href="index.html">Home</a> &rsaquo; <span>Our Warranty</span></div>
      <div class="eyebrow" style="color:#ff8a94">{W['tagline']}</div>
      <h1>{W['name']}</h1>
      <p class="lead">Every fence we install is backed by {W['issuer']} for {W['weeks']} weeks ({W['approx']}) against defects in our installation and assembly. If it's our workmanship, we'll make it right.</p>
      <div class="cta-row">
        <a class="btn btn-red" href="contact-us.html">Get a Free Estimate</a>
        <a class="btn btn-outline" href="#request-service">Request Warranty Service</a>
        <a class="btn btn-outline" href="assets/docs/76-fence-warranty.pdf" download>Download PDF</a>
      </div>
    </div>
    {warranty_seal("lg")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Built to Last. Backed by {W['issuer']}.</div>
      <h2>What Our Warranty Means for You</h2>
    </div>
    <div class="grid grid-3">{pillars_html}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <h3>What's Covered</h3>
        <p>Defects resulting directly from our workmanship or installation, such as:</p>
        <ul class="check-list">{covered}</ul>
      </div>
      <div class="card">
        <h3>What's Not Covered</h3>
        <p>Damage or changes resulting from:</p>
        <ul class="x-list">{not_covered}</ul>
      </div>
    </div>
    <p class="small center" style="margin-top:20px">Coverage applies to projects paid in full and runs from your recorded installation completion date. Material and product issues may be covered separately by the product manufacturer's warranty, where applicable.</p>
  </div>
</section>

<section class="section" id="request-service">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Warranty Service</div>
      <h2>How to Request Warranty Service</h2>
    </div>
    <div class="grid grid-3 steps">
      <div class="card"><h3>Contact Us</h3><p>Call or text Tampa at <a href="tel:{SITE['tampa_phone_tel']}">{SITE['tampa_phone']}</a> or Lutz at <a href="tel:{SITE['lutz_phone_tel']}">{SITE['lutz_phone']}</a>, or email <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p></div>
      <div class="card"><h3>Share the Details</h3><p>Send your installation address and a description or photos of the issue.</p></div>
      <div class="card"><h3>We Inspect &amp; Fix It</h3><p>We evaluate the condition, and if it's covered, we repair or correct the workmanship at no charge.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div style="max-width:800px;margin:0 auto">
      <div class="section-head"><h2>Warranty FAQs</h2></div>
      {faq_accordion(warranty_faqs)}
    </div>
  </div>
</section>

<section class="section">
  <div class="container terms" style="max-width:800px">
    <div class="eyebrow">Full Terms</div>
    <h2>{W['issuer']} &mdash; {W['name']}</h2>
    {terms}
    <p style="margin-top:24px"><a class="btn btn-navy-outline" href="assets/docs/76-fence-warranty.pdf" download>Download Warranty (PDF)</a></p>
  </div>
</section>

{cta_banner("Get a Fence That's Built to Last", f"Every installation comes with our {W['short']}. Get your free estimate today.")}
'''
    write("warranty.html", page(f"{W['name']} | {W['issuer']}",
        f"Every fence installed by {SITE['full_brand']} is backed by the {W['issuer']} {W['name']}. See what's covered, what's not, and how to request warranty service.",
        "warranty.html", content))


# ---------------------------------------------------------------- 404
def build_404():
    links = [
        ("Fence Materials", "fence-materials.html", "Vinyl, wood, aluminum, chain link, composite, and steel."),
        ("Fence Styles", "fence-styles.html", "Privacy, semi-privacy, horizontal, picket, and split rail."),
        ("Service Areas", "service-areas.html", f"Every community we serve around {SITE['city']}."),
        ("Our Warranty", "warranty.html", "Our 76-Week Limited Workmanship Warranty."),
        ("Pricing", "fence-pricing.html", "Typical fence costs by material and yard size."),
        ("Contact Us", "contact-us.html", "Request your free, no-obligation estimate."),
    ]
    cards = "".join(f'''
<div class="card">
  <h3>{t}</h3>
  <p>{d}</p>
  <a class="more" href="{href}">Go &rarr;</a>
</div>''' for t, href, d in links)
    content = f'''
<section class="page-hero">
  <div class="container">
    <div class="eyebrow" style="color:#ff8a94">Page Not Found</div>
    <h1>Sorry, we can't find that page.</h1>
    <p class="lead">The link may be old or mistyped. Try one of the pages below, or call us and we'll help you directly.</p>
    <div class="cta-row">
      <a class="btn btn-red" href="index.html">Go to the Homepage</a>
      <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">{cards}</div>
  </div>
</section>
{cta_banner()}
'''
    write_404(CURRENT['out_dir'], page(f"Page Not Found | {SITE['full_brand']}",
        f"The page you're looking for isn't here. Find fence services, service areas, and free estimates from {SITE['full_brand']}.",
        "404.html", content, noindex=True))


# ---------------------------------------------------------------- PRIVACY POLICY
def build_privacy():
    content = page_hero("Legal", "Privacy Policy", f"Last updated {SITE['year']}.",
        [("Home", "index.html"), ("Privacy Policy", None)])
    content += f'''
<section class="section">
  <div class="container" style="max-width:800px">
    <p>{SITE['name']} ({SITE['domain']}), operating as {SITE['full_brand']}, respects your privacy. This page explains what information we collect and how we use it.</p>
    <h3>Information We Collect</h3>
    <p>Like most websites, we automatically log basic technical details such as IP address, browser type, referring page, and time of visit. We also use cookies to remember preferences, and we collect information you volunteer to us directly, such as your name, phone number, and email address when you request an estimate.</p>
    <h3>How We Use Your Information</h3>
    <p>We use the information you provide to respond to estimate requests, schedule installations, and share relevant updates about our services. Email addresses are never sold, rented, or leased to third parties.</p>
    <h3>Your Choices</h3>
    <p>You can unsubscribe from marketing emails at any time using the link in those emails. Blocking cookies in your browser may limit some site functionality.</p>
    <h3>Third-Party Advertising</h3>
    <p>We may use third-party vendors, including Google, who use cookies to serve ads based on your prior visits to this and other websites. You can opt out of interest-based advertising through your browser or ad settings.</p>
    <h3>Contact Us</h3>
    <p>Questions about this policy? Email us at <a href="mailto:{SITE['email']}">{SITE['email']}</a> or call {SITE['phone']}.</p>
  </div>
</section>
'''
    write("privacy-policy.html", page(f"Privacy Policy | {SITE['full_brand']}",
        f"Privacy policy for {SITE['name']} / {SITE['full_brand']}.", "privacy-policy.html", content))
