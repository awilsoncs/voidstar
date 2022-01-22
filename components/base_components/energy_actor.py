from abc import ABC
from dataclasses import dataclass

from components.base_components.actor import Actor
from engine.constants import PRIORITY_MEDIUM


@dataclass
class EnergyActor(Actor, ABC):
    """Provides control and other 'mind' information."""
    INSTANT = 0
    QUARTER_HOUR = 3
    HALF_HOUR = 6
    FAST = 8
    HOURLY = 12
    VERY_SLOW = 24
    DAILY = 288

    priority: int = PRIORITY_MEDIUM
    energy: int = 0
    energy_cost: int = HOURLY
    is_recharging: bool = True  # True if the entity should accept energy

    def can_act(self) -> bool:
        return self.energy >= 0

    def pass_turn(self, time=None) -> None:
        if time is None:
            time = self.energy_cost
        self.energy -= time
