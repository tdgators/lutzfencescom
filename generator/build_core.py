# -*- coding: utf-8 -*-
"""Builds: homepage, about, service-areas, contact, faq, gallery, pricing, privacy-policy"""
from pathlib import Path
from data import SITE, TOWNS, MATERIALS, STYLES, COMMERCIAL, OTHER_SERVICES, FAQS, PRICING_TABLE
from templates import page, page_hero, faq_accordion, mini_quote_form, contact_form_card, map_section, town_chips, cta_banner, fence_illustration

OUT = Path("/mnt/user-data/outputs/lutz-fences-site")

def write(path, html):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")


# ---------------------------------------------------------------- HOMEPAGE
def build_home():
    service_tiles = "".join(f'''
<div class="card">
  <div class="tile-img" style="aspect-ratio:16/10;margin-bottom:14px">{fence_illustration(m['img'])}</div>
  <h3>{m['name']}</h3>
  <p>{m['tagline']}</p>
  <a class="more" href="{m['slug']}.html">Learn More &rarr;</a>
</div>''' for m in MATERIALS)

    gallery_tiles = "".join(f'''
<div class="tile-img">{fence_illustration(kind)}
  <div class="tile-label">{label}</div>
</div>''' for label, kind in [
        ("Vinyl Privacy Fence", "vinyl"), ("Aluminum Pool Enclosure", "aluminum"),
        ("Wood Privacy Fence", "wood"), ("Chain Link Install", "chain-link"),
        ("Composite Fence", "composite"), ("Commercial Security Fence", "security"),
        ("Picket Fence", "picket"), ("HOA Community Fencing", "steel"),
    ])

    why_items = [
        ("Licensed, Bonded &amp; Insured", "76 FENCE is licensed, bonded, and insured in all 50 states, on every job we do."),
        ("Free Estimates", "Every estimate is free, with no obligation and no pressure."),
        ("Manufacturer Warranty", "Every material we install is backed by the manufacturer's warranty, plus our own workmanship guarantee."),
        ("Family Owned &amp; Locally Operated", "76 FENCE Lutz is owned and run by Tom &amp; Kate Donnelly, right here in the Tampa Bay area."),
        ("We Handle Your Permit", "In most cases we manage the local permitting process for you, included in your price."),
        ("Flexible Financing", "Ask about flexible financing options to make your project fit your budget."),
    ]
    why_html = "".join(f'''
<div class="card">
  <div class="icon">✓</div>
  <h3>{t}</h3>
  <p>{d}</p>
</div>''' for t, d in why_items)

    commercial_tiles = "".join(f'''
<div class="card">
  <h3>{c['name']}</h3>
  <p>{c['desc']}</p>
  <a class="more" href="{c['slug']}.html">Learn More &rarr;</a>
</div>''' for c in COMMERCIAL)

    pricing_rows = ""
    for size, mats in PRICING_TABLE.items():
        pass
    first_size = list(PRICING_TABLE.keys())[0]
    header_cols = "".join(f"<th>{m}</th>" for m in PRICING_TABLE[first_size].keys())
    rows = ""
    for size, mats in PRICING_TABLE.items():
        cells = "".join(f"<td>{v}</td>" for v in mats.values())
        rows += f"<tr><td>{size}</td>{cells}</tr>"

    diy_tiles = "".join(f'''
<div class="card">
  <h3>{t}</h3><p>{d}</p>
</div>''' for t, d in [
        ("Materials Only", "Buy fence materials at contractor pricing and install it yourself."),
        ("Post Hole Digging", "We dig the holes; you handle the rest of the build."),
        ("Installation Consultation", "A paid on-site visit to plan layout, materials, and permitting before you start."),
    ])

    content = f'''
<section class="hero">
  <div class="container">
    <div>
      <div class="eyebrow" style="color:#ff8a94">{SITE['full_brand']}</div>
      <h1>The Trusted Fence Company in {SITE['city']}, {SITE['state']}</h1>
      <p class="lead">Residential &amp; commercial fence installation built on quality, trust, and proven results. Vinyl, wood, aluminum, chain link, composite &amp; steel — installed, repaired, and maintained by a locally owned {SITE['region']} team.</p>
      <div class="cta-row">
        <a class="btn btn-red" href="contact-us.html">Get a Free Estimate</a>
        <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
      </div>
      <div class="hero-badges">
        <div class="hero-badge"><span class="dot"></span>Licensed, Bonded &amp; Insured (All 50 States)</div>
        <div class="hero-badge"><span class="dot"></span>Free Estimates</div>
        <div class="hero-badge"><span class="dot"></span>Family Owned &amp; Locally Operated</div>
      </div>
    </div>
    {mini_quote_form()}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">What We Install</div>
      <h2>Fencing Services in {SITE['city']} &amp; the {SITE['region']} Area</h2>
      <p>From a simple backyard privacy fence to a full commercial security perimeter, we install and stand behind every material we offer.</p>
    </div>
    <div class="grid grid-3">{service_tiles}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Our Work</div>
      <h2>Recent {SITE['city']}-Area Fence Installations</h2>
      <p>We're building out our full photo gallery of local installs — in the meantime, here's a look at the styles and materials we install most.</p>
    </div>
    <div class="grid grid-4">{gallery_tiles}</div>
    <div class="center" style="margin-top:28px"><a class="btn btn-navy-outline" href="fence-gallery.html">View Full Gallery</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Why 76 FENCE</div>
      <h2>Why Homeowners Choose {SITE['full_brand']}</h2>
      <p>We're part of the {SITE['brand']} network — bringing national buying power and manufacturer relationships to a locally owned, locally operated business.</p>
    </div>
    <div class="grid grid-3">{why_html}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Pricing</div>
        <h2>What Does a Fence Cost?</h2>
        <p>Every project is different, but here's a general idea of what {SITE['city']}-area homeowners typically invest based on yard size and material. Get a free, no-obligation quote for exact pricing on your property.</p>
        <a class="btn btn-blue" href="fence-pricing.html">See Full Pricing Breakdown</a>
      </div>
      <div>
        <table class="pricing">
          <tr><th>Yard Size</th>{header_cols}</tr>
          {rows}
        </table>
        <p class="small" style="margin-top:10px">Estimates only. Actual pricing depends on linear footage, material, gates, and site conditions.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Commercial</div>
      <h2>Commercial &amp; Industrial Fencing</h2>
      <p>We handle commercial fencing projects of every size — from a single dumpster enclosure to a full industrial security perimeter.</p>
    </div>
    <div class="grid grid-4">{commercial_tiles}</div>
    <div class="center" style="margin-top:28px"><a class="btn btn-navy-outline" href="commercial-fencing.html">See All Commercial Services</a></div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">DIY</div>
      <h2>Building Your Own Fence?</h2>
      <p>Not every project needs a full install — here's how we can help without taking over the whole job.</p>
    </div>
    <div class="grid grid-3">{diy_tiles}</div>
    <div class="center" style="margin-top:24px"><a class="btn btn-blue" href="diy-fence.html">Ask About DIY</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Reviews</div>
      <h2>See What {SITE['city']}-Area Customers Are Saying</h2>
      <p>Read our latest reviews on Google and Facebook, or leave us one of your own after your project.</p>
    </div>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-navy-outline" href="{SITE['google']}" target="_blank" rel="noopener">Read Our Google Reviews</a>
      <a class="btn btn-navy-outline" href="{SITE['fb']}" target="_blank" rel="noopener">Read Our Facebook Reviews</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="split rev">
      <div class="split-media">{map_section()}</div>
      <div>
        <div class="eyebrow">Service Area</div>
        <h2>Proudly Serving {SITE['city']} &amp; the {SITE['region']} Area</h2>
        <p>We install and repair fences throughout {SITE['city']} and dozens of surrounding communities.</p>
        {town_chips(limit=14)}
        <div style="margin-top:20px"><a class="btn btn-blue" href="service-areas.html">See All Cities We Serve</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">FAQ</div>
      <h2>Frequently Asked Questions</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
      {faq_accordion(FAQS[:6], open_first=True)}
      <div class="center" style="margin-top:24px"><a class="btn btn-navy-outline" href="faq.html">See All FAQs</a></div>
    </div>
  </div>
</section>

{cta_banner()}
'''
    write("index.html", page(
        f"{SITE['full_brand']} | Fence Company in {SITE['city']}, {SITE['state']}",
        f"76 FENCE Lutz installs and repairs vinyl, wood, aluminum, chain link, composite, and steel fencing for homes and businesses in {SITE['city']}, FL and the greater Tampa Bay area. Free estimates — call {SITE['phone']}.",
        "index.html", content))


