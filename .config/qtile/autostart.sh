#!/usr/bin/env bash 

sh .screenlayout/default.sh &
sh .screenlayout/default.sh &
festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
#sh /home/cryoss/Pictures/styli.sh/styli.sh -s nature &
#nitrogen --restore &
feh --randomize --bg-fill ~/Pictures/dWallpaper/ &
/usr/bin/emacs --daemon &
volumeicon &
nm-applet &
xfce4-power-manager &
