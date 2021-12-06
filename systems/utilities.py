from components import Coordinates
from components.actors.actor import Actor
from components.enums import Intention
from components.events.turn_event import TurnEvent
from components.faction import Faction
from components.material import Material
from engine.component_manager import ComponentManager
from engine.core import log_debug


def get_blocking_object(cm: ComponentManager, x: int, y: int) -> int:
    materials_at_coords = filter(
        lambda material: material and material.blocks,
        iter(
            cm.get_one(Material, coord.entity)
            for coord in cm.get(Coordinates)
            if (coord.x == x and coord.y == y)
        )
    )
    blocking_material = next(materials_at_coords, None)
    return blocking_material.entity if blocking_material else None


@log_debug(__name__)
def set_intention(scene, entity, target, intention):
    actor = scene.cm.get_one(Actor, entity=entity)
    if actor:
        actor.intention = intention
        actor.intention_target = target


def retract_intention(scene, entity):
    set_intention(scene, entity, None, Intention.NONE)


@log_debug(__name__)
def retract_turn(scene, entity: int):
    turn = scene.cm.get_one(TurnEvent, entity=entity)
    if turn:
        scene.cm.delete_component(turn)


def get_actors_with_intention(scene, intention):
    for actor in scene.cm.get(Actor):
        if actor.intention is intention:
            yield actor


def get_enemies(scene, entity):
    entity_faction = scene.cm.get_one(Faction, entity=entity)
    if not entity_faction:
        # entities without a faction cannot have enemies
        return []
    return [f.entity for f in scene.cm.get(Faction) if f.faction is not entity_faction.faction]


def get_enemies_in_range(scene, entity, min_range=0, max_range=1000):
    coords = scene.cm.get_one(Coordinates, entity)

    # get coordinates for each enemy
    enemies = get_enemies(scene, entity)
    enemy_coords = [scene.cm.get_one(Coordinates, entity=e) for e in enemies]

    # return filtered coordinates by distance < range
    return [
        enemy_coord.entity
        for enemy_coord in enemy_coords
        if min_range <= enemy_coord.distance_from(coords) <= max_range
    ]
