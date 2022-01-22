from dataclasses import dataclass

from components.base_components.component import Component
from components.base_components.energy_actor import EnergyActor


@dataclass
class Move(Component):
    energy_cost: int = EnergyActor.HOURLY
