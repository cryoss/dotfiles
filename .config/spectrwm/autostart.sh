#!/usr/bin/env bash 

bash .screenlayout/default1.sh &
bash ~/.screenlayout/default.sh &
lxsession &
picom &
#sh /home/cryoss/Pictures/styli.sh/styli.sh -s nature &
#nitrogen --restore &
feh --randomize --bg-fill ~/Pictures/dWallpaper/ &
/usr/bin/emacs --daemon &
volumeicon &
nm-applet &
xfce4-power-manager &
mailspring &
#bash ~/.config/polybar/polybar.sh
