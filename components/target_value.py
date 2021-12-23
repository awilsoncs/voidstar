from dataclasses import dataclass

from engine.component import Component

PEASANT = 100
PLAYER = 25
CROPS = 50
DEFAULT = 0


@dataclass
class TargetValue(Component):
    value: int = DEFAULT
