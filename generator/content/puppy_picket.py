# -*- coding: utf-8 -*-
"""Puppy Picket Aluminum Fence page (every site). The shared copy is BASE["puppy-picket-fence"]
in new_pages.py (used as-is on Lutz); LOCAL and VARIANTS here are merged into
content.new_local.LOCAL and content.new_variants.VARIANTS by build_new.py.

Spacing figures are typical product specs (Nov 2026), not code: standard aluminum pickets
sit just under 4" apart; puppy picket sections roughly halve that along the bottom 12-18".
"""

LOCAL = {
    "lutz": dict(
        tagline="Aluminum fencing with a tighter bottom, built to keep small dogs home.",
        intro=["A standard aluminum fence keeps big dogs in but leaves gaps a puppy can walk through. Puppy picket panels close those gaps along the bottom, so the whole family, including the smallest member, can use the yard safely."],
        local=("Lake lots and open backyards", [
            "Many Lutz yards run down to a lake or a wooded edge, where an open fence keeps the view you bought the house for. Puppy picket aluminum is the way to keep that view and still keep a small dog from following a duck to the water's edge.",
        ])),
    "brooksville": dict(
        tagline="Puppy picket aluminum for Brooksville and Spring Hill homes.",
        intro=["Out here a small dog that gets loose has a lot of ground to cover, and not all of it is safe. Puppy picket aluminum gives you a fenced area by the house where little dogs can be outside without you watching every move."],
        local=("A safe yard inside the bigger property", [
            "On acreage, you don't always need to fence the whole parcel to keep pets safe. A puppy picket enclosure off the back door or around the pool area gives small dogs a secure space close to the house, while the rest of the land stays open.",
        ])),
    "northtampa": dict(
        tagline="Puppy picket aluminum for New Tampa and North Tampa yards.",
        intro=["In neighborhoods built around ponds and preserves, plenty of homeowners want an open fence. Puppy picket aluminum keeps that open look, with extra pickets near the ground so small dogs stay on your side of it."],
        local=("Ponds, preserves and HOA rules", [
            "Many North Tampa communities favor or require open aluminum fencing along ponds and preserves. Puppy picket panels usually fit within those guidelines because they look like the same fence, just with more pickets down low. We'll confirm with your HOA before we order anything.",
        ])),
    "carrollwood": dict(
        tagline="Puppy picket aluminum for Carrollwood and Northdale homes.",
        intro=["If your older fence has gaps your new puppy has already found, puppy picket aluminum is a clean way to start over. It's an open fence with a tighter bottom, made for small dogs."],
        local=("Replacing an aging fence for a new dog", [
            "Many Carrollwood families are replacing a tired wood fence at the same time they bring home a new dog. Switching to puppy picket aluminum means no more rotting boards for a dog to push past. We set posts around mature oak roots instead of cutting through them.",
        ])),
    "westchase": dict(
        tagline="Puppy picket aluminum that fits Westchase neighborhoods.",
        intro=["Black aluminum is one of the most common fences in Westchase, and puppy picket panels make it work for small dogs too. From the street, it looks like the neighbors' fences, but the gaps along the bottom are much tighter."],
        local=("Matching the neighborhood", [
            "Because puppy picket panels match standard aluminum in style and color, they usually blend in with the fences around them, which helps when your HOA reviews the application. On corner lots, they keep small dogs safe on the busy side without blocking the view.",
        ])),
    "southtampa": dict(
        tagline="Puppy picket aluminum for South Tampa homes and courtyards.",
        intro=["South Tampa yards are often small, so every foot of fence counts. Puppy picket aluminum gives a little dog a safe front garden or courtyard while keeping the house in view."],
        local=("Front gardens and courtyards", [
            "Plenty of South Tampa homes use a low front fence to define the garden, and that's exactly where small dogs slip out. A low puppy picket fence keeps the classic look of an iron fence while closing the gaps. In a historic district, we check what's allowed for your address first.",
        ])),
    "starkey": dict(
        tagline="Puppy picket aluminum for Starkey Ranch, Odessa and Trinity.",
        intro=["New home, new puppy: it's a common combination around Starkey Ranch. Puppy picket aluminum gives the puppy a safe yard from day one, and it still suits the dog when it's full grown."],
        local=("Preserve views and new-build lots", [
            "Many Starkey Ranch homes back up to preserves and trails, and the open look of aluminum keeps those views. Puppy picket panels stop small dogs from slipping through to follow the wildlife, and they meet the open-fence style many local HOAs prefer.",
        ])),
}

