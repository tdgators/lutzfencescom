# -*- coding: utf-8 -*-
import re
from pathlib import Path
from data import SITE, TOWNS, COPY, THEME, T, MATERIALS, STYLES, COMMERCIAL, OTHER_SERVICES, WARRANTY

def esc(s):
    return s

def nav_html(active=""):
    def li(label, href, key, dropdown=None, extra=False):
        # extra=True: hidden from the header at medium widths (still in the menu-button drawer)
        cls = ' class="nav-extra"' if extra else ""
        if dropdown:
            return f'''<li{cls}><button class="nav-toggle" type="button">{label} <span>▾</span></button>
              <div class="dropdown">{dropdown}</div></li>'''
        return f'<li{cls}><a href="{href}">{label}</a></li>'

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
    about_dd = '<a href="about-us.html">Meet the Team</a><a href="warranty.html">Our Warranty</a><a href="service-areas.html">Service Areas</a>'
    contact_dd = '<a href="contact-us.html">Contact Us</a><a href="faq.html">FAQs</a>'

    items = [
        li("Home", "index.html", "home"),
        li("Residential", "#", "residential", residential_dd, extra=True),
        li("Commercial", "#", "commercial", commercial_dd, extra=True),
        li("Other Services", "#", "other", other_dd, extra=True),
        li("Fence Gallery", "fence-gallery.html", "gallery"),
        li("About", "#", "about", about_dd),
        li("Contact", "#", "contact", contact_dd),
    ]
    return "<ul>" + "".join(items) + "</ul>"


def header_html(active=""):
    return f'''
<div class="topbar">
  <div class="container">
    <div>Licensed in {SITE['licensed_short']} &middot; Fully Insured &middot; Free Estimates &middot; Serving {SITE['city']}, {SITE['state']} &amp; the {SITE['region']} area</div>
    <div><a href="mailto:{SITE['email']}">{SITE['email']}</a> &nbsp;|&nbsp; <a class="topbar-phone" href="tel:{SITE['phone_tel']}">{SITE['phone']}</a></div>
  </div>
</div>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="index.html">
      <img src="assets/images/logo.png" alt="{SITE['full_brand']} logo" width="54" height="54">
      <span>{SITE['brand']}<small>{SITE['brand_sub']}</small></span>
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
        <p>{T("footer_about", f"{SITE['name']} ({SITE['domain']}) is a marketing website for {SITE['brand']}&trade;, serving {SITE['city']}, {SITE['state']} and the surrounding {SITE['region']} area with residential and commercial fence installation, repair, and maintenance.")}</p>
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
          <li><a href="warranty.html">76-Week Warranty</a></li>
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
      <div>&copy; {SITE['year']} {SITE['brand']}&trade;. All rights reserved. {SITE['name']} is a division of {SITE['parent']}, a registered DBA in the State of {SITE['state_full']}.</div>
      <div><a href="privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="tel:{SITE['phone_tel']}">{SITE['phone']}</a> &nbsp;|&nbsp; <a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
    </div>
  </div>
</footer>
{estimate_modal()}
{FORMSPREE_AJAX_SCRIPT}
<script src="assets/js/main.js"></script>
'''


def pretty_url(path):
    """'vinyl-fence.html' -> '/vinyl-fence/', 'index.html' -> '/'."""
    slug = path[:-len(".html")] if path.endswith(".html") else path
    return "/" if slug == "index" else f"/{slug}/"


_PAGE_LINK = re.compile(r'(href)="([a-z0-9-]+)\.html(#[^"]*)?"')
_ASSET_LINK = re.compile(r'(href|src|content)="assets/')


def finalize(html):
    """Rewrite in-site links to directory-style URLs and make asset paths root-relative,
    so pages work from any directory depth."""
    html = _PAGE_LINK.sub(lambda m: f'{m[1]}="{pretty_url(m[2] + ".html")}{m[3] or ""}"', html)
    html = _ASSET_LINK.sub(lambda m: f'{m[1]}="/assets/', html)
    return html



# Every page written this build, keyed by URL path — used by build_sitemap.py.
WRITTEN_PAGES = {}


def write_404(out_root, html):
    """GitHub Pages serves /404.html (site root, not a folder) for any missing address.
    Not added to the sitemap."""
    (Path(out_root) / "404.html").write_text(finalize(html), encoding="utf-8")


