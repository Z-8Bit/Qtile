#!/bin/bash

maim --select | xclip -selection clipboard -t image/png
notify-send "Title" "Clipped"
