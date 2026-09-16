# -*- coding: utf-8 -*-
from data import SITE, TOWNS, MATERIALS, STYLES, COMMERCIAL, OTHER_SERVICES

def esc(s):
    return s

def nav_html(active=""):
    def li(label, href, key, dropdown=None):
        cls = " class=\"open\"" if False else ""
        if dropdown:
            return f'''<li><button class="nav-toggle" type="button">{label} <span>▾</span></button>
              <div class="dropdown">{dropdown}</div></li>'''
        return f'<li><a href="{href}">{label}</a></li>'

    materials_links = "".join(f'<a href="{m["slug"]}.html">{m["name"]}</a>' for m in MATERIALS)
    styles_links = "".join(f'<a href="{s["slug"]}.html">{s["name"]}</a>' for s in STYLES)
    residential_dd = f'''
      <div class="dd-head">Fence Materials</div>
      {materials_links}
      <div class="dd-head">Fence Styles</div>
      {styles_links}
      <div class="dd-head">More</div>
      <a href="fence-gallery.html">Fence Gallery</a>
      <a href="fence-pricing.html">Pricing</a>
    '''
    commercial_dd = "".join(f'<a href="{c["slug"]}.html">{c["name"]}</a>' for c in COMMERCIAL)
    commercial_dd = f'<a href="commercial-fencing.html">Commercial Fencing (All)</a>' + commercial_dd
    other_dd = "".join(f'<a href="{o["slug"]}.html">{o["name"]}</a>' for o in OTHER_SERVICES)
    about_dd = '<a href="about-us.html">Meet the Team</a><a href="service-areas.html">Service Areas</a>'
    contact_dd = '<a href="contact-us.html">Contact Us</a><a href="faq.html">FAQs</a>'

    items = [
        li("Home", "index.html", "home"),
        li("Residential", "#", "residential", residential_dd),
        li("Commercial", "#", "commercial", commercial_dd),
        li("Other Services", "#", "other", other_dd),
        li("Fence Gallery", "fence-gallery.html", "gallery"),
        li("About", "#", "about", about_dd),
        li("Contact", "#", "contact", contact_dd),
    ]
    return "<ul>" + "".join(items) + "</ul>"


def header_html(active=""):
    return f'''
<div class="topbar">
  <div class="container">
    <div>Licensed, Bonded &amp; Insured in All 50 States &middot; Free Estimates &middot; Serving {SITE['city']}, {SITE['state']} &amp; the {SITE['region']} area</div>
    <div><a href="mailto:{SITE['email']}">{SITE['email']}</a> &nbsp;|&nbsp; <a class="topbar-phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
  </div>
</div>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="index.html">
      <img src="assets/images/logo.png" alt="{SITE['full_brand']} logo" width="54" height="54">
      <span>{SITE['brand']}<small>{SITE['city']}, {SITE['state']}</small></span>
    </a>
    <nav class="primary-nav">
      {nav_html(active)}
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{SITE['phone_tel']}"><span>Call or Text</span>{SITE['phone']}</a>
      <a class="btn btn-red" href="contact-us.html">Get Free Quote</a>
      <button class="menu-toggle" aria-label="Menu">&#9776;</button>
    </div>
  </div>
</header>
<div class="nav-scrim"></div>
<div class="mobile-call-bar"><a href="tel:{SITE['phone_tel']}" style="color:inherit">Call Now: {SITE['phone']}</a></div>
'''


