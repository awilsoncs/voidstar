from dataclasses import field, dataclass

from components.component import component_repr
from components.enums import Intention, ControlMode
from engine.constants import PRIORITY_MEDIUM
from engine.core import get_id


@dataclass
class Brain:
    """Provides control and other 'mind' information."""
    entity: int = None
    control_mode: ControlMode = None  # which system controls this entity
    priority: int = PRIORITY_MEDIUM
    take_turn: bool = False  # if True, take a turn on update

    # action management
    intention: Intention = Intention.NONE
    intention_target: int = None

    id: int = field(default_factory=get_id)

    def __repr__(self):
        return component_repr(self)
