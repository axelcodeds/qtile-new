from libqtile import widget

from colors import current_theme as colors

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    background=colors['background'],
    foreground=colors['foreground']
)

widgets = [
    widget.CurrentLayout(),
    widget.GroupBox(),
    widget.Prompt(),
    widget.WindowName(),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.KeyboardLayout(
        configured_keyboards=['us', 'latam'],
        display_map={'us': 'US', 'latam': 'Latam'},
        option='grp:win_space_toggle'
    ),
    widget.Systray(),
    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    widget.QuickExit(),
]

