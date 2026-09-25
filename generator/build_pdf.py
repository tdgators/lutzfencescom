# -*- coding: utf-8 -*-
"""Builds the printable warranty PDF (assets/docs/76-fence-warranty.pdf) from WARRANTY in data.py.
Uses headless Google Chrome to print an HTML layout to PDF."""
import subprocess, tempfile, shutil
from pathlib import Path
from data import SITE, WARRANTY

OUT = Path(__file__).resolve().parent.parent
PDF_PATH = "assets/docs/76-fence-warranty.pdf"
CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chromium-browser",
]


def _chrome():
    for c in CHROME_CANDIDATES:
        if Path(c).exists() or shutil.which(c):
            return c
    return None


def warranty_print_html():
    W = WARRANTY
    logo = (OUT / "assets/images/logo.png").as_uri()
    covered = "".join(f"<li>{x}</li>" for x in W["covered"])
    not_covered = "".join(f"<li>{x}</li>" for x in W["not_covered"])
    terms = "".join(f"<h3>{h}</h3><p>{t}</p>" for h, t in W["terms"])
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{W['issuer']} {W['name']}</title>
<style>
  @page {{ size: letter; margin: 0.55in 0.6in 0.6in; }}
  :root {{ --navy:#17356b; --navy-dark:#0d2447; --red:#e22a38; --ink:#1c2733; --gray:#45505c; --muted:#6b7686; --line:#e4e8ee; --bg:#f4f6f9; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family: -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif; color:var(--ink); font-size:10pt; line-height:1.45;
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  h1,h2,h3 {{ color:var(--navy); margin:0; line-height:1.15; }}
  p {{ margin:0 0 .6em; color:var(--gray); }}
  .band {{ background:linear-gradient(120deg,var(--navy),var(--navy-dark)); color:#fff; border-radius:10px; padding:22px 26px;
          display:flex; align-items:center; gap:22px; border-bottom:5px solid var(--red); }}
  .band img {{ width:62px; height:62px; flex:none; }}
  .band .t {{ flex:1; }}
  .band .eyebrow {{ color:#ff8a94; font-size:8pt; font-weight:800; letter-spacing:.14em; text-transform:uppercase; margin-bottom:4px; }}
  .band h1 {{ color:#fff; font-size:20pt; }}
  .band p {{ color:#d3ddea; margin:6px 0 0; font-size:9.5pt; }}
  .seal {{ flex:none; width:104px; height:104px; border-radius:50%; background:var(--navy); border:4px solid var(--red);
          box-shadow:0 0 0 3px #fff; display:flex; flex-direction:column; align-items:center; justify-content:center; line-height:1; text-align:center; }}
  .seal b {{ font-size:32pt; color:#fff; letter-spacing:-.02em; }}
  .seal span {{ font-size:7pt; font-weight:800; color:#fff; letter-spacing:.18em; text-transform:uppercase; margin-top:2px; }}
  .seal small {{ font-size:5.5pt; font-weight:700; color:#c9d5e3; letter-spacing:.08em; text-transform:uppercase; margin-top:4px; line-height:1.25; }}
  .pillars {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin:18px 0 16px; }}
  .pill {{ border:1px solid var(--line); border-top:3px solid var(--navy); border-radius:8px; padding:12px 14px; }}
  .pill h3 {{ font-size:10.5pt; margin-bottom:4px; }}
  .pill p {{ font-size:8.8pt; margin:0; }}
  .cols {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }}
  .box {{ background:var(--bg); border-radius:8px; padding:14px 16px; }}
  .box h2 {{ font-size:11.5pt; margin-bottom:4px; }}
  .box p {{ font-size:8.8pt; margin-bottom:6px; }}
  ul {{ list-style:none; margin:0; padding:0; }}
  li {{ position:relative; padding:3px 0 3px 20px; font-size:8.8pt; color:var(--gray); }}
  li::before {{ position:absolute; left:0; top:4px; width:13px; height:13px; border-radius:50%; color:#fff; font-size:7pt; font-weight:800;
               display:flex; align-items:center; justify-content:center; }}
  .yes li::before {{ content:"\\2713"; background:var(--navy); }}
  .no li::before {{ content:"\\2715"; background:var(--muted); }}
  .note {{ font-size:8.3pt; color:var(--muted); text-align:center; margin:10px 0 0; }}
  .steps {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:8px; }}
  .step {{ border:1px solid var(--line); border-radius:8px; padding:12px 14px 10px; }}
  .step .n {{ display:inline-flex; width:20px; height:20px; border-radius:50%; background:var(--red); color:#fff; font-weight:800; font-size:8.5pt;
             align-items:center; justify-content:center; margin-bottom:6px; }}
  .step h3 {{ font-size:10pt; margin-bottom:3px; }}
  .step p {{ font-size:8.8pt; margin:0; }}
  .sec {{ margin-top:18px; }}
  .sec > h2 {{ font-size:13pt; }}
  .kicker {{ color:var(--red); font-size:7.5pt; font-weight:800; letter-spacing:.14em; text-transform:uppercase; margin-bottom:3px; }}
  .terms {{ break-before:page; }}
  .terms > h2 {{ font-size:15pt; padding-bottom:8px; border-bottom:3px solid var(--red); margin-bottom:4px; }}
  .terms h3 {{ font-size:10.5pt; margin:14px 0 4px; }}
  .terms p {{ font-size:9.6pt; }}
  .contact {{ margin-top:22px; background:var(--navy); color:#fff; border-radius:8px; padding:14px 18px; display:flex; justify-content:space-between; align-items:center; gap:16px; }}
  .contact b {{ font-size:11pt; }}
  .contact span {{ color:#d3ddea; font-size:9.5pt; }}
  .foot {{ margin-top:14px; font-size:7.8pt; color:var(--muted); text-align:center; }}
  a {{ color:inherit; text-decoration:none; }}
</style></head><body>

<div class="band">
  <img src="{logo}" alt="">
  <div class="t">
    <div class="eyebrow">{W['tagline']}</div>
    <h1>{W['name']}</h1>
    <p>Every fence we install is backed by {W['issuer']} for {W['weeks']} weeks ({W['approx']}) against defects in our installation and assembly. If it's our workmanship, we'll make it right.</p>
  </div>
  <div class="seal"><b>{W['weeks']}</b><span>Week</span><small>Workmanship<br>Warranty</small></div>
</div>

<div class="pillars">
  <div class="pill"><h3>Covers Our Workmanship</h3><p>Defects in our installation and assembly. If it's our workmanship, we'll make it right.</p></div>
  <div class="pill"><h3>{W['weeks']} Weeks of Coverage</h3><p>Coverage runs {W['weeks']} weeks from your installation completion date, as recorded in our records.</p></div>
  <div class="pill"><h3>No Charge to You</h3><p>If an issue is covered, we repair or correct the workmanship at no cost to you.</p></div>
</div>

<div class="cols">
  <div class="box yes"><h2>What&rsquo;s Covered</h2><p>Defects resulting directly from our workmanship or installation, such as:</p><ul>{covered}</ul></div>
  <div class="box no"><h2>What&rsquo;s Not Covered</h2><p>Damage or changes resulting from:</p><ul>{not_covered}</ul></div>
</div>
<p class="note">Coverage applies to projects paid in full and runs from your recorded installation completion date. Material and product issues may be covered separately by the product manufacturer&rsquo;s warranty, where applicable.</p>

<div class="sec">
  <div class="kicker">Warranty Service</div>
  <h2>How to Request Warranty Service</h2>
  <div class="steps">
    <div class="step"><div class="n">1</div><h3>Contact Us</h3><p>Call or text Tampa at {SITE['tampa_phone']} or Lutz at {SITE['phone']}, or email {SITE['email']}.</p></div>
    <div class="step"><div class="n">2</div><h3>Share the Details</h3><p>Send your installation address and a description or photos of the issue.</p></div>
    <div class="step"><div class="n">3</div><h3>We Inspect &amp; Fix It</h3><p>We evaluate the condition, and if it&rsquo;s covered, we repair or correct the workmanship at no charge.</p></div>
  </div>
</div>

<div class="terms">
  <div class="kicker">Full Terms</div>
  <h2>{W['issuer']} &mdash; {W['name']}</h2>
  {terms}
  <div class="contact">
    <div><b>{W['issuer']}</b><br><span>Tampa &amp; Lutz locations &middot; serving the {SITE['region']} area</span></div>
    <div style="text-align:right"><b>Tampa {SITE['tampa_phone']} &nbsp;&middot;&nbsp; Lutz {SITE['phone']}</b><br><span>{SITE['email']} &middot; {SITE['domain']}</span></div>
  </div>
  <div class="foot">&copy; {SITE['year']} {SITE['brand']}&trade;. This document states the terms of the {W['issuer']} {W['name']}.</div>
</div>

</body></html>'''


def build_warranty_pdf():
    chrome = _chrome()
    if not chrome:
        print("Chrome not found — skipped warranty PDF.")
        return
    out = OUT / PDF_PATH
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "warranty-print.html"
        src.write_text(warranty_print_html(), encoding="utf-8")
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--allow-file-access-from-files", f"--print-to-pdf={out}", src.as_uri()],
                       check=True, capture_output=True, timeout=120)
    print(f"wrote {PDF_PATH}")


if __name__ == "__main__":
    build_warranty_pdf()
