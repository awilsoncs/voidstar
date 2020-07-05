from dataclasses import dataclass

from engine.component import Component
from components.enums import Intention, ControlMode
from engine.constants import PRIORITY_MEDIUM


@dataclass
class TimedActor(Component):
    SLOWEST = 100000
    QUARTER_HOUR = 250
    HALF_HOUR = 500
    HOURLY = 1000
    DAILY = 10000

    REAL_TIME = 0

    """Provides control and other 'mind' information."""
    control_mode: ControlMode = None  # which system controls this entity
    priority: int = PRIORITY_MEDIUM
    timer_delay: int = HALF_HOUR
    next_update: int = 0

    # action management
    intention: Intention = Intention.NONE
    intention_target: int = None
