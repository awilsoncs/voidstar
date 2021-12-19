import logging
from dataclasses import dataclass
from typing import List

from components import TimedActor
from components.delete_listeners.delete_listener import DeleteListener
from engine.core import log_debug


@dataclass
class Deleter(TimedActor):
    """Add this to an entity to have it delete itself after some time."""
    next_update: int = 0

    @log_debug(__name__)
    def act(self, scene):
        logging.info(f"EID#{self.entity}:Deleter event")
        delete_listeners: List[DeleteListener] = scene.cm.get(DeleteListener, query=lambda dl: dl.entity == self.entity)
        for listener in delete_listeners:
            listener.on_delete(scene)

        scene.cm.delete(self.entity)
