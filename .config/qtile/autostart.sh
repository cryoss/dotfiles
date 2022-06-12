#!/usr/bin/env bash 
if $DEVICE=="laptop"
then
    #mount ~/disk1
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
    xfce4-power-manager &
    touchegg &
    kdeconnect-indicator &
fi
if $DEVICE=="desktop"
then
    #mount ~/disk1
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
fi
