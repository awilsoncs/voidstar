from math import sqrt

from components import Coordinates
from components.abilities.thwack_ability import ThwackAbility
from components.events.chargeabilityevent import ChargeAbilityEvent
from components.actions.attack_action import AttackAction
from components.actions.thwack_action import ThwackAction
from components.states.dizzy_state import DizzyState
from content.attacks import thwack_animation, thwack_dizzy_animation
from systems.utilities import get_enemies_in_range, retract_turn


def apply_dizzy(scene, thwacker):
    scene.cm.add(DizzyState(entity=thwacker, duration=3))


def handle_thwack_action(scene, thwack):
    thwacker = thwack.entity
    thwack_ability = scene.cm.get_one(ThwackAbility, thwacker)

    if thwack_ability.count > 0:
        # determine whether this thwacktivity is legal
        thwack_ability.count -= 1

        # convert the thwack action to an attack action each adjacent enemy
        thwackables = get_enemies_in_range(scene, thwack.entity, max_range=sqrt(2))
        attacks = [
            AttackAction(entity=thwack.entity, recipient=t, damage=1)
            for t in thwackables
        ]

        for attack in attacks:
            scene.cm.add(attack)

        thwacker_coords = scene.cm.get_one(Coordinates, thwacker)

        if thwack_ability.count > 0:
            scene.cm.add(*thwack_animation(thwacker, thwacker_coords.x, thwacker_coords.y)[1])
        else:
            scene.cm.add(*thwack_dizzy_animation(thwacker, thwacker_coords.x, thwacker_coords.y)[1])
    if thwack_ability.count <= 0:
        apply_dizzy(scene, thwacker)
    
    retract_turn(scene, thwacker)


def handle_thwack_ability(scene, thwack_ability):
    thwack_actions = scene.cm.get_all(ThwackAction, entity=thwack_ability.entity)

    if not thwack_actions and scene.cm.get_one(ChargeAbilityEvent, entity=thwack_ability.entity):
        thwack_ability.count = min(thwack_ability.count + 1, thwack_ability.max)

    for thwack in thwack_actions:
        handle_thwack_action(scene, thwack)


def run(scene):
    """A thwack action applies the entity's attack to each adjacent enemy."""
    thwack_abilities = scene.cm.get(ThwackAbility)
    for thwack_ability in thwack_abilities:
        handle_thwack_ability(scene, thwack_ability)
    scene.cm.delete_components(ThwackAction)
