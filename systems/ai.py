import random

from components import Brain, Coordinates
from components.enums import Intention, ControlMode
from components.target_value import TargetValue
from systems.utilities import set_intention


def run(scene) -> None:
    for brain in scene.cm.get(Brain):
        do_take_turn(scene, brain)


def do_take_turn(scene, brain) -> None:
    if (
        brain
        and brain.control_mode is ControlMode.WANDER
        and brain.take_turn
    ):
        set_intention(scene, brain.entity, 0, random.choice(STEPS))
    elif (
        brain
        and brain.control_mode is ControlMode.MONSTER
        and brain.take_turn
    ):
        take_monster_turn(scene, brain)


def take_monster_turn(scene, brain):
    # find all possible targets
    targets = [t.entity for t in scene.cm.get(TargetValue)]
    if targets:
        # find the closest one
        owner_coord = scene.cm.get_one(Coordinates, entity=brain.entity)
        related_coords = [
            scene.cm.get_one(Coordinates, entity=e)
            for e in targets
        ]
        sorted_coords = sorted(related_coords, key=lambda c: c.distance_from(owner_coord))
        closest_target = sorted_coords[0]
        if owner_coord.distance_from(closest_target) == 1:
            set_intention(scene, brain.entity, closest_target.entity, Intention.MELEE_ATTACK)
        else:
            # get the direction to step towards it
            direction = owner_coord.direction_towards(closest_target)
            # set the intention
            step_intention = VECTOR_STEP_MAP[direction]
            set_intention(scene, brain.entity, 0, step_intention)
    else:
        set_intention(scene, brain.entity, 0, random.choice(STEPS))


VECTOR_STEP_MAP = {
    (0, -1): Intention.STEP_NORTH,
    (-1, -1): Intention.STEP_NORTH,
    (1, -1): Intention.STEP_NORTH,
    (0, 1): Intention.STEP_SOUTH,
    (0, 0): Intention.NONE,
    (1, 1): Intention.STEP_SOUTH,
    (-1, 1): Intention.STEP_SOUTH,
    (1, 0): Intention.STEP_EAST,
    (-1, 0): Intention.STEP_WEST
}


STEPS = [
    Intention.NONE,
    Intention.STEP_NORTH,
    Intention.STEP_SOUTH,
    Intention.STEP_EAST,
    Intention.STEP_WEST
]
