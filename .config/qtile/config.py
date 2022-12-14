# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen, ScratchPad, DropDown
from libqtile import layout, bar, widget, hook
from libqtile.command import lazy
from typing import List  # noqa: F401
from libqtile.lazy import LazyCall

from libqtile.log_utils import logger


type_of_dev = "laptop"

def to_next_group(qtile):
     next_group_name = qtile.current_group.get_next_group().name
     qtile.current_window.togroup(next_group_name, switch_group=True)

def to_prev_group(qtile):
     prev_group_name = qtile.current_group.get_previous_group().name
     qtile.current_window.togroup(prev_group_name, switch_group=True)

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
calendar = "thunderbird"
# browser = "firefox"
browser = "qutebrowser"
files = "dolphin"
launcher = "/home/cryoss/.config/rofi/bin/launcher_misc"
#START_KEYS
keys = [
         Key([mod, "shift"], "s",
             lazy.spawn("bash /home/cryoss/.config/qtile/showkeys.sh"),
             desc='Show keys'
             ),
         Key([mod], "Return",
             lazy.spawn(myTerm+" -e fish"),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn("bash "+launcher),
             desc='Run Launcher'
             ),
         Key([mod, "shift"], "l",
             lazy.spawn("looking-glass-client -C /home/cryoss/VM/lg.rc"),
             desc='looking-glass-client'
             ),
         # Key([mod, "shift"], "m",
         #     lazy.spawn("thunderbird"),
         #     desc='thunderbird'
         #     ),
         Key([mod, "shift"], "c",
             lazy.spawn("qalculate-gtk"),
             desc='qalculate'
             ),
         Key([mod], "d",
             lazy.spawn(files),
             desc='files'
             ),
         Key([mod], "space",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "w",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "F12",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod, "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         Key([mod, "control"], "Delete",
             lazy.spawn(myTerm+" -e bpytop"),
             desc='bpytop sys tool'
             ),
         Key([mod, "control"], "s",
             lazy.spawn("flameshot gui"),
             desc='flameshot'
             ),
####
##### Switch focus to specific monitor (out of three)
#####
#####
#####
         Key([mod], "Up",
             lazy.next_screen(),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "Down",
             lazy.prev_screen(),
             desc='Keyboard focus to monitor 2'
             ),
######## Window controls
########
########
########
         Key([mod], "Right",
             lazy.screen.next_group(),
             desc='Left Group'
             ),
         Key([mod, "shift"], "o",
             lazy.spawn("setxkbmap -model pc104 -layout de"),
             desc='de layout'
             ),
         Key([mod, "shift"], "p",
             lazy.spawn("setxkbmap -model pc104 -layout us"),
             desc='us layout'
             ),
         Key([mod], "Left",
             lazy.screen.prev_group(),
             desc='Right Group'
             ),
         Key([mod, "shift"], "Right",
             lazy.function(to_next_group),
             desc='Move window to next group'
             ),
         Key([mod, "shift"], "Left",
             lazy.function(to_prev_group),
             desc='Move window to prev group'
             ),
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             # lazy.layout.shrink()
             lazy.layout.grow_left(),
             # lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             # lazy.layout.grow(),
             lazy.layout.grow_right(),
             # lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         # Key([mod], "m",
         #     lazy.layout.maximize(),
         #     desc='toggle window between minimum and maximum sizes'
         #     ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),

     ### Volume Control

         Key([mod], "Page_Up",
             lazy.spawn("pactl -- set-sink-volume 0 +5%"),
             lazy.spawn("pactl -- set-sink-volume 1 +5%"),
             lazy.spawn("pactl -- set-sink-volume 2 +5%"),
             desc='Vol +'
             ),
         Key([mod], "Page_Down",
             lazy.spawn("pactl -- set-sink-volume 0 -5%"),
             lazy.spawn("pactl -- set-sink-volume 1 -5%"),
             lazy.spawn("pactl -- set-sink-volume 2 -5%"),
             desc='Vol -'
             ),
         Key([mod, "shift"], "F3",
             lazy.spawn("pactl -- set-sink-volume 0 +5%"),
             lazy.spawn("pactl -- set-sink-volume 1 +5%"),
             lazy.spawn("pactl -- set-sink-volume 2 +5%"),
             desc='Vol +'
             ),
         Key([mod, "shift"], "F2",
             lazy.spawn("pactl -- set-sink-volume 0 -5%"),
             lazy.spawn("pactl -- set-sink-volume 1 -5%"),
             lazy.spawn("pactl -- set-sink-volume 2 -5%"),
             desc='Vol -'
             ),

         ### Stack controls

         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             lazy.layout.swap_column_left(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "Tab",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),

     ### Groups

         Key([mod], '1',
             lazy.group['1'].toscreen(),
             desc="switch to group {}".format('1')
             ),
         Key([mod], '2',
             lazy.group['2'].toscreen(),
             desc="switch to group {}".format('2')
             ),
         Key([mod], '3',
             lazy.group['3'].toscreen(),
             desc="switch to group {}".format('3')
             ),
         Key([mod], '4',
             lazy.group['4'].toscreen(),
             desc="switch to group {}".format('4')
             ),
         Key([mod], '5',
             lazy.group['5'].toscreen(),
             desc="switch to group {}".format('5')
             ),
         Key([mod], '6',
             lazy.group['6'].toscreen(),
             desc="switch to group {}".format('6')
             ),
         Key([mod], '7',
             lazy.group['7'].toscreen(),
             desc="switch to group {}".format('7')
             ),
         Key([mod], '8',
             lazy.group['8'].toscreen(),
             desc="switch to group {}".format('8')
             ),
         Key([mod], 'v',
             lazy.group['vid'].toscreen(),
             desc="switch to group {}".format('vid')
             ),
         Key([mod], 'm',
             lazy.group['mail'].toscreen(),
             desc="switch to group {}".format('mail')
             ),

### Window To Group
         Key([mod, "shift"], '1', lazy.window.togroup('1', switch_group=True),
             lazy.group['1'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '2', lazy.window.togroup('2', switch_group=True),
             lazy.group['2'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '3', lazy.window.togroup('3', switch_group=True),
             lazy.group['3'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '4', lazy.window.togroup('4', switch_group=True),
             lazy.group['4'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '5', lazy.window.togroup('5', switch_group=True),
             lazy.group['5'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '6', lazy.window.togroup('6', switch_group=True),
             lazy.group['6'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '7', lazy.window.togroup('7', switch_group=True),
             lazy.group['7'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], '8', lazy.window.togroup('8', switch_group=True),
             lazy.group['8'].toscreen(),
             desc="switch to group"
             ),
         Key([mod, "shift"], 'm', lazy.window.togroup('vid', switch_group=True),
             lazy.group['vid'].toscreen(),
             desc="switch to group"
             ),

         KeyChord(["control"], "b",[
             Key([], "b",
                 # lazy.spawn(browser+" --new-window"),
                 lazy.spawn(browser),
                 desc="Launch browser emby"
                 ),
             Key([], "e",
                 lazy.spawn(myTerm+" -e cmus"),
                 desc="Launch cmus"
                 ),
             # Key([], "y",
             #     lazy.spawn(browser+" --new-window https://youtube.com"),
             #     desc="Launch browser emby"
             #     )
         ]),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         KeyChord(["control"],"e", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Launch Emacs'
                 )
         ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         KeyChord([mod], "p", [
             Key([], "k",
                 lazy.spawn("./dmscripts/scripts/dm-kill"),
                 desc='Kill processes via dmenu'
                 ),
             Key([], "p",
                 lazy.spawn("bash /home/cryoss/.config/rofi/applets/menu/battery.sh"),
                 desc='Powermenu'
                 ),
             Key([], "q",
                 lazy.spawn("bash /home/cryoss/.config/rofi/applets/menu/powermenu.sh"),
                 desc='A logout menu'
                 ),
             Key([], "o",
                 lazy.spawn("./dmscripts/scripts/dm-bookman"),
                 desc='Search your qutebrowser bookmarks and quickmarks'
                 ),
              Key([], "a",
                 lazy.group['scratchpad'].dropdown_toggle('audio'),
                 desc='audioMixer'
                 )
         ])

]

#END_KEYS

groups = [
     Group("1"),
     Group("2"),
     Group("3"),
     Group("4"),
     Group("5"),
     Group("6"),
     Group("7"),
     Group("8"),
     Group("vid"),
     Group("mail", matches=[Match(wm_class=["Mail"])]),
     # Group("sys", matches=[Match(wm_class=["pavucontrol", "arandr"])]),
     ScratchPad("scratchpad", [
          # define a drop down terminal.
          # it is placed in the upper third of screen by default.
          # DropDown("audio", myTerm+" -e fish", opacity=0.8)])
          DropDown("audio", 'pavucontrol', opacity=0.95)])

]

#
layout_theme = {"border_width": 3,
               "margin": 1,
               "border_focus": "#12e038",
               "border_normal": "1D2330"
               }

layouts = [
    # layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    layout.Columns(num_columns=4,**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Zoomy(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    # layout.Stack(num_stacks=3),
    # layout.TreeTab(
    #     font = "Ubuntu",
    #     fontsize = 10,
    #     sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #     section_fontsize = 10,
    #     border_width = 2,
    #     bg_color = "1c1f24",
    #     active_bg = "c678dd",
    #     active_fg = "000000",
    #     inactive_bg = "a9a1e1",
    #     inactive_fg = "1c1f24",
    #     padding_left = 0,
    #     padding_x = 0,
    #     padding_y = 5,
    #     section_top = 10,
    #     section_bottom = 20,
    #     level_shift = 8,
    #     vspace = 3,
    #     panel_width = 200
    #     ),
    # layout.Floating(**layout_theme)
]

colors = ["#282c34", #0 panel background
          "#3d3f4b", #1 background for current screen tab
          "#3498db", #2backround active screen
          "#ff5555", #3 border line color for current tab
          "#2e4053", #4 border line color for 'other tabs' and color for 'odd widgets'
          "#2f4735", #5 color for the 'even widgets'
          "#9ea9ba", #6 main text colour
          "#454649", #7 backround for inactive screens
          "#8574b5", #8 widget text colour
          "#17202a", #9
          "#6b86b0", #10
          "#51afef", #11
          "#98be65", #12
          "#12e038", #13
          "#1D2330" , #14
          "#2b6917"]  #15


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Comic Mono",
    fontsize = 18,
    padding = 0,
    background=colors[8]
)
extension_defaults = widget_defaults.copy()

if type_of_dev == "desktop":

     def init_widgets_list():
          widgets_list = [
                    widget.Sep( #1
                              linewidth = 0,
                              padding = 6,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.Image( #2
                              filename = "~/.config/qtile/icons/python-white.png",
                              scale = "False",
                              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                              ),
                    widget.Sep( #3
                              linewidth = 0,
                              padding = 6,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.GroupBox( #4
                              font = "Comic Mono",
                              # font = "Fraktur",
                              fontsize = 25,
                              margin_y = 0,
                              margin_x = 0,
                              padding_y = 0 ,
                              padding_x = 7,
                              borderwidth = 1,
                              active = colors[12],
                              inactive = colors[7],
                              rounded = True,
                              highlight_color = colors[14],
                              highlight_method = "border",
                              this_current_screen_border = colors[13],
                              this_screen_border = colors [1],
                              other_current_screen_border = colors[15],
                              other_screen_border = colors[15],
                              foreground = colors[12],
                              background = colors[0]
                              ),
                    widget.Prompt( #5
                              prompt = prompt,
                              font = "Comic Mono",
                              padding = 10,
                              foreground = colors[12],
                              background = colors[1]
                              ),
                    widget.Sep( #6
                              linewidth = 0,
                              padding = 30,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.WindowName( #7
                              foreground = colors[12],
                              background = colors[0],
                              padding = 0
                              ),
                    widget.Sep( #8
                              linewidth = 0,
                              padding = 6,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.TextBox( #9
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 5,
                              fontsize = 37
                              ),
                         widget.Clock( #10
                              foreground = colors[12],
                              background = colors[0],
                              padding = 5,
                              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(calendar)},
                              format = "KW%W %A %d.%m.%Y - %H:%M:%S"
                              ),
                         widget.TextBox( #11
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Sep( #12
                              linewidth = 0,
                              padding = 500,
                              foreground = colors[0],
                              background = colors[0]
                              ),
                    widget.Cmus( #13
                              foreground = colors[12],
                              background = colors[0],
                              noplay_color = colors[6],
                              play_color = '4893f5',
                              update_interval = .5,
                              padding = 2,
                              ),
                    widget.Sep( #14
                              linewidth = 0,
                              padding = 200,
                              foreground = colors[0],
                              background = colors[0]
                              ),
                         widget.TextBox( #15
                              text = " ???",
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              fontsize = 14
                              ),
                    widget.CheckUpdates( #14
                              update_interval = 1800,
                              distro = "Arch_checkupdates",
                              display_format = "{updates} Updates",
                              foreground = colors[12],
                              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                              background = colors[0]
                              ),
                    widget.TextBox( #15
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.TextBox( #16
                              text = " Vol:",
                              foreground = colors[12],
                              background = colors[0],
                              padding = 0
                              ),
                    # widget.Volume( #17
                    #          foreground = colors[6],
                    #          background = colors[0],
                    #          mouse_callbacks = {'Button3' : lambda: qtile.cmd_spawn("pavucontrol")},
                    #          #volume_app = "pavucontrol",
                    #          padding = 5
                    #          ),
                    widget.PulseVolume( #17
                              foreground = colors[12],
                              background = colors[0],
                              mouse_callbacks = {'Button3' : lambda: lazy.group['scratchpad'].dropdown_toggle('audio')},
                              volume_app = "pavucontrol",
                              padding = 5
                              ),
                    widget.TextBox( #18
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.CPU( #19
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                              fontsize = 14
                              ),
                    widget.TextBox( #20
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Memory( #21
                              background = colors[0],
                              foreground = colors[12],
                              padding = 0,
                              measure_mem = 'G',
                              fontsize = 17
                              ),
                    widget.TextBox( #22
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Net( #23
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                              fontsize = 14
                              ),
                    widget.TextBox( #24
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Wlan( #25
                              background = colors[0],
                              foreground = colors[12],
                              padding = 0,
                              fontsize = 17
                              ),
                    widget.TextBox( #26
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Battery( #27
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              fontsize = 14
                              ),
                    widget.TextBox( #28
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Backlight( #29
                              background = colors[0],
                              foreground = colors[4],
                              padding = 0,
                              fontsize = 17
                              ),
                    widget.TextBox( #30
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.CurrentLayoutIcon( #31
                              custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                              foreground = colors[12],
                              background = colors[0],
                              padding = 0,
                              scale = 0.7
                              ),
                    widget.CurrentLayout( #32
                              foreground = colors[12],
                              background = colors[0],
                              padding = 5
                              ),
                    widget.TextBox( #33
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Systray( #34
                              background = colors[0],
                              padding = 5
                              ),
                    ]
          return widgets_list

     def init_widgets_screen1():
          widgets_screen1 = init_widgets_list()
          del widgets_screen1[25:31] # Uncomment for Desktop
     #del widgets_screen1[27:30] #Uncomment for Laptop
     ####################################del widget_screen[22:24] #Uncomment for Laptop
          return widgets_screen1                 # Monitor 2 will display all widgets in widgets_list


     def init_widgets_screen2():
          widgets_screen2 = init_widgets_list()
          return widgets_screen2

     def init_screens():
          return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=38, margin=2)),
               Screen()]
               #Screen()]

if type_of_dev == "laptop":

     def init_widgets_list():
          widgets_list = [
 widget.Sep( #1
                              linewidth = 0,
                              padding = 6,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.Image( #2
                              filename = "~/.config/qtile/icons/python-white.png",
                              scale = "False",
                              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)}
                              ),
                    widget.Sep( #3
                              linewidth = 0,
                              padding = 6,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.GroupBox( #4
                              font = "Comic Mono",
                              # font = "Fraktur",
                              fontsize = 25,
                              margin_y = 0,
                              margin_x = 0,
                              padding_y = 0 ,
                              padding_x = 7,
                              borderwidth = 1,
                              active = colors[12],
                              inactive = colors[7],
                              rounded = True,
                              highlight_color = colors[14],
                              highlight_method = "border",
                              this_current_screen_border = colors[13],
                              this_screen_border = colors [1],
                              other_current_screen_border = colors[15],
                              other_screen_border = colors[15],
                              foreground = colors[12],
                              background = colors[0]
                              ),
                    widget.Prompt( #5
                              prompt = prompt,
                              font = "Comic Mono",
                              padding = 10,
                              foreground = colors[12],
                              background = colors[1]
                              ),
                    widget.Sep( #6
                              linewidth = 0,
                              padding = 30,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.WindowName( #7
                              foreground = colors[12],
                              background = colors[0],
                              padding = 0
                              ),
                    widget.Sep( #8
                              linewidth = 0,
                              padding = 6,
                              foreground = colors[11],
                              background = colors[0]
                              ),
                    widget.TextBox( #9
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 5,
                              fontsize = 37
                              ),
                         widget.Clock( #10
                              foreground = colors[12],
                              background = colors[0],
                              padding = 5,
                              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(calendar)},
                              format = "KW%W %A %d.%m.%Y - %H:%M:%S"
                              ),
                         widget.TextBox( #11
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Sep( #12
                              linewidth = 0,
                              padding = 100,
                              foreground = colors[0],
                              background = colors[0]
                              ),
                    widget.Cmus( #13
                              foreground = colors[12],
                              background = colors[0],
                              noplay_color = colors[6],
                              play_color = '4893f5',
                              update_interval = .5,
                              padding = 2,
                              ),
                    widget.Sep( #14
                              linewidth = 0,
                              padding = 200,
                              foreground = colors[0],
                              background = colors[0]
                              ),
                         widget.TextBox( #15
                              text = " ???",
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              fontsize = 14
                              ),
                    widget.CheckUpdates( #14
                              update_interval = 1800,
                              distro = "Arch_checkupdates",
                              display_format = "{updates} Updates",
                              foreground = colors[12],
                              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                              background = colors[0]
                              ),
                    widget.TextBox( #15
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.TextBox( #16
                              text = " Vol:",
                              foreground = colors[12],
                              background = colors[0],
                              padding = 0
                              ),
                    # widget.Volume( #17
                    #          foreground = colors[6],
                    #          background = colors[0],
                    #          mouse_callbacks = {'Button3' : lambda: qtile.cmd_spawn("pavucontrol")},
                    #          #volume_app = "pavucontrol",
                    #          padding = 5
                    #          ),
                    widget.PulseVolume( #17
                              foreground = colors[12],
                              background = colors[0],
                              mouse_callbacks = {'Button3' : lambda: lazy.group['scratchpad'].dropdown_toggle('audio')},
                              volume_app = "pavucontrol",
                              padding = 5
                              ),
                    widget.TextBox( #18
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.CPU( #19
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                              fontsize = 14
                              ),
                    widget.TextBox( #20
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Memory( #21
                              background = colors[0],
                              foreground = colors[12],
                              padding = 0,
                              measure_mem = 'G',
                              fontsize = 17
                              ),
                    widget.TextBox( #22
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Net( #23
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                              fontsize = 14
                              ),
                    # widget.TextBox( #24
                    #           text = '|',
                    #           background = colors[0],
                    #           foreground = colors[11],
                    #           padding = 0,
                    #           fontsize = 37
                    #           ),
                    # widget.Wlan( #25
                    #           background = colors[0],
                    #           foreground = colors[12],
                    #           padding = 0,
                    #           fontsize = 17
                    #           ),
                    widget.TextBox( #26
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Battery( #27
                              padding = 2,
                              foreground = colors[12],
                              background = colors[0],
                              fontsize = 14
                              ),
                    widget.TextBox( #28
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Backlight( #29
                              background = colors[0],
                              foreground = colors[4],
                              padding = 0,
                              fontsize = 17
                              ),
                    widget.TextBox( #30
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.CurrentLayoutIcon( #31
                              custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                              foreground = colors[12],
                              background = colors[0],
                              padding = 0,
                              scale = 0.7
                              ),
                    # widget.CurrentLayout( #32
                    #           foreground = colors[12],
                    #           background = colors[0],
                    #           padding = 5
                    #           ),
                    widget.TextBox( #33
                              text = '|',
                              background = colors[0],
                              foreground = colors[11],
                              padding = 0,
                              fontsize = 37
                              ),
                    widget.Systray( #34
                              background = colors[0],
                              padding = 100
                              ),
                    ]
          return widgets_list

     def init_widgets_screen1():
          widgets_screen1 = init_widgets_list()
          # del widgets_screen1[25:29] # Uncomment for Desktop
     # del widgets_screen1[23:29] # Uncomment for Desktop
     #del widgets_screen1[27:30] #Uncomment for Laptop
     ####################################del widget_screen[22:24] #Uncomment for Laptop
          return widgets_screen1                 # Monitor 2 will display all widgets in widgets_list


     def init_widgets_screen2():
          widgets_screen2 = init_widgets_list()
          return widgets_screen2

     def init_screens():
          return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=40, margin=2)),
                    Screen()]
               #Screen()]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
reconfigure_screens = True
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),
    #Match(wm_class='pavucontrol'),# tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),# GPG key password entry
    Match(wm_class='nm-connection-editor'),
    Match(wm_class='yad'),
    Match(wm_class='blueberry.py'),
    Match(wm_class='zoom'),
    Match(wm_class='clight-gui'),
    Match(wm_class='tk'),
    Match(wm_class='Toplevel'),
    Match(wm_class='forcemeter.py'),
    Match(wm_class='flameshot'),
    Match(wm_class='feh'),
])
auto_fullscreen = True
focus_on_window_activation = "urgent"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/onreload.sh'])
    lazy.group['vid'].toscreen()




# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
