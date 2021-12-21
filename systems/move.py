from functools import reduce
from typing import Tuple

from components import Senses
from components.actions.attack_action import AttackAction
from components.actors.actor import Actor
from components.attack import Attack
from components.coordinates import Coordinates
from components.enums import Intention
from components.faction import Faction
from components.material import Material
from components.move import Move
from components.move_listeners.move_listener import MoveListener
from components.move_costs.hindrances import Hindered, Hindrance
from content.attacks import stab
from systems.utilities import get_blocking_object, retract_intention


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
        if obj_faction and obj_faction.faction is not entity_faction.faction:
            return obj
    return None


def run(scene):
    for actor in get_actors_with_step_intention(scene):
        entity = actor.entity
        actor = scene.cm.get_one(Actor, entity=entity)

        # is there a hostile in that direction? if so, bump attack
        # is there a non-hostile blocking entity in that direction? if so, too bad
        # otherwise, move them
        step_direction = STEP_VECTORS[actor.intention]
        if can_step(scene, entity, step_direction):
            # do move
            move(scene, entity, step_direction)
            dirty_senses(scene, entity)
            move_component = scene.cm.get_one(Move, entity=entity)

            # account for the mob's state
            move_factor = reduce(
                lambda x, y: x*y,
                [mc.factor for mc in scene.cm.get_all(Hindered, entity=entity)],
                1.0
            )
            final_move_cost = int(move_component.energy_cost * move_factor)
            actor.pass_turn(final_move_cost)
            retract_intention(scene, entity)
        elif get_hostile(scene, entity, step_direction):

            entity_attack = scene.cm.get_one(Attack, entity=entity)
            if entity_attack:
                hostile = get_hostile(scene, entity, step_direction)
                scene.cm.add(AttackAction(entity=entity, recipient=hostile, damage=1))
                coords = scene.cm.get_one(Coordinates, entity)
                scene.cm.add(
                    *stab(
                        entity,
                        coords.x + step_direction[0],
                        coords.y + step_direction[1]
                    )[1]
                )
            else:
                actor.pass_turn()
            retract_intention(scene, entity)
        else:
            actor.pass_turn()
            retract_intention(scene, entity)


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
    move_costs = scene.cm.get_all(Hindered, entity=entity)
    if len(move_costs) > 1:
        raise NotImplementedError("Can't handle more than one move cost yet.")
    if move_costs:
        move_cost = move_costs.pop()
        scene.cm.delete_component(move_cost)

    coords = scene.cm.get_one(Coordinates, entity=entity)
    if coords:
        move_coords(coords, vector)
        move_listeners = scene.cm.get(MoveListener)
        for move_listener in move_listeners:
            move_listener.on_move(scene)

        hindering_entities = scene.cm.get(
            Coordinates,
            query=lambda c: c.x == coords.x and c.y == coords.y and scene.cm.get_one(Hindrance, entity=c.entity),
            project=lambda c: c.entity
        )

        if hindering_entities:
            hindering_entity = hindering_entities.pop()
            hindrance_component = scene.cm.get_one(Hindrance, entity=hindering_entity)
            scene.cm.add(Hindered(entity=entity, factor=hindrance_component.factor))


def move_coords(coords: Coordinates, vector: Tuple[int, int]):
    coords.x += vector[0]
    coords.y += vector[1]