def footer_html():
    popular_towns = TOWNS[:10]
    town_links = "".join(f'<li><a href="fence-company-{slug}-fl.html">{name}, FL</a></li>' for name, slug in popular_towns)
    material_links = "".join(f'<li><a href="{m["slug"]}.html">{m["name"]}</a></li>' for m in MATERIALS[:6])
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="assets/images/logo.png" alt="{SITE['full_brand']} logo" width="46" height="46">
          <span>{SITE['full_brand']}</span>
        </div>
        <p>{SITE['name']} ({SITE['domain']}) is a marketing website for {SITE['brand']}&trade;, serving {SITE['city']}, {SITE['state']} and the surrounding {SITE['region']} area with residential and commercial fence installation, repair, and maintenance.</p>
        <div class="footer-social">
          <a href="{SITE['fb']}" target="_blank" rel="noopener" aria-label="Facebook">f</a>
          <a href="{SITE['ig']}" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
          <a href="{SITE['google']}" target="_blank" rel="noopener" aria-label="Google Reviews">G</a>
        </div>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about-us.html">Meet the Team</a></li>
          <li><a href="service-areas.html">Service Areas</a></li>
          <li><a href="fence-gallery.html">Fence Gallery</a></li>
          <li><a href="fence-pricing.html">Pricing</a></li>
          <li><a href="faq.html">FAQs</a></li>
          <li><a href="contact-us.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Popular Services</h4>
        <ul>
          {material_links}
          <li><a href="commercial-fencing.html">Commercial Fencing</a></li>
          <li><a href="fence-repair.html">Fence Repair</a></li>
        </ul>
      </div>
      <div>
        <h4>Popular Service Areas</h4>
        <ul>
          {town_links}
          <li><a href="service-areas.html"><strong>See All Cities &rarr;</strong></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; {SITE['year']} {SITE['brand']}&trade;. All rights reserved. {SITE['name']} is a registered DBA in the State of {SITE['state_full']}.</div>
      <div><a href="privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a> &nbsp;|&nbsp; <a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
'''


def page(title, description, path, content, canonical=None):
    canonical = canonical or f"https://{SITE['domain']}/{path}"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="assets/images/favicon.png">
<link rel="apple-touch-icon" href="assets/images/logo.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="assets/images/logo.png">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
{header_html()}
{content}
{footer_html()}
</body>
</html>'''


def breadcrumb(items):
    parts = []
    for label, href in items:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return '<div class="breadcrumbs">' + " &rsaquo; ".join(parts) + '</div>'


def page_hero(eyebrow, title, lead, breadcrumbs_items=None):
    bc = breadcrumb(breadcrumbs_items) if breadcrumbs_items else ""
    return f'''
<section class="page-hero">
  <div class="container">
    {bc}
    <div class="eyebrow" style="color:#ff8a94">{eyebrow}</div>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    <div class="cta-row">
      <a class="btn btn-red" href="contact-us.html">Get a Free Estimate</a>
      <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
    </div>
  </div>
</section>
'''


def faq_accordion(items, open_first=False):
    out = ['<div class="faq-list">']
    for i, (q, a) in enumerate(items):
        cls = "faq-item open" if (open_first and i == 0) else "faq-item"
        out.append(f'''<div class="{cls}">
  <button class="faq-q" type="button">{q}<span class="plus">+</span></button>
  <div class="faq-a"><p>{a}</p></div>
</div>''')
    out.append('</div>')
    return "\n".join(out)


def _formspree_id():
    return SITE['formspree'].rstrip('/').split('/')[-1]


FORMSPREE_AJAX_SCRIPT = '<script src="https://unpkg.com/@formspree/ajax@1" defer></script>'


