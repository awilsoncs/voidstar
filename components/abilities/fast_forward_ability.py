from dataclasses import dataclass

from components.abilities.ability import Ability
from components.events.fast_forward import FastForward


@dataclass
class FastForwardAbility(Ability):
    ability_title: str = "Fast Forward"
    unlock_cost: int = 0
    use_cost: int = 0

    def use(self, scene, dispatcher):
        scene.cm.add(FastForward(entity=self.entity))
