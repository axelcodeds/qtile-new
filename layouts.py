from libqtile import layout
from libqtile.config import Match

from colors import current_theme as colors

layouts = [
    layout.Columns(
        # border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4
        border_focus=colors['primary'],
        border_normal=colors['inactive'],
        border_width=2
        ),
    layout.Max(),
    # Add more layouts as needed
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)