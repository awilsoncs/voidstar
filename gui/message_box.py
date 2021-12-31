import textwrap

from engine import palettes
from gui.gui_element import GuiElement


class MessageBox(GuiElement):
    def __init__(self, x, y, width, height, value=None):
        super().__init__(x, y)
        self.height = height
        self.width = width
        self.value = value if value is not None else []

    def render(self, panel):
        panel.print(self.x, self.y, 'Messages_______________', bg=None, fg=palettes.WHITE)
        y = 1
        output = []
        for message in self.value:
            new_msg = message.text
            color = message.color
            new_msg_lines = textwrap.wrap(new_msg, self.width)

            for line in new_msg_lines:
                if len(output) == self.height - 2:
                    del output[0]
                output.append((line, color))

        for (line, color) in output:
            panel.print(self.x, self.y+y, line, bg=None, fg=color)
            y += 1

        panel.print(self.x, self.y + self.height, '_______________________', bg=None, fg=palettes.WHITE)

