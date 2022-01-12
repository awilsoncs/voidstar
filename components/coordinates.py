import math
from dataclasses import dataclass
from typing import Tuple

from engine.component import Component
from engine.constants import PRIORITY_MEDIUM


@dataclass
class Coordinates(Component):
    """Provide location information."""
    x: int = None
    y: int = None
    priority: int = PRIORITY_MEDIUM
    buildable: bool = False

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

    def distance_from(self, other: 'Coordinates') -> float:
        return self.distance_from_point(other.x, other.y)

    def distance_from_point(self, x: int, y: int) -> float:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def is_at(self, other: "Coordinates") -> bool:
        return self.x == other.x and self.y == other.y

    def is_at_point(self, point: Tuple[int, int]) -> bool:
        return self.x == point[0] and self.y == point[1]
