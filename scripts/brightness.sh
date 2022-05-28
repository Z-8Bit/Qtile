#!/usr/bin/env bash

# You can call this script like this:
# $ ./brightness.sh up
# $ ./brightness.sh down

DIR="$HOME/.config/dunst"

function get_brightness {
  light -G | cut -d '.' -f 1
}

function send_notification {
  icon="$DIR/icons/brightness.svg"
  brightness=$(get_brightness)
  # Make the bar with the special character ─ (it's not dash -)
  # https://en.wikipedia.org/wiki/Box-drawing_character
  bar=$(seq -s "━" 0 $((brightness / 5)) | sed 's/[0-9]//g')
  # Send the notification
  dunstify "Brightness : $brightness" "$bar" -i $icon -r 5555 -u normal
}

case $1 in
  up)
    # increase the backlight by 5%
    #backlight_control +4
    sudo brillo -A 2 -q
    send_notification
    ;;
  down)
    # decrease the backlight by 5%
    #backlight_control -4
    sudo brillo -U 2 -q
    send_notification
    ;;
    esac
