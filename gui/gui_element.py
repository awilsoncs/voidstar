from typing import List
from uuid import uuid4

import tcod


class GuiElement:
    """Form the base behavior of a GuiElement."""
    def __init__(self, x, y, name=None, single_shot=False):
        self.__x = x
        self.__y = y
        self.name = name if name else uuid4()
        self.children = []
        self.single_shot = single_shot  # if true, the GUI won't store this element, but will render it immediately

    @property
    def x(self) -> int:
        return self._resolve(self.__x)

    @property
    def y(self) -> int:
        return self._resolve(self.__y)

    def on_load(self) -> None:
        """
        Perform any actions necessary before rendering.

        Called while pushing the scene, after the scene's on_load method.
        """
        pass

    def render_to_screen(self, panel: tcod.console.Console) -> None:
        """Render this element, then each child."""
        self.render(panel)
        for child in self.children:
            child.render_to_screen(panel)

    def render(self, panel: tcod.console.Console) -> None:
        raise NotImplementedError("GuiElement must define render()")

    def add(self, *children: List['GuiElement']) -> None:
        for child in children:
            self.children.append(child)

    @staticmethod
    def _resolve(value):
        return value() if callable(value) else value
