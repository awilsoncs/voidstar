from dataclasses import dataclass, field
from typing import List

from gui.gui_element import GuiElement


@dataclass
class VerticalAnchor(GuiElement):
    next_row: int = 0
    elements: List = field(default_factory=list)

    def add_element(self, element):
        self.next_row += 1
        element.y = self.next_row
        self.elements.append(element)

    def add_space(self, n):
        self.next_row += n

    def update(self, scene):
        for element in self.elements:
            element.update(scene)

    def render(self, panel):
        for element in self.elements:
            element.render(panel)
