#!/usr/bin/env bash

uptime=$(uptime -p | sed -e 's/up //g')
rofi_command="rofi -theme ~/.config/rofi/power.rasi"

# Options
picom="Picom"
bluetooth="Bluetooth"
desktop="Polybar"
update="Update"
shutdown="Shutdown"
reboot="Reboot"
suspend="Suspend"

# Variable passed to rofi
options="$desktop\n$picom\n$shutdown\n$reboot\n$bluetooth\n$update"

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
    killall polybar
        ;;
    $picom)
    killall picom
    	;;
    $bluetooth)
    alacritty -e ./blue.sh
        ;;
esac
