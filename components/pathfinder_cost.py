from dataclasses import dataclass

from engine.base_components.component import Component


@dataclass
class PathfinderCost(Component):
    cost: int = 100
