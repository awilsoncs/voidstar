from dataclasses import dataclass
from typing import List

from components import Coordinates, Attributes
from components.actions.attack_action import AttackAction
from components.base_components.energy_actor import EnergyActor
from components.events.die_events import Die
from content.explosion import make_explosion
from content.states import character_animation
from engine.utilities import get_3_by_3_square


@dataclass
class BombActor(EnergyActor):
    turns: int = 3
    energy: int = -1 * EnergyActor.HOURLY

    def act(self, scene) -> None:
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        if self.turns <= 0:
            self._explode(scene)
            self.pass_turn()
            return
        scene.cm.add(*character_animation(coords.x, coords.y, f"{self.turns}")[1])
        self.turns -= 1
        self.pass_turn()

    def _explode(self, scene):
        attributes: List[Attributes] = scene.cm.get(Attributes)
        targets = set()
        for attribute in attributes:
            if is_adjacent(scene, attribute.entity, self.entity):
                targets.add(attribute.entity)
        for target in list(targets):
            scene.cm.add(AttackAction(entity=self.entity, target=target, damage=3))

        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        explosion_area = get_3_by_3_square(coords.x, coords.y)
        for explosion in explosion_area:
            scene.cm.add(*make_explosion(explosion[0], explosion[1])[1])

        scene.warn("A bomb exploded!")
        scene.cm.add(Die(entity=self.entity, killer=self.entity))

    def can_act(self) -> bool:
        return self.energy >= 0


def is_adjacent(scene, first: int, second: int):
    first_coord: Coordinates = scene.cm.get_one(Coordinates, entity=first)
    second_coord: Coordinates = scene.cm.get_one(Coordinates, entity=second)
    return first_coord and second_coord and first_coord.distance_from(second_coord) < 2