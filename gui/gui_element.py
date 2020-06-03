from dataclasses import dataclass, field

import tcod

from engine.core import get_id


@dataclass
class GuiElement:
    """Form the base behavior of a GuiElement."""
    x: int = 0
    y: int = 0
    name: str = ''
    id: int = field(default_factory=get_id)
    single_shot: bool = False    # if true, the GUI won't store this element, but will render it immediately

    def on_load(self) -> None:
        """
        Perform any actions necessary before rendering.

        Called while pushing the scene, after the scene's on_load method.
        """
        pass

    def update(self, scene) -> None:
        pass

    def render(self, panel: tcod.console.Console) -> None:
        raise NotImplementedError("GuiElement must define render()")
