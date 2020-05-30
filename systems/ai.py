import logging
import random

from components import Brain, Coordinates
from components.enums import Intention, ControlMode
from components.actions.attack_action import AttackAction
from components.events.turn_event import TurnEvent
from components.target_value import TargetValue
from engine.core import log_debug
from systems.utilities import set_intention


def run(scene) -> None:
    for brain in get_brains(scene, ControlMode.MONSTER):
        handle_monster(scene, brain)
    for brain in get_brains(scene, ControlMode.WANDER):
        handle_wander(scene, brain)


def get_brains(scene, control_mode):
    return [
        brain
        for brain in scene.cm.get(Brain)
        for turn in [scene.cm.get_one(TurnEvent, entity=brain.entity)]
        if turn and brain.control_mode is control_mode
    ]


@log_debug(__name__)
def handle_wander(scene, brain):
    set_intention(scene, brain.entity, 0, random.choice(STEPS))


@log_debug(__name__)
def handle_monster(scene, brain):
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

        # < 2 allows diagonal attacks
        if owner_coord.distance_from(closest_target) < 2:
            scene.cm.add(
                AttackAction(
                    entity=brain.entity,
                    recipient=closest_target.entity,
                    damage=1
                )
            )
        else:
            # get the direction to step towards it
            direction = owner_coord.direction_towards(closest_target)
            # set the intention
            step_intention = VECTOR_STEP_MAP[direction]
            set_intention(scene, brain.entity, 0, step_intention)
    else:
        set_intention(scene, brain.entity, 0, random.choice(STEPS))


# TODO info duplicated between here and move
VECTOR_STEP_MAP = {
    (0, -1): Intention.STEP_NORTH,
    (-1, -1): Intention.STEP_NORTH,
    (1, -1): Intention.STEP_NORTH,
    (0, 1): Intention.STEP_SOUTH,
    (0, 0): Intention.NONE,
    (1, 1): Intention.STEP_SOUTH,
    (-1, 1): Intention.STEP_SOUTH,
    (1, 0): Intention.STEP_EAST,
    (-1, 0): Intention.STEP_WEST,
    (1, -1): Intention.STEP_NORTH_EAST,
    (-1, -1): Intention.STEP_SOUTH_WEST,
    (1, 1): Intention.STEP_SOUTH_EAST,
    (-1, 1): Intention.STEP_SOUTH_WEST
}


STEPS = [
    Intention.NONE,
    Intention.STEP_NORTH,
    Intention.STEP_SOUTH,
    Intention.STEP_EAST,
    Intention.STEP_WEST
]
