from abc import ABC
from dataclasses import dataclass

from components.actors.actor import Actor
from components.enums import Intention, ControlMode
from engine.constants import PRIORITY_MEDIUM


@dataclass
class EnergyActor(Actor, ABC):
    """Provides control and other 'mind' information."""

    INSTANT = 0
    QUARTER_HOUR = 3
    HALF_HOUR = 6
    HOURLY = 12
    DAILY = 288

    control_mode: ControlMode = None  # which system controls this entity
    priority: int = PRIORITY_MEDIUM
    energy: int = 0
    energy_cost: int = HOURLY
    is_recharging: bool = True  # True if the entity should accept energy

    # action management
    intention: Intention = Intention.NONE
    intention_target: int = None

    def can_act(self) -> bool:
        return self.energy >= 0

    def pass_turn(self, time=None) -> None:
        if time is None:
            time = self.energy_cost
        self.energy -= time
