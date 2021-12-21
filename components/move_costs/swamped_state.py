from dataclasses import dataclass

from components.move_costs.move_cost import MoveCost
from engine.component import Component


@dataclass
class Swamped(MoveCost):
    factor: float = 2.0


@dataclass
class Swamper(Component):
    pass
