from typing import List  # noqa: F401
import os
import re
import socket
import subprocess
from libqtile.command import lazy
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
    Key([mod1], "r", lazy.spawn("rofi -show drun -auto-select")),
    Key([mod], "d", lazy.spawn("findex")),

    Key([], "XF86AudioMute", lazy.spawn("volume.sh mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume.sh down")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume.sh up")),
    
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightness.sh down")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightness.sh up")),

    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod1], "p", lazy.spawn("pavucontrol")),
    Key([mod1], "n", lazy.spawn("thunar")),
    Key([mod1], "v", lazy.spawn("vscodium")),
    Key([mod1], "d", lazy.spawn("discord")),
    Key([mod1], "s", lazy.spawn("spotify")),
    Key([mod1], "q", lazy.spawn("transmission-gtk")),
    Key([mod1], "m", lazy.spawn("multimc")),
    Key([mod1, "control"], "l", lazy.spawn("alacritty -e killmocp.sh")),
    Key([mod1], "l", lazy.spawn("alacritty -e mocp -M ~/.config/moc")),
    Key([mod1], "t", lazy.spawn("teams-for-linux")),
    Key([mod1], "f", lazy.spawn("firefox-developer-edition")),
    Key([mod1], "b", lazy.spawn("blueman-manager")),
    
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
    Key([mod, "shift"], "r", lazy.restart()),   

]

