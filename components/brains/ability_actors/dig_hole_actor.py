from dataclasses import dataclass
from typing import List

import tcod

import settings
from components import Coordinates, Entity
from components.actors.energy_actor import EnergyActor
from components.brains.temporary_brain import TemporaryBrain
from components.events.die_events import Die
from components.enums import Intention
from components.diggable import Diggable
from content.terrain.dirt import make_dirt
from content.terrain.hole import make_hole
from engine import core, palettes


@dataclass
class DigHoleActor(TemporaryBrain):
    energy_cost: int = EnergyActor.INSTANT

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

    def _dig_hole(self, scene, direction):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        x = coords.x
        y = coords.y
        direction = STEP_VECTORS[direction]
        hole_x = x+direction[0]
        hole_y = y+direction[1]
        if not _in_bounds(hole_x, hole_y):
            scene.message("You can't build outside of the town.", color=palettes.WHITE)
            self.back_out(scene)
        elif _is_empty(scene, hole_x, hole_y):
            self._apply_dig_hole(hole_x, hole_y, scene)
        else:
            diggable_entities = _get_diggables(scene, hole_x, hole_y)
            if diggable_entities:
                scene.gold -= 2
                entity = diggable_entities.pop()
                scene.cm.add(Die(entity=entity, killer=self.entity))
                diggable = scene.cm.get_one(Diggable, entity=entity)
                if diggable.is_free:
                    # there's a dirt here, skip straight to digging the new hole
                    self._apply_dig_hole(hole_x, hole_y, scene)
                    return
                else:
                    entity = scene.cm.get_one(Entity, entity=entity)
                    scene.message(f"You dug up {entity.name}.")

                dirt = make_dirt(hole_x, hole_y)
                scene.cm.add(*dirt[1])
                old_actor = self.back_out(scene)
                old_actor.pass_turn()
            else:
                self.back_out(scene)

    def _apply_dig_hole(self, hole_x, hole_y, scene):
        scene.message("You dug a deep hole.")
        hole = make_hole(hole_x, hole_y)
        scene.cm.add(*hole[1])
        scene.gold -= 2
        old_actor = self.back_out(scene)
        old_actor.pass_turn()


def _in_bounds(x, y):
    in_x_bounds = 0 < x < settings.MAP_WIDTH - 1
    in_y_bounds = 0 < y < settings.MAP_HEIGHT - 1
    return in_y_bounds and in_x_bounds


def _is_empty(scene, x, y) -> bool:
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
