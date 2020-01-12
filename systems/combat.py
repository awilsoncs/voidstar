import random

from components import Attributes, Brain
from components.enums import Intention
from systems.utilities import retract_intention, retract_turn


def run(scene):
    for brain in [b for b in scene.cm.get(Brain) if b.intention is Intention.MELEE_ATTACK]:
        attacker = brain.entity
        defender = brain.intention_target

        attacker_fighter = scene.cm.get_one(Attributes, entity=attacker)
        defender_fighter = scene.cm.get_one(Attributes, entity=defender)
        if not attacker_fighter or not defender_fighter:
            return
        roll = random.randint(1, 20)
        if roll > 10:
            defender_fighter.hp -= random.randint(1, 10)
        retract_intention(scene, brain.entity)
        retract_turn(scene, brain.entity)
