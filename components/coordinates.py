import math
from typing import Tuple

from sqlalchemy import Column, Integer, Boolean

from components.component import Component, component_repr
from engine.constants import PRIORITY_MEDIUM


class Coordinates(Component):
    """Provide location information."""
    # TODO 'blocks' and 'blocks_sight' should be part of a material component, not the coordinate
    __tablename__ = 'coordinates'
    id = Column(Integer, primary_key=True)
    entity = Column(Integer, index=True, nullable=False)
    x = Column(Integer, index=True)
    y = Column(Integer, index=True)
    blocks = Column(Boolean, default=False)
    blocks_sight = Column(Boolean, default=False)
    priority = Column(Integer, default=PRIORITY_MEDIUM)
    terrain = Column(Boolean, default=False, nullable=False)

    @property
    def position(self) -> Tuple[int, int]:
        """Get a position tuple"""
        return self.x, self.y

    def direction_towards(self, other):
        from_x = self.x
        from_y = self.y
        to_x = other.x
        to_y = other.y

        dx = to_x - from_x
        dy = to_y - from_y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # normalize it to length 1 (preserving direction), then round it and
        # convert to integer so the movement is restricted to the map grid
        if distance != 0:
            dx = int(round(dx / distance))
            dy = int(round(dy / distance))
            return dx, dy
        else:
            return 0, 0

    def distance_from(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return component_repr(self)
