from typing import List  # noqa: F401
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, DropDown, Group, KeyChord, Key, Match, Screen, ScratchPad
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
home = os.path.expanduser('~')
mod1 = "mod1"

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

################# USER SHORTCUTS #################

keys = [
    Key([mod1], "r", lazy.spawn("rofi -show drun")),
    Key([mod], "x", lazy.spawn("blurlock")),
    Key([mod], "d", lazy.spawn("findex")),

    Key([], "XF86AudioMute", lazy.spawn("volume.sh mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume.sh down")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume.sh up")),
    
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightness.sh down")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightness.sh up")),

    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod1], "p", lazy.spawn("pavucontrol")),
    Key([mod1], "n", lazy.spawn("thunar")),
    Key([mod1], "a", lazy.spawn("xterm")),
    Key([mod1], "v", lazy.spawn("vscodium")),
    Key([mod1], "d", lazy.spawn("discord")),
    Key([mod1], "s", lazy.spawn("spotify")),
    Key([mod1], "q", lazy.spawn("qbittorrent")),
    Key([mod1], "m", lazy.spawn("multimc")),
    Key([mod1], "l", lazy.spawn("lollypop")),
    Key([mod1], "t", lazy.spawn("teams-for-linux")),
    Key([mod1], "f", lazy.spawn("firefox-developer-edition")),
    
    Key([mod, mod1], "q", lazy.spawn("shutdown.sh")),
    Key([mod, mod1], "r", lazy.spawn("reboot.sh")),

############## SCREENSHOTS ###################
    
   # Key(["shift"], "Print", lazy.spawn("maim | xclip -selection clipboard -t image/png")),
   # Key([mod], "Print", lazy.spawn("maim --select | xclip -selection clipboard -t image/png")),
   Key([], "Print", lazy.spawn("clip.sh")),
   Key(["shift"], "Print", lazy.spawn("shot.sh")),


################# SWITCH LAYOUT ###################

# TOGGLE FLOATING LAYOUT
    Key([mod], "t", lazy.window.toggle_floating()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod, mod1], "h",lazy.layout.grow(), lazy.layout.increase_nmaster()),
    Key([mod, mod1], "l", lazy.layout.shrink(), lazy.layout.decrease_nmaster()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.window.toggle_fullscreen()),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    Key([mod], "s", lazy.layout.next()),

# BSPWM 

    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "Down", lazy.layout.flip_down()),
    Key([mod, "mod1"], "Up", lazy.layout.flip_up()),
    Key([mod, "mod1"], "Left", lazy.layout.flip_left()),
    Key([mod, "mod1"], "Right", lazy.layout.flip_right()),
    Key([mod, "control"], "Down", lazy.layout.grow_down()),
    Key([mod, "control"], "Up", lazy.layout.grow_up()),
    Key([mod, "shift"], "l", lazy.layout.grow_left()),
    Key([mod, "shift"], "m", lazy.layout.grow_right()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "z", lazy.layout.toggle_split()),
    Key([mod], "period", lazy.layout.increase_ratio()),
    Key([mod], "comma", lazy.layout.decrease_ratio()),

    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod], "c", lazy.restart()),   

]

