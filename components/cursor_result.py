from dataclasses import dataclass

from engine.component import Component


@dataclass
class CursorResult(Component):
    x: int = None
    y: int = None
