import logging

from components import Attributes
from components.actions.attack_action import AttackAction
from engine.core import log_debug
from systems.utilities import retract_intention, retract_turn


def run(scene):
    for event in scene.cm.get(AttackAction):
        handle_attack_action(scene, event)
    scene.cm.delete_components(AttackAction)


@log_debug(__name__)
def handle_attack_action(scene, event):
    entity = event.entity
    target = event.recipient

    target_attributes = scene.cm.get_one(Attributes, entity=target)
    if target_attributes:
        target_attributes.hp -= event.damage
        target_attributes.hp = max(0, target_attributes.hp)
    retract_turn(scene, entity)

