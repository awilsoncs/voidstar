from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple

import tcod

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.enums import Intention
from components.brains.brain import Brain
from engine import constants, core
from engine.component import Component


@dataclass
class PlaceThingActor(Brain, ABC):
    energy_cost: int = EnergyActor.INSTANT
    old_actor: int = constants.INVALID
    gold_cost: int = constants.INVALID

    def act(self, scene) -> None:
        key_event = core.get_key_event()
        if key_event:
            key_event = key_event.sym
            intention = KEY_ACTION_MAP.get(key_event, None)
            if intention in {
                Intention.STEP_NORTH,
                Intention.STEP_EAST,
                Intention.STEP_WEST,
                Intention.STEP_SOUTH
            }:
                self._place_thing(scene, intention)
            elif intention is Intention.BACK:
                self.back_out(scene)

    @abstractmethod
    def make_thing(self, x: int, y: int) -> Tuple[int, List[Component]]:
        raise NotImplementedError()

    def _place_thing(self, scene, direction):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        x = coords.x
        y = coords.y
        direction = STEP_VECTORS[direction]
        thing_x = x+direction[0]
        thing_y = y+direction[1]
        if is_buildable(scene, thing_x, thing_y):
            thing = self.make_thing(thing_x, thing_y)
            scene.cm.add(*thing[1])
            scene.gold -= self.gold_cost
            old_actor = self.back_out(scene)
            old_actor.pass_turn()
        else:
            self.back_out(scene)

    def back_out(self, scene):
        old_actor = scene.cm.unstash_component(self.old_actor)
        blinker = scene.cm.get_one(AnimationBlinker, entity=self.entity)
        blinker.stop(scene)
        scene.cm.delete_component(blinker)
        scene.cm.delete_component(self)
        return old_actor


def is_buildable(scene, x, y):
    target_coords = scene.cm.get(
        Coordinates,
        query=lambda coords: coords.x == x and coords.y == y and not coords.buildable
    )
    return not target_coords


KEY_ACTION_MAP = {
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_ESCAPE: Intention.BACK
}

STEP_VECTORS = {
    Intention.STEP_NORTH: (0, -1),
    Intention.STEP_SOUTH: (0, 1),
    Intention.STEP_EAST: (1, 0),
    Intention.STEP_WEST: (-1, 0),
    Intention.STEP_NORTH_EAST: (1, -1),
    Intention.STEP_NORTH_WEST: (-1, -1),
    Intention.STEP_SOUTH_EAST: (1, 1),
    Intention.STEP_SOUTH_WEST: (-1, 1)
}
