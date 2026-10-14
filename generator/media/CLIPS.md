# Hero video sources

Each `<site>-hero.mp4` is a ~28s loop built with `tools/hero_loop.swift` from six 5s Story Hero
clips (Kling 2.5 Turbo Pro, image-to-video), played forward at 0.9x with ~0.8s crossfades
between clips and back into the start. Each site opens on its own hero scene and closes on its
own evening scene; the four clips in between come from a shared pool of fence pans (wood
shadowbox, chain link, picket, aluminum, lattice vinyl, gray vinyl, composite, three-rail, etc.).
The per-site clip order is in `tools/hero_playlists.sh`.

Clips are compressed with `avconvert -p Preset1280x720` (the first clip of each loop with
`Preset960x540`, which sets the output size) before building. Source clips live in Story Hero.

All imagery here is AI-generated scenery. Don't present it as photos of real installs.
