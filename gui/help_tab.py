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
        panel.print(self.x, self.y+2, "Q W E", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y + 3, "A   D  : Move / Attack", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+4, "Z X C", fg=self.fg, bg=self.bg)

        panel.print(self.x, self.y+6, "7 8 9", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+7, "4   6  : Move / Attack", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+8, "1 2 3", fg=self.fg, bg=self.bg)

        panel.print(self.x, self.y+10, "SPACE  : Thwack", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+11, "S / 4  : Wait", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+12, "`      : Debug", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+13, "ESC    : Back to Menu", fg=self.fg, bg=self.bg)
