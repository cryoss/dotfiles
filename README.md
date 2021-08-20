##  from arch repos 
    pacman -Syu xmonad xmonad-contrib trayer dolphin alacritty ranger dmenu texlive-most fish nvim qalculate-gtk mypy emacs fd git okular ripgrep
##  from aur    
    yay -S paru
    paru -S shell-color-scripts 
##  from github
##  doom-emacs
    git clone --depth 1 https://github.com/hlissner/doom-emacs ~/.emacs.d
    ~/.emacs.d/bin/doom install 
    
##  oh-my-fish
    curl -L https://get.oh-my.fish | fish 
##  pip
    pip install psutil
    pip install iwlib
##  picom jonaburg
    paru -S picom-jonaburg-git
