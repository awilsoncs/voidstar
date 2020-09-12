from dataclasses import dataclass, field
import random

from components import TimedActor
from engine.core import log_debug


def get_delete_delay():
    return random.randrange(5000, 10000)


@dataclass
class Deleter(TimedActor):
    """Add this to an entity to have it delete itself after some time."""
    timer_delay: int = field(default_factory=get_delete_delay)

    @log_debug(__name__)
    def act(self, scene):
        if self.next_update:
            scene.cm.delete(self.entity)
