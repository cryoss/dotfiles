#!/usr/bin/env bash
root=$(pwd)
packages='trayer alacritty dmenu rofi texlive-most fish qalculate-gtk emacs fd exa git ripgrep thunderbird cmus locate'
echo 'Working dir =' $root
if [ -f "/etc/arch-release" ]; then
    echo 'distro is arch'

    sudo pacman -Syyyu $packages
# picom jonaburg
    paru -S picom-jonaburg-git
# for laptop
    paru -S clight-gui-git
else
    echo 'distro is not arch'
fi

#FONTS

sudo mkdir /usr/share/fonts/comic-mono
sudo cp .fonts/* /usr/share/fonts/comic-mono/


#SHELL and Stuff

curl -sS https://starship.rs/install.sh | sh
curl -L https://get.oh-my.fish | fish

cp -rf .config/fish/* ~/.config/fish/
cp -rf .config/picom/* ~/.config/picom/
cp -rf .config/rofi/* ~/.config/rofi/
cp -rf .config/alacritty/* ~/.config/alacritty/
cp -rf .config/starship.toml ~/.config/


#DOOM

git clone --depth 1 https://github.com/hlissner/doom-emacs ~/.emacs.d

bash ~/.emacs.d/bin/doom install
cp -rf .doomd/* ~/.doomd/
bash ~/.emacs.d/bin/doom sync
bash ~/.emacs.d/bin/doom upgrade


#Init Git
git config --global user.name "cryoss"
git config --global user.email n.billing@billtec.de
git config --global core.editor "vim"
git config --global credential.${remote}.username cryoss
git config --global credential.helper store

## pip
pip3 install psutil
pip3 install iwlib

##  smb share
# //10.10.20.10/disk1 /home/cryoss/disk1 cifs username=alle,password=billing,iocharset=utf8,user,rw 0 0
