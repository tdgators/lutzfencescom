# -*- coding: utf-8 -*-
"""Per-site settings. Every site shares the templates, design, warranty, and forms in
data.py / templates.py; only what's listed here differs.

Add a site: copy an entry, change the values, give it its own local wording (so the
sites aren't near-duplicates), and run: python3 build_all.py --site <domain>

Town-page wording can use {town}, {state}, {state_full}, {brand}, {region} placeholders."""
from pathlib import Path

REPOS = Path(__file__).resolve().parent.parent.parent  # ~/Repos

# Shared by every site: 76 FENCE Tampa is the registered DBA; Lutz and Tampa are its two lines.
COMMON = dict(
    brand="76 FENCE",
    parent="76 FENCE Tampa",
    tampa_phone="813-669-4555",
    tampa_phone_tel="+18136694555",
    lutz_phone="813-669-4511",
    lutz_phone_tel="+18136694511",
    email="tampa@76fence.com",
    state="FL",
    state_full="Florida",
    fb="https://www.facebook.com/76FenceLutz",
    ig="https://www.instagram.com/76fencelutz",
    google="https://g.page/r/CYR3FNx_NQIDEAI",
    year="2026",
    formspree="https://formspree.io/f/xaenwbav",
)

SITES = {
    # ------------------------------------------------------------------ lutzfences.com
    "lutzfences.com": dict(
        out_dir=REPOS / "lutzfencescom",
        legacy_redirects=True,  # keep the old /page.html addresses forwarding to /page/
        site=dict(
            name="Lutz Fences",
            full_brand="76 FENCE Lutz",
            brand_sub="Lutz, FL",
            phone="813-669-4511",
            phone_tel="+18136694511",
            city="Lutz",
            region="Tampa Bay",
            domain="lutzfences.com",
            map_embed="https://www.google.com/maps?q=76+Fence+Tampa,+Lutz,+FL&output=embed",
        ),
        towns=[
            ("Lutz", "lutz"), ("Land O' Lakes", "land-o-lakes"), ("Land O' Lakes North", "land-o-lakes-north"),
            ("Odessa", "odessa"), ("Wesley Chapel", "wesley-chapel"), ("New Port Richey", "new-port-richey"),
            ("New Port Richey East", "new-port-richey-east"), ("Port Richey", "port-richey"),
            ("Zephyrhills", "zephyrhills"), ("Dade City", "dade-city"), ("San Antonio", "san-antonio"),
            ("Saint Leo", "saint-leo"), ("Spring Hill", "spring-hill"), ("Spring Hill South", "spring-hill-south"),
            ("Brooksville", "brooksville"), ("Brooksville East", "brooksville-east"), ("Ridge Manor", "ridge-manor"),
            ("Nobleton", "nobleton"), ("Masaryktown", "masaryktown"), ("Shady Hills", "shady-hills"),
            ("Hudson", "hudson"), ("Hudson South", "hudson-south"), ("Gulf Harbors", "gulf-harbors"),
            ("Angeline", "angeline"), ("Beacon Woods", "beacon-woods"), ("Bexley", "bexley"),
            ("Chapel Crossings", "chapel-crossings"), ("Connerton", "connerton"), ("Epperson Lagoon", "epperson-lagoon"),
            ("Estancia", "estancia"), ("Lake Bernadette", "lake-bernadette"), ("Lake Jovita", "lake-jovita"),
            ("Lake Padgett Estates", "lake-padgett-estates"), ("Lexington Oaks", "lexington-oaks"),
            ("Meadow Pointe", "meadow-pointe"), ("Oakstead", "oakstead"), ("Richland", "richland"),
            ("Saddlebrook", "saddlebrook"), ("Saint Joseph", "saint-joseph"), ("Seven Hills", "seven-hills"),
            ("Seven Oaks", "seven-oaks"), ("Southern Hills", "southern-hills"), ("Southport Springs", "southport-springs"),
            ("Sterling Hill", "sterling-hill"), ("Union Park", "union-park"), ("WaterGrass", "watergrass"),
            ("Wilderness Lake Preserve", "wilderness-lake-preserve"), ("Wiregrass Ranch", "wiregrass-ranch"),
        ],
        copy=dict(
            hero_lead="Residential &amp; commercial fence installation built on quality, trust, and proven results. Vinyl, wood, aluminum, chain link, composite &amp; steel — installed, repaired, and maintained by a locally owned Tampa Bay team.",
            why_local=("Family Owned &amp; Locally Operated", "76 FENCE Lutz is owned and run by Tom &amp; Kate Donnelly, right here in the Tampa Bay area."),
            about_lead="76 FENCE Lutz is a locally owned and operated fence company, proudly part of the national 76 FENCE network.",
            about_story=[
                "76 FENCE Lutz brings the training, purchasing power, and manufacturer relationships of the national 76 FENCE network to a business that's owned and run right here in the Tampa Bay area. The 76 FENCE name is a nod to 1776 — American craftsmanship, straightforward dealing, and standing behind the work.",
                "We install and repair fencing for homeowners, HOAs, and businesses across Lutz and the surrounding communities, and we handle the permitting process, the installation, and anything that needs fixing down the road.",
            ],
            service_areas_meta="See every city and community 76 FENCE Lutz serves near Lutz, FL, including Land O' Lakes, Wesley Chapel, Odessa, New Port Richey, and more.",
            faq_lead="Answers to the questions we hear most from Lutz-area homeowners and businesses.",
            address_placeholder="e.g. Lutz, FL",
            local_section=None,
            local_faqs=[],
            town_intros=[
                "When you're ready to add a fence in {town}, you want a contractor who shows up, pulls the right permits, and builds something that holds up to Florida weather for years to come. That's what {brand} does for homeowners and businesses across {town} every week.",
                "Looking for a fence company near {town}, {state}? {brand} installs and repairs residential and commercial fencing throughout {town} and the surrounding {region} area, with free estimates and no pressure.",
                "{brand} is proud to serve {town} with professional fence installation, repair, and maintenance — from a simple backyard privacy fence to a full commercial security perimeter.",
                "Homeowners and businesses in {town} trust {brand} for fence installation because we handle the permitting, the install, and anything that needs fixing down the road, all under one roof.",
            ],
            town_why=[
                "We're locally owned and operated, backed by the training and manufacturer relationships of the national {brand} network — so you get big-company buying power with small-business accountability.",
                "Every {town} estimate is free, and every installation is backed by the manufacturer's warranty plus our own <a href=\"warranty.html\">76-Week Limited Workmanship Warranty</a>.",
                "We're fully insured — general liability and workers' compensation — and we handle the local permitting process for most {town} projects as part of your price.",
            ],
            town_permit=[
                "Most fence projects in {state_full} require a local permit, and if your property has a pool, your fence or gate also needs to meet Florida's residential pool safety barrier code. We handle that process for {town} homeowners so you don't have to.",
                "If you're part of an HOA in {town}, your community likely requires board approval before installation — we're happy to help put together what your HOA needs to review your project.",
            ],
        ),
    ),

    # ------------------------------------------------------------------ brooksvillefence.com
    "brooksvillefence.com": dict(
        out_dir=REPOS / "brooksvillefencecom",
        site=dict(
            name="Brooksville Fence",
            full_brand="76 FENCE Tampa",
            brand_sub="Brooksville &amp; Hernando County",
            phone="813-669-4555",
            phone_tel="+18136694555",
            city="Brooksville",
            region="Hernando County",
            domain="brooksvillefence.com",
            map_embed="https://www.google.com/maps?q=Brooksville,+FL&output=embed",
        ),
        towns=[
            ("Brooksville", "brooksville"), ("Spring Hill", "spring-hill"), ("Weeki Wachee", "weeki-wachee"),
            ("Ridge Manor", "ridge-manor"), ("Nobleton", "nobleton"), ("Masaryktown", "masaryktown"),
            ("Hernando Beach", "hernando-beach"), ("Dade City", "dade-city"), ("San Antonio", "san-antonio"),
        ],
        copy=dict(
            hero_lead="Fence installation for Brooksville's acreage, hills, and neighborhoods — privacy, farm, pool, and security fencing in vinyl, wood, aluminum, chain link, and steel, installed and backed by the 76 FENCE Tampa team.",
            why_local=("Owner-Operated, Hernando County Crews", "76 FENCE Tampa is owned and run by Tom &amp; Kate Donnelly, and our crews work Brooksville, Spring Hill, and the rest of Hernando County every week."),
            about_lead="Brooksville Fence is the Hernando County home of 76 FENCE Tampa — the same owner-operated team, focused on Brooksville and its neighbors.",
            about_story=[
                "Brooksville Fence is part of 76 FENCE Tampa, the locally owned 76 FENCE location run by Tom &amp; Kate Donnelly. We started in the Tampa Bay suburbs and now build fences across Brooksville, Spring Hill, and the rest of Hernando County — with the training, purchasing power, and manufacturer relationships of the national 76 FENCE network behind every job.",
                "Brooksville properties aren't typical suburban lots. Rolling terrain, larger acreage, and rock close to the surface all change how a fence goes in, so we plan post depth, grade changes, and gate placement on site instead of quoting from a template.",
            ],
            service_areas_meta="76 FENCE Tampa builds fences across Brooksville and Hernando County, including Spring Hill, Weeki Wachee, Ridge Manor, Nobleton, and Masaryktown.",
            faq_lead="Answers to the questions we hear most from Brooksville and Hernando County property owners.",
            address_placeholder="e.g. Brooksville, FL",
            local_section=dict(
                eyebrow="Built for Brooksville",
                title="Fencing for Hernando County Properties",
                intro="From downtown Brooksville to acreage along the Brooksville Ridge, local properties ask more of a fence than a standard backyard does.",
                cards=[
                    ("Acreage &amp; Farm Fencing", "Split rail, ranch-style wood, and wire-mesh combinations to mark property lines, keep animals in, and cover long runs without breaking the budget."),
                    ("Hills &amp; Grade Changes", "On sloped lots we step or rack panels to follow the ground, so there are no big gaps under the fence and no crooked lines on top."),
                    ("Rock &amp; Soil", "Where rock sits close to the surface, we plan post depth and footings on site so posts are set solid the first time."),
                    ("Pools &amp; Code", "Aluminum and vinyl pool enclosures with self-closing, self-latching gates built to Florida's pool barrier requirements."),
                ],
            ),
            local_faqs=[
                ("Do you install fencing on acreage and farm properties around Brooksville?",
                 "Yes. We build split rail, ranch-style wood, and wire-mesh fencing for larger Hernando County properties, and we'll walk the property line with you to plan corners, gates, and access for equipment."),
                ("Do I need a permit for a fence in Brooksville or Hernando County?",
                 "Many fence projects in the City of Brooksville and unincorporated Hernando County need a permit, and any fence that's part of a pool barrier has to meet Florida's pool code. We check the requirements for your address and handle the permit as part of the job."),
                ("Can you build a fence on a sloped or hilly lot?",
                 "Yes. Depending on the material, we step the panels down the slope or rack them to follow the grade, and we set posts to match the terrain so the fence stays straight and secure."),
            ],
            town_intros=[
                "Planning a fence in {town}? {brand} builds privacy, pool, farm, and security fencing across {town} and the rest of {region}, and we quote every job on site — not from a price sheet.",
                "{town} homeowners call {brand} when they want the fence done right the first time: permits handled, posts set for the ground they're going into, and a crew that cleans up before it leaves.",
                "From small backyards to multi-acre lots, {brand} installs and repairs fencing throughout {town}. Tell us what you need to keep in, keep out, or keep private, and we'll recommend the material that fits.",
            ],
            town_why=[
                "{brand} is owner-operated by Tom &amp; Kate Donnelly and backed by the national {brand} network, so {town} customers get a local point of contact with national buying power.",
                "Every {town} estimate is free, and every installation comes with the manufacturer's warranty plus our <a href=\"warranty.html\">76-Week Limited Workmanship Warranty</a>.",
                "We're fully insured, with general liability and workers' compensation coverage, and we check the permit requirements for your {town} address before we quote — no surprises on install day.",
            ],
            town_permit=[
                "Fence rules in {region} depend on whether your property is inside city limits, in a deed-restricted neighborhood, or on rural land. We sort out the permit and any HOA paperwork for {town} projects so you don't have to.",
                "If you have a pool, your fence or gate may be part of the required pool barrier under Florida code. We build {town} pool enclosures with self-closing, self-latching gates that meet it.",
            ],
        ),
    ),

    # ------------------------------------------------------------------ northtampafencing.com
    "northtampafencing.com": dict(
        out_dir=REPOS / "northtampafencingcom",
        site=dict(
            name="North Tampa Fencing",
            full_brand="76 FENCE Tampa",
            brand_sub="New Tampa &amp; North Tampa",
            phone="813-669-4555",
            phone_tel="+18136694555",
            city="North Tampa",
            region="Tampa Bay",
            domain="northtampafencing.com",
            map_embed="https://www.google.com/maps?q=New+Tampa,+Tampa,+FL&output=embed",
        ),
        towns=[
            ("New Tampa", "new-tampa"), ("Tampa Palms", "tampa-palms"), ("Hunter's Green", "hunters-green"),
            ("Cross Creek", "cross-creek"), ("K-Bar Ranch", "k-bar-ranch"), ("Temple Terrace", "temple-terrace"),
            ("Carrollwood", "carrollwood"), ("Lutz", "lutz"),
        ],
        copy=dict(
            hero_lead="Fence installation for New Tampa, Tampa Palms, Temple Terrace, and North Tampa neighborhoods — HOA-ready privacy, pool, and decorative fencing from the owner-operated 76 FENCE Tampa team.",
            why_local=("Owner-Operated, North Tampa Based", "76 FENCE Tampa is owned and run by Tom &amp; Kate Donnelly, and North Tampa is our home turf — New Tampa, Tampa Palms, and the neighborhoods around them."),
            about_lead="North Tampa Fencing is 76 FENCE Tampa's team for New Tampa and North Tampa — owner-operated, and backed by the national 76 FENCE network.",
            about_story=[
                "North Tampa Fencing is part of 76 FENCE Tampa, the locally owned 76 FENCE location run by Tom &amp; Kate Donnelly. We install and repair fencing across New Tampa, Tampa Palms, Hunter's Green, Temple Terrace, and the rest of North Tampa, with the training and manufacturer relationships of the national 76 FENCE network behind every job.",
                "Most North Tampa neighborhoods are planned communities with architectural review, and many homes back up to preserves, ponds, or golf courses. We help you pick a style your HOA will approve, prepare the paperwork, and build to the lot you actually have.",
            ],
            service_areas_meta="76 FENCE Tampa installs fences across New Tampa and North Tampa, including Tampa Palms, Hunter's Green, Cross Creek, K-Bar Ranch, Temple Terrace, and Carrollwood.",
            faq_lead="Answers to the questions we hear most from New Tampa and North Tampa homeowners.",
            address_placeholder="e.g. New Tampa, Tampa, FL",
            local_section=dict(
                eyebrow="Built for North Tampa",
                title="Fencing for New Tampa &amp; North Tampa Homes",
                intro="Planned communities, conservation lots, and pools are the norm here, and each one changes what the right fence looks like.",
                cards=[
                    ("HOA &amp; ARC Approval", "We help you choose a style, height, and color your association allows, and prepare the drawings and product sheets your architectural review committee asks for."),
                    ("Preserve &amp; Pond Lots", "Aluminum and other open styles keep the view on lots that back up to preserves, ponds, and golf courses, while still securing the yard."),
                    ("Pool Enclosures", "Pool barriers with self-closing, self-latching gates built to Florida's pool code, in aluminum, vinyl, or steel."),
                    ("Privacy Where You Need It", "Vinyl and wood privacy fencing for side yards and homes close to the street or the neighbors."),
                ],
            ),
            local_faqs=[
                ("Do I need HOA approval for a fence in New Tampa?",
                 "Almost always. Most New Tampa and North Tampa neighborhoods — including Tampa Palms, Hunter's Green, Cross Creek, and K-Bar Ranch — have architectural review. We'll help you pick an approvable design and prepare what your committee needs."),
                ("Do I need a permit for a fence in Tampa?",
                 "Fences inside Tampa city limits generally need a permit through the City of Tampa, while Temple Terrace and unincorporated Hillsborough County have their own processes. We confirm the rules for your address and handle the permit."),
                ("What fence works best for a home that backs up to a preserve or pond?",
                 "Aluminum is the most popular choice, because it secures the yard without blocking the view, and it's often what HOAs require on water and preserve lots. We'll also check for easements and setbacks before we lay out the line."),
            ],
            town_intros=[
                "Getting a fence in {town} usually starts with your HOA. {brand} helps {town} homeowners pick an approvable design, handles the paperwork and permit, and builds it right.",
                "{brand} installs privacy, pool, and decorative fencing across {town} and the rest of North Tampa, with free on-site estimates from the owners' own team.",
                "Whether your {town} home backs up to a preserve, a pond, or the neighbors, {brand} will recommend a fence that fits the lot, the HOA rules, and your budget.",
            ],
            town_why=[
                "{brand} is owner-operated by Tom &amp; Kate Donnelly and backed by the national {brand} network — a local team you can reach, with national buying power.",
                "Every {town} estimate is free, and every installation comes with the manufacturer's warranty plus our <a href=\"warranty.html\">76-Week Limited Workmanship Warranty</a>.",
                "We're fully insured, with general liability and workers' compensation coverage, and we confirm {town} permit and HOA requirements before install day.",
            ],
            town_permit=[
                "Fence permits around {town} depend on whether you're in the City of Tampa, Temple Terrace, or unincorporated Hillsborough County. We check your address and handle the permit either way.",
                "If you have a pool, your fence or gate may count as the required pool barrier under Florida code. We build {town} pool enclosures with self-closing, self-latching gates that meet it.",
            ],
        ),
    ),
}
