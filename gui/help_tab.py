from engine import palettes
from gui.gui_element import GuiElement


class HelpTab(GuiElement):
    """Represent a text label."""
    def __init__(self, x, y, fg=palettes.WHITE, bg=palettes.BACKGROUND, name=None):
        super().__init__(x, y, name=name)
        self.fg = fg
        self.bg = bg

    def render(self, panel):
        """Draw the bar onto the panel"""
        panel.print(self.x, self.y, "Controls", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+2, "  ↑ ", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y + 3, "← ↓ →  : Move / Attack", fg=self.fg, bg=self.bg)

        panel.print(self.x, self.y+10, "SPACE  : Thwack", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+11, "f      : Shoot", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+12, "a      : Fast Forward", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+13, "`      : Debug", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+14, "ESC    : Back to Menu", fg=self.fg, bg=self.bg)
