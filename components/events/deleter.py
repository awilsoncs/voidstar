from dataclasses import dataclass, field
import random

from components import TimedActor
from engine import core
from engine.core import log_debug


def get_delete_delay():
    return random.randrange(1000, 15000) + core.time_ms()


@dataclass
class Deleter(TimedActor):
    """Add this to an entity to have it delete itself after some time."""
    next_update: int = field(default_factory=get_delete_delay)

    @log_debug(__name__)
    def act(self, scene):
        scene.cm.delete(self.entity)
