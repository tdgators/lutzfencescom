"""Regenerate every site (or one) from sites.py + the shared templates.

Run: python3 build_all.py                      # all sites
     python3 build_all.py --site brooksvillefence.com
"""
import argparse
import shutil
from pathlib import Path

import build_core, build_services, build_towns, build_pdf, build_sitemap
from data import CURRENT, use_site
from sites import SITES
from templates import WRITTEN_PAGES

ASSETS_SRC = Path(__file__).resolve().parent.parent / "assets"  # shared css/js/images (lutzfencescom repo)


def sync_shared_files(out_dir, domain):
    """Give a site its own copy of the shared assets, plus the files GitHub Pages needs."""
    if out_dir.resolve() != ASSETS_SRC.parent.resolve():
        for sub in ("css", "js", "images"):
            shutil.copytree(ASSETS_SRC / sub, out_dir / "assets" / sub, dirs_exist_ok=True)
        gitignore = out_dir / ".gitignore"
        if not gitignore.exists():
            gitignore.write_text(".DS_Store\n")
        readme = out_dir / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# {domain}\n\nGenerated site — do not edit these files by hand.\n\n"
                "The pages are built from the shared generator in the `lutzfencescom` repo:\n\n"
                f"```\ncd ../lutzfencescom/generator\npython3 build_all.py --site {domain}\n```\n\n"
                "Site-specific settings and wording live in `generator/sites.py`.\n")
    (out_dir / "CNAME").write_text(domain + "\n")


def build_site(domain):
    use_site(domain)
    WRITTEN_PAGES.clear()
    out_dir = CURRENT["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    sync_shared_files(out_dir, domain)
    build_core.build_home(); build_core.build_about(); build_core.build_service_areas()
    build_core.build_contact(); build_core.build_faq(); build_core.build_gallery()
    build_core.build_pricing(); build_core.build_privacy(); build_core.build_warranty()
    build_services.build_materials(); build_services.build_styles()
    build_services.build_commercial(); build_services.build_other_services()
    build_towns.build_towns()
    build_pdf.build_warranty_pdf()
    build_sitemap.build_sitemap()
    print(f"{domain}: built {len(WRITTEN_PAGES)} pages -> {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--site", choices=sorted(SITES), help="build only this site")
    args = parser.parse_args()
    for domain in ([args.site] if args.site else SITES):
        build_site(domain)
