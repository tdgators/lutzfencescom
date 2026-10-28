# -*- coding: utf-8 -*-
"""P1 pages from PAGE_BACKLOG.md: pool fences, pool inspection guide, gates, driveway gates,
dog fences, fence replacement, storm/hurricane repair.

BASE holds the content every site shares (facts, process, FAQs). Each site's own tagline,
intro and local section live in content/new_local.py, keyed by the site's content module
name, so no two sites carry the same page text. Pool law facts are from Florida Statutes
ss. 515.27 and 515.29 (checked Oct 2026); never add code numbers here without a source.
"""

POOL_LAW = "https://www.flsenate.gov/Laws/Statutes/2025/515.29"
POOL_FEATURES = "https://www.flsenate.gov/Laws/Statutes/2025/515.27"

BASE = {
    "pool-fence": dict(
        name="Pool Fences", kicker="Fence Types", photo="pool-fence.webp",
        photo_alt="Black aluminum pool fence around a lit backyard pool at dusk",
        meta_title="Pool Fence Installation in {city}, FL | {brand}",
        meta="Pool fence installation in {city}, FL: aluminum, vinyl and other barriers built to Florida's pool barrier law, with self-closing, self-latching gates.",
        glance=["Built to Florida's pool barrier law", "At least 4' tall, measured outside", "Self-closing, self-latching gates that open outward",
                "Aluminum, vinyl and other materials", "Ready for your pool inspection"],
        sections=[
            ("What Florida law requires", [
                f'Florida\'s Residential Swimming Pool Safety Act sets the baseline. A pool barrier must be <strong>at least 4 feet high on the outside</strong>, with no gaps, openings or features a young child could crawl under, squeeze through or climb over. It has to surround the pool and sit far enough from the water\'s edge that a child who gets past it can\'t fall straight in (<a href="{POOL_LAW}" target="_blank" rel="noopener">Fla. Stat. 515.29</a>).',
                "Gates are where most barriers fail. Florida requires pool gates to open outward, away from the pool, and to be self-closing and self-latching, with the release on the pool side and out of a young child's reach. A house wall can be part of the barrier only if no door or window opens directly onto the pool.",
                f'For a new pool, a barrier is one of the approved safety features the pool needs to pass final inspection; the others are an approved safety cover, door and window exit alarms, self-closing door latches, or a certified pool alarm (<a href="{POOL_FEATURES}" target="_blank" rel="noopener">Fla. Stat. 515.27</a>). Your county or city inspector also applies the Florida Building Code\'s detailed barrier specs, so we build to those, not just the statute.',
            ]),
            ("Choosing a pool fence material", [
                "<strong>Aluminum</strong> is the most popular choice around Florida pools: it won't rust, it keeps the view open, and its vertical pickets are hard to climb. <strong>Vinyl</strong> works well when you want privacy around the pool deck, as long as the panel design leaves no footholds. <strong>Wood and composite</strong> can work too, built so horizontal rails sit on the pool side, not the outside where a child could use them as a ladder.",
                "Whatever the material, we plan the layout around the gate first: where people walk, where the pool equipment sits, and which way the gate swings so it always opens away from the water.",
            ]),
            ("Small details inspectors notice", [
                "Planters, AC units, pool pumps and patio furniture placed against the outside of the fence can count as climbing aids. Ground that washes out under the bottom rail after a summer storm can open a gap. A latch that sticks, or a gate that doesn't swing shut on its own, will fail. Our <a href=\"pool-fence-inspection-florida.html\">pool fence inspection guide</a> walks through what to check before the inspector arrives.",
            ]),
        ],
        faqs=[
            ("How tall does a pool fence need to be in Florida?", "Florida law requires a residential pool barrier to be at least 4 feet high on the outside. Your city, county or HOA can require more, so we confirm the local rule for your address before we build."),
            ("Can my existing yard fence be my pool barrier?", "Sometimes. Florida allows a yard enclosure to serve as the pool barrier if it surrounds the pool and meets every barrier requirement, including the gates. Many older fences need gate hardware or repairs before they qualify."),
            ("Which way does a pool gate have to swing?", "Outward, away from the pool. It also has to close and latch on its own, with the latch release on the pool side out of a young child's reach."),
            ("Do you handle the permit?", "In most cases, yes. We manage the permit and schedule around your pool inspection so the barrier is ready when the inspector arrives."),
        ],
        related=["pool-fence-inspection-florida", "aluminum-fence", "vinyl-fence", "fence-gates", "hoa-fence-approval-guide", "financing"],
    ),

    "pool-fence-inspection-florida": dict(
        name="Pool Fence Inspection Guide", kicker="Fence Guides", photo="pool-inspection.webp",
        photo_alt="Black aluminum fence along a calm pond at sunrise",
        meta_title="Florida Pool Fence Inspection: What the Inspector Checks | {brand}",
        meta="What a Florida pool barrier inspection looks at: height, gaps, self-closing gates, latch location, climbing aids and house doors. A checklist from {brand}.",
        glance=["Based on Florida Statutes 515.27 and 515.29", "A walk-through you can do yourself", "The gate is the most common failure",
                "Remove climbing aids before inspection day", "Local codes can add requirements"],
        sections=[
            ("Before you start", [
                f'This checklist follows Florida\'s pool barrier law (<a href="{POOL_LAW}" target="_blank" rel="noopener">s. 515.29</a>). Your inspector also applies the Florida Building Code and any local rules, which add exact measurements for openings and latch heights, so treat this as a pre-check, not a pass guarantee. When we build the barrier, we build to the code your inspector uses.',
            ]),
            ("1. Height, measured from the outside", [
                "The barrier must be at least 4 feet high measured on the outside, the side a child would approach from. Check low spots: a fence that's 48 inches on a level patio can come up short where the yard slopes or where mulch and soil have built up against it.",
            ]),
            ("2. No way under, through or over", [
                "Look for gaps under the bottom rail, especially where rain has washed soil away, and for openings a small child could squeeze through. Check that horizontal rails or decorative pieces don't give a foothold on the outside of the fence.",
            ]),
            ("3. The gate", [
                "Open the gate and let go. It should swing shut and latch on its own, every time, from any position. It must open outward, away from the pool, and the latch release needs to be on the pool side, out of a young child's reach. Sagging gates that drag or latches that don't catch are the most common reasons a barrier fails.",
            ]),
            ("4. Climbing aids", [
                "Walk the outside of the fence. Pool equipment, AC units, planters, benches, trash cans and play sets placed near the barrier can count as a way over it. Move anything portable before inspection day and plan permanent equipment so it isn't next to the fence.",
            ]),
            ("5. House doors and windows", [
                f'If a wall of your house is part of the barrier, no door or window can open directly onto the pool unless it has one of the approved safety features, such as an exit alarm or a self-closing, self-latching door device (<a href="{POOL_FEATURES}" target="_blank" rel="noopener">s. 515.27</a>). This is the item most homeowners don\'t expect.',
            ]),
            ("6. Distance from the water", [
                "The barrier has to sit far enough from the water's edge that a child or frail adult who gets past it can't fall straight into the pool. Fences built right at the coping can be a problem.",
            ]),
        ],
        faqs=[
            ("What is the most common reason a pool fence fails inspection?", "The gate. Gates that don't close and latch on their own, swing toward the pool, or have the latch release on the outside account for most failures we see."),
            ("Does a screen enclosure count as a pool barrier?", "It can, if it meets the same barrier requirements, including self-closing, self-latching doors. Your inspector decides based on the enclosure's construction and local code."),
            ("Can you fix a fence that failed inspection?", "Yes. Most failures come down to gate hardware, a gap under the fence, or a climbing aid, and we can usually correct them quickly so you can schedule your re-inspection."),
        ],
        related=["pool-fence", "fence-gates", "aluminum-fence", "fence-repair", "hoa-fence-approval-guide", "warranty"],
    ),

    "fence-gates": dict(
        name="Fence Gates", kicker="Fence Types", photo="fence-gates.webp",
        photo_alt="Bronze aluminum fence with an arched double gate in front of a craftsman bungalow",
        meta_title="Fence Gates: Walk, Double Drive & Slide Gates in {city}, FL | {brand}",
        meta="Walk gates, double drive gates and cantilever slide gates in {city}, FL, sized for mowers, trailers and boats, with hardware that doesn't sag.",
        glance=["Walk, single drive and double drive gates", "Cantilever slide gates for wide openings", "Sized for mowers, trailers and boats",
                "Steel-framed vinyl and wood gates that don't sag", "Self-closing and lockable hardware"],
        sections=[
            ("Pick the gate by what has to fit through it", [
                "A 4' walk gate handles people and push mowers. A 5' gate fits most riding mowers and wheelbarrows comfortably. If a trailer, boat, golf cart or truck needs backyard access, a double drive gate of 10' to 12' or wider is the usual answer, with two leaves that swing open from the center and a drop rod to hold the inactive side.",
            ]),
            ("Swing or slide", [
                "Swing gates need clear ground for the leaves to travel. On a slope, or where a driveway or landscaping is in the way, a cantilever slide gate is often the better fit. It rolls sideways on a track mounted to its posts, with no wheels on the ground, so grade changes and gravel don't matter. Slide gates need room alongside the opening for the gate to travel back, which we measure on site.",
            ]),
            ("Hardware that lasts", [
                "Most gate problems come from hardware, not the fence. We hang vinyl and wood gates on steel or aluminum gate frames that resist sagging, set gate posts deeper and in more concrete than line posts, and use stainless or coated hinges and latches that stand up to Florida humidity. For pools, gates are self-closing and self-latching and open away from the water.",
            ]),
        ],
        faqs=[
            ("How wide should a backyard gate be?", "4' for foot traffic, 5' for most riding mowers, and a 10' to 12' double drive gate for trailers, boats or vehicles. We measure your equipment before we build."),
            ("Why do gates sag, and can you fix mine?", "Sagging usually comes from an undersized or shallow gate post or a gate with no internal frame. We can reset posts, add frame kits or anti-sag hardware, or replace the gate."),
            ("Can a gate be automated later?", "Yes. If an opener might be added later, tell us up front so we set the right posts and leave room for the operator."),
        ],
        related=["driveway-gates", "pool-fence", "privacy-fence", "aluminum-fence", "fence-repair", "commercial-fencing"],
    ),

    "driveway-gates": dict(
        name="Driveway Gates", kicker="Fence Types", photo="driveway-gates.webp",
        photo_alt="Modern Florida home at dusk with a horizontal fence and driveway gate",
        meta_title="Driveway Gate Installation in {city}, FL | {brand}",
        meta="Swing and slide driveway gates in aluminum, steel, vinyl and wood for {city}, FL homes, installed manual or ready for an automatic gate opener.",
        glance=["Swing and cantilever slide gates", "Aluminum, steel, vinyl and wood", "Manual now, automation-ready later",
                "Posts set for the gate's full weight", "Gate openers available as an add-on"],
        sections=[
            ("Swing gates vs. slide gates", [
                "<strong>Swing gates</strong>, single or double, are the classic driveway look. They need a flat arc of driveway to open into, so they work best on level drives with space inside the gate. <strong>Cantilever slide gates</strong> roll sideways and need no swing room, which makes them the better choice for sloped driveways, short setbacks or openings wider than about 16 feet. They do need clear space along the fence for the gate to slide back.",
            ]),
            ("Materials", [
                "Aluminum is light, rust-free and pairs with most ornamental fences. Steel is stronger and heavier, for larger gates and more security. Vinyl and wood gates match privacy fences, built on internal metal frames so they stay square. We match the gate to your fence and your HOA's guidelines.",
            ]),
            ("Manual or automatic", [
                "Every driveway gate we build can be manual. If you want an automatic opener, it's quoted as a separate add-on: the operator, safety sensors and the power run. Automated gates must meet the UL 325 safety standard for gate operators, which affects the gate design itself, so let us know early if automation is in your plans.",
            ]),
        ],
        faqs=[
            ("How much room does a slide gate need?", "A cantilever slide gate needs clear, fairly level space beside the opening, usually longer than the opening itself, for the gate to travel back. We measure it on site."),
            ("Can you add an opener to my existing gate?", "Often, yes, if the gate and posts can handle it and the gate can be made compliant with the UL 325 safety standard. We'll inspect it first."),
            ("Do I need HOA approval for a driveway gate?", "In most communities, yes. Driveway gates are visible from the street, so most HOAs review them. We provide the drawings and specs your HOA asks for."),
        ],
        related=["fence-gates", "aluminum-fence", "steel-wrought-iron-fence", "commercial-fencing", "hoa-fence-approval-guide", "financing"],
    ),

    "dog-fence": dict(
        name="Dog & Pet Fences", kicker="Fence Types", photo="dog-fence.webp",
        photo_alt="Black aluminum puppy-picket fence along a green lawn",
        meta_title="Dog Fence Installation in {city}, FL | {brand}",
        meta="Dog and pet fences in {city}, FL: the right height for your breed, puppy-picket bottoms, dig guards and latches pets can't open.",
        glance=["Height matched to your dog", "Puppy-picket bottoms for small pets", "Dig guards along the fence line",
                "Latches dogs can't nudge open", "Privacy panels for reactive dogs"],
        sections=[
            ("Height: match the fence to the dog", [
                "Most small and medium dogs are fine behind a 4' fence. Big, athletic or anxious dogs that jump or climb usually need 5' to 6', and climbers do better with a solid privacy fence that gives them nothing to grip. Tell us about your dog, not just its size: a determined 30-pound terrier can get out of fences a lab ignores.",
            ]),
            ("Gaps, digging and gates", [
                "Small dogs and puppies slip through standard picket spacing, so for aluminum we use puppy-picket panels with extra pickets along the bottom. Diggers need a dig guard: wire mesh buried along the fence line or a concrete mow strip. And gates are where most escapes happen, so we hang them to close on their own and use latches a nose or paw can't open.",
            ]),
            ("Picking the material", [
                "Aluminum keeps the yard open and is easy to see through, which suits calm dogs. Privacy vinyl or wood blocks the view of passing dogs and people, which helps dogs that bark at everything. Chain link is the budget option and works well for large yards. In Florida heat, think about shade and airflow too: a semi-privacy style lets the breeze through.",
            ]),
        ],
        faqs=[
            ("How tall should a dog fence be?", "4' for most small and medium dogs, 5' to 6' for large dogs, jumpers and climbers. A solid privacy fence is best for climbers."),
            ("What is a puppy-picket fence?", "An aluminum fence with extra pickets along the bottom so small dogs, puppies and cats can't slip through."),
            ("How do I stop my dog from digging under the fence?", "A dig guard: galvanized wire buried along the bottom of the fence, or a concrete mow strip. We can add either during installation."),
        ],
        related=["aluminum-fence", "privacy-fence", "vinyl-fence", "chain-link-fence", "fence-gates", "semi-privacy-fence"],
    ),

    "fence-replacement": dict(
        name="Fence Replacement", kicker="Services", photo="fence-replacement.webp",
        photo_alt="Long new cedar shadowbox privacy fence along a backyard lawn",
        meta_title="Fence Replacement in {city}, FL | {brand}",
        meta="Old fence leaning, rotting or storm-damaged? {brand} removes it and installs a new fence in {city}, FL, with the permit and HOA paperwork handled.",
        glance=["Old fence removal and haul-away available", "Back-to-back removal and install", "Permit and HOA paperwork handled",
                "Upgrade the material or keep the look", "Workmanship warranty on the new fence"],
        sections=[
            ("Repair or replace?", [
                "If a few boards, a gate or one or two posts are the problem, a <a href=\"fence-repair.html\">repair</a> usually makes sense. When posts are rotting at ground level across the fence, panels are leaning in several places, or the fence is near the end of its life, replacement is the better value. Patching an old fence over and over usually costs more in the end.",
            ]),
            ("How a replacement works", [
                "We start with a free estimate and confirm your property lines, then handle the HOA application and permit where they're needed. On install day, the old fence comes down and the new one goes up, usually back to back so your yard isn't open for long. If you have a pool or pets, tell us and we'll plan the swap to keep the yard secure. Removal and haul-away of the old fence can be included in your quote.",
            ]),
            ("A chance to upgrade", [
                "A replacement is the easiest time to change materials. Many homeowners move from wood to vinyl or aluminum to get out of the stain-and-repair cycle, or go taller for privacy where the code and HOA allow it. If you like the look you have, we can match it with longer-lasting materials.",
            ]),
        ],
        faqs=[
            ("Can you reuse my old fence posts?", "Usually not. Old posts are often the weakest part of the fence, and setting new posts is what makes the new fence last."),
            ("Do I need a permit to replace a fence?", "It depends on where you live and what you're building. We check the rules for your address and handle the permit when one is needed."),
            ("How long does a fence replacement take?", "Most residential replacements take one to two days on site, once the permit and any HOA approval are in hand."),
        ],
        related=["fence-repair", "vinyl-fence", "wood-fence", "aluminum-fence", "hoa-fence-approval-guide", "warranty"],
    ),

    "hurricane-fence-repair": dict(
        name="Storm & Hurricane Fence Repair", kicker="Services", photo="hurricane-fence-repair.webp",
        photo_alt="White vinyl privacy fence with lattice top along a Florida side yard",
        meta_title="Storm & Hurricane Fence Repair in {city}, FL | {brand}",
        meta="Fence damaged in a storm or hurricane? What to do first, how to document it for insurance, and when to repair or replace. {brand} serves {city}, FL.",
        glance=["Safety first: check for downed lines", "Photograph everything before cleanup", "Secure pool barriers right away",
                "Repair or replace, honestly assessed", "Upgrades that ride out the next storm"],
        sections=[
            ("Right after the storm", [
                "Stay clear of downed power lines. A fence touching a line can be energized, so call the utility and keep everyone away. Then photograph the damage from several angles before anything is moved or cleaned up; your insurance company will want to see it as it was. Keep receipts for any emergency work.",
                "If the fence is your pool barrier, securing it is the priority. Close off gaps with temporary fencing or keep the pool area off limits until the barrier is repaired.",
            ]),
            ("Repair or replace?", [
                "After a storm, look at the posts first. Snapped panels or a few loose boards on a fence with solid posts can usually be repaired. Posts that are leaning, cracked or lifted out of the ground across a long stretch usually mean replacement, especially on an older fence. We'll tell you which one makes sense and put it in writing, which also helps with an insurance claim.",
            ]),
            ("Building back stronger", [
                "Most storm failures we see start at the posts: too shallow, too little concrete, or rotted below grade. When we repair or replace, we set posts to the depth and footing the fence needs. Aluminum and other open designs let wind pass through. For privacy fences, a sturdier panel system and stronger posts matter more than the material alone.",
            ]),
        ],
        faqs=[
            ("Does homeowners insurance cover fence damage?", "It depends on your policy and what caused the damage. Many policies cover wind damage to fences, often subject to your hurricane deductible. Photograph the damage and check with your agent; we can provide a written estimate for your claim."),
            ("How fast can you repair a storm-damaged fence?", "After major storms, demand spikes across the area. Call early, and tell us if the fence is a pool barrier or keeps pets or children contained so we can prioritize it."),
            ("Can a fence be built to resist hurricanes?", "No fence is storm-proof, but deeper posts, more concrete, quality panel systems and open designs that let wind through hold up far better."),
        ],
        related=["fence-repair", "fence-replacement", "pool-fence", "aluminum-fence", "vinyl-fence", "warranty"],
    ),
}

