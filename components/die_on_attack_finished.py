from dataclasses import dataclass

from components.events.attack_events import OnAttackFinishedListener
from components.events.die_events import Die


@dataclass
class DieOnAttackFinished(OnAttackFinishedListener):
    def on_attack_finished(self, scene, caller):
        if caller == self.entity:
            scene.cm.add(Die(entity=self.entity))
