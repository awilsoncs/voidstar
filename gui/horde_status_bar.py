from dataclasses import dataclass

from components.tags import Tag
from engine import palettes
from gui.gui_element import GuiElement


@dataclass
class HordeStatusBar(GuiElement):
    count: int = 0
    fg_color: tuple = palettes.HORDELING
    bg_color: tuple = palettes.BACKGROUND
    status: str = "Peaceful"
    current_hordelings: str = ""  # how many hordelings remain
    max_hordelings: str = ""  # how many hordelings were original in the attacking wave

    def render(self, panel):
        panel.print(self.x, self.y, self.status, fg=self.fg_color, bg=self.bg_color)
        panel.print(self.x, self.y + 1, self.current_hordelings)

    def update(self, scene):
        hordelings = scene.cm.get(Tag)
        hordelings = len([p for p in hordelings if p.value == 'hordeling'])
        self.current_hordelings = 'h'*hordelings
        self.max_hordelings = 'h'*hordelings
