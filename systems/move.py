from typing import Tuple

from components import Brain, Senses
from components.coordinates import Coordinates
from components.enums import Intention
from components.material import Material
from systems.utilities import get_blocking_object, retract_turn, retract_intention


def run(scene):
    for brain in get_brains_with_step_intention(scene):
        entity = brain.entity

        # is there a hostile in that direction? if so, bump attack
        # is there a non-hostile blocking entity in that direction? if so, too bad
        # otherwise, move them

        if can_step(scene, entity, STEP_VECTORS[brain.intention]):
            # do move
            move(scene, entity, STEP_VECTORS[brain.intention])
            dirty_senses(scene, entity)
            retract_turn(scene, entity)
            retract_intention(scene, entity)
        else:
            retract_turn(scene, entity)
            retract_intention(scene, entity)


def get_brains_with_step_intention(scene):
    return [
        brain
        for brain in scene.cm.get(Brain)
        if brain.intention in STEP_INTENTIONS
    ]


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

STEP_INTENTIONS = list(STEP_VECTORS.keys())


def get_step_target(scene, entity, step_action):
    dx, dy = STEP_VECTORS[step_action]
    entity_coords = scene.cm.get_one(Coordinates, entity)
    target_x = entity_coords.x + dx
    target_y = entity_coords.y + dy
    return target_x, target_y


def can_step(scene, entity, step_action) -> bool:
    """Validate a step action."""
    entity_coords = scene.cm.get_one(Coordinates, entity)
    target_x = entity_coords.x + step_action[0]
    target_y = entity_coords.y + step_action[1]
    blocking_object = get_blocking_object(scene.cm, target_x, target_y)

    entity_material = scene.cm.get_one(Material, entity)
    return not (
        entity_material
        and blocking_object
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
