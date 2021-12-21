from dataclasses import dataclass

from engine.component import Component


@dataclass
class MoveCost(Component):
    """A component to increase or decrease the energy cost of moving."""
    factor: float = 1.0
