from components.enums import Intention
from systems.utilities import get_brains_with_intention, retract_turn, retract_intention


def run(scene):
    for brain in get_brains_with_intention(scene, Intention.DALLY):
        retract_turn(scene, brain.entity)
        retract_intention(scene, brain.entity)
