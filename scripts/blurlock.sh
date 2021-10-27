#!/bin/bash

# CREATING WORKING DIRECTORY
mkdir -p ~/.image 

# TAKING AND BLURRING SCREENSHOT
import -window root ~/.image/image.png
convert ~/.image/image.png -channel RGBA -blur 0x8 ~/.image/image_blurred.png

# LOCKING SCREEN
i3lock -i ~/.image/image_blurred.png

# CLEANING UP
rm -rf ~/.image/image.png
rm -rf ~/.image/image_blurred.png