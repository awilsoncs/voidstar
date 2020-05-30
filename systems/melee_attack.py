from components import Attributes
from components.actions.attack_action import AttackAction
from systems.utilities import retract_intention, retract_turn


def run(scene):
    for event in scene.cm.get(AttackAction):
        entity = event.entity
        target = event.recipient

        target_attributes = scene.cm.get_one(Attributes, entity=target)
        if target_attributes:
            target_attributes.hp -= event.damage
            target_attributes.hp = max(0, target_attributes.hp)
        retract_intention(scene, entity)
        retract_turn(scene, entity)

    scene.cm.delete_components(AttackAction)
