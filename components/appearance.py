from dataclasses import dataclass

from engine.component import Component
from engine import colors


@dataclass
class Appearance(Component):
    """Define an entity's base appearance."""
    symbol: str = ' '
    color: tuple = colors.white
    bg_color: tuple = colors.black

    def to_tile(self):
        """Return the Appearance in the tcod Tile format."""
        return (
            ord(self.symbol),
            (*self.color, 255),
            (*self.bg_color, 255)
        )
