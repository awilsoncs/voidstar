from dataclasses import dataclass

from components.delete_listeners.delete_listener import DeleteListener
from components.events.events import Event


@dataclass
class Deleter(Event):
    """Add this to an entity to have it delete itself after some time."""
    next_update: int = 0

    def listener_type(self):
        return DeleteListener

    def notify(self, scene, listener):
        if listener.entity == self.entity:
            listener.on_delete(scene)

    def _after_notify(self, scene):
        scene.cm.delete(self.entity)
