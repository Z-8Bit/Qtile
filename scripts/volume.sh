#!/bin/bash

# You can call this script like this:
# $ ./volume.sh up
# $ ./volume.sh down

DIR="$HOME/.config/dunst"

function is_mute {
  pamixer --get-mute
}

function send_notification {
  volume=$(pamixer --get-volume)
  bar=$(seq -s "━" 0 $(($volume / 5)) | sed 's/[0-9]//g')
  if [ '$(pamixer --get-mute)' = "true" ]; then
    icon_name="$DIR/icons/volume-muted.svg"
    bar=""
    #dunstify " Volume " "$volume" -i $icon_name -r 5555 -u normal
  else
    if [  "$volume" -lt "10" ]; then
      icon_name="$DIR/icons/volume-low.svg"
    #dunstify " Volume " "$volume" -i $icon_name -r 5555 -u normal
    else
      if [ "$volume" -lt "30" ]; then
        icon_name="$DIR/icons/volume-low.svg"
      else
        if [ "$volume" -lt "70" ]; then
          icon_name="$DIR/icons/volume-medium.svg"
        else
          icon_name="$DIR/icons/volume-high.svg"
        fi
      fi
    fi
  fi
  # Send the notification
  #dunstify -a "changevolume" -u low -r "9993" -h int:value:"$volume" -i $icon_name "Volume: ${volume}%" -t 2000
  dunstify "Volume : $volume" "$bar" -i $icon_name -r 5555 -u normal
}

case $1 in
  up)
    pamixer -u
    pamixer -i 5 --allow-boost
    send_notification
    ;;
  down)
    pamixer -u
    pamixer -d 5 --allow-boost
    send_notification
    ;;
  mute)
    # Toggle mute
    pactl set-sink-mute @DEFAULT_SINK@  toggle > /dev/null
    if is_mute ; then
      icon_name="$DIR/icons/volume-muted.svg"
      dunstify "Muted" -i $icon_name -r 5555 -u normal
    else
      send_notification
    fi
    ;;
esac