def mini_quote_form(heading="Get Your Free Estimate"):
    fid = _formspree_id()
    return f'''
<div class="hero-panel">
  <h3>{heading}</h3>
  <p>Tell us a little about your project — we'll call or text you back fast.</p>
  <div class="fs-success" data-fs-success>Thanks! Your request is in — we'll call or text you back shortly.</div>
  <form id="hero-quote-form">
    <input type="text" name="first_name" placeholder="First Name" data-fs-field required>
    <span class="fs-field-error" data-fs-error="first_name"></span>
    <input type="text" name="last_name" placeholder="Last Name" data-fs-field required>
    <span class="fs-field-error" data-fs-error="last_name"></span>
    <input type="tel" name="phone" placeholder="Phone Number" data-fs-field required>
    <span class="fs-field-error" data-fs-error="phone"></span>
    <input type="email" name="email" placeholder="Email Address" data-fs-field required>
    <span class="fs-field-error" data-fs-error="email"></span>
    <input type="hidden" name="_subject" value="New quote request from {SITE['domain']}">
    <div class="fs-error" data-fs-error></div>
    <button class="btn btn-red btn-block" type="submit" data-fs-submit-btn>Request My Free Estimate</button>
  </form>
  <p class="consent" style="margin-top:10px">By submitting, you consent to be contacted by {SITE['full_brand']} by phone, text, or email about your request.</p>
</div>
{FORMSPREE_AJAX_SCRIPT}
<script>
  window.formspree = window.formspree || function () {{ (formspree.q = formspree.q || []).push(arguments); }};
  formspree('initForm', {{ formElement: '#hero-quote-form', formId: '{fid}' }});
</script>
'''


def contact_form_card():
    fid = _formspree_id()
    return f'''
<div class="form-card">
  <h3>Request Your Free Estimate</h3>
  <p>Fill out the form and our team will reach out to schedule your free, no-obligation estimate.</p>
  <div class="fs-success" data-fs-success>Thanks! Your request is in — we'll be in touch shortly to schedule your free estimate.</div>
  <form id="contact-quote-form">
    <div class="form-row">
      <div><label for="first_name">First Name</label><input id="first_name" type="text" name="first_name" data-fs-field required>
        <span class="fs-field-error" data-fs-error="first_name"></span></div>
      <div><label for="last_name">Last Name</label><input id="last_name" type="text" name="last_name" data-fs-field required>
        <span class="fs-field-error" data-fs-error="last_name"></span></div>
    </div>
    <div class="form-row">
      <div><label for="phone">Phone</label><input id="phone" type="tel" name="phone" data-fs-field required>
        <span class="fs-field-error" data-fs-error="phone"></span></div>
      <div><label for="email">Email</label><input id="email" type="email" name="email" data-fs-field required>
        <span class="fs-field-error" data-fs-error="email"></span></div>
    </div>
    <div class="form-row full">
      <div><label for="address">Property Address / City</label><input id="address" type="text" name="address" placeholder="e.g. Lutz, FL" data-fs-field></div>
    </div>
    <div class="form-row full">
      <div><label for="project">Tell us about your project</label>
        <textarea id="project" name="project" rows="4" placeholder="Fence type, approximate length, timeline..." data-fs-field></textarea>
      </div>
    </div>
    <input type="hidden" name="_subject" value="New quote request from {SITE['domain']}">
    <div class="fs-error" data-fs-error></div>
    <button class="btn btn-red btn-block" type="submit" data-fs-submit-btn>Send My Request</button>
    <p class="consent" style="margin-top:12px">By submitting, you consent to be contacted by {SITE['full_brand']} by phone, text, or email about your request. We don't sell or share your information.</p>
  </form>
</div>
{FORMSPREE_AJAX_SCRIPT}
<script>
  window.formspree = window.formspree || function () {{ (formspree.q = formspree.q || []).push(arguments); }};
  formspree('initForm', {{ formElement: '#contact-quote-form', formId: '{fid}' }});
</script>
'''


def map_section():
    return f'''
<div class="map-embed">
  <iframe src="{SITE['map_embed']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Service area map"></iframe>
</div>
'''


def town_chips(exclude_slug=None, limit=None):
    towns = [(n, s) for n, s in TOWNS if s != exclude_slug]
    if limit:
        towns = towns[:limit]
    return '<div class="chip-grid">' + "".join(
        f'<a class="chip" href="fence-company-{s}-fl.html">{n}, FL</a>' for n, s in towns
    ) + '</div>'


def _svg_wrap(inner, sky="#e7edf6", ground="#d7e6d4"):
    return f'''<svg viewBox="0 0 480 240" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" style="width:100%;height:100%;display:block;">
  <rect x="0" y="0" width="480" height="240" fill="{sky}"/>
  <rect x="0" y="185" width="480" height="55" fill="{ground}"/>
  {inner}
</svg>'''


