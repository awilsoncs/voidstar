from dataclasses import dataclass

from components.abilities.ability import Ability


@dataclass
class NullAbility(Ability):
    ability_title: str = "No Abilities"
    unlock_cost: int = 0
    use_cost: int = 0

    def use(self, scene, dispatcher):
        pass
