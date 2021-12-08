from dataclasses import dataclass

from engine.component import Component
from engine import palettes


@dataclass
class Appearance(Component):
    """Define an entity's base appearance."""
    symbol: str = ' '
    color: tuple = palettes.WHITE
    bg_color: tuple = palettes.BACKGROUND

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
