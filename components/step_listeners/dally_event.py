from dataclasses import dataclass

from engine.components.events import Event
from components.step_listeners.dally_listener import DallyListener


@dataclass
class DallyEvent(Event):

    def notify(self, scene, listener):
        listener.on_dally(scene)

    def listener_type(self):
        return DallyListener
