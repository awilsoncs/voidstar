from typing import Tuple

from components import Brain, Senses
from components.coordinates import Coordinates
from components.enums import Intention
from systems.utilities import get_blocking_object, retract_turn, retract_intention


def run(scene):
    for brain in get_brains_with_step_intention(scene):
        entity = brain.entity
        if can_step(scene, entity, STEP_VECTORS[brain.intention]):
            move(scene, entity, STEP_VECTORS[brain.intention])
            dirty_senses(scene, entity)
            retract_intention(scene, entity)
            retract_turn(scene, entity)


def get_brains_with_step_intention(scene):
    return [
        brain
        for brain in scene.cm.get(Brain)
        if brain.intention in {
            Intention.STEP_NORTH,
            Intention.STEP_SOUTH,
            Intention.STEP_EAST,
            Intention.STEP_WEST
        }
    ]


STEP_VECTORS = {
    Intention.STEP_NORTH: (0, -1),
    Intention.STEP_SOUTH: (0, 1),
    Intention.STEP_EAST: (1, 0),
    Intention.STEP_WEST: (-1, 0)
}


def can_step(scene, entity, step_action) -> bool:
    """Validate a step action."""
    entity_coords = scene.cm.get_one(Coordinates, entity)
    target_x = entity_coords.x + step_action[0]
    target_y = entity_coords.y + step_action[1]
    blocking_object = get_blocking_object(scene.cm, target_x, target_y)
    return not (
        entity_coords.blocks and
        blocking_object
    )


def dirty_senses(scene, entity):
    if entity == 0:
        senses = scene.cm.get_one(Senses, entity=0)
        if senses:
            senses.dirty = True


def move(scene, entity: int, vector: Tuple[int, int]):
    """
    Perform a move action.

    This function is intended to be the final call before performing the actual move,
    and no validation occurs herein (except possibly to avoid crashes).
    """
    coords = scene.cm.get_one(Coordinates, entity=entity)
    if coords:
        move_coords(coords, vector)


def move_coords(coords: Coordinates, vector: Tuple[int, int]):
    coords.x += vector[0]
    coords.y += vector[1]
