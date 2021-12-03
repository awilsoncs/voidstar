from dataclasses import dataclass

from components.actors.energy_actor import EnergyActor
from components.attack_start_listeners.attack_start_actor import AttackStartListener
from engine.core import log_debug


@dataclass
class StartAttack(EnergyActor):
    energy_cost: int = EnergyActor.INSTANT

    @log_debug(__name__)
    def act(self, scene):
        actors = scene.cm.get(AttackStartListener)
        for actor in actors:
            actor.on_attack_start(scene)

        scene.cm.delete_component(self)
