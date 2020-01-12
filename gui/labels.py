from gui.gui_element import GuiElement


class Label(GuiElement):
    """Represent a text label."""
    def __init__(self, x, y, value, fg=None, bg=None, name=None):
        super().__init__(x, y, name=name)
        self.__value = value
        self.__fg = fg
        self.__bg = bg

    @property
    def value(self):
        return self._resolve(self.__value)

    @property
    def fg(self):
        return self._resolve(self.__fg)

    @property
    def bg(self):
        return self._resolve(self.__bg)

    def render(self, panel):
        """Draw the bar onto the panel"""
        panel.print(self.x, self.y, self.value, fg=self.fg, bg=self.bg)
