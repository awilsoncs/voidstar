from dataclasses import dataclass
from engine.components.events import Event
from components.peasant_listeners.peasant_added_listener import PeasantAddedListener


@dataclass
class PeasantAddedEvent(Event):
    def listener_type(self):
        return PeasantAddedListener

    def notify(self, scene, listener):
        listener.on_peasant_added(scene)
