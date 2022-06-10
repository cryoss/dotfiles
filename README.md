##  from arch repos 
    pacman -Syu trayer alacritty dmenu texlive-most fish qalculate-gtk emacs fd exa git ripgrep thunderbird cmus locate starship
##  from aur    
    yay -S paru
    paru -S shell-color-scripts 
##  from github
##  doom-emacs
    git clone --depth 1 https://github.com/hlissner/doom-emacs ~/.emacs.d
    ~/.emacs.d/bin/doom install 
## Init Git 
    git config --global user.name "cryoss" \
    git config --global user.email n.billing@billtec.de \
    git config --global core.editor "vim" \
    git config credential.${remote}.username cryoss \ 
    git config credential.helper store
## Starship
curl -sS https://starship.rs/install.sh | sh

##  oh-my-fish
    curl -L https://get.oh-my.fish | fish 
##  pip
    pip install psutil
    pip install iwlib
##  picom jonaburg
    paru -S picom-jonaburg-git
##  for laptop 
    paru -S clight-gui-git
    
##  smb share
    //10.10.20.10/disk1 /home/cryoss/disk1 cifs username=alle,password=billing,iocharset=utf8,user,rw 0 0
    
    
##  howdy face unlock
    pacman -Syu v4l-utils
    paru -S howdy
    v4l2-ctl --list-devices
##  device to /lib/security/howdy/config.ini
   
   
## in needed /etc/pam.d/... (sudo, system-local-login ...)
   auth sufficient pam_unix.so try_first_pass likeauth nullok
   auth sufficient pam_python.so /lib/security/howdy/pam.py

## new FONTS ACTUAL ::
Comic Sans
paru -S ttf-comic-mono-git

/
