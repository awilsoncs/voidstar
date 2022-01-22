from dataclasses import dataclass

from components.base_components.component import Component

PEASANT = 100
COW = 100
HAUNCH = 1000
PLAYER = 50
CROPS = 75
DEFAULT = 0


@dataclass
class TargetValue(Component):
    value: int = DEFAULT
