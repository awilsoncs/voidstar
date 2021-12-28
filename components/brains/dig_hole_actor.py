from dataclasses import dataclass
from typing import List

import tcod

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.death_listeners.die import Die
from components.enums import Intention
from components.diggable import Diggable
from components.brains.brain import Brain
from content.terrain.dirt import make_dirt
from content.terrain.hole import make_hole
from engine import constants, core


@dataclass
class DigHoleActor(Brain):
    energy_cost: int = EnergyActor.INSTANT
    old_actor: int = constants.INVALID

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
                self._dig_hole(scene, intention)
            elif intention is Intention.BACK:
                self.back_out(scene)

    def _dig_hole(self, scene, direction, old_actor=None):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        x = coords.x
        y = coords.y
        direction = STEP_VECTORS[direction]
        hole_x = x+direction[0]
        hole_y = y+direction[1]
        if _is_diggable(scene, hole_x, hole_y):
            self._apply_dig_hole(hole_x, hole_y, scene)
        else:
            diggable_entities = _get_diggables(scene, hole_x, hole_y)
            if diggable_entities:
                scene.gold -= 2
                entity = diggable_entities.pop()
                scene.cm.add(Die(entity=entity))
                diggable = scene.cm.get_one(Diggable, entity=entity)
                if diggable.is_free:
                    # there's a dirt here, skip straight to digging the new hole
                    self._apply_dig_hole(hole_x, hole_y, scene)
                    return

                dirt = make_dirt(hole_x, hole_y)
                scene.cm.add(*dirt[1])
                old_actor = self.back_out(scene)
                old_actor.pass_turn()
            else:
                self.back_out(scene)

    def _apply_dig_hole(self, hole_x, hole_y, scene):
        hole = make_hole(hole_x, hole_y)
        scene.cm.add(*hole[1])
        scene.gold -= 2
        old_actor = self.back_out(scene)
        old_actor.pass_turn()

    def back_out(self, scene):
        old_actor = scene.cm.unstash_component(self.old_actor)
        blinker = scene.cm.get_one(AnimationBlinker, entity=self.entity)
        blinker.stop(scene)
        scene.cm.delete_component(blinker)
        scene.cm.delete_component(self)
        return old_actor


def _is_diggable(scene, x, y) -> bool:
    target_coords = scene.cm.get(
        Coordinates,
        query=lambda coords: coords.x == x and coords.y == y and not coords.buildable
    )
    return not target_coords


def _get_diggables(scene, x, y) -> List[int]:
    """Return True if there's something that can be removed by digging."""
    fillable_entities = scene.cm.get(
        Coordinates,
        query=lambda coords: coords.x == x and coords.y == y and scene.cm.get_one(Diggable, entity=coords.entity)
    )
    return [fe.entity for fe in sorted(fillable_entities, key=lambda fe: fe.priority)]


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
