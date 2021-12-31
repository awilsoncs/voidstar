from components.abilities.build_wall_ability import BuildWallAbility
from engine import palettes
from gui.gui_element import GuiElement


class HelpTab(GuiElement):
    """Represent a text label."""
    def __init__(
            self,
            x,
            y,
            fg=palettes.WHITE,
            mg=palettes.MEAT,
            bg=palettes.BACKGROUND,
            name=None
    ):
        super().__init__(x, y, name=name)
        self.fg = fg
        self.mg = mg
        self.bg = bg

    def render(self, panel):
        """Draw the bar onto the panel"""
        panel.print(self.x, self.y, "Controls", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+2, "  ↑ ", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+3, "← ↓ →  : Move / Attack", fg=self.fg, bg=self.bg)

        panel.print(self.x, self.y+5, "SPACE  : Use Ability", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+6, "q      : Last Ability", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+7, "e      : Next Ability", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+8, "ESC    : Back", fg=self.fg, bg=self.bg)
