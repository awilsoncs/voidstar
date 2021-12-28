from dataclasses import dataclass

from components.abilities.ability import Ability
from components.enums import Intention
from components.show_debug import ShowDebug


@dataclass
class DebugAbility(Ability):
    ability_title: str = "Show Debug"
    unlock_cost: int = 0
    use_cost: int = 0
    intention: Intention = Intention.SHOW_DEBUG_SCREEN

    def use(self, scene, dispatcher):
        scene.cm.add(ShowDebug(entity=self.entity))
