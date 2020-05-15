from dataclasses import dataclass

from components.component import Component

PEASANT = 100
PLAYER = 50
DEFAULT = 0


@dataclass
class TargetValue(Component):
    value: int = DEFAULT
