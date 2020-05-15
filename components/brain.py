from dataclasses import dataclass

from components.component import Component
from components.enums import Intention, ControlMode
from engine.constants import PRIORITY_MEDIUM


@dataclass
class Brain(Component):
    """Provides control and other 'mind' information."""
    control_mode: ControlMode = None  # which system controls this entity
    priority: int = PRIORITY_MEDIUM
    take_turn: bool = False  # if True, take a turn on update

    # action management
    intention: Intention = Intention.NONE
    intention_target: int = None
