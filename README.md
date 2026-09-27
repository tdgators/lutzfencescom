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

No build tools needed — it's plain HTML/CSS/JS, deployed on GitHub Pages.

**URLs:** every page lives in its own folder (`vinyl-fence/index.html`) and is served at a clean URL like `https://lutzfences.com/vinyl-fence/`. The old `vinyl-fence.html` addresses are tiny redirect pages so existing links and search results keep working. All links and asset paths are root-relative (`/assets/...`), so preview the site through a local server rather than opening files directly:

```
python3 -m http.server 8080
```

then visit http://localhost:8080.

**Sitemap:** `build_all.py` also writes `sitemap.xml` (every page, clean URLs only) and `robots.txt`. A page's `<lastmod>` date only changes when that page's content changes; `generator/sitemap-state.json` tracks this, so commit it along with the site. Submit `https://lutzfences.com/sitemap.xml` in Google Search Console.

## Before you go live — 2 things to finish

1. **Activate the contact/quote forms.** Every form on the site (homepage, every page's "Get a Free Estimate" panel, and the Contact page) posts to a Formspree endpoint that's currently a placeholder:
   `https://formspree.io/f/YOUR_FORM_ID`
   To make submissions actually land in your inbox:
   - Go to formspree.io and create a free account with **tampa@76fence.com**.
   - Create a new form — Formspree gives you a form ID/endpoint like `https://formspree.io/f/abcd1234`.
   - Find-and-replace `YOUR_FORM_ID` across every HTML file with your real ID (or just replace the whole `formspree` value in `data.py` and re-run the generator if you're comfortable with Python — see below).
   - Formspree's free plan covers 50 submissions/month, which is normally plenty for a quote-request form; paid tiers remove the cap.

2. **Swap in real project photos.** The gallery tiles and material photos on every page are intentionally simple placeholder graphics (no real installation photos were available to me). Send over real project photos whenever you have them and they can be dropped straight into `assets/images/` and swapped into the `.tile-img .ph` blocks.

## Regenerating the sites (one generator, several domains)

`generator/` builds every 76 FENCE Tampa area site from one set of templates:

| Domain | Output folder / repo |
|---|---|
| lutzfences.com | this repo |
| brooksvillefence.com | `../brooksvillefencecom` |
| northtampafencing.com | `../northtampafencingcom` |

- **Shared** (edit once, every site changes): design, header/footer, forms, warranty, materials, pricing, FAQ base — `generator/data.py`, `generator/templates.py`, `generator/build_*.py`, `assets/`.
- **Per site**: domain, phone, city/area, town list, map, and the site's own local wording — one entry in `generator/sites.py`. Give each site its own wording so the sites aren't near-duplicates.

```
cd generator
python3 build_all.py                            # all sites
python3 build_all.py --site brooksvillefence.com
```

Then commit and push each site's repo that changed. To add a new area site, copy an entry in `sites.py`, change it, build it, and create a GitHub repo for its output folder.