# Labels for related links to existing pages, by slug.
RELATED_LABELS = {
    "aluminum-fence": ("Aluminum Fences", "Rust-free, open-view fencing for pools, pets and front yards."),
    "vinyl-fence": ("Vinyl Fences", "Low-maintenance privacy and picket fencing."),
    "wood-fence": ("Wood Fences", "Classic privacy with cedar and pressure-treated pine."),
    "chain-link-fence": ("Chain Link Fences", "Durable, budget-friendly fencing for large yards."),
    "steel-wrought-iron-fence": ("Steel & Wrought Iron Fences", "Strength and security with an ornamental look."),
    "privacy-fence": ("Privacy Fences", "Full privacy in vinyl, wood and composite."),
    "semi-privacy-fence": ("Semi-Privacy Fences", "Privacy that still lets the breeze through."),
    "fence-repair": ("Fence Repair", "Leaning posts, broken boards and sagging gates fixed."),
    "commercial-fencing": ("Commercial Fencing", "Security, access control and gates for businesses."),
    "hoa-fence-approval-guide": ("HOA Approval Guide", "What to submit so your fence gets approved."),
    "financing": ("Financing", "Pay over time with Wisetack financing."),
    "warranty": ("Our Warranty", "Our 76-week workmanship warranty."),
}
