from dataclasses import dataclass
from enum import Enum

from engine.components.component import Component
from engine import palettes


@dataclass
class Appearance(Component):
    """Define an entity's base appearance."""
    class RenderMode(str, Enum):
        # entity appears dimmed in hidden areas
        NORMAL = 'NORMAL'
        # entity appears as normal even in hidden areas, e.g. cursors
        HIGH_VEE = 'HIGH_VEE'
        # entity does not appear at all in hidden areas
        STEALTHY = 'STEALTHY'

    symbol: str = ' '
    color: tuple = palettes.WHITE
    bg_color: tuple = palettes.BACKGROUND
    render_mode: RenderMode = RenderMode.NORMAL

    def to_tile(self):
        """Return the Appearance in the tcod Tile format."""
        return (
            ord(self.symbol),
            (*self.color, 255),
            (*self.bg_color, 255)
        )

    def set_appearance(self, symbol, fg, bg):
        self.symbol = symbol
        self.color = fg
        self.bg_color = bg
