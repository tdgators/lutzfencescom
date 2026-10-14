# Hero video sources

Each `<site>-hero.mp4` is a ~21s loop built with `tools/hero_loop.swift` from two 5s Story Hero
clips (Kling 2.5 Turbo Pro, image-to-video): clip 1 starts from `<site>-hero.webp`, clip 2 from
`<site>-dusk.webp` (North Tampa: its pool dusk image). Each clip plays forward then in reverse,
with crossfades between scenes and at the loop point, at 0.9x speed.

Rebuild (clip 1 compressed with `avconvert -p Preset960x540`, clip 2 with `Preset1280x720`):

    swiftc -O -o /tmp/hero_loop tools/hero_loop.swift
    /tmp/hero_loop media/<site>-hero.mp4 clip1.mp4 clip2.mp4

All imagery here is AI-generated scenery. Don't present it as photos of real installs.
