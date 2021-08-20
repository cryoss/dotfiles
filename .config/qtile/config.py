# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
#START_KEYS
keys = [
         ### The essentials

         Key([mod, "shift"], "s",
             lazy.spawn("bash /home/cryoss/.config/qtile/showkeys.sh"),
             desc='Show keys'
             ),
         Key([mod], "Return",
             lazy.spawn(myTerm+" -e fish"),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             #lazy.spawn("dmenu_run -p 'Run: '"),
             lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/arc-red-dark.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='Run Launcher'
             ),
         Key([mod, "shift"], "l",
             lazy.spawn("looking-glass-client"),
             desc='looking-glass-client'
             ),
         Key([mod, "shift"], "m",
             lazy.spawn("thunderbird"),
             desc='thunderbird'
             ),
         Key([mod, "shift"], "c",
             lazy.spawn("qalculate-gtk"),
             desc='qalculate'
             ),
         Key([mod], "b",
             lazy.spawn("firefox"),
             desc='firefox'
             ),
         Key([mod], "d",
             lazy.spawn("dolphin"),
             desc='dolphin'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "w",
             lazy.window.kill(),
             desc='Kill active wondow'
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
##         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
#         Key([mod], "r",
#             lazy.to_screen(2),
#             desc='Keyboard focus to monitor 3'
#             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
#         Key([mod, "shift"], "h",
#             lazy.layout.move_left(),
#             desc='Move up a section in treetab'
#             ),
#         Key([mod, "shift"], "ö",
#             lazy.layout.move_right(),
#             desc='Move down a section in treetab'
#             ),
         ### Window controls
         Key([mod], "Right",
             lazy.screen.next_group(),
             desc='Left Group'
             ),
         Key([mod], "Left",
             lazy.screen.prev_group(),
             desc='Right Group'
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
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         Key([mod], "Page_Up",
             lazy.spawn("amixer -D pulse sset Master 5%+"),
             desc='Vol +'
             ),
         Key([mod], "Page_Down",
             lazy.spawn("amixer -D pulse sset Master 5%-"),
             desc='Vol -'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         KeyChord(["control"],"e", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Launch Emacs'
                 ),
             Key([], "b",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                 desc='Launch ibuffer inside Emacs'
                 ),
             Key([], "d",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                 desc='Launch dired inside Emacs'
                 ),
             Key([], "i",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
                 desc='Launch erc inside Emacs'
                 ),
             Key([], "m",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
                 desc='Launch mu4e inside Emacs'
                 ),
             Key([], "n",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
                 desc='Launch elfeed inside Emacs'
                 ),
             Key([], "s",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                 desc='Launch the eshell inside Emacs'
                 ),
             Key([], "v",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                 desc='Launch vterm inside Emacs'
                 )
         ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         KeyChord([mod], "p", [
             Key([], "e",
                 lazy.spawn("./dmscripts/scripts/dm-confedit"),
                 desc='Choose a config file to edit'
                 ),
             Key([], "i",
                 lazy.spawn("./dmscripts/scripts/dm-maim"),
                 desc='Take screenshots via dmenu'
                 ),
             Key([], "k",
                 lazy.spawn("./dmscripts/scripts/dm-kill"),
                 desc='Kill processes via dmenu'
                 ),
             Key([], "q",
                 lazy.spawn("./dmscripts/scripts/dm-logout"),
                 desc='A logout menu'
                 ),
             Key([], "m",
                 lazy.spawn("./dmscripts/scripts/dm-man"),
                 desc='Search manpages in dmenu'
                 ),
             Key([], "o",
                 lazy.spawn("./dmscripts/scripts/dm-bookman"),
                 desc='Search your qutebrowser bookmarks and quickmarks'
                 ),
             Key([], "r",
                 lazy.spawn("./dmscripts/scripts/dm-reddit"),
                 desc='Search reddit via dmenu'
                 ),
             Key([], "s",
                 lazy.spawn("./dmscripts/scripts/dm-websearch"),
                 desc='Search various search engines via dmenu'
                 ),
              Key([], "a",
                 lazy.spawn("pavucontrol"),
                 desc='audioMixer'
                 ),
             Key([], "p",
                 lazy.spawn("passmenu"),
                 desc='Retrieve passwords with dmenu'
                 )
         ])
]
#END_KEYS
group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5: Win10", {'layout': 'max'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'max'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    # layout.TreeTab(
    #     font = "Ubuntu",
     #    fontsize = 10,
      #   sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
       #  section_fontsize = 10,
       #  border_width = 2,
       #  bg_color = "1c1f24",
       #  active_bg = "c678dd",
       #  active_fg = "000000",
       #  inactive_bg = "a9a1e1",
       #  inactive_fg = "1c1f24",
       #  padding_left = 0,
       #  padding_x = 0,
       #  padding_y = 5,
       #  section_top = 10,
       #  section_bottom = 20,
       #  level_shift = 8,
       #  vspace = 3,
       #  panel_width = 200
        # ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#3498db", "#3498db"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#2e4053", "#2e4053"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#2f4735", "#2f4735"], # color for the 'even widgets'
          ["#e1acff", "#e1acff"], # window name
          ["#d5d8dc", "#d5d8dc"], # backbround for inactive screens
          ["#f4d03f", "#f4d03f"],
          ["#17202a", "#17202a"]]
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Cascadia Mono",
    fontsize = 16,
    padding = 2,
    background=colors[8]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep( #1
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[8],
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
                       foreground = colors[8],
                       background = colors[0]
                       ),
              widget.GroupBox( #4
                       font = "Ubuntu Bold",
                       fontsize = 15,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[8],
                       background = colors[0]
                       ),
              widget.Prompt( #5
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep( #6
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[8],
                       background = colors[0]
                       ),
              widget.WindowName( #7
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Systray( #8
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep( #9
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox( #10
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox( #11
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[8],
                       background = colors[0],
                       fontsize = 14
                       ),
              widget.CheckUpdates( #12
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[8],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[0]
                       ),
              widget.TextBox( #13
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox( #14
                       text = " Vol:",
                       foreground = colors[8],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Volume( #15
                       foreground = colors[8],
                       background = colors[0],
                       mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn("pavucontrol")},
                       #volume_app = "pavucontrol",
                       padding = 5
                       ),
              widget.TextBox( #16
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CPU( #17
                       padding = 2,
                       foreground = colors[8],
                       background = colors[0],
                       mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                       fontsize = 14
                       ),
              widget.TextBox( #18
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Memory( #19
                       background = colors[0],
                       foreground = colors[8],
                       padding = 0,
                       measure_mem = 'G',
                       fontsize = 17
                       ),
              widget.TextBox( #20
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Net( #21
                       padding = 2,
                       foreground = colors[8],
                       background = colors[0],
                       mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                       fontsize = 14
                       ),
              widget.Clipboard( #22
                       background = colors[0],
                       foreground = colors[8],
                       max_chars = 30,
                       font = 'sans',
                       fmt = '{}',
                       selection = 'CLIPBOARD',
                       timeout = 0,
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox( #23
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Wlan( #24
                       background = colors[0],
                       foreground = colors[8],
                       padding = 0,
                       fontsize = 17
                       ),
              widget.TextBox( #25
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Battery( #26
                       padding = 2,
                       foreground = colors[8],
                       background = colors[0],
                       fontsize = 14
                       ),
              widget.TextBox( #27
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Backlight( #28
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 17
                       ),
              widget.TextBox( #29
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox( #30
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon( #31
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout( #32
                       foreground = colors[8],
                       background = colors[0],
                       padding = 5
                       ),
              widget.TextBox( #33
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock( #34
                       foreground = colors[8],
                       background = colors[0],
                       format = "%A, %B %d - %H:%M "
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[22:28] # Uncomment for Desktop
    #del widgets_screen1[27:30] #Uncomment for Laptop
    #del widget_screen[22:24] #Uncomment for Laptop
    return widgets_screen1                 # Monitor 2 will display all widgets in widgets_list


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[22:28]
    del widgets_screen2[7:8]
    return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=30, margin=2)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.9, size=30, margin=2))]
#            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

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

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),
    Match(wm_class='pavucontrol'),# tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),# GPG key password entry
    Match(wm_class='nm-connection-editor'),
    Match(wm_class='yad'),
    Match(wm_class='clight-gui'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
@hook.subscribe.startup
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/onreload.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
