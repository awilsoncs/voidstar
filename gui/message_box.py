import textwrap

import settings
from gui.gui_element import GuiElement


class MessageBox(GuiElement):
    def __init__(self, x, y, height, width, value=None):
        super().__init__(x, y)
        self.height = height
        self.width = width
        self.value = value if value is not None else []

    def render(self, panel):
        y = 1
        output = []
        for message in self.value:
            new_msg = message.message
            color = message.color
            new_msg_lines = textwrap.wrap(new_msg, settings.MSG_WIDTH)

            for line in new_msg_lines:
                if len(output) == settings.MSG_HEIGHT:
                    del output[0]
                output.append((line, color))

        for (line, color) in output:
            panel.print(self.x, self.y+y, line, bg=None, fg=color)
            y += 1
