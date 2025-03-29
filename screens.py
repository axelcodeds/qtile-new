from libqtile import bar
from libqtile.config import Screen
from widgets import widgets

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]