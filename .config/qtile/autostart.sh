#!/usr/bin/env bash 

sh .screenlayout/default1.sh &
sh .screenlayout/default.sh &
festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
#nitrogen --restore &
#sh /home/cryoss/Pictures/styli.sh/styli.sh -s nature &
feh --randomize --bg-fill ~/Pictures/dWallpaper/ &
/usr/bin/emacs --daemon &
volumeicon &
nm-applet &
xfce4-power-manager &
