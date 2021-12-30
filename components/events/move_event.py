from dataclasses import dataclass

from engine.component import Component


@dataclass
class MoveEvent(Component):
    dx: int = 0
    dy: int = 0
    is_forced: int = 0
