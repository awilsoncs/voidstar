from dataclasses import dataclass

from engine.component import Component


@dataclass
class PathfinderCost(Component):
    cost: int = 0
