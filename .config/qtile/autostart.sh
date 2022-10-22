#!/usr/bin/env bash 

if $DEVICE=="desktop"
then
    sh .screenlayout/default1.sh &
    sh .screenlayout/default.sh &
fi

if $DEVICE=="laptop"
then
    touchegg &
fi
mount ~/data
flameshot &
thunderbird &
pavucontrol &
volumeicon &
nm-applet &
xfce4-power-manager --daemon &
feh --randomize --bg-fill ~/Pictures/dWallpaper/ &
/usr/bin/emacs --daemon &
picom &
syncthing &
