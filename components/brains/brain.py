from dataclasses import dataclass

from engine.component import Component
from components.enums import Intention, ControlMode
from engine.constants import PRIORITY_MEDIUM


@dataclass
class Brain(Component):
    """Provides control and other 'mind' information."""
    control_mode: ControlMode = None  # which system controls this entity
    priority: int = PRIORITY_MEDIUM

    # action management
    intention: Intention = Intention.NONE
    intention_target: int = None
