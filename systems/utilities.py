from components import Coordinates, Brain
from components.enums import Intention
from components.material import Material
from engine.component_manager import ComponentManager


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