def _posts(xs, top=95, bottom=205, w=8, color="#5a6470"):
    return "".join(f'<rect x="{x-w/2:.1f}" y="{top}" width="{w}" height="{bottom-top}" fill="{color}"/>' for x in xs)


def svg_vinyl():
    posts_x = [30, 165, 300, 435]
    boards = "".join(
        f'<rect x="{x:.1f}" y="105" width="12" height="90" rx="2" fill="{"#f6f3ea" if i % 2 == 0 else "#efece0"}" stroke="#d8d3c2" stroke-width="1"/>'
        for i, x in enumerate([20 + n * 15.2 for n in range(30)])
    )
    caps = "".join(f'<rect x="{x-9}" y="88" width="18" height="10" rx="2" fill="#e7e2d2"/>' for x in posts_x)
    rails = '<rect x="10" y="118" width="460" height="8" fill="#e2ddcb"/><rect x="10" y="178" width="460" height="8" fill="#e2ddcb"/>'
    return _svg_wrap(boards + rails + _posts(posts_x, top=90, color="#c9c2ab") + caps)


def svg_wood():
    boards = "".join(
        f'<rect x="{x:.1f}" y="{100+(4 if i%3==0 else 0)}" width="13" height="{100-(4 if i%3==0 else 0)}" fill="{["#b9895a","#a97845","#c39569"][i%3]}" stroke="#8f6236" stroke-width="1"/>'
        for i, x in enumerate([18 + n * 15 for n in range(31)])
    )
    posts_x = [30, 165, 300, 435]
    return _svg_wrap(boards + _posts(posts_x, top=92, bottom=205, w=12, color="#7c5330"))


def svg_composite():
    boards = "".join(
        f'<rect x="{x:.1f}" y="100" width="13" height="100" fill="{"#8a7361" if i % 2 == 0 else "#93806e"}" stroke="#6f5c4c" stroke-width="1"/>'
        for i, x in enumerate([18 + n * 15 for n in range(31)])
    )
    posts_x = [30, 165, 300, 435]
    rail = '<rect x="10" y="96" width="460" height="7" fill="#6f5c4c"/>'
    return _svg_wrap(boards + rail + _posts(posts_x, top=92, bottom=205, w=12, color="#5f4d3f"))


def svg_aluminum():
    xs = [24 + n * 11.5 for n in range(40)]
    pickets = "".join(f'<rect x="{x-2.5:.1f}" y="100" width="5" height="100" fill="#262b31"/>' for x in xs)
    finials = "".join(f'<circle cx="{x:.1f}" cy="97" r="4" fill="#262b31"/>' for x in xs)
    rails = '<rect x="10" y="112" width="460" height="6" fill="#1d2126"/><rect x="10" y="178" width="460" height="6" fill="#1d2126"/>'
    posts_x = [30, 165, 300, 435]
    return _svg_wrap(pickets + rails + finials + _posts(posts_x, top=88, bottom=205, w=9, color="#181c20"))


def svg_steel():
    xs = [24 + n * 13.5 for n in range(34)]
    pickets = "".join(f'<rect x="{x-2.2:.1f}" y="98" width="4.4" height="102" fill="#1a1d21"/>' for x in xs)
    finials = "".join(
        f'<path d="M {x-5:.1f} 98 L {x:.1f} 84 L {x+5:.1f} 98 Z" fill="#1a1d21"/><circle cx="{x:.1f}" cy="82" r="2.6" fill="#c9a227"/>'
        for x in xs
    )
    scroll = "".join(f'<circle cx="{x:.1f}" cy="150" r="6" fill="none" stroke="#1a1d21" stroke-width="3"/>' for x in xs[::3])
    rails = '<rect x="10" y="110" width="460" height="6" fill="#101215"/><rect x="10" y="188" width="460" height="6" fill="#101215"/>'
    posts_x = [30, 165, 300, 435]
    return _svg_wrap(pickets + rails + scroll + finials + _posts(posts_x, top=78, bottom=210, w=9, color="#101215"))


