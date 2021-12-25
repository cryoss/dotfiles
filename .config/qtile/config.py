# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile import layout, bar, widget, hook
from libqtile.command import lazy
from typing import List  # noqa: F401
from libqtile.lazy import LazyCall
from libqtile.command.client import CommandClient

def to_next_group(qtile):
     next_group_name = qtile.current_group.get_next_group().name
     qtile.current_window.togroup(next_group_name, switch_group=True)

def to_prev_group(qtile):
     prev_group_name = qtile.current_group.get_previous_group().name
     qtile.current_window.togroup(prev_group_name, switch_group=True)

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
calendar = "thunderbird"
browser = "firefox"
files = "dolphin"
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
             lazy.spawn("dmenu_run -p 'Run: '"),
             lazy.spawn("bash launcher_text"),
             desc='Run Launcher'
             ),
         Key([mod, "shift"], "l",
             lazy.spawn("looking-glass-client -C /home/cryoss/VM/lg.rc"),
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
         Key([mod], "d",
             lazy.spawn(files),
             desc='files'
             ),
         Key([mod], "Tab",
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
         KeyChord(["control"], "b",[
             Key([], "b",
                 lazy.spawn(browser+" --new-window"),
                 desc="Launch browser emby"
                 ),
             Key([], "e",
                 lazy.spawn(browser+" --new-window http://emby:8096"),
                 desc="Launch browser emby"
                 ),
             Key([], "y",
                 lazy.spawn(browser+" --new-window https://youtube.com"),
                 desc="Launch browser emby"
                 )
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
             Key([], "q",
                 lazy.spawn("bash powermenu"),
                 desc='A logout menu'
                 ),
             Key([], "o",
                 lazy.spawn("./dmscripts/scripts/dm-bookman"),
                 desc='Search your qutebrowser bookmarks and quickmarks'
                 ),
              Key([], "a",
                 lazy.spawn("pavucontrol"),
                 desc='audioMixer'
                 )
         ])
]
#END_KEYS
groups = [Group(i) for i in "123456789"]
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        # Key([mod, "shift"], "left", lazy.window.togroup(i.name-1)))

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
                        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


    layout_theme = {"border_width": 2,
                "margin": 1,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Zoomy(**layout_theme),
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
          "#6b86b0"] #10
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Cascadia Mono",
    fontsize = 16,
    padding = 1,
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
                       fontsize = 17,
                       margin_y = 0,
                       margin_x = 0,
                       padding_y = 0 ,
                       padding_x = 5,
                       borderwidth = 1,
                       active = colors[6],
                       inactive = colors[7],
                       rounded = True,
                       highlight_color = colors[1],
                       highlight_method = "border",
                       this_current_screen_border = colors[10],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[10],
                       other_screen_border = colors[4],
                       foreground = colors[6],
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
              widget.Sep( #8
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox( #9
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 5,
                       fontsize = 37
                       ),
               widget.Clock( #10
                       foreground = colors[6],
                       background = colors[0],
                       padding = 5,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(calendar)},
                       format = "KW%W %A %d.%m.%Y - %H:%M:%S"
                       ),
               widget.TextBox( #11
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Sep( #12
                       linewidth = 0,
                       padding = 600,
                       foreground = colors[0],
                       background = colors[0]
                       ),
               widget.TextBox( #13
                       text = " ⟳",
                       padding = 2,
                       foreground = colors[6],
                       background = colors[0],
                       fontsize = 14
                       ),
              widget.CheckUpdates( #14
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[6],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[0]
                       ),
              widget.TextBox( #15
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox( #16
                       text = " Vol:",
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Volume( #17
                       foreground = colors[6],
                       background = colors[0],
                       mouse_callbacks = {'Button3' : lambda: qtile.cmd_spawn("pavucontrol")},
                       #volume_app = "pavucontrol",
                       padding = 5
                       ),
              widget.TextBox( #18
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CPU( #19
                       padding = 2,
                       foreground = colors[6],
                       background = colors[0],
                       mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                       fontsize = 14
                       ),
              widget.TextBox( #20
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Memory( #21
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       measure_mem = 'G',
                       fontsize = 17
                       ),
              widget.TextBox( #22
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Net( #23
                       padding = 2,
                       foreground = colors[6],
                       background = colors[0],
                       mouse_callbacks = {'Button1' : lambda: qtile.cmd_spawn(myTerm+ ' -e htop')},
                       fontsize = 14
                       ),
              widget.TextBox( #24
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Wlan( #25
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       fontsize = 17
                       ),
              widget.TextBox( #26
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Battery( #27
                       padding = 2,
                       foreground = colors[6],
                       background = colors[0],
                       fontsize = 14
                       ),
              widget.TextBox( #28
                       text = '|',
                       background = colors[0],
                       foreground = colors[9],
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
                       foreground = colors[6],
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
              widget.Systray( #34
                       background = colors[0],
                       padding = 5
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[23:29] # Uncomment for Desktop
    #del widgets_screen1[27:30] #Uncomment for Laptop
    #del widget_screen[22:24] #Uncomment for Laptop
    return widgets_screen1                 # Monitor 2 will display all widgets in widgets_list


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.9, size=35, margin=2)),
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
    Match(wm_class='pavucontrol'),# tastyworks exit box
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
])
auto_fullscreen = True
focus_on_window_activation = "urgent"

@hook.subscribe.startup
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/onreload.sh'])
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
