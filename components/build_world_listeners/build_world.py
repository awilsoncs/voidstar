from dataclasses import dataclass

from components.build_world_listeners.build_world_listeners import BuildWorldListener
from components.events.events import Event


@dataclass
class BuildWorld(Event):
    """Event to trigger world building steps."""

    def listener_type(self):
        return BuildWorldListener

    def notify(self, scene, listener):
        listener.on_build_world(scene)
