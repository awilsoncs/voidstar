from dataclasses import dataclass
from math import sqrt

from components import Coordinates
from components.abilities.ability import Ability
from components.actors.energy_actor import EnergyActor
from components.actions.attack_action import AttackAction
from components.states.dizzy_state import DizzyState
from content.attacks import thwack_animation, thwack_dizzy_animation
from systems.utilities import get_enemies_in_range


@dataclass
class ThwackAbility(Ability, EnergyActor):
    ability_title: str = "Thwack"
    unlock_cost: int = 0
    use_cost: int = 0
    count: int = 0
    max: int = 3
    is_recharging: bool = False

    def use(self, scene, dispatcher):
        self.thwack(scene, dispatcher)

    def thwack(self, scene, dispatcher):
        if self.count > 0:
            # determine whether this thwacktivity is legal
            self.is_recharging = True
            self.count -= 1

            # convert the thwack action to an attack action each adjacent enemy
            thwackables = get_enemies_in_range(scene, self.entity, max_range=sqrt(2))
            attacks = [AttackAction(entity=self.entity, target=t, damage=1) for t in thwackables]

            for attack in attacks:
                scene.cm.add(attack)

            thwacker_coords = scene.cm.get_one(Coordinates, entity=self.entity)

            if self.count > 0:
                scene.cm.add(*thwack_animation(self.entity, thwacker_coords.x, thwacker_coords.y)[1])
            else:
                scene.warn("You thwacked yourself dizzy!")
                scene.cm.add(*thwack_dizzy_animation(self.entity, thwacker_coords.x, thwacker_coords.y)[1])
        brain = scene.cm.get_component_by_id(dispatcher)
        brain.pass_turn()
        self.pass_turn()

        if self.count <= 0:
            self.apply_dizzy(scene)

    def apply_dizzy(self, scene):
        scene.cm.add(DizzyState(entity=self.entity, duration=3))

    def act(self, scene):
        self.count = min(self.max, self.count + 1)
        self.is_recharging = self.count < self.max
        self.pass_turn()

