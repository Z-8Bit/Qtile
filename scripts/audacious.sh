#!/usr/bin/env bash

song=$(audtool --current-song)
rofi_command="rofi -theme ~/.config/rofi/audacious.rasi"

# Options
pause="Play/Pause"
next="Next"
back="Back"
jump="Jump"
close="Quit"

# Variable passed to rofi
options="$pause\n$jump\n$next\n$back\n$close"

chosen="$(echo -e "$options" | $rofi_command -p "$song" -dmenu -selected-row 0)"
case $chosen in
    $pause)
		audacious -u
        ;;
    $next)
		audacious -f
        ;;
    $back)
    audacious -r
        ;;
    $jump)
	audacious -j
        ;;
    $close)
    audtool --shutdown
        ;;
esac
