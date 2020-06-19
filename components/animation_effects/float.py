from dataclasses import dataclass

from engine.component import Component
from engine import core


@dataclass
class AnimationFloat(Component):
    """Randomly float up or right."""
    duration: int = 10
    delay_ms: int = 250  # how long to wait between steps
    next_update_time: int = core.time_ms()
    delete_on_complete: bool = True  # whether to delete the entity when the path is done
