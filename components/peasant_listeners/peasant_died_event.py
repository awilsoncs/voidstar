from dataclasses import dataclass

from components.events.events import Event
from components.peasant_listeners.peasant_died_listener import PeasantDiedListener


@dataclass
class PeasantDiedEvent(Event):

    def listener_type(self):
        return PeasantDiedListener

    def notify(self, scene, listener):
        listener.on_peasant_died(scene)
