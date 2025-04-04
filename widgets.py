import subprocess

from libqtile import widget
from libqtile.lazy import lazy

from current_theme import colors

widget_defaults = dict(
    font="UbuntuMono Nerd Font Bold",
    fontsize=18,
    padding=3,
    background=colors['background'],
    foreground=colors['foreground']
)

widgets = [
    widget.Sep(
        padding=0,
        linewidth=5,
        background=colors["background"],
        foreground=colors["background"],
    ),
    widget.TextBox(
        text="󰣇 ",  # Icono (puedes usar 🔌, ⏻, ⏼, etc.)
        fontsize=30,
        padding=10,
        foreground=colors['primary'],
        background=colors['background'],
        mouse_callbacks={
            "Button1": lazy.spawn("bash /home/arch/.config/qtile/scripts/update_system.sh"),
        },
    ),
    widget.TextBox(
        text=" ",
        fontsize=55,
        padding=-12,
        foreground=colors['background'],
        background=colors['primary'],
    ),
    widget.GenPollText(
        update_interval=30,
        func=lambda: subprocess.check_output("~/.config/qtile/scripts/disk_usage.sh", shell=True).decode("utf-8").strip(),
        padding=5,
        foreground=colors['background'],
        background=colors['primary'],
    ),
    widget.TextBox(
        text=" ",
        fontsize=55,
        padding=-12,
        background=colors['background'],
        foreground=colors['primary'],
    ),
    widget.Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
    ),
    widget.TextBox(
        text=" ",
        fontsize=55,
        padding=-12,
        foreground=colors['background'],
        background=colors['inactive'],
    ),
    widget.GenPollText(
        update_interval=60,  # Actualizar cada 60 segundos
        func=lambda: subprocess.check_output(
            "~/.config/qtile/scripts/get_ip.sh",
            shell=True
        ).decode("utf-8").strip(),
        foreground=colors['success'],
        background=colors['inactive'],
        padding=5,
    ),
    widget.TextBox(
        text=" ",
        fontsize=55,
        padding=-12,
        background=colors['background'],
        foreground=colors['inactive'],
    ),

    widget.Spacer(),
    widget.GroupBox(
        highlight_method='block',
        padding=10,
        block_highlight_text_color=colors['background'],
        active=colors['active'],
        inactive=colors['inactive'],
        this_current_screen_border=colors['primary'],
        fontsize=25,
        font='D2coding Nerd Font',
        disable_drag=True
    ),
    widget.Spacer(),

    widget.TextBox(
        text="",
        fontsize=55,
        padding=-1,
        background=colors['background'],
        foreground=colors['inactive'],
    ),
    widget.Pomodoro(
        background=colors['inactive'],
        color_active=colors['success'],
        color_break=colors['warning'],
        color_inactive=colors['alert']
    ),
    widget.TextBox(
        text="",
        fontsize=55,
        padding=-1,
        foreground=colors['background'],
        background=colors['inactive'],
    ),
    widget.KeyboardLayout(
        configured_keyboards=['us', 'latam'],
        display_map={'us': 'US', 'latam': 'Latam'},
        option='grp:win_space_toggle'
    ),
    widget.TextBox(
        text="\\",
    ),
    widget.Systray(),
    widget.TextBox(
        text="\\",
    ),
    widget.GenPollText(
        script="~/.config/qtile/scripts/battery.sh",
        update_interval=5,  # Actualiza cada 10 segundos
        func=lambda: subprocess.check_output(
            "~/.config/qtile/scripts/battery.sh",
            shell=True
        ).decode("utf-8").strip(),
        padding=5,
    ),
    widget.TextBox(
        text="",
        fontsize=55,
        padding=-1,
        background=colors['background'],
        foreground=colors['primary'],
    ),
    widget.Clock(
        format="%Y-%m-%d %I:%M %p",
        background=colors['primary'],
        foreground=colors['background'],
    ),
    widget.TextBox(
        text="",
        fontsize=55,
        padding=-1,
        foreground=colors['background'],
        background=colors['primary']
    ),
    widget.TextBox(
        #text="󰣇 ",  # Icono (puedes usar 🔌, ⏻, ⏼, etc.)
        text='⏻ ',
        fontsize=30,
        padding=10,
        foreground=colors['primary'],
        background=colors['background'],
        mouse_callbacks={
            "Button1": lazy.spawn("bash /home/arch/.config/qtile/scripts/powermenu.sh"),
        },
    ),
    widget.Sep(
        padding=0,
        linewidth=5,
        background=colors["background"],
        foreground=colors["background"],
    ),
    # widget.QuickExit(),
]

