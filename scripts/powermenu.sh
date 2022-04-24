#!/usr/bin/env bash

uptime=$(uptime -p | sed -e 's/up //g')
rofi_command="rofi -theme ~/.config/rofi/power.rasi"

# Options
bluetooth="Bluetooth"
desktop="ModernFamily"
update="Update"
shutdown="Shutdown"
reboot="Restart"
suspend="Suspend"

# Variable passed to rofi
options="$bluetooth\n$desktop\n$update\n$reboot\n$shutdown"

chosen="$(echo -e "$options" | $rofi_command -p "Uptime: $uptime" -dmenu -selected-row 0)"
case $chosen in
    $shutdown)
		systemctl poweroff
        ;;
    $reboot)
		systemctl reboot
        ;;
    $suspend)
		amixer set Master mute
		systemctl suspend
        ;;
    $update)
    alacritty -e paru -Syu --ignore fluent-gtk-theme-git
        ;;
    $desktop)
    thunar Desktop/Modern\ Family\ 2009\ Season\ 8/
        ;;
    $bluetooth)
    alacritty -e ./blue.sh
        ;;
esac
