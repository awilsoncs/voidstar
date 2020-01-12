from components import Coordinates, Brain
from components.enums import Intention
from engine.component_manager import ComponentManager


def get_blocking_object(cm: ComponentManager, x: int, y: int) -> Coordinates:
    coordinates = cm.get(Coordinates)
    blocking_objects = (
        c for c in coordinates if (
            c.x == x and
            c.y == y and
            c.blocks
        )
    )
    return next(blocking_objects, None)


def set_intention(scene, entity, target, intention):
    brain = scene.cm.get_one(Brain, entity=entity)
    if brain:
        brain.intention = intention
        brain.intention_target = target


def retract_intention(scene, entity):
    set_intention(scene, entity, None, Intention.NONE)


def retract_turn(scene, entity: int):
    brain = scene.cm.get_one(Brain, entity=entity)
    if brain:
        brain.take_turn = False


def get_brains_with_intention(scene, intention):
    for brain in scene.cm.get(Brain):
        if brain.intention is intention:
            yield brain
