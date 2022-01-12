from dataclasses import dataclass

from components.attack_start_listeners.attack_start_actor import AttackStartListener
from components.events.events import Event


@dataclass
class StartAttack(Event):

    def listener_type(self):
        return AttackStartListener

    def notify(self, scene, listener):
        listener.on_attack_start(scene)