groups= [

    Group("1",
          label="I",
          ),

    Group("2",
          label="II",
          ),

    Group("3",
          label="III",
          ),

    Group("4",
          label="IV",
          ),

    Group("5",
          label="V",
          ),

    Group("6",
          label="VI",
          ),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# LAYOUTS

layouts = [
    layout.MonadTall(margin=6, border_width=2, border_focus="#007dcc", border_normal="#414a5b"),
    layout.MonadWide(margin=6, border_width=2, border_focus="#007dcc", border_normal="#414a5b"),
    layout.Bsp (margin=5, border_width=2, border_focus="#007dcc", border_normal="#414a5b", fair=False),
    layout.matrix.Matrix(columns=2, margin=2, border_width=2, border_focus="#007dcc"),
    layout.Max(margin=0, border_width=0),
]


colors =  [

        ["#181c22", "#232831"], # color 0
        ["#4aa3ed", "#4aa3ed"], # color 1
        ["#e8969d", "#e8969d"], # color 2
        ["#78bbf1", "#78bbf1"], # color 3
        ["#f984a0", "#f984a0"], # color 4
        ["#ffffff", "#ffffff"], # color 5
        ["#B9BCDF", "#B9BCDF"], # color 6
        ["#e48189", "#e48189"], # color 7
        ["#61afef", "#61afef"], # color 8
        ["#bbebca", "#bbebca"]] # color 9

widget_defaults = dict(
    font='novamono for Powerline',
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.45,
                    padding=0,
                ),
                widget.TextBox(
                    text='|',
                    padding=0,
                    fontsize = 17,
                    foreground=colors[5],
                ),
                widget.GroupBox(
                    font="space mono for powerline",
                    fontsize=14,
                    margin_y=3,
                    margin_x=4,
                    padding_y=4,
                    padding_x=4,
                    borderwidth=6,
                    inactive=colors[6],
                    active=colors[4],
                    rounded=True,
                    highlight_color=colors[0],
                    highlight_method="block",
                    this_current_screen_border=colors[6],
                    block_highlight_text_color=colors[0],
                ),
                widget.Spacer(),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.Systray(
                    background=colors[0],
                    icons_size=20,
                    padding=4,
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='17',
                    padding=0,
                    background=colors[0],
                    foreground=colors[3],
                ),
                widget.TextBox(
                    text=' ﬙',
                    fontsize='20',
                    padding=0,
                    background=colors[0],
                    foreground=colors[3],
                ),
                widget.Memory(
                    background=colors[0],
                    foreground=colors[3],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                    format = '{MemUsed: .0f} MB',
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='17',
                    padding=0,
                    background=colors[0],
                    foreground=colors[8],
                ),
                widget.Sep(
                    padding=4,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 5 Free",
                    foreground=colors[8],
                    background=colors[0],
                    padding=0,
                    fontsize=22
                ),
                widget.Sep(
                    padding=4,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.CPU(
                    background=colors[0],
                    foreground=colors[8],
                    format='CPU: {load_percent}%'
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='17',
                    padding=0,
                    background=colors[0],
                    foreground=colors[1],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text = "",
                    foreground = colors[1],
                    background = colors[0],
                    padding = 1,
                    font = "Font Awesome 5 Free",
                    fontsize = 13,
                ),
                widget.Sep(
                    padding=1,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.Volume(
                    font="novamono for powerline",
                    background=colors[0],
                    foreground=colors[1],
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='17',
                    padding=0,
                    background=colors[0],
                    foreground=colors[2],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='',
                    font="Font Awesome 5 Free",
                    fontsize='14',
                    padding=0,
                    background=colors[0],
                    foreground=colors[2],
                ),
                widget.Sep(
                    padding=4,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.Clock(
                    font = "comic sans ms",
                    foreground = colors[2],
                    background = colors[0],
                    fontsize = 15,
                    format = '%a %d %B, %H:%M',
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text='|',
                    fontsize='17',
                    padding=0,
                    background=colors[0],
                    foreground=colors[7],
                ),
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors[0],
                ),
                widget.TextBox(
                    text = "", 
                    font = "Font Awesome 5 Free", 
                    fontsize = 14, 
                    foreground = colors[7], 
                    background = colors[0],
                    padding = 0,
                    ),
                widget.Battery(
                    foreground = colors[7],
                    background = colors[0],
                    fontsize = 16,
                    low_percentage = 0.2,
                    low_foreground = colors[5],
                    font = "novamono for powerline",
                    update_interval = 1,
                    padding = 5,
                    format = '{percent:2.0%}',
                ),
            ],
        36,
            opacity=1,
            background=colors[0],
            # margin=[4,4,0,4]
            ),
       ),
    ]

################# Drag floating layouts #################
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wmname = "LG3D"
