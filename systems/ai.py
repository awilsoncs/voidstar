import random

from components import Brain
from components.enums import Intention, ControlMode
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


STEPS = [
    Intention.NONE,
    Intention.STEP_NORTH,
    Intention.STEP_SOUTH,
    Intention.STEP_EAST,
    Intention.STEP_WEST
]
