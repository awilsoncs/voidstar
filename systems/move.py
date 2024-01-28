import logging
from typing import Tuple

import settings
from components import Senses
from engine.components.actor import Actor
from components.attacks.attack import Attack
from components.brains.brain import Brain
from components.coordinates import Coordinates
from components.enums import Intention
from components.faction import Faction
from components.material import Material
from components.movement.move import Move
from components.states.move_cost_affectors import Hindered, DifficultTerrain, EasyTerrain, Haste
from components.events.dally_event import DallyEvent
from components.events.step_event import StepEvent
from engine import palettes
from systems.utilities import get_blocking_object


def get_hostile(scene, entity, step_direction):
    entity_faction = scene.cm.get_one(Faction, entity)
    if not entity_faction:
        return None
    coords = scene.cm.get_one(Coordinates, entity=entity)
    x = coords.x + step_direction[0]
    y = coords.y + step_direction[1]
    obj = get_blocking_object(scene.cm, x, y)
    if obj:
        obj_faction = scene.cm.get_one(Faction, obj)
        if obj_faction and obj_faction.faction != entity_faction.faction:
            return obj
    return None


def run(scene):
    for actor in get_actors_with_step_intention(scene):
        logging.debug(f"Move System: moving {actor}")
        entity = actor.entity
        actor = scene.cm.get_one(Brain, entity=entity)

        # is there a hostile in that direction? if so, bump attack
        # is there a non-hostile blocking entity in that direction? if so, too bad
        # otherwise, move them
        if actor.intention not in STEP_VECTORS:
            print(actor)
        if actor.intention == Intention.DALLY:
            scene.cm.add(DallyEvent(entity=entity))
            actor.intention = Intention.NONE
            actor.pass_turn()
            return

        step_direction = STEP_VECTORS[actor.intention]
        if can_step(scene, entity, step_direction):
            # do move
            move(scene, entity, step_direction)
            dirty_senses(scene, entity)
            move_component = scene.cm.get_one(Move, entity=entity)
            if scene.cm.get_one(Haste, entity=entity):
                energy = move_component.energy_cost // 2
            else:
                energy = move_component.energy_cost
            actor.pass_turn(energy)
            actor.intention = Intention.NONE
        elif get_hostile(scene, entity, step_direction):
            entity_attack: Attack = scene.cm.get_one(Attack, entity=entity)
            if entity_attack:
                hostile: int = get_hostile(scene, entity, step_direction)
                entity_attack.apply_attack(scene, hostile)
            actor.pass_turn()
            actor.intention = Intention.NONE
        else:
            actor.pass_turn()
            actor.intention = Intention.NONE


def get_actors_with_step_intention(scene):
    return [
        actor
        for actor in scene.cm.get(Actor)
        if actor.intention in STEP_INTENTIONS
    ]


STEP_VECTORS = {
    Intention.STEP_NORTH: (0, -1),
    Intention.STEP_SOUTH: (0, 1),
    Intention.STEP_EAST: (1, 0),
    Intention.STEP_WEST: (-1, 0),
    Intention.STEP_NORTH_EAST: (1, -1),
    Intention.STEP_NORTH_WEST: (-1, -1),
    Intention.STEP_SOUTH_EAST: (1, 1),
    Intention.STEP_SOUTH_WEST: (-1, 1),
    Intention.DALLY: (0, 0)
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
    move_component = scene.cm.get_one(Move, entity=entity)
    if not move_component:
        return False

    entity_coords = scene.cm.get_one(Coordinates, entity)
    target_x = entity_coords.x + step_action[0]
    target_y = entity_coords.y + step_action[1]

    if not in_bounds((target_x, target_y)):
        if entity == scene.player:
            scene.message("You shouldn't leave the village.", color=palettes.WHITE)
        return False

    blocking_object = get_blocking_object(scene.cm, target_x, target_y)

    entity_material = scene.cm.get_one(Material, entity)
    return not (entity_material and blocking_object)


def in_bounds(point):
    return (
        point[0] in range(settings.MAP_FRAME_WIDTH)
        and point[1] in range(settings.MAP_FRAME_HEIGHT)
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
    swamped = scene.cm.get_one(Hindered, entity=entity)

    if swamped:
        scene.cm.delete_component(swamped)
        return

    coords = scene.cm.get_one(Coordinates, entity=entity)
    if coords:
        move_coords(coords, vector)
        _apply_post_move_factors(coords, entity, scene)
    scene.cm.add(StepEvent(entity=entity, new_location=(coords.x, coords.y)))


def _apply_post_move_factors(coords, entity, scene):
    difficult_terrain: bool = any(
        scene.cm.get_one(DifficultTerrain, entity=coord.entity) is not None
        for coord in scene.cm.get(Coordinates)
        if (coord.x == coords.x and coord.y == coords.y)
    )

    if entity == scene.player:
        # Only the player should be hasty
        easy_terrain: bool = any(
            scene.cm.get_one(EasyTerrain, entity=coord.entity) is not None
            for coord in scene.cm.get(Coordinates)
            if (coord.x == coords.x and coord.y == coords.y)
        )
    else:
        easy_terrain = False

    haste = scene.cm.get_one(Haste, entity=entity)
    if not easy_terrain and haste:
        scene.cm.delete_component(haste)

    if easy_terrain and not haste:
        scene.cm.add(Haste(entity=entity))
    elif difficult_terrain and not easy_terrain:
        if entity == scene.player:
            scene.message("You stumbled over the terrain.")
        scene.cm.add(Hindered(entity=entity))


def move_coords(coords: Coordinates, vector: Tuple[int, int]):
    coords.x += vector[0]
    coords.y += vector[1]
