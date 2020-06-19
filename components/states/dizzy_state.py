from dataclasses import dataclass

from engine.component import Component
from engine import core


@dataclass
class DizzyState(Component):
    """While dizzy, the entity takes random steps."""
    duration: int = 3
    next_turn: int = core.time_ms() + 2900
