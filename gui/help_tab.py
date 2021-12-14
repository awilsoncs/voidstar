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

        panel.print(self.x, self.y+5, "SPACE  : Thwack", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+6, "f      : Shoot", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+7, "a      : Fast Forward", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+8, "`      : Debug", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+9, "ESC    : Back", fg=self.fg, bg=self.bg)
