#!/usr/bin/env bash 

mount ~/disk1
sh .screenlayout/default1.sh &
sh .screenlayout/default.sh &
picom &
#nitrogen --restore &
#sh /home/cryoss/Pictures/styli.sh/styli.sh -s nature &
feh --randomize --bg-fill ~/Pictures/dWallpaper/ &
/usr/bin/emacs --daemon &
flameshot &
thunderbird &
volumeicon &
pavucontrol &
nm-applet &
xfce4-power-manager --daemon &
kdeconnect-indicator &
arandr &