def write_page(out_root, path, html):
    """Write 'foo.html' as foo/index.html (served at /foo/).
    index.html stays at the site root."""
    out_root = Path(out_root)
    html = finalize(html)
    WRITTEN_PAGES[pretty_url(path)] = html
    if path == "index.html":
        (out_root / "index.html").write_text(html, encoding="utf-8")
        return
    slug = path[:-len(".html")]
    target = out_root / slug / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


DEFAULT_FONTS = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"


def theme_style():
    """The site's design tokens (THEME['vars'], e.g. {'--accent': '#2f5d3a'}) layered over styles.css."""
    tokens = THEME.get("vars")
    if not tokens:
        return ""
    return "<style>:root{" + "".join(f"{k}:{v};" for k, v in tokens.items()) + "}</style>\n"


def body_class():
    cls = THEME.get("body_class")
    return f' class="{cls}"' if cls else ""


def page(title, description, path, content, canonical=None, noindex=False):
    canonical = canonical or f"https://{SITE['domain']}{pretty_url(path)}"
    head_meta = ('<meta name="robots" content="noindex">' if noindex
                 else f'<link rel="canonical" href="{canonical}">')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
{head_meta}
<link rel="icon" href="assets/images/favicon.png">
<link rel="apple-touch-icon" href="assets/images/logo.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://{SITE['domain']}/assets/images/logo.png">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="{THEME.get('fonts_href', DEFAULT_FONTS)}" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
{theme_style()}</head>
<body{body_class()}>
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
    <div class="eyebrow">{eyebrow}</div>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    <div class="cta-row">
      <a class="btn btn-red" href="contact-us.html">{T("labels.estimate", "Get a Free Estimate")}</a>
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

def source_fields():
    """Hidden fields on every quote form: the email subject names the site the lead came from,
    and `source` carries the domain as data (for Jobber lead source / the platform later)."""
    domain = SITE['domain']
    return (f'<input type="hidden" name="_subject" value="[{domain}] New quote request">\n'
            f'    <input type="hidden" name="source" value="{domain}">\n'
            f'    {HONEYPOT_FIELD}')


# Honeypot: hidden from people, but bots fill it in — Formspree silently discards those submissions.
HONEYPOT_FIELD = '<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="display:none">'


def formspree_init(form_selector):
    """Wire a form to Formspree. On success: clear the form and scroll the thank-you
    message into view (on phones the submit button is far below it)."""
    return f'''<script>
  window.formspree = window.formspree || function () {{ (formspree.q = formspree.q || []).push(arguments); }};
  formspree('initForm', {{
    formElement: '{form_selector}',
    formId: '{_formspree_id()}',
    onSuccess: function (context) {{
      context.form.reset();
      if (window.estimateStep) window.estimateStep(context.form, 1);
      var msg = context.form.parentElement.querySelector('[data-fs-success]');
      if (msg) msg.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    }}
  }});
</script>'''


