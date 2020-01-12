from engine import colors
from gui.gui_element import GuiElement


class Bar(GuiElement):
    def __init__(
        self,
        x,
        y,
        total_width,
        name,
        value,
        maximum,
        bar_color,
        back_color
     ):
        super().__init__(x, y, name=name)
        self.__total_width = total_width
        self.__value = value
        self.__maximum = maximum
        self.__bar_color = bar_color
        self.__back_color = back_color

    @property
    def total_width(self):
        return self._resolve(self.__total_width)

    @property
    def value(self):
        return self._resolve(self.__value)

    @property
    def maximum(self):
        return self._resolve(self.__maximum)

    @property
    def bar_color(self):
        return self._resolve(self.__bar_color)

    @property
    def back_color(self):
        return self._resolve(self.__back_color)

    def render(self, panel):
        """Draw the bar onto the panel"""
        bar_width = int(float(self.value) / self.maximum * self.total_width)
        panel.draw_rect(self.x, self.y, self.total_width, 1, 0, bg=self.back_color)
        if bar_width > 0:
            panel.draw_rect(self.x, self.y, bar_width, 1, 0, bg=self.bar_color)
        text = self.name + ': ' + str(self.value) + '/' + str(self.maximum)
        x_centered = self.x + (self.total_width - len(text)) // 2
        panel.print(x_centered, self.y, text, fg=colors.white, bg=None)