from dataclasses import dataclass

from engine.base_components.energy_actor import EnergyActor
from engine.base_components.component import Component


@dataclass
class Move(Component):
    energy_cost: int = EnergyActor.HOURLY
