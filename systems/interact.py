from components import Entity, Attributes, Brain
from components.coordinates import Coordinates
from components.enums import Intention
from systems.utilities import set_intention, retract_intention

"""
Object Interaction System

Manages the ways that entities interact with the world.
"""


def run(scene):
    for brain in [b for b in scene.cm.get(Brain) if b.intention is Intention.INTERACT_NEARBY]:
        entity = brain.entity
        entity_coords = scene.cm.get_one(Coordinates, entity=entity)
        x = entity_coords.x
        y = entity_coords.y
        nearby_objects = get_nearby_objects(scene, x, y, ignore=entity)

        if len(nearby_objects) == 0:
            scene.message("There's nothing to interact with.")
            retract_intention(scene, entity)
        elif len(nearby_objects) == 1:
            interactee = nearby_objects[0].entity
            interact_with(scene, entity, interactee)


def get_nearby_objects(scene, x, y, ignore=None):
    return [
        c
        for c in scene.cm.get(Coordinates)
        if (
            x - 1 <= c.x <= x + 1
            and y - 1 <= c.y <= y + 1
            and c.entity != ignore
            and not scene.cm.get_one(Entity, c.entity).static
        )
    ]


def interact_with(scene, entity: int, interactee: int):
    interaction = determine_interaction(scene, interactee)
    if interaction == 'use':
        set_intention(scene, entity, interactee, Intention.USE_ITEM)
    elif interaction == 'get':
        set_intention(scene, entity, interactee, Intention.GET_NEARBY)
    elif interaction == 'fight':
        set_intention(scene, entity, interactee, Intention.MELEE_ATTACK)
    else:
        scene.message("You can't interact with anything here.")
        retract_intention(scene, entity)


def determine_interaction(scene, interactee: int):
    health = scene.cm.get_one(Attributes, entity=interactee)
    if health:
        return 'fight'
