from dataclasses import dataclass

from components.abilities.ability import Ability
from components.enums import Intention
from components.events.fast_forward import FastForward


@dataclass
class FastForwardAbility(Ability):
    ability_title: str = "Fast Forward"
    unlock_cost: int = 0
    use_cost: int = 0
    intention: Intention = Intention.FAST_FORWARD

    def use(self, scene, dispatcher):
        scene.cm.add(FastForward(entity=self.entity))
