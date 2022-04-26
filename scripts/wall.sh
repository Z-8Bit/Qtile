#!/bin/bash

cd /etc/lightdm

background_home=/home/zishaan/Pictures/Wallpapers

# Shuffle backgrounds and pick one
background=$(ls $background_home | shuf -n 1)

# Replace current LightDM greeter background
cp $background_home/$background background.jpg
