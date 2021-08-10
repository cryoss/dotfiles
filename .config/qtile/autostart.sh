#!/usr/bin/env bash 

sh .screenlayout/default.sh &
festival --tts $HOME/.config/qtile/welcome_msg &
lxsession &
picom &
./home/cryoss/Pictures/styli.sh/styli.sh -s nature &
#nitrogen --restore &
/usr/bin/emacs --daemon &
volumeicon &
nm-applet &
