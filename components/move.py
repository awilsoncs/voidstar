from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from engine.component import Component


@dataclass
class Move(Component):
    energy_cost: int = EnergyActor.HOURLY
