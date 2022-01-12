from dataclasses import dataclass

from components.events.events import Event
from components.terrain_changed_listeners.terrain_changed_listener import TerrainChangedListener


@dataclass
class TerrainChangedEvent(Event):

    def listener_type(self):
        return TerrainChangedListener

    def notify(self, scene, listener):
        listener.on_terrain_changed(scene)