VARIANTS = {
    "brooksville": dict(
        glance=["Tight gaps down low", "Pool areas and back-door yards", "Rust-free in rain and sun", "Matching gates", "Add a dig guard for diggers"],
        sections=[
            ("What makes it different", ["On a regular aluminum fence, pickets sit almost 4 inches apart. A puppy picket panel adds short pickets in between along the bottom, usually the lowest foot or foot and a half, which brings that gap down to roughly 2 inches. Above that, the fence looks and works like any other aluminum fence."]),
            ("Who it's for", ["It's made for toy breeds, small terriers and puppies. Bigger dogs don't need it, but it doesn't hurt them either. It won't hold a cat that wants to climb, so if you're fencing for cats, tell us, because that's a different conversation."]),
            ("Finishing the job", ["Order matching puppy picket gates, because the gate is where most dogs get out. Add self-closing hinges, and if your dog digs in our sandy soil, a buried wire dig guard along the bottom."]),
        ],
        faqs=[("Can you add puppy pickets to my existing aluminum fence?", "Sometimes. It depends on the style of your fence, so send us a photo."),
              ("Will it hold a large dog?", "Yes, as long as the height is right. The extra pickets are only for small dogs."),
              ("Can it be part of a pool barrier?", "Aluminum pool fences are common. We build pool barriers to Florida's rules, and we'll tell you if a design works.")],
    ),
    "northtampa": dict(
        glance=["Same open look as aluminum", "Gaps about half as wide at the bottom", "Usually HOA-friendly", "Matching self-closing gates", "No rust, no painting"],
        sections=[
            ("How puppy picket works", ["Standard aluminum has pickets just under 4 inches apart. That's fine for most dogs, but small breeds and puppies can squeeze through. Puppy picket panels add a short picket between each pair at the bottom, so the gaps there are about half as wide."]),
            ("Is it right for your dog?", ["If your dog weighs under 20 pounds, or you're bringing home a puppy that will grow, it's worth the upgrade. If you have both a small and a large dog, puppy picket covers the small one, and height covers the big one. For climbers and jumpers, a solid fence may suit better."]),
            ("The rest of the fence", ["Gates should be puppy picket too, and fitted with self-closing hinges and a latch that catches every time. Keep the bottom close to the ground, and if your dog digs, add a wire dig guard."]),
        ],
        faqs=[("Does puppy picket cost more?", "Yes, a little more than standard aluminum, because each panel has extra pickets. We'll price both so you can compare."),
              ("Will my HOA approve it?", "Usually. It looks like standard aluminum from a distance. We'll prepare the application."),
              ("Does it work for cats?", "Not really. Cats can climb aluminum. It's made for small dogs.")],
    ),
    "carrollwood": dict(
        glance=["Built for small dogs and puppies", "No boards to rot or push loose", "Tighter gaps along the bottom", "Gates that match and self-close", "Routed around tree roots"],
        sections=[
            ("A tighter bottom on a familiar fence", ["Puppy picket is aluminum fencing with extra short pickets along the lowest 12 to 18 inches of each panel. Instead of a gap of nearly 4 inches, a small dog faces a gap of around 2 inches. Higher up, it's the same open fence."]),
            ("Why aluminum beats patching old wood", ["Older wood fences develop gaps at the ground, loose boards and soft spots that small dogs find quickly. Aluminum doesn't rot or warp, and it doesn't lose pickets, so the gaps stay the size they were on install day."]),
            ("Gates and digging", ["Make the gate puppy picket too, and add self-closing hinges if the kids sometimes leave it open. If your dog is a digger, a wire dig guard along the bottom finishes the job."]),
        ],
        faqs=[("Can you replace just the back section?", "Yes. Many families fence the backyard first and leave the front for later."),
              ("How long does aluminum last?", "Aluminum doesn't rust or rot, so it holds up very well in Florida with occasional washing."),
              ("Is it good for big dogs too?", "Yes. Choose the height for your biggest dog, and the puppy pickets cover the smallest.")],
    ),
    "westchase": dict(
        glance=["Looks like standard black aluminum", "Small-dog gaps closed at the bottom", "Good fit for HOA review", "Corner-lot friendly", "Low upkeep"],
        sections=[
            ("The difference is at the bottom", ["Each puppy picket panel carries extra short pickets near the ground, usually the bottom foot or so. Those pickets cut the gap from nearly 4 inches to about 2, which is enough to keep most small dogs and puppies in."]),
            ("Picking the right height", ["A 4-foot fence suits most small and medium dogs. If you also have a large or athletic dog, go taller. Puppy picket deals with squeezing, and height deals with jumping."]),
            ("Gates are part of the plan", ["Order matching puppy picket gates with self-closing hinges and a reliable latch. With kids, landscapers and pool service in and out, the gate is where most dogs get out."]),
        ],
        faqs=[("Will it look different from my neighbors' fences?", "Barely. Up close you'll see the extra pickets at the bottom, but the style and color match."),
              ("What color should I choose?", "Black is the most common choice around Westchase. Check your HOA's approved colors first."),
              ("Can you match my existing aluminum fence?", "Often. Send us a photo, and we'll check styles.")],
    ),
    "southtampa": dict(
        glance=["Classic iron-fence look", "Closes the gaps small dogs use", "Works on low front fences", "Rust-free near the bay", "Historic-district checks first"],
        sections=[
            ("Small gaps, same style", ["Aluminum pickets are usually set just under 4 inches apart. Puppy picket panels add a short picket between them across the bottom of the panel, so a toy breed or puppy faces gaps closer to 2 inches. From the sidewalk it reads as a classic metal fence."]),
            ("Good near salt air", ["Aluminum doesn't rust like steel, which helps near the bay. Its powder-coated finish only needs a rinse now and then to wash off salt and pollen."]),
            ("Gates on tight lots", ["On narrow South Tampa lots, the gate is often a few steps from the sidewalk. A self-closing hinge and a dependable latch matter even more there. We'll make the gate puppy picket to match the fence."]),
        ],
        faqs=[("Can a front-yard fence be puppy picket?", "Yes. Many owners use a low puppy picket fence to keep a small dog in the front garden. Height rules for front yards depend on your address."),
              ("Is aluminum allowed in historic districts?", "It depends on the district and the design. We check for your address before we design."),
              ("Will it keep a cat in?", "No. Cats can climb it. It's made for small dogs.")],
    ),
    "starkey": dict(
        glance=["Safe for puppies from day one", "Keeps preserve views open", "Fits open-fence HOA styles", "Matching self-closing gates", "Lasts as the dog grows"],
        sections=[
            ("What you're getting", ["Puppy picket aluminum adds a row of short pickets between the regular ones along the bottom of each panel, usually the lowest 12 to 18 inches. The gaps there drop from almost 4 inches to about 2, which stops most puppies and small dogs from squeezing out."]),
            ("Planning for the grown-up dog", ["A puppy won't stay small forever, so choose the height for the adult dog. If you're getting a large breed, the puppy pickets keep it in early on and the height keeps it in later."]),
            ("Gates, gaps and diggers", ["Puppy picket gates with self-closing hinges finish the fence. Keep the bottom tight to the ground, and add a wire dig guard if your puppy starts tunneling toward the preserve."]),
        ],
        faqs=[("Will my HOA allow it?", "Many Starkey Ranch-area HOAs prefer open aluminum, and puppy picket usually fits. We'll prepare the application."),
              ("Is it worth it for a big breed?", "For a puppy, yes. A big-breed puppy can slip through standard gaps for its first few months."),
              ("How long does installation take?", "Most backyard fences take a day or two once the materials arrive and approvals are in.")],
    ),
}
