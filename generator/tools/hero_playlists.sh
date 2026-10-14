# clip name -> file in $C ; existing: <site>-1.mp4 (hero), <site>-2w.mp4 (evening)
build() { out=$1; shift; args=(); for c in "$@"; do args+=("$C/$c.mp4"); done; "$C/hero_loop" "$G/media/$out-hero.mp4" "${args[@]}"; }
build lutz        lutz-1 p-whitevinyl p-shadowbox p-lattice p-pond lutz-2w
build brooksville brooksville-1 p-splitrail p-pasture p-chainlink p-shadowbox brooksville-2w
build northtampa  northtampa-1 p-pond p-grayvinyl p-puppypicket p-lattice northtampa-2w
build carrollwood p-cwclean p-tanvinyl p-chainlink p-bungalowpicket p-shadowbox carrollwood-2w
build westchase   westchase-1 p-composite p-slatdusk p-grayvinyl p-pond westchase-2w
build southtampa  southtampa-1 p-picket p-bronzegate p-bungalowpicket p-lattice southtampa-2w
build starkey     starkey-1 p-puppypicket p-grayvinyl p-pond p-chainlink starkey-2w
