#!/usr/bin/env bash 

mount ~/disk1
sh .screenlayout/default1.sh &
sh .screenlayout/default.sh &
festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
#nitrogen --restore &
#sh /home/cryoss/Pictures/styli.sh/styli.sh -s nature &
feh --randomize --bg-fill ~/Pictures/dWallpaper/ &
/usr/bin/emacs --daemon &
flameshot &
thunderbird &
volumeicon &
nm-applet &
xfce4-power-manager --daemon &
pulse-audio --start &
kdeconnect-indicator &
