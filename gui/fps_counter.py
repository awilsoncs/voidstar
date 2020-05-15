import time

from engine import colors
from gui.gui_element import GuiElement
from gui.labels import Label


class FPSCounter(GuiElement):
    """Automatically monitor FPS with a label."""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.last_update = time.time()
        self.fps = 0
        self.label = Label(x, y, lambda: f'fps: {self.fps}', fg=colors.yellow)

    def render(self, panel):
        # fps tracking
        t = time.time()
        if t == self.last_update:
            return
        self.fps = int(round(1.0 / (t - self.last_update)))
        self.last_update = t
        self.label.render(panel)
