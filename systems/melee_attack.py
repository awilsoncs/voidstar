from typing import List

from components import Attributes, Coordinates
from components.actions.attack_action import AttackAction
from components.actors.actor import Actor
from components.attack_effect.attack_effect import AttackEffect
from components.cry_for_help import CryForHelp
from components.house_structure import HouseStructure
from components.owner import Owner
from content.states import help_animation
from engine.core import log_debug


def run(scene):
    for event in scene.cm.get(AttackAction):
        handle_attack_action(scene, event)
    scene.cm.delete_components(AttackAction)


@log_debug(__name__)
def handle_attack_action(scene, event):
    entity: int = event.entity
    target: int = event.recipient

    owner = scene.cm.get_one(Owner, entity=target)
    if owner:
        structures = scene.cm.get(HouseStructure, query=lambda hs: hs.house_id == owner.owner)
        house_structure = structures[0] if structures else None
    else:
        house_structure = None

    damage = event.damage
    if house_structure:
        _handle_house_damage(scene, house_structure, damage)
    else:
        _handle_entity_damage(scene, target, damage)
        attack_effects: List[AttackEffect] = scene.cm.get_all(AttackEffect, entity=entity)
        for attack_effect in attack_effects:
            attack_effect.apply(scene, entity, target)

    cry_for_help = scene.cm.get_one(CryForHelp, entity=target)
    if cry_for_help:
        coords = scene.cm.get_one(Coordinates, entity=target)
        help_anim = help_animation(coords.x, coords.y)
        scene.cm.add(*help_anim[1])

    actor = scene.cm.get_one(Actor, entity=entity)
    actor.pass_turn()


def _handle_house_damage(scene, house_structure, damage):
    for entity in house_structure.get_all():
        _handle_entity_damage(scene, entity, damage)


def _handle_entity_damage(scene, target, damage):
    target_attributes = scene.cm.get_one(Attributes, entity=target)
    if target_attributes:
        target_attributes.hp -= damage
        target_attributes.hp = max(0, target_attributes.hp)
