from sqlalchemy import Column, Integer, String

from components.component import Component, component_repr


class Attack(Component):
    __tablename__ = 'attack'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, unique=True, index=True, nullable=False)
    damage = Column(String, nullable=False)

    def to_tile(self):
        """Return the Appearance in the tcod Tile format."""
        return (
            ord(self.symbol),
            (*self.color, 255),
            (*self.bg_color, 255)
        )

    def __repr__(self):
        return component_repr(self)
