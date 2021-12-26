from components.abilities.masonry_ability import MasonryAbility
from engine import palettes
from gui.gui_element import GuiElement


class HelpTab(GuiElement):
    """Represent a text label."""
    def __init__(
            self,
            x,
            y,
            fg=palettes.WHITE,
            mg=palettes.GABRIEL_3_5,
            bg=palettes.BACKGROUND,
            name=None
    ):
        super().__init__(x, y, name=name)
        self.fg = fg
        self.mg = mg
        self.bg = bg

        self.has_masonry = False

    def update(self, scene):
        if scene.cm.get_one(MasonryAbility, entity=scene.player):
            self.has_masonry = True
        else:
            self.has_masonry = False

    def render(self, panel):
        """Draw the bar onto the panel"""
        masonry_color = self.fg if self.has_masonry else self.mg
        panel.print(self.x, self.y, "Controls", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+2, "  ↑ ", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y + 3, "← ↓ →  : Move / Attack", fg=self.fg, bg=self.bg)

        panel.print(self.x, self.y+5, "SPACE  : Thwack", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+6, "f      : Shoot", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+7, "s      : Plant Sapling", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+8, "d      : Dig", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+9, "e      : Build Fence", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+10, "r      : Build Wall", fg=masonry_color, bg=self.bg)
        panel.print(self.x, self.y+11, "c      : Dig", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+12, "a      : Fast Forward", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+13, "`      : Debug", fg=self.fg, bg=self.bg)
        panel.print(self.x, self.y+114, "ESC    : Back", fg=self.fg, bg=self.bg)
