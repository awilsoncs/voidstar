from abc import ABC, abstractmethod
from dataclasses import dataclass

import tcod

import settings
from components import Coordinates
from engine.components.energy_actor import EnergyActor
from components.brains.brain import Brain
from components.enums import Intention
from engine import constants, core


@dataclass
class PainterBrain(Brain, ABC):
    """Provide a base class for debug object placing controllers."""
    energy_cost: int = EnergyActor.INSTANT
    cursor: int = constants.INVALID

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
                self._move_cursor(scene, intention)
            if intention is Intention.USE_ABILITY:
                self._paint(scene)
            elif intention is Intention.BACK:
                scene.cm.delete(self.cursor)
                self.back_out(scene)

    def _paint(self, scene):
        coords = scene.cm.get_one(Coordinates, entity=self.cursor)
        scene.cm.add(*self.paint_one(scene, coords.position))

    @abstractmethod
    def paint_one(self, scene, position):
        pass

    def _move_cursor(self, scene, intention):
        cursor_coords = scene.cm.get_one(Coordinates, entity=self.cursor)
        direction = STEP_VECTORS[intention]
        cursor_coords.x += direction[0]
        cursor_coords.y += direction[1]
        if 0 > cursor_coords.x or cursor_coords.x >= settings.MAP_FRAME_WIDTH:
            cursor_coords.x -= direction[0]
        if 0 > cursor_coords.y or cursor_coords.y >= settings.MAP_FRAME_HEIGHT:
            cursor_coords.y -= direction[1]


KEY_ACTION_MAP = {
    tcod.event.K_UP: Intention.STEP_NORTH,
    tcod.event.K_DOWN: Intention.STEP_SOUTH,
    tcod.event.K_RIGHT: Intention.STEP_EAST,
    tcod.event.K_LEFT: Intention.STEP_WEST,
    tcod.event.K_ESCAPE: Intention.BACK,
    tcod.event.K_SPACE: Intention.USE_ABILITY
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
