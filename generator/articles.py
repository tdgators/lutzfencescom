# -*- coding: utf-8 -*-
"""Articles from PAGE_BACKLOG.md. Unlike the pages in new_pages.py, each article lives on
one or two sites only, and every site gets its own full text, so ARTICLES is keyed
slug -> shared fields, then content module name -> that site's copy.

Facts checked Nov 2026: horse heights from UGA Extension B1192, sheep and goat height from
UC ANR, private lines from Sunshine 811, Tampa cart sizes from the city's cart cleaning
program. Never add code numbers or permit rules here without a source.
"""

UGA_HORSE = "https://fieldreport.caes.uga.edu/publications/B1192/"
UC_GOATS = "https://ccfruitandnuts.ucanr.edu/sites/default/files/2020-08/332289.pdf"
SUNSHINE_811 = "https://sunshine811.com/news-blog/april-is-safe-digging-month-know-the-ground-rules-florida"
TAMPA_CARTS = "https://www.fox13news.com/news/tampa-solid-waste-department-starts-trash-recycling-bin-cleaning-service"


def _link(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


# Related cards: (title, href, blurb)
R_COMMERCIAL = ("Commercial Fencing", "commercial-fencing.html", "Security, access control and gates for businesses.")
R_SECURITY = ("Security Fencing", "security-fencing.html", "Perimeter fencing for sites that need real protection.")
R_INDUSTRIAL = ("Industrial Fencing", "industrial-fencing.html", "Heavy-duty fencing for yards and warehouses.")
R_HOA = ("HOA &amp; Community Fencing", "hoa-fencing.html", "Fencing for shared amenities and entrances.")
R_DUMPSTER = ("Dumpster Enclosures", "dumpster-enclosures.html", "Screening for commercial trash areas.")
R_DOG = ("Dog &amp; Pet Fences", "dog-fence.html", "Fences built around how your dog behaves.")
R_REPAIR = ("Fence Repair", "fence-repair.html", "Leaning posts, broken boards and gates that won't latch.")
R_ALUMINUM = ("Aluminum Fence", "aluminum-fence.html", "Open views and no rust.")
R_PRIVACY = ("Privacy Fence", "privacy-fence.html", "Solid screening for your yard.")
R_VINYL = ("Vinyl Fence", "vinyl-fence.html", "Low upkeep in Florida weather.")
R_WOOD = ("Wood Fence", "wood-fence.html", "Classic look, easy to match.")
R_SPLIT = ("Split Rail Fence", "split-rail-fence.html", "Open, rustic rail fencing.")
R_GATES = ("Fence Gates", "fence-gates.html", "Walk, double drive and slide gates.")
R_DRIVEWAY = ("Driveway Gates", "driveway-gates.html", "Manual gates, with operators as an add-on.")
R_HOA_GUIDE = ("HOA Approval Guide", "hoa-fence-approval-guide.html", "What to send your HOA before you build.")
R_FINANCING = ("Financing", "financing.html", "Payment plans through Wisetack.")
R_HORSE = ("Horse &amp; Pasture Fences", "horse-pasture-fence.html", "Rail and mesh options for horses and livestock.")
R_SOLAR = ("Fencing Around Ground-Mounted Solar", "fence-guides/ground-mounted-solar-fence.html", "What to plan before fencing an array.")

ARTICLES = {
    "fence-guides/choosing-commercial-fence": dict(
        kicker="Fence Guides", photo="commercial-fence.webp",
        photo_alt="Black chain link fence and rolling gate around a Florida warehouse lot",
        blurb="What to decide before you request a commercial fence bid.",
        sites={
            "northtampa": dict(
                name="Choosing a Commercial Fence",
                tagline="Start with what the fence has to do, then pick the material.",
                meta_title="How to Choose a Commercial Fence in North Tampa | {brand}",
                meta="How North Tampa property owners and managers choose a commercial fence: security level, traffic flow, materials, gates and what to include in a bid.",
                intro=["Most commercial fence decisions start with the wrong question. Before you compare materials, write down what the fence has to do: stop theft, direct traffic, hide equipment, or just mark a property line. That one sentence narrows your options quickly and gets you better bids."],
                glance=["Define the job before the material", "Plan gates around daily traffic", "Chain link, steel, aluminum or vinyl", "Automatic gates are an add-on", "Get bids on the same scope"],
                sections=[
                    ("Match the fence to the risk", [
                        "A storage yard with equipment outdoors needs something different from a medical office that wants a clean edge along the parking lot. Security fences are about delay and visibility: height, strong posts, and little to grab or climb. Screening fences are about what people can see. Boundary fences mostly need to look right and last.",
                        "Be honest about which one you need. Paying for high security on a site that only needs screening wastes budget, and a decorative fence around a yard full of copper won't do much.",
                    ]),
                    ("North Tampa sites we think about differently", [
                        "North Tampa mixes warehouses and contractor yards with apartment communities, offices and shops, often close together. A fence behind a shopping strip may back up to homes, so the look from the neighbor's side matters. Sites with ponds or retention areas also need the fence line planned around the water and any drainage easement.",
                        "Trucks are the other local issue. If delivery vehicles or trailers use the lot, we walk the turning path before anything is drawn, because a gate in the wrong spot gets hit.",
                    ]),
                    ("The main materials", [
                        "<strong>Chain link</strong> is the workhorse: affordable, strong and easy to repair, with optional privacy slats. <strong>Ornamental steel or aluminum</strong> looks better from the street and suits offices, retail and community entrances. <strong>Vinyl</strong> gives you full screening with little upkeep, which is useful around dumpsters and equipment.",
                    ]),
                    ("Gates decide how the site works", [
                        "Count who comes through every day and how. A slide gate needs clear space along the fence line, and a swing gate needs room to open. If you want an automatic gate, plan power and access control from the start and make sure the operator meets UL 325, the safety standard for gate operators.",
                    ]),
                    ("Getting bids you can compare", [
                        "Give every contractor the same scope: a site plan, fence height, material, gate count and sizes, and any requirements from your landlord, association or the city. Ask each one to confirm permits, removal of the old fence, and a certificate of insurance. Bids on different scopes aren't comparable, whatever the price.",
                    ]),
                ],
                faqs=[
                    ("What's the most affordable commercial fence?", "Chain link usually costs the least per foot and holds up well. Privacy slats add screening for a modest extra cost."),
                    ("Can you work around our business hours?", "Tell us your hours and busy periods up front. We'll plan the phases so that access stays open where it needs to."),
                    ("Can you add an automatic gate later?", "Yes, if the gate and posts are built for it. Tell us at the start so we can plan for power and a gate that suits an operator."),
                ],
                related=[R_COMMERCIAL, R_SECURITY, R_INDUSTRIAL],
            ),
            "westchase": dict(
                name="Choosing a Commercial Fence",
                tagline="A short guide for property managers, business owners and boards.",
                meta_title="Choosing a Commercial Fence in Westchase | {brand}",
                meta="A Westchase guide to choosing a commercial fence for offices, retail and community properties: appearance, screening, gates and how to scope a bid.",
                intro=["If you manage an office park, a retail center or a community amenity around Westchase, a fence is usually part of how the property looks as much as how it's protected. Here's how we'd approach the decision if we were in your seat."],
                glance=["Appearance often comes first", "Screen dumpsters and equipment", "Keep sight lines at driveways", "Check owner and association rules", "Write one scope for all bidders"],
                sections=[
                    ("Decide who the fence is for", [
                        "Customers, tenants, neighbors and residents all see a commercial fence differently. Along a storefront or a clubhouse entrance, the fence is part of the first impression, so finish and proportion matter. Behind the building, the job may just be to keep people out of a service area and keep carts and dumpsters out of view.",
                        "Many properties need both, and there's no reason to use one fence for the whole site. Using nicer fencing where people look and simpler fencing where they don't is a sensible way to spend the budget.",
                    ]),
                    ("Well-kept properties, shared rules", [
                        "Around Westchase, commercial sites often sit next to established neighborhoods, and many answer to a landlord, an owners' association or a management company. Before picking a style, get any written requirements for color, height and placement. It's much cheaper to learn them before the drawing than after the install.",
                    ]),
                    ("Style choices that age well", [
                        "Black ornamental aluminum or steel is the safe choice for visible frontage: it looks clean and doesn't compete with the building. White or tan vinyl gives solid screening around utility areas and needs only occasional washing. Coated chain link is practical for back-of-house areas and sport courts.",
                    ]),
                    ("Don't forget gates and sight lines", [
                        "Delivery drivers, trash trucks, maintenance crews and emergency access all need a way through. List them before you choose gate locations. Near driveways, keep fencing and landscaping from blocking a driver's view of the sidewalk or street. Your site plan and local rules determine exactly what's allowed, so we check that for your address.",
                    ]),
                    ("Scope it once, then bid it", [
                        "Write one scope and send it to everyone: the footage, height, finish, gates, old-fence removal, and working hours. If tenants are open during the work, say so. Ask for a certificate of insurance and a clear warranty. Then you're comparing prices, not guesses.",
                    ]),
                ],
                faqs=[
                    ("Do you work with property managers and associations?", "Yes. Send us the site plan and any written requirements, and we'll write the proposal so it's easy to take to an owner or board."),
                    ("What fence works best around a dumpster?", "Solid vinyl or a similar screening panel with a sturdy gate is the usual answer. Our dumpster enclosures page has more detail."),
                    ("Can a fence be installed while we're open?", "Usually. We plan the work in sections and keep entrances open. Tell us your busiest days and any tenant needs."),
                ],
                related=[R_COMMERCIAL, R_HOA, R_DUMPSTER],
            ),
        },
    ),

    "fence-guides/dog-fence-problems": dict(
        kicker="Fence Guides", photo="dog-fence.webp",
        photo_alt="Black aluminum puppy-picket fence along a green lawn",
        blurb="Why dogs get out, and the fence fix for each kind of escape.",
        sites={
            "starkey": dict(
                name="Why Dogs Escape, and How to Fix It",
                tagline="Diggers, jumpers and squeezers each need a different fix.",
                meta_title="Dog Fence Problems and Fixes in Starkey Ranch | {brand}",
                meta="Why dogs get out of fenced yards in Starkey Ranch and Odessa, and the fence fix for digging, jumping, squeezing through gaps and slipping past gates.",
                intro=["If your dog keeps getting out, the fence is telling you how. Look at where and how the escape happens, because the right fix for a digger does nothing for a jumper. Here are the most common problems we see, and what we'd do about each one."],
                glance=["Find the escape route first", "Dig guards stop tunneling", "Height and footholds stop jumpers", "Close-set pickets stop squeezers", "Gates are the most common weak spot"],
                sections=[
                    ("The digger", [
                        "Look for loose soil or a shallow trench along the fence line, usually where your dog can smell or see something on the other side. The fix is a dig guard: wire mesh or a similar barrier along the bottom of the fence, turned out or set below the soil so there's nothing to tunnel past.",
                    ]),
                    ("Preserve views and curious noses", [
                        "Many Starkey Ranch homes look out over a preserve or a trail. That's lovely for you, but it's a lot of smells and movement for a dog. Open fences keep the view, so the bottom edge matters more here. On aluminum, puppy-picket panels and a tight gap at the ground handle most small dogs. Check your community's fence rules before you change the style, and see our <a href=\"hoa-fence-approval-guide.html\">HOA approval guide</a> if you need to send a request.",
                    ]),
                    ("The jumper", [
                        "If your dog clears the fence, or scrambles up it, you need more height or fewer places to push off. Check for AC units, benches, planters and woodpiles beside the fence first. Moving those can solve the problem for free. Horizontal rails on the inside can also work as a ladder, so ask us about turning rails toward the outside where your rules allow it.",
                    ]),
                    ("The squeezer", [
                        "Puppies and small dogs fit through gaps you wouldn't expect. Hold a tape to the space between pickets, the space under the fence and the gap at each gate post. Puppy-picket panels close the lower gaps on aluminum, and a low rail or trim board can close a gap at the ground on other fences.",
                    ]),
                    ("The gate slipper", [
                        "Plenty of dogs never touch the fence. They wait for the gate. A self-closing hinge and a latch that catches every time fix a surprising number of escapes, especially with kids, landscapers and pool crews in and out. If a gate sags or drags, have it adjusted before it stops latching.",
                    ]),
                ],
                faqs=[
                    ("How tall should a fence be for my dog?", "It depends on the dog more than the breed. A 4' fence is fine for many small dogs, while strong jumpers often need 6' with nothing nearby to push off from. Your community's rules may also limit height."),
                    ("Do you train dogs not to escape?", "No, we fix the fence. If your dog is anxious or determined, a trainer or your vet can help with the behavior while we close the gaps."),
                    ("Can you fix my fence, or does it need replacing?", "Most escape problems can be solved with repairs or add-ons. If the fence has reached the end of its life, we'll tell you."),
                ],
                related=[R_DOG, R_ALUMINUM, R_HOA_GUIDE],
            ),
            "carrollwood": dict(
                name="Fixing an Older Fence for Your Dog",
                tagline="Most escapes come down to a few weak spots you can find yourself.",
                meta_title="Fixing Dog Escape Problems on Older Fences in Carrollwood | {brand}",
                meta="How Carrollwood homeowners can find and fix the weak spots dogs use on older fences: gaps at the ground, loose boards, tree roots, and bad gate latches.",
                intro=["You don't always need a new fence to keep a dog home. On older Carrollwood lots, the usual culprit is one or two weak spots that a determined dog has found. Walk the fence with a tape measure and a critical eye, and you'll often find the answer in about ten minutes."],
                glance=["Walk the whole fence line", "Check gaps at the ground", "Look for rot and loose boards", "Test every gate latch", "Repair first, replace if needed"],
                sections=[
                    ("Start at the bottom", [
                        "Wood fences settle, soil washes away and bottom edges rot. A gap that started at one inch may be big enough for a small dog after a few rainy seasons. Measure along the ground, especially at low spots where water runs. Filling a washout, adding a rot board or fitting wire mesh along the bottom closes most of these gaps.",
                    ]),
                    ("Big oaks, lifted fences", [
                        "Mature oaks are one of the best parts of living in Carrollwood, but their roots can lift posts and force the fence up. That leaves gaps at the ground and leaning sections your dog can push against. We work around roots rather than through them, often by moving a post or spanning the root with a custom section instead of cutting it.",
                    ]),
                    ("Loose boards and hidden holes", [
                        "Push on the pickets as you walk. If one swings aside, a dog has probably already noticed. Pickets that have lost their fasteners are a quick fix. Soft, dark wood at the rails or the base is a sign of rot, and that section may need replacing so that new boards have something solid to attach to.",
                    ]),
                    ("Gates: the first thing to test", [
                        "Close each gate, then pull on it. A sagging gate often looks closed even when the latch hasn't caught. Tightening hinges, adding an anti-sag kit or resetting the post usually solves it. Self-closing hinges are worth adding if the gate gets left open. Our <a href=\"fence-care.html\">fence care guide</a> covers the simple fixes you can try first.",
                    ]),
                    ("Dogs that dig or climb", [
                        "If there's digging along one stretch, a dig guard can stop it. If your dog gets over, look for what's helping: a stacked woodpile, an AC unit or a low roofline beside the fence. Moving them is free. Adding height is possible on some fences, but check the rules for your address and the condition of the posts first.",
                    ]),
                    ("When replacing makes more sense", [
                        "If posts are rotted through, most sections lean, or you're patching the same fence every year, repairs stop being a bargain. We'll give you an honest answer either way, and if it's time, a <a href=\"fence-replacement.html\">fence replacement</a> lets you choose a fence that suits your dog from the start.",
                    ]),
                ],
                faqs=[
                    ("Can you just fix one section?", "Yes. We repair single sections, posts and gates all the time. We'll match the existing fence as closely as we can, though aged wood will look a little different at first."),
                    ("Will tree roots damage a new fence too?", "They can, over time. We plan post locations around big roots and tell you where future movement is likely."),
                    ("What's the fastest fix for a small dog?", "Usually closing the gaps at the ground and at the gate posts, with mesh or a low board. A proper latch is often the other half."),
                ],
                related=[R_DOG, R_REPAIR, R_PRIVACY],
            ),
        },
    ),

    "horse-pasture-fence": dict(
        kicker="Fence Types", photo="horse-pasture-fence.webp",
        photo_alt="Black four-rail board fence in a green Florida pasture with a horse in the distance",
        blurb="Rail, board, vinyl and mesh options for horses and livestock.",
        sites={
            "brooksville": dict(
                name="Horse &amp; Pasture Fences",
                tagline="Rail, board, vinyl and mesh fences for horses and livestock.",
                meta_title="Horse &amp; Pasture Fences in Brooksville, FL | {brand}",
                meta="Horse and pasture fence options for Brooksville and Hernando County: 3-rail and 4-rail black fences, vinyl, wood board, stable matching, sheep and goat fencing.",
                intro=["There's no single right pasture fence. A paddock for a young horse, a long boundary line, and a pen for goats all ask different things of a fence. This overview walks through the main options we can build around Brooksville, and how to choose between them."],
                glance=["3-rail and 4-rail black fences", "Vinyl or wood board", "Match an existing stable", "Sheep and goat fencing", "Gates sized for trucks and trailers"],
                sections=[
                    ("Start with the animal", [
                        f'Height comes first. University of Georgia Extension recommends a minimum of 5 feet for horse perimeter pasture fences, with dividing fences as low as 4.5 feet. For paddocks and pens, it suggests a top rail about 4 to 6 inches above the withers ({_link(UGA_HORSE, "UGA Extension, Fences for Horses")}). Young, tall or spirited horses can push those numbers up, so tell us who will be living behind it.',
                        "Horses also run into fences, lean over them and chew on them. Visible rails, no sharp wire ends, and nothing a hoof can get caught in matter more than they do with almost any other fence.",
                    ]),
                    ("Hernando County acreage", [
                        "Long fence lines change the math. On a few acres, the price per foot matters, and so does how much upkeep you're signing up for. A common approach is to use a nicer rail fence along the road and around the house and barn, then a practical mesh or wire fence for the back boundary. Sandy ground and low spots also affect post depth and placement, so we walk the line before we quote it.",
                    ]),
                    ("3-rail and 4-rail black fences", [
                        "Black rail fencing is the classic farm look, and it hides dirt and wear well. Three rails suit open pastures and frontage. Four rails give you a tighter, taller fence, which helps with smaller animals, foals and busy paddocks. Boards need repainting over time to stay black, so plan on that upkeep.",
                    ]),
                    ("Wood or vinyl", [
                        "<strong>Wood board</strong> is strong and easy to repair one rail at a time, and you can stain or paint it to suit the property. <strong>Vinyl rail</strong> skips the painting and won't rot, and a washdown keeps it looking clean. Either one can have a mesh added on the inside if you need to keep smaller animals or dogs in.",
                    ]),
                    ("Matching your stable", [
                        "If you have a barn or stable, the fence should look like it belongs there. We can match its color and trim, repeat the rail count from an existing section, or carry a single style from the entrance through to the paddocks. Bring photos and we'll work out what fits the budget.",
                    ]),
                    ("Sheep and goats", [
                        f'Goats treat most fences as a puzzle. A horse rail won\'t hold them, so sheep and goat fences use woven wire or mesh with small openings. UC Cooperative Extension advises at least 48 inches of height to stop animals climbing over ({_link(UC_GOATS, "UC ANR")}). If predators are a concern, tell us, because that changes the mesh and may add a bottom strand.',
                    ]),
                ],
                faqs=[
                    ("What's the best fence for horses?", "It depends on the horses and the land. Rail fences are highly visible and suit paddocks and frontage, while no-climb mesh is a common choice for long boundaries. We'll help you weigh them."),
                    ("Should I use barbed wire for horses?", "We don't recommend it. Horses that run into or reach through barbed wire can be badly cut, and there are safer options at similar costs."),
                    ("Can one fence hold horses and goats?", "Yes, with mesh on a taller fence, usually topped with a rail so that horses can see it. Tell us everything you plan to keep."),
                    ("Can you build gates for trucks and trailers?", "Yes. Tell us what needs to get through, and we'll size the gate and plan the turning room."),
                ],
                related=[R_SPLIT, R_GATES, R_SOLAR],
            ),
            "lutz": dict(
                name="Horse &amp; Pasture Fences",
                tagline="Fences for small farms and horse properties north of Tampa.",
                meta_title="Horse &amp; Pasture Fences in Lutz, FL | {brand}",
                meta="Horse and pasture fences for Lutz, Land O' Lakes and Pasco County: black rail, vinyl and wood board styles, stable matching, and sheep and goat fencing.",
                intro=["Small horse properties need a fence that works hard and still looks good beside the house. Whether you're fencing two acres in Lutz or a larger parcel farther into Pasco County, here's a quick guide to the styles available and what each one is good at."],
                glance=["Black rail in 3 or 4 rails", "Low-upkeep vinyl rail", "Wood board, painted or stained", "Fences to match your barn", "Sheep and goat mesh"],
                sections=[
                    ("How tall is tall enough?", [
                        f'A good starting point is the guidance from University of Georgia Extension: a 5-foot minimum around the outside of a horse pasture, 4.5 feet between pastures, and about 4 to 6 inches above the withers for paddocks and pens ({_link(UGA_HORSE, "Fences for Horses, UGA")}). A pony and a big warmblood don\'t need the same fence, so we start with your animals, then design from there.',
                    ]),
                    ("Small acreage, close neighbors", [
                        "Around Lutz and Land O' Lakes, horse properties often sit near homes, roads and lakes rather than in the middle of open land. That makes visibility and strength important, because a loose horse quickly reaches a street. It's also why the frontage matters: your fence is what the neighborhood sees. A double line or an extra rail along a busy road is worth discussing.",
                    ]),
                    ("Black rail fences", [
                        "A black 3-rail fence gives you the open look you see on horse farms, and a 4-rail version closes up the spacing for foals, ponies and smaller animals. Painted board needs recoating from time to time, so if you'd rather not, a vinyl version is worth pricing.",
                    ]),
                    ("Vinyl and wood board compared", [
                        "Vinyl rail stays looking new with a wash and doesn't need paint, and it won't rot in our wet summers. Wood board usually costs less up front, feels solid, and lets you replace one broken rail in a few minutes. On many farms the answer is both: vinyl at the front, wood where horses actually lean on it.",
                    ]),
                    ("Tying it into your barn", [
                        "A fence that matches your barn makes the whole property feel planned. We can pick up the trim color, match a rail style you already have, or help you choose a look for both if you're building new.",
                    ]),
                    ("Sheep, goats and mixed pastures", [
                        f'Small flocks and herds need a different fence: woven wire or mesh with small openings, and at least 48 inches tall to discourage climbing, according to {_link(UC_GOATS, "UC Cooperative Extension")}. If you keep goats beside horses, mesh on a rail fence can do both jobs. We\'ll also ask about coyotes and dogs, since that may change the plan.',
                    ]),
                ],
                faqs=[
                    ("Do I need a permit for a pasture fence?", "It depends on the property and where it sits. We'll check the rules for your address before we build, so you're not guessing."),
                    ("How long does a farm fence take to install?", "It depends on footage, terrain and gates. We'll give you a schedule with your estimate once we've walked the line."),
                    ("Will black paint fade in Florida sun?", "It can, over time. Recoating is part of owning a painted board fence. If you want less upkeep, ask us about vinyl."),
                    ("Can you fence around a pond or lake edge?", "Usually, yes. Tell us what's on your survey, and we'll plan around water, wet ground and any easements."),
                ],
                related=[R_GATES, R_VINYL, R_WOOD],
            ),
        },
    ),

    "fence-guides/ground-mounted-solar-fence": dict(
        kicker="Fence Guides", photo="ground-mounted-solar-fence.webp",
        photo_alt="Ground-mounted solar array in a large yard with a low black fence around it",
        blurb="What to plan before you fence a ground-mounted solar array.",
        sites={
            "lutz": dict(
                name="Fencing Around Ground-Mounted Solar",
                tagline="Keep kids, pets and mowers clear without shading your panels.",
                meta_title="Fencing Around Ground-Mounted Solar in Lutz, FL | {brand}",
                meta="How to fence a ground-mounted solar array in Lutz: avoiding shade, keeping service access, working around buried wiring, and choosing the right fence.",
                intro=["Ground-mounted solar means photovoltaic racking set directly on the earth rather than on a roof. That's good for access, but the panels and wiring end up within reach of children, pets, mowers and wildlife. A fence solves that, as long as it's planned around the array rather than simply added afterward."],
                glance=["Keep the fence from shading panels", "Leave room for service and mowing", "Locate buried solar wiring first", "Keep the fence off the racking", "Ask your installer before you build"],
                sections=[
                    ("Why fence an array at all?", [
                        "Ground-mounted panels often have exposed wiring on the back, sometimes at a height a child or a dog can reach. A fence keeps people, pets and mowers at a distance. Whether your system or your local rules actually require one depends on the installation, so ask your solar installer and check with the local building department before you decide on a design.",
                    ]),
                    ("Shade is the first thing to check", [
                        "A fence can cast a shadow across the bottom row of panels, especially in winter when the sun sits low. Solid privacy fencing is the worst offender. On most arrays, an open style like aluminum or coated chain link, set well back from the panels, is the safer choice. Ask your installer how much clearance your array needs, and we'll lay out the fence to match.",
                    ]),
                    ("Lutz lots and lake edges", [
                        "Larger lots around Lutz give you room for an array, but also bring lake edges, wet ground and trees to plan around. Walk the spot with us after a heavy rain if you can. It tells you where water sits, and that affects posts and gates. Check your community's rules too, if you have an HOA, because they may want screening or a certain style.",
                    ]),
                    ("Leave room to work", [
                        "Your solar company will need to get in, and so will your mower. Weeds and tall grass can shade panels just as a fence can, so a clear strip inside the fence is useful. We plan gates wide enough for whatever needs to reach the array, and that strip wide enough to mow.",
                    ]),
                    ("What's under the ground", [
                        f'A buried line usually runs from the array back to the house. Call 811 before any digging, but remember that utilities mark public lines, and Sunshine 811 says it\'s the owner\'s job to have private lines marked ({_link(SUNSHINE_811, "Sunshine 811")}). Get the wiring plan from your installer, and consider a private locator if you don\'t have one.',
                    ]),
                    ("Keep the fence separate", [
                        "We set the fence on its own posts and don't attach anything to the racking. If you're using a metal fence close to the array, ask your solar installer or electrician whether it needs to be bonded or grounded. That's an electrical question, and they should answer it.",
                    ]),
                ],
                faqs=[
                    ("What fence works best around solar panels?", "Usually an open style such as aluminum or coated chain link, because it casts less shadow. The right height depends on your array and how far back the fence sits."),
                    ("Will a fence keep rodents away from the wiring?", "Not by itself. Small animals pass through most fences. Ask your solar installer about guards for the wiring."),
                    ("Can I add a fence after the array goes in?", "Yes, and that's the most common case. We'll need the layout of the buried wiring first."),
                ],
                related=[R_ALUMINUM, R_HORSE, R_GATES],
            ),
            "brooksville": dict(
                name="Fencing Around Ground-Mounted Solar",
                tagline="Protect an array from livestock, wildlife and wandering mowers.",
                meta_title="Fencing a Ground-Mounted Solar Array in Brooksville | {brand}",
                meta="Fencing ground-mounted solar on rural Brooksville property: keeping livestock and wildlife away, avoiding shade, service access, and buried wire safety.",
                intro=["Acreage is a natural fit for ground-mounted solar, where photovoltaic racking stands directly on the ground instead of on a roof. In rural Hernando County, though, the array shares the land with animals, tractors and brush. Here's what to think about before you fence one in."],
                glance=["Keep livestock off the racking", "Open fences cast less shade", "Gates wide enough for equipment", "Mark buried lines before digging", "Check rules with your installer"],
                sections=[
                    ("Animals are the main reason out here", [
                        "Horses rub, goats climb and cattle lean. Any of them can damage racking or reach wiring on the back of the panels. Near livestock, the fence has to be built to hold that animal, not just to mark off the array. If you already have a pasture fence style you like, we can often extend it around the array so that everything matches.",
                    ]),
                    ("Deer, hogs and smaller visitors", [
                        "Larger wildlife is a fair reason to fence, but be realistic about what a fence does. Mesh at the bottom helps with hogs and armadillos. Very small animals still get through, so ask your installer about wire guards under the panels. Fencing and wire guards work together.",
                    ]),
                    ("Don't shade your own power", [
                        "It's easy to forget that a fence throws a shadow. In winter the sun is low, and even a few feet of shade along the bottom of a row can reduce output. Stick with open fence styles and keep the line back from the panels. Your solar company can tell you how much clearance your layout needs.",
                    ]),
                    ("Getting equipment in and out", [
                        "Plan the gate for the biggest thing that will need to reach the array, whether that's a service truck or a tractor with a mower deck. Keep a mowable strip inside the fence, because brush grows fast here and will shade the panels as surely as a fence will.",
                    ]),
                    ("Before anyone digs", [
                        f'Buried solar wiring often runs a long way on rural property. Calling 811 is required, but utilities mark public lines, and private lines are the owner\'s responsibility according to {_link(SUNSHINE_811, "Sunshine 811")}. Ask your installer for the as-built drawing. If there isn\'t one, a private locating company can help.',
                    ]),
                    ("Rules and electrical questions", [
                        "Whether a fence is required, and what type, can depend on the system and on local rules, so check with your solar installer and the building department. We keep the fence on its own posts, separate from the racking. If it's metal, ask your installer or an electrician whether it should be bonded or grounded.",
                    ]),
                ],
                faqs=[
                    ("Will my solar array need a fence?", "It depends on your system, your animals and the local rules. Your solar installer and the building department can tell you what's required. We'll build to that."),
                    ("Can you fence the array into my pasture?", "Yes, as long as the fence is built for what's grazing there and leaves room for service and mowing."),
                    ("Can you match my existing farm fence?", "In most cases. Send us photos, and we'll tell you how close we can get."),
                ],
                related=[R_HORSE, R_GATES, R_SPLIT],
            ),
        },
    ),

    "fence-guides/garbage-bin-enclosures": dict(
        kicker="Fence Guides", photo="garbage-bin-enclosure.webp",
        photo_alt="White vinyl enclosure screening two rolling garbage carts beside a Florida home",
        blurb="How to size and place a screen for your home's trash carts.",
        sites={
            "southtampa": dict(
                name="Garbage Bin Enclosures",
                tagline="Hide the carts, keep the side yard, and still make it to the curb.",
                meta_title="Garbage Bin Enclosures in South Tampa | {brand}",
                meta="Garbage bin enclosures for South Tampa homes: sizing for City of Tampa carts, tight side yards, gate widths, materials, and checking historic district rules.",
                intro=["On a South Tampa street where the houses sit close together, trash carts are often parked in plain view. A simple enclosure tidies that up. It doesn't take much material, but a few measurements decide whether it works, or whether you end up dragging carts around it every week."],
                glance=["Measure your actual carts", "Leave room for lids to open", "Plan a clear path to the curb", "Keep meters and AC units clear", "Check historic district rules"],
                sections=[
                    ("Measure before you design", [
                        f'The City of Tampa has issued both 95-gallon and 65-gallon carts ({_link(TAMPA_CARTS, "Fox 13")}). A large rolling cart is typically around 44 to 46 inches tall, about 30 inches wide, and about 36 inches deep, though sizes vary. Measure yours with the lid closed, and again with it open. Add a few inches of clearance on each side so that carts roll out without scraping.',
                    ]),
                    ("Tight side yards and alleys", [
                        "Many South Tampa lots have narrow side yards, and some homes back up to alleys. Before you pick a spot, check that you aren't blocking a gas meter, an electrical panel, an AC unit or a gate you rely on. If the side yard is tight, a three-sided screen with no gate can do the job in less space than a full enclosure.",
                    ]),
                    ("Historic homes and street views", [
                        "If you're in a local historic district such as Hyde Park, check whether a new structure or fence needs review before you build. An enclosure that's visible from the street should look like part of the house, so we usually match the existing fence, trim color or picket style. We'll check for your address before we design.",
                    ]),
                    ("Choosing a material", [
                        "<strong>Vinyl</strong> is the easy choice, because it wipes clean and won't soak up odors. <strong>Wood</strong> matches older homes well, but it needs sealing and should sit off the wet ground. <strong>Aluminum with screening panels</strong> suits a modern home. Any of them can be built with a bit of air at the bottom, which helps it dry out.",
                    ]),
                    ("Details that make it easy to live with", [
                        "A hard surface such as pavers or a small slab keeps wheels out of the mud. Give the enclosure a gate at least as wide as your cart plus a comfortable margin. If you add a lid or roof, make sure it clears the open cart lids. Before a storm, bring carts inside the garage if you can. An enclosure is a screen, not a tie-down.",
                    ]),
                ],
                faqs=[
                    ("How big should an enclosure be for two carts?", "Plan for about 6 feet wide by 4 feet deep, then adjust for your carts and gate. We'll measure on site."),
                    ("Do I need a permit?", "It depends on what you're building and where. We check the City of Tampa and historic district requirements for your address first."),
                    ("Will it keep raccoons out?", "A closed gate and a lid can help, but open-top screens only hide the carts. Latching cart lids are the other half of the answer."),
                ],
                related=[R_VINYL, R_PRIVACY, R_GATES],
            ),
            "westchase": dict(
                name="Garbage Bin Enclosures",
                tagline="A tidy spot for your carts that keeps neighbors and your HOA happy.",
                meta_title="Garbage Bin Enclosures in Westchase | {brand}",
                meta="Trash can screens and enclosures for Westchase homes: HOA approval, matching your fence, sizing for rolling carts, placement and easy upkeep.",
                intro=["Trash carts are a common complaint in deed-restricted neighborhoods. A small screen or enclosure keeps them out of sight between collection days, and it adds a bit of polish to the side of the house. Here's how to get one right the first time."],
                glance=["Ask your HOA first", "Match your existing fence", "Size it for carts and open lids", "Keep a straight path to the street", "Choose an easy-to-clean material"],
                sections=[
                    ("Start with your HOA", [
                        "If you live in a deed-restricted community, check the guidelines before you buy anything. Many associations care about where carts sit and what can be seen from the street, and some have rules on enclosure materials, colors or placement. Send a sketch, a photo of the spot and the material with your request. Our <a href=\"hoa-fence-approval-guide.html\">HOA approval guide</a> shows you what to include.",
                    ]),
                    ("Smaller lots, smart placement", [
                        "With homes close together around Westchase, the best spot is usually beside the garage, behind the front corner of the house. That keeps the walk to the curb short. Watch out for meters, the AC unit, hose bibs and side gates, and don't crowd your neighbor's path along the property line.",
                    ]),
                    ("Make it match", [
                        "An enclosure looks best when it looks like it came with the house. If you already have a white vinyl fence, use the same panels. If your fence is wood, stain the screen to match. Low screens need only hide the carts, so they often look better than tall, boxy ones, and they cost less.",
                    ]),
                    ("Getting the size right", [
                        "A large rolling cart is typically around 30 inches wide, 36 inches deep and 44 to 46 inches tall, but measure your own with the lid open. For two carts, allow space between them and on either side. If you recycle, leave room for that as well. A few spare inches now will save you from scraping panels every week.",
                    ]),
                    ("Easy to keep clean", [
                        "Carts leak and attract bugs, so plan for washing. Vinyl hoses off easily. A paver pad or small slab keeps the spot from turning muddy, and a slight slope carries water away from the house. Leave a little air under the panels so that the area can dry out between rains.",
                    ]),
                    ("Sturdy enough for Florida", [
                        "A screen acts a bit like a sail in strong wind, so the posts need to be properly set. We build enclosures with the same care as a fence. When a storm is coming, move carts into the garage. A loose cart can do more damage than the enclosure would.",
                    ]),
                ],
                faqs=[
                    ("Will my HOA allow a trash enclosure?", "Many do, but rules differ. Ask before you build, and send a sketch. We can provide the details your request will need."),
                    ("Do I need a gate?", "Not always. A two- or three-sided screen is simpler and quicker to use. A gate gives you a neater look from every angle."),
                    ("Can you build one when you install my fence?", "Yes, and that's the easiest time, because the materials and crew are already on site."),
                ],
                related=[R_VINYL, R_HOA_GUIDE, R_DUMPSTER],
            ),
        },
    ),
}

# Guides on every site, listed on each site's /fence-guides/ hub after its own articles.
SHARED_GUIDES = [
    ("Pool Inspection Guide", "pool-fence-inspection-florida.html", "What an inspector checks on a pool barrier."),
    ("HOA Approval Guide", "hoa-fence-approval-guide.html", "What to send your HOA before you build."),
    ("Fence Care &amp; Easy Fixes", "fence-care.html", "Keep your fence in shape, and fix the small things."),
]