# ---------------------------------------------------------------- ABOUT
def build_about():
    content = page_hero("About Us", f"Meet the {SITE['full_brand']} Team",
        f"{SITE['full_brand']} is a locally owned and operated fence company, proudly part of the national {SITE['brand']} network.",
        [("Home", "index.html"), ("About", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <div class="eyebrow">Our Story</div>
        <h2>Local Ownership. National Backing.</h2>
        <p>{SITE['full_brand']} brings the training, purchasing power, and manufacturer relationships of the national {SITE['brand']} network to a business that's owned and run right here in the Tampa Bay area. The {SITE['brand']} name is a nod to 1776 — American craftsmanship, straightforward dealing, and standing behind the work.</p>
        <p>We install and repair fencing for homeowners, HOAs, and businesses across {SITE['city']} and the surrounding communities, and we handle the permitting process, the installation, and anything that needs fixing down the road.</p>
      </div>
      <div class="tile-img">{fence_illustration('wood')}</div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div class="eyebrow">Ownership</div>
      <h2>Meet the Owners</h2>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <div class="tile-img" style="aspect-ratio:1/1;margin-bottom:16px">{fence_illustration('steel')}</div>
        <h3>Tom Donnelly &mdash; Owner</h3>
        <p>Tom brings over 20 years of experience in information technology within the finance and banking industries, having served as both a principal engineer and a people leader managing global teams. As owner of {SITE['full_brand']}, Tom is focused on building a trusted, locally operated business that delivers exceptional craftsmanship and customer service, bringing the strength and professionalism of the {SITE['brand']} brand to the {SITE['city']} community.</p>
      </div>
      <div class="card">
        <div class="tile-img" style="aspect-ratio:1/1;margin-bottom:16px">{fence_illustration('aluminum')}</div>
        <h3>Kate Donnelly &mdash; Owner</h3>
        <p>Kate brings over 20 years of experience serving the federal government as an intelligence analyst, with a master's degree and deep experience in strategic analysis and attention to detail. As owner of {SITE['full_brand']}, Kate is committed to building a business grounded in integrity, operational excellence, and outstanding customer service for every {SITE['city']}-area project.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-4 center">
      <div class="badge">Licensed &amp; Bonded — All 50 States</div>
      <div class="badge">Fully Insured</div>
      <div class="badge">Manufacturer Warranty</div>
      <div class="badge">Family Owned &amp; Operated</div>
    </div>
  </div>
</section>

{cta_banner("Ready to Work With Us?", f"Get a free estimate from the {SITE['full_brand']} team today.")}
'''
    write("about-us.html", page(f"Meet the Team | {SITE['full_brand']}",
        f"Meet Tom and Kate Donnelly, the owners of 76 FENCE Lutz, a locally owned fence company serving {SITE['city']}, FL and the Tampa Bay area.",
        "about-us.html", content))


# ---------------------------------------------------------------- SERVICE AREAS
def build_service_areas():
    content = page_hero("Service Areas", f"Cities We Serve Near {SITE['city']}, {SITE['state']}",
        f"{SITE['full_brand']} provides fence installation, repair, and maintenance across {SITE['city']} and the entire {SITE['region']} region.",
        [("Home", "index.html"), ("Service Areas", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div>
        <h2>Proudly Serving the Following Communities</h2>
        <p>Don't see your city listed? Give us a call — we likely still serve your area.</p>
        {town_chips()}
      </div>
      <div>{map_section()}</div>
    </div>
  </div>
</section>
{cta_banner()}
'''
    write("service-areas.html", page(f"Service Areas | {SITE['full_brand']}",
        f"See every city and community {SITE['full_brand']} serves near {SITE['city']}, FL, including Land O' Lakes, Wesley Chapel, Odessa, New Port Richey, and more.",
        "service-areas.html", content))


# ---------------------------------------------------------------- CONTACT
def build_contact():
    content = page_hero("Contact Us", "Get Your Free Fence Estimate",
        f"Call, text, or send us a message and the {SITE['full_brand']} team will get back to you fast.",
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
        <div class="divider"></div>
        {map_section()}
      </div>
    </div>
  </div>
</section>
'''
    write("contact-us.html", page(f"Contact Us | {SITE['full_brand']}",
        f"Contact 76 FENCE Lutz for a free fence estimate in {SITE['city']}, FL. Call or text {SITE['phone']} or email {SITE['email']}.",
        "contact-us.html", content))


# ---------------------------------------------------------------- FAQ
def build_faq():
    content = page_hero("FAQ", "Frequently Asked Questions",
        "Answers to the questions we hear most from Lutz-area homeowners and businesses.",
        [("Home", "index.html"), ("FAQ", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div style="max-width:820px;margin:0 auto">
      {faq_accordion(FAQS, open_first=True)}
    </div>
  </div>
</section>
{cta_banner("Still Have Questions?", "Give us a call and we'll walk you through it.")}
'''
    write("faq.html", page(f"FAQ | {SITE['full_brand']}",
        f"Answers to common questions about fence installation, pricing, permits, and materials from 76 FENCE Lutz.",
        "faq.html", content))


# ---------------------------------------------------------------- GALLERY
def build_gallery():
    cats = [("Vinyl", "vinyl"), ("Wood", "wood"), ("Aluminum", "aluminum"),
            ("Chain Link", "chain-link"), ("Composite", "composite"), ("Commercial", "security")]
    tiles = "".join(f'''
<div class="tile-img">{fence_illustration(kind)}
  <div class="tile-label">{cat} Fence — {SITE['city']}, {SITE['state']} area</div>
</div>''' for cat, kind in cats * 3)
    content = page_hero("Gallery", "Fence Gallery",
        f"A look at the fence styles and materials we install across {SITE['city']} and the {SITE['region']} area. Real project photos coming soon.",
        [("Home", "index.html"), ("Gallery", None)])
    content += f'''
<section class="section">
  <div class="container">
    <div class="grid grid-4">{tiles}</div>
  </div>
</section>
{cta_banner()}
'''
    write("fence-gallery.html", page(f"Fence Gallery | {SITE['full_brand']}",
        f"Browse vinyl, wood, aluminum, chain link, and composite fence styles installed by 76 FENCE Lutz.",
        "fence-gallery.html", content))


# ---------------------------------------------------------------- PRICING
def build_pricing():
    first_size = list(PRICING_TABLE.keys())[0]
    header_cols = "".join(f"<th>{m}</th>" for m in PRICING_TABLE[first_size].keys())
    rows = ""
    for size, mats in PRICING_TABLE.items():
        cells = "".join(f"<td>{v}</td>" for v in mats.values())
        rows += f"<tr><td>{size}</td>{cells}</tr>"

    content = page_hero("Pricing", "What Does a Fence Cost?",
        f"General pricing guidance for fence installation in {SITE['city']} and the {SITE['region']} area. Get a free quote for exact pricing.",
        [("Home", "index.html"), ("Pricing", None)])
    content += f'''
<section class="section">
  <div class="container">
    <table class="pricing">
      <tr><th>Yard Size</th>{header_cols}</tr>
      {rows}
    </table>
    <p class="small" style="margin-top:14px">Estimates only, based on typical residential installations. Actual pricing depends on linear footage, material, existing fence removal, gates, and site conditions. Composite and custom-colored vinyl typically run 50%-100% above standard vinyl pricing.</p>

    <div class="divider"></div>

    <div class="grid grid-3">
      <div class="card"><h3>Yard Size</h3><p>The single biggest driver of your total price — more linear footage means more material and labor.</p></div>
      <div class="card"><h3>Existing Fence Removal</h3><p>Removing and hauling away an old fence typically adds a few dollars per linear foot.</p></div>
      <div class="card"><h3>Gates</h3><p>Gates typically add a few hundred dollars each on top of your overall fence quote, depending on size and hardware.</p></div>
    </div>
  </div>
</section>
{cta_banner("Want an Exact Price?", "Every yard is different — get a free, no-obligation estimate for yours.")}
'''
    write("fence-pricing.html", page(f"Fence Pricing | {SITE['full_brand']}",
        f"See typical fence installation pricing by material and yard size in {SITE['city']}, FL, or get a free custom quote.",
        "fence-pricing.html", content))


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
        "Privacy policy for Lutz Fences / 76 FENCE Lutz.", "privacy-policy.html", content))


if __name__ == "__main__":
    build_home()
    build_about()
    build_service_areas()
    build_contact()
    build_faq()
    build_gallery()
    build_pricing()
    build_privacy()
    print("core pages done")
