from dice import roll

from components import Attributes, Brain
from components.attack import Attack
from components.enums import Intention
from systems.utilities import retract_intention, retract_turn


def run(scene):
    for brain in [b for b in scene.cm.get(Brain) if b.intention is Intention.MELEE_ATTACK]:
        entity = brain.entity
        target = brain.intention_target
        weapon = scene.cm.get_one(Attack, entity=entity)
        target_attributes = scene.cm.get_one(Attributes, entity=target)
        if weapon:
            target_attributes.hp -= sum(roll(weapon.damage))
        else:
            scene.message("No weapon!")
        retract_intention(scene, entity)
        retract_turn(scene, entity)
