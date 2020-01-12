from sqlalchemy import Column, Integer, String

from components.component import Component, component_repr
from engine import colors
from engine.types import Color


class Appearance(Component):
    """Define an entity's base appearance."""
    __tablename__ = 'appearance'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    symbol = Column(String(1))
    color = Column(Color(7), default=colors.white)
    bg_color = Column(Color(7), default=colors.black)

    def to_tile(self):
        """Return the Appearance in the tcod Tile format."""
        return (
            ord(self.symbol),
            (*self.color, 255),
            (*self.bg_color, 255)
        )

    def __repr__(self):
        return component_repr(self)
