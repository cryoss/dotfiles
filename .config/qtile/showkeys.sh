#!/usr/bin/env bash
# set -euo pipefail

# sed -n '/#START_KEYS/,/#END_KEYS/p' ~/.config/qtile/config.py | \
#     grep -e 'Key(' -e 'desc' |\
# yad --text-info --back=#282c34 --fore=#46d9ff --geometry=1200x800 --no-buttons --undecorated --borders=0 --alpha=0

python3 ~/.config/qtile/src/qtile/scripts/gen-keybinding-img -o ~/.config/qtile/shortcuts
feh --scale-down ~/.config/qtile/shortcuts/
