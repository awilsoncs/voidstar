from dataclasses import dataclass

from engine.components.energy_actor import EnergyActor
from engine.components.component import Component


@dataclass
class Move(Component):
    energy_cost: int = EnergyActor.HOURLY
