from components import Attributes
from components.actions.attack_action import AttackAction
from components.actors.actor import Actor
from engine.core import log_debug


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
    actor = scene.cm.get_one(Actor, entity=entity)
    actor.pass_turn()

