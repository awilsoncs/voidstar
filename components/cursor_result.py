from dataclasses import dataclass

from components.component import Component


@dataclass
class CursorResult(Component):
    x: int = None
    y: int = None
