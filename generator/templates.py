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

    materials_links = "".join(f'<a href="/{m["slug"]}.html">{m["name"]}</a>' for m in MATERIALS)
    styles_links = "".join(f'<a href="/{s["slug"]}.html">{s["name"]}</a>' for s in STYLES)
    residential_dd = f'''
      <div class="dd-head">Fence Materials</div>
      {materials_links}
      <div class="dd-head">Fence Styles</div>
      {styles_links}
      <div class="dd-head">More</div>
      <a href="/fence-gallery.html">Fence Gallery</a>
      <a href="/fence-pricing.html">Pricing</a>
    '''
    commercial_dd = "".join(f'<a href="/{c["slug"]}.html">{c["name"]}</a>' for c in COMMERCIAL)
    commercial_dd = f'<a href="/commercial-fencing.html">Commercial Fencing (All)</a>' + commercial_dd
    other_dd = "".join(f'<a href="/{o["slug"]}.html">{o["name"]}</a>' for o in OTHER_SERVICES)
    about_dd = '<a href="/about-us.html">Meet the Team</a><a href="/service-areas.html">Service Areas</a>'
    contact_dd = '<a href="/contact-us.html">Contact Us</a><a href="/faq.html">FAQs</a>'

    items = [
        li("Home", "/index.html", "home"),
        li("Residential", "#", "residential", residential_dd),
        li("Commercial", "#", "commercial", commercial_dd),
        li("Other Services", "#", "other", other_dd),
        li("Fence Gallery", "/fence-gallery.html", "gallery"),
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
    <a class="brand" href="/index.html">
      <img src="/assets/images/logo.png" alt="{SITE['full_brand']} logo" width="54" height="54">
      <span>{SITE['brand']}<small>{SITE['city']}, {SITE['state']}</small></span>
    </a>
    <nav class="primary-nav">
      {nav_html(active)}
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{SITE['phone_tel']}"><span>Call or Text</span>{SITE['phone']}</a>
      <a class="btn btn-red" href="/contact-us.html">Get Free Quote</a>
      <button class="menu-toggle" aria-label="Menu">&#9776;</button>
    </div>
  </div>
</header>
<div class="nav-scrim"></div>
<div class="mobile-call-bar"><a href="tel:{SITE['phone_tel']}" style="color:inherit">Call Now: {SITE['phone']}</a></div>
'''


def footer_html():
    popular_towns = TOWNS[:10]
    town_links = "".join(f'<li><a href="/fence-company-{slug}-fl.html">{name}, FL</a></li>' for name, slug in popular_towns)
    material_links = "".join(f'<li><a href="/{m["slug"]}.html">{m["name"]}</a></li>' for m in MATERIALS[:6])
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="/assets/images/logo.png" alt="{SITE['full_brand']} logo" width="46" height="46">
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
          <li><a href="/about-us.html">Meet the Team</a></li>
          <li><a href="/service-areas.html">Service Areas</a></li>
          <li><a href="/fence-gallery.html">Fence Gallery</a></li>
          <li><a href="/fence-pricing.html">Pricing</a></li>
          <li><a href="/faq.html">FAQs</a></li>
          <li><a href="/contact-us.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h4>Popular Services</h4>
        <ul>
          {material_links}
          <li><a href="/commercial-fencing.html">Commercial Fencing</a></li>
          <li><a href="/fence-repair.html">Fence Repair</a></li>
        </ul>
      </div>
      <div>
        <h4>Popular Service Areas</h4>
        <ul>
          {town_links}
          <li><a href="/service-areas.html"><strong>See All Cities &rarr;</strong></a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; {SITE['year']} {SITE['brand']}&trade;. All rights reserved. {SITE['name']} is a registered DBA in the State of {SITE['state_full']}.</div>
      <div><a href="/privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a> &nbsp;|&nbsp; <a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js"></script>
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
<link rel="icon" href="/assets/images/favicon.png">
<link rel="apple-touch-icon" href="/assets/images/logo.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="/assets/images/logo.png">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
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
      <a class="btn btn-red" href="/contact-us.html">Get a Free Estimate</a>
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
        f'<a class="chip" href="/fence-company-{s}-fl.html">{n}, FL</a>' for n, s in towns
    ) + '</div>'


def cta_banner(title="Ready to Get Started?", sub="Get a free, no-obligation fence estimate today."):
    return f'''
<section class="section section-navy">
  <div class="container center">
    <h2>{title}</h2>
    <p style="max-width:560px;margin:0 auto 24px">{sub}</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-red" href="/contact-us.html">Get a Free Estimate</a>
      <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
    </div>
  </div>
</section>
'''