def estimate_steps(prefix, submit_label):
    """Two-step estimate form body. Step 1 (required): contact + property address.
    Step 2 (optional): fence details, then Submit. Field names match the
    76 FENCE platform's lead fields (street_address, zip, job_type, fence_type) for a later hand-off.
    Step switching lives in assets/js/main.js (.est-form)."""
    def field(name, label, type_="text", required=True, extra=""):
        req = " required" if required else ""
        return (f'<div><label for="{prefix}-{name}">{label}</label>'
                f'<input id="{prefix}-{name}" type="{type_}" name="{name}" data-fs-field{req}{extra}>'
                f'<span class="fs-field-error" data-fs-error="{name}"></span></div>')

    def choices(name, legend, options):
        opts = "".join(f'<label class="est-choice"><input type="radio" name="{name}" value="{v}"><span>{v}</span></label>'
                       for v in options)
        return f'<fieldset class="est-choices"><legend>{legend}</legend><div>{opts}</div></fieldset>'

    materials = ["Not sure yet", "Vinyl", "Wood", "Aluminum", "Chain link", "Composite", "Steel / ornamental"]
    material_opts = "".join(f'<option value="{m}">{m}</option>' for m in materials)
    return f'''
    <div class="est-steps">
    <div class="est-step is-active" data-step="1">
      <div class="est-progress"><b>Step 1 of 2</b> · Your contact info &amp; property</div>
      <div class="form-row full">{field("full_name", "Full Name", extra=' autocomplete="name"')}</div>
      <div class="form-row">{field("phone", "Phone", "tel", extra=' autocomplete="tel"')}{field("email", "Email", "email", extra=' autocomplete="email"')}</div>
      <div class="form-row full">{field("street_address", "Street Address", extra=' autocomplete="address-line1"')}</div>
      <div class="form-row est-cityzip">{field("city", "City", extra=' autocomplete="address-level2"')}{field("zip", "ZIP", extra=' inputmode="numeric" pattern="[0-9]{5}" maxlength="5" title="5-digit ZIP code" autocomplete="postal-code"')}</div>
      <button class="btn btn-red btn-block est-next" type="button">Next: Fence Details &rarr;</button>
    </div>
    <div class="est-step" data-step="2" inert aria-hidden="true">
      <div class="est-progress"><b>Step 2 of 2</b> · A few quick details <span>(optional)</span></div>
      {choices("job_type", "New fence or repair?", ["New fence", "Repair"])}
      <div class="form-row full"><div><label for="{prefix}-fence_type">Fence material</label>
        <select id="{prefix}-fence_type" name="fence_type" autocomplete="off"><option value="">Choose one</option>{material_opts}</select></div></div>
      <div class="form-row">
        <div><label for="{prefix}-linear_feet">Approx. feet of fence</label><input id="{prefix}-linear_feet" type="number" name="linear_feet" min="0" step="10" inputmode="numeric" placeholder="e.g. 150" autocomplete="off"></div>
        <div><label for="{prefix}-gates">Number of gates</label><select id="{prefix}-gates" name="gates" autocomplete="off"><option value="">Choose</option><option>0</option><option>1</option><option>2</option><option>3+</option></select></div>
      </div>
      {choices("remove_old_fence", "Remove &amp; haul away an old fence?", ["Yes", "No"])}
      <div class="est-actions">
        <button class="est-back" type="button">&larr; Back</button>
        <button class="btn btn-red" type="submit" data-fs-submit-btn>{submit_label}</button>
      </div>
    </div>
    </div>
    {source_fields()}
    <div class="fs-error" data-fs-error></div>'''


def estimate_modal():
    """The estimate form as a pop-up (full-screen sheet on phones). main.js opens it from any
    button linking to the contact page; without JS those buttons still go to the page."""
    return f'''
<div class="est-modal" id="estimate-modal" hidden>
  <div class="est-modal-backdrop" data-close></div>
  <div class="est-modal-panel" role="dialog" aria-modal="true" aria-labelledby="estimate-modal-title">
    <div class="est-modal-head">
      <button class="est-modal-close" type="button" data-close aria-label="Close">&times;</button>
      <div class="est-modal-brand">
        <img src="assets/images/logo.png" alt="" width="46" height="46">
        <span>{SITE['name'] if SITE['full_brand'] == SITE['parent'] else SITE['full_brand']}<small>{SITE['parent']}</small></span>
      </div>
      <h3 id="estimate-modal-title">{T("labels.modal_title", "Get Your Free Estimate")}</h3>
      <p class="est-modal-trust">Licensed &amp; insured &middot; 76-week workmanship warranty &middot; No obligation</p>
    </div>
    <div class="est-modal-body">
      <div class="fs-success" data-fs-success>Thanks! Your request is in — we'll call or text you back shortly.</div>
      <form id="modal-quote-form" class="est-form">{estimate_steps("modal", "Submit")}
      </form>
      <p class="est-modal-call">Prefer to talk? <a href="tel:{SITE['phone_tel']}">Call or text {SITE['phone']}</a></p>
      <p class="consent">By submitting, you consent to be contacted by {SITE['full_brand']} by phone, text, or email about your request.</p>
    </div>
  </div>
</div>
{formspree_init('#modal-quote-form')}'''


