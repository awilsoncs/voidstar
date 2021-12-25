from dataclasses import dataclass
from typing import List

import tcod

from components import Coordinates
from components.actors.energy_actor import EnergyActor
from components.animation_effects.blinker import AnimationBlinker
from components.death_listeners.die import Die
from components.enums import Intention
from components.diggable import Diggable
from components.Sellable import Sellable
from content.terrain.dirt import make_dirt
from content.terrain.hole import make_hole
from engine import constants, core
from engine.types import EntityId


@dataclass
class SellThingActor(EnergyActor):
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
                self._sell_thing(scene, intention)
            elif intention is Intention.BACK:
                self.back_out(scene)

    def _sell_thing(self, scene, direction):
        coords = scene.cm.get_one(Coordinates, entity=self.entity)
        x = coords.x
        y = coords.y
        direction = STEP_VECTORS[direction]
        hole_x = x+direction[0]
        hole_y = y+direction[1]
        sellables = _get_sellables(scene, (hole_x, hole_y))
        if sellables:
            assert len(sellables) == 1, "found more than one diggable on a tile"
            entity = sellables.pop()
            scene.cm.add(Die(entity=entity))
            sellable: Sellable = scene.cm.get_one(Sellable, entity=entity)
            scene.gold += sellable.value
            dirt = make_dirt(hole_x, hole_y)
            scene.cm.add(*dirt[1])
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


def _get_sellables(scene, point) -> List[EntityId]:
    """Return a list of sellable EntityIds at this point."""
    sellables = set(scene.cm.get(Sellable, project=lambda s: s.entity))
    nearby = [
        c.entity for c in scene.cm.get(Coordinates)
        if c.distance_from_point(point[0], point[1]) == 0 and c.entity in sellables
    ]
    return nearby


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
