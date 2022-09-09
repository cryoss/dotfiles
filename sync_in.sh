#!/usr/bin/env bash

# mkdir .config
cp -rf ~/.config/fish .config/
cp -rf ~/.config/picom .config/
cp -rf ~/.config/rofi .config/
cp -rf ~/.config/alacritty .config/
cp -rf ~/.config/qutebrowser .config/
cp -rf ~/.config/starship.toml .config/starship.toml

cp -rf ~/.config/qtile/config.py .config/qtile/
cp -rf ~/.config/qtile/autostart.sh .config/qtile/
cp -rf ~/.config/qtile/onreload.sh .config/qtile/
cp -rf ~/.config/qtile/showkeys.sh .config/qtile/

cp -rf ~/.doom.d/* .doom.d/
