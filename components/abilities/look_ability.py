from dataclasses import dataclass

from components import Coordinates
from components.abilities.ability import Ability
from components.brains.ability_actors.look_cursor_controller import LookCursorController
from content.cursor import make_cursor


@dataclass
class LookAbility(Ability):
    ability_title: str = "Look Around"
    unlock_cost: int = 0
    use_cost: int = 0

    def use(self, scene, dispatcher):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        cursor = make_cursor(coords.x, coords.y)
        scene.cm.add(LookCursorController(entity=self.entity, old_brain=dispatcher, cursor=cursor[0]))
        scene.cm.add(*cursor[1])
        scene.cm.stash_component(dispatcher)
