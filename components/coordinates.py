import math
from dataclasses import dataclass, field
from typing import Tuple

from components.component import component_repr
from engine.constants import PRIORITY_MEDIUM
from engine.core import get_id


@dataclass
class Coordinates:
    """Provide location information."""
    entity: int = None
    x: int = None
    y: int = None
    priority: int = PRIORITY_MEDIUM
    terrain: bool = False
    id: int = field(default_factory=get_id)

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