def mini_quote_form(heading="Get Your Free Estimate"):
    return f'''
<div class="hero-panel">
  <h3>{heading}</h3>
  <p>Tell us where the fence is going — we'll call or text you back fast.</p>
  <div class="fs-success" data-fs-success>Thanks! Your request is in — we'll call or text you back shortly.</div>
  <form id="hero-quote-form" class="est-form">{estimate_steps("hero", "Submit")}
  </form>
  <p class="consent" style="margin-top:10px">By submitting, you consent to be contacted by {SITE['full_brand']} by phone, text, or email about your request.</p>
</div>
{formspree_init('#hero-quote-form')}
'''


def contact_form_card():
    return f'''
<div class="form-card">
  <h3>Request Your Free Estimate</h3>
  <p>Start with your address, then add a few optional details about the fence you have in mind.</p>
  <div class="fs-success" data-fs-success>Thanks! Your request is in — we'll be in touch shortly to schedule your free estimate.</div>
  <form id="contact-quote-form" class="est-form">{estimate_steps("contact", "Submit")}
    <p class="consent" style="margin-top:12px">By submitting, you consent to be contacted by {SITE['full_brand']} by phone, text, or email about your request. We don't sell or share your information.</p>
  </form>
</div>
{formspree_init('#contact-quote-form')}
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

# Real installed-fence photos, keyed by the same "kind" strings used above.
# Any kind not listed here (currently just "steel") falls back to the SVG
# illustration since no real photo is available for it yet.
_PHOTO_KINDS = {
    "vinyl": "vinyl-fence.jpg",
    "wood": "wood-fence.jpg",
    "aluminum": "aluminum-fence.jpg",
    "chain-link": "chain-link-fence.jpg",
    "composite": "composite-fence.jpg",
    "security": "security-fence.jpg",
    "picket": "picket-fence.jpg",
    "split-rail": "split-rail-fence.jpg",
    "horizontal": "horizontal-fence.jpg",
    "steel": "steel-fence.jpg",
}


def fence_illustration(kind):
    photo = _PHOTO_KINDS.get(kind)
    if photo:
        return (f'<img src="assets/images/materials/{photo}" alt="{kind.replace("-", " ").title()} fence" '
                f'loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;">')
    fn = _SVG_KINDS.get(kind, svg_vinyl)
    return fn()


def warranty_seal(size=""):
    cls = f"warranty-seal {size}".strip()
    return f'''<div class="{cls}" aria-hidden="true">
  <span class="ws-num">{WARRANTY['weeks']}</span>
  <span class="ws-unit">Week</span>
  <span class="ws-label">Workmanship<br>Warranty</span>
</div>'''


def warranty_callout(context="your fence"):
    """Compact strip linking to warranty.html — dropped into service and town pages."""
    return f'''
<section class="section warranty-strip">
  <div class="container">
    <div class="warranty-callout">
      {warranty_seal()}
      <div>
        <div class="eyebrow">{T("warranty_box.eyebrow", WARRANTY['tagline'])}</div>
        <h2>{T("warranty_box.title", f"Backed by Our {WARRANTY['short']}")}</h2>
        <p>{T("warranty_box.text", "Every installation comes with the {issuer} {name}. If there's a defect in how we installed or assembled {context} within {weeks} weeks ({approx}) of your installation date, we'll inspect it and make it right at no charge. Materials are also covered separately by the manufacturer's warranty.").format(issuer=WARRANTY['issuer'], name=WARRANTY['name'], context=context, weeks=WARRANTY['weeks'], approx=WARRANTY['approx'])}</p>
        <a class="btn btn-navy-outline" href="warranty.html">See Warranty Details</a>
      </div>
    </div>
  </div>
</section>
'''


def cta_banner(title=None, sub=None):
    title = title or T("cta.title", "Ready to Get Started?")
    sub = sub or T("cta.sub", "Get a free, no-obligation fence estimate today.")
    return f'''
<section class="section section-navy">
  <div class="container center">
    <h2>{title}</h2>
    <p style="max-width:560px;margin:0 auto 24px">{sub}</p>
    <div class="cta-row" style="justify-content:center">
      <a class="btn btn-red" href="contact-us.html">{T("labels.estimate", "Get a Free Estimate")}</a>
      <a class="btn btn-outline" href="tel:{SITE['phone_tel']}">Call {SITE['phone']}</a>
    </div>
  </div>
</section>
'''
