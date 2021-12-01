from components import Attributes, Coordinates
from components.actions.attack_action import AttackAction
from components.actors.actor import Actor
from components.cry_for_help import CryForHelp
from content.states import help_animation
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

    cry_for_help = scene.cm.get_one(CryForHelp, entity=target)
    if cry_for_help:
        coords = scene.cm.get_one(Coordinates, entity=target)
        help_anim = help_animation(coords.x, coords.y)
        scene.cm.add(*help_anim[1])

    actor = scene.cm.get_one(Actor, entity=entity)
    actor.pass_turn()