def svg_chain_link(security=False):
    lines = []
    step = 16
    for i in range(-2, 32):
        x0 = i * step
        lines.append(f'<path d="M {x0} 205 L {x0+step*4} 100" stroke="#9aa4ad" stroke-width="2" fill="none"/>')
        lines.append(f'<path d="M {x0} 100 L {x0+step*4} 205" stroke="#9aa4ad" stroke-width="2" fill="none"/>')
    mesh = f'<clipPath id="meshclip"><rect x="10" y="100" width="460" height="105"/></clipPath><g clip-path="url(#meshclip)">{"".join(lines)}</g>'
    posts_x = [30, 165, 300, 435]
    top_y = 92 if security else 100
    rail = f'<rect x="10" y="{top_y-4}" width="460" height="6" fill="#7c858d"/><rect x="10" y="201" width="460" height="6" fill="#7c858d"/>'
    barbs = ""
    if security:
        barbs = "".join(
            f'<path d="M {x} 92 L {x+22} 80 M {x+6} 88 L {x+2} 94 M {x+12} 84 L {x+8} 90 M {x+18} 81 L {x+14} 87" stroke="#7c858d" stroke-width="2" fill="none"/>'
            for x in [20, 130, 240, 350]
        )
    return _svg_wrap(mesh + rail + barbs + _posts(posts_x, top=(80 if security else 90), bottom=205, w=8, color="#5a6470"))


def svg_picket():
    xs = [20 + n * 13.2 for n in range(34)]
    pickets = "".join(
        f'<path d="M {x-5:.1f} 205 L {x-5:.1f} 128 L {x:.1f} 115 L {x+5:.1f} 128 L {x+5:.1f} 205 Z" fill="{"#fbfaf5" if i%2==0 else "#f2f0e6"}" stroke="#d8d3c2" stroke-width="1"/>'
        for i, x in enumerate(xs)
    )
    rails = '<rect x="10" y="150" width="460" height="7" fill="#e2ddcb"/><rect x="10" y="185" width="460" height="7" fill="#e2ddcb"/>'
    posts_x = [30, 165, 300, 435]
    return _svg_wrap(pickets + rails + _posts(posts_x, top=100, bottom=205, w=10, color="#c9c2ab"))


def svg_split_rail():
    posts_x = [30, 130, 230, 330, 430]
    posts = _posts(posts_x, top=110, bottom=205, w=13, color="#8a6a42")
    rails = ""
    for i in range(len(posts_x) - 1):
        x1, x2 = posts_x[i], posts_x[i + 1]
        rails += f'<rect x="{x1}" y="128" width="{x2-x1}" height="11" rx="4" fill="#a9814f"/>'
        rails += f'<rect x="{x1}" y="168" width="{x2-x1}" height="11" rx="4" fill="#a9814f"/>'
    return _svg_wrap(rails + posts)


_SVG_KINDS = {
    "vinyl": svg_vinyl,
    "wood": svg_wood,
    "composite": svg_composite,
    "aluminum": svg_aluminum,
    "steel": svg_steel,
    "chain-link": svg_chain_link,
    "security": lambda: svg_chain_link(security=True),
    "picket": svg_picket,
    "split-rail": svg_split_rail,
}


def fence_illustration(kind):
    fn = _SVG_KINDS.get(kind, svg_vinyl)
    return fn()


def cta_banner(title="Ready to Get Started?", sub="Get a free, no-obligation fence estimate today."):
    return f'''
<section class="section section-navy">
  <div class="container center">
    <h2>{title}</h2>
    <p style="max-width:560px;margin:0 auto 24px">{sub}</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-red" href="contact-us.html">Get a Free Estimate</a>
      <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
    </div>
  </div>
</section>
'''
