from engine import palettes
from gui.gui_element import GuiElement


class Label(GuiElement):
    """Represent a text label."""
    def __init__(self, x, y, value, fg=palettes.WHITE, bg=palettes.BACKGROUND, name=None):
        super().__init__(x, y, name=name)
        self.value = value
        self.fg = fg
        self.bg = bg

    def render(self, panel):
        """Draw the bar onto the panel"""
        panel.print(self.x, self.y, self.value, fg=self.fg, bg=self.bg)