groups= [

    Group("1",
          label="",
          ),

    Group("2",
          label="",
          ),

    Group("3",
          label="",
          ),

    Group("4",
          label="",
          ),

    Group("5",
          label="",
          ),

    Group("6",
          label="",
          ),
    Group("7",
          label="",
          ),  
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# LAYOUTS

layouts = [
    layout.MonadTall(margin=6, border_width=2, border_focus="#0aaccf", border_normal="#414a5b", fair=False),
    #layout.MonadWide(margin=6, border_width=2, border_focus="#0aaccf", border_normal="#414a5b"),
    layout.Bsp (margin=5, border_width=2, border_focus="#0aaccf", border_normal="#414a5b", fair=False),
    #layout.matrix.Matrix(columns=2, margin=2, border_width=2, border_focus="#007dcc"),
    layout.Max(margin=0, border_width=0),
    #layout.zoomy.Zoomy(columnwidth=400,margin=2,),
    #layout.tree.TreeTab(active_bg="#0aaccf",active_fg="#1a1e25",bg_color="#1a1e25",font='comic sans ms',inactive_bg="#303643",border_width=2, border_focus="#0aaccf", border_normal="#414a5b", vspace=2,margin_left=4,margin_y=4,panel_width=200),
]

colors =  [
        ["#FFFFFF", "#FFFFFF"], # white / color 0
        ["#7bf52e", "#99f75e"], # lime / color 1
        ["#384657", "#384657"], # dark gray / color 2
        ["#b2b2b2", "#b2b2b2"], # light gray / color 3
        ["#0aaccf", "#0aaccf"], # cyan / color 4
        ["#6bb7fa", "#6bb7fa"], # blue / color 5
        ["#bf0be2", "#d42bf5"], # purple / color 6
        ["#5268f9", "#5268f9"], # dark blue / color 7
        ["1a1e25", "#1a1e25"], # navy blue / color 8
        ["#1a1e25", "#1a1e25"]] # black / color 9
        

widget_defaults = dict(
    font='JetBrainsMono Nerd Font',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    background = colors[9],
                    padding = 5,
                    linewidth = 0,
                 ),
                 widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale = 0.50,
                    padding = 0,
                    foreground = colors[0],
                    background = colors[9],
                ),
                widget.GroupBox(
                    font = "JetBrainsMono Nerd Font",
                    fontsize = 15,
                    margin_y = 2,
                    margin_x = 2,
                    center_aligned = True,
                    padding_y = 5,
                    padding_x = 10,
                    active = "#f7768e",
                    inactive = colors[0],
                    this_current_screen_border = "#69d588",
                    highlight_color = colors[9],
                    urgent_alert_method = 'text',
                    highlight_method = "text",
                    #foreground = "#D8DEE9",
                    background = colors[8],
                ),
                widget.Spacer(
                    background = colors[9],
                    length = 540,
                ),
                widget.Clock(
                    font = "DM Sans Medium",
                    foreground = colors[0],
                    background = colors[8],
                    fontsize = 15,
                    format = '%A, %d %B at %H:%M',
                ),
                widget.Spacer(background = colors[8]),
                widget.Systray(
                    background = colors[9],
                    icons_size = 20,
                    padding = 4,
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    background = colors[8],
                ),
                widget.TextBox(
                    text = "\uE0B6", 
                    font = "Font Awesome 5 Free", 
                    fontsize = 32, 
                    foreground = colors[6], 
                    background = colors[9], 
                    padding = 0, 
                    update_interval = 60, 
                ),
                #widget.TextBox(
                #    text = "",
                #    foreground = colors[9],
                #    background = colors[6],
                #    padding = 2,
                #     font = "Font Awesome 5 Free",
                #    fontsize = 12,
                #),
                # Spotify Module
                #widget.Mpris2(
                #    name='spotify',
                #    background = colors[6],
                #    foreground = colors[9],
                #    objname="org.mpris.MediaPlayer2.spotify",
                #   font = "comic sans ms",
                #    fontsize = 15,
                #    padding = 2,
                #   display_metadata=['xesam:title'],
                #    scroll_chars=15,
                #    stop_pause_text='Paused',
                #    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 0,
                    background = colors[6],
                ),
                widget.TextBox(
                    text = "",
                    foreground = colors[9],
                    background = colors[6],
                    padding = 2,
                     font = "Font Awesome 5 Free",
                    fontsize = 24,
                ),
                widget.OpenWeather(
                    font = "DM Sans Medium",
                    foreground = colors[9],
                    background = colors[6],
                    cityid = 1259229,
                    fontsize = 15,
                    format = '{main_temp} °{units_temperature}',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    background = colors[6],
                ),
                widget.TextBox(
                    text = "\uE0B6", 
                    font = "Font Awesome 5 Free", 
                    fontsize = 32, 
                    foreground = colors[4], 
                    background = colors[6], 
                    padding = 0, 
                    update_interval = 60,
                ),
                widget.TextBox(
                    text = "﬙",
                    foreground = colors[9],
                    background = colors[4],
                    padding = 1,
                    fontsize = 20,
                ),
                widget.Memory(
                    foreground = colors[9],
                    background = colors[4],
                    font = "DM Sans Medium",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                    fontsize = 15,
                    update_interval = 5.0,
                    format = '{MemUsed: .0f} MB',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 0,
                    background = colors[4],
                ),
                widget.TextBox(
                    text = " ",
                    foreground = colors[9],
                    background = colors[4],
                    padding = 6,
                    fontsize = 20,
                ),
                widget.CPU(
                    foreground = colors[9],
                    background = colors[4],
                    font = "comic sans ms",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                    fontsize = 15,
                    update_interval = 5.0,
                    format = '{load_percent}%',
                        
                ),
                widget.Sep(linewidth = 0,
                    padding = 6,
                    foreground = colors[9],
                    background = colors[4],
                ),
                widget.TextBox(
                    text = "\uE0B6", 
                    font = "Font Awesome 5 Free", 
                    fontsize = 32, 
                    foreground = colors[6], 
                    background = colors[4], 
                    padding = 0, 
                    update_interval = 60,
                ),
                widget.TextBox(
                    text = "墳",
                    foreground = colors[9],
                    background = colors[6],
                    padding = 2,
                    font = "Font Awesome 5 Free",
                    fontsize = 24,
                ),
                widget.Volume(
                    foreground = colors[9],
                    background = colors[6],
                    font = "DM Sans Medium",
                    fontsize = 15,
                    mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    volume_app = "pavucontrol",
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    background = colors[6],
                ),
                widget.TextBox(
                    text = " ", 
                    font = "JetBrainsMono Nerd Font", 
                    fontsize = 14, 
                    foreground = colors[9], 
                    background = colors[6],
                    padding = 0,
                    ),
                widget.Battery(
                    foreground = colors[9],
                    background = colors[6],
                    fontsize = 15,
                    low_percentage = 0.2,
                    low_foreground = colors[8],
                    font = "DM Sans Medium",
                    update_interval = 1,
                    format = '{percent:2.0%}',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    foreground = colors[9],
                    background = colors[6],
                ),
              ],
            34,
        background = colors[9],
        #margin=[12,20,4,20],
        #margin=[8,8,2,8],
        margin=[0,0,2,0],
        opacity= 1.0,
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
