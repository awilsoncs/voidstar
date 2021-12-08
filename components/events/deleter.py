from dataclasses import dataclass

from components import TimedActor
from engine.core import log_debug


@dataclass
class Deleter(TimedActor):
    """Add this to an entity to have it delete itself after some time."""
    next_update: int = 0

    @log_debug(__name__)
    def act(self, scene):
        scene.cm.delete(self.entity)
