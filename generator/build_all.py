"""Regenerate the entire site from data.py/templates.py. Run: python3 build_all.py"""
import build_core, build_services, build_towns

if __name__ == "__main__":
    build_core.build_home(); build_core.build_about(); build_core.build_service_areas()
    build_core.build_contact(); build_core.build_faq(); build_core.build_gallery()
    build_core.build_pricing(); build_core.build_privacy()
    build_services.build_materials(); build_services.build_styles()
    build_services.build_commercial(); build_services.build_other_services()
    build_towns.build_towns()
    print("Site regenerated.")
