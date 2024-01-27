from dataclasses import dataclass

from engine.components.component import Component


@dataclass
class PathfinderCost(Component):
    cost: int = 100
