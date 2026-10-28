# -*- coding: utf-8 -*-
"""Per-site rewrites of the shared P1 page body (new_pages.BASE): each site's own glance list,
main sections and FAQs, so the network doesn't repeat itself. Lutz uses BASE as-is.
Facts must stay consistent with BASE (pool law: Fla. Stat. 515.27 / 515.29)."""
from new_pages import POOL_LAW, POOL_FEATURES

LAW = f'<a href="{POOL_LAW}" target="_blank" rel="noopener">Fla. Stat. 515.29</a>'
FEAT = f'<a href="{POOL_FEATURES}" target="_blank" rel="noopener">Fla. Stat. 515.27</a>'
GUIDE = '<a href="pool-fence-inspection-florida.html">pool inspection guide</a>'

VARIANTS = {
    # ================================================================== Brooksville
    "brooksville": {
        "pool-fence": dict(
            glance=["Meets Florida's 4' pool barrier minimum", "Gates swing out, close and latch themselves", "Separate pool enclosures for acreage", "Aluminum, vinyl or wood", "Built for Hernando County inspections"],
            sections=[
                ("The rules every pool barrier follows", [f"State law sets the floor for every pool fence in Hernando County. The barrier has to stand at least 4 feet tall on the outside, wrap the whole pool, and leave nothing a small child could slip under, squeeze through or use to climb over. It also needs some distance from the water so anyone who does get past it can't tumble right in ({LAW}).",
                                                          "The gate gets the strictest treatment: it must swing outward, away from the pool, close by itself and latch by itself, with the release on the pool side where a young child can't reach it. If a wall of the house forms part of the barrier, it can't have doors or windows opening straight onto the pool."]),
                ("Materials that hold up out here", ["Aluminum shrugs off sun and rain and keeps the view across the property. Vinyl gives a private pool deck. Wood suits a rustic home, as long as the framing faces the pool so the outside stays smooth and unclimbable. Whatever you pick, we lay out the gate first, based on the path you actually walk from the house."]),
            ],
            faqs=[("Does my pasture fence count as a pool barrier?", "Almost never. Farm and ranch fencing has openings and rails a child can climb, so the pool needs its own barrier that meets the state rules."),
                  ("How tall must a pool fence be in Hernando County?", "At least 4 feet on the outside under Florida law. We confirm any local or HOA requirements for your address."),
                  ("What else can make a pool pass inspection?", f"Florida accepts a barrier, an approved safety cover, door and window exit alarms, self-closing door latches or a certified pool alarm ({FEAT}). A fence is the most common choice.")]),
        "pool-fence-inspection-florida": dict(
            glance=["Measure height on the low side of the yard", "Close the gate from every angle", "Check under the fence after rain", "Move anything a child could climb", "Check house doors facing the pool"],
            sections=[
                ("Walk the barrier like an inspector", [f"Everything below comes from Florida's pool barrier statute ({LAW}). Your inspector also uses the Florida Building Code, which spells out exact openings and latch heights, so use this as a pre-check rather than a guarantee."]),
                ("Height and gaps", ["The barrier has to be at least 4 feet tall measured from the outside. On rolling Brooksville lots, measure at the lowest point, not the highest. Then look along the bottom for washouts and along the face for footholds or openings a small child could use."]),
                ("The gate", ["Open it a few inches and let go, then open it all the way and let go. Both times it should swing shut and latch on its own. It must open outward, away from the pool, and the latch release has to be on the pool side out of a child's reach."]),
                ("Climbing aids, doors and distance", [f"Clear the outside of the fence: no pumps, feeders, wheelbarrows or furniture a child could climb. If the house wall is part of the barrier, doors or windows opening onto the pool need an approved safety feature such as an exit alarm ({FEAT}). And the barrier must sit far enough from the water that someone who gets past it can't fall straight in."]),
            ],
            faqs=[("What fails most often?", "The gate. Gates that don't close and latch themselves every time, or that swing toward the pool, are the top reason for a failed inspection."),
                  ("My screen enclosure door won't close on its own. Is that a problem?", "Yes, if the enclosure is your barrier. A new door closer usually fixes it."),
                  ("Can you fix things the inspector flagged?", "Yes. Gate hardware, gaps and height problems are usually quick fixes before your re-inspection.")]),
        "fence-gates": dict(
            glance=["Walk gates for people and mowers", "Wide farm and drive gates", "Slide gates for slopes", "Heavy posts that stop sagging", "Latches built for daily use"],
            sections=[
                ("Size it for the biggest thing that passes through", ["A 4' gate is for people. Go 5' for a riding mower. For trucks, trailers, tractors or a horse trailer, plan on a double gate of 12' or more, and on rural land 14' to 16' is common so you're not threading the needle every time."]),
                ("Swing, slide or ride on a wheel", ["Swing gates need level ground to open across. Where the ground rises, floods or turns to sand, a cantilever slide gate runs on its own track with nothing touching the ground, and a long farm gate can carry a wheel to take weight off the hinge post."]),
                ("Why gates sag, and how we stop it", ["Long gates pull on their hinge post every day. We set gate posts deeper and with more concrete than line posts, use frames that stay square and pick hinges and latches rated for the gate's weight."]),
            ],
            faqs=[("How wide should a farm gate be?", "For tractors and trailers, 12' at minimum; 14' to 16' is easier for long equipment."),
                  ("My gate drags on the ground. Can it be fixed?", "Usually. Resetting or upsizing the post, adding a brace or a gate wheel often solves it."),
                  ("Can you add a gate to an existing fence?", "Yes, in most materials, including wire and board fences.")]),
        "driveway-gates": dict(
            glance=["Entrance gates for long drives", "Aluminum, steel, wood or vinyl", "Built ready for an opener", "Set back for safe pull-offs", "Openers quoted as an add-on"],
            sections=[
                ("Swinging or sliding entrance gates", ["Swing gates look classic on a country entrance and suit a level approach. Slide gates roll sideways on a track mounted to the posts, so they handle slopes and very wide openings, as long as there's room along the fence for the gate to travel."]),
                ("Choosing the material", ["Steel is the heavy-duty choice for big entrances and security. Aluminum won't rust and is light enough for long spans. Wood and vinyl suit ranch and farmhouse styles, built on metal frames so they stay straight."]),
                ("Opening it from the truck", ["Gates are built manual, with an automatic opener quoted separately: the operator, safety sensors and the power run. Automated gates have to meet the UL 325 safety standard, which shapes how the gate is built, so mention it early if you might automate."]),
            ],
            faqs=[("How far back should an entrance gate sit?", "Far enough that your longest vehicle can pull completely off the road while the gate opens."),
                  ("Can a gate be solar-powered?", "Often, yes, for gates far from the house. We'll look at sun exposure and how often the gate is used."),
                  ("Will my gate need a permit?", "It depends on the location and design. We check the rules for your property.")]),
        "dog-fence": dict(
            glance=["Height for your breed", "Woven or welded wire for big areas", "Dig guards for diggers", "Self-latching gates", "Puppy-picket for small dogs"],
            sections=[
                ("How high is high enough", ["Most small and mid-size dogs stay behind 4 feet. Hounds, shepherds and other athletic breeds often need 5 to 6 feet, and dogs that climb do best behind a solid fence with no rails to grab."]),
                ("Keeping them from going under or through", ["Wire mesh on a ranch fence stops dogs from slipping between rails across big areas. For small dogs near the house, aluminum puppy-picket closes up the gaps at the bottom. Diggers need a buried wire dig guard or a concrete strip along the bottom."]),
                ("Gates are where dogs get out", ["A gate left open is the number one escape. Self-closing hinges and latches a dog can't nose open close that gap."]),
            ],
            faqs=[("Can you fence a large area for dogs?", "Yes. Woven or welded wire on wood or steel posts is cost-effective over several acres."),
                  ("Will a 4' fence hold a lab?", "Usually, unless your lab is a jumper. Tell us how your dog behaves and we'll size it."),
                  ("How do you stop digging?", "Buried galvanized wire along the fence line, or a concrete mow strip.")]),
        "fence-replacement": dict(
            glance=["Removal and haul-away available", "New posts set deep and solid", "Permit handled when required", "Wood, vinyl, aluminum or wire", "Workmanship warranty"],
            sections=[
                ("Time to repair or time to replace", ["A few broken boards or one bad post is a repair. When posts are soft at the ground across the fence, sections lean, or the wire is rusting through, replacing it costs less over time than patching."]),
                ("What replacement day looks like", ["We confirm your lines, take down the old fence and put the new one up, usually back to back. If animals or a pool need to stay secured, we plan the work in sections. Removal and haul-away can be included in your quote."]),
                ("Choosing what goes back up", ["Some owners keep the same look with better materials; others switch from wood to vinyl or aluminum to stop maintaining it. On rural lines, upgrading posts often matters more than the fence material."]),
            ],
            faqs=[("Can you replace just part of a fence?", "Yes. We can replace the worst runs and match or transition to the rest."),
                  ("Do old posts get reused?", "Rarely. New, properly set posts are what make the new fence last."),
                  ("How long does it take?", "Most residential jobs take one to two days; long rural runs take longer.")]),
        "hurricane-fence-repair": dict(
            glance=["Stay clear of downed lines", "Photos before cleanup", "Secure animals and pools first", "Written estimates for claims", "Stronger posts on rebuild"],
            sections=[
                ("The first few hours", ["Keep away from any fence touching a power line and call the utility. Before moving debris, take photos of every damaged section from several angles for your insurer. If animals or a pool depend on the fence, put up temporary fencing or keep them clear until it's repaired."]),
                ("Fix it or replace it", ["Check the posts. Broken boards or wire on solid posts usually mean repair. Leaning or snapped posts along a long run, especially on an older fence, usually mean replacement. We'll give you our honest call in writing."]),
                ("Rebuilding for the next storm", ["Most fences that fail in a storm fail at the posts. When we rebuild, we set posts deeper with more concrete, and we suggest open designs where privacy isn't needed so the wind passes through."]),
            ],
            faqs=[("Will insurance pay for my fence?", "That depends on your policy and deductible. Many policies cover wind damage; we provide written estimates for claims."),
                  ("What should I do first?", "Stay safe, photograph everything and secure animals and pools."),
                  ("Can you fix wire fencing too?", "Yes, including field fence and woven wire on rural properties.")]),
    },

    # ================================================================== North Tampa
    "northtampa": {
        "pool-fence": dict(
            glance=["Florida-compliant pool barriers", "HOA-matched styles and colors", "Outward-swinging, self-latching gates", "Views to the pond kept open", "Inspection-ready"],
            sections=[
                ("Florida's pool barrier requirements", [f"For any home pool, Florida requires a barrier at least 4 feet tall measured from outside, with no openings or footholds a young child could use to get under, through or over it. The barrier has to surround the pool and stand back far enough from the water that a child who gets past it can't fall directly in ({LAW}).",
                                                         "Pool gates must open away from the pool and both close and latch on their own, with the release out of a young child's reach on the pool side. Where the house itself forms part of the barrier, no door or window can open directly onto the pool unless it has an approved safety device."]),
                ("Aluminum, vinyl or something else", ["Aluminum is the go-to around New Tampa pools because the pickets are hard to climb and the view stays open. Vinyl creates a private pool area if the design has no footholds. We build to your HOA's approved style and confirm the details meet the barrier rules."]),
                ("Getting ready for the inspector", [f"Inspectors look closely at the gate, the gaps along the bottom and anything placed against the outside of the fence. Our {GUIDE} covers the walk-through."]),
            ],
            faqs=[("Will my HOA allow a pool fence?", "Most do, within approved styles and colors. We prepare the application drawing for you."),
                  ("Is a screened lanai enough?", "It can be, if it meets the barrier rules, including self-closing, self-latching doors. Many older lanai doors need new hardware."),
                  ("How tall does it have to be?", "At least 4 feet measured from outside under state law; your HOA may require a specific height.")]),
        "pool-fence-inspection-florida": dict(
            glance=["Built from Florida's pool statutes", "Gate checks come first", "Look at lanai doors", "Keep the outside of the fence clear", "Local code may add details"],
            sections=[
                ("How to use this checklist", [f"These items follow Florida's barrier law ({LAW}). Inspectors also apply the Florida Building Code's measurements, so this is a pre-check, not a promise."]),
                ("Gate and latch", ["Release the gate from half open and from wide open; it should close and latch every time. It must swing away from the pool, and the latch release belongs on the pool side, beyond a young child's reach."]),
                ("Height, gaps and footholds", ["Measure the barrier from outside: it needs to be at least 4 feet. Look for gaps under the bottom rail and anything on the outside face a child could step on."]),
                ("Doors, climbing aids and setback", [f"Doors or windows opening straight onto the pool from the house need an approved safety feature, such as an exit alarm or self-closing latch ({FEAT}). Move pool equipment, planters and furniture away from the outside of the fence, and make sure the barrier isn't right at the water's edge."]),
            ],
            faqs=[("What do inspectors flag most?", "Gates that don't self-close and self-latch reliably."),
                  ("Do lanai sliders need alarms?", "If they open directly onto the pool and the house is part of the barrier, they need one of the approved safety features."),
                  ("Can you get my barrier ready before inspection?", "Yes. We check the barrier and fix gates, gaps and hardware.")]),
        "fence-gates": dict(
            glance=["Gates matched to your fence", "Walk, double and slide gates", "Framed so they don't sag", "Self-closing pool gates", "HOA drawings included"],
            sections=[
                ("Choosing the right width", ["A 4' gate covers foot traffic and trash bins. A 5' gate gets a riding mower through. Boats, trailers and golf carts call for a 10' to 12' double gate with a drop rod on the fixed side."]),
                ("When a slide gate makes sense", ["If the gate would swing across a slope, a planting bed or a driveway, a cantilever slide gate glides sideways on its own track instead. It just needs clear space along the fence to travel back."]),
                ("Built to stay square", ["We build vinyl and wood gates on metal frames, set gate posts deeper and in more concrete, and use corrosion-resistant hinges and latches. Pool gates are self-closing, self-latching and swing away from the water."]),
            ],
            faqs=[("Will my HOA need to approve a new gate?", "Often, yes, especially if it changes the fence line or faces the street. We include gate details in your application."),
                  ("Can you match my existing fence?", "In most cases we can match the style and color."),
                  ("Why does my vinyl gate sag?", "Usually no internal frame or a weak gate post. A frame kit or a new post typically fixes it.")]),
        "driveway-gates": dict(
            glance=["Swing and slide driveway gates", "Designed for HOA review", "Aluminum, steel, vinyl and wood", "Opener-ready construction", "Operators quoted separately"],
            sections=[
                ("Swing vs. slide", ["Swing gates need a level arc of driveway to open into. Slide gates move sideways, so they work on sloped drives, short setbacks and wide openings, provided there's space along the fence."]),
                ("Matching your home", ["Ornamental aluminum and steel suit most New Tampa architecture; vinyl and wood gates can match a privacy fence. We design to your community's guidelines and prepare the drawings for review."]),
                ("Automation as an add-on", ["Manual gates come standard; an automatic opener is a separate line with the operator, sensors and power. Automated gates must meet the UL 325 safety standard, so we plan for it from the start if it's on your list."]),
            ],
            faqs=[("Do driveway gates need HOA approval?", "Usually. They're visible from the street, so most HOAs review them."),
                  ("Can I add an opener later?", "Yes, if we build the gate and posts for it. Tell us up front."),
                  ("What's best for a sloped driveway?", "A cantilever slide gate, which doesn't need to swing across the slope.")]),
        "dog-fence": dict(
            glance=["Sized for your dog", "Puppy-picket aluminum", "Keeps dogs out of ponds", "Privacy for barkers", "HOA-approved styles"],
            sections=[
                ("Pick the height for the dog", ["Four feet keeps most small and medium dogs in. Large dogs and jumpers need 5 to 6 feet, and a climber needs a solid surface with nothing to grab."]),
                ("Close the gaps", ["Standard aluminum picket spacing can let a small dog through, so puppy-picket panels add extra pickets at the bottom. If your dog digs, we add a buried wire dig guard."]),
                ("Choosing the look", ["Aluminum keeps the pond view; vinyl privacy blocks distractions for dogs who bark at passersby; semi-privacy styles let air move in the summer heat. We build within your HOA's approved options."]),
            ],
            faqs=[("Can a dog fence go along a pond?", "Yes, within your property and community rules. A continuous aluminum fence keeps dogs away from the water."),
                  ("What's a dig guard?", "Galvanized wire buried along the bottom of the fence to stop digging."),
                  ("Which fence is best for a barking dog?", "A solid privacy fence that blocks the view of the street or walking path.")]),
        "fence-replacement": dict(
            glance=["Matches current HOA standards", "Old fence removed and hauled", "Permit handled", "Back-to-back install", "76-week workmanship warranty"],
            sections=[
                ("Replace or keep repairing?", ["When a few pieces fail, we repair. When posts are rotting at grade, panels are faded and cracking all along the fence, or it leans in several places, replacement is the better investment."]),
                ("Our replacement process", ["Free estimate, property lines confirmed, HOA application and permit handled, then the old fence comes out and the new fence goes in, usually in the same visit. Removal and haul-away can be included."]),
                ("Upgrading on the way", ["Replacement is the time to switch to vinyl or aluminum, adjust the fence line if the HOA allows, or add a wider gate."]),
            ],
            faqs=[("Will my HOA let me replace with a different material?", "Often, if it's on the approved list. We check current guidelines first."),
                  ("Can you reuse my posts?", "Usually not; new posts are what make the new fence last."),
                  ("How long will my yard be open?", "Usually just the hours between removal and install.")]),
        "hurricane-fence-repair": dict(
            glance=["Avoid downed power lines", "Document before you clean up", "Pool barriers secured first", "Repair vs. replace in writing", "Rebuilt for wind exposure"],
            sections=[
                ("After the wind dies down", ["Stay clear of fences touching power lines. Photograph damage before anything is moved, and save receipts for emergency fixes. If the fence is your pool barrier, block the opening or keep the pool area off limits until it's repaired."]),
                ("Should it be repaired or replaced?", ["Panels down on solid posts: repair. Posts leaning or broken across long runs, or an older fence: replace. We'll put our assessment in writing to support your claim."]),
                ("Rebuilding stronger", ["Posts are where storm failures start. We set them deeper with more concrete on exposed runs, and open designs like aluminum let wind pass through."]),
            ],
            faqs=[("Does insurance cover fences?", "Many policies cover wind damage, subject to your deductible. Check with your agent; we'll provide an estimate."),
                  ("Do storm repairs need HOA approval?", "Matching repairs often don't, but replacements usually do. We help with the paperwork."),
                  ("How soon can you come out?", "Demand spikes after storms. Call early and tell us if it's a pool barrier.")]),
    },

    # ================================================================== Carrollwood
    "carrollwood": {
        "pool-fence": dict(
            glance=["Brings older pool areas up to code", "4' minimum, measured outside", "Self-closing, self-latching gates", "Aluminum or vinyl", "Works around mature trees"],
            sections=[
                ("What a Florida pool barrier must do", [f"Under Florida law, a pool barrier must be at least 4 feet tall on the outside, surround the pool and have no gaps or features a young child could use to get under, through or over it. It also has to be set back from the water so someone who gets past it can't fall right in ({LAW}).",
                                                          "Gates must swing outward, away from the pool, and close and latch by themselves, with the latch release on the pool side beyond a young child's reach."]),
                ("Choosing a material", ["Aluminum is the most common pool fence here: it doesn't rust, stays open to the yard and is hard to climb. Vinyl gives the pool deck privacy if the design has no footholds outside. Wood works when its framing faces the pool."]),
                ("Before the inspection", [f"Roots lifting the fence, planters against the outside and gates that no longer close on their own are the usual problems in older yards. See our {GUIDE}."]),
            ],
            faqs=[("My pool fence is old. Does it need to be replaced?", "Not always. New gate hardware or a few new sections can bring it up to standard. We'll check it."),
                  ("Which way should my pool gate open?", "Outward, away from the pool, closing and latching on its own."),
                  ("Do I need a fence if I have a pool cover?", f"For a new pool, Florida accepts several safety options, including approved covers and alarms ({FEAT}). Many families still choose a fence.")]),
        "pool-fence-inspection-florida": dict(
            glance=["Check the gate first", "Look under the fence near tree roots", "Measure height outside", "Clear climbing aids", "Doors onto the pool need protection"],
            sections=[
                ("A quick pre-check", [f"This follows Florida's pool barrier law ({LAW}); your inspector adds the Florida Building Code's specifics."]),
                ("Gate", ["The gate must swing away from the pool and close and latch on its own every time. The latch release has to be on the pool side, out of a young child's reach."]),
                ("Height, gaps and roots", ["Measure the barrier from the outside: 4 feet minimum. Under Carrollwood's oaks, roots can heave fence sections and open gaps at the bottom, so check the whole run."]),
                ("Doors, climbing aids and setback", [f"House doors and windows opening onto the pool need an approved safety feature, such as an exit alarm ({FEAT}). Clear furniture and equipment away from the outside of the fence, and make sure the barrier isn't right at the water's edge."]),
            ],
            faqs=[("Why did my old fence fail inspection?", "Usually the gate hardware, a gap underneath or a climbable feature on the outside."),
                  ("Can tree roots cause a failure?", "Yes, if they lift the fence and open a gap. We can reset or replace those sections."),
                  ("How fast can you fix it?", "Most fixes are quick, so you can schedule your re-inspection.")]),
        "fence-gates": dict(
            glance=["Narrow side-yard gates", "Double drive gates", "Gate-only replacements", "Frames that prevent sagging", "Durable hinges and latches"],
            sections=[
                ("Sizing for your yard", ["Narrow side yards often fit only a 3' or 4' walk gate. If you need a mower through, aim for 5'. For a boat or trailer, a 10' to 12' double gate is standard."]),
                ("Swing or slide", ["Swing gates need clear, level ground. Where roots, beds or slopes get in the way, a cantilever slide gate runs on its own track, provided there's room alongside."]),
                ("Making it last", ["Old gates fail at the hinge post. We set gate posts deeper with more concrete, frame vinyl and wood gates with metal and use hardware that resists humidity."]),
            ],
            faqs=[("Can you replace just my gate?", "Yes. If the fence is sound, a new gate and post is often all you need."),
                  ("Can a new gate match my old fence?", "Usually, or we can build one in a longer-lasting material."),
                  ("How wide should my side gate be?", "At least 4' for bins and foot traffic; 5' if a mower goes through.")]),
        "driveway-gates": dict(
            glance=["Swing or slide designs", "Works around trees and beds", "Aluminum, steel, vinyl or wood", "Ready for automation", "Openers quoted separately"],
            sections=[
                ("Which style fits", ["A swing gate needs open, level driveway to swing across. A slide gate rolls sideways and needs space along the fence instead, which often suits Carrollwood's tree-lined drives better."]),
                ("Materials", ["Aluminum and steel for ornamental styles; vinyl or wood to match a privacy fence, built on metal frames to stay square."]),
                ("Automation", ["Manual is standard. Automatic openers are an add-on including the operator, sensors and power. Automated gates must meet the UL 325 safety standard, which shapes the gate design."]),
            ],
            faqs=[("Will a gate hurt my oak's roots?", "We place posts to avoid major roots and can use a slide gate to reduce digging."),
                  ("Can I automate later?", "Yes, if the gate is built for it from the start."),
                  ("Do I need approval?", "If you're in an HOA or deed-restricted area, likely yes. We provide drawings.")]),
        "dog-fence": dict(
            glance=["Right height for your dog", "Fixes gaps under old fences", "Dig guards", "Self-latching gates", "Puppy-picket aluminum"],
            sections=[
                ("Height", ["4' works for most small to medium dogs; jumpers and large dogs need 5' to 6'. Climbers do best behind solid privacy panels."]),
                ("Gaps and digging", ["Older fences often have gaps at the bottom from settling or roots. We close those, add puppy-picket panels for small dogs and bury wire along the line for diggers."]),
                ("Gates and materials", ["Self-closing gates with dog-proof latches stop the most common escapes. Aluminum keeps the yard open; vinyl privacy calms dogs that bark at the street."]),
            ],
            faqs=[("Can you dog-proof my existing fence?", "Often, by fixing gaps, replacing weak sections and upgrading gate hardware."),
                  ("What's best for small dogs?", "Aluminum puppy-picket or a privacy fence with no gaps."),
                  ("Can a fence keep other animals out too?", "A solid or puppy-picket fence with a dig guard keeps out most neighborhood dogs and digging wildlife.")]),
        "fence-replacement": dict(
            glance=["Most of our Carrollwood work", "Old fence removal", "Works around big roots", "Vinyl and aluminum upgrades", "Workmanship warranty"],
            sections=[
                ("Is it time?", ["Rotting posts at the ground line, leaning runs and boards that won't hold nails mean it's time. A few bad boards can still be repaired."]),
                ("How we do it", ["We confirm lines, handle any required permit and paperwork, remove the old fence and install the new one, usually back to back. Removal and haul-away can be included in your quote."]),
                ("Upgrades worth considering", ["Vinyl doesn't rot under shade and leaf litter, and aluminum keeps an open look. We can also widen a gate while we're at it."]),
            ],
            faqs=[("Will you damage my trees?", "We route posts around major roots and avoid cutting them where possible."),
                  ("Can you match my neighbor's fence?", "Often, yes, in style and color."),
                  ("How long does it take?", "Usually one to two days on site.")]),
        "hurricane-fence-repair": dict(
            glance=["Watch for downed lines", "Photograph before cleanup", "Targeted repairs for limb damage", "Pool barriers first", "Written estimates"],
            sections=[
                ("Right away", ["Stay away from fences touching power lines. Photograph all damage before cleanup and secure pool barriers with temporary fencing if needed."]),
                ("Repair or replace", ["Limb damage usually affects a section or two, which we can repair. If posts are failing throughout an older fence, replacement is the better value."]),
                ("Stronger next time", ["Deeper posts with more concrete and quality panels hold up better. Trimming limbs over the fence line helps too."]),
            ],
            faqs=[("Does insurance cover tree damage to my fence?", "Often, depending on your policy. Photograph everything and talk to your agent."),
                  ("Can you match my existing fence for repairs?", "Usually, yes."),
                  ("How quickly can you come out?", "Demand spikes after storms, so call early and tell us if the fence is a pool barrier.")]),
    },

    # ================================================================== Westchase
    "westchase": {
        "pool-fence": dict(
            glance=["Designed for HOA approval", "Florida pool barrier compliant", "Self-closing, self-latching gates", "Modern aluminum styles", "Inspection-ready"],
            sections=[
                ("Florida's barrier rules", [f"Every pool barrier in Florida must be at least 4 feet high from outside, enclose the pool and offer no way for a young child to get under, through or over. It must sit back from the water so anyone who gets past it can't fall directly in ({LAW}). Gates swing outward, close and latch on their own, and keep the release on the pool side, out of reach."]),
                ("Design that passes review", ["Most Westchase-area pool fences are black aluminum in the community's approved style. We prepare the drawing for your architectural review and build the approved design with compliant gates and latches."]),
                ("Inspection details", [f"Decorative rails on the wrong side, gaps along the bottom and furniture against the fence are common problems. Our {GUIDE} has the full checklist."]),
            ],
            faqs=[("Will an HOA-approved fence pass inspection?", "Not automatically. The details, like gates, latches and rails, have to meet the barrier rules too."),
                  ("How long does approval take?", "It varies by community. We submit a complete package to avoid delays."),
                  ("Can the house wall be part of the barrier?", "Yes, if no door or window opens directly onto the pool without an approved safety feature.")]),
        "pool-fence-inspection-florida": dict(
            glance=["Based on Florida's pool statutes", "Gate swing and latch", "No climbable outside rails", "Clear the fence line", "Check doors to the pool"],
            sections=[
                ("Using this list", [f"This checklist mirrors Florida's barrier law ({LAW}). Your inspector also checks Florida Building Code details."]),
                ("Gate and latch", ["The gate must open away from the pool, close and latch on its own, with the release on the pool side out of a young child's reach."]),
                ("Height and climbability", ["4 feet minimum, measured outside. Decorative horizontal rails or panels on the outside can create footholds even on an approved design."]),
                ("Doors, clutter and distance", [f"Doors and windows opening to the pool from the house need an approved safety feature ({FEAT}). Keep equipment and furniture off the outside of the fence, and make sure it's not right at the water."]),
            ],
            faqs=[("What fails most often?", "Gate hardware and swing direction."),
                  ("Do decorative rails matter?", "Yes, if they're on the outside and climbable."),
                  ("Can you fix problems before my inspection?", "Yes, usually quickly.")]),
        "fence-gates": dict(
            glance=["Matches your approved fence", "Rigid frames for horizontal styles", "Walk, double and slide gates", "Quality hinges and latches", "HOA-ready drawings"],
            sections=[
                ("Gate sizes", ["4' for foot traffic, 5' for mowers and 10' to 12' double gates for boats and trailers."]),
                ("Modern gates stay level", ["Horizontal and modern designs put more stress on the hinge side, so we build them on rigid internal frames with adjustable hardware."]),
                ("Swing or slide", ["Where swing room is tight, a cantilever slide gate moves sideways on its own track, with no wheels on the ground."]),
            ],
            faqs=[("Will my horizontal gate sag?", "Not if it's built on a rigid frame with proper posts, which is how we build them."),
                  ("Can you match my existing fence?", "Usually, yes."),
                  ("Do new gates need HOA approval?", "Often, especially if they change the fence line or face the street.")]),
        "driveway-gates": dict(
            glance=["Modern and classic designs", "Approval-ready drawings", "Swing or slide", "Automation-ready", "Openers as an add-on"],
            sections=[
                ("Design first", ["We design driveway gates to match your home and approved fence, then prepare elevations, materials and colors for review."]),
                ("Swing or slide", ["Swing gates need a clear arc of driveway; slide gates need space along the fence instead and suit tight setbacks."]),
                ("Automation", ["Gates are manual by default. Openers are quoted separately with the operator, sensors and power, and must meet the UL 325 safety standard."]),
            ],
            faqs=[("Will my HOA approve a driveway gate?", "Many do with the right design; we'll check your community's rules."),
                  ("Which is more modern, swing or slide?", "Both can be; slide gates often suit wide, modern drives."),
                  ("Can I add an opener later?", "Yes, if planned for when the gate is built.")]),
        "dog-fence": dict(
            glance=["Height for your breed", "Puppy-picket aluminum", "Privacy for reactive dogs", "Dig guards", "Self-latching gates"],
            sections=[
                ("Height and type", ["4' for most small and medium dogs, 5' to 6' for large or athletic dogs. Solid privacy suits climbers and dogs that react to the sidewalk."]),
                ("Gaps and digging", ["Puppy-picket aluminum closes bottom gaps for small dogs; buried wire stops diggers."]),
                ("Gates", ["Self-closing hinges and dog-proof latches prevent most escapes."]),
            ],
            faqs=[("What's best on a corner lot?", "Often a mix: privacy along the busy side, aluminum elsewhere, within HOA rules."),
                  ("Can you add puppy-picket to my fence?", "On many aluminum fences, yes."),
                  ("Will my HOA allow a dog fence?", "Most allow approved styles; we'll prepare the application.")]),
        "fence-replacement": dict(
            glance=["Current HOA standards checked", "Application and permit handled", "Old fence removed", "Quick swap", "Workmanship warranty"],
            sections=[
                ("When to replace", ["Widespread post rot, cracked or faded panels and leaning runs are signs it's time. Isolated damage can be repaired."]),
                ("The process", ["We check current guidelines, submit the application, handle any permit, then remove and replace in a quick back-to-back install. Haul-away can be included."]),
                ("Upgrade options", ["Many owners choose vinyl or aluminum, or a modern horizontal style where approved."]),
            ],
            faqs=[("Do I need approval to replace a fence?", "Usually, especially if anything changes."),
                  ("Can I switch materials?", "If the new material is approved by your community."),
                  ("How long is the yard open?", "Typically just during install.")]),
        "hurricane-fence-repair": dict(
            glance=["Safety first", "Photos for insurance", "Pool areas secured", "Matching repairs", "Help with HOA paperwork"],
            sections=[
                ("Immediately after", ["Avoid downed lines, photograph all damage before cleanup and secure pool areas."]),
                ("Repair or replace", ["Panels down on good posts can be repaired; widespread post failure usually calls for replacement. We'll explain which in writing."]),
                ("Rebuild right", ["Deeper posts, more concrete and quality panels resist wind better."]),
            ],
            faqs=[("Will insurance cover it?", "Many policies cover wind damage subject to your deductible; we provide estimates."),
                  ("Do I need HOA approval for repairs?", "Matching repairs often don't; replacements usually do."),
                  ("Can you match my fence?", "Usually, yes.")]),
    },

    # ================================================================== South Tampa
    "southtampa": {
        "pool-fence": dict(
            glance=["Florida pool barrier compliant", "Planned for tight lots", "Self-closing, self-latching gates", "Styles that suit historic homes", "Doors and alarms considered"],
            sections=[
                ("What Florida requires", [f"Florida law requires residential pool barriers to be at least 4 feet tall measured outside, to surround the pool and to have no openings or features a young child could use to get under, through or over. The barrier also needs to stand back from the water's edge ({LAW}).",
                                            "Gates must open outward, away from the pool, and close and latch on their own, with the latch release on the pool side out of a young child's reach."]),
                ("Doors and windows count", [f"On small lots where the house is part of the barrier, any door or window that opens directly onto the pool needs an approved safety feature, such as an exit alarm or a self-closing, self-latching door device ({FEAT}). We plan the fence and doors together."]),
                ("Material choices", ["Aluminum and ornamental styles suit most South Tampa homes and keep the pool area open; vinyl adds privacy where neighbors are close. Hardware rated for salt air matters near the bay."]),
            ],
            faqs=[("Can my house wall be part of the pool barrier?", "Yes, if doors and windows onto the pool have an approved safety feature."),
                  ("Does a historic district affect my pool fence?", "It can affect visible fences. We'll check what review applies to your address."),
                  ("What's the minimum height?", "4 feet from outside under state law.")]),
        "pool-fence-inspection-florida": dict(
            glance=["Doors onto the pool are key", "Gate swing and latch", "4' minimum height", "No climbing aids", "Barrier set back from water"],
            sections=[
                ("Start here", [f"This pre-check follows Florida's barrier law ({LAW}); your inspector also applies the Florida Building Code."]),
                ("Doors and windows", [f"Most South Tampa pools sit close to the house, so check every door and window that opens onto the pool area for an approved safety feature ({FEAT})."]),
                ("Gate", ["Outward-swinging, self-closing and self-latching, with the release on the pool side out of a child's reach."]),
                ("Height, gaps and clutter", ["Measure 4 feet from outside, look for gaps under the fence and remove anything a child could climb, like pool equipment or planters near the fence."]),
            ],
            faqs=[("Do I need door alarms?", "If doors open directly to the pool and the house is part of the barrier, an approved safety feature is required; alarms are one option."),
                  ("What fails most?", "Gates and doors that don't close and latch on their own."),
                  ("Can you help before inspection?", "Yes, we check and fix barriers.")]),
        "fence-gates": dict(
            glance=["Picket and ornamental gates", "Arched and custom designs", "Salt-air-ready hardware", "Walk and drive gates", "Self-closing options"],
            sections=[
                ("Gates that suit the house", ["A picket gate for a bungalow, an ornamental aluminum gate for a Mediterranean, a privacy gate for an alley. We design gates to match the home."]),
                ("Sizes", ["3' to 4' for walkways, 5' for side yards with mowers, 10' to 12' double gates or slide gates for vehicles."]),
                ("Hardware for the bay", ["Near the water, hinges and latches corrode faster, so we use stainless or coated hardware and frames that stay square."]),
            ],
            faqs=[("Can you build an arched gate?", "Yes, in aluminum, steel or wood."),
                  ("Will my gate rust?", "Not with the right materials and hardware for salt air."),
                  ("Can you replace only my gate?", "Yes.")]),
        "driveway-gates": dict(
            glance=["Slide gates for narrow drives", "Alley gates", "Ornamental styles", "Automation-ready", "Openers as an add-on"],
            sections=[
                ("Fitting the space", ["Many South Tampa drives can't fit a swing gate's arc, so slide gates are common. Alley entrances can be gated to secure the whole backyard."]),
                ("Style", ["Ornamental aluminum and steel suit most homes; wood and vinyl can match privacy fencing."]),
                ("Automatic operation", ["Openers are quoted separately with operator, sensors and power. Automated gates must meet the UL 325 safety standard."]),
            ],
            faqs=[("Is a slide gate possible on a short drive?", "If there's space along the fence for it to travel back."),
                  ("Do historic districts affect gates?", "Visible changes may need review; we'll check."),
                  ("Can I automate later?", "Yes, if built for it.")]),
        "dog-fence": dict(
            glance=["Height for your breed", "Privacy along busy sidewalks", "Picket fronts", "Dig guards", "Self-latching gates"],
            sections=[
                ("Height", ["4' contains most small and medium dogs; larger and athletic dogs need 5' to 6' where allowed."]),
                ("Front yards and sidewalks", ["Front yard fences are often limited in height, so a well-built picket or aluminum fence with a secure gate is common up front, with privacy in back for reactive dogs."]),
                ("Gaps, digging, gates", ["We close gaps at the bottom, add dig guards and use self-closing, dog-proof latches."]),
            ],
            faqs=[("How tall can my front fence be?", "That depends on local code for your address; we'll check before designing."),
                  ("What helps a barking dog?", "Solid privacy panels that block the view."),
                  ("Can you secure an alley gate?", "Yes, with self-closing hinges and a locking latch.")]),
        "fence-replacement": dict(
            glance=["Removal and haul-away", "Salt-air-ready materials", "Drainage-aware post setting", "Permit handled", "Workmanship warranty"],
            sections=[
                ("Repair or replace", ["Patched-up fences with failing posts throughout are better replaced; isolated damage can be repaired."]),
                ("How it works", ["We confirm lines, handle any required permit or review, remove the old fence and install the new one back to back. Haul-away can be included."]),
                ("Choosing materials", ["Near the bay, we recommend materials and fasteners that resist corrosion, and we watch drainage on low lots."]),
            ],
            faqs=[("Do historic districts affect replacement?", "Visible changes may need review; we'll check your address."),
                  ("Can you reuse posts?", "Rarely."),
                  ("How long does it take?", "Usually one to two days.")]),
        "hurricane-fence-repair": dict(
            glance=["Avoid downed lines", "Document for insurance", "Check posts after flooding", "Secure pool barriers", "Corrosion-resistant rebuilds"],
            sections=[
                ("First steps", ["Stay clear of downed lines, photograph damage before cleanup and secure pool areas."]),
                ("After flooding", ["Water-softened ground lets posts shift. We check posts for movement, not just panel damage, before recommending repair or replacement."]),
                ("Rebuilding", ["Deeper posts, more concrete and corrosion-resistant hardware stand up better to the next storm."]),
            ],
            faqs=[("Does flood damage count?", "Coverage depends on your policy; check with your agent."),
                  ("Can you repair metal fences?", "Yes, aluminum and steel included."),
                  ("How fast can you come?", "Call early, and tell us if the fence is your pool barrier.")]),
    },

    # ================================================================== Starkey
    "starkey": {
        "pool-fence": dict(
            glance=["Florida pool barrier compliant", "Timed with your pool build", "Self-closing, self-latching gates", "Open views to watch kids", "HOA-approved styles"],
            sections=[
                ("Florida's pool barrier basics", [f"Florida law sets the minimum: a barrier at least 4 feet high measured outside, surrounding the pool, with no gaps or footholds a young child could use to get under, through or over it, and set back from the water ({LAW}). Gates open away from the pool and close and latch on their own, with the release out of a young child's reach."]),
                ("Coordinating with your pool builder", ["When a pool is added after move-in, the barrier needs to be ready for the pool's final inspection. We schedule around your builder and HOA approval."]),
                ("What families choose", ["Black aluminum is a popular choice because parents can see the pool from the house. Vinyl privacy works when neighbors are close. Either way, we keep the outside of the fence free of footholds."]),
            ],
            faqs=[("When should I order my pool fence?", "As soon as your pool is scheduled, so HOA approval is done before the pool's final inspection."),
                  ("Can my yard fence double as the pool barrier?", "It can if it surrounds the pool and meets every barrier requirement, including the gates."),
                  ("What other safety options are there?", f"For new pools, Florida also accepts covers, alarms and door devices ({FEAT}).")]),
        "pool-fence-inspection-florida": dict(
            glance=["Clear kids' gear off the fence", "Gate must close and latch itself", "4' minimum from outside", "Check doors to the pool", "Barrier set back from water"],
            sections=[
                ("Before the inspector arrives", [f"This list follows Florida's pool barrier law ({LAW}); the inspector also applies building code details."]),
                ("The gate", ["Swings away from the pool, closes and latches itself every time, with the release on the pool side out of a child's reach."]),
                ("Climbing aids", ["Play sets, bikes, coolers and furniture against the outside of the fence can count as climbing aids. Move them before inspection."]),
                ("Height, gaps and doors", [f"Measure 4 feet from outside, check for gaps underneath, and make sure doors opening onto the pool have an approved safety feature ({FEAT})."]),
            ],
            faqs=[("Does a play set near the fence matter?", "Yes, if a child could use it to climb over."),
                  ("What's the top failure?", "Gates that don't self-close and self-latch reliably."),
                  ("Can you check my barrier first?", "Yes.")]),
        "fence-gates": dict(
            glance=["Self-closing family gates", "Kid-proof latch heights", "Walk and double gates", "Framed to stay square", "Pool-compliant options"],
            sections=[
                ("Sizes for family yards", ["4' for everyday use, 5' for mowers and wagons, double gates for boats or trailers."]),
                ("Gates that close themselves", ["Self-closing hinges and gravity latches keep gates shut even when kids forget, which matters for pets and pools."]),
                ("Built to last", ["Metal-framed vinyl and wood gates, deeper gate posts and quality hardware keep gates working smoothly."]),
            ],
            faqs=[("Can latches be out of kids' reach?", "Yes, we set latch height for your family."),
                  ("Do I need HOA approval for a gate?", "Often, as part of your fence application."),
                  ("Can you add a second gate?", "Yes, in most fence types.")]),
        "driveway-gates": dict(
            glance=["Keeps kids and dogs off the street", "Swing or slide", "Built for openers", "Set back for pull-off", "Openers as an add-on"],
            sections=[
                ("Choosing a style", ["Swing gates for level drives; slide gates for slopes, short setbacks or wide openings."]),
                ("Acreage and long drives", ["On larger Odessa and Keystone properties, gates are often far from the house, so we build them ready for an opener."]),
                ("Automation", ["Openers are quoted separately with the operator, sensors and power, and must meet the UL 325 safety standard."]),
            ],
            faqs=[("Can a gate keep my kids off the street?", "Yes, especially with self-closing hardware."),
                  ("Is solar an option?", "Often, for remote gates."),
                  ("Does my HOA need to approve?", "Most likely.")]),
        "dog-fence": dict(
            glance=["Puppy-picket aluminum", "Dig guards along preserves", "Right height for your dog", "Self-latching gates", "HOA-approved styles"],
            sections=[
                ("Height", ["4' for most small and medium dogs; 5' to 6' for large or athletic dogs and jumpers."]),
                ("Puppies and preserves", ["Puppy-picket panels keep small dogs from slipping out, and a dig guard stops tunneling toward the preserve."]),
                ("Gates", ["Self-closing gates and dog-proof latches prevent escapes when kids leave a gate open."]),
            ],
            faqs=[("Will puppy-picket keep a small puppy in?", "It closes the bottom gaps that standard aluminum leaves."),
                  ("Can you fence along the preserve?", "Within your lot and HOA rules, yes."),
                  ("How tall for a lab?", "Usually 4' to 5', depending on your dog.")]),
        "fence-replacement": dict(
            glance=["Builder fences upgraded", "Stronger posts", "Heavier panels", "Permit and HOA handled", "Workmanship warranty"],
            sections=[
                ("Signs it's time", ["Leaning sections, loose panels and posts moving in the ground mean replacement; small issues can be repaired."]),
                ("The process", ["Estimate, HOA application, permit when needed, then removal and installation back to back. Haul-away can be included."]),
                ("Upgrade the builder fence", ["Deeper posts and heavier panels make the new fence far sturdier than many original builder installs."]),
            ],
            faqs=[("Why is my newer fence leaning?", "Often shallow posts or lightweight panels."),
                  ("Can I switch materials?", "If your HOA approves it."),
                  ("How long does it take?", "Usually one to two days.")]),
        "hurricane-fence-repair": dict(
            glance=["Safety first", "Photos for insurance", "Pool barriers first", "Honest repair vs. replace", "Sturdier rebuilds"],
            sections=[
                ("Right after the storm", ["Avoid downed lines, photograph damage before cleanup and secure pool areas and pets."]),
                ("Repair or replace", ["Panel damage on solid posts is repairable; leaning or broken posts across runs usually mean replacement."]),
                ("Stronger rebuilds", ["Deeper posts and heavier panels resist wind far better than lightweight builder fences."]),
            ],
            faqs=[("Does insurance cover my fence?", "Many policies cover wind damage; we provide written estimates."),
                  ("Do I need HOA approval?", "Matching repairs often don't; replacements usually do."),
                  ("How soon can you come?", "Call early, and tell us if the fence is a pool barrier or keeps pets in.")]),
    },
}
