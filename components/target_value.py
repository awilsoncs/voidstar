from dataclasses import dataclass

from engine.component import Component

PEASANT = 100
PLAYER = 50
CROPS = 25
DEFAULT = 0


@dataclass
class TargetValue(Component):
    value: int = DEFAULT
