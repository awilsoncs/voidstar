from dataclasses import dataclass

from components.death_listeners.death_listener import DeathListener
from components.events.events import Event
from engine import constants


@dataclass
class Die(Event):
    killer: int = constants.INVALID

    def listener_type(self):
        return DeathListener

    def notify(self, scene, listener):
        if listener.entity == self.entity:
            listener.on_die(scene)

    def _after_notify(self, scene):
        scene.cm.delete(self.entity)
