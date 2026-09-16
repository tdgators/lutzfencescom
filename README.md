# Lutz Fences (76 FENCE Lutz) — Website

A full static marketing site for 76 FENCE Lutz, built from the structure of schaumburgfence.com and populated with real Lutz, FL / Tampa Bay details (phone 813-669-4511, tampa@76fence.com, real service-area towns, real team bios for Tom & Kate Donnelly).

## What's included

- `index.html` — homepage
- 6 fence material pages (vinyl, wood, aluminum, chain link, composite, steel/wrought iron) + `fence-materials.html` hub
- 5 fence style pages (privacy, semi-privacy, horizontal, picket, split rail) + `fence-styles.html` hub
- Commercial hub + 4 commercial service pages (industrial, security, HOA, dumpster enclosures)
- 6 other-service pages (repair, staining, artificial grass, DIY, deck & railing, retaining walls)
- 48 individual town/service-area landing pages (`fence-company-<town>-fl.html`)
- `about-us.html`, `service-areas.html`, `contact-us.html`, `faq.html`, `fence-gallery.html`, `fence-pricing.html`, `privacy-policy.html`
- `assets/` — stylesheet, JS (mobile nav + FAQ accordion), logo, favicon

No build tools needed — it's plain HTML/CSS/JS. Open `index.html` in a browser, or deploy the whole folder to any static host (Netlify, GitHub Pages, S3, etc.).

## Before you go live — 2 things to finish

1. **Activate the contact/quote forms.** Every form on the site (homepage, every page's "Get a Free Estimate" panel, and the Contact page) posts to a Formspree endpoint that's currently a placeholder:
   `https://formspree.io/f/YOUR_FORM_ID`
   To make submissions actually land in your inbox:
   - Go to formspree.io and create a free account with **tampa@76fence.com**.
   - Create a new form — Formspree gives you a form ID/endpoint like `https://formspree.io/f/abcd1234`.
   - Find-and-replace `YOUR_FORM_ID` across every HTML file with your real ID (or just replace the whole `formspree` value in `data.py` and re-run the generator if you're comfortable with Python — see below).
   - Formspree's free plan covers 50 submissions/month, which is normally plenty for a quote-request form; paid tiers remove the cap.

2. **Swap in real project photos.** The gallery tiles and material photos on every page are intentionally simple placeholder graphics (no real installation photos were available to me). Send over real project photos whenever you have them and they can be dropped straight into `assets/images/` and swapped into the `.tile-img .ph` blocks.

## Regenerating the site

The whole site is generated from Python in `generator/` — all 80 pages share one header/footer/nav/town-list/FAQ, defined once in `generator/data.py` and `generator/templates.py`. To make a sitewide change (add a town, edit the FAQ, update pricing, change the phone number, swap the Formspree ID), edit `generator/data.py` (or the page builders in `generator/build_*.py`) and run:

```
cd generator
python3 build_all.py
```

This rewrites every HTML file in place from the current data — much safer than hand-editing 80 files individually when something needs to change everywhere at once (like a phone number or the Formspree ID).
