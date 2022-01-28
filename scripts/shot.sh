#!/bin/bash

maim | xclip -selection clipboard -t image/png
notify-send "Screenshot Taken"