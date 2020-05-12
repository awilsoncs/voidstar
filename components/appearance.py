from dataclasses import field, dataclass

from components.component import Component, component_repr
from engine import colors
from engine.core import get_id


@dataclass
class Appearance:
    """Define an entity's base appearance."""
    entity: int
    symbol: str
    color: tuple = colors.white
    bg_color: tuple = colors.black
    id: int = field(default_factory=get_id)

    def to_tile(self):
        """Return the Appearance in the tcod Tile format."""
        return (
            ord(self.symbol),
            (*self.color, 255),
            (*self.bg_color, 255)
        )

    def __repr__(self):
        return component_repr(self)
